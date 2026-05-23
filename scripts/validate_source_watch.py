#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "skills" / "egypt-payment-guardian" / "references" / "provider-index.json"
BASELINE_PATH = ROOT / "docs" / "source-watch-baseline.json"
REPORT_PATH = ROOT / "docs" / "source-watch-report.md"
MAX_BASELINE_BYTES = 200_000
MAX_EXCERPT_CHARS = 600
ALLOWED_STATUSES = {"OK", "JS_CHALLENGE", "FAIL"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def read_json(path: Path) -> dict:
    if not path.exists():
        fail(f"Missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def provider_urls() -> set[str]:
    data = read_json(INDEX_PATH)
    urls: set[str] = set()
    for provider in data["providers"]:
        for url in provider["source_urls"]:
            urls.add(url)
    return urls


def validate_baseline() -> None:
    if BASELINE_PATH.stat().st_size > MAX_BASELINE_BYTES:
        fail("source-watch-baseline.json is too large; do not commit full provider docs")
    data = read_json(BASELINE_PATH)
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        fail("source-watch-baseline.json must contain a non-empty sources list")
    baseline_urls = {item.get("url") for item in sources}
    expected_urls = provider_urls()
    missing = sorted(expected_urls - baseline_urls)
    extra = sorted(baseline_urls - expected_urls)
    if missing:
        fail(f"Baseline missing provider URLs: {missing}")
    if extra:
        fail(f"Baseline has URLs no longer in provider-index.json: {extra}")
    for item in sources:
        url = item.get("url")
        status = item.get("status")
        if status not in ALLOWED_STATUSES:
            fail(f"{url} has invalid status {status}")
        excerpt = item.get("excerpt", "")
        if not isinstance(excerpt, str) or len(excerpt) > MAX_EXCERPT_CHARS:
            fail(f"{url} excerpt is missing or too long")
        forbidden_keys = {"content", "raw", "snapshot", "full_text", "html", "markdown"}
        if forbidden_keys & set(item):
            fail(f"{url} contains a forbidden full-doc key")
        if status == "OK" and not item.get("sha256"):
            fail(f"{url} OK record must include sha256")


def validate_report() -> None:
    if not REPORT_PATH.exists():
        fail("Missing docs/source-watch-report.md")
    if REPORT_PATH.stat().st_size > 100_000:
        fail("source-watch-report.md is too large; do not commit full provider docs")
    text = REPORT_PATH.read_text(encoding="utf-8")
    required = [
        "Source Watch Report",
        "Full provider docs are not committed",
    ]
    for phrase in required:
        if phrase not in text:
            fail(f"source-watch-report.md missing {phrase}")


def main() -> None:
    validate_baseline()
    validate_report()
    print("Source watch validation passed")


if __name__ == "__main__":
    main()
