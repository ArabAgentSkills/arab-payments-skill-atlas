# Source Watch Report

- Generated: 2026-08-31T10:27:56Z
- Total URLs checked: 110
- Changes detected: 0
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Classification: `payment_behavior_change`.

Private watcher issue #17 and runs 32695874748 and 33381932301 were reviewed after source snapshot capture completed before source-link checking. The current run reported source-change exit code `2`, source-link exit code `0`, artifact `9754111532`, and artifact digest `sha256:e771ad088a97364b37c3350c53bfbe23c4622c8d722908b9980d4e02c3592e38`.

The public-safe update covers current Tabby guidance for UAE/AED and Saudi Arabia/SAR scope, nested hosted-checkout URL extraction, merchant-code webhook registration, and duplicate-capture race handling. It also adds Tamara pre-check eligibility guidance before final checkout-session creation, and HyperPay handling for the `000.000.001` partially approved success result code.

Tap Payments Markdown URL hints, Geidea and MyFatoorah `llms.txt` index churn, Tamara index removals unrelated to current checkout/capture guidance, Tabby docs navigation/footer changes, and Paymob `JS_CHALLENGE` responses were reviewed as source-index or chrome noise rather than separate payment guidance changes.

## Result

Public baseline refreshed after reviewed payment guidance updates and source-watch normalization hardening. No provider documentation changes remain against the refreshed baseline.

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
