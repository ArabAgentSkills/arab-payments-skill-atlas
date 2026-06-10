# Source Watch Report

- Generated: 2026-06-10T17:45:37Z
- Total URLs checked: 103
- Changes detected: 8
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Private watcher runs 27294185835 and 27294164650 detected current public source fingerprint drift. Maintainer review classified the stable changes as docs-site chrome, navigation, and agent-readable index churn for FawryPay, MyFatoorah, Tabby, Tamara, and EasyKash. One extra Kashier GitHub API HTTP 504 in run 27294164650 was a transient fetch warning because the same source was reachable in link checking and did not recur in run 27294185835. No endpoint, auth/signature, webhook, status, amount/currency, refund/capture/void, test-card, adapter, eval, or payment-behavior guidance change was identified.

## Changes

### CHANGED: https://developer.fawrystaging.com/docs/introduction

- Providers: egypt-payment-guardian:fawrypay, mena-payment-guardian:fawrypay
- Previous status: OK / hash `d2306d6cf55e8a3dd390dae1b030dca88622ef4735e002a864004eec8fba4838`
- Current status: OK / hash `646f53fac93610ab8a91cca60d5b2354f668cb329cc3a9b806653a494db1bcb4`
- Excerpt: FawryPay-Documentation Let's start Support Ticket Tracking Home Getting Started Integration Guide Online Payments Overview Express Checkout Overview Checkout Button Integration Checkout Link Integration myFawry App Payment ValU Hosted Payment Migrate From Legacy Checkout Plugin Server-Side APIs Overview Pay Using Card Pay Using Card Moto Authorize and Capture Payments E-Wallet Payments Payment Request using Reference Number myFawry App Payment Pay Using Bank Installments Refund API Cancel Unpaid...

### CHANGED: https://docs.myfatoorah.com/llms.txt

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `8cf19e480acb6d128b7364f1e078f6d78950d9641eb1bf603d555015f04ce037`
- Current status: OK / hash `aefcbca796563e16247027396d95a5259a37a367bd744bd2a1e221a18b395f94`
- Excerpt: # MyFatoorah API Documentation ## Guides - [Card Verification](https://docs.myfatoorah.com/docs/card-verification.md) - [Features](https://docs.myfatoorah.com/docs/features.md) - [Get Payment Details](https://docs.myfatoorah.com/docs/get-payment-details.md) - [Updating Payment Status Guidelines](https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines.md) - [Idempotency](https://docs.myfatoorah.com/docs/idempotency.md) - [Bypass 3DS](https://docs.myfatoorah.com/docs/bypass3ds.md) -...

### CHANGED: https://docs.tabby.ai/api-reference/checkout/create-a-session

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `9f3f5fec6d5e7f82f04501381be372e19b55cc7ace742499fc2d13ce53e7ea04`
- Current status: OK / hash `8768cb80deb18e42130eb6c481cc3c8fd8e9cd69b4d3309f756771d2d74ce617`
- Excerpt: Create a session - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Checkout Create a session Documentation API Playground Marketing Toolkit API Playground API Reference Documentation Checkout POST Create a session Session creation payload model Payments GET Retrieve a payment PUT Update a payment POST Capt...

### CHANGED: https://docs.tabby.ai/api-reference/payments/retrieve-a-payment

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `b3e0e85ad4285dae2e75ac5dfbd9815fd9a70a7af039de153281dd7cb27b7501`
- Current status: OK / hash `f9fbf1edcb8596818cb43cb64d478fa51185e9636975c2a8807d6d4bad04193d`
- Excerpt: Retrieve a payment - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Payments Retrieve a payment Documentation API Playground Marketing Toolkit API Playground API Reference Documentation Checkout POST Create a session Session creation payload model Payments GET Retrieve a payment PUT Update a payment POST...

### CHANGED: https://docs.tamara.co/docs/online-order-status-flow

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `e5dcb889d6b24bfb916df97a1d88b26296dc65b88f86ffe10385fe84358862e2`
- Current status: OK / hash `55406d8c9822b30e5fbf05f7dae30524266503806bc7a3e890b35947646c88e9`
- Excerpt: Online Order Status Flow For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login Guides System Status Support Business Login Guides Online Order Status Flow Online Order Status Flow \U0001f44b Introduction Get to know Tamara \U0001f6d2 E-Commerce Platforms Platforms Quick Start ExpandCart FatherS...

### CHANGED: https://docs.tamara.co/docs/transaction-authorisation

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `5e210ff99b2836e488a0f0c1ac9965126f5a8e23415138fe9b627c355831a499`
- Current status: OK / hash `310bb1a2cb0db96a52042cbf7b318bde3978b8f2c1de57ad68c0a2b6cf486974`
- Excerpt: Webhook Registration & Order Authorisation For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login Guides System Status Support Business Login Guides Webhook Registration & Order Authorisation Webhook Registration & Order Authorisation \U0001f44b Introduction Get to know Tamara \U0001f6d2 E-Comme...

### CHANGED: https://docs.tamara.co/llms.txt

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `79d6528576ba8497aae33d61a057858f1d418a22d14bf5d4c4345c106b7d7074`
- Current status: OK / hash `12f41deb422b561a830b3d10e93a9b80dd5d5f2c22ae4304f2bfa0bcaa98871d`
- Excerpt: # Tamara Documentation and APIs Hub Documentation ## Guides - [Get to know Tamara](https://docs.tamara.co/docs/introduction-to-tamara.md): Learn more about **Tamara**'s product offerings and how we can help you and your customers! - [Educational Institutions](https://docs.tamara.co/docs/education.md): For merchants with educational institutions, such as schools, colleges, etc. - [General](https://docs.tamara.co/docs/general-risk-assessment.md): For all merchant categories - [Hotel Booking](https...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api

- Providers: egypt-payment-guardian:easykash, egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:easykash, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `47ce711d80a40479484eeb590b88d9b80a050d98b67a0a209a025c156f4d6c1e`
- Current status: OK / hash `6753c05afc62cdf9685429920f7b2421e509ed4419973598cf0b297245a383fb`
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
