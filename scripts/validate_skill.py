#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "egypt-payment-guardian"
INDEX_PATH = SKILL_DIR / "references" / "provider-index.json"

REQUIRED_PROVIDER_HEADINGS = [
    "## Use When",
    "## Source Map",
    "## Integration Paths",
    "## Setup Prerequisites",
    "## Auth And Secret Boundary",
    "## Callback Or Webhook Contract",
    "## Signature Or HMAC",
    "## Idempotency Keys",
    "## Amount And Currency",
    "## Status Mapping",
    "## Refunds Voids And Subscriptions",
    "## Sandbox And Test Notes",
    "## Unknowns And Do Not Invent",
    "## Agent Checklist",
    "## Fail If",
]

REQUIRED_PROVIDER_FIELDS = [
    "id",
    "name",
    "category",
    "market",
    "priority",
    "readiness",
    "public_docs_status",
    "reference_file",
    "last_checked",
    "source_urls",
]

FORBIDDEN_MARKERS = [
    "TBD",
    "TODO",
    "FIXME",
    "lorem ipsum",
    "fill in later",
    "copy vendor docs here",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path} is not valid UTF-8: {exc}")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must close with ---")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def validate_skill_md() -> None:
    path = SKILL_DIR / "SKILL.md"
    if not path.exists():
        fail("Missing skills/egypt-payment-guardian/SKILL.md")
    text = read_text(path)
    frontmatter, body = parse_frontmatter(text)
    if set(frontmatter) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only name and description")
    if frontmatter["name"] != "egypt-payment-guardian":
        fail("Skill name must be egypt-payment-guardian")
    if not re.fullmatch(r"[a-z0-9-]+", frontmatter["name"]):
        fail("Skill name must use lowercase letters, digits, and hyphens only")
    if not frontmatter["description"].startswith("Use when "):
        fail('Skill description must start with "Use when "')
    if len(frontmatter["name"]) + len(frontmatter["description"]) > 1024:
        fail("Frontmatter name plus description is too long")
    required_refs = [
        "references/providers/paymob.md",
        "references/providers/fawrypay.md",
        "references/providers/geidea-egypt.md",
        "references/providers/easykash.md",
        "references/providers/kashier.md",
        "references/providers/paysky.md",
        "references/providers/egypt-bnpl-methods.md",
        "references/patterns/webhook-first-fulfillment.md",
        "references/patterns/idempotency-state-transitions.md",
        "references/patterns/server-secret-boundary.md",
        "references/patterns/private-docs-policy.md",
    ]
    for ref in required_refs:
        if ref not in body:
            fail(f"SKILL.md does not reference {ref}")


def validate_provider_index() -> None:
    if not INDEX_PATH.exists():
        fail("Missing provider-index.json")
    data = json.loads(read_text(INDEX_PATH))
    providers = data.get("providers")
    if not isinstance(providers, list) or not providers:
        fail("provider-index.json must contain a non-empty providers list")
    seen_ids: set[str] = set()
    for provider in providers:
        for field in REQUIRED_PROVIDER_FIELDS:
            if field not in provider:
                fail(f"Provider entry missing {field}: {provider}")
        provider_id = provider["id"]
        if provider_id in seen_ids:
            fail(f"Duplicate provider id: {provider_id}")
        seen_ids.add(provider_id)
        if not isinstance(provider["source_urls"], list) or not provider["source_urls"]:
            fail(f"{provider_id} must have source_urls")
        for url in provider["source_urls"]:
            if not isinstance(url, str) or not url.startswith("https://"):
                fail(f"{provider_id} has non-HTTPS or invalid source URL: {url}")
        ref_path = SKILL_DIR / provider["reference_file"]
        if not ref_path.exists():
            fail(f"{provider_id} reference file missing: {ref_path}")
        validate_provider_file(provider_id, ref_path)


def validate_provider_file(provider_id: str, path: Path) -> None:
    text = read_text(path)
    for heading in REQUIRED_PROVIDER_HEADINGS:
        if heading not in text:
            fail(f"{provider_id} missing heading {heading}")
    required_prefixes = [
        "- Provider:",
        "- Scope:",
        "- Priority:",
        "- Readiness:",
        "- Public docs status:",
        "- Last checked:",
        "- Source confidence:",
        "- Sources:",
    ]
    for prefix in required_prefixes:
        if prefix not in text:
            fail(f"{provider_id} missing metadata prefix {prefix}")


def validate_evals() -> None:
    scenarios = sorted((SKILL_DIR / "evals" / "scenarios").glob("*.md"))
    if len(scenarios) < 8:
        fail("Expected at least 8 eval scenarios")
    for path in scenarios:
        text = read_text(path)
        for heading in ["## User Prompt", "## Required Skill Use", "## Expected Agent Behavior", "## Fail If"]:
            if heading not in text:
                fail(f"{path} missing {heading}")


def scan_for_forbidden_markers() -> None:
    for path in ROOT.rglob("*"):
        if path.is_dir():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".yml", ".yaml"}:
            continue
        text = read_text(path)
        lower = text.lower()
        for marker in FORBIDDEN_MARKERS:
            if marker.lower() in lower:
                fail(f"{path} contains forbidden marker {marker}")


def main() -> None:
    validate_skill_md()
    validate_provider_index()
    validate_evals()
    scan_for_forbidden_markers()
    print("Skill validation passed")


if __name__ == "__main__":
    main()
