#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "__pycache__", "private-docs", "local-docs", "vendor-doc-snapshots"}
TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".txt"}

SECRET_PATTERNS = [
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("aws access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("stripe-like live key", re.compile(r"\b[psrk]k_live_[0-9A-Za-z]{16,}\b")),
    ("stripe webhook secret", re.compile(r"\bwhsec_[0-9A-Za-z]{16,}\b")),
    ("assigned service role key", re.compile(r"service_role\s*[:=]\s*[A-Za-z0-9._-]{12,}", re.IGNORECASE)),
    ("assigned payment secret", re.compile(r"(secret|hmac|api[_-]?key|authorization)\s*[:=]\s*[A-Za-z0-9._:/+=-]{24,}", re.IGNORECASE)),
    ("kashier merchant id value", re.compile(r"\bMID-\d{2,}-\d{2,}\b")),
]


def should_skip(path: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return True
    if path == Path(__file__).resolve():
        return True
    return False


def main() -> None:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or should_skip(path):
            continue
        if path.name == ".env" or path.name.startswith(".env."):
            failures.append(f"{path}: env file must not be committed")
            continue
        if path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}:
            failures.append(f"{path}: private key/certificate file must not be committed")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                failures.append(f"{path}: possible {label}")
    if failures:
        print("Secret scan failed:")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)
    print("Secret scan passed")


if __name__ == "__main__":
    main()
