# Source Watch Report

- Generated: 2026-06-15T08:07:12Z
- Total URLs checked: 106
- Changes detected: 86
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

This report was regenerated for release 1.1.1 after source-watch normalization hardening. The new normalizer strips common provider docs navigation/sidebar/footer chrome, AI-readable index notices, GitBook Markdown notices, API-reference recent-request widgets, and approximate relative update ages before hashing.

Release 1.1.2 additionally hardens source-watch comparison after immediate private watcher verification found runner-only GitHub API JavaScript challenges on Kashier source references. Those OK-to-JavaScript-challenge degradations, plus transient HTTP 408, 429, and 5xx fetch failures, are now treated as maintainer review warnings rather than payment documentation changes.

Classification: `chrome_noise` plus `transient_fetch` / watcher hardening. No new endpoint, auth/signature, webhook, status, amount/currency, refund/capture/void, test-card, adapter, eval, or payment-behavior guidance change was identified beyond the already-released Moyasar 1.1.0 update.

## Changes

### CHANGED: https://developer.fawrystaging.com/docs/card-tokens/card-tokenization-overview

- Providers: egypt-payment-guardian:fawrypay, mena-payment-guardian:fawrypay
- Previous status: OK / hash `042e4c87205cb9167bf2375a99ccd7a5ee904444319ae834434dfe3cf1fe7183`
- Current status: OK / hash `36a515834b38bcc1eea00d16ffd913ec4a14998bd5e086cf55a64c5e4a14ab4b`
- Excerpt: Card Tokenization Store your client's card information for a more secure and fast checkout experience. Introduction With FawryPay, you can securely store one or more payment details per client. Storing your clients' payment data not only allows you to offer subscription payments, but also gives your clients a faster and more convenient checkout experience by using their stored card. We refer to these saved card details as card tokens and storing a client's card details as card tokenization. Why...

### CHANGED: https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/get-payment-notification

- Providers: egypt-payment-guardian:fawrypay, mena-payment-guardian:fawrypay
- Previous status: OK / hash `dda79a586b12ad2fd2d93cd32a73c65cdc4458571fdd5ca2e19b21f7d8abba82`
- Current status: OK / hash `9fb651bd7faeac9236c06fb9ce9fe6a88eebbbb0ab451e795a2bdf41c6060655`
- Excerpt: Stay Updated With Your Transactions Status Whenever a transaction status has been updated, FawryPay will keep you informed. Introduction After a successful issuance of a given payment transaction by one of your clients using any of our payment methods, you will need to be up-to-date with the status of your transaction. FawryPay delivers several solutions to keep our valued merchants informed once the status of their respective transactions has been updated. For our valued merchants\u2019 convenience,...

### CHANGED: https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/get-payment-status-v2

- Providers: egypt-payment-guardian:fawrypay, mena-payment-guardian:fawrypay
- Previous status: OK / hash `05b805f7fd3184a1039177365c98f79e84b7fd5e11fe6744121e24a109cc0497`
- Current status: OK / hash `9112537dfc050d8eb39bd5136524dcfccbbb658c89c4ac91197fe62e73c11827`
- Excerpt: Get Payment Status V2 Pull information about your transactions whenever needed. FawryPay delivers the Get Payment Status API as a responsive API for merchants who wishes to pull the status of their transactions whenever needed. Our valued merchants can use Get Payment Status API to retrieve the payment status for the charge request, using GET method. FawryPay Sample GET Request: A sample GET where you can pull your transaction status updates whenever needed is provided below. HTTP GET Parameters...

### CHANGED: https://developer.fawrystaging.com/docs/card-tokens/payment-notifications/server-notification-v2

- Providers: egypt-payment-guardian:fawrypay, mena-payment-guardian:fawrypay
- Previous status: OK / hash `eb9a480ee00b8f941d055cd0ac8dd61982787674f41b43fe7f43651df3cb3d39`
- Current status: OK / hash `90ec9caaf1d7e519d6c58a419a1ba48accc689aa87cf185a6e6554c517725b7c`
- Excerpt: Server To Server Notification V2 Throughout its entire roadmap, Your FawryPay transactions shall experience several status updates. Depending on the specific nature of your core business, the status of your clients\u2019 transactions can range from created, paid, cancelled, expired, shipped to delivered. Whenever the status of one of your transactions has been altered, FawryPay will send an informative HTTP POST request to your preconfigured endpoint on your own application server with the current de...

### CHANGED: https://developer.fawrystaging.com/docs/introduction

- Providers: egypt-payment-guardian:fawrypay, mena-payment-guardian:fawrypay
- Previous status: OK / hash `646f53fac93610ab8a91cca60d5b2354f668cb329cc3a9b806653a494db1bcb4`
- Current status: OK / hash `35a3f1c7ba6ce4d388d0fafd4f982eb8b28113f60da997b43230b2e5eb386a69`
- Excerpt: FawryPay Online Payments Start accepting payments on your website and/or mobile apps through Fawry retail network, banking channels, cards, and mobile wallets. Introduction FawryPay is Egypt\u2019s top online payment processing technology service provider. It provides a collection of comprehensive solutions to fulfill the needs of the diverse range of merchants\u2019 core businesses, products, and services nature enabling different payment methods. FawryPay enables both front-end and back-end technologies...

### CHANGED: https://developer.fawrystaging.com/docs/server-apis/server-apis-overview

- Providers: egypt-payment-guardian:fawrypay, mena-payment-guardian:fawrypay
- Previous status: OK / hash `d65605d692a95d8274305c5fe264f0c5b67cf4e1d3536f16ed828cf5912ecd80`
- Current status: OK / hash `9b164d49c6068d6867e97a734986505ede0e2af1a67e8c808ee4459dab16c064`
- Excerpt: Server to Server APIs The fastest way to build conversion-optimized payment forms, hosted on FawryPay. Introduction If you are looking forward taking control over the look and feel of your checkout page, our set of comprehensive server side APIs are ready for you. With our set of APIs you can: Make payments using Cards. Issue tokens for your clients' Cards so a more secure payments. Receive payments at any of our FawryPay POS retail store. Issue cash on delivery payments. Take full control of ch...

### CHANGED: https://developers.tap.company/docs/authentication

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `f05041bc03b74409ae497d8c643b625aaeca7a6c8935351bf8d6a364491feba0`
- Current status: OK / hash `916c3cf92a08ccef6d2259e8391bee1756e7405f03c29447359dd4b157970d34`
- Excerpt: Authentication A detailed overview of API integration, workflow, and usage examples for 3D Secure authentication with Tap Payments. Overview This guide provides a comprehensive resource for implementing 3D Secure (3DS) authentication with Tap Payments, a security protocol that adds an extra layer of authentication to online credit and debit card transactions to reduce fraud and enhance customer trust. It details how Tap Payments handles 3DS authentication, including both internal processing (whe...

### CHANGED: https://developers.tap.company/docs/get-started

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `d0d6185bb6e3154844d34ba371f4ef7cf760d6865ba7737dddec056ff96e8dc3`
- Current status: OK / hash `a12de1a6fe0101eec418eef7ff0544c24cce3e1fac664ebc565dc85cca50c62f`
- Excerpt: Overview This page guides you to set up your account with Tap, and start accepting online payments on your website or mobile App. 1. Registration You can create your account from here Get-Started 2. Get Your API Keys Once registration has been completed, follow the steps below to get your API testing keys: Sign in to Tap\u2019s Dashboard using your email or phone number Click on Accounts Click on the ID in the Operators section Click on the MERCHANT section to get the default API keys. The data you w...

### CHANGED: https://developers.tap.company/docs/recurring-payments

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `732448f73edaa07b8cf19bdbf189a8a6b288540e30f1b2b096066facaaf2a524`
- Current status: OK / hash `1406f8535258ddddbe8a1aa12ddbaf5f0e36630138f3605e6bcf7262533ef73f`
- Excerpt: Recurring Payments A Step-by-Step Documentation for Setting Up and Processing Recurring Payments Recurring payments allow merchants to charge customers on a regular basis, such as for subscriptions or installment plans. This guide provides a detailed guide on setting up and processing recurring payments using Tap APIs. Please note that this guide assumes you have already familiarized yourself with the API reference documentation for Tap Payments, specifically the Charges API and Authorize API. S...

### CHANGED: https://developers.tap.company/docs/webhook

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `08005dd39c2e0c65471da751c00560ffe1cdc1c792ae1099821ff63df5a3692f`
- Current status: OK / hash `a1bfd0d43cb8d46d7bfbbee339cb39427fea8e9a33b5f9cf5151e0aeb9fa6670`
- Excerpt: Webhook Tap ensures secure and realtime webhooks for payment events, and to send the post payment details. Payments webhook is a server-to-server call(also known as IPN "Instant Payment Notification"), that allows merchants to receive the post-payment details to automate and synchronize their internal ERPs by checking the actual payment status and other technical details, as per requirements. It's supported with all our APIs, SDKs & Libraries where it is required to be. Tap also triggers the web...

### CHANGED: https://developers.tap.company/reference/api-actions

- Providers: mena-payment-guardian:tap-payments
- Previous status: OK / hash `31c5bcf453cb659074201562f9db3b8085e743db8da710368db206b3cb6a90f9`
- Current status: OK / hash `3f98c9f02cada8d5f700376a78592edede60f37a7a0fa85dd9fbf64c80a3fa77`
- Excerpt: API Actions You can perform the following API actions on payments: Updated <relative-age> ago

### CHANGED: https://docs.geidea.net/

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `651cc3d52107e9da94603406d954b0acb6e80def8557d0ae02757d1365b0313c`
- Current status: OK / hash `af2cf130d3cce447a25cfcdebf15d3821fb14c53db50554ddfbef53632b1ad42`
- Excerpt: Overview Geidea is one of the leading financial technology companies in the MENA region, providing innovative payment solutions and digital financial services. Established in Saudi Arabia and now operating across several countries, Geidea focuses on enabling businesses of all sizes\u2014from small merchants to large enterprises\u2014to accept and manage payments seamlessly. The company\u2019s mission is to make financial technology accessible, affordable, and easy to use, supporting merchants with reliable inf...

### CHANGED: https://docs.geidea.net/docs/buy-now-pay-later-bnpl

- Providers: egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `cbfc8c2d4e97f19a68acc61eef76bf415d8d98eb9872c9ff73bd6cc34a2ea928`
- Current status: OK / hash `79b422b932693d7ddb40562b899f6ccd2f6a92fb9d077c2c13a9509e287e2a17`
- Excerpt: Buy Now Pay Later (BNPL) What is BNPL? Buy Now Pay Later (BNPL) has emerged as one of the most popular payment methods worldwide recently. One of the main reasons is that it allows customers to buy goods immediately and pay for them later, over time, without paying the full amount upfront. It is used by a wide variety of businesses, especially e-commerce retailers, to increase conversions, boost average order value, and reach new customers. The most commonly used Buy Now Pay Later service is 'In...

### CHANGED: https://docs.geidea.net/docs/cancel-order-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `ded4ee10305fcd9f39d9ab3e80cf3b22f1c9a8a171ef4f2021d39cf58287c7d6`
- Current status: OK / hash `2c438b378f08c4fe25118cc4cc019d04ddccfe2ea8673013aaf093f44224d825`
- Excerpt: Cancel Order Cancel on order for which payment has been initiated You can use the Cancel Order API to initiate a request to cancel an order that has been initiated. \U0001f6a7 You can cancel an order only if you have executed the Cancel Order API call either after the Initiate Authentication API call or the Authenticate Payer API call. Trying the execute the Cancel Order API call after the Pay API call will not cancel the order. This attempt returns a response with the message " Order is already complete...

### CHANGED: https://docs.geidea.net/docs/geidea-checkout-v2

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `a40d1ec8a9ceb419cce7702585dc0716f9831ad7e090efba444016647727188d`
- Current status: OK / hash `d47fc2d854fd4573ae0d324cb0d6ac9751c6ce11f0087d194c14711ffbd8a0e0`
- Excerpt: Geidea HPP Checkout Overview Our Checkout offering is a pre-built payment UI that offers the quickest way to integrate and start securely accepting payments. It allows you to accept popular payment methods through a single web front-end implementation. Geidea Checkout supports both one-time payments and subscriptions for your customers - through a quick, easy and low-code integration into your website's checkout flow. It is very user-friendly and customizable. Additional payment methods can be e...

### CHANGED: https://docs.geidea.net/docs/overview-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `2a97f1f27b783a0f43941e3685de6036fd3673d033b45034b2ac818c8e67293f`
- Current status: OK / hash `f2d929601100dd356549273931cd4972654c7cdfae8280284d53625293827618`
- Excerpt: Transaction and Order Management You can use the following capabilities to manage your orders and payments after they have occurred. # Capability Description 1 Cancel Order Cancel an Order 2 Refund Payment Refund a payment 3 Void Transaction This operation is available only on the Geidea platform in Saudi Arabia now. Based on the merchant's requirements, we will enable them on a case-by-case basis for the merchant. For details on integration, please get in touch with our support team via our sup...

### CHANGED: https://docs.geidea.net/docs/pay-by-link-apis

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `ccb1b45209a96fb07daf5831925b4d46909aead1907e3f3b068a4db2c5ce992f`
- Current status: OK / hash `9ac3eeec0e1637c6950834fd709697a79c636e620b355c01d7c9eb3bbf15822a`
- Excerpt: Pay by Link - APIs You can use our Pay by Link APIs to create your custom flows to personalize the digital journey of your customers. Advantages of Geidea's Pay by Link APIs Advantage Description Personalization The APIs empower you to tailor the digital user experience and equip you with robust tools for monitoring payment links. Control Take full command of the payment process using our Pay by Link APIs. They offer a multitude of capabilities, including configuring accepted payment methods, cu...

### CHANGED: https://docs.geidea.net/docs/pay-v2

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `165aeeedde35094886dd081c8017622e696ae3f674d3141996763a8c1e88bcb8`
- Current status: OK / hash `8c69bb7d0486899989751861cb82526bca24c3293af38eeef2b4c984be037a1c`
- Excerpt: Pay Complete the payment using the Pay API You can complete the payment using the Pay API Call the Pay operation as soon as you have executed the authentication operations successfully through the Initiate Authentication and Authenticate Payer API calls. You must use the same parameter values used in the authentication operations or any mismatch between parameters will result in an error. To carry out this operation, you will need the following details from other API calls: Parameter Datatype De...

### CHANGED: https://docs.geidea.net/docs/refund-2

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `fa18b6c1e9438dd91dd62dbe066df46b072e2213a44961ab7a6a34bac6e9e827`
- Current status: OK / hash `6c1c8a9385be7a079af4ec34650ac5db332878dc1d19ed42c6dae02327a82d32`
- Excerpt: Refund Overview When a customer buys an item and wants to return it, then you can easily refund their payment. You can use the Geidea merchant portal or our Refund API to refund money to your customers either fully or partially. \U0001f6a7 You can refund a payment only for payments that have been completed i.e. the Pay API has been executed successfully or the Authorise and Capture APIs have been executed successfully. \U0001f44d You can refund a transaction for the full amount or a partial amount. You can refund...

### CHANGED: https://docs.geidea.net/docs/sample-callback-responses

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `081fc713b3d48c2d4b9f5c803fb3db73aa4529360f409fabff303ae50bbdb5e2`
- Current status: OK / hash `704961a57475165c641ee2c292b61cccf0c2c740a6b02edfb90fe9978ec4bde1`
- Excerpt: Webhook/Callback Notifications A callback URL, also known as a webhook or notification URL, is a URL (Uniform Resource Locator) which can be used by you when you integrate with our payment gateway to receive real-time notifications and data regarding payment transactions. Callback URLs are an essential component of online payment processing, and they serve several important purposes like: 1 : Transaction Status Updates: When a customer makes a payment through our payment gateway, the transaction...

### CHANGED: https://docs.geidea.net/docs/souhoola

- Providers: egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `6b5cc4fc37060025aef03e1dc1be7f8058e392d5190f40e8a1abbdadeb1aa065`
- Current status: OK / hash `7154ff719c6ceb77d6f92f44149b19be75b04d9a5ad5c87d4578d7e481b6822d`
- Excerpt: Souhoola [Egypt] Souhoola is an Egyptian Buy Now, Pay Later (BNPL) provider that offers customers a convenient way to pay for their purchases through monthly installment plans. As a merchant, you benefit from receiving the full payment upfront as soon as the transaction is processed, while your customers enjoy the flexibility of spreading their payments over time. With Souhoola, customers can enjoy a quick and remote credit approval process, allowing them to obtain their credit limit instantly....

### CHANGED: https://docs.geidea.net/docs/valu

- Providers: egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `12e5c00d08f5f8b6df42cea1a2cd43a450133cbbd1e5ab1d1279802318644802`
- Current status: OK / hash `a314aefc322f69a203789d3cf5ae73e96103228e194189d66ee7b2556aeb7caf`
- Excerpt: ValU [Egypt] ValU offers Egyptian customers a way to pay for purchases through a specific monthly installment plan over time. As a merchant, you have the advantage of receiving the full payment upfront as soon as the transaction is processed. Established in 2017, ValU is the leading Buy-Now Pay-Later (BNPL) Fintech platform, providing convenient and customizable financing plans in the MENA region. ValU offers customers an ultra-fast approval process, allowing them to buy what they want now and p...

### CHANGED: https://docs.geidea.net/docs/void-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `39bc385c969273c7482fb546c884c06e81f397cc647fa88164d6d167b0f81a61`
- Current status: OK / hash `330c1cc745bdc552ba695cf2c487af3b283ec00aa2771bcbd908ee4c811a396a`
- Excerpt: Void Overview If you authorised a payment, but do not want to capture it, say because you found the inventory for the product was accidentally damaged and it suddenly becomes out of stock, you have the option to void the payment. \U0001f4d8 Void means that the uncaptured/unpaid/unsettled transaction is cancelled from the merchant side. You can use the Void operation for pre-authorized and uncaptured transactions, while refunds can be initiated only for captured or paid or settled transactions. Using the...

### CHANGED: https://docs.geidea.net/reference/capture-transaction-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `767d3e2678ea26e1e40b035a9888497d1a02b6d6a69a37d82ffcbc78f7d1c1ea`
- Current status: OK / hash `0e70ab8ebb34fa568705dd26a3fe03083d855bee15dc708a584691213880be33`
- Excerpt: Capture Transaction post https://api.ksamerchant.geidea.net /pgw/api/v1/direct/capture Body Params orderId string required Unique ID for the order. callbackUrl string The URL of your callback server to receive useful information for keeping track of your inventory, records, etc. The URL may have protocol (http/https), subdomain (optional), domain name and path (optional) captureAmount float Amount for which capture is requested. Amount must be greater than 0.01. Won't be allowed to capture more...

### CHANGED: https://docs.moyasar.com/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `bba608f9946715c912c5e56e19bcc036c8ac1d39b3157a8301030ffe601a0823`
- Current status: OK / hash `25e1f69749756ad85d954918b589d6e725fc27a646411d1f14ee09d8f6228325`
- Excerpt: Moyasar Docs Welcome to Moyasar Developer Documentation! We will guide you through the process of integration and providing payments within your web or mobile application. Follow these steps to get started. info Click here if you would like an overview of the Developer Docs tree structure. Create An Account \u200b If you haven't created an account yet, please do so by visiting the sign up page then continue with the next step Sign Up Here . tip Moyasar offers a free account for you to try the service...

### CHANGED: https://docs.moyasar.com/api/authentication/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `1609c4b152e231bf9de07bc6051374f9e33af34165f7587b3a72d2bbdd4fdae3`
- Current status: OK / hash `1aee05b2a71b7fbb5912b025bafb2502486551eb292ca732f18cfc0639ec5152`
- Excerpt: Authentication Authentication Introduction \u200b Moyasar's API uses API Keys to authenticate requests. You can view and manage your API keys in the Moyasar Dashboard. Publishable Key \u200b Sending cardholder data to the merchant backend is prohibited and will result in canceling the agreement between Moyasar and the merchant in addition to the immediate termination of the service. To address this issue, Moyasar has implemented a publishable API key, enabling merchants to initiate payments directly from...

### CHANGED: https://docs.moyasar.com/api/card_auths/01-create-card-auth

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `2cee9b5c183e0fd565380811ad274521eb76439f5be872fbc1e9a84f40dc102c`
- Current status: OK / hash `ad29a3fdfd6054ec1096190ba1b764c4e0c512dd4e0486463abf05e00ce3dbb4`
- Excerpt: Card Authentication API Create Card Authentication Create Card Authentication POST /card_auths Start a standalone 3D Secure authentication for a card, without charging it. Standalone 3D Secure is enabled only for selected merchants. When the authentication is created, its status will be one of: available \u2014 a challenge is required; redirect the cardholder to transaction_url . failed \u2014 the card is not enrolled or enrollment failed. Once the cardholder completes the in-browser flow, the status beco...

### CHANGED: https://docs.moyasar.com/api/card_auths/02-fetch-card-auth

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `c724113682fc93664fcea9cf299f4687fc7eed9245da5d9b5312003276a780d6`
- Current status: OK / hash `2f1ae2c5960a7c81ffb769025a32ecb6a63128a8ac66038ae98d13a5218de0ae`
- Excerpt: Card Authentication API Fetch Card Authentication Fetch Card Authentication GET /card_auths/:id Retrieve a card authentication and its result once the cardholder has finished. The result object is returned only with secret key authentication. A publishable key may fetch the authentication for 15 minutes after creation \u2014 for example to check the status after the cardholder is redirected back \u2014 but result is always null on those responses. Request \u200b Path Parameters id uuid required ID of the card...

### CHANGED: https://docs.moyasar.com/api/other/webhooks/webhook-reference

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `ca5fa3dab79d6f0de850294d0a4042e3df15c8d1b5eb81a0e1c45fbec9a203e5`
- Current status: OK / hash `81131a2dfadbcf71eba33cd240a626b52c017a1b572d4d66c1c719bf7188a23d`
- Excerpt: Other APIs Webhooks Webhook Reference Webhook Reference Introduction \u200b With Moyasar's webhooks, you can stay in the know about payment events in real time. Set up webhooks by specifying a notification URL. Choose the specific events you want to be alerted about, such as successful payments or refunds. Then, handle these events in your application to stay updated on payment activity. It's that easy! Payment Events \u200b Payment events provide valuable information about the status and progress of your...

### CHANGED: https://docs.moyasar.com/category/payments-api/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `f1b05ebf8cfa43c8e53bade7355dfe01231d761c2bdd08b7c7802e27a70095b0`
- Current status: OK / hash `543ccdfd8cd3aaf2461c0b9679812a12c04e7cab7c3b851ca27dd4263af7c02a`
- Excerpt: \U0001f4c4\ufe0f Create Payment Start a new Card, Apple Pay, Samsung Pay or STC Pay payment.

### CHANGED: https://docs.moyasar.com/guides/3d-secure/standalone-authentication

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `3bcbef2ba5db5746f9a9b3e0253b8e4b30e2c8ed00b8055f8bf46fa357043d2c`
- Current status: OK / hash `8e13e05f1b7b2eda90fb4a13a1a834e9665e25d8da01a91e383df203dd476bc4`
- Excerpt: 3D Secure Standalone Authentication Standalone Authentication A standalone authentication ( card_auth ) is a 3D Secure authentication on its own \u2014 it has an amount, a currency, and a card, but it does not charge anything. Use it to authenticate now and charge later, or to authenticate on Moyasar and authorize elsewhere. Full request/response details are in the Card Authentication API reference; this page walks through the flow. note Standalone 3D Secure is enabled only for selected merchants. 1....

### CHANGED: https://docs.moyasar.com/guides/dashboard/setting-up-webhooks/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `503df8a33d59495c1d5086206d00fececc15c57fc315ddda72775e7e9c2b07a1`
- Current status: OK / hash `0a70a2954f3bfb426c5227aaf2ee50397a7cfa9337eb9b00590f336b3a4c00ca`
- Excerpt: Dashboard Configure Webhooks Configure Webhooks This guide will go through how to setup and manage webhooks on your Moyasar account. Getting Started \u200b Go to https://dashboard.moyasar.com/ Log in to your account. Click on the Settings tab. Go to the Webhooks tab Webhooks \u200b Add Webhook \u200b To get started, click on add webhook Required Fields \u200b Term Description Endpoint a URL on your server that will receive the notification (must be HTTPS) Secret Token is a password you need to validate on your serv...

### CHANGED: https://docs.moyasar.com/guides/payment-operations/

- Providers: mena-payment-guardian:moyasar
- Previous status: OK / hash `4c844330cf0675bbd846c7d7c222c70011f13c42e0eca9af80d9888b047b5ca9`
- Current status: OK / hash `a8ba8b54d230877cde580b7abd5fa074d0940ead889f8924e68ed99727c48617`
- Excerpt: Payment Operations Payment Flows Moyasar supports two payment flows: 1. Purchase (default) \u200b Authorizes and captures in one step. The card is charged immediately and the payment status is paid . 2. Authorization \u200b Only places a hold on the card without capturing the funds. You then decide whether to capture (charge) or void (release) the held amount. Authorization \u200b To authorize a payment without charging, set manual to true in the source when creating the payment. Endpoint: POST /v1/payments Au...

### CHANGED: https://docs.myfatoorah.com/docs/execute-payment

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `84e915791ecc2f2c4174bad83cab6d53a5c8f598c5e74cc5bc4d7bf4db15e99e`
- Current status: OK / hash `54ffae4ec2bbd68175d977b205c98166f736c16ff703f968627ebaaebedcb52a`
- Excerpt: ExecutePayment Endpoint Overview The "ExecutePayment" endpoint is a POST request. It is used to create a MyFatoorah invoice against a certain gateway. Detailed functionality of how to create an invoice is explained in the Gateway Integration section. The endpoint on Swagger is: Payment_ExecutePayment . Now, we are going to declare the endpoint and its models along with each accepted parameter and possible value. \U0001f4d8 Request Header Add "Authorization": "Bearer {Token}" to request header. Token of d...

### CHANGED: https://docs.myfatoorah.com/docs/get-payment-details

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `e8f046d96fa0e2848affc66624d2537a18e9f152619d36dfbb2965256e7f6198`
- Current status: OK / hash `851fd4f54e590716bc818e7f950e3f8c118be8b89dd61f44ccb2f66bedaaa445`
- Excerpt: Get Payment Details Overview Use this endpoint to retrieve the status and detailed information of a specific payment. When a payment is processed through MyFatoorah, the PaymentId is returned as a parameter in the Redirection URL . This PaymentId should then be used to inquire about the payment details and confirm whether the payment was successful or not. \U0001f44d Good Practice As a good practice, to ensure the payment response is returned from the MyFatoorah end, we encourage you to call GET /v3/paym...

### CHANGED: https://docs.myfatoorah.com/docs/get-started

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `843bd4fc98258fedd522d2d969b9147494037c0a5d81e966046faca4d2f9ad35`
- Current status: OK / hash `356f2e31af780b0037da71d62b9eb6ab99441b0322679bc82229afc69a64c694`
- Excerpt: Get Started Build your integration and start accepting payments online Introduction In this section of the documentation, we will explain the different types of integration with MyFatoorah. This guide helps developers to get a better understanding of the exact technical endpoints and functions needed. It will serve the business accordingly and save development time and efforts to project the required business needs on the desired API and integration. Integration Methods Embedded Payment (Recomme...

### CHANGED: https://docs.myfatoorah.com/docs/v3-auth-capture

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `2fc0a3e292fd30a79e18d17660aa3ffc7b8134bc80ba3b49d9f3d4646f5a4179`
- Current status: OK / hash `452b03c8a70e2711aa3b8f972f92d115b0a1ea2acd315d6a929ab94af35f5771`
- Excerpt: Authorize & Capture Capturing/Releasing Amounts Introduction When a payment is made using a gateway that supports Authorization & Capture , you have the ability to capture (either partially or fully) the amount of the authorized payment or release it back to the customer. Once the invoice is paid, it will appear in your MyFatoorah Portal and in the response of GET /v3/payments with the status "AUTHORIZE" . You can perform Capture or Release operations using the PUT /v3/payments/{paymentId} endpo...

### CHANGED: https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `1c01a35d2d2bb7d514ac8da8247b40c0d7724f09d0c24ed608ccf50aa9938bf5`
- Current status: OK / hash `f0a75f6f6301bcb944beeb65dae4c4f9c45d3ca1cdd84f99297bcff89b7567e9`
- Excerpt: Updating Payment Status Guidelines Overview In this section, we will cover the paths available to update the order status on your system after the customer makes the payment on the MyFatoorah system. We are covering the: Redirection to RedirectionUrl Transactions Webhook Handling both the webhook and the redirection together RedirectionUrl: After the customer makes a payment, MyFatoorah redirects the customer to the provided redirection URL, appending the PaymentId to the URL. Steps: Call the (...

### CHANGED: https://docs.myfatoorah.com/docs/webhook-v2

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `348b30735b474c34fb0497019f178b45cdbec517e68a342b9b2c87af1481f328`
- Current status: OK / hash `9ca4e03a9156a40cc69c2106d7a3801c2c9c11e52ab57ec416b4deecee863472`
- Excerpt: Webhook V2 Introduction In Webhook v2, we have restructured the webhook event format and enriched its content for each event type. Compared to Webhook v1, it now provides more detailed information. Additionally, the webhook structure has been redesigned to follow an object-based format. With Webhook v2, you can configure a retry count for events that your server fails to receive and specify the delay between each retry. The maximum number of retries is 5 , and the maximum delay is 180 seconds ....

### CHANGED: https://docs.myfatoorah.com/reference/update-payment

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `e4498af9d24f37715397f17552b600b91e3c927e4edc3c36a2ff38d35979b9a2`
- Current status: OK / hash `c61770d2badd575105e81f55feb4619b6d52603fabc5a5b57f9ad2688bee7fe5`
- Excerpt: Update Payment (Capture or Release) put https://apitest.myfatoorah.com /v3/payments/ {paymentId} Used in the Auth & Capture flow to capture full/partial amount or release the authorized amount back to the customer. Only one Capture or Release operation is allowed for each invoice. Path Params paymentId string required Body Params OperationType string enum required Operation type to execute. Use CAPTURE to capture the authorized amount (fully or partially) or RELEASE to return the full amount to...

### CHANGED: https://docs.paytabs.com/

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `c5705042f6c6a42b6748d110b8f7d963ce86c19a1316953636c77d21e0fd45ea`
- Current status: OK / hash `570d06f7cfe9c9152c7f047a5dde9605903baf8dd696d9698f7b8627747b88e8`
- Excerpt: PayTabs Technical Portal Integrate your system through our Empowering your payments journey with seamless integration, comprehensive support, and innovative solutions tailored to your business needs for a smooth and efficient experience. Scroll Down Seamless Integration with Top Platforms Find your best case Build, launch and get paid. Enable your platform with flexible payment solutions for every business model. Find Your Use Case Meet Our AI Assistant! Our AI chatbot is ready to assist you 24/...

### CHANGED: https://docs.tabby.ai/api-reference/checkout/create-a-session

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `8768cb80deb18e42130eb6c481cc3c8fd8e9cd69b4d3309f756771d2d74ce617`
- Current status: OK / hash `2f78378f1375d1a9037fa4eeab3b6220215ae3aaf4c804dd2dbd8fb7c2da326d`
- Excerpt: Create a session cURL curl --request POST \ --url https://api.tabby.ai/api/v2/checkout \ --header 'Authorization: Bearer <token>' \ --header 'Content-Type: application/json' \ --data ' { "payment": { "amount": "100", "currency": "AED", "buyer": { "name": "John Doe", "email": "jsmith@example.com", "phone": "500000001", "dob": "2000-01-20" }, "shipping_address": { "city": "Dubai", "address": "Dubai", "zip": "1111" }, "order": { "reference_id": "1001", "items": [ { "title": "Name of the product", "...

### CHANGED: https://docs.tabby.ai/api-reference/payments/retrieve-a-payment

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `b3e0e85ad4285dae2e75ac5dfbd9815fd9a70a7af039de153281dd7cb27b7501`
- Current status: OK / hash `cc799c4bb3085623b150c8bfd23bff84202a0b789f0c3d95048bc58dea059243`
- Excerpt: Retrieve a payment cURL curl --request GET \ --url https://api.tabby.ai/api/v2/payments/{id} \ --header 'Authorization: Bearer <token>' { "amount" : "100" , "currency" : "AED" , "buyer" : { "name" : "John Doe" , "email" : "jsmith@example.com" , "phone" : "500000001" , "dob" : "2000-01-20" }, "shipping_address" : { "city" : "Dubai" , "address" : "Dubai" , "zip" : "1111" }, "order" : { "reference_id" : "1001" , "items" : [ { "title" : "Name of the product" , "quantity" : 1 , "unit_price" : "0.00"...

### CHANGED: https://docs.tabby.ai/introduction/what-is-tabby

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `15f762465415b3040b4107c70694bb8729e4afb83017163e7d8fa47dbb92e354`
- Current status: OK / hash `f6e10623dc103eca94637dfe6e260b0b444c1752811897113be34c4f00ed78b7`
- Excerpt: Introduction What is Tabby? Tabby is MENA\u2019s biggest Buy Now Pay Later, operating in KSA, UAE and Kuwait. Tabby lets merchants grow their business by offering their shoppers flexible payments, and is constantly growing its product offering. Pay in Installments - Split your purchase into several payments Online - easily through nearly any e-commerce platform In-Store - with the Tabby Card, through paylinks or with a QR code Pay next month - Pay for groceries, food, rides at the end of the month Wa...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/checkout-flow

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `aab2bf526106ddac5cf811fb4fbb2f4c2c7f758fd26e6e59fc44802c271adaa9`
- Current status: OK / hash `a031e7c276e61751f3f56617d1072b7d7cbd997807d75daed5b2bcb1f37bf702`
- Excerpt: On this page Tabby on Checkout Recommended: Checkout Snippet Alternative: Payment Method Description Background Pre-scoring Check Quick Implementation Response handling Possible rejection_reason values Best Practices Eligibility Check vs Session Creation Checkout Session Initiation Example of a minimal payload for eligibility check Response and Validation At Tabby Hosted Payment Page Redirection to the Store Handling redirects Approved messages for redirects Allowed characters in redirect URLs (...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/payment-processing

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `f22a5cc5cfdc0b82e6c5f4d8365ab9285f1a20d2bf5b8a9716491d769a10814a`
- Current status: OK / hash `a13f102a85f012ab9893af436734db5093edcc721881db5ce35cd50c7bee5fae`
- Excerpt: On this page Payment Verification Don\u2019t Miss Authorized Payments Session Expiration Payment Capture Missing Captures Payment Refund Refunds Troubleshooting Idempotent Requests Online Custom Integration Payment Processing What to do after the customer completes the Tabby checkout: verify the payment, capture it, and process refunds when needed. Once the customer completes the Tabby checkout, three server-side steps remain: 1 2 3 \u200b Payment Verification Never rely on the redirect alone \u2014 always ver...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/payment-statuses

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `5ddc2a0dd6b2998536a4f9124cc2d30db43eb70b43f8971fe000946752ff9030`
- Current status: OK / hash `2426c26c0ec31d9b7d11a9a8c7a08c50589260708c3ef4453f720f271cbda9b0`
- Excerpt: On this page Payment Lifecycle Merchant Dashboard Statuses Lifecycle in Detail Statuses in API Responses vs Webhooks Online Custom Integration Payment Statuses How a Tabby payment moves through its lifecycle, and how API statuses map to what you see on Merchant Dashboard. \u200b Payment Lifecycle The status field of a payment ( GET /api/v2/payments/{id} ) has five possible values: CREATED , AUTHORIZED , CLOSED , REJECTED , and EXPIRED . Two statuses allow repeated actions without changing: a partial...

### CHANGED: https://docs.tabby.ai/pay-in-4-custom-integration/webhooks

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `f8aadb29f59d2f35ebc6f83ef27e9b1bb6ed785d548ec61006adf2ff24e7eeb5`
- Current status: OK / hash `7a5b60bf90872fc5a7d251a88d01d794295ea086f3b8fa95f3e75d3b028358e7`
- Excerpt: On this page How They Work Payload Supported Events A Typical Payment Best Practices Retry Attempts Online Custom Integration Webhooks Get notified about payment status changes: registration, payload, supported events, delivery order, and retries. Tabby Webhooks are HTTPS callbacks that notify you about payment-related and token-related events. You register a URL once, and Tabby sends a POST request to it whenever an event related to your account occurs \u2014 even when the customer never returns to...

### CHANGED: https://docs.tamara.co/

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `5a96a872a6ee737e3afb27512ef7b882ba09ad34a80565d2abe2ee76be3cdb06`
- Current status: OK / hash `5fa6f7fa5acded8571b4f11be195c777119a0cd0c7be5c6bfc9a08b74d41dd4b`
- Excerpt: Explore our comprehensive library Integrations Platform Integrations Tamara works with all major eCommerce platforms to make integration effortless. Direct Integrations Explore direct integration options with Tamara\u2019s API to provide customers with a smooth checkout experience. In-Store Checkout Enhance your in-store payment experience with our versatile integrations. Testing Guide Your key to seamless test transactions - our testing guide. Widgets Enhance your e-commerce site with Tamara\u2019s widge...

### CHANGED: https://docs.tamara.co/docs/direct-online-checkout

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `b3a558c4d32acf2baaa54bbe27e5438e6359449cab01b10456f4a00c3e41a13f`
- Current status: OK / hash `2a609f410e432352c943dc012b09e1b29b30b5aebb791d9bce621afdb4f54aae`
- Excerpt: Online Checkout \U0001f6a7 This page is a high-level explanation only. Consult the API References for further details on how to use our APIs properly. The Tamara online payment journey will always start with a customer adding items to their cart and heading to the checkout page to choose Tamara as the payment method to use. Step 1. Create Checkout Session API Customer now sees Tamara as an available payment method on your store, and proceeds to choose it to checkout with. When a customer decides to pay u...

### CHANGED: https://docs.tamara.co/docs/online-order-status-flow

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `9d2c50e5cbfda6100f6284b8f08514df9f99db97b5c71243cbe2f9c7d7d9f1bf`
- Current status: OK / hash `90319cc37b2c70bc9cac9cd1dbc673701f538cc90e839cdaa00851d08650f50d`
- Excerpt: Online Order Status Flow To integrate with Tamara and connect your e-commerce platform with our service, it is necessary to fully understand how the flow of our order statuses work and map them to your system\u2019s statuses. \U0001f449 Click on any status in the flow to learn more about it. Online Order Status Flow Online Order Status Description new Customer has initiated the checkout session with Tamara as a payment method. declined Customer was declined to continue the payment with Tamara . expired Custom...

### CHANGED: https://docs.tamara.co/docs/transaction-authorisation

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `476fe311d7ddda5b1a92db4cec559736462c16fa87b9ebbb07fb921fa411b8d0`
- Current status: OK / hash `6e0e8d6795abc45e559d77a4e4d679ddd4d051feaad8ef7797c9b59e44ed8a01`
- Excerpt: Webhook Registration & Order Authorisation One of the most important steps merchants must do to complete online checkout integration is the Order Authorisation. This is an important step in the Tamara online order flow as it ensures that you, as the merchant, successfully acknowledge receiving the approved order status notification from Tamara . Register a notification webhook URL (One-time Only) 1. Login to Tamara's Partner Portal 2. Go to Settings --> General Settings --> Webhooks Click on Add...

### CHANGED: https://docs.tamara.co/reference/captureorder

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `de2bbeaf41edbf5ca77538cda046504e314267cf92c84a4902e3255c438c7c85`
- Current status: OK / hash `6c1b84766bf4813857d2c3f3ae2fba96aeda88f72641697a3ce06f224c3ed757`
- Excerpt: Capture Order post https://{environment}.tamara.co /payments/capture This endpoint is requested to perform a full or partial capture of the order, confirming the fulfillment or shipment of the items to the customer. The order status value will be fully_captured or partially_captured based on the total amount value sent in the request. Body Params order_id uuid required Defaults to 8fe4cce9-d0aa-4020-a863-c708547795e9 Unique Tamara order_id , obtained from the response of create checkout/in-store...

### CHANGED: https://docs.tamara.co/reference/getorderdetails

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `372bf43aa40570c2fccde7a1a5906e74c0d4e45eae30a3dd4103df71c29a194d`
- Current status: OK / hash `1e20ce887213c7baa818c780e69c4079eea11972b4f28062746411e5f635b6d7`
- Excerpt: Get Order Details by Tamara's order_id get https://{environment}.tamara.co /orders/ {order_id} Fetch all the order details available on Tamara's side using the unique order_id that is issued by Tamara for every order whether online or in-store. Path Params order_id uuid required Defaults to ff776045-513b-4cd7-8b4f-e60673daad84 Unique Tamara order_id from the response of the creation of the checkout session whether online or in-store. Response Updated <relative-age> ago What\u2019s Next Update order_r...

### CHANGED: https://docs.tamara.co/reference/simplifiedrefund

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `948e8e94f90d9329bec8f472ebc3ae7581717c20267732909901423dd93231d3`
- Current status: OK / hash `62cfbda5c0b48006c2e7a17d7973dc4dddebfb9c79f7a39f23f78b0bcd668f03`
- Excerpt: Simplified Refund post https://{environment}.tamara.co /payments/simplified-refund/ {order_id} This API is to be used to process refunds for captured orders. Path Params order_id uuid required Defaults to ff776045-513b-4cd7-8b4f-e60673daad84 Unique Tamara order_id from the response of the creation of the checkout session whether online or in-store. Body Params total_amount object required Total amount to be refunded to consumer, not including any discount amount. comment string required Defaults...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `fc75d00f93749f1b6ca04f3073af0c83b67101753c624d39c3eb4a83cd304701`
- Current status: OK / hash `871bbc9ecf5472d9d5926577807f94f066b84daacc01800f7a2edd8afbc732e8`
- Excerpt: Copy On this page Direct Payment (Hosted) Direct Payment is an API to allow customers to integrate Easykash\u2019s payment methods into their website. Prerequisites: To be able to begin the integration of your website with Direct Payment, you must have the feature enabled for your EasyKash business account (contact support for that). When it\u2019s enabled head to the Integration Settings page on your side menu (under Settings) for the below: The API Key is your authentication in the initial request. Call...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/cash-api-cash-only

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `7b60761115c8a33eb801278ac651a5323eb16cc4884747b6fc9c5e102a451d94`
- Current status: OK / hash `96f5b2e8dad3de701c996ae3a45a9ce33bd15fc2dbdf006c1a22bee237f63ce5`
- Excerpt: Copy On this page Cash API (Cash-only) This feature only works for Cash payment methods. What is our API feature? For Businesses that already have running websites, EasyKash provides an integration feature to perform two things. Create payments (cash only) with two types. Quick Cash (Type: in) and Cash Out (Type: out) Callback service, to confirm current pending payments (all payment methods) Prerequisites: To be able to begin the integration of your website with Easykash, you must have the feat...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `e19e6bec43d16d0a1040a90c2676f2ecfd0c077a196c21a50697bdc550b83103`
- Current status: OK / hash `4ac5347cbf130f9870178b89cb1968b8b9dc65f3736232b5876395f9d7538352`
- Excerpt: Copy On this page Callback Service If your API service is enabled for your account, after every successful payment, you receive an API notification to the callback URL added in your Easykash account If you still haven't configured your Callback URL, head to your Integration Settings page and configure it ahead of this step. Callback URL is the URL you\u2019ll receive the details of transactions on such as status, reference number, etc. Make sure it\u2019s a working URL on your end that will receive and pr...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service/callback-response-verification

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `b63ec30ffa7e4d6f9e7c791d4be31c1784c287818ccb1e345b66a4bcf76c7e80`
- Current status: OK / hash `222bb59f985dfa011366b4262567369f19f919ac3a8f109434b5e2b3baf69931`
- Excerpt: Copy On this page Callback Service Callback response verification Callbacks rely on HMAC authentication to verify response's identity and integrity of its data. Prerequisites HMAC secret key is needed for response verification, you can find it in your Integration Settings page HMAC calculation Whenever you receive a callback from Easykash, you will receive a value of the HMAC related to the data, HMAC value is signatureHash in response body . In order to calculate an HMAC similar to the one you...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api

- Providers: egypt-payment-guardian:easykash, egypt-payment-guardian:egypt-bnpl-methods, mena-payment-guardian:easykash, mena-payment-guardian:valu-souhoola
- Previous status: OK / hash `3563c5dfffb6a4094750a35a49c2c37e0c2f91be20b61839cf76298cdd28edf5`
- Current status: OK / hash `c289293225b7d00ad1f1c8fecdd7eb5b757f6d31605e4cc78c8bae3531e42b87`
- Excerpt: Copy On this page Pay API API to create direct pay link Create direct pay link POST https://back.easykash.net/api/directpayv1/pay To get your api key, open your Integration Settings page Headers Name Type Description authorization * String API key Request Body Name Type Description amount * number Base amount. Amount must be in the currency being sent and NOT in EGP. Note: The end user will be charged in EGP ( Total amount in currency sent * Exchange Rate at the time of payment). Deprecated proc...

### CHANGED: https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/payment-inquiry

- Providers: egypt-payment-guardian:easykash, mena-payment-guardian:easykash
- Previous status: OK / hash `687d8e7c29026baded764f70512f1e579a95a900232822a2989f4f2208b0cc4b`
- Current status: OK / hash `b111292930add860ce9547622dc2fb2bc1cd373bde0aaf211dbac55809fc9573`
- Excerpt: Copy On this page Payment Inquiry If you'd like to inquire about a specific transaction, use this payment inquiry API below. Inquire about specific transaction on Easykash POST https://back.easykash.net/api/cash-api/inquire Headers Name Type Description authorization * String API key Request Body Name Type Description customerReference * String Product's reference number of the Direct Pay customer Request Example { " customerReference " : " 111 " } Response PaymentMethod Method of payment. All p...

### CHANGED: https://hyperpay.docs.oppwa.com/integrations/server-to-server

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `96af9980c921bcbd854ccc2761e23133d52932e9bdcaa3d36cfe7fe0b2f14e6e`
- Current status: OK / hash `d9610a43ec824a47834d912b2226770b0c9605bf49a17cb5dca2d2b066a93324`
- Excerpt: Server-to-Server Integration Guide Last updated: December 27, 2024 This guide walks you through the entire payment journey, from start to finish. As a merchant, you\u2019ll be in full control, collecting all card and payment details directly. This behind-the-scenes process ensures a smooth and seamless experience for your shoppers. Navigate the complexities of the payment landscape with ease and efficiency, all thanks to our Server-to-Server guide. Start your journey today! PCI-DSS Compliance : To co...

### CHANGED: https://hyperpay.docs.oppwa.com/integrations/widget

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `e87ecf461786ddc2a2981e5a020be7c7a8429367022fc530d51080a863303156`
- Current status: OK / hash `e74d9aa10204afe8899d0857a8ae83053085f902fff1d6aa3c47f977011a3a0f`
- Excerpt: COPYandPAY Integration Guide COPYandPAY is a SAQ-A compliant payment-form solution, making it both secure and simple-to-integrate. There are just three simple steps required to integrate : How it works 1 Prepare the checkout Send the request parameters server-to-server to prepare the payment form. 2 Create the payment form(s) Display the payment form on your checkout page and the shopper submits the payment information. 3 Get the payment status Find out if the payment was successful. 1. Prepare...

### CHANGED: https://hyperpay.docs.oppwa.com/reference/parameters

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `4f1d228550e2197ad2aa140f6b87d5fe15b888a6070d62efd46faeebe0f98fd8`
- Current status: OK / hash `dec0ba1e1a2af1e17721ee26026be54ceb59ead23d4475e7cf57a7074f9bd50c`
- Excerpt: API Reference Introduction This reference section provides you with a complete and in-depth description of the Open Payment Platform API. Hosts Test: https://eu-test.oppwa.com/ Live: https://eu-prod.oppwa.com/ Security / Authentication All requests must be sent over SSL All requests are authenticated against an Authorization Bearer header with an access token. All the other data parameters are sent as body parameters, see Authentication Parameters for more information. Throttling Throttling is t...

### CHANGED: https://hyperpay.docs.oppwa.com/reference/resultCodes

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `43008054bb1aeed1bb4d7325360778bb10089d593667fe3d31820d8e8055aa33`
- Current status: OK / hash `6cc7567fe1841a11393b46be06f9506bdbc0697e9e48fd109326795b6516da8a`
- Excerpt: Result Codes Last updated: September 29, 2025 This guide helps merchants and integrators understand the structure, meaning, and recommended actions for each result code returned in the result field of the API response, enabling accurate handling of transaction outcomes across success, pending, rejection, and risk scenarios. Quick links What are result codes? Download JSON result code list Success & pending transactions Rejected transactions Rejections specific to risk handling Rejections due to...

### CHANGED: https://hyperpay.docs.oppwa.com/support/webhooks

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `95676faa6ad9e2bfdf6d6fb41dace9d60346b0ea29f0880e66865b7d251ac8e7`
- Current status: OK / hash `df71730fc06af8d30b9ddb659c085bd8ed621a8a0bb0210036fbf99a4c6db672`
- Excerpt: Webhooks FAQ Last updated: May 12, 2026 How can I verify that my webhook URL is correctly set to receive notifications? You have the ability to send test notitications to the webhook URL at the configuration time in the user interface. This guarantees the correctness of the webhook setup before the notifications feature is turned on. I'm not receiving webhooks anymore. Am I alerted when something goes wrong? An automated daily email is going to be sent to all the configured webhook email address...

### CHANGED: https://paymentservices.amazon.com/docs/

- Providers: mena-payment-guardian:amazon-payment-services
- Previous status: OK / hash `f9377ab03442df5636e3da80f442387d693c5c5cdd322b49d3cd919e9deb9c06`
- Current status: OK / hash `d02277c0b5c3cef6089819c5d37eca0843c03443f1a87cd50ffeed27ae2190e0`
- Excerpt: Brewing next-gen API docs. Got feedback? \u2192 Documentation Explore guides, examples, and resources for every step of your Amazon Payment Services journey. Quickstart API Reference amazon-payment-services.com Payment Status Processing Transaction ID #APS-2024-156 Amount 499.99 Secured by APS \u2022 Processing time: 2.3s Choose your integration path From no-code solutions to fully customizable APIs, we have the right integration type for your business needs. No-Code Solutions Payment Links for invoicing...

### CHANGED: https://paymentservices.amazon.com/docs/api/faqs/faq

- Providers: mena-payment-guardian:amazon-payment-services
- Previous status: OK / hash `754d533d3a27bcde4f4b3566bf3ee20ea2c529ce06bffbe82e7d3e1f37a00ecf`
- Current status: OK / hash `89ef9aa9ef24f1d87da74a76deada47cf9e6987e88bdd9f1feffbe1b00f0ff42`
- Excerpt: FAQ FAQs Frequently Asked Questions Copy page Copy page Copy page as Markdown for LLMs Open in Claude Ask questions about this page This comprehensive FAQ addresses the most common questions and challenges developers encounter when integrating with Amazon Payment Services (APS). Each section provides practical solutions, step-by-step guidance, and direct links to relevant documentation. Can't find what you're looking for? Check our Error Codes Guide or contact our support team at merchantsupport...

### CHANGED: https://paymentservices.amazon.com/docs/managing-payments/capturing-payment

- Providers: mena-payment-guardian:amazon-payment-services
- Previous status: OK / hash `b356369933eab867d3dccc41a23dba7eb29e398e49482c639f0b92dfffecc94f`
- Current status: OK / hash `7c16cfd7467325e0f5af5d9bbbd286cb9ce189ea9c075fb58540122db5f93996`
- Excerpt: Managing Payments Capturing a Payment Capturing a Payment Copy page Copy page Copy page as Markdown for LLMs Open in Claude Ask questions about this page Capture is used after authorizing a payment, as authorization alone doesn't transfer the funds it only puts them on hold. To complete the transaction and move the money to your account, the payment must be captured within a set timeframe usually 5-7 days maximum. Amazon Payment Services provides merchants with flexible options to capture paymen...

### CHANGED: https://paymentservices.amazon.com/docs/managing-payments/tracking-a-payment/webhooks

- Providers: mena-payment-guardian:amazon-payment-services
- Previous status: OK / hash `99cdd994c07dce8b924f11a1c6fc3b7360b5c6eac27f87159e3ecdbae2a6bdb2`
- Current status: OK / hash `91d4c927fe718ae0b9d7bfd7828307fca78f53b2e0ed306323b9a51e4a4e771f`
- Excerpt: Managing Payments Tracking Payments Webhooks Webhooks Copy page Copy page Copy page as Markdown for LLMs Open in Claude Ask questions about this page Amazon Payment Services provides real-time webhook notifications to keep your system synchronized with payment statuses. Webhooks ensure you receive transaction updates even when customers don't complete the return flow, making them essential for reliable payment processing. Overview \u200b Amazon Payment Services offers two types of webhooks for compre...

### CHANGED: https://paysky.io/docs/

- Providers: egypt-payment-guardian:paysky, mena-payment-guardian:paysky
- Previous status: OK / hash `c16607b8554b2d463cb15b617f28d7591f3ff928ab16974b07c1a31181b4ac81`
- Current status: OK / hash `b5c309578fa201211b2740d81e71ab11ee8d49f0606e2760b2cfd57ee19f84cc`
- Excerpt: API\u2019s & documentation 1 PaySky OMNI Gateway \u2013 Notification Services Integration Guide

### CHANGED: https://paysky.io/docs/paysky-omni-gateway-payform-plus-integration-guide/

- Providers: egypt-payment-guardian:paysky, mena-payment-guardian:paysky
- Previous status: OK / hash `7067db1e98f4d14eafd4a23331b2948ec9fa262fdb88450f15b3e9e66f3cc7d4`
- Current status: OK / hash `d48c2cdd8cbb8b1350ba20f20539b5a6901279346760025cbda1f4d41bf5650a`
- Excerpt: API\u2019s & documentation 1 PaySky OMNI Gateway \u2013 Notification Services Integration Guide

### CHANGED: https://paysky.io/docs/paysky-omni-gateway/

- Providers: egypt-payment-guardian:paysky, mena-payment-guardian:paysky
- Previous status: OK / hash `2df8bfdf67160753c8a813ef27ecf9a908503a6ae103352b402b5e9d243a277a`
- Current status: OK / hash `d48c2cdd8cbb8b1350ba20f20539b5a6901279346760025cbda1f4d41bf5650a`
- Excerpt: API\u2019s & documentation 1 PaySky OMNI Gateway \u2013 Notification Services Integration Guide

### CHANGED: https://paysky.io/docs/paysky-paybutton-sdk-android-guide/

- Providers: egypt-payment-guardian:paysky, mena-payment-guardian:paysky
- Previous status: OK / hash `0cc2958e87189a444f34f344bf84edb330d3477623286fd00458769ae262a09a`
- Current status: OK / hash `d48c2cdd8cbb8b1350ba20f20539b5a6901279346760025cbda1f4d41bf5650a`
- Excerpt: API\u2019s & documentation 1 PaySky OMNI Gateway \u2013 Notification Services Integration Guide

### CHANGED: https://paysky.io/docs/paysky-paybutton-sdk-ios-guide/

- Providers: egypt-payment-guardian:paysky, mena-payment-guardian:paysky
- Previous status: OK / hash `767c13c3bc4bcc58eb8b7cde345d8541420a5bce384af1b207be2f2220a67bda`
- Current status: OK / hash `d48c2cdd8cbb8b1350ba20f20539b5a6901279346760025cbda1f4d41bf5650a`
- Excerpt: API\u2019s & documentation 1 PaySky OMNI Gateway \u2013 Notification Services Integration Guide

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000710069

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `59b90d2159f4b7a514e7a5675153da6bd6824cc9e00d8a7a6879ea26d6e86233`
- Current status: OK / hash `0b9c24654ccca1dd9bbcee7d38a862933da4cb94cc8a285b4312e3878c202cdd`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for How to configure Instant Payment notification (IPN)? Modified on Sun, Mar 9, 2025 at 12:34 PM In this article you will get to know: Video Tutorial What is the Instant Payment Notification (IPN)? How to configure a new IPN? How does the IPN service work? IPN vs Callback: How to Configure UserAgent Sent in IPN Request Headers? Sample IPNs Response Payload: Default Web JSO...

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000718961

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `d09d6486399edfee3fa5ca89958d713983d446f58b7b6ae05ee44313437dd689`
- Current status: OK / hash `9432f6d9eb12f8312cd817b27d9970a11f9869dff1427c9d028e75ba9d3798c2`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for How to verify the response received from PayTabs? (Signature Verification) Modified on Sat, Dec 17, 2022 at 3:58 PM To ensure that the response you are receiving is genuine, we are sending a custom header Signature including an HMAC signature hashed by Profile ServerKey for you to validate and verify the response. In this article you will be going to know how to perform...

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000803800-request-response-parameters-the-return-url-return-

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `898e5a34e5f59d23d9fa9c1dc9ef479fbb020ce6a7c37f8f40cb014a189b4a1e`
- Current status: OK / hash `45ae77b53ade9b6ad24f4576d0dec1b0bba45dbb8334ce8ccfaac2bbcf29df1b`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for Request/Response Parameters | The Return URL (return) Modified on Tue, Jun 4, 2024 at 12:21 PM Paytabs provides you with a collection of API endpoints which used to process all payments, regardless of if they are through either your own payment pages, the managed payment pages, or if you are using the hosted payment pages. This article is dedicated to the clarification...

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000805341

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `2d3c33627d76b46cb2d19379ae48985742c368d1ef8bed712317feb9cf47aa59`
- Current status: OK / hash `093af641acb689d05c090743b2762802e3299d4a693b0a723d616d97f4c9b02a`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for Request/Response Parameters | The Callback URL (callback) Modified on Wed, Jan 4, 2023 at 3:55 PM Paytabs provides you with a collection of API endpoints which used to process all payments, regardless of if they are through either your own payment pages, the managed payment pages, or if you are using the hosted payment pages. This article is dedicated to the clarificati...

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000818152-request-response-parameters-cart-id-cart-id-

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `16b22a6646b173cd1b6683e1b72e9fb213ecba7e2c3063702d731f31f2503487`
- Current status: OK / hash `c6257ea8b0a069bf54ce58feca7b306ed787b064acc6426630c4575b49330689`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for Request/Response Parameters | Cart ID (cart_id) Modified on Wed, Jan 4, 2023 at 1:31 PM Paytabs provides you with a collection of API endpoints which used to process all payments, regardless of if they are through either your own payment pages, the managed payment pages, or if you are using the hosted payment pages. This article is dedicated to the clarification of the...

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000818154-request-response-parameters-cart-amount-cart-amount-

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `6ef6d9bb6e60d8df410a1dfa524467364b17e1e9e70198b0f4610df04c105d4e`
- Current status: OK / hash `cee9047d6fe74cc1d03215247c88c33657f22bb37e3b5759ad93ad7100cc52d1`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for Request/Response Parameters | Cart Amount (cart_amount) Modified on Wed, Jan 4, 2023 at 6:10 PM Paytabs provides you with a collection of API endpoints which used to process all payments, regardless of if they are through either your own payment pages, the managed payment pages, or if you are using the hosted payment pages. This article is dedicated to the clarification...

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000818155-request-response-parameters-cart-currency-cart-currency-

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `c89abbc928aa2d255008f3eb018553059f06108cd83f3b603fa39da13fda5738`
- Current status: OK / hash `b2a21b855fe311ed46b542647f11ed9d5175bc4e3cf500a7c2b9569eae416043`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for Request/Response Parameters | Cart Currency (cart_currency) Modified on Tue, Jun 4, 2024 at 12:16 PM Paytabs provides you with a collection of API endpoints which used to process all payments, regardless of if they are through either your own payment pages, the managed payment pages, or if you are using the hosted payment pages. This article is dedicated to the clarific...

### CHANGED: https://support.paytabs.com/en/support/solutions/articles/60000992876-3-2-1-hosted-payment-page-apis-initiating-the-payment

- Providers: mena-payment-guardian:paytabs
- Previous status: OK / hash `73b330b26335b4a36b6895408677adce2eab70ed7af483813e89ec21ddc042eb`
- Current status: OK / hash `e06616c6007bf71c6fef92abb84d2f2560624f5fb065128b5316fed0421f73a3`
- Excerpt: Recent Searches No recent searches Popular Articles Articles View all Topics View all Tickets View all Sorry! nothing found for 3.2.1 Hosted Payment Page APIs | Initiating the payment Modified on Tue, Jun 4, 2024 at 11:22 AM Paytabs provides you with a collection of API endpoints which used to process all payments, regardless of if they are through either your own payment pages, the managed payment pages, or if you are using the hosted payment pages. Hosted Payment Page integration type is suita...

### CHANGED: https://www.hyperpay.com/integration-guide/

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `665d7433d77af4fb1bb925dc3ba643e22c6e34a5828577ceef902fbd77f280ed`
- Current status: OK / hash `84a558a32a6a5f526e0e90fac391d0e572175c965d87ae105b728629204f0da5`
- Excerpt: Integration Guides The HyperPay platform offers a complete, easy-to-use guide to enable seamless integration of our end-to-end payment gateway for mobile and desktop browsers. Through a unified API, you can enable and gain access to all platform features. Choose one of the options below to quickly get started Integration Options COPY AND PAY COPYandPay is our JavaScript payment widget that sends sensitive payment data directly from the Shopper\u2019s browser to our paymets platform. Learn more SERVER...

### CHANGED: https://www.kashier.io/

- Providers: egypt-payment-guardian:kashier, mena-payment-guardian:kashier
- Previous status: OK / hash `6e82608cb1e44a138d9fffad56ea31ced101d690e12682bb0fee8a717c1135e6`
- Current status: OK / hash `d053e8ddd717abb0a782efe94e6f6bdd31adc8ae352133e9388f51ca1b4f5f94`
- Excerpt: Kashier | Online Payment Platform Company Pricing Partners Developers Support Create A Free Account Log In \u0639\u0631\u0628\u064a We Grow Your Online Sales We are a digital payment platform that aims to grow your business through enabling fast, easy and secure acceptance of digital payments from your customers and partners. We celebrate achievement when our digital services enable your business to interact with the growing digital economy, adding direct value to your bottom line. Create Free Account >> GROW SMART...

### CHANGED: https://www.kashier.io/blog-posts/kashier-api---power-flexibility-simplicity

- Providers: mena-payment-guardian:kashier
- Previous status: OK / hash `803b6c8b83639bd66b892c76868ee78c0f23a7bfead30391eecb400390dcd191`
- Current status: OK / hash `778db8953e67ba182e4d6e17848c9d5ddbc32c6cb3d669f0ff5e8d10cf729c0e`
- Excerpt: Kashier API - Power, Flexibility, Simplicity Company Pricing Partners Developers Support Create A Free Account Log In \u0639\u0631\u0628\u064a Back to Blog Kashier API - Power, Flexibility, Simplicity Business Growth August 12, 2025 Introducingthe Kashier API: Power, Flexibility, Simplicity In Egypt and across the MENA region, digital payment adoption is accelerating. Businesses, from growing e-commerce startups to established enterprises, need reliable payment infrastructure that is fast to integrate, secure by de...

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
