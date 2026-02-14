"""Tests for the RAG pipeline (ingest, retriever, vectorstore)."""

import pytest
from backend.app.rag.retriever import retrieve, retrieve_with_scores
from backend.app.rag.ingest import load_all_documents, chunk_documents
from backend.app.modules.rag_qa import answer_question


# --- Ingestion ---

class TestIngestion:
    def test_load_all_documents_returns_list(self):
        docs = load_all_documents()
        assert isinstance(docs, list)
        assert len(docs) > 0

    def test_all_6_types_present(self):
        docs = load_all_documents()
        types = {d.metadata.get("type") for d in docs}
        expected = {"faq", "fundraising_guide", "regulation", "investor", "grant", "metric"}
        assert expected.issubset(types), f"Missing types: {expected - types}"

    def test_chunking_produces_more_than_documents(self):
        docs = load_all_documents()
        chunks = chunk_documents(docs)
        # Chunking should produce more pieces than original documents
        assert len(chunks) >= len(docs)

    def test_chunks_have_metadata(self):
        docs = load_all_documents()
        chunks = chunk_documents(docs)
        for chunk in chunks[:10]:
            assert "type" in chunk.metadata
            assert "source" in chunk.metadata

    def test_investor_count(self):
        docs = load_all_documents()
        investors = [d for d in docs if d.metadata.get("type") == "investor"]
        assert len(investors) == 38

    def test_grant_count(self):
        docs = load_all_documents()
        grants = [d for d in docs if d.metadata.get("type") == "grant"]
        assert len(grants) == 25

    def test_faq_count(self):
        docs = load_all_documents()
        faqs = [d for d in docs if d.metadata.get("type") == "faq"]
        assert len(faqs) == 50


# --- Retriever ---

class TestRetriever:
    def test_retrieve_returns_documents(self):
        results = retrieve("Comment valoriser ma startup ?")
        assert len(results) > 0

    def test_retrieve_respects_k(self):
        results = retrieve("financement startup", k=3)
        assert len(results) == 3

    def test_retrieve_default_k(self):
        results = retrieve("financement startup")
        assert len(results) == 5  # TOP_K default

    def test_retrieve_with_scores_returns_tuples(self):
        results = retrieve_with_scores("valorisation startup")
        assert len(results) > 0
        doc, score = results[0]
        assert hasattr(doc, "page_content")
        assert isinstance(score, float)

    def test_retrieve_relevant_content(self):
        """Searching for investors should return investor-type documents."""
        results = retrieve("investisseurs fintech Maroc", k=5)
        types = [r.metadata.get("type") for r in results]
        assert "investor" in types

    def test_retrieve_grants(self):
        """Searching for grants should return grant-type documents."""
        results = retrieve("subvention startup Maroc Innov Start", k=5)
        types = [r.metadata.get("type") for r in results]
        assert "grant" in types


# --- RAG Q&A ---

class TestRagQA:
    def test_answer_returns_dict(self):
        result = answer_question("Qu'est-ce que le MRR ?")
        assert "answer" in result
        assert "sources" in result
        assert "mode" in result

    def test_answer_has_sources(self):
        result = answer_question("Qu'est-ce que le MRR ?")
        assert len(result["sources"]) > 0

    def test_fallback_mode_without_api_key(self):
        """Without an OpenAI key, should fall back gracefully."""
        result = answer_question("Comment lever des fonds ?")
        # Should either use LLM or fallback — both are valid
        assert result["mode"] in ("rag_llm", "fallback_no_llm")
