# Source Watch Report

- Generated: 2026-08-17T07:17:45Z
- Total URLs checked: 109
- Changes detected: 0
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Classification: `payment_behavior_change`.

Private watcher issue #16 and runs through 32000027072 were reviewed after source snapshot capture completed before source-link checking. The public-safe update clarifies Tamara auto-authorisation: confirmed auto-authorisation reaches `authorised`, not capture or settlement, and capture remains a separate fulfillment step unless current merchant-specific docs or account settings prove otherwise.

Tap, Tabby, Tamara index, and HyperPay drift reviewed during this maintenance pass was source index, rendering, example, or endpoint-detail churn and was not treated as separate unsupported payment behavior guidance. Kashier GitHub source drift was source-watch API metadata recovery only. Paymob `JS_CHALLENGE` responses remain manual browser-verification warnings, not broken links.

## Result

Public baseline refreshed after the reviewed Tamara behavior correction, current source-watch normalization review, and token-aware GitHub API source checking. No provider documentation changes remain against the refreshed baseline.

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
