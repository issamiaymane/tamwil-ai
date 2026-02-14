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

Règles :
- Réponds UNIQUEMENT en français.
- Base tes réponses EXCLUSIVEMENT sur le contexte fourni ci-dessous.
- Si le contexte ne contient pas l'information, dis-le clairement : "Je n'ai pas cette information dans ma base de connaissances."
- Cite les sources quand c'est pertinent.
- Sois concis, structuré et actionnable.

Contexte :
{context}"""

USER_PROMPT = "{question}"


def answer_question(question: str, k: int = 5) -> dict:
    """Answer a question using RAG (retrieve + generate).

    Args:
        question: User question in French.
        k: Number of chunks to retrieve (default 5).

    Returns:
        Dict with answer text and sources used.
    """
    # Retrieve relevant chunks
    docs = retrieve(question, k=k)

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

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", USER_PROMPT),
    ])

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
