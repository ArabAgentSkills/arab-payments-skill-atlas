# Capture Refund Void Lifecycle

Use this pattern when a provider or BNPL flow separates authorization, capture, cancel/void/release, close, or refund.

## State Meanings

- `created`: checkout/payment exists but is not approved.
- `authorized`: provider approved a hold or BNPL authorization; not necessarily settled.
- `captured`: merchant captured the authorized amount.
- `paid`: direct-sale payment completed without a separate capture step.
- `voided`, `released`, `cancelled`, or `closed`: authorization or uncaptured order is cancelled according to provider rules.
- `refunded`: captured/paid amount is returned in full or part.

## Safe Operation Rules

- Capture only from an authorized state where the provider supports capture.
- Void/release/cancel only before capture where provider docs allow it.
- Refund only captured/paid value and never exceed captured/paid amount.
- Store each operation with its own idempotency key.
- Reconcile operation webhooks/status inquiry before changing customer value access.

## Provider Examples

- Tabby: authorization requires capture; close cancels uncaptured payment; refund applies after capture.
- Tamara: approved notification must be authorised, then captured; cancel before capture; refund after capture.
- Moyasar: authorized is separate from captured; void/refund rules depend on state.
- Geidea, APS, PayTabs, HyperPay, MyFatoorah, Tap: capture/refund/void semantics are provider-operation-specific.
