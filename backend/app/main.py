"""
FastAPI server for Tamwil AI.
Exposes the router/orchestrator as an HTTP API for the Next.js frontend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.app.router import route


# --- Pydantic models matching the frontend TypeScript interfaces ---

class StartupProfile(BaseModel):
    secteur: str = ""
    stade: str = ""
    pays: str = ""
    mrr: float | str = ""
    burnRate: float | str = ""
    churn: float | str = ""
    cac: float | str = ""
    ltv: float | str = ""


class HistoryMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    profile: StartupProfile = StartupProfile()
    history: list[HistoryMessage] = []


class ChatResponse(BaseModel):
    reply: str


# --- App ---

app = FastAPI(title="Tamwil AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Profile mapping: frontend (FR/camelCase) → router (EN/snake_case) ---

STAGE_MAP = {
    "pre-seed": "pre-seed",
    "seed": "seed",
    "series-a": "série a",
    "serie-a": "série a",
    "": "seed",
}

COUNTRY_MAP = {
    "maroc": "Maroc",
    "france": "France",
    "tunisie": "Tunisie",
    "senegal": "Sénégal",
    "cote-divoire": "Côte d'Ivoire",
    "": "Maroc",
}


def _build_router_profile(profile: StartupProfile) -> dict:
    """Convert frontend profile to the dict format expected by router.route()."""
    metrics = {}
    if profile.mrr != "":
        metrics["MRR"] = float(profile.mrr)
    if profile.burnRate != "":
        metrics["BURN_RATE"] = float(profile.burnRate)
    if profile.churn != "":
        metrics["CHURN_RATE"] = float(profile.churn)
    if profile.cac != "":
        metrics["CAC"] = float(profile.cac)
    if profile.ltv != "":
        metrics["LTV"] = float(profile.ltv)

    return {
        "sector": profile.secteur,
        "stage": STAGE_MAP.get(profile.stade, profile.stade),
        "geography": COUNTRY_MAP.get(profile.pays, profile.pays or "Maroc"),
        "country": COUNTRY_MAP.get(profile.pays, profile.pays or "Maroc"),
        "metrics": metrics,
    }


# --- Markdown formatters ---

def _format_scoring(result: dict) -> str:
    """Format scoring result as markdown."""
    lines = [f"**Score de Fundability : {result['score']}/100**\n"]

    if result.get("breakdown"):
        lines.append("| Métrique | Valeur | Niveau | Score |")
        lines.append("|----------|--------|--------|-------|")
        for b in result["breakdown"]:
            level_emoji = {"excellent": "🟢", "good": "🟢", "ok": "🟡", "bad": "🔴"}.get(b["level"], "")
            lines.append(f"| {b['name_fr']} | {b['value']} | {level_emoji} {b['level']} | {b['level_score']}/100 |")
        lines.append("")

    if result.get("strengths"):
        lines.append("**Forces :**")
        for s in result["strengths"]:
            lines.append(f"- ✅ {s}")
        lines.append("")

    if result.get("weaknesses"):
        lines.append("**Faiblesses :**")
        for w in result["weaknesses"]:
            lines.append(f"- ⚠️ {w}")
        lines.append("")

    if result.get("action_plan"):
        lines.append(f"**{result['action_plan']}**")

    return "\n".join(lines)


def _format_diagnostic(result: dict) -> str:
    """Format diagnostic result as markdown."""
    lines = [f"**Diagnostic Financier**\n"]

    if result.get("summary"):
        lines.append(f"_{result['summary']}_\n")

    for a in result.get("analyses", []):
        level_emoji = {"excellent": "🟢", "good": "🟢", "ok": "🟡", "bad": "🔴"}.get(a["level"], "")
        lines.append(f"### {a['name_fr']} ({a['metric']})")
        lines.append(f"- **Valeur :** {a['value']} → {level_emoji} {a['level']}")
        lines.append(f"- **Benchmark :** bad={a['benchmark'].get('bad')}, ok={a['benchmark'].get('ok')}, good={a['benchmark'].get('good')}, excellent={a['benchmark'].get('excellent')}")

        if a.get("improvement_tips"):
            lines.append("- **Conseils :**")
            for tip in a["improvement_tips"][:3]:
                lines.append(f"  - {tip}")
        lines.append("")

    return "\n".join(lines)


def _format_investors(result: dict) -> str:
    """Format investor matching result as markdown."""
    lines = [f"**Investisseurs correspondant à votre profil** ({result['total_found']} trouvés)\n"]

    for i, m in enumerate(result.get("matches", []), 1):
        lines.append(f"{i}. **{m['name']}** — {m['type']}")
        lines.append(f"   - Ticket : {m['ticket']}")
        lines.append(f"   - Score : {m['match_score']}/4")
        lines.append(f"   - Raisons : {', '.join(m['match_reasons'])}")
        if m.get("criteria"):
            lines.append(f"   - Critères : {m['criteria'][:150]}")
        lines.append("")

    return "\n".join(lines)


def _format_grants(result: dict) -> str:
    """Format grant matching result as markdown."""
    lines = [f"**Subventions éligibles** ({result['total_found']} trouvées)\n"]

    for i, m in enumerate(result.get("matches", []), 1):
        lines.append(f"{i}. **{m['name']}** — {m['organization']}")
        lines.append(f"   - Type : {m['type']}")
        lines.append(f"   - Montant : {m['amount']}")
        if m.get("conditions"):
            lines.append(f"   - Conditions : {'; '.join(m['conditions'][:2])}")
        lines.append("")

    return "\n".join(lines)


def _format_metrics(result: dict) -> str:
    """Format metric explanations as markdown."""
    explanations = result.get("metrics", [])
    if not explanations:
        return "Aucune métrique trouvée."

    lines = ["Voici les métriques clés pour évaluer votre startup :\n"]
    for m in explanations:
        lines.append(f"### {m['name_fr']} ({m['id']})")
        lines.append(f"{m['definition']}\n")
        if m.get("formula"):
            lines.append(f"**Formule :** {m['formula']}\n")
    lines.append("---\nVous pouvez maintenant fournir vos KPIs pour calculer votre score, par exemple :\n*MRR: 8000, churn: 5%, CAC: 200, stade seed*")
    return "\n".join(lines)


def _format_qa(result: dict) -> str:
    """Format RAG Q&A result as markdown."""
    lines = [result.get("answer", "")]
    if result.get("sources"):
        lines.append("\n---\n**Sources :** " + ", ".join(result["sources"]))
    return "\n".join(lines)


def _format_response(router_output: dict) -> str:
    """Convert router output dict to a markdown string for the frontend."""
    if "error" in router_output:
        return router_output["error"]

    intent = router_output.get("intent", "qa")
    result = router_output.get("result", {})

    formatters = {
        "scoring": _format_scoring,
        "diagnostic": _format_diagnostic,
        "metrics": _format_metrics,
        "investors": _format_investors,
        "grants": _format_grants,
        "qa": _format_qa,
    }

    formatter = formatters.get(intent, _format_qa)
    return formatter(result)


# --- Endpoint ---

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process a chat message and return a markdown response."""
    profile = _build_router_profile(request.profile)
    history = [{"role": m.role, "content": m.content} for m in request.history]
    router_output = route(request.message, startup_profile=profile, history=history)
    reply = _format_response(router_output)
    return ChatResponse(reply=reply)


@app.get("/health")
async def health():
    return {"status": "ok"}
