#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION_PATH = ROOT / "skill-version.json"
UPDATER_VERSION = "0.1.0"
MANIFEST_NAME = ".egypt-payment-guardian-install.json"


def load_version(root: Path) -> dict[str, str]:
    path = root / "skill-version.json"
    if not path.exists():
        return {
            "name": "egypt-payment-guardian",
            "version": "local",
            "canonical_repo_url": "",
            "skill_path": "skills/egypt-payment-guardian",
        }
    return json.loads(path.read_text(encoding="utf-8"))


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(item for item in path.rglob("*") if item.is_file())


def relative_manifest(source: Path, target: Path) -> dict[str, str]:
    manifest: dict[str, str] = {}
    if source.is_file():
        manifest[target.name] = file_hash(source)
        return manifest
    for src in iter_files(source):
        rel = src.relative_to(source).as_posix()
        manifest[rel] = file_hash(src)
    return manifest


def read_manifest(target: Path) -> dict[str, str]:
    manifest_path = target / MANIFEST_NAME if target.is_dir() else target.parent / MANIFEST_NAME
    if not manifest_path.exists():
        return {}
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data.get("files", {})


def write_manifest(target: Path, files: dict[str, str], version: str, dry_run: bool) -> None:
    if dry_run:
        return
    manifest_path = target / MANIFEST_NAME if target.is_dir() else target.parent / MANIFEST_NAME
    payload = {
        "name": "egypt-payment-guardian",
        "version": version,
        "updater_version": UPDATER_VERSION,
        "files": files,
    }
    manifest_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def detect_local_changes(source: Path, target: Path, previous: dict[str, str]) -> list[str]:
    if not target.exists():
        return []
    changed: list[str] = []
    if source.is_file():
        rel = target.name
        if target.exists() and previous.get(rel) and file_hash(target) != previous[rel]:
            changed.append(str(target))
        elif target.exists() and not previous and file_hash(target) != file_hash(source):
            changed.append(str(target))
        return changed
    for src in iter_files(source):
        rel = src.relative_to(source).as_posix()
        dst = target / rel
        if not dst.exists():
            continue
        old_hash = previous.get(rel)
        if old_hash and file_hash(dst) != old_hash:
            changed.append(str(dst))
        elif not previous and file_hash(dst) != file_hash(src):
            changed.append(str(dst))
    return changed


def copy_item(source: Path, target: Path, version: str, force: bool, dry_run: bool, scope: str) -> None:
    previous = read_manifest(target)
    local_changes = detect_local_changes(source, target, previous)
    if local_changes and not force:
        if dry_run:
            print(f"Would refuse to overwrite {scope} local changes unless --force is provided:")
            for item in local_changes[:20]:
                print(f"- {item}")
            return
        print(f"Refusing to overwrite {scope} local changes. Re-run with --force after reviewing:")
        for item in local_changes[:20]:
            print(f"- {item}")
        raise SystemExit(1)
    if dry_run:
        print(f"Would install [{scope}] {source} -> {target}")
        return
    if source.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        files = relative_manifest(source, target)
        write_manifest(target, files, version, dry_run)
        print(f"Installed [{scope}] {target}")
        return
    if target.exists() and force:
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)
    for src in iter_files(source):
        rel = src.relative_to(source)
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    files = relative_manifest(source, target)
    write_manifest(target, files, version, dry_run)
    print(f"Installed [{scope}] {target}")


def repo_api_url(repo_url: str) -> str:
    normalized = repo_url.rstrip("/").removesuffix(".git")
    parts = normalized.split("/")
    if len(parts) < 2:
        raise ValueError("repo URL must end with owner/repo")
    owner, repo = parts[-2], parts[-1]
    return f"https://api.github.com/repos/{owner}/{repo}/releases/latest"


def download_latest_release(repo_url: str) -> Path:
    api_url = repo_api_url(repo_url)
    request = urllib.request.Request(api_url, headers={"User-Agent": "egypt-payment-guardian-updater/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))
    zip_url = data.get("zipball_url")
    if not zip_url:
        raise RuntimeError("latest release has no zipball_url")
    tmp_dir = Path(tempfile.mkdtemp(prefix="egypt-payment-guardian-release-"))
    zip_path = tmp_dir / "release.zip"
    with urllib.request.urlopen(urllib.request.Request(zip_url, headers={"User-Agent": "egypt-payment-guardian-updater/1.0"}), timeout=60) as response:
        zip_path.write_bytes(response.read())
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(tmp_dir)
    roots = [item for item in tmp_dir.iterdir() if item.is_dir()]
    if not roots:
        raise RuntimeError("release archive did not contain a repo directory")
    return roots[0]


def install_plan(source_root: Path, agent: str, target: Path | None, include_global_codex: bool) -> list[tuple[Path, Path, str]]:
    home = Path.home()
    items: list[tuple[Path, Path, str]] = []
    if agent == "codex" or (agent == "all" and include_global_codex):
        items.append((source_root / "skills" / "egypt-payment-guardian", home / ".agents" / "skills" / "egypt-payment-guardian", "global-codex"))
    project = target or Path.cwd()
    if agent == "all":
        items.append((source_root / "AGENTS.md", project / "AGENTS.md", "project-local"))
    if agent in {"claude", "all"}:
        items.append((source_root / "skills" / "egypt-payment-guardian", project / ".claude" / "skills" / "egypt-payment-guardian", "project-local"))
        items.append((source_root / "CLAUDE.md", project / "CLAUDE.md", "project-local"))
    if agent in {"cursor", "all"}:
        items.append((source_root / ".cursor" / "rules" / "egypt-payment-guardian.mdc", project / ".cursor" / "rules" / "egypt-payment-guardian.mdc", "project-local"))
    if agent in {"copilot", "all"}:
        items.append((source_root / ".github" / "copilot-instructions.md", project / ".github" / "copilot-instructions.md", "project-local"))
    if agent in {"generic", "all"}:
        items.append((source_root / "adapters" / "generic" / "EGYPT_PAYMENT_GUARDIAN_PROMPT.md", project / "EGYPT_PAYMENT_GUARDIAN_PROMPT.md", "project-local"))
    return items


def main() -> None:
    parser = argparse.ArgumentParser(description="Install or update Egypt Payment Guardian from an approved public package.")
    parser.add_argument("--agent", choices=["codex", "claude", "cursor", "copilot", "generic", "all"], default="codex")
    parser.add_argument("--target", type=Path, help="Target project root for project-local adapters.")
    parser.add_argument("--source-root", type=Path, default=ROOT, help="Local approved package root.")
    parser.add_argument("--use-latest-release", action="store_true", help="Download latest approved public GitHub release before installing.")
    parser.add_argument("--include-global-codex", action="store_true", help="With --agent all, also install the global Codex skill under $HOME/.agents/skills.")
    parser.add_argument("--repo-url", help="Public GitHub repo URL. Defaults to skill-version.json canonical_repo_url.")
    parser.add_argument("--force", action="store_true", help="Overwrite local changes after review.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be installed without writing files.")
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    version = load_version(source_root)
    repo_url = args.repo_url or version.get("canonical_repo_url", "")
    if args.use_latest_release:
        if not repo_url:
            raise SystemExit("No repo URL configured for latest release lookup")
        try:
            source_root = download_latest_release(repo_url)
            version = load_version(source_root)
        except (urllib.error.URLError, urllib.error.HTTPError, RuntimeError, ValueError) as exc:
            raise SystemExit(f"Could not download latest approved release: {exc}") from exc

    print(f"{version.get('package_title', 'Arab Payments Skill Atlas')} updater {UPDATER_VERSION}")
    print(f"Installed skill: {version.get('name', 'egypt-payment-guardian')}")
    print(f"Source version: {version.get('version', 'local')}")
    print("Updates are opt-in and install only from the selected approved public package.")
    if args.agent == "all" and not args.include_global_codex:
        print("Mode: project-local adapters only. Add --include-global-codex to update the global Codex skill too.")
    for source, target, scope in install_plan(source_root, args.agent, args.target, args.include_global_codex):
        if not source.exists():
            raise SystemExit(f"Missing source path: {source}")
        copy_item(source, target, str(version.get("version", "local")), args.force, args.dry_run, scope)


if __name__ == "__main__":
    main()
