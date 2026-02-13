"""
Document ingestion and chunking for Tamwil AI.
Loads all FAQ, fundraising guides, and regulation documents,
splits them into chunks, and prepares them for vectorization.
"""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.app.config import CHUNK_SIZE, CHUNK_OVERLAP
from backend.app.utils.data_loader import (
    load_faq,
    load_fundraising_guides,
    load_regulations,
)


def _build_faq_documents() -> list[Document]:
    """Convert FAQ entries into LangChain Documents.
    Each Q&A becomes one document (question + answer combined).
    """
    faq_data = load_faq()
    documents = []
    for entry in faq_data:
        text = f"Question : {entry['question']}\nRéponse : {entry['reponse']}"
        doc = Document(
            page_content=text,
            metadata={
                "source": "faq.json",
                "type": "faq",
                "id": entry.get("id"),
                "categorie": entry.get("categorie", ""),
            },
        )
        documents.append(doc)
    return documents


def _build_markdown_documents(loader_func, source_type: str) -> list[Document]:
    """Convert markdown files into LangChain Documents."""
    md_files = loader_func()
    documents = []
    for md in md_files:
        doc = Document(
            page_content=md["content"],
            metadata={
                "source": md["filename"],
                "type": source_type,
            },
        )
        documents.append(doc)
    return documents


def load_all_documents() -> list[Document]:
    """Load all documents from all sources (FAQ + guides + regulations)."""
    documents = []
    documents.extend(_build_faq_documents())
    documents.extend(_build_markdown_documents(load_fundraising_guides, "fundraising_guide"))
    documents.extend(_build_markdown_documents(load_regulations, "regulation"))
    return documents


def chunk_documents(documents: list[Document]) -> list[Document]:
    """Split documents into smaller chunks for vectorization."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n## ", "\n### ", "\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    return chunks


def ingest() -> list[Document]:
    """Full ingestion pipeline: load all documents, then chunk them."""
    documents = load_all_documents()
    chunks = chunk_documents(documents)
    return chunks


# --- Standalone: test the ingestion ---
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    print("=" * 60)
    print("  Tamwil AI — Document Ingestion")
    print("=" * 60)
    print()

    documents = load_all_documents()
    print(f"  Documents loaded: {len(documents)}")
    for doc_type in ["faq", "fundraising_guide", "regulation"]:
        count = sum(1 for d in documents if d.metadata.get("type") == doc_type)
        print(f"    - {doc_type}: {count}")

    print()
    chunks = chunk_documents(documents)
    print(f"  Chunks created: {len(chunks)}")
    print()

    # Show a sample chunk
    if chunks:
        sample = chunks[0]
        print(f"  Sample chunk:")
        print(f"    Source: {sample.metadata.get('source')}")
        print(f"    Type: {sample.metadata.get('type')}")
        print(f"    Length: {len(sample.page_content)} chars")
        print(f"    Preview: {sample.page_content[:150]}...")

    print()
    print("=" * 60)
    print("  Ingestion complete!")
