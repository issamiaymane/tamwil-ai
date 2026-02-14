"""
Fundability Scoring for Tamwil AI.
Compares user metrics to stage-specific benchmarks and computes a weighted score /100.
"""

import re
from backend.app.utils.data_loader import load_metrics


# Benchmark level → numeric score
LEVEL_SCORES = {"bad": 25, "ok": 50, "good": 75, "excellent": 100}

# Stage name normalization (user input → JSON key)
STAGE_MAP = {
    "pre-seed": "pre_seed", "pre_seed": "pre_seed", "preseed": "pre_seed",
    "seed": "seed",
    "série a": "serie_a", "serie a": "serie_a", "serie_a": "serie_a", "series a": "serie_a",
    "série b": "serie_b", "serie b": "serie_b", "serie_b": "serie_b",
    "série b+": "serie_b", "series b": "serie_b", "growth": "serie_b",
}

# Metrics where lower is better (inverted)
INVERTED_METRICS = {"CAC", "CHURN_RATE", "BURN_RATE", "PAYBACK_PERIOD"}


def _parse_number(text: str) -> float | None:
    """Extract a numeric value from a benchmark string like '<500€/mois' or '5-10% MoM'."""
    text = text.replace("\u202f", "").replace("\xa0", "").replace(" ", "")
    numbers = re.findall(r"[\d]+(?:[.,]\d+)?", text.replace(",", "."))
    if numbers:
        return float(numbers[0].replace(",", "."))
    return None


def _classify_value(value: float, benchmarks: dict, metric_id: str) -> str:
    """Classify a metric value as bad/ok/good/excellent based on benchmarks."""
    inverted = metric_id in INVERTED_METRICS

    # Parse thresholds from benchmark strings
    bad_val = _parse_number(benchmarks.get("bad", ""))
    ok_val = _parse_number(benchmarks.get("ok", ""))
    good_val = _parse_number(benchmarks.get("good", ""))
    excellent_val = _parse_number(benchmarks.get("excellent", ""))

    if inverted:
        # Lower is better: excellent < good < ok < bad
        if excellent_val is not None and value <= excellent_val:
            return "excellent"
        if good_val is not None and value <= good_val:
            return "good"
        if ok_val is not None and value <= ok_val:
            return "ok"
        return "bad"
    else:
        # Higher is better: bad < ok < good < excellent
        if excellent_val is not None and value >= excellent_val:
            return "excellent"
        if good_val is not None and value >= good_val:
            return "good"
        if ok_val is not None and value >= ok_val:
            return "ok"
        return "bad"


def score_fundability(user_metrics: dict, stage: str) -> dict:
    """Compute a fundability score /100 based on user metrics vs benchmarks.

    Args:
        user_metrics: Dict of metric_id → value, e.g. {"MRR": 8000, "CHURN_RATE": 5}
        stage: Startup stage, e.g. "seed", "pre-seed", "série a"

    Returns:
        Dict with score, breakdown, strengths, weaknesses, action_plan.
    """
    stage_key = STAGE_MAP.get(stage.lower().strip(), "seed")
    metrics_ref = {m["id"]: m for m in load_metrics()}

    breakdown = []
    total_weighted_score = 0
    total_weight = 0
    strengths = []
    weaknesses = []
    all_tips = []

    for metric_id, value in user_metrics.items():
        metric_id_upper = metric_id.upper().replace(" ", "_")
        ref = metrics_ref.get(metric_id_upper)
        if not ref:
            continue

        benchmarks = ref.get("benchmarks", {}).get(stage_key)
        if not benchmarks:
            continue

        level = _classify_value(value, benchmarks, metric_id_upper)
        level_score = LEVEL_SCORES[level]
        weight = ref.get("weight_in_scoring", 0.1)

        total_weighted_score += level_score * weight
        total_weight += weight

        entry = {
            "metric": metric_id_upper,
            "name_fr": ref.get("name_fr", ref["name"]),
            "value": value,
            "level": level,
            "level_score": level_score,
            "weight": weight,
            "benchmark": benchmarks,
        }
        breakdown.append(entry)

        if level in ("good", "excellent"):
            strengths.append(f"{ref.get('name_fr', ref['name'])} : {level} ({value})")
        else:
            weaknesses.append(f"{ref.get('name_fr', ref['name'])} : {level} ({value})")
            all_tips.extend(ref.get("improvement_tips", [])[:2])

    final_score = round(total_weighted_score / total_weight) if total_weight > 0 else 0

    # Action plan from static tips (no LLM needed)
    action_plan = ""
    if weaknesses:
        action_plan = "Plan d'action recommandé :\n"
        for i, tip in enumerate(all_tips[:5], 1):
            action_plan += f"  {i}. {tip}\n"

    return {
        "score": final_score,
        "stage": stage,
        "metrics_evaluated": len(breakdown),
        "breakdown": breakdown,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "action_plan": action_plan,
    }


# --- Standalone test ---
if __name__ == "__main__":
    test_metrics = {
        "MRR": 8000,
        "BURN_RATE": 15000,
        "CHURN_RATE": 5,
        "CAC": 200,
        "LTV": 2000,
    }

    print("=" * 60)
    print("  Tamwil AI — Fundability Scoring Test")
    print("=" * 60)
    print()

    result = score_fundability(test_metrics, "seed")
    print(f"  Score: {result['score']}/100")
    print(f"  Stage: {result['stage']}")
    print(f"  Metrics evaluated: {result['metrics_evaluated']}")
    print()

    print("  Breakdown:")
    for b in result["breakdown"]:
        print(f"    - {b['name_fr']}: {b['value']} → {b['level']} ({b['level_score']}/100)")
    print()

    if result["strengths"]:
        print("  Forces:")
        for s in result["strengths"]:
            print(f"    + {s}")
    if result["weaknesses"]:
        print("  Faiblesses:")
        for w in result["weaknesses"]:
            print(f"    - {w}")
    print()

    if result["action_plan"]:
        print(f"  {result['action_plan']}")
