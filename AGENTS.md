# Egypt Payment Guardian Adapter

Use this adapter for Codex, OpenCode, AGENTS.md-compatible agents, and any coding agent that reads root project instructions.

Before building or reviewing Egypt payment code, load `skills/egypt-payment-guardian/SKILL.md`. Then load only the needed provider reference from `skills/egypt-payment-guardian/references/providers/`.

Trigger on Paymob, FawryPay, Geidea Egypt, EasyKash, Kashier, PaySky, valU, Souhoola, checkout, callbacks, webhooks, redirects, HMAC, signatures, SecureHash, refunds, voids, captures, payment inquiry, or payment secret boundaries.

Payment non-negotiables:

- Never trust redirect alone.
- Verify signature, HMAC, or SecureHash before processing.
- Keep payment secrets server-side.
- Compare amount, currency, order reference, and provider reference.
- Process callbacks and retries idempotently.

If provider docs are partial or gated, say so and ask for official merchant docs. Do not invent endpoints, fields, signatures, status names, test cards, or credentials.
