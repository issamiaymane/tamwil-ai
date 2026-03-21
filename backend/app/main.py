"""
FastAPI server for Tamwil AI.
Exposes the router/orchestrator as an HTTP API for the Next.js frontend.
"""

import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.app.router import route, detect_intent
from backend.app.modules.rag_qa import answer_question_stream
from backend.app.source_urls import get_source_url


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


class SourceInfo(BaseModel):
    name: str
    type: str
    url: str


class ChatResponse(BaseModel):
    reply: str
    sources: list[SourceInfo] = []


# --- App ---

app = FastAPI(title="Tamwil AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://192.168.88.1:3000"],
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
    return result.get("answer", "")


def _extract_sources(router_output: dict) -> list[dict]:
    """Extract structured source info from router output."""
    result = router_output.get("result", {})
    raw_sources = result.get("sources", [])
    sources = []
    for entry in raw_sources:
        # entry format: "filename.md (type)"
        name = entry
        doc_type = ""
        if " (" in entry and entry.endswith(")"):
            name, doc_type = entry.rsplit(" (", 1)
            doc_type = doc_type.rstrip(")")
        url = get_source_url(name)
        sources.append({"name": name, "type": doc_type, "url": url})
    return sources


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
    sources = _extract_sources(router_output)
    return ChatResponse(reply=reply, sources=sources)


def _sse_event(event: str, data: str) -> str:
    """Format a single SSE event. Multi-line data gets split into multiple data: lines."""
    lines = data.split("\n")
    data_lines = "\n".join(f"data: {line}" for line in lines)
    return f"event: {event}\n{data_lines}\n\n"


def _resolve_sources(raw_sources: list[str]) -> list[dict]:
    """Convert raw source strings to structured dicts with URLs."""
    sources = []
    for entry in raw_sources:
        name = entry
        doc_type = ""
        if " (" in entry and entry.endswith(")"):
            name, doc_type = entry.rsplit(" (", 1)
            doc_type = doc_type.rstrip(")")
        url = get_source_url(name)
        sources.append({"name": name, "type": doc_type, "url": url})
    return sources


async def _stream_qa(message: str, profile: dict, history: list[dict]):
    """Generator for streaming QA responses as SSE events."""
    for item in answer_question_stream(message, history=history):
        if item["type"] == "sources":
            sources = _resolve_sources(item["sources"])
            yield _sse_event("sources", json.dumps(sources))
        elif item["type"] == "token":
            yield _sse_event("token", item["token"])
    yield _sse_event("done", "")


async def _stream_non_qa(message: str, profile: dict, history: list[dict]):
    """Generator for non-streaming intents sent as single SSE events."""
    router_output = route(message, startup_profile=profile, history=history)
    reply = _format_response(router_output)
    sources = _extract_sources(router_output)

    yield _sse_event("sources", json.dumps(sources))
    yield _sse_event("reply", json.dumps({"text": reply}))
    yield _sse_event("done", "")


GREETING_WORDS = {"bonjour", "salut", "hello", "hi", "hey", "bonsoir", "coucou", "salam", "yo", "merci", "thanks", "thank you", "ok", "oui", "non", "d'accord", "hola", "bonne", "journée", "soir", "nuit", "svp", "stp", "wesh", "azul", "marhaba"}


def _is_greeting(message: str) -> bool:
    """Check if the message is a casual greeting with no real question."""
    words = set(message.lower().strip().rstrip("!?.,").split())
    return len(words) <= 3 and bool(words & GREETING_WORDS)


async def _stream_greeting(message: str, profile: dict, history: list[dict]):
    """Generator for greeting messages — no sources, fixed French response."""
    yield _sse_event("sources", json.dumps([]))
    greeting = "Bonjour ! Comment puis-je vous aider aujourd'hui dans le domaine du financement de startups au Maroc et en Afrique francophone ?"
    yield _sse_event("token", greeting)
    yield _sse_event("done", "")


@app.post("/api/chat/stream")
async def chat_stream(request: ChatRequest):
    """Process a chat message and stream the response as SSE events."""
    profile = _build_router_profile(request.profile)
    history = [{"role": m.role, "content": m.content} for m in request.history]

    if _is_greeting(request.message):
        generator = _stream_greeting
    else:
        intent = detect_intent(request.message, history=history)
        generator = _stream_qa if intent == "qa" else _stream_non_qa

    return StreamingResponse(
        generator(request.message, profile, history),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
