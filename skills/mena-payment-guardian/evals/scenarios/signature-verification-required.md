# Signature Verification Required

## User Prompt

"The webhook payload says success. Can we just trust it if it came to our endpoint?"

## Required Skill Use

The agent loads the relevant provider file and `server-secret-boundary.md`.

## Expected Agent Behavior

- Requires PayTabs raw-body HMAC, Paymob HMAC, PaySky SecureHash, APS response signature, MyFatoorah webhook signature, HyperPay encrypted webhook authentication, Moyasar secret token, or the provider's documented equivalent.
- Rejects or manual-reviews unsigned, unverifiable, or mismatched payloads.
- Keeps verification credentials server-side.

## Fail If

- Agent trusts webhook body without authenticity validation.
- Agent invents a signature algorithm when docs are partial.
- Agent exposes verification secrets in client code.
