# Source Watch Report

- Generated: 2026-06-08T10:47:26Z
- Total URLs checked: 103
- Changes detected: 1
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Private watcher run 27130472493 detected a public EasyKash Pay API fingerprint change. Maintainer review found the current public docs still match the existing guidance for server-side Pay API creation, redirect-as-UX-only handling, callback HMAC verification, payment inquiry fallback, amount/currency/reference reconciliation, and idempotent fulfillment. No endpoint, auth/signature, status, test-card, adapter, eval, or payment-behavior guidance change was identified.

## Changes

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api

- Providers: egypt-payment-guardian:easykash, egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:easykash, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `b54419e36667b038ac2a73feae54e6193172c2d0913c8dd17d57dbed8dab799e`
- Current status: OK / hash `47ce711d80a40479484eeb590b88d9b80a050d98b67a0a209a025c156f4d6c1e`
- Excerpt: Pay API | EasyKash APIs EasyKash APIs \u2318 Ctrl k EasyKash APIs Direct Payment (Hosted) Pay API Callback Service Payment Inquiry Cash API (Cash-only) Direct Payment (WordPress WooCommerce Plugin) Direct Payment shopify plugin Powered by GitBook On this page Copy On this page Direct Payment (Hosted) Pay API API to create direct pay link Create direct pay link POST https://back.easykash.net/api/directpayv1/pay To get your api key, open your Integration Settings page Headers Name Type Description auth...

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
