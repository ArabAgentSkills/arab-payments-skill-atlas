# Adapter MENA Routing

## User Prompt

"I am integrating Tap Payments and Tabby in a Saudi React app. Can you use the Arab Payments Skill Atlas?"

## Required Skill Use

The agent loads `skills/mena-payment-guardian/SKILL.md`, then the Tap Payments and Tabby provider references.

## Expected Agent Behavior

- Chooses `mena-payment-guardian`, not Egypt-only `egypt-payment-guardian`.
- Explains redirect success is UX only.
- Requires webhook/status verification and server-side secret handling.
- Separates Tap charge/authorize from Tabby authorization/capture lifecycle.

## Fail If

- Agent loads only Egypt-specific docs.
- Agent treats Tabby approval or Tap redirect as final fulfillment.
- Agent writes secrets into frontend code.
