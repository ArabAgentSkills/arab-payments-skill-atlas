# Source Watch Report

- Generated: 2026-09-28T07:18:57Z
- Total URLs checked: 119
- Changes detected: 0
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Classification: `payment_behavior_change` for Tabby dispute webhook registration guidance, with non-release source-watch deltas treated as docs-index, heading, formatting, or GitBook chrome churn.

Private watcher issue #19 and run 36389511653 were reviewed after source snapshot capture completed before source-link checking. The run reported source-change exit code `2`, source-link exit code `0`, artifact `10956110613`, and artifact digest `sha256:3a58eb323377e8ce319cc17abb1cd03171bed1d4fda900d4941637e583912466`.

The public-safe update covers current Tabby dispute webhook source coverage and setup guidance: dispute webhook registration is separate from payment webhooks, uses the documented dispute-webhook API surface, requires merchant-code-aware registration, should not drive payment fulfillment/capture/refund/cancel state, and live dispute webhook settings must not be mutated without explicit approval.

Tap, Geidea, MyFatoorah, Tamara, and EasyKash source-watch diffs were reviewed as docs-index, heading, formatting, or GitBook chrome churn against existing public guidance. Paymob JavaScript-challenge responses remain manual browser verification warnings, not broken source links. Kashier GitHub API records were reverified as `OK` with authenticated source-watch metadata.

## Result

Public baseline refreshed after reviewed Tabby dispute webhook guidance and source-watch metadata updates. Authenticated `check_source_changes.py --check` verified that no provider documentation changes remain against the refreshed baseline.

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
