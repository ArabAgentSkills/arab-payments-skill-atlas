#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

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


def skill_dirs() -> list[Path]:
    dirs = sorted(path for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").exists())
    if not dirs:
        fail("No installable skills found under skills/")
    return dirs


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)} frontmatter must close with ---")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line in {path.relative_to(ROOT)}: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def validate_skill_md(skill_dir: Path, providers: list[dict[str, object]]) -> None:
    path = skill_dir / "SKILL.md"
    if not path.exists():
        fail(f"Missing {path.relative_to(ROOT)}")
    text = read_text(path)
    frontmatter, body = parse_frontmatter(text, path)
    if set(frontmatter) != {"name", "description"}:
        fail(f"{path.relative_to(ROOT)} frontmatter must contain only name and description")
    if frontmatter["name"] != skill_dir.name:
        fail(f"{path.relative_to(ROOT)} name must be {skill_dir.name}")
    if not re.fullmatch(r"[a-z0-9-]+", frontmatter["name"]):
        fail(f"{path.relative_to(ROOT)} name must use lowercase letters, digits, and hyphens only")
    if not frontmatter["description"].startswith("Use when "):
        fail(f'{path.relative_to(ROOT)} description must start with "Use when "')
    if len(frontmatter["name"]) + len(frontmatter["description"]) > 1024:
        fail(f"{path.relative_to(ROOT)} frontmatter name plus description is too long")
    required_refs = [str(provider["reference_file"]) for provider in providers]
    required_refs.extend(path.relative_to(skill_dir).as_posix() for path in sorted((skill_dir / "references" / "patterns").glob("*.md")))
    for ref in required_refs:
        if ref not in body:
            fail(f"{path.relative_to(ROOT)} does not reference {ref}")


def load_provider_index(skill_dir: Path) -> list[dict[str, object]]:
    index_path = skill_dir / "references" / "provider-index.json"
    if not index_path.exists():
        fail(f"Missing {index_path.relative_to(ROOT)}")
    data = json.loads(read_text(index_path))
    if data.get("skill") != skill_dir.name:
        fail(f"{index_path.relative_to(ROOT)} skill must be {skill_dir.name}")
    providers = data.get("providers")
    if not isinstance(providers, list) or not providers:
        fail(f"{index_path.relative_to(ROOT)} must contain a non-empty providers list")
    return providers


def validate_provider_index(skill_dir: Path, providers: list[dict[str, object]]) -> None:
    seen_ids: set[str] = set()
    for provider in providers:
        for field in REQUIRED_PROVIDER_FIELDS:
            if field not in provider:
                fail(f"{skill_dir.name} provider entry missing {field}: {provider}")
        provider_id = str(provider["id"])
        if provider_id in seen_ids:
            fail(f"{skill_dir.name} duplicate provider id: {provider_id}")
        seen_ids.add(provider_id)
        if not isinstance(provider["source_urls"], list) or not provider["source_urls"]:
            fail(f"{provider_id} must have source_urls")
        for url in provider["source_urls"]:
            if not isinstance(url, str) or not url.startswith("https://"):
                fail(f"{skill_dir.name}:{provider_id} has non-HTTPS or invalid source URL: {url}")
        ref_path = skill_dir / str(provider["reference_file"])
        if not ref_path.exists():
            fail(f"{skill_dir.name}:{provider_id} reference file missing: {ref_path}")
        validate_provider_file(f"{skill_dir.name}:{provider_id}", ref_path)


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


def validate_evals(skill_dir: Path) -> None:
    scenarios = sorted((skill_dir / "evals" / "scenarios").glob("*.md"))
    if len(scenarios) < 8:
        fail(f"{skill_dir.name} expected at least 8 eval scenarios")
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
    for skill_dir in skill_dirs():
        providers = load_provider_index(skill_dir)
        validate_skill_md(skill_dir, providers)
        validate_provider_index(skill_dir, providers)
        validate_evals(skill_dir)
    scan_for_forbidden_markers()
    print("Skill validation passed")


if __name__ == "__main__":
    main()
