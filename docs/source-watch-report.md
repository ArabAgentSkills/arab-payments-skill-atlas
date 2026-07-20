# Source Watch Report

- Generated: 2026-07-20T07:13:09Z
- Total URLs checked: 109
- Changes detected: 12
- Full provider docs are not committed. Private watcher artifacts may contain fetched snapshots for maintainer review.

## Maintainer Result

Classification: `source_url_replacement`.

Private watcher issue #15 and run 29723426211 were reviewed after source snapshot capture completed before source-link checking. The reviewed public-safe update replaces Tamara's old combined webhook/order-authorisation monitored source with the provider's current webhook registration, authorise-order guide, and Authorise Order API sources from the official `llms.txt` index.

No payment behavior guidance changed. Geidea and MyFatoorah diffs were reviewed as docs feedback/footer chrome, Tamara capture/refund/get-order diffs were footer chrome, Tabby drift was docs-index metadata, and HyperPay parameter additions remain endpoint-level official-doc detail covered by the existing instruction to check current docs before field-level integration. Paymob `JS_CHALLENGE` responses remain manual browser-verification warnings and were not treated as broken links.

## Result

Public baseline refreshed after approved Tamara source URL replacements and source-watch normalization review.

## Changes

### CHANGED: https://docs.geidea.net/reference/capture-transaction-1

- Providers: egypt-payment-guardian:geidea-egypt, mena-payment-guardian:geidea
- Previous status: OK / hash `0e70ab8ebb34fa568705dd26a3fe03083d855bee15dc708a584691213880be33`
- Current status: OK / hash `620bf22c9d3587b23d7381c044450c127f7acb6f86fd800e77b8dd7632d10ff8`
- Excerpt: Capture Transaction post https://api.ksamerchant.geidea.net /pgw/api/v1/direct/capture Body Params orderId string required Unique ID for the order. callbackUrl string The URL of your callback server to receive useful information for keeping track of your inventory, records, etc. The URL may have protocol (http/https), subdomain (optional), domain name and path (optional) captureAmount float Amount for which capture is requested. Amount must be greater than 0.01. Won't be allowed to capture more...

### CHANGED: https://docs.myfatoorah.com/reference/update-payment

- Providers: mena-payment-guardian:myfatoorah
- Previous status: OK / hash `c61770d2badd575105e81f55feb4619b6d52603fabc5a5b57f9ad2688bee7fe5`
- Current status: OK / hash `7f5ad7a84ef7c602b19b078ea53edef5514eb252a823ee9a26f2f450e4f525b7`
- Excerpt: Update Payment (Capture or Release) put https://apitest.myfatoorah.com /v3/payments/ {paymentId} Used in the Auth & Capture flow to capture full/partial amount or release the authorized amount back to the customer. Only one Capture or Release operation is allowed for each invoice. Path Params paymentId string required Body Params OperationType string enum required Operation type to execute. Use CAPTURE to capture the authorized amount (fully or partially) or RELEASE to return the full amount to...

### CHANGED: https://docs.tabby.ai/llms.txt

- Providers: mena-payment-guardian:tabby
- Previous status: OK / hash `1b94cb99213215140c2b5370f82d9aa7612dce2913ffc55d734fea46536f4914`
- Current status: OK / hash `cc2fd4ea5184475a7783adc995751b276294973e002d38e2e6d7fb2594b6f42c`
- Excerpt: # Tabby ## Docs - [Create a session](https://docs.tabby.ai/api-reference/checkout/create-a-session.md): Creates a Checkout session. Creates Session and Payment, returns Pre-Scoring result (status), ids of Payment and Session. - [Session creation payload model](https://docs.tabby.ai/api-reference/checkout/session-payload-model.md) - [Approve disputes](https://docs.tabby.ai/api-reference/disputes/approve-disputes.md): Approve disputes (refund money to the customer). Only 20 disputes can be approve...

### NEW: https://docs.tamara.co/docs/pp-order-mgmt-authorise-order

- Providers: mena-payment-guardian:tamara
- Current status: OK / hash `228dbda0244131f4bb8c39c930b2c99361e86adda59c048c065735683d2ec449`
- Excerpt: Authorise an order Once Tamara verifies the customer's payment and approves the order, it's considered as paid, and you should proceed accordingly by authorising the order at your end. Step 1. Click on the Approved order to be authorised to go into its Order Details, then click on the Authorise button. Step 2. Click on the Authorise Order button to complete the authorisation of the order. \U0001f44d A confirmation message will appear on the screen to indicate that the order has been successfully authoris...

### NEW: https://docs.tamara.co/docs/webhook-subscription

- Providers: mena-payment-guardian:tamara
- Current status: OK / hash `6e89cdc1ed82bbb6bc133ce0cf6289109b3f137e9854319e9d7c0de803a816d8`
- Excerpt: Webhook Registration Register your notification webhook URL to recieve real-time events from Tamara. This one-time setup ensures your system is notified whenever a customer payment is processed succesfully. This is an important step in the Tamara online order flow as it ensures that you, as the merchant, successfully receive webhook notifications that confirm the customer payment, and further related events. Register a notification webhook URL (One-time Only) 1. Login to Tamara's Partner Portal...

### CHANGED: https://docs.tamara.co/llms.txt

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `880bafcb87ae7be86834fb0075cf151d40cd7347b9b3c8b0bc0214c1d5e807f4`
- Current status: OK / hash `0f4d7f65b16cb529eebd4cfd613d8b611c2bf74357d4f674578c8013be034a03`
- Excerpt: # Tamara Documentation and APIs Hub Documentation > Discover the ultimate toolkit right here, enabling you to seamlessly integrate Tamara's payment solution into your site with detailed guides and an interactive API explorer at your fingertips. ## Guides - [Get to know Tamara](https://docs.tamara.co/docs/introduction-to-tamara.md): Learn more about **Tamara**'s product offerings and how we can help you and your customers! - [Platforms Quick Start](https://docs.tamara.co/docs/platforms-quick-star...

### NEW: https://docs.tamara.co/reference/authoriseorder

- Providers: mena-payment-guardian:tamara
- Current status: OK / hash `21f9e7f62c64d6de154ec4213c5444ea56f8e4e3693858c22210717af6ca1e2d`
- Excerpt: Authorise Order post https://{environment}.tamara.co /orders/ {order_id} /authorise This endpoint plays a crucial role in the online checkout flow and should be executed upon receipt of the approved status webook event from Tamara . Its primary function is to update the order status to authorised ensuring status synchronization and smooth progression of the online order flow. \U0001f44d We now support Auto-authorisation! If this is enabled, then the order status will move from New --> Approved --> Fully...

### CHANGED: https://docs.tamara.co/reference/captureorder

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `543bded8eebc37e98306443b6f55e4d4c1bab11576ad0d7f77fb11eeea9159be`
- Current status: OK / hash `cc37743a7240969dfcf4aa97d200247bcdc4930e2beda219e52720b98b45e5a8`
- Excerpt: Capture Order post https://{environment}.tamara.co /payments/capture This endpoint is requested to perform a full or partial capture of the order, confirming the fulfillment or shipment of the items to the customer. The order status value will be fully_captured or partially_captured based on the total amount value sent in the request. \U0001f4d8 If an order is not Captured within 21 days from when it is Authorised, Tamara will auto-capture that order and it will be moved to Fully Captured status Body Par...

### CHANGED: https://docs.tamara.co/reference/getorderdetails

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `1e20ce887213c7baa818c780e69c4079eea11972b4f28062746411e5f635b6d7`
- Current status: OK / hash `6e8fe153ba0ad7283b9b59295d4fcb6eb5e5c2f7f347546a9a06314eb9406c9b`
- Excerpt: Get Order Details by Tamara's order_id get https://{environment}.tamara.co /orders/ {order_id} Fetch all the order details available on Tamara's side using the unique order_id that is issued by Tamara for every order whether online or in-store. Path Params order_id uuid required Defaults to ff776045-513b-4cd7-8b4f-e60673daad84 Unique Tamara order_id from the response of the creation of the checkout session whether online or in-store. Response

### CHANGED: https://docs.tamara.co/reference/simplifiedrefund

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `62cfbda5c0b48006c2e7a17d7973dc4dddebfb9c79f7a39f23f78b0bcd668f03`
- Current status: OK / hash `696a19714e607046ddec34e7a95ed5e15e0aa0cd5714451d73b14c6977434295`
- Excerpt: Simplified Refund post https://{environment}.tamara.co /payments/simplified-refund/ {order_id} This API is to be used to process refunds for captured orders. Path Params order_id uuid required Defaults to ff776045-513b-4cd7-8b4f-e60673daad84 Unique Tamara order_id from the response of the creation of the checkout session whether online or in-store. Body Params total_amount object required Total amount to be refunded to consumer, not including any discount amount. comment string required Defaults...

### CHANGED: https://hyperpay.docs.oppwa.com/reference/parameters

- Providers: mena-payment-guardian:hyperpay
- Previous status: OK / hash `dec0ba1e1a2af1e17721ee26026be54ceb59ead23d4475e7cf57a7074f9bd50c`
- Current status: OK / hash `f39783fbdd3b97a7043e581f951e06b5e4f6547207cb94a6736044bbfd7b0613`
- Excerpt: API Reference Introduction This reference section provides you with a complete and in-depth description of the Open Payment Platform API. Hosts Test: https://eu-test.oppwa.com/ Live: https://eu-prod.oppwa.com/ Security / Authentication All requests must be sent over SSL All requests are authenticated against an Authorization Bearer header with an access token. All the other data parameters are sent as body parameters, see Authentication Parameters for more information. Throttling Throttling is t...

### REMOVED: https://docs.tamara.co/docs/transaction-authorisation

- Providers: mena-payment-guardian:tamara
- Previous status: OK / hash `6e0e8d6795abc45e559d77a4e4d679ddd4d051feaad8ef7797c9b59e44ed8a01`

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
