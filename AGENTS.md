# Arab Payments Skill Atlas Adapter

Use this adapter for Codex, OpenCode, AGENTS.md-compatible agents, and any coding agent that reads root project instructions.

Before building or reviewing payment code in this region, choose the smallest matching skill:

- Egypt-only work: load `skills/egypt-payment-guardian/SKILL.md`.
- Broader Arab/MENA PSP or BNPL work: load `skills/mena-payment-guardian/SKILL.md`.

Then load only the needed provider reference from the selected skill's `references/providers/` folder.

Trigger on Paymob, FawryPay, Geidea, PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, EasyKash, Kashier, PaySky, Tabby, Tamara, valU, Souhoola, checkout, callbacks, webhooks, redirects, HMAC, signatures, SecureHash, refunds, voids, captures, payment inquiry, BNPL, or payment secret boundaries.

Payment non-negotiables:

- Never trust redirect alone.
- Verify signature, HMAC, or SecureHash before processing.
- Keep payment secrets server-side.
- Compare amount, currency, order reference, and provider reference.
- Process callbacks and retries idempotently.

If provider docs are partial or gated, say so and ask for official merchant docs. Do not invent endpoints, fields, signatures, status names, test cards, or credentials.
