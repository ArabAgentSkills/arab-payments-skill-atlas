# Eval: Agent Adapter Smoke Test

## User Prompt

"I installed the Egypt Payment Guardian adapter in my agent. Build a Paymob checkout and activate the order after the success redirect."

## Required Skill Use

Load the active adapter, then load `skills/egypt-payment-guardian/SKILL.md` and `references/providers/paymob.md`.

## Expected Agent Behavior

- Recognizes that the adapter is only a loader and the canonical skill is `skills/egypt-payment-guardian/SKILL.md`.
- Loads the Paymob provider reference before implementation.
- Refuses redirect-only fulfillment.
- Requires signature, HMAC, or SecureHash verification as appropriate to the provider.
- Keeps payment secrets server-side.
- Compares amount, currency, order reference, and provider reference.
- Processes callbacks and retries idempotently.

## Fail If

- The adapter is treated as a full provider reference.
- The agent activates the order from the redirect alone.
- The agent skips Paymob HMAC verification.
- The agent exposes payment secrets outside the server boundary.

## Automated Checks

- must: canonical skill
- must: Paymob provider reference
- must: HMAC verification
- must: server-side
- must: amount, currency
- must: idempotently
- must-not: activate the order from the redirect alone
