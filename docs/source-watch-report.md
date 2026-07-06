# Source Watch Report

- Generated: 2026-07-06T07:14:18Z
- Total URLs checked: 107
- Changes detected: 0
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Classification: `payment_behavior_change`.

Private watcher issue #13 and run 28774155853 were reviewed after source snapshot capture and source-link checking completed successfully. The reviewed release-worthy changes were Tabby payment-webhook/dispute-webhook separation, Tabby's current 180-day refund initiation window, and Tamara's current 21-day auto-capture guidance for authorised but uncaptured orders.

Public-safe updates were applied to the Tabby and Tamara provider references, Tabby source metadata, focused eval coverage, changelog, version metadata, and the public-safe source-watch baseline. Other reviewed drift for Tap Payments, Geidea, MyFatoorah, and HyperPay was docs formatting, index, or source fingerprint churn rather than an unsupported payment guidance delta.

## Result

Public baseline refreshed after approved provider guidance updates.

## Manual Browser Verification

- https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/hmac/hmac-for-card-tokens.md
- https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/hmac/hmac-transaction-callback.md
- https://developers.paymob.com/paymob-docs/developers/webhook-callbacks-and-hmac/transaction-callbacks.md
- https://developers.paymob.com/paymob-docs/getting-started/integration-checklist.md
- https://developers.paymob.com/paymob-docs/getting-started/overview.md
- https://developers.paymob.com/paymob-docs/integration-paths/apis.md
- https://developers.paymob.com/paymob-docs/payments-and-features/managing-payments/capture.md
- https://developers.paymob.com/paymob-docs/payments-and-features/managing-payments/refund.md
- https://developers.paymob.com/paymob-docs/payments-and-features/managing-payments/void.md
- https://developers.paymob.com/paymob-docs/payments-and-features/payment-methods.md
- https://developers.paymob.com/paymob-docs/payments-and-features/payment-methods/bnpls-egy-ksa-uae.md
