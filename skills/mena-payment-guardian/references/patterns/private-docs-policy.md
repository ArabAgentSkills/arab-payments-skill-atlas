# Private Docs Policy

Use this policy whenever a provider portal, merchant email, dashboard export, PDF, screenshot, or partner document is not clearly public.

## Public Repo Rule

Commit only:

- concise original summaries
- official public URLs
- source confidence notes
- unknowns and do-not-invent guidance
- public-safe hashes, lengths, statuses, timestamps, and short excerpts for source watch

## Never Commit

- private merchant PDFs
- portal screenshots
- copied full provider docs
- API credentials or test/live secrets
- merchant IDs tied to a real account
- dashboard exports

## Safe Workflow

1. Store private material only in ignored local folders such as `private-docs/` or `local-docs/`.
2. Summarize only what licensing and access terms permit.
3. Mark gated docs as gated instead of inventing missing behavior.
4. Add evals for any risky provider-specific behavior.
