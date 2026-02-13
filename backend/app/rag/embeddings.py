"""
Embedding model configuration for Tamwil AI.
Uses sentence-transformers with a multilingual model that supports French.
Runs locally — no API cost, no internet needed after first download.
"""

from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.app.config import EMBEDDING_MODEL


def get_embedding_function() -> HuggingFaceEmbeddings:
    """Return the embedding model used across the entire project.

    Model: paraphrase-multilingual-MiniLM-L12-v2
    - Dimension: 384
    - Supports French
    - Free and local
    """
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


# --- Standalone: test the embedding model ---
if __name__ == "__main__":
    print("Loading embedding model...")
    embeddings = get_embedding_function()

    test_texts = [
        "Comment valoriser ma startup en pré-seed ?",
        "Quelles sont les obligations RGPD au Maroc ?",
    ]

    for text in test_texts:
        vector = embeddings.embed_query(text)
        print(f"\n  Text: {text}")
        print(f"  Vector dim: {len(vector)}")
        print(f"  First 5 values: {vector[:5]}")

    print("\nEmbedding model OK!")
