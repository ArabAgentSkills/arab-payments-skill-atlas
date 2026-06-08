#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
BASELINE_PATH = ROOT / "docs" / "source-watch-baseline.json"
REPORT_PATH = ROOT / "docs" / "source-watch-report.md"
USER_AGENT = "arab-payments-skill-atlas-source-watch/1.0"
MAX_EXCERPT_CHARS = 500
ARTIFACT_INVALID_CHARS = re.compile(r'[<>:"/\\|?*\r\n]+')
MAX_ARTIFACT_FILENAME_CHARS = 96
FETCH_ATTEMPTS = 3
BASELINE_DEGRADED_STATUSES = {"TLS_VERIFY"}
TRANSIENT_FAILURE_EXCERPTS = {"TimeoutError", "URLError"}
RELATIVE_UPDATED_AGE = re.compile(r"\bUpdated \d+ (?:second|minute|hour|day|week|month|year)s? ago\b")
HYPERPAY_GREETING_NAV_CHROME = re.compile(r"\bBoard of Directors Greetings Contact us\b")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ascii_safe(value: str) -> str:
    return value.encode("ascii", errors="backslashreplace").decode("ascii")


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


def load_provider_urls() -> dict[str, dict[str, object]]:
    urls: dict[str, dict[str, object]] = {}
    for index_path in sorted(SKILLS_ROOT.glob("*/references/provider-index.json")):
        data = json.loads(index_path.read_text(encoding="utf-8"))
        skill = data.get("skill", index_path.parents[1].name)
        for provider in data["providers"]:
            provider_id = f"{skill}:{provider['id']}"
            for url in provider["source_urls"]:
                item = urls.setdefault(url, {"url": url, "provider_ids": []})
                item["provider_ids"].append(provider_id)
    for item in urls.values():
        item["provider_ids"] = sorted(set(item["provider_ids"]))
    return dict(sorted(urls.items()))


def load_baseline() -> dict[str, dict[str, object]]:
    if not BASELINE_PATH.exists():
        return {}
    data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return {item["url"]: item for item in data.get("sources", [])}


def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", text)
    text = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", text)
    text = re.sub(r"(?is)<noscript[^>]*>.*?</noscript>", " ", text)
    text = re.sub(r"(?s)<!--.*?-->", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return html.unescape(text)


def normalize_text(raw: bytes, content_type: str) -> str:
    decoded = raw.decode("utf-8", errors="ignore")
    lowered_type = content_type.lower()
    if "html" in lowered_type or "<html" in decoded[:500].lower():
        decoded = strip_html(decoded)
    decoded = decoded.replace("\r\n", "\n").replace("\r", "\n")
    decoded = re.sub(r"[ \t]+", " ", decoded)
    decoded = re.sub(r"\n{3,}", "\n\n", decoded)
    decoded = RELATIVE_UPDATED_AGE.sub("Updated <relative-age> ago", decoded)
    decoded = HYPERPAY_GREETING_NAV_CHROME.sub("Board of Directors Contact us", decoded)
    return decoded.strip()


def excerpt(text: str) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= MAX_EXCERPT_CHARS:
        return ascii_safe(compact)
    return ascii_safe(compact[:MAX_EXCERPT_CHARS].rstrip() + "...")


def artifact_safe_slug(value: str) -> str:
    cleaned = ARTIFACT_INVALID_CHARS.sub("-", value)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-. ")
    return cleaned or "source"


def snapshot_filename(provider_ids: list[str], url: str) -> str:
    provider_prefix = "-".join(artifact_safe_slug(provider_id) for provider_id in provider_ids)
    name = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    suffix = f"-{name}.txt"
    max_prefix_length = max(1, MAX_ARTIFACT_FILENAME_CHARS - len(suffix))
    if len(provider_prefix) > max_prefix_length:
        provider_prefix = provider_prefix[:max_prefix_length].rstrip("-. ")
    return f"{provider_prefix or 'source'}{suffix}"


def fetch_url(url: str) -> dict[str, object]:
    github_api_url = github_source_api_url(url)
    if github_api_url:
        request = urllib.request.Request(
            github_api_url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/vnd.github+json",
                "Accept-Encoding": "identity",
            },
            method="GET",
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                payload = json.loads(raw.decode("utf-8"))
                if "/orgs/" in github_api_url:
                    metadata = {
                        "login": payload.get("login", ""),
                        "html_url": payload.get("html_url", url),
                        "description": payload.get("description") or "",
                        "type": payload.get("type", ""),
                        "public_repos": payload.get("public_repos", 0),
                    }
                else:
                    metadata = {
                        "full_name": payload.get("full_name", ""),
                        "html_url": payload.get("html_url", url),
                        "description": payload.get("description") or "",
                        "default_branch": payload.get("default_branch", ""),
                        "archived": bool(payload.get("archived")),
                        "disabled": bool(payload.get("disabled")),
                        "pushed_at": payload.get("pushed_at", ""),
                        "updated_at": payload.get("updated_at", ""),
                    }
                normalized = json.dumps(metadata, sort_keys=True, ensure_ascii=True)
                digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
                return {
                    "status": "OK",
                    "http_status": response.status,
                    "normalized": normalized,
                    "hash": digest,
                    "content_length": len(normalized),
                    "excerpt": excerpt(normalized),
                }
        except urllib.error.HTTPError as exc:
            if exc.code in {401, 403}:
                return {
                    "status": "JS_CHALLENGE",
                    "http_status": exc.code,
                    "normalized": "",
                    "hash": "",
                    "content_length": 0,
                    "excerpt": "GitHub API verification requires retry or manual browser verification.",
                }
            return {
                "status": "FAIL",
                "http_status": exc.code,
                "normalized": "",
                "hash": "",
                "content_length": 0,
                "excerpt": f"GitHub API HTTP error {exc.code}.",
            }
        except Exception as exc:
            return {
                "status": "FAIL",
                "http_status": "",
                "normalized": "",
                "hash": "",
                "content_length": 0,
                "excerpt": f"GitHub API {exc.__class__.__name__}",
            }

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/json,text/plain,*/*",
            "Accept-Encoding": "identity",
        },
        method="GET",
    )
    for attempt in range(1, FETCH_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                content_encoding = response.headers.get("content-encoding", "").lower()
                if "gzip" in content_encoding:
                    raw = gzip.decompress(raw)
                status = response.status
                content_type = response.headers.get("content-type", "")
                preview = raw[:4096].decode("utf-8", errors="ignore").lower()
                if "javascript is disabled" in preview and "verify that you're not a robot" in preview:
                    return {
                        "status": "JS_CHALLENGE",
                        "http_status": status,
                        "normalized": "",
                        "hash": "",
                        "content_length": 0,
                        "excerpt": "Manual browser verification required.",
                    }
                normalized = normalize_text(raw, content_type)
                digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
                return {
                    "status": "OK",
                    "http_status": status,
                    "normalized": normalized,
                    "hash": digest,
                    "content_length": len(normalized),
                    "excerpt": excerpt(normalized),
                }
        except urllib.error.HTTPError as exc:
            if exc.code in {401, 403}:
                return {
                    "status": "JS_CHALLENGE",
                    "http_status": exc.code,
                    "normalized": "",
                    "hash": "",
                    "content_length": 0,
                    "excerpt": "Manual browser verification required.",
                }
            return {
                "status": "FAIL",
                "http_status": exc.code,
                "normalized": "",
                "hash": "",
                "content_length": 0,
                "excerpt": f"HTTP error {exc.code}.",
            }
        except urllib.error.URLError as exc:
            if isinstance(getattr(exc, "reason", None), ssl.SSLCertVerificationError):
                return {
                    "status": "TLS_VERIFY",
                    "http_status": "",
                    "normalized": "",
                    "hash": "",
                    "content_length": 0,
                    "excerpt": "Manual browser/TLS verification required.",
                }
            if attempt < FETCH_ATTEMPTS:
                continue
            return {
                "status": "FAIL",
                "http_status": "",
                "normalized": "",
                "hash": "",
                "content_length": 0,
                "excerpt": exc.__class__.__name__,
            }
        except Exception as exc:
            if attempt < FETCH_ATTEMPTS:
                continue
            return {
                "status": "FAIL",
                "http_status": "",
                "normalized": "",
                "hash": "",
                "content_length": 0,
                "excerpt": exc.__class__.__name__,
            }
    raise RuntimeError("unreachable fetch retry state")


def build_current_records(output_dir: Path | None = None) -> list[dict[str, object]]:
    now = utc_now()
    records: list[dict[str, object]] = []
    for url, meta in load_provider_urls().items():
        result = fetch_url(url)
        normalized = str(result.pop("normalized"))
        record = {
            "url": url,
            "provider_ids": meta["provider_ids"],
            "status": result["status"],
            "http_status": result["http_status"],
            "sha256": result["hash"],
            "content_length": result["content_length"],
            "excerpt": result["excerpt"],
            "last_checked": now,
        }
        records.append(record)
        if output_dir and normalized:
            target = output_dir / snapshot_filename(list(record["provider_ids"]), url)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(normalized, encoding="utf-8")
    return records


def compare_records(current: list[dict[str, object]], baseline: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    changes: list[dict[str, object]] = []
    current_by_url = {item["url"]: item for item in current}
    for item in current:
        previous = baseline.get(item["url"])
        if previous is None:
            changes.append({"change": "NEW", "current": item, "previous": None})
            continue
        if item["status"] != previous.get("status"):
            if previous.get("status") == "OK" and item["status"] in BASELINE_DEGRADED_STATUSES:
                continue
            if (
                previous.get("status") == "OK"
                and item["status"] == "FAIL"
                and item.get("excerpt") in TRANSIENT_FAILURE_EXCERPTS
            ):
                continue
            changes.append({"change": "CHANGED", "current": item, "previous": previous})
            continue
        if item["status"] == "OK" and item["sha256"] != previous.get("sha256"):
            changes.append({"change": "CHANGED", "current": item, "previous": previous})
    for url, previous in baseline.items():
        if url not in current_by_url:
            changes.append({"change": "REMOVED", "current": None, "previous": previous})
    return changes


def write_baseline(records: list[dict[str, object]]) -> None:
    payload = {
        "generated_at": utc_now(),
        "policy": "Public-safe source watch baseline. Stores hashes, lengths, statuses, timestamps, and short excerpts only. Full provider docs are not committed.",
        "sources": records,
    }
    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def render_report(changes: list[dict[str, object]], current: list[dict[str, object]]) -> str:
    lines = [
        "# Source Watch Report",
        "",
        f"- Generated: {utc_now()}",
        f"- Total URLs checked: {len(current)}",
        f"- Changes detected: {len(changes)}",
        "- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.",
        "",
    ]
    if not changes:
        lines.extend(["## Result", "", "No provider documentation changes detected.", ""])
    else:
        lines.extend(["## Changes", ""])
        for change in changes:
            current_item = change.get("current")
            previous_item = change.get("previous")
            item = current_item or previous_item
            assert item is not None
            lines.append(f"### {change['change']}: {item['url']}")
            lines.append("")
            lines.append(f"- Providers: {', '.join(item.get('provider_ids', []))}")
            if previous_item:
                lines.append(f"- Previous status: {previous_item.get('status')} / hash `{previous_item.get('sha256')}`")
            if current_item:
                lines.append(f"- Current status: {current_item.get('status')} / hash `{current_item.get('sha256')}`")
                lines.append(f"- Excerpt: {current_item.get('excerpt')}")
            lines.append("")
    js_items = [item for item in current if item["status"] == "JS_CHALLENGE"]
    if js_items:
        lines.extend(["## Manual Browser Verification", ""])
        for item in js_items:
            lines.append(f"- {item['url']}")
        lines.append("")
    tls_items = [item for item in current if item["status"] == "TLS_VERIFY"]
    if tls_items:
        lines.extend(["## Manual Browser/TLS Verification", ""])
        for item in tls_items:
            lines.append(f"- {item['url']}")
        lines.append("")
    return "\n".join(lines)


def write_report(text: str) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect public provider documentation source changes.")
    parser.add_argument("--check", action="store_true", help="Compare current sources with baseline and exit non-zero when changes are detected.")
    parser.add_argument("--update-baseline", action="store_true", help="Update the public-safe baseline and report.")
    parser.add_argument("--output-dir", type=Path, help="Optional private artifact directory for full normalized snapshots.")
    args = parser.parse_args()

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
    current = build_current_records(args.output_dir)
    baseline = load_baseline()
    changes = compare_records(current, baseline)
    report = render_report(changes, current)
    print(report)

    if args.update_baseline:
        write_baseline(current)
        write_report(report)
        print(f"\nUpdated {BASELINE_PATH.relative_to(ROOT)} and {REPORT_PATH.relative_to(ROOT)}")
        return
    if args.check and changes:
        print("\nSource changes detected. Review privately before publishing guidance updates.")
        sys.exit(2)
    if args.check:
        print("\nSource watch baseline is current.")


if __name__ == "__main__":
    main()
