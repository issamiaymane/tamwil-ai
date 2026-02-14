"""Tests for the fundability scoring module."""

import pytest
from backend.app.modules.scoring import (
    score_fundability,
    _parse_number,
    _classify_value,
    LEVEL_SCORES,
    INVERTED_METRICS,
)


# --- _parse_number ---

class TestParseNumber:
    def test_simple_integer(self):
        assert _parse_number("500") == 500

    def test_currency_with_symbol(self):
        assert _parse_number("<500€") == 500

    def test_currency_with_spaces(self):
        assert _parse_number("5 000€/mois") == 5000

    def test_percentage(self):
        assert _parse_number("5-10% MoM") == 5

    def test_ratio(self):
        assert _parse_number(">3x") == 3

    def test_empty_string(self):
        assert _parse_number("") is None

    def test_no_numbers(self):
        assert _parse_number("N/A") is None


# --- _classify_value ---

class TestClassifyValue:
    def test_normal_metric_excellent(self):
        benchmarks = {"bad": "<500", "ok": "500-2000", "good": "2000-5000", "excellent": ">5000"}
        assert _classify_value(6000, benchmarks, "MRR") == "excellent"

    def test_normal_metric_good(self):
        benchmarks = {"bad": "<500", "ok": "500-2000", "good": "2000-5000", "excellent": ">5000"}
        assert _classify_value(3000, benchmarks, "MRR") == "good"

    def test_normal_metric_ok(self):
        benchmarks = {"bad": "<500", "ok": "500-2000", "good": "2000-5000", "excellent": ">5000"}
        assert _classify_value(1000, benchmarks, "MRR") == "ok"

    def test_normal_metric_bad(self):
        benchmarks = {"bad": "<500", "ok": "500-2000", "good": "2000-5000", "excellent": ">5000"}
        assert _classify_value(100, benchmarks, "MRR") == "bad"

    def test_inverted_metric_excellent(self):
        """For CAC/churn, lower is better."""
        benchmarks = {"bad": ">1000", "ok": "400-1000", "good": "100-400", "excellent": "<100"}
        assert _classify_value(50, benchmarks, "CAC") == "excellent"

    def test_inverted_metric_bad(self):
        benchmarks = {"bad": ">1000", "ok": "400-1000", "good": "100-400", "excellent": "<100"}
        assert _classify_value(1500, benchmarks, "CAC") == "bad"

    def test_inverted_churn(self):
        benchmarks = {"bad": ">7%", "ok": "4-7%", "good": "2-4%", "excellent": "<2%"}
        assert _classify_value(1, benchmarks, "CHURN_RATE") == "excellent"


# --- score_fundability ---

class TestScoreFundability:
    def test_returns_dict_with_required_keys(self):
        result = score_fundability({"MRR": 8000}, "seed")
        assert "score" in result
        assert "breakdown" in result
        assert "strengths" in result
        assert "weaknesses" in result
        assert "action_plan" in result

    def test_score_is_between_0_and_100(self):
        result = score_fundability({"MRR": 8000, "CAC": 200}, "seed")
        assert 0 <= result["score"] <= 100

    def test_metrics_evaluated_count(self):
        result = score_fundability({"MRR": 8000, "CAC": 200, "CHURN_RATE": 5}, "seed")
        assert result["metrics_evaluated"] == 3

    def test_unknown_metric_ignored(self):
        result = score_fundability({"FAKE_METRIC": 999}, "seed")
        assert result["metrics_evaluated"] == 0
        assert result["score"] == 0

    def test_stage_normalization(self):
        r1 = score_fundability({"MRR": 8000}, "seed")
        r2 = score_fundability({"MRR": 8000}, "Seed")
        assert r1["score"] == r2["score"]

    def test_pre_seed_stage(self):
        result = score_fundability({"MRR": 3000}, "pre-seed")
        assert result["metrics_evaluated"] == 1
        # 3000 MRR at pre-seed should be good (2000-5000 range)
        assert result["breakdown"][0]["level"] == "good"

    def test_excellent_metrics_in_strengths(self):
        # Very high MRR at pre-seed should be excellent
        result = score_fundability({"MRR": 50000}, "pre-seed")
        assert len(result["strengths"]) > 0

    def test_bad_metrics_in_weaknesses(self):
        result = score_fundability({"CHURN_RATE": 15}, "seed")
        assert len(result["weaknesses"]) > 0

    def test_action_plan_generated_for_weaknesses(self):
        result = score_fundability({"CHURN_RATE": 15}, "seed")
        assert result["action_plan"] != ""

    def test_breakdown_has_correct_fields(self):
        result = score_fundability({"MRR": 8000}, "seed")
        b = result["breakdown"][0]
        assert "metric" in b
        assert "name_fr" in b
        assert "value" in b
        assert "level" in b
        assert "weight" in b

    def test_dev_plan_scenario(self):
        """Test scenario from DEVELOPMENT_PLAN.md: MRR 8K, burn 15K, churn 5%, stade seed."""
        result = score_fundability(
            {"MRR": 8000, "BURN_RATE": 15000, "CHURN_RATE": 5},
            "seed",
        )
        assert result["score"] > 0
        assert result["metrics_evaluated"] == 3
