# Egypt Payment Guardian Claude Adapter

For Claude Code, treat `skills/egypt-payment-guardian/SKILL.md` as the canonical skill. If native skills are available, install the folder at `.claude/skills/egypt-payment-guardian/SKILL.md`. This file is only a project memory shim.

Use the skill before building or reviewing Egypt payment flows involving Paymob, FawryPay, Geidea Egypt, EasyKash, Kashier, PaySky, valU, Souhoola, callbacks, webhooks, redirects, HMAC, signatures, SecureHash, payment inquiry, refunds, voids, captures, or payment secret boundaries.

Payment non-negotiables:

- Never trust redirect alone.
- Verify signature, HMAC, or SecureHash before processing.
- Keep payment secrets server-side.
- Compare amount, currency, order reference, and provider reference.
- Process callbacks and retries idempotently.

Load provider detail from `skills/egypt-payment-guardian/references/providers/` only when the provider is relevant. If official docs are missing, partial, or gated, ask for merchant docs instead of guessing.
