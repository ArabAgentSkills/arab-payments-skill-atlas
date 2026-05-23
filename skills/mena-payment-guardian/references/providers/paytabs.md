# PayTabs

- Provider: PayTabs
- Scope: Saudi Arabia / UAE / MENA PSP with hosted payment pages, invoices, PayLinks, managed forms, own forms, mobile SDKs, backend packages, callbacks, and IPN.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-24
- Source confidence: High for official PayTabs technical portal and support docs.
- Sources: PayTabs technical portal, hosted payment initiating payment, callback URL, IPN, signature verification, return URL, cart id, cart amount, cart currency.

## Use When

Use for PayTabs payment pages, managed forms, PayLinks/invoices, callback/IPN handling, return URL verification, and server-key signature validation.

## Source Map

- Portal: `https://docs.paytabs.com/`
- Hosted payment request: `https://support.paytabs.com/en/support/solutions/articles/60000992876-3-2-1-hosted-payment-page-apis-initiating-the-payment`
- Callback URL: `https://support.paytabs.com/en/support/solutions/articles/60000805341`
- IPN: `https://support.paytabs.com/en/support/solutions/articles/60000710069`
- Signature verification: `https://support.paytabs.com/en/support/solutions/articles/60000718961`

## Integration Paths

- Hosted Payment Page, Managed Form, Own Form, invoices, PayLinks, mobile SDKs, plugins, and backend packages.
- Request parameters include merchant profile, transaction type/class, cart id, cart amount, cart currency, cart description, callback, and return depending on path.

## Setup Prerequisites

- Merchant profile id, server key, endpoint region, callback/IPN URL, return URL, enabled payment methods, and sandbox/live profile separation.
- Confirm the exact integration type because response handling differs between callback/IPN and return URL.

## Auth And Secret Boundary

- Keep server key and profile credentials server-side.
- Frontend may display PayTabs redirect URL or hosted widget only after the server creates the payment request.

## Callback Or Webhook Contract

- PayTabs callback is a server-to-server POST to a pre-defined HTTPS URL and is not dependent on the customer completing the redirect.
- IPN is also server-to-server and can be configured account-side for selected events.
- Return URL is customer-browser dependent and must not be used as the only fulfillment signal.

## Signature Or HMAC

- Callback/IPN verification: calculate HMAC SHA-256 over the whole raw payload using the profile server key and compare with the `Signature` header.
- Return URL verification: remove `signature`, drop empty fields, sort keys, URL-encode, calculate HMAC SHA-256 using server key, and compare to the returned signature.
- Do not mix return verification with callback/IPN raw-body verification.

## Idempotency Keys

- Use `cart_id` for merchant order reference and `tran_ref` for PayTabs transaction reference.
- Deduplicate callback/IPN by transaction reference and response status.

## Amount And Currency

- `cart_amount` is decimal and `cart_currency` is a 3-letter supported currency.
- Compare returned/requested `cart_id`, amount, and currency before paid state.

## Status Mapping

- Response status/code/message fields identify authorization/payment outcome.
- Treat authorized/success-like statuses as paid only after signature validation and amount/currency/reference match.
- Failed, error, cancelled, or incomplete statuses must not fulfill.

## Refunds Voids And Subscriptions

- Use documented PayTabs transaction/back-office APIs or merchant portal operations for refund/void/capture.
- Keep each operation idempotent and tied to the original `tran_ref`.
- Recurring/token flows require explicit merchant enablement and documented token handling.

## Sandbox And Test Notes

- Use the matching regional secure endpoint and test profile.
- Test callback/IPN raw body handling because parsing body before HMAC can break verification.

## Unknowns And Do Not Invent

- Do not invent regional endpoints, response status meanings, or APM-specific parameters.
- Ask for merchant docs when PayLinks, invoices, or dashboard-created transactions require default signature key behavior.

## Agent Checklist

- Create payment server-side with profile/server key.
- Store `cart_id` and `tran_ref`.
- Verify callback/IPN `Signature` header from raw body.
- Treat return URL as UX only.
- Compare amount/currency/reference.

## Fail If

- You fulfill from return URL alone.
- You verify callback/IPN after mutating the raw body.
- You expose server key to frontend.
- You ignore cart amount or currency.
