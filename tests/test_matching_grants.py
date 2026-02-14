"""Tests for the grant matching module."""

import pytest
from backend.app.modules.matching_grants import match_grants, _parse_age_max


class TestParseAgeMax:
    def test_parse_5_ans(self):
        assert _parse_age_max("5 ans") == 5

    def test_parse_3_ans(self):
        assert _parse_age_max("3 ans") == 3

    def test_parse_none(self):
        assert _parse_age_max("") is None

    def test_parse_na(self):
        assert _parse_age_max("N/A") is None


class TestMatchGrants:
    def test_returns_dict_with_required_keys(self):
        result = match_grants("fintech", "seed", "Maroc")
        assert "query" in result
        assert "total_found" in result
        assert "matches" in result

    def test_matches_have_correct_fields(self):
        result = match_grants("fintech", "seed", "Maroc")
        if result["matches"]:
            m = result["matches"][0]
            assert "name" in m
            assert "organization" in m
            assert "amount" in m
            assert "match_reasons" in m

    def test_maroc_seed_finds_innov_start(self):
        result = match_grants("fintech", "seed", "Maroc")
        names = [m["name"] for m in result["matches"]]
        assert "Innov Start" in names

    def test_dev_plan_scenario(self):
        """Test scenario: edtech, 2 ans, Maroc."""
        result = match_grants("edtech", "seed", "Maroc", company_age=2)
        assert result["total_found"] > 0

    def test_country_filter_france(self):
        result = match_grants("saas", "seed", "France")
        for m in result["matches"]:
            assert m["country"] in ("France", "International")

    def test_country_filter_maroc(self):
        result = match_grants("saas", "seed", "Maroc")
        for m in result["matches"]:
            assert m["country"] in ("Maroc", "International")

    def test_age_filter_excludes_old_companies(self):
        """Company with 10 years should be excluded from programs with 5-year max."""
        result_young = match_grants("fintech", "seed", "Maroc", company_age=2)
        result_old = match_grants("fintech", "seed", "Maroc", company_age=10)
        assert result_young["total_found"] >= result_old["total_found"]

    def test_no_results_for_impossible_country(self):
        result = match_grants("fintech", "seed", "Antarctique")
        # Only international grants should match
        for m in result["matches"]:
            assert m["country"] == "International"

    def test_query_echoed_in_result(self):
        result = match_grants("edtech", "pre-seed", "Maroc", company_age=1)
        assert result["query"]["sector"] == "edtech"
        assert result["query"]["stage"] == "pre-seed"
        assert result["query"]["country"] == "Maroc"
        assert result["query"]["company_age"] == 1
