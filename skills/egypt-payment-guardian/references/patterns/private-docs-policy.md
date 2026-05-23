# Private Docs Policy

## Principle

Use private merchant docs only as local research material. Do not commit raw private docs or copied vendor text.

## Allowed Local Workflow

1. Store private provider PDFs, screenshots, portal exports, or merchant emails under `private-docs/` or `local-docs/`.
2. Extract only the implementation facts needed for a concise summary.
3. Add source status such as `private merchant docs reviewed locally` only if the user approves that wording.
4. Commit only original summaries, source metadata, and safe field names.
5. Leave secrets, screenshots, full pages, tokens, and copied docs out of git.

## Public Repo Rule

Public reference files should say what is known, what is unknown, and what must be verified from official docs. If a provider's docs are gated, say so clearly and ask the user for merchant docs before endpoint-level implementation.

## Source Confidence Labels

- High: official public docs cover the behavior.
- Medium: official product pages or official demos cover behavior, but endpoint docs are missing or gated.
- Low: non-official sources only. Do not implement from this without confirmation.

## Fail The Review If

- The repo contains raw vendor PDFs, screenshots, copied portal pages, or full docs.
- The repo contains real credentials or merchant-specific values.
- The skill instructs agents to guess gated endpoint behavior.
