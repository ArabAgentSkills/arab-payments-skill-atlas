#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SKILL = "skills/egypt-payment-guardian/SKILL.md"

ADAPTERS = [
    ROOT / "AGENTS.md",
    ROOT / "CLAUDE.md",
    ROOT / ".cursor" / "rules" / "egypt-payment-guardian.mdc",
    ROOT / ".github" / "copilot-instructions.md",
    ROOT / "adapters" / "generic" / "EGYPT_PAYMENT_GUARDIAN_PROMPT.md",
]

REQUIRED_PHRASES = [
    "Never trust redirect alone",
    "Verify signature, HMAC, or SecureHash",
    "Keep payment secrets server-side",
    "Compare amount, currency, order reference, and provider reference",
    "Process callbacks and retries idempotently",
]

FORBIDDEN_MARKERS = [
    "TBD",
    "TODO",
    "FIXME",
    "lorem ipsum",
    "fill in later",
    "copy vendor docs here",
]

SECRET_PATTERNS = [
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("assigned secret", re.compile(r"(secret|hmac|api[_-]?key|authorization)\s*[:=]\s*[A-Za-z0-9._:/+=-]{24,}", re.IGNORECASE)),
    ("live payment key", re.compile(r"\b[psrk]k_live_[0-9A-Za-z]{16,}\b")),
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
        fail("Cursor adapter must start with MDC frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("Cursor adapter frontmatter must close with ---")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid Cursor frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def validate_adapter(path: Path) -> None:
    if not path.exists():
        fail(f"Missing adapter file: {path.relative_to(ROOT)}")
    text = read_text(path)
    display = str(path.relative_to(ROOT))
    if CANONICAL_SKILL not in text:
        fail(f"{display} must reference {CANONICAL_SKILL}")
    for phrase in REQUIRED_PHRASES:
        if phrase not in text:
            fail(f"{display} missing non-negotiable phrase: {phrase}")
    lower = text.lower()
    for marker in FORBIDDEN_MARKERS:
        if marker.lower() in lower:
            fail(f"{display} contains forbidden marker {marker}")
    for label, pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"{display} contains possible {label}")


def validate_cursor_rule() -> None:
    path = ROOT / ".cursor" / "rules" / "egypt-payment-guardian.mdc"
    text = read_text(path)
    frontmatter, _body = parse_frontmatter(text)
    expected_keys = {"description", "globs", "alwaysApply"}
    if set(frontmatter) != expected_keys:
        fail("Cursor adapter frontmatter must contain description, globs, and alwaysApply only")
    if not frontmatter["description"].startswith("Use when "):
        fail('Cursor adapter description must start with "Use when "')
    if frontmatter["globs"] != "":
        fail("Cursor adapter globs must be empty for Agent Requested behavior")
    if frontmatter["alwaysApply"] != "false":
        fail("Cursor adapter alwaysApply must be false")


def validate_docs() -> None:
    path = ROOT / "docs" / "agent-compatibility.md"
    if not path.exists():
        fail("Missing docs/agent-compatibility.md")
    text = read_text(path)
    required = [
        "Codex",
        "Claude Code",
        "Cursor",
        "GitHub Copilot",
        "OpenClaw",
        "Hermes",
        "adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md",
    ]
    for item in required:
        if item not in text:
            fail(f"agent compatibility docs missing {item}")
    readme = read_text(ROOT / "README.md")
    if "# Arab Payments Skill Atlas" not in readme:
        fail("README must use Arab Payments Skill Atlas as the public project title")
    if "V1 ships with Egypt Payment Guardian" not in readme:
        fail("README must state that V1 ships with Egypt Payment Guardian")
    if "V1 is Egypt-only" not in readme:
        fail("README must make the Egypt-only V1 scope explicit")
    if "Created by Mohamed Waleed and Fady Azzouny with the help of Codex GPT-5.5" not in readme:
        fail("README must include the approved co-creator credit")
    if "https://github.com/ArabAgentSkills/arab-payments-skill-atlas" not in readme:
        fail("README must include the approved public repository URL")
    if "--include-global-codex" not in readme:
        fail("README must document explicit --include-global-codex behavior")
    if "Until the public repository and first GitHub release exist" not in readme:
        fail("README must state latest-release updates are unavailable before first release")
    if "--agent all --target" not in readme:
        fail("README must document project-local all-agent install")
    if "--agent codex --dry-run" not in readme:
        fail("README must include a dedicated Codex updater dry-run check")
    if "--include-global-codex" not in text:
        fail("agent compatibility docs must document explicit global Codex opt-in")
    version = json.loads(read_text(ROOT / "skill-version.json"))
    if version.get("name") != "egypt-payment-guardian":
        fail("skill-version.json must keep the installed skill name as egypt-payment-guardian")
    if version.get("package_name") != "arab-payments-skill-atlas":
        fail("skill-version.json must include package_name arab-payments-skill-atlas")
    if version.get("canonical_repo_url") != "https://github.com/ArabAgentSkills/arab-payments-skill-atlas":
        fail("skill-version.json must use the ArabAgentSkills canonical repo URL")
    updater = read_text(ROOT / "scripts" / "install_or_update_skill.py")
    if "package_title" not in updater or "Installed skill:" not in updater:
        fail("updater output must show Atlas package title and installed skill ID")


def main() -> None:
    for adapter in ADAPTERS:
        validate_adapter(adapter)
    validate_cursor_rule()
    validate_docs()
    print("Adapter validation passed")


if __name__ == "__main__":
    main()
