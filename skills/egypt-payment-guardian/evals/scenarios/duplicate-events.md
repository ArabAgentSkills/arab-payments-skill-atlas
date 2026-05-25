# Eval: Duplicate Events

## User Prompt

"Our provider callback sometimes retries three times and users refresh the success page. Make sure paid orders are created."

## Required Skill Use

Load `references/patterns/idempotency-state-transitions.md`.

## Expected Agent Behavior

- Creates or uses uniqueness around provider reference/event IDs.
- Stores payment event before fulfillment.
- Makes fulfillment idempotent.
- Returns success for duplicate verified callbacks without repeating side effects.
- Prevents success page refresh from calling fulfillment directly.

## Fail If

- Duplicate callbacks create duplicate subscriptions, bookings, invoices, credits, or paid records.
- Fulfillment happens before event persistence.
- No unique provider reference is stored.

## Automated Checks

- must: unique
- must: provider reference
- must: event before fulfillment
- must: idempotent
- must: duplicate verified callbacks
- must-not: duplicate subscriptions
