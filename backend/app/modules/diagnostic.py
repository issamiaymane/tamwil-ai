"""
Financial Diagnostic for Tamwil AI.
Analyzes individual KPIs against stage benchmarks and provides recommendations.
"""

from backend.app.utils.data_loader import load_metrics
from backend.app.modules.scoring import _classify_value, STAGE_MAP


def diagnose_kpis(kpis: dict, stage: str) -> dict:
    """Analyze user KPIs against stage-specific benchmarks.

    Args:
        kpis: Dict of metric_id → value, e.g. {"CAC": 200, "LTV": 400, "CHURN_RATE": 8}
        stage: Startup stage, e.g. "seed"

    Returns:
        Dict with per-metric analysis including level, interpretation, and tips.
    """
    stage_key = STAGE_MAP.get(stage.lower().strip(), "seed")
    metrics_ref = {m["id"]: m for m in load_metrics()}

    analyses = []
    for metric_id, value in kpis.items():
        metric_id_upper = metric_id.upper().replace(" ", "_")
        ref = metrics_ref.get(metric_id_upper)
        if not ref:
            continue

        benchmarks = ref.get("benchmarks", {}).get(stage_key)
        if not benchmarks:
            continue

        level = _classify_value(value, benchmarks, metric_id_upper)

        analyses.append({
            "metric": metric_id_upper,
            "name_fr": ref.get("name_fr", ref["name"]),
            "value": value,
            "unit": ref.get("unit", ""),
            "level": level,
            "benchmark": benchmarks,
            "definition": ref.get("definition", ""),
            "formula": ref.get("formula", ""),
            "interpretation": ref.get("interpretation", ""),
            "improvement_tips": ref.get("improvement_tips", []),
            "related_metrics": ref.get("related_metrics", []),
        })

    # Summary
    levels = [a["level"] for a in analyses]
    summary = ""
    if levels:
        n_good = sum(1 for l in levels if l in ("good", "excellent"))
        n_bad = sum(1 for l in levels if l == "bad")
        if n_bad == 0:
            summary = "Votre startup est en bonne santé financière sur les métriques analysées."
        elif n_bad <= len(levels) // 2:
            summary = "Quelques indicateurs nécessitent votre attention, mais la situation globale est correcte."
        else:
            summary = "Plusieurs indicateurs sont en zone critique. Un plan d'action est recommandé."

    return {
        "stage": stage,
        "metrics_analyzed": len(analyses),
        "summary": summary,
        "analyses": analyses,
    }


# --- Standalone test ---
if __name__ == "__main__":
    test_kpis = {"CAC": 200, "LTV": 400, "CHURN_RATE": 8}

    print("=" * 60)
    print("  Tamwil AI — Financial Diagnostic Test")
    print("=" * 60)
    print()

    result = diagnose_kpis(test_kpis, "seed")
    print(f"  Stage: {result['stage']}")
    print(f"  Summary: {result['summary']}")
    print()

    for a in result["analyses"]:
        print(f"  {a['name_fr']} ({a['metric']})")
        print(f"    Valeur: {a['value']} → {a['level']}")
        print(f"    Benchmark: {a['benchmark']}")
        if a["improvement_tips"]:
            print(f"    Conseils:")
            for tip in a["improvement_tips"][:2]:
                print(f"      - {tip}")
        print()
