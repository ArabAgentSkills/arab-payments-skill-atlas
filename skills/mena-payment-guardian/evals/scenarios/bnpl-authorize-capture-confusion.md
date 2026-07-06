# BNPL Authorize Capture Confusion

## User Prompt

"Tabby/Tamara approved the customer. Can we activate the subscription and ship immediately?"

## Required Skill Use

The agent loads `tabby.md` or `tamara.md` plus `capture-refund-void-lifecycle.md`.

## Expected Agent Behavior

- Explains approval/authorization is not the same as capture/settlement.
- For Tabby, retrieves payment status and captures with idempotent `reference_id` where required.
- For Tamara, verifies approved webhook token/header, calls Authorise Order, then captures according to fulfillment rules.
- For Tamara, notes the current 21-day auto-capture window for authorised but uncaptured orders without treating approval or authorisation as fulfilled settlement.
- Blocks final fulfillment until the provider state supports it.

## Fail If

- Agent ships from BNPL approval screen alone.
- Agent skips Tabby retrieve payment or Tamara Authorise Order.
- Agent mixes cancel/close/refund semantics.

## Automated Checks

- must: approval/authorization is not the same as capture/settlement
- must: retrieves payment status
- must: idempotent `reference_id`
- must: Authorise Order
- must: captures
- must: 21-day auto-capture window
- must-not: ships from BNPL approval screen alone
