# Source Watch Report

- Generated: 2026-06-01T11:54:47Z
- Total URLs checked: 103
- Changes detected: 1
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Release v1.0.6 supersedes the v1.0.5 validation attempt and handles source-watch CI noise only. GitHub Actions run 26749516850 failed on MyFatoorah hashes after public docs chrome moved from `Updated 3 months ago` to `Updated 4 months ago`; local validation also exposed transient HyperPay navigation chrome around `Board of Directors` / `Contact us`. After v1.0.5 was published, workflow-dispatch run 26753574735 passed `validate` and source-link reachability, then failed source-change hashing on transient FawryPay `URLError` fetches. Maintainer review found no provider behavior, endpoint, auth/signature, status, test-card, adapter, or eval guidance change.

## Changes

### CHANGED: https://www.hyperpay.com/integration-guide/

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `e80feb8ef12482f6a58ca78c5e14ac4a442c9206ef5a3d43f4089780c2d15a9a`
- Current status: OK / hash `00f5de183272e1b46b8c3174d138ac149e6fd79a210663b1a9b5e386e6c5b7de`
- Excerpt: Integration Guide - HyperPay Products Payments Billing Payout Protect Hospitality Hypertap Services Recurring billing Data reporting Merchants mobile app Partner Program Blogs Board of Directors Products Payments Billing Payout Protect Hospitality Hypertap Services Recurring billing Data reporting Merchants mobile app Partner Program Blogs Board of Directors Contact us \u0627\u0644\u0639\u0631\u0628\u064a\u0629 Contact us \u0627\u0644\u0639\u0631\u0628\u064a\u0629 Integration Guides The HyperPay platform offers a complete, easy-to-use guide to enable seamless inte...

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
