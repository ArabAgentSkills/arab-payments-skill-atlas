# Egypt Payment Guardian Copilot Instructions

For Egypt payment work, use `skills/egypt-payment-guardian/SKILL.md` as the source of truth. Load provider detail from `skills/egypt-payment-guardian/references/providers/` for Paymob, FawryPay, Geidea Egypt, EasyKash, Kashier, PaySky, valU, or Souhoola.

Payment non-negotiables:

- Never trust redirect alone.
- Verify signature, HMAC, or SecureHash before processing.
- Keep payment secrets server-side.
- Compare amount, currency, order reference, and provider reference.
- Process callbacks and retries idempotently.

If official docs are partial or gated, do not guess. Ask for official merchant docs and keep credentials out of frontend code, logs, screenshots, and git.
