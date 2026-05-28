# Geidea Egypt

- Provider: Geidea Egypt
- Scope: Egypt hosted checkout, direct API, Pay by Link, callbacks, refunds, cancellations, capture, subscriptions, tokenization, and PSP-routed Egypt methods.
- Priority: P0
- Readiness: A
- Public docs status: public.
- Last checked: 2026-05-29
- Source confidence: High for public docs, Egypt endpoint, callback signature, checkout signature, refund/cancel distinctions, and transaction management; verify account enablement and endpoint version before coding.
- Sources:
  - https://docs.geidea.net/llms.txt
  - https://docs.geidea.net/
  - https://docs.geidea.net/docs/geidea-checkout-v2
  - https://docs.geidea.net/docs/pay-v2
  - https://docs.geidea.net/docs/sample-callback-responses
  - https://docs.geidea.net/docs/pay-by-link-apis
  - https://docs.geidea.net/docs/refund-2
  - https://docs.geidea.net/docs/cancel-order-1
  - https://docs.geidea.net/docs/void-1
  - https://docs.geidea.net/reference/capture-transaction-1
  - https://docs.geidea.net/docs/overview-1
  - https://docs.geidea.net/docs/valu
  - https://docs.geidea.net/docs/souhoola

## Use When

Use for Geidea Egypt checkout, hosted payment page, Direct API, Pay API, Pay by Link, callbacks, refunds, cancellations, capture/auth flows, subscriptions, tokenization, Meeza QR, bank installments, valU, and Souhoola routed through Geidea.

## Source Map

- Overview explains checkout, Direct API, Pay by Link, order query, refunds, card on file, and callbacks.
- HPP Checkout docs provide create-session fields, server-to-server warning, amount/currency format, callback URL, return URL, signature rules, and Egypt endpoint.
- Callback docs provide callback signature construction and response code checks.
- Refund, cancel, void, capture, and transaction-management docs define operation distinctions.
- valU and Souhoola docs define PSP-routed BNPL method handling for Egypt.
- Agent-readable docs: `https://docs.geidea.net/llms.txt` for Geidea Egypt source discovery only; do not import unrelated MENA provider assumptions.

## Integration Paths

- Geidea Checkout/HPP pre-built UI.
- Direct API flow for merchants prepared for higher PCI scope.
- Pay by Link APIs and portal-based payment links.
- Mobile SDKs and ecommerce plugins.
- Tokenization, card-on-file, and subscriptions where enabled.
- Transaction/order fetch APIs for reconciliation.
- Refund, cancel order, void, and capture where supported for the merchant/account/region.

## Setup Prerequisites

- Geidea merchant profile and credentials.
- Correct regional endpoint: Egypt uses `https://api.merchant.geidea.net/`.
- Merchant public key and API password stored in backend secrets.
- Checkout session creation performed server-to-server.
- Callback URL uses HTTPS and is reachable.
- Local order stores expected amount with two-decimal precision, ISO alphabetic currency such as `EGP`, merchant reference, Geidea order ID when returned, and payment attempt state.
- PCI impact reviewed before using Direct API.

## Auth And Secret Boundary

Geidea Create Session uses basic authentication with merchant public key as username and API password as password. The API password is secret and must never be exposed in frontend code, mobile public config, logs, screenshots, or GitHub. Use a backend proxy/server endpoint for all Geidea API calls that require credentials or signatures.

Direct card APIs can increase PCI scope. Prefer hosted checkout unless the merchant explicitly owns PCI compliance for the custom card flow.

## Callback Or Webhook Contract

Geidea callbacks provide real-time backend transaction/order updates. Use callbacks only after signature validation, amount/currency comparison, reference matching, and response-code checks. Client callbacks such as `onSuccess`, `onError`, `onCancel`, and return URLs are UX events and must not directly fulfill orders.

Geidea callback docs warn that no callback is sent for intermediate authentication failures while the order remains in progress. A final paid callback can include the history of multiple attempts under the same order. The order may remain in progress until it is paid, failed, cancelled, or otherwise finalized.

## Signature Or HMAC

Geidea uses HMAC SHA-256 style signatures converted to Base64 strings, with operation-specific field lists:

- Create Session signature: concatenate `MerchantPublicKey + OrderAmount + OrderCurrency + MerchantReferenceId + timeStamp`; format amount with two decimals; hash with merchant API password; Base64 encode.
- Callback signature: concatenate `MerchantPublicKey + OrderAmount + OrderCurrency + OrderId + Status + MerchantReferenceId + timeStamp`; hash with merchant API password; Base64 encode.
- Refund signature: concatenate `TimeStamp + MerchantPublicKey + RefundAmount + OrderID`; hash with merchant API password; Base64 encode.
- Cancel subscription signatures and other operations have their own documented field lists.

Do not reuse one operation signature for another. Missing, malformed, or mismatched signature means no fulfillment.

## Idempotency Keys

Use local order ID, merchant reference ID, Geidea `orderId`, transaction ID, payment attempt ID, correlation ID, and operation type. Geidea `orderId` must be unique under the merchant profile. Store each callback/event once and transition state idempotently.

## Amount And Currency

Create Session amount is a two-decimal value. Currency is an ISO 4217 alphabetic code; Geidea docs list EGP among supported currencies. Reject callbacks, fetch responses, refund responses, or capture responses whose amount, currency, merchant reference, or order ID does not match the local payment attempt.

## Status Mapping

- Local `paid`: verified callback or fetch response has success response codes and successful detailed response, with amount/currency/reference matching.
- Local `pending`: session/order created, intermediate authentication attempts, or in-progress status.
- Local `failed`: verified failed response codes or detailed response.
- Local `cancelled`: verified user/gateway cancellation or Cancel Order response.
- Local `authorized`: pre-authorization confirmed but not captured.
- Local `captured`: capture response confirms capture.
- Local `refunded` or `partially_refunded`: refund response/event confirms refund state.
- Local `voided`: void confirmed for authorized/uncaptured state where supported.

Authentication success, client callback success, or `onSuccess` data is not enough by itself for backend fulfillment.

## Refunds Voids And Subscriptions

Refunds are for completed paid, captured, or settled transactions and can be full or partial. Refund totals must not exceed the original captured/paid amount. Cancel Order is for initiated orders before Pay API completion. Void is for authorized, uncaptured, unpaid, or unsettled transactions; Geidea transaction-management docs say void availability is region/account dependent and should be confirmed before implementation. Capture completes an authorization and must not exceed the authorized amount. Subscriptions and cancel-subscription flows have separate signature rules.

## Sandbox And Test Notes

Use Geidea test credentials and test cards before production. Test Egypt endpoint configuration, create-session signature, callback signature, amount mismatch, currency mismatch, return URL/client callback without backend callback, multi-attempt order history, refund, cancel before pay, capture, and region-specific void availability.

## Unknowns And Do Not Invent

- Do not assume KSA, UAE, and Egypt endpoints or operation availability are identical.
- Do not implement void for Egypt without confirming current merchant support.
- Do not treat client callback events or return URL parameters as backend payment proof.
- Do not invent signature field lists.
- Do not assume valU/Souhoola are direct API providers when routed through Geidea checkout.
- Fetch the current Geidea `llms.txt` index before endpoint-level or signature work, then keep only Egypt-applicable guidance in this file.

## Agent Checklist

- Confirm regional endpoint is Egypt when the merchant is Egyptian.
- Choose HPP/Checkout unless Direct API PCI scope is intentional.
- Create session server-to-server.
- Generate the operation-specific signature exactly.
- Verify callback signature before processing.
- Require response code and detailed response success for paid fulfillment.
- Compare amount, currency, order ID, and merchant reference.
- Keep duplicate callbacks and multiple attempts idempotent.
- Treat refund, cancel, capture, and void as separate state transitions.

## Fail If

- The agent fulfills from `onSuccess`, return URL, or client callback data alone.
- The agent skips callback signature verification.
- The agent accepts response code mismatch, detailed response mismatch, amount mismatch, or currency mismatch.
- The agent exposes the API password or basic auth material to frontend code.
- The agent treats auth, capture, refund, void, and cancel as interchangeable.
- The agent implements region-specific void/capture behavior without checking current official docs and merchant enablement.
