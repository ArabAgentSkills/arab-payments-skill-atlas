# Security Policy

## Reporting

Open a GitHub security advisory or private issue if you find:

- A committed credential or secret.
- A provider flow that can mark an order paid from an unverified redirect.
- Missing signature verification guidance.
- Missing idempotency guidance that can duplicate paid state.
- Advice that places service role keys or merchant secrets in frontend code.

## Handling Secrets

Do not include real provider credentials in issues, screenshots, logs, examples, or evals. Replace values with descriptive placeholders such as `<PAYMOB_SECRET_KEY>` or `<EASYKASH_HMAC_SECRET>`.

## Payment Safety Baseline

Payment fulfillment must be server-confirmed, signature-verified where the provider supports it, amount/currency-checked, and idempotent.
