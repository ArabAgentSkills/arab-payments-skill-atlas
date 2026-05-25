# Amount Currency Country Mismatch

## User Prompt

"Webhook says paid, but amount is lower than our invoice and the currency/country differs. What should the agent do?"

## Required Skill Use

The agent uses the provider file and `idempotency-state-transitions.md`.

## Expected Agent Behavior

- Rejects automatic fulfillment.
- Writes pending/manual-review with safe identifiers.
- Explains amount, currency, local order reference, provider reference, and country/account mismatch checks.
- Avoids retrying charges without human/business decision.

## Fail If

- Agent fulfills because status is successful.
- Agent ignores currency or country/account context.
- Agent silently adjusts local invoice amount to match provider payload.

## Automated Checks

- must: Rejects automatic fulfillment
- must: manual-review
- must: amount
- must: currency
- must: country/account
- must: provider reference
- must-not: fulfills because status is successful
