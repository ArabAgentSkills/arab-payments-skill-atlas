# HyperPay Partial Approval

## User Prompt

"HyperPay returned result code 000.000.001. It says succeeded, so unlock the whole order and ship everything."

## Required Skill Use

The agent loads `hyperpay.md`, `webhook-first-fulfillment.md`, and `idempotency-state-transitions.md`.

## Expected Agent Behavior

- Recognizes `000.000.001` as a succeeded but partially approved result code.
- Checks amount, currency, merchant reference, provider transaction id, and local order policy before fulfillment.
- Does not fulfill the full order unless the approved amount covers the obligation or partial payment is explicitly supported.
- Keeps the payment in a partial or manual-review state when the approved amount does not match the full local order.
- Handles subsequent webhook/status messages idempotently.

## Fail If

- Agent treats partial approval as full payment without checking amount and order policy.
- Agent fulfills the full order when the approved amount is below the local order total.
- Agent ignores transaction status query or encrypted webhook verification.
- Agent creates duplicate fulfillment on later webhook messages.

## Automated Checks

- must: `000.000.001`
- must: partially approved
- must: amount, currency
- must: merchant reference
- must: local order policy
- must: partial or manual-review
- must: idempotently
- must-not: full payment
- must-not: ship everything
