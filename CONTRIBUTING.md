# Contributing

## Provider Updates

Use official or provider-controlled documentation first. Acceptable sources include official docs, official GitHub organizations, official product pages, and official support portals.

Do not copy full vendor docs into this repository. Summarize only the contract an agent needs to avoid unsafe implementation decisions.

## Required Provider Fields

Each provider file must include:

- Integration types
- Auth and secret boundary
- Callback or webhook contract
- Signature or HMAC rules
- Idempotency keys
- Amount and currency handling
- Status mapping
- Refunds, voids, and subscriptions when documented
- Sandbox and test notes
- Unknowns and do-not-invent notes

## Private Docs

Private merchant docs may be used locally to inform a summary only if licensing allows it. Keep raw private docs under `private-docs/` or `local-docs/`. Never commit them.

## Security

Never commit live credentials, sandbox credentials, HMAC secrets, merchant IDs tied to a real account, service role keys, raw card data, webhook signatures, or provider tokens.
