"""Tests for the financial diagnostic module."""

import pytest
from backend.app.modules.diagnostic import diagnose_kpis


class TestDiagnoseKpis:
    def test_returns_dict_with_required_keys(self):
        result = diagnose_kpis({"CAC": 200}, "seed")
        assert "stage" in result
        assert "metrics_analyzed" in result
        assert "summary" in result
        assert "analyses" in result

    def test_metrics_analyzed_count(self):
        result = diagnose_kpis({"CAC": 200, "LTV": 400, "CHURN_RATE": 8}, "seed")
        assert result["metrics_analyzed"] == 3

    def test_analysis_has_correct_fields(self):
        result = diagnose_kpis({"CAC": 200}, "seed")
        a = result["analyses"][0]
        assert "metric" in a
        assert "name_fr" in a
        assert "value" in a
        assert "level" in a
        assert "benchmark" in a
        assert "interpretation" in a
        assert "improvement_tips" in a

    def test_unknown_metric_ignored(self):
        result = diagnose_kpis({"FAKE_KPI": 999}, "seed")
        assert result["metrics_analyzed"] == 0

    def test_summary_healthy(self):
        """All good/excellent metrics should give healthy summary."""
        result = diagnose_kpis({"CAC": 50}, "seed")  # excellent CAC
        assert any(word in result["summary"].lower() for word in ["bonne", "correcte"])

    def test_summary_critical(self):
        """Multiple bad metrics should give critical summary."""
        result = diagnose_kpis({"CAC": 2000, "LTV": 100, "CHURN_RATE": 15}, "seed")
        assert "critique" in result["summary"].lower() or "plan d'action" in result["summary"].lower()

    def test_dev_plan_scenario(self):
        """Test scenario from DEVELOPMENT_PLAN.md: CAC 200, LTV 400, churn 8%."""
        result = diagnose_kpis({"CAC": 200, "LTV": 400, "CHURN_RATE": 8}, "seed")
        assert result["metrics_analyzed"] == 3

        levels = {a["metric"]: a["level"] for a in result["analyses"]}
        # LTV 400 at seed (bad < 2000) should be bad
        assert levels["LTV"] == "bad"
        # Churn 8% at seed (bad > 7%) should be bad
        assert levels["CHURN_RATE"] == "bad"

    def test_stage_affects_results(self):
        """Same value should classify differently at different stages."""
        r_preseed = diagnose_kpis({"MRR": 3000}, "pre-seed")
        r_serie_a = diagnose_kpis({"MRR": 3000}, "série a")

        level_preseed = r_preseed["analyses"][0]["level"]
        level_serie_a = r_serie_a["analyses"][0]["level"]
        # 3000 MRR is good at pre-seed but bad at série A
        assert level_preseed in ("good", "excellent")
        assert level_serie_a == "bad"

    def test_improvement_tips_present(self):
        result = diagnose_kpis({"CHURN_RATE": 15}, "seed")
        tips = result["analyses"][0]["improvement_tips"]
        assert len(tips) > 0
