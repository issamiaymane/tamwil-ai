"""
Grant/Subsidy Matching for Tamwil AI.
Filters grants based on startup eligibility criteria.
"""

import re
from backend.app.utils.data_loader import load_grants


def _parse_age_max(age_str: str) -> int | None:
    """Parse age string like '5 ans' into integer years."""
    if not age_str or age_str == "N/A":
        return None
    match = re.search(r"(\d+)", str(age_str))
    return int(match.group(1)) if match else None


def match_grants(
    sector: str,
    stage: str,
    country: str,
    company_age: int = None,
) -> dict:
    """Find eligible grants for a startup profile.

    Args:
        sector: Startup sector, e.g. "fintech", "edtech"
        stage: Startup stage, e.g. "seed", "pre-seed"
        country: Startup country, e.g. "Maroc", "France"
        company_age: Age of the company in years (optional)

    Returns:
        Dict with matched grants.
    """
    grants = load_grants()
    sector_lower = sector.lower().strip()
    stage_lower = stage.lower().strip()
    country_lower = country.lower().strip()

    matches = []
    for g in grants:
        eligibility = g.get("eligibility", {})
        reasons = []

        # Country match
        g_country = g.get("country", "").lower()
        if g_country != country_lower and g_country != "international":
            continue

        # Stage match
        elig_stages = [s.lower() for s in eligibility.get("stage", [])]
        if elig_stages and stage_lower not in elig_stages:
            continue
        reasons.append(f"Stade '{stage}' éligible")

        # Sector match — "tous secteurs" or "all" matches everything
        elig_sectors = [s.lower() for s in eligibility.get("sectors", [])]
        sector_ok = (
            not elig_sectors
            or any("tous" in s or "all" in s for s in elig_sectors)
            or sector_lower in elig_sectors
            or any(sector_lower in s for s in elig_sectors)
        )
        if not sector_ok:
            continue
        reasons.append(f"Secteur '{sector}' couvert")

        # Age check
        age_max = _parse_age_max(eligibility.get("age_max_company", ""))
        if company_age is not None and age_max is not None:
            if company_age > age_max:
                continue
            reasons.append(f"Âge ({company_age} ans) ≤ max ({age_max} ans)")

        amount = f"{(g.get('amount_min') or 0):,} - {(g.get('amount_max') or 0):,} {g.get('currency', '')}"

        matches.append({
            "name": g["name"],
            "organization": g.get("organization", ""),
            "country": g.get("country", ""),
            "type": g.get("type", ""),
            "description": g.get("description", ""),
            "amount": amount,
            "amount_min": g.get("amount_min", 0),
            "amount_max": g.get("amount_max", 0),
            "currency": g.get("currency", ""),
            "conditions": eligibility.get("conditions", []),
            "deadline": g.get("deadline_type", g.get("deadline", "N/A")),
            "website": g.get("website", ""),
            "application_process": g.get("application_process", ""),
            "match_reasons": reasons,
        })

    return {
        "query": {
            "sector": sector,
            "stage": stage,
            "country": country,
            "company_age": company_age,
        },
        "total_found": len(matches),
        "matches": matches,
    }


# --- Standalone test ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Tamwil AI — Grant Matching Test")
    print("=" * 60)
    print()

    result = match_grants("edtech", "seed", "Maroc", company_age=2)
    print(f"  Query: {result['query']}")
    print(f"  Found: {result['total_found']} grants")
    print()

    for i, m in enumerate(result["matches"], 1):
        print(f"  [{i}] {m['name']} — {m['organization']}")
        print(f"      Type: {m['type']} | Montant: {m['amount']}")
        print(f"      Raisons: {', '.join(m['match_reasons'])}")
        print()
