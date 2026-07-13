# Source Watch Report

- Generated: 2026-07-13T07:13:30Z
- Total URLs checked: 107
- Changes detected: 18
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Classification: `source_url_replacement`.

Private watcher issue #14 and run 29230960823 were reviewed after source snapshot capture completed before source-link checking. The reviewed public-safe update is limited to Tap Payments monitored source URLs: the provider's official `llms.txt` index now points to Markdown source variants, and those Markdown URLs preserve stable normalized content where extensionless HTML pages produced source-watch churn.

No payment behavior guidance changed. Tap, Geidea, MyFatoorah, Tabby, and Tamara diffs were reviewed as source URL, docs-index, code-example, or formatting churn. Paymob `JS_CHALLENGE` responses remain manual browser-verification warnings and were not treated as broken links.

## Result

Public baseline refreshed after approved source URL replacements and metadata review.

## Changes

### NEW: https://developers.tap.company/docs/authentication.md

- Providers: mena-payment-guardian:tap-payments
- Current status: OK / hash `8837398db3682a437379d01f371f6d9455e04a2c10b09400ba7c04b60489e915`
- Excerpt: # Authentication A detailed overview of API integration, workflow, and usage examples for 3D Secure authentication with Tap Payments. ## Overview This guide provides a comprehensive resource for implementing 3D Secure (3DS) authentication with Tap Payments, a security protocol that adds an extra layer of authentication to online credit and debit card transactions to reduce fraud and enhance customer trust. It details how Tap Payments handles 3DS authentication, including both internal processing...

### NEW: https://developers.tap.company/docs/get-started.md

- Providers: mena-payment-guardian:tap-payments
- Current status: OK / hash `2465e9e23b45e2bdd7eeeacd2f0e1cd62ab8a8c166927a4cbecf9fd86922aae6`
- Excerpt: # Overview This page guides you to set up your account with Tap, and start accepting online payments on your website or mobile App. ## 1. Registration You can create your account from here [Get-Started](https://tap.company/) <hr /> ## 2. Get Your API Keys Once registration has been completed, follow the steps below to get your API testing keys: 1. Sign in to [Tap\u2019s Dashboard](https://os.tap.company/) using your email or phone number 2. Click on Accounts 3. Click on the ID in the **Operators** se...

### NEW: https://developers.tap.company/docs/recurring-payments.md

- Providers: mena-payment-guardian:tap-payments
- Current status: OK / hash `1c42ed91aca4272ee96a832cf2e2f24ff78ecca937adfe8cd7016387a6a095c8`
- Excerpt: # Recurring Payments A Step-by-Step Documentation for Setting Up and Processing Recurring Payments Recurring payments allow merchants to charge customers on a regular basis, such as for subscriptions or installment plans. This guide provides a detailed guide on setting up and processing recurring payments using Tap APIs. Please note that this guide assumes you have already familiarized yourself with the API reference documentation for Tap Payments, specifically the [Charges](charges) API and [Au...

### NEW: https://developers.tap.company/docs/webhook.md

- Providers: mena-payment-guardian:tap-payments
- Current status: OK / hash `8c8970d47a6e41c2aa646833a442d5b3c3e3c4ee7e250f3e6170260af36e6394`
- Excerpt: # Webhook Tap ensures secure and realtime webhooks for payment events, and to send the post payment details. Payments webhook is a server-to-server call(also known as IPN "Instant Payment Notification"), that allows merchants to receive the post-payment details to automate and synchronize their internal ERPs by checking the actual payment status and other technical details, as per requirements. It's supported with all our APIs, SDKs & Libraries where it is required to be. Tap also triggers the w...

### CHANGED: https://developers.tap.company/llms.txt

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `d337d529523e15c13cdcd8be3847b671dc60e668f51d580d02273351d3248bc4`
- Current status: OK / hash `4ef23d011821f1938542fb08957e009eed5d1df9734b5332706515c96b3c4226`
- Excerpt: # Tap API Docs 1.0 Documentation > Documentation for Tap API Docs 1.0 ## Guides - [Overview](https://developers.tap.company/docs/get-started.md) - [Authentication](https://developers.tap.company/docs/authentication.md): A detailed overview of API integration, workflow, and usage examples for 3D Secure authentication with Tap Payments. - [Recurring Payments](https://developers.tap.company/docs/recurring-payments.md): A Step-by-Step Documentation for Setting Up and Processing Recurring Payments -...

### NEW: https://developers.tap.company/reference/api-actions.md

- Providers: mena-payment-guardian:tap-payments
- Current status: OK / hash `1369224591c01ff2ef4aadb95702079432a7b340b615113adde1f8100640a313`
- Excerpt: # API Actions You can perform the following API actions on payments: ## Capture a payment If your transaction is AUTHORIZED using the [Authorize API](https://tappayments.readme.io/reference/create-an-authorize), and you want to CAPTURE it, you can use the [Create a Charge API](https://tappayments.readme.io/reference/create-a-charge) and provide the Authorize ID ## Retrieve the details of a payment If you would like to retrieve the details of a payment at any stage of the payment transaction life...

### CHANGED: https://docs.geidea.net/llms.txt

- Providers: egypt-payment-guardian:egypt-bnpl-methods, egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `d1ae1de9f8e3f5ff8a6135aed62b61b8c8f049c31935dc0b36258bdc3f0cb06f`
- Current status: OK / hash `efdd9c270c8feec71f4c89214a7fc2ded01ccb9741474752b541e5955d16dd02`
- Excerpt: # Geidea Documentation > Documentation for Geidea ## Guides - [Overview](https://docs.geidea.net/docs/overview.md) - [Pre-requisites](https://docs.geidea.net/docs/pre-requisites.md) - [Geidea HPP Checkout](https://docs.geidea.net/docs/geidea-checkout-v2.md) - [Express Checkout (Wallets)](https://docs.geidea.net/docs/express-checkout-wallets.md): Allow customers to pay instantly with Apple Pay, Google Pay, or Samsung Pay \u2014 no card entry required. - [Pay by Link (Egypt & UAE)](https://docs.geidea....

### CHANGED: https://docs.myfatoorah.com/llms.txt

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `78d470dc063f6665ce972854f1289d008f5f64be5d7d49b689cf1f605ee02f9c`
- Current status: OK / hash `91bc082f258ff9bc9ef85d9ea5e81e70e002234fc05bace7e48f9ae2ca909439`
- Excerpt: # MyFatoorah API Documentation > MyFatoorah Main API & E-commerce Plugins ## Guides - [Get Started](https://docs.myfatoorah.com/docs/get-started.md): Build your integration and start accepting payments online - [Live Account](https://docs.myfatoorah.com/docs/live-account.md): How to create your account with MyFatoorah? - [Account Information](https://docs.myfatoorah.com/docs/account-information.md) - [Orders Information](https://docs.myfatoorah.com/docs/orders-information.md) - [API Key](https:/...

### CHANGED: https://docs.tabby.ai/api-reference/checkout/create-a-session

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `2f78378f1375d1a9037fa4eeab3b6220215ae3aaf4c804dd2dbd8fb7c2da326d`
- Current status: OK / hash `d9ed855c456824a6c32f9aa493ecaeff527fbf5ebbd4f0d1e7d09795fbea8ce8`
- Excerpt: Create a session cURL curl --request POST \ --url https://api.tabby.ai/api/v2/checkout \ --header 'Authorization: Bearer <token>' \ --header 'Content-Type: application/json' \ --data ' { "payment": { "amount": "100", "currency": "AED", "buyer": { "name": "John Doe", "email": "jsmith@example.com", "phone": "500000001", "dob": "2000-01-20" }, "shipping_address": { "city": "Dubai", "address": "Dubai", "zip": "1111" }, "order": { "reference_id": "1001", "items": [ { "title": "Name of the product", "...

### CHANGED: https://docs.tabby.ai/api-reference/payments/retrieve-a-payment

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `63a1f0f463b5658a4502ec33d3d8ff7fe797d28fcb89d8ebbfa8b7f75473da67`
- Current status: OK / hash `5988b691c9c0c7027fd3be464a38e72d8900718cb036021ff465e9447e8fea15`
- Excerpt: Retrieve a payment cURL curl --request GET \ --url https://api.tabby.ai/api/v2/payments/{id} \ --header 'Authorization: Bearer <token>' import requests url = "https://api.tabby.ai/api/v2/payments/ {id} " headers = { "Authorization" : "Bearer <token>" } response = requests.get(url, headers =headers) print (response.text) const options = { method: 'GET' , headers: { Authorization: 'Bearer <token>' }}; fetch ( 'https://api.tabby.ai/api/v2/payments/{id}' , options ) . then ( res => res . json ()) ....

### CHANGED: https://docs.tabby.ai/llms.txt

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `3b58681bc4accb36aa6caa4539e56537218d9ab2f8f673f4eb85955e5438da0c`
- Current status: OK / hash `1b94cb99213215140c2b5370f82d9aa7612dce2913ffc55d734fea46536f4914`
- Excerpt: # Tabby ## Docs - [Create a session](https://docs.tabby.ai/api-reference/checkout/create-a-session.md): Creates a Checkout session. Creates Session and Payment, returns Pre-Scoring result (status), ids of Payment and Session. - [Session creation payload model](https://docs.tabby.ai/api-reference/checkout/session-payload-model.md) - [Approve disputes](https://docs.tabby.ai/api-reference/disputes/approve-disputes.md): Approve disputes (refund money to the customer). Only 20 disputes can be approve...

### CHANGED: https://docs.tamara.co/docs/online-order-status-flow

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `19229a3c6b5fe5a8fc301b58ca4afaf48f6f9152ac36dcc0967080c6a0695abf`
- Current status: OK / hash `262b656d7c6985d27fd8db898002d145ece7f83299b51acc2e096d830a6c8fc8`
- Excerpt: Online Order Status Flow To integrate with Tamara and connect your e-commerce platform with our service, it is necessary to fully understand how the flow of our order statuses work and map them to your system\u2019s statuses. \U0001f449 Click on any status in the flow to learn more about it. Online Order Status Flow Online Order Status Description new Customer has initiated the checkout session with Tamara as a payment method. declined Customer was declined to continue the payment with Tamara . expired Custom...

### CHANGED: https://docs.tamara.co/llms.txt

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `fe0f899b780c35e00e8933df1458512507aa35d0532c095973a4b315568d9547`
- Current status: OK / hash `880bafcb87ae7be86834fb0075cf151d40cd7347b9b3c8b0bc0214c1d5e807f4`
- Excerpt: # Tamara Documentation and APIs Hub Documentation > Discover the ultimate toolkit right here, enabling you to seamlessly integrate Tamara's payment solution into your site with detailed guides and an interactive API explorer at your fingertips. ## Guides - [Get to know Tamara](https://docs.tamara.co/docs/introduction-to-tamara.md): Learn more about **Tamara**'s product offerings and how we can help you and your customers! - [Platforms Quick Start](https://docs.tamara.co/docs/platforms-quick-star...

### REMOVED: https://developers.tap.company/docs/authentication

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `d431bfe5b9c12b10ad079d1615abc9544f6237405187859776437f56426ee0ef`

### REMOVED: https://developers.tap.company/docs/get-started

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `fe1c892c3e9e84e9b279ce72098fbce810dfd97c1737c096bf96a5c694af628a`

### REMOVED: https://developers.tap.company/docs/recurring-payments

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `8aaeec8c5e5e7cdc3fcf2ebcba999ba66c6be5638073bf1aa24a1ff5dee7dd12`

### REMOVED: https://developers.tap.company/docs/webhook

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `a3e018ea60989feb69b93151b23b8b7b4fafdbd2d373ad91a590cd14aa9e2fdb`

### REMOVED: https://developers.tap.company/reference/api-actions

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `4cc236197baafa3170048fec8a8268480da73429fe6e263cc613d5eeee7d5af3`

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
