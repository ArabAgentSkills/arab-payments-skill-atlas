# Source Watch Report

- Generated: 2026-09-07T22:03:16Z
- Total URLs checked: 114
- Changes detected: 0
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Classification: `payment_behavior_change`, with supporting `source_url_replacement` evidence for MyFatoorah refund documentation.

Private watcher issue #18 and run 34112647995 were reviewed after source snapshot capture completed before source-link checking. The run reported source-change exit code `2`, source-link exit code `0`, artifact `10014995338`, and artifact digest `sha256:9be8c99314ba3567522fbd0904dd7b9f9bd2818dd830760fe38de331068ee59a`.

The public-safe update covers current MyFatoorah refund source coverage and refund handling: Create Refund is a refund request, Refund Status Changed webhooks are the primary refund-state update path, Get Refund Details is the fallback, refund amount/account-base-currency/PaymentId checks are required, and duplicate partial-refund retries must be blocked with local idempotency.

PayTabs blank-line diffs, Tabby `llms.txt` docs-index cleanup, and local Tabby Retrieve Payment code-example formatting drift were reviewed as `chrome_noise`. Paymob JavaScript-challenge responses remain manual browser verification warnings, not broken source links. Kashier GitHub API records were reverified as `OK`.

## Result

Public baseline refreshed after reviewed MyFatoorah refund guidance and source-watch metadata updates. No provider documentation changes remain against the refreshed baseline.

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
