"""
ChromaDB vector store for Tamwil AI.
Handles initialization, indexing, and persistence of document embeddings.
"""

import shutil
from pathlib import Path
from langchain_community.vectorstores import Chroma
from backend.app.config import CHROMA_PERSIST_DIR
from backend.app.rag.embeddings import get_embedding_function
from backend.app.rag.ingest import ingest


COLLECTION_NAME = "tamwil_knowledge_base"


def get_vectorstore() -> Chroma:
    """Load the existing ChromaDB vector store from disk.
    Call this after build_vectorstore() has been run at least once.
    """
    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=get_embedding_function(),
    )


def build_vectorstore() -> Chroma:
    """Full pipeline: ingest documents, embed them, store in ChromaDB.
    This clears any existing data and rebuilds from scratch.
    """
    # Clear old data if it exists
    db_path = Path(CHROMA_PERSIST_DIR)
    if db_path.exists():
        shutil.rmtree(db_path)
        print(f"  Cleared old ChromaDB at {db_path}")

    # Ingest and chunk all documents
    print("  Ingesting documents...")
    chunks = ingest()
    print(f"  {len(chunks)} chunks ready to index")

    # Create ChromaDB and store all chunks
    print("  Embedding and storing in ChromaDB (this may take a minute)...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_function(),
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PERSIST_DIR,
    )

    print(f"  ChromaDB built and persisted to {CHROMA_PERSIST_DIR}")
    return vectorstore


# --- Standalone: build the vector store ---
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    print("=" * 60)
    print("  Tamwil AI — Build Vector Store")
    print("=" * 60)
    print()

    vectorstore = build_vectorstore()

    # Verify it works
    count = vectorstore._collection.count()
    print()
    print(f"  Verification: {count} vectors stored in ChromaDB")
    print()
    print("=" * 60)
    print("  Vector store ready!")
