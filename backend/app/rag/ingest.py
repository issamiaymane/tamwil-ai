"""
Document ingestion and chunking for Tamwil AI.
Loads all FAQ, fundraising guides, regulation documents,
investors, grants, and metrics — then splits them into
chunks and prepares them for vectorization.
"""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.app.config import CHUNK_SIZE, CHUNK_OVERLAP
from backend.app.utils.data_loader import (
    load_faq,
    load_fundraising_guides,
    load_regulations,
    load_investors,
    load_grants,
    load_metrics,
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


def _build_investor_documents() -> list[Document]:
    """Convert investor profiles into LangChain Documents."""
    investors = load_investors()
    documents = []
    for inv in investors:
        sectors = ", ".join(inv.get("sectors") or [])
        stages = ", ".join(inv.get("stage") or [])
        geo = ", ".join(inv.get("geography") or [])
        t_min = inv.get("ticket_min") or 0
        t_max = inv.get("ticket_max") or 0
        ticket = f"{t_min:,} - {t_max:,} {inv.get('currency', '')}"
        criteria = (inv.get("criteria") or {}).get("description", "")
        portfolio_raw = inv.get("portfolio_examples") or []
        portfolio = ", ".join(portfolio_raw) if isinstance(portfolio_raw, list) else str(portfolio_raw)

        text = (
            f"Investisseur : {inv['name']}\n"
            f"Type : {inv.get('type', '')}\n"
            f"Description : {inv.get('description', '')}\n"
            f"Secteurs : {sectors}\n"
            f"Stades : {stages}\n"
            f"Ticket : {ticket}\n"
            f"Géographie : {geo}\n"
            f"Critères : {criteria}\n"
            f"Portfolio : {portfolio}"
        )
        doc = Document(
            page_content=text,
            metadata={
                "source": "investors.json",
                "type": "investor",
                "id": inv.get("id"),
                "name": inv.get("name"),
            },
        )
        documents.append(doc)
    return documents


def _build_grant_documents() -> list[Document]:
    """Convert grant programs into LangChain Documents."""
    grants = load_grants()
    documents = []
    for g in grants:
        eligibility = g.get("eligibility") or {}
        stages = ", ".join(eligibility.get("stage") or [])
        sectors = ", ".join(eligibility.get("sectors") or [])
        conditions = "; ".join(eligibility.get("conditions") or [])
        a_min = g.get("amount_min") or 0
        a_max = g.get("amount_max") or 0
        amount = f"{a_min:,} - {a_max:,} {g.get('currency', '')}"

        text = (
            f"Programme : {g['name']}\n"
            f"Organisation : {g.get('organization', '')}\n"
            f"Pays : {g.get('country', '')}\n"
            f"Type : {g.get('type', '')}\n"
            f"Description : {g.get('description', '')}\n"
            f"Montant : {amount}\n"
            f"Stades éligibles : {stages}\n"
            f"Secteurs : {sectors}\n"
            f"Âge max : {eligibility.get('age_max_company', 'N/A')}\n"
            f"Conditions : {conditions}\n"
            f"Processus : {g.get('application_process', '')}"
        )
        doc = Document(
            page_content=text,
            metadata={
                "source": "grants.json",
                "type": "grant",
                "id": g.get("id"),
                "name": g.get("name"),
            },
        )
        documents.append(doc)
    return documents


def _build_metric_documents() -> list[Document]:
    """Convert metric definitions into LangChain Documents."""
    metrics = load_metrics()
    documents = []
    for m in metrics:
        benchmarks_text = ""
        for stage, levels in m.get("benchmarks", {}).items():
            benchmarks_text += f"  {stage}: bad={levels.get('bad')}, ok={levels.get('ok')}, good={levels.get('good')}, excellent={levels.get('excellent')}\n"

        tips = "; ".join(m.get("improvement_tips", []))

        text = (
            f"Métrique : {m.get('name_fr', m['name'])} ({m['id']})\n"
            f"Définition : {m.get('definition', '')}\n"
            f"Formule : {m.get('formula', '')}\n"
            f"Unité : {m.get('unit', '')}\n"
            f"Benchmarks :\n{benchmarks_text}"
            f"Interprétation : {m.get('interpretation', '')}\n"
            f"Conseils d'amélioration : {tips}"
        )
        doc = Document(
            page_content=text,
            metadata={
                "source": "metrics_reference.json",
                "type": "metric",
                "id": m.get("id"),
                "name": m.get("name_fr", m["name"]),
            },
        )
        documents.append(doc)
    return documents


def load_all_documents() -> list[Document]:
    """Load all documents from all 6 sources."""
    documents = []
    documents.extend(_build_faq_documents())
    documents.extend(_build_markdown_documents(load_fundraising_guides, "fundraising_guide"))
    documents.extend(_build_markdown_documents(load_regulations, "regulation"))
    documents.extend(_build_investor_documents())
    documents.extend(_build_grant_documents())
    documents.extend(_build_metric_documents())
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
    for doc_type in ["faq", "fundraising_guide", "regulation", "investor", "grant", "metric"]:
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
