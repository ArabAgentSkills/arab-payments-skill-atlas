# Arab Payments Skill Atlas Copilot Instructions

For Egypt-only payment work, use `skills/egypt-payment-guardian/SKILL.md` as the source of truth.

For broader Arab/MENA PSP or BNPL work, use `skills/mena-payment-guardian/SKILL.md` as the source of truth.

Load provider detail only when relevant. Covered providers include Paymob, FawryPay, Geidea, PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, EasyKash, Kashier, PaySky, Tabby, Tamara, valU, and Souhoola.

Payment non-negotiables:

- Never trust redirect alone.
- Verify signature, HMAC, or SecureHash before processing.
- Keep payment secrets server-side.
- Compare amount, currency, order reference, and provider reference.
- Process callbacks and retries idempotently.

If official docs are partial or gated, do not guess. Ask for official merchant docs and keep credentials out of frontend code, logs, screenshots, and git.
