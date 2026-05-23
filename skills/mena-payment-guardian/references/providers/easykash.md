# EasyKash

- Provider: EasyKash
- Scope: Egypt PSP with Direct Payment Hosted, Pay API, callback service, HMAC verification, payment inquiry, and Cash API.
- Priority: P2
- Readiness: A
- Public docs status: public-gitbook
- Last checked: 2026-05-24
- Source confidence: High for public EasyKash GitBook.
- Sources: EasyKash API docs, Pay API, callback service, callback response verification, payment inquiry, Cash API.

## Use When

Use for EasyKash hosted direct payment, redirect UX, callback HMAC verification, inquiry fallback, cash collection API, and Egypt payment flows.

## Source Map

- Docs: `https://easykash.gitbook.io/easykash-apis-documentation/`
- Pay API: `https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/pay-api`
- Callback service: `https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service`
- Callback verification: `https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/callback-service/callback-response-verification`
- Inquiry: `https://easykash.gitbook.io/easykash-apis-documentation/direct-payment-hosted/payment-inquiry`

## Integration Paths

- Direct Payment Hosted Pay API creates a payment and sends the customer through hosted payment UX.
- Callback service sends payment result to merchant backend.
- Payment inquiry is the fallback/confirmation path.
- Cash API is separate from card/hosted payment flow.

## Setup Prerequisites

- Merchant credentials, secret/HMAC configuration, callback URL, sandbox/live base URLs, payment method enablement, and local order reference storage.

## Auth And Secret Boundary

- Keep merchant credentials and HMAC secret server-side.
- Frontend should receive only a hosted payment URL or safe payment reference.

## Callback Or Webhook Contract

- Redirect status is UX only and can show success, pending, or failed before backend reconciliation.
- Use verified callback or payment inquiry before fulfillment.
- Store EasyKash payment id/reference, local order id, amount, callback status, and inquiry status.

## Signature Or HMAC

- Callback verification uses HMAC SHA-512 per EasyKash docs.
- Verify HMAC before trusting status.
- Use inquiry if callback is missing, delayed, or cannot be verified.

## Idempotency Keys

- Use local order id plus EasyKash payment reference.
- Deduplicate callback and inquiry responses by provider payment reference and final state.

## Amount And Currency

- Compare amount and expected Egypt currency before marking paid.
- Do not assume redirect status means the amount settled.

## Status Mapping

- Verified successful callback or successful inquiry maps to paid.
- Pending remains pending until verified final status.
- Failed/cancelled remains non-fulfillment unless inquiry later confirms paid.

## Refunds Voids And Subscriptions

- Use only documented EasyKash APIs for cash/payment follow-up and any reversal behavior.
- No subscription behavior should be invented from hosted payment docs.

## Sandbox And Test Notes

- Test redirect success/pending/failed against callback and inquiry.
- Test invalid HMAC and duplicate callback.

## Unknowns And Do Not Invent

- Do not invent status values, refund APIs, or callback fields beyond public GitBook or merchant docs.
- If GitBook hash changes, manually inspect before changing guidance.

## Agent Checklist

- Create payment server-side.
- Show redirect result as processing until backend verifies.
- Verify callback HMAC SHA-512.
- Use inquiry fallback.
- Compare amount/reference.

## Fail If

- You fulfill from redirect result alone.
- You skip HMAC verification.
- You ignore inquiry fallback.
- Duplicate callback creates duplicate fulfillment.
