# Idempotency And State Transitions

## Principle

Every payment event can be delivered more than once, out of order, or after a user refresh. Durable uniqueness and explicit transitions are required.

## Minimal Data Model

Use equivalent fields in the target stack:

- `payment_attempts`
  - local attempt id
  - local order/user id
  - provider id
  - provider order/reference
  - expected amount
  - expected currency
  - status
  - created/updated timestamps
- `payment_events`
  - local event id
  - payment attempt id
  - provider event/reference id
  - provider status
  - verified boolean
  - raw payload storage policy or safe summary
  - received timestamp

## Uniqueness

Add uniqueness around:

- local order id plus provider id for active attempts where appropriate
- provider transaction/reference id
- provider event id when available
- merchant reference/customer reference when provider uses merchant-provided references

## Transition Rules

- `pending -> paid` only from verified provider success plus amount/currency/reference match.
- `pending -> failed/cancelled/expired` only from verified provider status.
- `paid -> refunded/partially_refunded/voided` only from verified refund/void event or confirmed server-side operation.
- `paid` must not become `failed`, `cancelled`, `expired`, or `pending` from a stale event.
- Duplicate events return success to the provider after confirming no new side effect is needed.

## Side Effects

Run fulfillment after the paid transition commits. If possible, make fulfillment itself idempotent by unique order/subscription/enrollment keys.

## Fail The Review If

- The same provider callback can insert two paid rows.
- Fulfillment happens before the payment event is stored.
- A later failed callback can erase paid state.
- The code has no amount/currency mismatch branch.
