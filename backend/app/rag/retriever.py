"""
Retriever for Tamwil AI.
Searches ChromaDB for the most relevant chunks given a user query.
"""

from langchain_core.documents import Document
from backend.app.config import TOP_K
from backend.app.rag.vectorstore import get_vectorstore


def retrieve(query: str, k: int = None, filter_type: str = None) -> list[Document]:
    """Search ChromaDB for chunks most similar to the query.

    Args:
        query: The user's question in French.
        k: Number of results to return (default from config: 5).
        filter_type: Optional filter by document type ("faq", "fundraising_guide", "regulation").

    Returns:
        List of LangChain Documents sorted by relevance.
    """
    if k is None:
        k = TOP_K

    vectorstore = get_vectorstore()

    search_kwargs = {"k": k}
    if filter_type:
        search_kwargs["filter"] = {"type": filter_type}

    results = vectorstore.similarity_search(query, **search_kwargs)
    return results


def retrieve_with_scores(query: str, k: int = None) -> list[tuple[Document, float]]:
    """Same as retrieve() but also returns similarity scores.

    Returns:
        List of (Document, score) tuples. Lower score = more similar.
    """
    if k is None:
        k = TOP_K

    vectorstore = get_vectorstore()
    results = vectorstore.similarity_search_with_score(query, k=k)
    return results


# --- Standalone: test the retriever ---
if __name__ == "__main__":
    import sys

    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Comment valoriser ma startup en pré-seed ?"

    print("=" * 60)
    print(f"  Query: {query}")
    print("=" * 60)
    print()

    results = retrieve_with_scores(query)

    for i, (doc, score) in enumerate(results, 1):
        source = doc.metadata.get("source", "?")
        doc_type = doc.metadata.get("type", "?")
        preview = doc.page_content[:200].replace("\n", " ")
        print(f"  [{i}] score: {score:.4f} | source: {source} | type: {doc_type}")
        print(f"      {preview}...")
        print()
