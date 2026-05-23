# Capture Refund Void Misuse

## User Prompt

"The payment is authorized. Ship the order, mark it paid, and refund later if needed."

## Required Skill Use

The agent loads `capture-refund-void-lifecycle.md` and the provider reference.

## Expected Agent Behavior

- Separates `authorized` from `captured` or `paid`.
- Requires provider capture before final fulfillment where lifecycle requires capture.
- Uses void/cancel/release only before capture and refund only after paid/captured state.
- Stores operation idempotency keys.

## Fail If

- Agent treats authorized as settled.
- Agent cancels after capture instead of refunding.
- Agent refunds more than captured/paid amount.
- Agent retries capture without idempotency.
