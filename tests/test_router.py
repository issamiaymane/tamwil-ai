"""Tests for the router/orchestrator."""

import pytest
from backend.app.router import (
    route,
    _detect_intent,
    _extract_metrics,
    _extract_stage,
    _extract_sector,
    _extract_country,
    _extract_age,
    _extract_amount,
)


# --- Intent Detection ---

class TestDetectIntent:
    def test_scoring_intent(self):
        assert _detect_intent("Quel est mon score de fundability ?") == "scoring"

    def test_scoring_via_keywords(self):
        assert _detect_intent("Je veux noter ma startup") == "scoring"

    def test_diagnostic_intent(self):
        assert _detect_intent("Fais un diagnostic de mes KPIs") == "diagnostic"

    def test_diagnostic_via_keywords(self):
        assert _detect_intent("Analyse ma santé financière") == "diagnostic"

    def test_investors_intent(self):
        assert _detect_intent("Quels investisseurs pour ma startup ?") == "investors"

    def test_investors_via_vc(self):
        assert _detect_intent("Je cherche un VC au Maroc") == "investors"

    def test_grants_intent(self):
        assert _detect_intent("Quelles subventions sont disponibles ?") == "grants"

    def test_grants_via_keywords(self):
        assert _detect_intent("Programme de financement public") == "grants"

    def test_fallback_to_qa(self):
        assert _detect_intent("Comment valoriser ma startup en pré-seed ?") == "qa"

    def test_metric_values_trigger_scoring(self):
        assert _detect_intent("MRR: 8000, CAC: 200") == "scoring"


# --- Data Extraction ---

class TestExtractMetrics:
    def test_extract_mrr(self):
        metrics = _extract_metrics("MRR: 8000")
        assert metrics.get("MRR") == 8000

    def test_extract_churn(self):
        metrics = _extract_metrics("churn: 5%")
        assert metrics.get("CHURN_RATE") == 5

    def test_extract_cac(self):
        metrics = _extract_metrics("CAC: 200")
        assert metrics.get("CAC") == 200

    def test_extract_multiple(self):
        metrics = _extract_metrics("MRR: 8000, burn rate: 15000, churn: 5%")
        assert "MRR" in metrics
        assert "BURN_RATE" in metrics
        assert "CHURN_RATE" in metrics

    def test_no_metrics(self):
        metrics = _extract_metrics("Bonjour, comment ça va ?")
        assert len(metrics) == 0


class TestExtractStage:
    def test_seed(self):
        assert _extract_stage("stade seed") == "seed"

    def test_pre_seed(self):
        assert _extract_stage("en pre-seed") == "pre-seed"

    def test_serie_a(self):
        assert _extract_stage("levée série A") == "série a"

    def test_default_seed(self):
        assert _extract_stage("rien de spécial") == "seed"


class TestExtractSector:
    def test_fintech(self):
        assert _extract_sector("startup fintech") == "fintech"

    def test_saas(self):
        assert _extract_sector("une boîte SaaS") == "saas"

    def test_no_sector(self):
        assert _extract_sector("bonjour") == ""


class TestExtractCountry:
    def test_maroc(self):
        assert _extract_country("au Maroc") == "Maroc"

    def test_france(self):
        assert _extract_country("en France") == "France"

    def test_default_maroc(self):
        assert _extract_country("rien de spécial") == "Maroc"


class TestExtractAge:
    def test_2_ans(self):
        assert _extract_age("startup de 2 ans") == 2

    def test_5_ans(self):
        assert _extract_age("entreprise de 5 ans") == 5

    def test_no_age(self):
        assert _extract_age("startup fintech") is None


class TestExtractAmount:
    def test_5m(self):
        assert _extract_amount("cherche 5M MAD") == 5_000_000

    def test_500k(self):
        assert _extract_amount("levée de 500K") == 500_000

    def test_millions(self):
        assert _extract_amount("3 millions") == 3_000_000

    def test_no_amount(self):
        assert _extract_amount("cherche un investisseur") is None


# --- Full Router ---

class TestRoute:
    def test_scoring_route(self):
        result = route("Score de fundability : MRR: 8000, churn: 5%")
        assert result["intent"] == "scoring"
        assert "result" in result
        assert "score" in result["result"]

    def test_diagnostic_route(self):
        result = route("Diagnostic de mes KPIs : CAC: 200, LTV: 400")
        assert result["intent"] == "diagnostic"
        assert "result" in result

    def test_investors_route(self):
        result = route("Quels investisseurs pour une startup fintech seed au Maroc ?")
        assert result["intent"] == "investors"
        assert "result" in result
        assert result["result"]["total_found"] > 0

    def test_grants_route(self):
        result = route("Quelles subventions pour une startup edtech de 2 ans au Maroc ?")
        assert result["intent"] == "grants"
        assert "result" in result
        assert result["result"]["total_found"] > 0

    def test_qa_fallback(self):
        result = route("Comment valoriser ma startup en pré-seed ?")
        assert result["intent"] == "qa"
        assert "result" in result
        assert "answer" in result["result"]

    def test_scoring_error_without_metrics(self):
        result = route("Je veux mon score de fundability")
        assert result["intent"] == "scoring"
        assert "error" in result

    def test_startup_profile_used(self):
        """Profile data should supplement message data."""
        profile = {"sector": "fintech", "stage": "seed"}
        result = route("Quels investisseurs pour ma startup ?", startup_profile=profile)
        assert result["intent"] == "investors"
        assert result["result"]["total_found"] > 0

    def test_dev_plan_scenario_1(self):
        """Scenario 1: MRR 8K, burn 15K, churn 5%, stade seed → score ~58."""
        result = route("Score : MRR: 8000, burn rate: 15000, churn: 5%, stade seed")
        assert result["intent"] == "scoring"
        assert 0 < result["result"]["score"] <= 100

    def test_dev_plan_scenario_3(self):
        """Scenario 3: fintech, seed, Maroc, MRR 10K → top 5 investors."""
        result = route("Investisseurs pour fintech seed Maroc")
        assert result["intent"] == "investors"
        assert result["result"]["total_found"] > 0

    def test_dev_plan_scenario_4(self):
        """Scenario 4: edtech, 2 ans, Maroc → list of grants."""
        result = route("Subventions pour startup edtech de 2 ans au Maroc")
        assert result["intent"] == "grants"
        assert result["result"]["total_found"] > 0
