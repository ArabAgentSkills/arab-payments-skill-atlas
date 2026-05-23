# Idempotency And State Transitions

Use this pattern for all callback, webhook, inquiry, capture, void, refund, close, cancel, and retry logic.

## Durable Records

- Payment attempt: local order id, provider, country, amount, currency, local status.
- Provider event: provider event id or deterministic fingerprint, raw status, verified flag, received timestamp.
- Provider transaction: provider payment/order/transaction id, merchant reference, amount, currency, finality.
- Operation record: capture, refund, void, cancel, close, release, with local operation id and provider operation id.

## Transition Rules

- `pending` can move to `authorized`, `paid`, `captured`, `failed`, `cancelled`, `expired`, or manual review after verification.
- `authorized` can move to `captured`, `voided`, `cancelled`, expired, or manual review depending on provider.
- `paid` or `captured` must not be overwritten by stale `pending`, `failed`, `cancelled`, or duplicate signals.
- `refunded` and `partially_refunded` update value access according to business rules, not by deleting payment history.

## Idempotency Keys

- Use local order id plus provider payment id.
- Add operation ids for capture/refund/void/cancel.
- Use provider idempotency fields where documented, such as Tabby `reference_id`.

## Fail Closed

When status, amount, currency, country, or references do not match, write manual-review/pending state and do not fulfill.
