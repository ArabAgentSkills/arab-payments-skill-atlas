# Arab Payments Skill Atlas Claude Adapter

For Claude Code, treat the skill folders as canonical and this file as a project memory shim.

Use `skills/egypt-payment-guardian/SKILL.md` for Egypt-only payment flows. If native skills are available, install it at `.claude/skills/egypt-payment-guardian/SKILL.md`.

Use `skills/mena-payment-guardian/SKILL.md` for broader Arab/MENA PSP or BNPL flows. If native skills are available, install it at `.claude/skills/mena-payment-guardian/SKILL.md`.

Trigger on Paymob, FawryPay, Geidea, PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, EasyKash, Kashier, PaySky, Tabby, Tamara, valU, Souhoola, callbacks, webhooks, redirects, HMAC, signatures, SecureHash, payment inquiry, refunds, voids, captures, BNPL, or payment secret boundaries.

Payment non-negotiables:

- Never trust redirect alone.
- Verify signature, HMAC, or SecureHash before processing.
- Keep payment secrets server-side.
- Compare amount, currency, order reference, and provider reference.
- Process callbacks and retries idempotently.

Load provider detail only when the provider is relevant. If official docs are missing, partial, or gated, ask for merchant docs instead of guessing.
