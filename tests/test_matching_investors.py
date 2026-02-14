"""Tests for the investor matching module."""

import pytest
from backend.app.modules.matching_investors import match_investors


class TestMatchInvestors:
    def test_returns_dict_with_required_keys(self):
        result = match_investors("fintech", "seed", "Maroc")
        assert "query" in result
        assert "total_found" in result
        assert "showing" in result
        assert "matches" in result

    def test_default_top_k_is_5(self):
        result = match_investors("fintech", "seed", "Maroc")
        assert result["showing"] <= 5

    def test_custom_top_k(self):
        result = match_investors("fintech", "seed", "Maroc", top_k=3)
        assert result["showing"] <= 3

    def test_matches_have_correct_fields(self):
        result = match_investors("fintech", "seed", "Maroc")
        if result["matches"]:
            m = result["matches"][0]
            assert "name" in m
            assert "type" in m
            assert "match_score" in m
            assert "match_reasons" in m
            assert "ticket" in m

    def test_fintech_seed_maroc(self):
        """Dev plan scenario: fintech, seed, Maroc."""
        result = match_investors("fintech", "seed", "Maroc")
        assert result["total_found"] > 0
        # 212 Founders should be in results (fintech + seed + Maroc)
        names = [m["name"] for m in result["matches"]]
        assert "212 Founders" in names

    def test_sorted_by_score_descending(self):
        result = match_investors("fintech", "seed", "Maroc")
        scores = [m["match_score"] for m in result["matches"]]
        assert scores == sorted(scores, reverse=True)

    def test_funding_amount_filter(self):
        result = match_investors("fintech", "seed", "Maroc", funding_amount=5_000_000)
        for m in result["matches"]:
            # All matches should have ticket compatibility as a reason
            # or at least match on other criteria
            assert m["match_score"] >= 1

    def test_few_matches_for_impossible_criteria(self):
        """Impossible sector + geography still matches on stage alone."""
        result = match_investors("underwater_basket_weaving", "impossible_stage", "Antarctique")
        assert result["total_found"] == 0

    def test_match_score_max_is_4(self):
        """Max score is 4: sector + stage + geography + ticket."""
        result = match_investors("fintech", "seed", "Maroc", funding_amount=5_000_000)
        if result["matches"]:
            assert result["matches"][0]["match_score"] <= 4

    def test_query_echoed_in_result(self):
        result = match_investors("saas", "série a", "France")
        assert result["query"]["sector"] == "saas"
        assert result["query"]["stage"] == "série a"
        assert result["query"]["geography"] == "France"
