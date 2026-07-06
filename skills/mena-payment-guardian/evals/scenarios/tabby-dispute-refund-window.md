# Tabby Dispute And Refund Window

## User Prompt

"Tabby sent a dispute webhook and the customer wants a refund after checkout. Can we mark the order refunded and stop fulfillment?"

## Required Skill Use

The agent loads `tabby.md`, `webhook-first-fulfillment.md`, and `capture-refund-void-lifecycle.md`.

## Expected Agent Behavior

- Separates Tabby payment webhooks from opt-in dispute webhooks.
- Refuses to treat a dispute webhook as payment authorization, capture, refund, or fulfillment state.
- Retrieves the payment before changing payment state.
- Refunds only a captured or closed payment, never more than the captured amount.
- Checks the current documented refund window, including the 180-day initiation window, before advising refund execution.
- Uses `reference_id` idempotency for refund retries.

## Fail If

- Agent marks the order paid, refunded, or canceled from a dispute webhook alone.
- Agent refunds an uncaptured or non-closed payment.
- Agent ignores the documented refund window or captured amount.
- Agent retries a refund without idempotency.

## Automated Checks

- must: dispute webhook
- must: payment webhooks
- must: retrieves the payment
- must: captured or closed payment
- must: 180-day
- must: reference_id
- must-not: dispute webhook alone
- must-not: uncaptured
