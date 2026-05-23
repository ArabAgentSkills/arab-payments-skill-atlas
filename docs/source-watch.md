# Source Watch

Arab Payments Skill Atlas monitors official provider documentation with public-safe fingerprints. V1 monitoring covers the Egypt Payment Guardian provider set. The public repository stores hashes, content lengths, statuses, timestamps, and short excerpts only.

## What Is Public

- `docs/source-watch-baseline.json`: URL fingerprints and short excerpts.
- `docs/source-watch-report.md`: latest public-safe report.
- Provider references updated only after human review.

## What Must Stay Private

- Full fetched provider documentation snapshots.
- Private merchant docs, dashboards, screenshots, onboarding emails, and credentials.
- Unreviewed provider behavior changes.

Full snapshots belong only in a private watcher repository or short-retention private GitHub Actions artifacts. They must not be committed to this public repository.

## Local Commands

Check current sources against the public baseline:

```powershell
python scripts\check_source_changes.py --check
```

Refresh the public-safe baseline after human review:

```powershell
python scripts\check_source_changes.py --update-baseline
```

Capture full normalized snapshots for private review only:

```powershell
python scripts\check_source_changes.py --check --output-dir source-watch-artifacts\manual-review
```

The `source-watch-artifacts/` folder is ignored by git.

## Approval Policy

Provider docs may change automatically, but public payment guidance must not. A maintainer should review the private watcher output, update provider summaries by hand, run validation, then publish an approved release.
