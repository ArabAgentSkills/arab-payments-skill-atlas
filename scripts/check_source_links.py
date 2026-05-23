#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "skills" / "egypt-payment-guardian" / "references" / "provider-index.json"


def load_urls() -> list[str]:
    data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    urls: list[str] = []
    for provider in data["providers"]:
        urls.extend(provider["source_urls"])
    return sorted(set(urls))


def check_url(url: str) -> tuple[str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "egypt-payment-guardian-link-check/1.0",
            "Accept": "text/html,application/json,text/plain,*/*",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            status = response.status
            body = response.read(4096).decode("utf-8", errors="ignore").lower()
            if "javascript is disabled" in body and "verify that you're not a robot" in body:
                return "js_challenge", str(status)
            if 200 <= status < 400:
                return "ok", str(status)
            return "fail", str(status)
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            return "js_challenge", str(exc.code)
        return "fail", str(exc.code)
    except Exception as exc:
        return "fail", exc.__class__.__name__


def main() -> None:
    failures: list[str] = []
    js_challenges: list[str] = []
    for url in load_urls():
        status, detail = check_url(url)
        marker = {"ok": "OK", "js_challenge": "JS_CHALLENGE"}.get(status, "FAIL")
        print(f"{marker} {detail} {url}")
        if status == "js_challenge":
            js_challenges.append(f"{detail} {url}")
        elif status != "ok":
            failures.append(f"{detail} {url}")
    if js_challenges:
        print("\nSource URLs requiring browser/JavaScript verification, not marked broken:")
        for item in js_challenges:
            print(f"- {item}")
    if failures:
        print("\nBroken source URLs:")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)
    print("All source links reachable")


if __name__ == "__main__":
    main()
