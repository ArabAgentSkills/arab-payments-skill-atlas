# Source Watch

Arab Payments Skill Atlas monitors official provider documentation with public-safe fingerprints. V1.0.0 monitoring covers both `egypt-payment-guardian` and `mena-payment-guardian` provider indexes. The public repository stores hashes, content lengths, statuses, timestamps, and short excerpts only.

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

`JS_CHALLENGE`, `TLS_VERIFY`, and source-link `SERVER_ERROR` warnings mean the URL needs manual browser/provider verification. `SERVER_ERROR` exits with review-required code `2`; it is not treated as confirmed broken by itself. Clear missing-link failures such as `404` or `410` still exit as hard failures and require maintainer action.
