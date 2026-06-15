# Source Watch Report

- Generated: 2026-06-15T07:14:20Z
- Total URLs checked: 106
- Changes detected: 52
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Private watcher run 27529717585 detected current public source fingerprint drift. Maintainer review classified the Moyasar webhook-reference delta as `payment_behavior_change` because the official docs added standalone 3D Secure card-authentication webhook events and clarified that card-authentication payloads are distinct from payment payloads. The public update adds conservative Moyasar guidance, monitored card-authentication source URLs, and an eval scenario without copying full provider snapshots.

Concurrent Tap Payments, Geidea, MyFatoorah, Tabby, Tamara, and EasyKash fingerprint drift was reviewed as docs-site navigation, agent-readable index, and page chrome churn. Link checking completed successfully; Paymob browser-verification warnings remain manual-review warnings, not confirmed broken links. No source URL replacement was identified.

## Changes

### CHANGED: https://developers.tap.company/docs/authentication

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `6c693afc631203c378e060faa638bb1385802b967a79898f7dd375d17041fd83`
- Current status: OK / hash `f05041bc03b74409ae497d8c643b625aaeca7a6c8935351bf8d6a364491feba0`
- Excerpt: Authentication For AI agents: visit https://developers.tap.company/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Home Guides API Reference Home Log In Guides Log In Home Guides API Reference Authentication Get Started Overview Acceptance Authentication Saved Cards Payment Agreement and Contracts Creating Payment Agreement Merchant Initiated Transaction Liability Shift: Customer vs Merchant Recurring Payments SDK BenefitPay Benefit Pay Web...

### CHANGED: https://developers.tap.company/docs/get-started

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `7f24b5326729df56a5244f573ac072df24d8467b99c359060bf4c6e8f4114979`
- Current status: OK / hash `d0d6185bb6e3154844d34ba371f4ef7cf760d6865ba7737dddec056ff96e8dc3`
- Excerpt: Overview For AI agents: visit https://developers.tap.company/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Home Guides API Reference Home Log In Guides Log In Home Guides API Reference Overview Get Started Overview Acceptance Authentication Saved Cards Payment Agreement and Contracts Creating Payment Agreement Merchant Initiated Transaction Liability Shift: Customer vs Merchant Recurring Payments SDK BenefitPay Benefit Pay Web SDK Checkou...

### CHANGED: https://developers.tap.company/docs/recurring-payments

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `3dcc415d067237aa8aae9f067fce50b244baee0c8036cc3d77466d299e38650d`
- Current status: OK / hash `732448f73edaa07b8cf19bdbf189a8a6b288540e30f1b2b096066facaaf2a524`
- Excerpt: Recurring Payments For AI agents: visit https://developers.tap.company/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Home Guides API Reference Home Log In Guides Log In Home Guides API Reference Recurring Payments Get Started Overview Acceptance Authentication Saved Cards Payment Agreement and Contracts Creating Payment Agreement Merchant Initiated Transaction Liability Shift: Customer vs Merchant Recurring Payments SDK BenefitPay Benefit...

### CHANGED: https://developers.tap.company/docs/webhook

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `5525fd9dcdcb04aaa8fbeccfee573e7c86c4ccf6437af4124f100f5bc05f4b96`
- Current status: OK / hash `08005dd39c2e0c65471da751c00560ffe1cdc1c792ae1099821ff63df5a3692f`
- Excerpt: Webhook For AI agents: visit https://developers.tap.company/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Home Guides API Reference Home Log In Guides Log In Home Guides API Reference Webhook Get Started Overview Acceptance Authentication Saved Cards Payment Agreement and Contracts Creating Payment Agreement Merchant Initiated Transaction Liability Shift: Customer vs Merchant Recurring Payments SDK BenefitPay Benefit Pay Web SDK Checkout...

### CHANGED: https://developers.tap.company/reference/api-actions

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `68046607cc4f81bffc8e9508e331afb8eefb3c05670930ce0952aa4ae420d0c0`
- Current status: OK / hash `31c5bcf453cb659074201562f9db3b8085e743db8da710368db206b3cb6a90f9`
- Excerpt: API Actions For AI agents: visit https://developers.tap.company/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Home Guides API Reference Home Log In API Reference Log In Home Guides API Reference API Actions JUMP TO API Actions Copy Page You can perform the following API actions on payments: Updated about 1 year ago Updated about 1 year ago

### CHANGED: https://docs.geidea.net/

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `aad74baefdfd0440588ce9724e6b92ca17ab4c8779d1a350d3e4a14ce8d2abf4`
- Current status: OK / hash `651cc3d52107e9da94603406d954b0acb6e80def8557d0ae02757d1365b0313c`
- Excerpt: Overview For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Overview Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Portal [KSA] Direct API...

### CHANGED: https://docs.geidea.net/docs/buy-now-pay-later-bnpl

- Providers: egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `e3074a0cb6fce830a069e224075fa30a1450f7b469c012a23aa1d679b5dbddc7`
- Current status: OK / hash `cbfc8c2d4e97f19a68acc61eef76bf415d8d98eb9872c9ff73bd6cc34a2ea928`
- Excerpt: Buy Now Pay Later (BNPL) For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Buy Now Pay Later (BNPL) Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by I...

### CHANGED: https://docs.geidea.net/docs/cancel-order-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `d1f5dda2f2df353f5909edc3916e9423665c40a8a51f8beac36baeb49a817a3d`
- Current status: OK / hash `ded4ee10305fcd9f39d9ab3e80cf3b22f1c9a8a171ef4f2021d39cf58287c7d6`
- Excerpt: Cancel Order For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Cancel Order Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Portal [KSA] Di...

### CHANGED: https://docs.geidea.net/docs/geidea-checkout-v2

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `6ea52fda4373827b18e75a26fe9dfb1c94ccbc96176b43911d87f1ffbb54d1a8`
- Current status: OK / hash `a40d1ec8a9ceb419cce7702585dc0716f9831ad7e090efba444016647727188d`
- Excerpt: Geidea HPP Checkout For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Geidea HPP Checkout Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - P...

### CHANGED: https://docs.geidea.net/docs/overview-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `d3288526422ca88ff2fde9e89dd94a2f263295740831653e74c0c93e2c0c2dc0`
- Current status: OK / hash `2a97f1f27b783a0f43941e3685de6036fd3673d033b45034b2ac818c8e67293f`
- Excerpt: Transaction and Order Management For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Transaction and Order Management Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice...

### CHANGED: https://docs.geidea.net/docs/pay-by-link-apis

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `0f6f4b5be970951bc0f447487ea57232263e33aa754c2688bd0fd830ecf53a62`
- Current status: OK / hash `ccb1b45209a96fb07daf5831925b4d46909aead1907e3f3b068a4db2c5ce992f`
- Excerpt: Pay by Link - APIs For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Pay by Link - APIs Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Por...

### CHANGED: https://docs.geidea.net/docs/pay-v2

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `1bc3130ff650ca8bb19589183de047aa309f68b93a4a2b9b3423ccd07dbce0bf`
- Current status: OK / hash `165aeeedde35094886dd081c8017622e696ae3f674d3141996763a8c1e88bcb8`
- Excerpt: Pay For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Pay Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Portal [KSA] Direct API Integrati...

### CHANGED: https://docs.geidea.net/docs/refund-2

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `adba825f91089c0f5228e0febdd10230a87c7dd81468d1887cc7e4c391dd74e5`
- Current status: OK / hash `fa18b6c1e9438dd91dd62dbe066df46b072e2213a44961ab7a6a34bac6e9e827`
- Excerpt: Refund For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Refund Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Portal [KSA] Direct API Int...

### CHANGED: https://docs.geidea.net/docs/sample-callback-responses

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `9f3297b07a90ad1305943f8de44fe7d46d264dcd136c7a587b8b79ab40cba092`
- Current status: OK / hash `081fc713b3d48c2d4b9f5c803fb3db73aa4529360f409fabff303ae50bbdb5e2`
- Excerpt: Webhook/Callback Notifications For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Webhook/Callback Notifications Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - A...

### CHANGED: https://docs.geidea.net/docs/souhoola

- Providers: egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `1b5e71ece96709f6cd25b55f410b86ce1cc9a55b5aa26ef98e999dda1f318cac`
- Current status: OK / hash `6b5cc4fc37060025aef03e1dc1be7f8058e392d5190f40e8a1abbdadeb1aa065`
- Excerpt: Souhoola [Egypt] For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Souhoola [Egypt] Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Portal...

### CHANGED: https://docs.geidea.net/docs/valu

- Providers: egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `560835c545d8011afe17376bcff20ade267f93155185994dbecca5160bb76ad2`
- Current status: OK / hash `12e5c00d08f5f8b6df42cea1a2cd43a450133cbbd1e5ab1d1279802318644802`
- Excerpt: ValU [Egypt] For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference ValU [Egypt] Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Portal [KSA] Di...

### CHANGED: https://docs.geidea.net/docs/void-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `f15a60aa6a76bca7f29706d8b0c46d6a2da1b49ca693fd1da27617c8b95f3a3f`
- Current status: OK / hash `39bc385c969273c7482fb546c884c06e81f397cc647fa88164d6d167b0f81a61`
- Excerpt: Void For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea Docs geidea Docs API Reference Void Getting Started Overview Pre-requisites Geidea HPP Checkout Express Checkout (Wallets) Pay by Link (Egypt & UAE) Pay by Link - Portal [Egypt] Pay by Link - Portal [UAE] Pay by Link - APIs Pay by Invoice (KSA) Pay by Invoice - APIs Pay by Invoice - Portal [KSA] Direct API Integra...

### CHANGED: https://docs.geidea.net/reference/capture-transaction-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `394ce49a2db5ca3c5f8aeac1df3e3e7e4a125445bd07b3f0b9c47d8189fc486d`
- Current status: OK / hash `767d3e2678ea26e1e40b035a9888497d1a02b6d6a69a37d82ffcbc78f7d1c1ea`
- Excerpt: Capture Transaction For AI agents: visit https://docs.geidea.net/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Home Docs API Reference Home geidea API Reference geidea Docs API Reference Capture Transaction JUMP TO Powered by Capture Transaction Copy Page post https://api.ksamerchant.geidea.net /pgw/api/v1/direct/capture Recent Requests Log in to see full request history Time Status User Agent Retrieving recent requests\u2026 Loading Loading\u2026 Body...

### CHANGED: https://docs.moyasar.com/api/authentication/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `66fef518a9bec2d98b85112bd45ea532c766d55e2c4d92eedba42f400fca3753`
- Current status: OK / hash `1609c4b152e231bf9de07bc6051374f9e33af34165f7587b3a72d2bbdd4fdae3`
- Excerpt: Authentication | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard API Introduction Authentication Pagination Metadata Idempotency Payments API Card Authentication API Invoices API Payouts API Settlement API Internal Transactions API Sources API Other APIs Errors Authentication On this page Authentication Introduction \u200b Moyasar's API uses API Keys to authenticate requests. You can view and manage your API keys in the Moy...

### NEW: https://docs.moyasar.com/api/card_auths/01-create-card-auth

- Providers: mena-payment-guardian:moyasar
- Current status: OK / hash `2cee9b5c183e0fd565380811ad274521eb76439f5be872fbc1e9a84f40dc102c`
- Excerpt: Create Card Authentication | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard API Introduction Authentication Pagination Metadata Idempotency Payments API Card Authentication API Create Card Authentication Fetch Card Authentication Invoices API Payouts API Settlement API Internal Transactions API Sources API Other APIs Errors Card Authentication API Create Card Authentication Create Card Authentication POST /card_auths...

### NEW: https://docs.moyasar.com/api/card_auths/02-fetch-card-auth

- Providers: mena-payment-guardian:moyasar
- Current status: OK / hash `c724113682fc93664fcea9cf299f4687fc7eed9245da5d9b5312003276a780d6`
- Excerpt: Fetch Card Authentication | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard API Introduction Authentication Pagination Metadata Idempotency Payments API Card Authentication API Create Card Authentication Fetch Card Authentication Invoices API Payouts API Settlement API Internal Transactions API Sources API Other APIs Errors Card Authentication API Fetch Card Authentication Fetch Card Authentication GET /card_auths/:id...

### CHANGED: https://docs.moyasar.com/api/other/webhooks/webhook-reference

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `2c00ca894862d43001683a24f8c6f99eb9234f245d19546538bd3fd4d1711c95`
- Current status: OK / hash `ca5fa3dab79d6f0de850294d0a4042e3df15c8d1b5eb81a0e1c45fbec9a203e5`
- Excerpt: Webhook Reference | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard API Introduction Authentication Pagination Metadata Idempotency Payments API Card Authentication API Invoices API Payouts API Settlement API Internal Transactions API Sources API Other APIs Tokens Apple Pay Webhooks Attempts Create Webhook Fetch Webhook List Webhooks Available Webhooks Delete Webhook Webhook Reference Transfers Errors Other APIs Webhoo...

### CHANGED: https://docs.moyasar.com/category/payments-api/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `0a2850f5c6eb4d414e5d2eb7cde356180e649791551b6112157a7479430ba735`
- Current status: OK / hash `f1b05ebf8cfa43c8e53bade7355dfe01231d761c2bdd08b7c7802e27a70095b0`
- Excerpt: Payments API | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard API Introduction Authentication Pagination Metadata Idempotency Payments API Create Payment Fetch Payment List Payments Update Payment Refund Payment Capture Payment Void Payment Payment Status Reference Card Authentication API Invoices API Payouts API Settlement API Internal Transactions API Sources API Other APIs Errors Payments API Payments API Complete...

### NEW: https://docs.moyasar.com/guides/3d-secure/standalone-authentication

- Providers: mena-payment-guardian:moyasar
- Current status: OK / hash `3bcbef2ba5db5746f9a9b3e0253b8e4b30e2c8ed00b8055f8bf46fa357043d2c`
- Excerpt: Standalone Authentication | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard Payment Operations Card Payments Apple Pay Samsung Pay 3D Secure Overview 3DS in a Payment Standalone Authentication Use an Authentication in a Payment STC Pay Tokenization Settlements Invoices Payouts Coupons Dashboard References 3D Secure Standalone Authentication On this page Standalone Authentication A standalone authentication ( card_auth...

### CHANGED: https://docs.moyasar.com/guides/dashboard/setting-up-webhooks/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `578a62ac4864e0627fa0f06bb190eeab8d211ec443c66184b9ba290d2c58d8f0`
- Current status: OK / hash `503df8a33d59495c1d5086206d00fececc15c57fc315ddda72775e7e9c2b07a1`
- Excerpt: Configure Webhooks | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard Payment Operations Card Payments Apple Pay Samsung Pay 3D Secure STC Pay Tokenization Settlements Invoices Payouts Coupons Dashboard Get Your API Keys IP Whitelist Configure Webhooks Apple and Samsung Pay Certificates References Dashboard Configure Webhooks On this page Configure Webhooks This guide will go through how to setup and manage webhooks on...

### CHANGED: https://docs.moyasar.com/guides/payment-operations/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `d2f3231144b9c8e30068a07088cd3bcf16c2397025af209fc41140a1013fbece`
- Current status: OK / hash `4c844330cf0675bbd846c7d7c222c70011f13c42e0eca9af80d9888b047b5ca9`
- Excerpt: Payment Operations | Moyasar Online Docs Skip to main content Developer Documentation Getting Started Guides APIs SDKs eCommerce Plugins Dashboard Payment Operations Card Payments Apple Pay Samsung Pay 3D Secure STC Pay Tokenization Settlements Invoices Payouts Coupons Dashboard References Payment Operations On this page Payment Flows Moyasar supports two payment flows: 1. Purchase (default) \u200b Authorizes and captures in one step. The card is charged immediately and the payment status is paid . 2...

### CHANGED: https://docs.myfatoorah.com/docs/execute-payment

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `1663d081a44b898d2500e70d6ee95d71b14555066516209dd638879731e69478`
- Current status: OK / hash `84e915791ecc2f2c4174bad83cab6d53a5c8f598c5e74cc5bc4d7bf4db15e99e`
- Excerpt: ExecutePayment For AI agents: visit https://docs.myfatoorah.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Features Documentation API Reference Features Documentation Log In Jump to Content Features Documentation API Reference ExecutePayment Log In Introduction Get Started Live Account Account Information Orders Information API Key Test Cards ISO Lookups Payment Flows Choose Your Payment Integration Embedded Payment Customizing Embedded Pay...

### CHANGED: https://docs.myfatoorah.com/docs/get-payment-details

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `ad3be5256e793fcf55e9b3c12fc1c1f28e485d6130c2a79829461f1a44048573`
- Current status: OK / hash `e8f046d96fa0e2848affc66624d2537a18e9f152619d36dfbb2965256e7f6198`
- Excerpt: Get Payment Details For AI agents: visit https://docs.myfatoorah.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Features Documentation API Reference Features Documentation Log In Jump to Content Features Documentation API Reference Get Payment Details Log In Introduction Get Started Live Account Account Information Orders Information API Key Test Cards ISO Lookups Payment Flows Choose Your Payment Integration Embedded Payment Customizing Em...

### CHANGED: https://docs.myfatoorah.com/docs/get-started

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `a73ccfb125ba3c181f03121e1a2e2dac719939af45d00ad47e7c2791dcc1a437`
- Current status: OK / hash `843bd4fc98258fedd522d2d969b9147494037c0a5d81e966046faca4d2f9ad35`
- Excerpt: Get Started For AI agents: visit https://docs.myfatoorah.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Features Documentation API Reference Features Documentation Log In Jump to Content Features Documentation API Reference Get Started Log In Introduction Get Started Live Account Account Information Orders Information API Key Test Cards ISO Lookups Payment Flows Choose Your Payment Integration Embedded Payment Customizing Embedded Payment T...

### CHANGED: https://docs.myfatoorah.com/docs/v3-auth-capture

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `ad43434dba65af8cd7536b19c30d686e45ee4606cadce68e292c2ee6359a3805`
- Current status: OK / hash `2fc0a3e292fd30a79e18d17660aa3ffc7b8134bc80ba3b49d9f3d4646f5a4179`
- Excerpt: Authorize & Capture For AI agents: visit https://docs.myfatoorah.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Features Documentation API Reference Features Documentation Log In Jump to Content Features Documentation API Reference Authorize & Capture Log In Introduction Get Started Live Account Account Information Orders Information API Key Test Cards ISO Lookups Payment Flows Choose Your Payment Integration Embedded Payment Customizing Em...

### CHANGED: https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `02897b265aa0f9d1211ba1388c4db162c4f1b3976882a652fe9ba581734e1071`
- Current status: OK / hash `1c01a35d2d2bb7d514ac8da8247b40c0d7724f09d0c24ed608ccf50aa9938bf5`
- Excerpt: Updating Payment Status Guidelines For AI agents: visit https://docs.myfatoorah.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Features Documentation API Reference Features Documentation Log In Jump to Content Features Documentation API Reference Updating Payment Status Guidelines Log In Introduction Get Started Live Account Account Information Orders Information API Key Test Cards ISO Lookups Payment Flows Choose Your Payment Integration E...

### CHANGED: https://docs.myfatoorah.com/docs/webhook-v2

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `ac53c14c791b5d91a411e4d50d51ac931c50f19697f9e7dfa58d29a61abf0cf5`
- Current status: OK / hash `348b30735b474c34fb0497019f178b45cdbec517e68a342b9b2c87af1481f328`
- Excerpt: Webhook V2 For AI agents: visit https://docs.myfatoorah.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Features Documentation API Reference Features Documentation Log In Jump to Content Features Documentation API Reference Webhook V2 Log In Introduction Get Started Live Account Account Information Orders Information API Key Test Cards ISO Lookups Payment Flows Choose Your Payment Integration Embedded Payment Customizing Embedded Payment Tok...

### CHANGED: https://docs.myfatoorah.com/reference/update-payment

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `732b9d45eb89069a3051ed24284d59ca4be5e07394fc13d1e61f95f3f2ebc0f2`
- Current status: OK / hash `e4498af9d24f37715397f17552b600b91e3c927e4edc3c36a2ff38d35979b9a2`
- Excerpt: Update Payment (Capture or Release) For AI agents: visit https://docs.myfatoorah.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Features Documentation API Reference API Reference Log In Jump to Content Features Documentation API Reference Update Payment (Capture or Release) Log In JUMP TO Powered by Update Payment (Capture or Release) Copy Page put https://apitest.myfatoorah.com /v3/payments/ {paymentId} Used in the Auth & Capture flow to c...

### CHANGED: https://docs.tabby.ai/api-reference/payments/retrieve-a-payment

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `f9fbf1edcb8596818cb43cb64d478fa51185e9636975c2a8807d6d4bad04193d`
- Current status: OK / hash `b3e0e85ad4285dae2e75ac5dfbd9815fd9a70a7af039de153281dd7cb27b7501`
- Excerpt: Retrieve a payment - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Payments Retrieve a payment Documentation API Playground Marketing Toolkit API Playground API Reference Documentation Checkout POST Create a session Session creation payload model Payments GET Retrieve a payment PUT Update a payment POST...

### CHANGED: https://docs.tabby.ai/introduction/what-is-tabby

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `a8829230c74bced559c1c8038208701c9c10ea951159c4e9d23726245be755ee`
- Current status: OK / hash `15f762465415b3040b4107c70694bb8729e4afb83017163e7d8fa47dbb92e354`
- Excerpt: What is Tabby? - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Introduction What is Tabby? Documentation API Playground Marketing Toolkit Introduction What is Tabby? Technical Requirements F.A.Q. Quick Start E-commerce Platforms Shopify Salla Zid WooCommerce Magento 2 OpenCart Odoo Matjrah Salesforce Exp...

### CHANGED: https://docs.tabby.ai/llms.txt

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `a149bb26941bed3b5cf2fe0ee0e9720d3674e59ce7d4e6c6604eab970c49478b`
- Current status: OK / hash `9df18ccbb83588e6f283dd2b9c9cff61dbb37f8763a849960fda72c7efd8a7d8`
- Excerpt: # Tabby ## Docs - [Create a session](https://docs.tabby.ai/api-reference/checkout/create-a-session.md): Creates a Checkout session. Creates Session and Payment, returns Pre-Scoring result (status), ids of Payment and Session. - [Session creation payload model](https://docs.tabby.ai/api-reference/checkout/session-payload-model.md) - [Approve disputes](https://docs.tabby.ai/api-reference/disputes/approve-disputes.md): Approve disputes (refund money to the customer). Only 20 disputes can be approve...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/checkout-flow

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `72d216d308cbc23375fbc96c6f17ffd2a18d5b29d49ef2bac0aff129dffbde72`
- Current status: OK / hash `aab2bf526106ddac5cf811fb4fbb2f4c2c7f758fd26e6e59fc44802c271adaa9`
- Excerpt: Checkout Flow - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Online Custom Integration Checkout Flow Documentation API Playground Marketing Toolkit Introduction What is Tabby? Technical Requirements F.A.Q. Quick Start E-commerce Platforms Shopify Salla Zid WooCommerce Magento 2 OpenCart Odoo Matjrah Sal...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/payment-processing

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `c06308df5a48708088236ecc89659f22c16b261c3ca0362a98be118fd5e928aa`
- Current status: OK / hash `f22a5cc5cfdc0b82e6c5f4d8365ab9285f1a20d2bf5b8a9716491d769a10814a`
- Excerpt: Payment Processing - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Online Custom Integration Payment Processing Documentation API Playground Marketing Toolkit Introduction What is Tabby? Technical Requirements F.A.Q. Quick Start E-commerce Platforms Shopify Salla Zid WooCommerce Magento 2 OpenCart Odoo M...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/payment-statuses

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `27db3536310400ecf0b8557d3e29311a3de77161def7e61d01c2cfa01325ebbe`
- Current status: OK / hash `5ddc2a0dd6b2998536a4f9124cc2d30db43eb70b43f8971fe000946752ff9030`
- Excerpt: Payment Statuses - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Online Custom Integration Payment Statuses Documentation API Playground Marketing Toolkit Introduction What is Tabby? Technical Requirements F.A.Q. Quick Start E-commerce Platforms Shopify Salla Zid WooCommerce Magento 2 OpenCart Odoo Matjr...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/webhooks

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `5c7ecd6f0d9d4d35e09f30d1173a6136c6dccc57e9b0896ee3431f37b97cbe78`
- Current status: OK / hash `f8aadb29f59d2f35ebc6f83ef27e9b1bb6ed785d548ec61006adf2ff24e7eeb5`
- Excerpt: Webhooks - Tabby Documentation Index Fetch the complete documentation index at: /llms.txt Use this file to discover all available pages before exploring further. Skip to main content Tabby home page Search... \u2318 K Register Register Search... Navigation Online Custom Integration Webhooks Documentation API Playground Marketing Toolkit Introduction What is Tabby? Technical Requirements F.A.Q. Quick Start E-commerce Platforms Shopify Salla Zid WooCommerce Magento 2 OpenCart Odoo Matjrah Salesforce Ex...

### CHANGED: https://docs.tamara.co/docs/direct-online-checkout

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `8b705e962a1a4c69fa6cec54c4289e8af593308ad33ffcc62b1758e65eb180cd`
- Current status: OK / hash `b3a558c4d32acf2baaa54bbe27e5438e6359449cab01b10456f4a00c3e41a13f`
- Excerpt: Online Checkout For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login Guides System Status Support Business Login Guides Online Checkout Online Checkout \U0001f44b Introduction Get to know Tamara \U0001f6d2 E-Commerce Platforms Platforms Quick Start ExpandCart FatherShops Magento 2 Installation...

### CHANGED: https://docs.tamara.co/docs/online-order-status-flow

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `55406d8c9822b30e5fbf05f7dae30524266503806bc7a3e890b35947646c88e9`
- Current status: OK / hash `9d2c50e5cbfda6100f6284b8f08514df9f99db97b5c71243cbe2f9c7d7d9f1bf`
- Excerpt: Online Order Status Flow For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login Guides System Status Support Business Login Guides Online Order Status Flow Online Order Status Flow \U0001f44b Introduction Get to know Tamara \U0001f6d2 E-Commerce Platforms Platforms Quick Start ExpandCart FatherS...

### CHANGED: https://docs.tamara.co/docs/transaction-authorisation

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `310bb1a2cb0db96a52042cbf7b318bde3978b8f2c1de57ad68c0a2b6cf486974`
- Current status: OK / hash `476fe311d7ddda5b1a92db4cec559736462c16fa87b9ebbb07fb921fa411b8d0`
- Excerpt: Webhook Registration & Order Authorisation For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login Guides System Status Support Business Login Guides Webhook Registration & Order Authorisation Webhook Registration & Order Authorisation \U0001f44b Introduction Get to know Tamara \U0001f6d2 E-Comme...

### CHANGED: https://docs.tamara.co/reference/captureorder

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `428cad09df204c01002a9ea13041d5c968e15118baf9400f5407d9ca4a82fac4`
- Current status: OK / hash `de2bbeaf41edbf5ca77538cda046504e314267cf92c84a4902e3255c438c7c85`
- Excerpt: Capture Order For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login API Explorer System Status Support Business Login API Explorer Capture Order JUMP TO Powered by Capture Order Copy Page post https://{environment}.tamara.co /payments/capture This endpoint is requested to perf...

### CHANGED: https://docs.tamara.co/reference/getorderdetails

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `4eda25e3f2d83a0597201d0329ff1f7cf8346a092432b72c8f30b0a9e35a7fa2`
- Current status: OK / hash `372bf43aa40570c2fccde7a1a5906e74c0d4e45eae30a3dd4103df71c29a194d`
- Excerpt: Get Order Details by Tamara's order_id For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login API Explorer System Status Support Business Login API Explorer Get Order Details by Tamara's order_id JUMP TO Powered by Get Order Details by Tamara's order_id Copy Page get https://{e...

### CHANGED: https://docs.tamara.co/reference/simplifiedrefund

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `c004d76d9673497e94a4d63f44b160a04cf37ba5cdf963c0c4330cc2f30c6c4e`
- Current status: OK / hash `948e8e94f90d9329bec8f472ebc3ae7581717c20267732909901423dd93231d3`
- Excerpt: Simplified Refund For AI agents: visit https://docs.tamara.co/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI. Jump to Content Guides Api Explorer Checkout Widget Home Guides API Explorer Guides Api Explorer Checkout Widget System Status Support Business Login API Explorer System Status Support Business Login API Explorer Simplified Refund JUMP TO Powered by Simplified Refund Copy Page post https://{environment}.tamara.co /payments/simplified-refund/ {order_id}...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `e40d22350c32faaa57c2255923be6e0a93801f001641c8bf1425a18a70c002f4`
- Current status: OK / hash `fc75d00f93749f1b6ca04f3073af0c83b67101753c624d39c3eb4a83cd304701`
- Excerpt: Direct Payment (Hosted) | EasyKash APIs EasyKash APIs \u2318 Ctrl k EasyKash APIs Direct Payment (Hosted) Pay API Callback Service Payment Inquiry Cash API (Cash-only) Direct Payment (WordPress WooCommerce Plugin) Direct Payment shopify plugin Powered by GitBook On this page For the complete documentation index, see llms.txt . This page is also available as Markdown . Copy On this page Direct Payment (Hosted) Direct Payment is an API to allow customers to integrate Easykash\u2019s payment methods into the...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/cash-api-cash-only

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `262b17775c15c87d4fd1c719ec69a7c264a7f7bb9cf04fec5629d39d43d26cdb`
- Current status: OK / hash `7b60761115c8a33eb801278ac651a5323eb16cc4884747b6fc9c5e102a451d94`
- Excerpt: Cash API (Cash-only) | EasyKash APIs EasyKash APIs \u2318 Ctrl k EasyKash APIs Direct Payment (Hosted) Cash API (Cash-only) Create a payment Direct Payment (WordPress WooCommerce Plugin) Direct Payment shopify plugin Powered by GitBook On this page For the complete documentation index, see llms.txt . This page is also available as Markdown . Copy On this page Cash API (Cash-only) This feature only works for Cash payment methods. What is our API feature? For Businesses that already have running websit...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `ca7fca8c9e098c96af1132b5badf22c63beff4db0bf869f5e6703c87a482ee1d`
- Current status: OK / hash `e19e6bec43d16d0a1040a90c2676f2ecfd0c077a196c21a50697bdc550b83103`
- Excerpt: Callback Service | EasyKash APIs EasyKash APIs \u2318 Ctrl k EasyKash APIs Direct Payment (Hosted) Pay API Callback Service Callback response verification Payment Inquiry Cash API (Cash-only) Direct Payment (WordPress WooCommerce Plugin) Direct Payment shopify plugin Powered by GitBook On this page For the complete documentation index, see llms.txt . This page is also available as Markdown . Copy On this page Direct Payment (Hosted) Callback Service If your API service is enabled for your account, af...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service/callback-response-verification

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `1afd85eea9915a4f89176d1a3e761644381b4079588562d4be9c78b08f7d55a2`
- Current status: OK / hash `b63ec30ffa7e4d6f9e7c791d4be31c1784c287818ccb1e345b66a4bcf76c7e80`
- Excerpt: Callback response verification | EasyKash APIs EasyKash APIs \u2318 Ctrl k EasyKash APIs Direct Payment (Hosted) Pay API Callback Service Callback response verification Payment Inquiry Cash API (Cash-only) Direct Payment (WordPress WooCommerce Plugin) Direct Payment shopify plugin Powered by GitBook On this page For the complete documentation index, see llms.txt . This page is also available as Markdown . Copy On this page Direct Payment (Hosted) Callback Service Callback response verification Callba...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api

- Providers: egypt-payment-guardian:easykash, egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:easykash, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `6753c05afc62cdf9685429920f7b2421e509ed4419973598cf0b297245a383fb`
- Current status: OK / hash `3563c5dfffb6a4094750a35a49c2c37e0c2f91be20b61839cf76298cdd28edf5`
- Excerpt: Pay API | EasyKash APIs EasyKash APIs \u2318 Ctrl k EasyKash APIs Direct Payment (Hosted) Pay API Callback Service Payment Inquiry Cash API (Cash-only) Direct Payment (WordPress WooCommerce Plugin) Direct Payment shopify plugin Powered by GitBook On this page For the complete documentation index, see llms.txt . This page is also available as Markdown . Copy On this page Direct Payment (Hosted) Pay API API to create direct pay link Create direct pay link POST https://back.easykash.net/api/directpayv1/...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/payment-inquiry

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `039e841651fab5b6097e659692c754de789dc305c1cd95ed3db2730244299eb3`
- Current status: OK / hash `687d8e7c29026baded764f70512f1e579a95a900232822a2989f4f2208b0cc4b`
- Excerpt: Payment Inquiry | EasyKash APIs EasyKash APIs \u2318 Ctrl k EasyKash APIs Direct Payment (Hosted) Pay API Callback Service Payment Inquiry Cash API (Cash-only) Direct Payment (WordPress WooCommerce Plugin) Direct Payment shopify plugin Powered by GitBook On this page For the complete documentation index, see llms.txt . This page is also available as Markdown . Copy On this page Direct Payment (Hosted) Payment Inquiry If you'd like to inquire about a specific transaction, use this payment inquiry API...

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
