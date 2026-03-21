"""
Mapping of dataset source filenames to their real internet URLs.
Update each URL to point to the actual online reference.
"""

SOURCE_URLS: dict[str, str] = {
    # Fundraising guides
    "pitch_deck.md": "",
    "etapes_levee.md": "",
    "valorisation.md": "",
    "term_sheet.md": "",
    "types_financement.md": "",
    "erreurs_courantes.md": "",

    # Regulations
    "rgpd.md": "https://www.cndp.ma/fr/",
    "fintech_maroc.md": "",
    "fiscalite_startup.md": "",
    "creation_entreprise_maroc.md": "",

    # JSON data sources
    "faq.json": "",
    "investors.json": "",
    "grants.json": "",
    "metrics_reference.json": "",
}


SEARCH_QUERIES: dict[str, str] = {
    "pitch_deck.md": "comment préparer un pitch deck startup",
    "etapes_levee.md": "étapes levée de fonds startup Maroc",
    "valorisation.md": "valorisation startup méthodes calcul",
    "term_sheet.md": "term sheet startup clauses importantes",
    "types_financement.md": "types de financement startup Afrique",
    "erreurs_courantes.md": "erreurs courantes levée de fonds startup",
    "fintech_maroc.md": "réglementation fintech Maroc Bank Al-Maghrib",
    "fiscalite_startup.md": "fiscalité startup Maroc avantages fiscaux",
    "creation_entreprise_maroc.md": "création entreprise Maroc procédure",
    "faq.json": "financement startup Maroc FAQ",
    "investors.json": "investisseurs startups Maroc Afrique",
    "grants.json": "subventions aides startups Maroc",
    "metrics_reference.json": "métriques KPI startup SaaS",
}


def get_source_url(filename: str) -> str:
    """Return the mapped URL or a Google search URL as fallback."""
    url = SOURCE_URLS.get(filename, "")
    if url:
        return url
    query = SEARCH_QUERIES.get(filename, filename.replace("_", " ").replace(".md", "").replace(".json", "") + " startup Maroc")
    return f"https://www.google.com/search?q={query.replace(' ', '+')}"
