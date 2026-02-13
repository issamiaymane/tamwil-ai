"""
Data loader for Tamwil AI.
Loads and validates all JSON and Markdown data files.
Used by all modules to access the knowledge base.
"""

import json
import logging
from pathlib import Path
from backend.app.config import (
    INVESTORS_PATH,
    GRANTS_PATH,
    METRICS_PATH,
    FAQ_PATH,
    FUNDRAISING_GUIDE_DIR,
    REGULATIONS_DIR,
)

logger = logging.getLogger(__name__)

# Required fields per record type
INVESTOR_REQUIRED = {"id", "name", "type", "sectors", "stage", "ticket_min", "ticket_max", "currency", "geography"}
GRANT_REQUIRED = {"id", "name", "country", "organization", "type", "amount_min", "amount_max", "currency", "eligibility"}
METRIC_REQUIRED = {"id", "name", "definition", "formula", "unit", "benchmarks"}
FAQ_REQUIRED = {"id", "categorie", "question", "reponse"}


def _load_json(path: Path, required_fields: set, label: str) -> list[dict]:
    """Load a JSON array file and validate each record has required fields."""
    if not path.exists():
        logger.error(f"[{label}] File not found: {path}")
        return []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        logger.error(f"[{label}] Expected JSON array, got {type(data).__name__}")
        return []

    valid_records = []
    for i, record in enumerate(data):
        missing = required_fields - set(record.keys())
        if missing:
            logger.warning(f"[{label}][{i}] id={record.get('id', '?')} missing fields: {missing}")
        valid_records.append(record)

    logger.info(f"[{label}] Loaded {len(valid_records)} records from {path.name}")
    return valid_records


def _load_markdown_files(directory: Path, label: str) -> list[dict]:
    """Load all .md files from a directory. Returns list of {filename, path, content}."""
    if not directory.exists():
        logger.error(f"[{label}] Directory not found: {directory}")
        return []

    documents = []
    for md_file in sorted(directory.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        if not content.strip():
            logger.warning(f"[{label}] Empty file: {md_file.name}")
            continue
        documents.append({
            "filename": md_file.name,
            "path": str(md_file),
            "content": content,
        })

    logger.info(f"[{label}] Loaded {len(documents)} markdown files from {directory.name}/")
    return documents


# --- Public API: call these from any module ---

def load_investors() -> list[dict]:
    return _load_json(INVESTORS_PATH, INVESTOR_REQUIRED, "investors")


def load_grants() -> list[dict]:
    return _load_json(GRANTS_PATH, GRANT_REQUIRED, "grants")


def load_metrics() -> list[dict]:
    return _load_json(METRICS_PATH, METRIC_REQUIRED, "metrics")


def load_faq() -> list[dict]:
    return _load_json(FAQ_PATH, FAQ_REQUIRED, "faq")


def load_fundraising_guides() -> list[dict]:
    return _load_markdown_files(FUNDRAISING_GUIDE_DIR, "fundraising_guide")


def load_regulations() -> list[dict]:
    return _load_markdown_files(REGULATIONS_DIR, "regulations")


def load_all() -> dict:
    """Load all data sources at once. Returns a dict with all datasets."""
    return {
        "investors": load_investors(),
        "grants": load_grants(),
        "metrics": load_metrics(),
        "faq": load_faq(),
        "fundraising_guides": load_fundraising_guides(),
        "regulations": load_regulations(),
    }


# --- Standalone: run this file directly to validate ---
if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    print("=" * 60)
    print("  Tamwil AI — Data Validation")
    print("=" * 60)
    print()

    data = load_all()
    has_errors = False

    for key, records in data.items():
        count = len(records)
        status = "PASS" if count > 0 else "FAIL"
        if count == 0:
            has_errors = True
        print(f"  [{status}] {key}: {count} items loaded")

    print()
    print("=" * 60)
    if has_errors:
        print("  RESULT: Some datasets failed to load. Check logs above.")
        sys.exit(1)
    else:
        print("  RESULT: All data validated successfully!")
        sys.exit(0)
