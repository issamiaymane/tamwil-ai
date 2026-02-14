"""
Investor Matching for Tamwil AI.
Filters and ranks investors based on startup profile criteria.
"""

from backend.app.utils.data_loader import load_investors


def match_investors(
    sector: str,
    stage: str,
    geography: str,
    funding_amount: int = None,
    top_k: int = 5,
) -> dict:
    """Find the best matching investors for a startup profile.

    Args:
        sector: Startup sector, e.g. "fintech", "SaaS", "edtech"
        stage: Funding stage, e.g. "seed", "série A"
        geography: Target geography, e.g. "Maroc"
        funding_amount: Desired funding amount in local currency (optional)
        top_k: Number of results to return (default 5)

    Returns:
        Dict with matched investors sorted by relevance score.
    """
    investors = load_investors()
    sector_lower = sector.lower().strip()
    stage_lower = stage.lower().strip()
    geo_lower = geography.lower().strip()

    scored = []
    for inv in investors:
        score = 0
        reasons = []

        # Sector match
        inv_sectors = [s.lower() for s in inv.get("sectors", [])]
        if sector_lower in inv_sectors or any(sector_lower in s for s in inv_sectors):
            score += 1
            reasons.append(f"Secteur '{sector}' couvert")

        # Stage match
        inv_stages = [s.lower() for s in inv.get("stage", [])]
        if stage_lower in inv_stages:
            score += 1
            reasons.append(f"Stade '{stage}' ciblé")

        # Geography match
        inv_geo = [g.lower() for g in inv.get("geography", [])]
        if geo_lower in inv_geo or any(geo_lower in g for g in inv_geo):
            score += 1
            reasons.append(f"Géographie '{geography}' couverte")

        # Ticket range match
        if funding_amount is not None:
            t_min = inv.get("ticket_min") or 0
            t_max = inv.get("ticket_max") or float("inf")
            if t_min <= funding_amount <= t_max:
                score += 1
                t_max_str = f"{int(t_max):,}" if t_max != float("inf") else "∞"
                reasons.append(f"Ticket {int(t_min):,}-{t_max_str} {inv.get('currency', '')} compatible")

        # Only include investors with at least 1 match
        if score > 0:
            scored.append({
                "name": inv["name"],
                "type": inv.get("type", ""),
                "description": inv.get("description", ""),
                "sectors": inv.get("sectors", []),
                "stages": inv.get("stage", []),
                "ticket": f"{(inv.get('ticket_min') or 0):,} - {(inv.get('ticket_max') or 0):,} {inv.get('currency', '')}",
                "geography": inv.get("geography", []),
                "criteria": inv.get("criteria", {}).get("description", ""),
                "portfolio": inv.get("portfolio_examples", []),
                "contact": inv.get("contact", {}),
                "match_score": score,
                "match_reasons": reasons,
            })

    # Sort by score descending, then by name
    scored.sort(key=lambda x: (-x["match_score"], x["name"]))
    top_matches = scored[:top_k]

    return {
        "query": {
            "sector": sector,
            "stage": stage,
            "geography": geography,
            "funding_amount": funding_amount,
        },
        "total_found": len(scored),
        "showing": len(top_matches),
        "matches": top_matches,
    }


# --- Standalone test ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Tamwil AI — Investor Matching Test")
    print("=" * 60)
    print()

    result = match_investors("fintech", "seed", "Maroc", funding_amount=5000000)
    print(f"  Query: {result['query']}")
    print(f"  Found: {result['total_found']} investors, showing top {result['showing']}")
    print()

    for i, m in enumerate(result["matches"], 1):
        print(f"  [{i}] {m['name']} ({m['type']}) — score: {m['match_score']}/4")
        print(f"      Ticket: {m['ticket']}")
        print(f"      Raisons: {', '.join(m['match_reasons'])}")
        print()
