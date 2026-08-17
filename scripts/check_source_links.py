#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
FETCH_ATTEMPTS = 3
TRANSIENT_HTTP_STATUSES = {408, 429}
USER_AGENT = "arab-payments-skill-atlas-link-check/1.0"


def is_transient_http_status(status: int) -> bool:
    return status >= 500 or status in TRANSIENT_HTTP_STATUSES


def github_source_api_url(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() != "github.com":
        return None
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if len(parts) == 1:
        owner = parts[0]
        return f"https://api.github.com/orgs/{urllib.parse.quote(owner)}"
    if len(parts) != 2:
        return None
    owner, repo = parts
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not owner or not repo:
        return None
    return f"https://api.github.com/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}"


def github_api_headers() -> dict[str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "Accept-Encoding": "identity",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def load_urls() -> list[str]:
    urls: list[str] = []
    for index_path in sorted(SKILLS_ROOT.glob("*/references/provider-index.json")):
        data = json.loads(index_path.read_text(encoding="utf-8"))
        for provider in data["providers"]:
            urls.extend(provider["source_urls"])
    return sorted(set(urls))


def check_url(url: str) -> tuple[str, str]:
    github_api_url = github_source_api_url(url)
    if github_api_url:
        api_request = urllib.request.Request(
            github_api_url,
            headers=github_api_headers(),
            method="GET",
        )
        try:
            with urllib.request.urlopen(api_request, timeout=25) as response:
                if 200 <= response.status < 400:
                    return "ok", f"{response.status} github_api"
                if is_transient_http_status(response.status):
                    return "server_error", f"{response.status} github_api"
                return "fail", str(response.status)
        except urllib.error.HTTPError as exc:
            if exc.code in {401, 403}:
                return "js_challenge", f"{exc.code} github_api"
            if is_transient_http_status(exc.code):
                return "server_error", f"{exc.code} github_api"
            return "fail", f"{exc.code} github_api"
        except Exception as exc:
            return "fail", f"{exc.__class__.__name__} github_api"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "arab-payments-skill-atlas-link-check/1.0",
            "Accept": "text/html,application/json,text/plain,*/*",
            "Accept-Encoding": "identity",
        },
        method="GET",
    )
    for attempt in range(1, FETCH_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                status = response.status
                body = response.read(4096).decode("utf-8", errors="ignore").lower()
                if "javascript is disabled" in body and "verify that you're not a robot" in body:
                    return "js_challenge", str(status)
                if 200 <= status < 400:
                    return "ok", str(status)
                if is_transient_http_status(status):
                    return "server_error", str(status)
                return "fail", str(status)
        except urllib.error.HTTPError as exc:
            if exc.code in {401, 403}:
                return "js_challenge", str(exc.code)
            if is_transient_http_status(exc.code):
                return "server_error", str(exc.code)
            return "fail", str(exc.code)
        except urllib.error.URLError as exc:
            if isinstance(getattr(exc, "reason", None), ssl.SSLCertVerificationError):
                return "tls_verify", "manual browser verification required"
            if attempt < FETCH_ATTEMPTS:
                continue
            return "fail", exc.__class__.__name__
        except Exception as exc:
            if attempt < FETCH_ATTEMPTS:
                continue
            return "fail", exc.__class__.__name__
    return "fail", "retry exhausted"


def main() -> None:
    failures: list[str] = []
    js_challenges: list[str] = []
    tls_verifications: list[str] = []
    server_errors: list[str] = []
    for url in load_urls():
        status, detail = check_url(url)
        marker = {
            "ok": "OK",
            "js_challenge": "JS_CHALLENGE",
            "tls_verify": "TLS_VERIFY",
            "server_error": "SERVER_ERROR",
        }.get(status, "FAIL")
        print(f"{marker} {detail} {url}")
        if status == "js_challenge":
            js_challenges.append(f"{detail} {url}")
        elif status == "tls_verify":
            tls_verifications.append(f"{detail} {url}")
        elif status == "server_error":
            server_errors.append(f"{detail} {url}")
        elif status != "ok":
            failures.append(f"{detail} {url}")
    if js_challenges:
        print("\nSource URLs requiring browser/JavaScript verification, not marked broken:")
        for item in js_challenges:
            print(f"- {item}")
    if tls_verifications:
        print("\nSource URLs requiring manual browser/TLS verification, not marked broken:")
        for item in tls_verifications:
            print(f"- {item}")
    if server_errors:
        print("\nSource URLs with transient provider/server errors, not marked broken:")
        for item in server_errors:
            print(f"- {item}")
        print("Run source-watch snapshot capture and maintainer review before changing guidance.")
        sys.exit(2)
    if failures:
        print("\nBroken source URLs:")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)
    print("All source links reachable")


if __name__ == "__main__":
    main()
