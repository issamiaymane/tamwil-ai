"""
RAG-based Q&A for Tamwil AI.
Retrieves relevant chunks from ChromaDB and generates answers via LLM.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from backend.app.config import OPENAI_API_KEY, LLM_MODEL
from backend.app.rag.retriever import retrieve


SYSTEM_PROMPT = """Tu es Tamwil AI, un assistant expert en financement de startups au Maroc et en Afrique francophone.

=== RÈGLES COMPORTEMENTALES (PRIORITAIRES) ===
1. Tente TOUJOURS de répondre en utilisant le contexte récupéré — ne refuse jamais sauf si la question est totalement hors domaine.
2. Si les documents récupérés couvrent partiellement le sujet, utilise-les comme base et complète avec tes connaissances générales — un contexte partiel n'est pas un contexte absent.
3. Ne fabrique JAMAIS de noms de documents, statistiques ou références. Si tu enrichis avec tes connaissances générales, signale-le naturellement (ex: "D'après les informations disponibles...").
4. Ne dis JAMAIS "Je n'ai pas cette information dans ma base de connaissances" ou toute variante de refus — réponds avec ce que tu sais et précise que certains détails peuvent varier.
5. Reste concentré sur le domaine (financement, startups, Maroc/Afrique) mais ne refuse pas les questions raisonnablement liées — fais preuve de jugement.
6. Réponds TOUJOURS dans la langue utilisée par l'utilisateur — ne change jamais de langue en cours de réponse.
7. Maintiens un ton professionnel et utile, quelle que soit la complétude du contexte.
8. Si aucun document pertinent n'est récupéré, donne la meilleure réponse générale possible et suggère à l'utilisateur de reformuler ou préciser.
9. Si les chunks récupérés ont une faible pertinence, tente quand même une réponse — faible pertinence ne signifie pas zéro pertinence.

RÈGLE D'OR : Une réponse partielle est TOUJOURS meilleure qu'aucune réponse. L'utilisateur doit toujours recevoir quelque chose d'utile.

=== INSTRUCTIONS ===
- Sois concis, structuré et actionnable.
- Tiens compte de l'historique de conversation pour comprendre les références implicites (ex: "ces métriques", "explique ça").

Contexte :
{context}"""

USER_PROMPT = "{question}"


def _build_enriched_query(question: str, history: list[dict] = None) -> str:
    """Enrich user question with recent conversation context for better RAG retrieval."""
    if not history:
        return question

    # Take last 2 exchanges max to add context
    recent = history[-4:]
    history_text = " ".join(msg["content"] for msg in recent)

    return f"{history_text} {question}"


def answer_question(question: str, k: int = 5, history: list[dict] = None) -> dict:
    """Answer a question using RAG (retrieve + generate).

    Args:
        question: User question in French.
        k: Number of chunks to retrieve (default 5).
        history: Conversation history as list of {"role": ..., "content": ...} dicts.

    Returns:
        Dict with answer text and sources used.
    """
    # Enrich query with conversation context for better retrieval
    enriched_query = _build_enriched_query(question, history)
    docs = retrieve(enriched_query, k=k)

    # Build context from retrieved documents
    context_parts = []
    sources = []
    for doc in docs:
        context_parts.append(doc.page_content)
        source = doc.metadata.get("source", "inconnu")
        doc_type = doc.metadata.get("type", "")
        source_entry = f"{source} ({doc_type})"
        if source_entry not in sources:
            sources.append(source_entry)

    context = "\n---\n".join(context_parts)

    # Generate answer via LLM
    if not OPENAI_API_KEY:
        # Fallback: return raw context without LLM
        return {
            "answer": (
                "⚠ Clé API OpenAI non configurée. Voici les extraits pertinents :\n\n"
                + "\n\n---\n\n".join(context_parts[:3])
            ),
            "sources": sources,
            "mode": "fallback_no_llm",
        }

    # Build message list with history for conversational context
    messages = [("system", SYSTEM_PROMPT)]
    if history:
        for msg in history[-6:]:  # Last 3 exchanges max
            role = "human" if msg["role"] == "user" else "ai"
            messages.append((role, msg["content"]))
    messages.append(("human", USER_PROMPT))

    prompt = ChatPromptTemplate.from_messages(messages)

    llm = ChatOpenAI(
        model=LLM_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.3,
    )

    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": question})

    return {
        "answer": answer,
        "sources": sources,
        "mode": "rag_llm",
    }


def answer_question_stream(question: str, k: int = 5, history: list[dict] = None):
    """Stream answer tokens using RAG (retrieve + generate).

    Yields:
        First yield: dict with {"type": "sources", "sources": [...]}
        Subsequent yields: dict with {"type": "token", "token": "..."}
    """
    enriched_query = _build_enriched_query(question, history)
    docs = retrieve(enriched_query, k=k)

    context_parts = []
    sources = []
    for doc in docs:
        context_parts.append(doc.page_content)
        source = doc.metadata.get("source", "inconnu")
        doc_type = doc.metadata.get("type", "")
        source_entry = f"{source} ({doc_type})"
        if source_entry not in sources:
            sources.append(source_entry)

    context = "\n---\n".join(context_parts)

    # Yield sources first
    yield {"type": "sources", "sources": sources}

    if not OPENAI_API_KEY:
        fallback = (
            "⚠ Clé API OpenAI non configurée. Voici les extraits pertinents :\n\n"
            + "\n\n---\n\n".join(context_parts[:3])
        )
        yield {"type": "token", "token": fallback}
        return

    messages = [("system", SYSTEM_PROMPT)]
    if history:
        for msg in history[-6:]:
            role = "human" if msg["role"] == "user" else "ai"
            messages.append((role, msg["content"]))
    messages.append(("human", USER_PROMPT))

    prompt = ChatPromptTemplate.from_messages(messages)

    llm = ChatOpenAI(
        model=LLM_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.3,
        streaming=True,
    )

    chain = prompt | llm | StrOutputParser()
    for chunk in chain.stream({"context": context, "question": question}):
        yield {"type": "token", "token": chunk}


# --- Standalone test ---
if __name__ == "__main__":
    import sys

    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Comment valoriser ma startup en pré-seed ?"

    print("=" * 60)
    print(f"  Tamwil AI — RAG Q&A Test")
    print("=" * 60)
    print(f"\n  Question: {question}\n")

    result = answer_question(question)
    print(f"  Mode: {result['mode']}")
    print(f"  Sources: {', '.join(result['sources'])}")
    print(f"\n  Réponse:\n  {result['answer']}")
