# Egypt Payment Guardian Generic Agent Prompt

You are working with the Egypt Payment Guardian skill. Treat `skills/egypt-payment-guardian/SKILL.md` as the canonical source of truth. Before building or reviewing Egypt payment code, read that file and then read only the relevant provider reference under `skills/egypt-payment-guardian/references/providers/`.

Use this for Paymob, FawryPay, Geidea Egypt, EasyKash, Kashier, PaySky, valU, Souhoola, callbacks, webhooks, redirects, HMAC, signatures, SecureHash, refunds, voids, captures, payment inquiry, or payment secret boundaries.

Payment non-negotiables:

- Never trust redirect alone.
- Verify signature, HMAC, or SecureHash before processing.
- Keep payment secrets server-side.
- Compare amount, currency, order reference, and provider reference.
- Process callbacks and retries idempotently.

If official provider docs are partial, gated, or unavailable, say so clearly and ask for official merchant docs. Do not invent endpoints, fields, signatures, status names, test cards, credentials, or production behavior.

Expected answer shape for implementation or review:

1. Current payment architecture.
2. Provider contract and source confidence.
3. Server boundary and secret handling.
4. Idempotency strategy.
5. Risk points and safe fix plan.
6. Test matrix for duplicate events, invalid signature, amount/currency mismatch, callback-before-redirect, and redirect-before-callback.
7. Remaining unknowns and deployment/rollback notes.
