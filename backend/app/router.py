"""
Router / Orchestrator for Tamwil AI.
Detects user intent via keyword matching and routes to the correct business module.
Fallback: RAG Q&A for general questions.
"""

import re

from backend.app.modules.scoring import score_fundability
from backend.app.modules.diagnostic import diagnose_kpis
from backend.app.modules.matching_investors import match_investors
from backend.app.modules.matching_grants import match_grants
from backend.app.modules.rag_qa import answer_question
from backend.app.utils.data_loader import load_metrics


# --- Intent Detection Keywords ---

INTENT_KEYWORDS = {
    "scoring": [
        "score", "scoring", "fundability", "noter", "note",
        "prêt à lever", "pret a lever", "évaluer ma startup",
        "score de levée", "fundable",
    ],
    "diagnostic": [
        "diagnostic", "diagnostiquer", "analyser mes kpi",
        "santé financière", "sante financiere", "comment va ma startup",
        "analyse financière", "bilan financier",
    ],
    "metrics": [
        "expliquer les métriques", "expliquer les metriques",
        "explique les métriques", "explique les metriques",
        "c'est quoi les métriques", "c'est quoi les metriques",
        "c'est quoi un kpi", "c'est quoi les kpi",
        "définition des métriques", "definition des metriques",
        "quelles métriques", "quelles metriques",
        "explique moi ces métriques", "explique moi ces metriques",
        "c'est quoi mrr", "c'est quoi le mrr",
        "c'est quoi cac", "c'est quoi le cac",
        "c'est quoi churn", "c'est quoi le churn",
        "c'est quoi ltv", "c'est quoi le ltv",
        "c'est quoi burn rate", "c'est quoi le burn rate",
        "ces métriques", "ces metriques",
    ],
    "investors": [
        "investisseur", "investor", "vc", "venture capital",
        "business angel", "ba", "fonds d'investissement",
        "qui peut investir", "trouver un investisseur",
        "lever des fonds", "levée de fonds",
    ],
    "grants": [
        "subvention", "aide", "programme", "financement public",
        "bourse", "innov start", "forsa", "tamwilcom",
        "financement non dilutif", "grant",
    ],
}

# --- Metric Value Extraction ---

METRIC_PATTERNS = {
    "MRR": r"(?:mrr|revenu mensuel)[:\s]*(\d[\d\s]*)",
    "ARR": r"(?:arr|revenu annuel)[:\s]*(\d[\d\s]*)",
    "BURN_RATE": r"(?:burn\s*rate|burn)[:\s]*(\d[\d\s]*)",
    "CHURN_RATE": r"(?:churn|désabonnement|taux de churn)[:\s]*(\d[\d\s.,]*)\s*%?",
    "CAC": r"(?:cac|coût d'acquisition|cout d'acquisition)[:\s]*(\d[\d\s]*)",
    "LTV": r"(?:ltv|lifetime value|valeur vie)[:\s]*(\d[\d\s]*)",
    "LTV_CAC": r"(?:ltv/cac|ratio ltv)[:\s]*(\d[\d\s.,]*)",
    "RUNWAY": r"(?:runway)[:\s]*(\d[\d\s.,]*)",
    "NPS": r"(?:nps)[:\s]*(\d[\d\s.,]*)",
    "GROSS_MARGIN": r"(?:marge brute|gross margin)[:\s]*(\d[\d\s.,]*)\s*%?",
    "MRR_GROWTH": r"(?:croissance|growth)[:\s]*(\d[\d\s.,]*)\s*%?",
    "TAKE_RATE": r"(?:take\s*rate|taux de commission)[:\s]*(\d[\d\s.,]*)\s*%?",
    "TPV": r"(?:tpv|total payment volume|volume de paiement)[:\s]*(\d[\d\s]*)",
    "DAU_MAU": r"(?:dau/mau|dau mau|stickiness|adh[ée]sivit[ée])[:\s]*(\d[\d\s.,]*)\s*%?",
}

STAGE_PATTERNS = [
    (r"\bpre[- ]?seed\b", "pre-seed"),
    (r"\bseed\b", "seed"),
    (r"\bs[ée]rie\s*a\b", "série a"),
    (r"\bseries?\s*a\b", "série a"),
    (r"\bs[ée]rie\s*b\b", "série b"),
    (r"\bseries?\s*b\b", "série b"),
    (r"\bgrowth\b", "growth"),
]

SECTOR_KEYWORDS = [
    "fintech", "saas", "edtech", "healthtech", "agritech",
    "e-commerce", "marketplace", "logistique", "deeptech",
    "foodtech", "proptech", "insurtech", "cleantech",
    "technologie", "mobile", "tic",
]

COUNTRY_KEYWORDS = [
    "maroc", "france", "tunisie", "sénégal", "côte d'ivoire",
    "algérie", "cameroun", "nigeria", "afrique",
]


def _detect_intent(message: str, history: list[dict] = None) -> str:
    """Detect user intent from message keywords. Returns intent name."""
    msg_lower = message.lower()

    # Check each intent's keywords
    scores = {}
    for intent, keywords in INTENT_KEYWORDS.items():
        count = sum(1 for kw in keywords if kw in msg_lower)
        if count > 0:
            scores[intent] = count

    if scores:
        return max(scores, key=scores.get)

    # Check if message contains metric values → scoring intent
    for pattern in METRIC_PATTERNS.values():
        if re.search(pattern, msg_lower, re.IGNORECASE):
            return "scoring"

    # Check if user is asking about metrics in context of a previous scoring/diagnostic request
    # Only trigger if the current message also mentions a metric term (not just "expliquer" + history)
    if history:
        metric_terms = ["métrique", "metrique", "kpi", "mrr", "cac", "churn", "ltv", "burn rate", "fundability"]
        explanation_words = ["explique", "expliquer", "c'est quoi", "définition", "definition", "signifie", "veut dire", "comprends pas"]
        has_explanation_request = any(w in msg_lower for w in explanation_words)
        has_metric_in_message = any(w in msg_lower for w in metric_terms)
        if has_explanation_request and has_metric_in_message:
            return "metrics"

    return "qa"


def detect_intent(message: str, history: list[dict] = None) -> str:
    """Public API for intent detection."""
    return _detect_intent(message, history)


# Key metrics to explain (most common for scoring/diagnostic)
CORE_METRICS = ["MRR", "CHURN_RATE", "CAC", "LTV", "BURN_RATE", "LTV_CAC", "RUNWAY"]


def _explain_metrics(message: str) -> dict:
    """Return definitions of key startup metrics from metrics_reference.json."""
    metrics_ref = {m["id"]: m for m in load_metrics()}
    msg_lower = message.lower()

    # Check if user asks about a specific metric
    specific_ids = []
    keyword_to_id = {
        "mrr": "MRR", "revenu mensuel": "MRR",
        "arr": "ARR", "revenu annuel": "ARR",
        "churn": "CHURN_RATE", "désabonnement": "CHURN_RATE", "desabonnement": "CHURN_RATE",
        "cac": "CAC", "coût d'acquisition": "CAC", "cout d'acquisition": "CAC",
        "ltv": "LTV", "lifetime value": "LTV", "valeur vie": "LTV",
        "ltv/cac": "LTV_CAC", "ratio ltv": "LTV_CAC",
        "burn rate": "BURN_RATE", "burn": "BURN_RATE", "trésorerie": "BURN_RATE",
        "runway": "RUNWAY",
        "nps": "NPS",
        "marge brute": "GROSS_MARGIN", "gross margin": "GROSS_MARGIN",
        "croissance": "MRR_GROWTH", "growth": "MRR_GROWTH",
    }
    for keyword, metric_id in keyword_to_id.items():
        if keyword in msg_lower and metric_id not in specific_ids:
            specific_ids.append(metric_id)

    # If no specific metric found, explain the core ones
    metric_ids = specific_ids if specific_ids else CORE_METRICS

    explanations = []
    for mid in metric_ids:
        ref = metrics_ref.get(mid)
        if not ref:
            continue
        explanations.append({
            "id": ref["id"],
            "name_fr": ref.get("name_fr", ref["name"]),
            "definition": ref.get("definition", ""),
            "formula": ref.get("formula", ""),
        })

    return {"metrics": explanations}


def _extract_metrics(message: str) -> dict:
    """Extract metric values from a natural language message."""
    msg_lower = message.lower()
    metrics = {}

    for metric_id, pattern in METRIC_PATTERNS.items():
        match = re.search(pattern, msg_lower, re.IGNORECASE)
        if match:
            raw = match.group(1).replace(" ", "").replace(",", ".")
            try:
                metrics[metric_id] = float(raw)
            except ValueError:
                pass

    return metrics


def _extract_stage(message: str) -> str:
    """Extract startup stage from message."""
    msg_lower = message.lower()
    for pattern, stage in STAGE_PATTERNS:
        if re.search(pattern, msg_lower):
            return stage
    return "seed"  # default


def _extract_sector(message: str) -> str:
    """Extract sector from message."""
    msg_lower = message.lower()
    for sector in SECTOR_KEYWORDS:
        if sector in msg_lower:
            return sector
    return ""


def _extract_country(message: str) -> str:
    """Extract country from message."""
    msg_lower = message.lower()
    for country in COUNTRY_KEYWORDS:
        if country in msg_lower:
            return country.capitalize()
    return "Maroc"  # default


def _extract_age(message: str) -> int | None:
    """Extract company age from message."""
    match = re.search(r"(\d+)\s*ans?", message.lower())
    return int(match.group(1)) if match else None


def _extract_amount(message: str) -> int | None:
    """Extract funding amount from message."""
    # Match patterns like "5M", "5 millions", "500K", "500 000"
    msg_lower = message.lower()

    match = re.search(r"(\d+)\s*m(?:illions?)?(?:\s*(?:mad|dh|€|eur|usd|\$))?", msg_lower)
    if match:
        return int(match.group(1)) * 1_000_000

    match = re.search(r"(\d+)\s*k", msg_lower)
    if match:
        return int(match.group(1)) * 1_000

    match = re.search(r"(\d[\d\s]{2,})\s*(?:mad|dh|€|eur|usd|\$)", msg_lower)
    if match:
        return int(match.group(1).replace(" ", ""))

    return None


def route(user_message: str, startup_profile: dict = None, history: list[dict] = None) -> dict:
    """Route a user message to the correct business module.

    Args:
        user_message: The user's natural language message.
        startup_profile: Optional pre-filled startup profile from sidebar form.
        history: Conversation history as list of {"role": ..., "content": ...} dicts.

    Returns:
        Dict with intent, module used, and result.
    """
    profile = startup_profile or {}
    intent = _detect_intent(user_message, history=history)

    if intent == "metrics":
        result = _explain_metrics(user_message)
        return {"intent": "metrics", "result": result}

    elif intent == "scoring":
        metrics = _extract_metrics(user_message)
        # Merge with profile if available
        metrics.update({k: v for k, v in profile.get("metrics", {}).items() if k not in metrics})
        stage = profile.get("stage") or _extract_stage(user_message)

        if not metrics:
            return {
                "intent": "scoring",
                "error": (
                    "Pour calculer votre score de fundability, j'ai besoin de vos KPIs. "
                    "Voici les métriques que vous pouvez fournir :\n\n"
                    "- **MRR** (Revenu Mensuel Récurrent) : vos revenus d'abonnements par mois (ex: MRR: 8000)\n"
                    "- **Churn** (Taux de Désabonnement) : % de clients perdus par mois (ex: churn: 5%)\n"
                    "- **CAC** (Coût d'Acquisition Client) : coût moyen pour acquérir un client (ex: CAC: 200)\n"
                    "- **LTV** (Valeur Vie Client) : revenu total généré par un client (ex: LTV: 2000)\n"
                    "- **Burn Rate** : trésorerie consommée par mois (ex: burn rate: 15000)\n\n"
                    "Exemple : *MRR: 8000, churn: 5%, CAC: 200, stade seed*"
                ),
            }

        result = score_fundability(metrics, stage)
        return {"intent": "scoring", "result": result}

    elif intent == "diagnostic":
        metrics = _extract_metrics(user_message)
        metrics.update({k: v for k, v in profile.get("metrics", {}).items() if k not in metrics})
        stage = profile.get("stage") or _extract_stage(user_message)

        if not metrics:
            return {
                "intent": "diagnostic",
                "error": (
                    "Pour réaliser votre diagnostic financier, j'ai besoin de vos KPIs. "
                    "Voici les métriques que vous pouvez fournir :\n\n"
                    "- **CAC** (Coût d'Acquisition Client) : coût moyen pour acquérir un client (ex: CAC: 200)\n"
                    "- **LTV** (Valeur Vie Client) : revenu total généré par un client (ex: LTV: 400)\n"
                    "- **Churn** (Taux de Désabonnement) : % de clients perdus par mois (ex: churn: 8%)\n"
                    "- **MRR** (Revenu Mensuel Récurrent) : vos revenus d'abonnements par mois\n"
                    "- **Burn Rate** : trésorerie consommée par mois\n\n"
                    "Exemple : *CAC: 200, LTV: 400, churn: 8%*"
                ),
            }

        result = diagnose_kpis(metrics, stage)
        return {"intent": "diagnostic", "result": result}

    elif intent == "investors":
        sector = profile.get("sector") or _extract_sector(user_message)
        stage = profile.get("stage") or _extract_stage(user_message)
        geography = profile.get("geography") or _extract_country(user_message)
        amount = _extract_amount(user_message) or profile.get("funding_amount")

        if not sector:
            return {
                "intent": "investors",
                "error": "Veuillez préciser votre secteur d'activité (ex: fintech, SaaS, edtech).",
            }

        result = match_investors(sector, stage, geography, funding_amount=amount)
        return {"intent": "investors", "result": result}

    elif intent == "grants":
        sector = profile.get("sector") or _extract_sector(user_message)
        stage = profile.get("stage") or _extract_stage(user_message)
        country = profile.get("country") or _extract_country(user_message)
        age = _extract_age(user_message) or profile.get("company_age")

        result = match_grants(sector or "tous", stage, country, company_age=age)
        return {"intent": "grants", "result": result}

    else:
        # Fallback: RAG Q&A (with conversation history for context)
        result = answer_question(user_message, history=history)
        return {"intent": "qa", "result": result}


# --- Standalone test ---
if __name__ == "__main__":
    import sys
    import json

    test_queries = [
        "Quel est mon score de fundability ? MRR: 8000, burn rate: 15000, churn: 5%, stade seed",
        "Fais un diagnostic de mes KPIs : CAC: 200, LTV: 400, churn: 8%",
        "Quels investisseurs pour une startup fintech seed au Maroc ?",
        "Quelles subventions sont disponibles pour une startup edtech de 2 ans au Maroc ?",
        "Comment valoriser ma startup en pré-seed ?",
    ]

    # Use CLI arg or run all test queries
    if len(sys.argv) > 1:
        test_queries = [" ".join(sys.argv[1:])]

    print("=" * 60)
    print("  Tamwil AI — Router Test")
    print("=" * 60)

    for query in test_queries:
        print(f"\n  Query: {query}")
        print(f"  {'─' * 50}")

        result = route(query)
        intent = result["intent"]
        print(f"  Intent: {intent}")

        if "error" in result:
            print(f"  Error: {result['error']}")
        elif intent == "scoring":
            r = result["result"]
            print(f"  Score: {r['score']}/100")
            print(f"  Forces: {r['strengths']}")
            print(f"  Faiblesses: {r['weaknesses']}")
        elif intent == "diagnostic":
            r = result["result"]
            print(f"  Summary: {r['summary']}")
            for a in r["analyses"]:
                print(f"    - {a['name_fr']}: {a['value']} → {a['level']}")
        elif intent == "investors":
            r = result["result"]
            print(f"  Found: {r['total_found']} investors")
            for m in r["matches"][:3]:
                print(f"    - {m['name']} ({m['type']}) — score {m['match_score']}")
        elif intent == "grants":
            r = result["result"]
            print(f"  Found: {r['total_found']} grants")
            for m in r["matches"][:3]:
                print(f"    - {m['name']} ({m['organization']})")
        elif intent == "qa":
            r = result["result"]
            print(f"  Mode: {r['mode']}")
            print(f"  Answer: {r['answer'][:200]}...")

        print()
