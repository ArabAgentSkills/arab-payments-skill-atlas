# MyFatoorah

- Provider: MyFatoorah
- Scope: Kuwait / GCC PSP with ExecutePayment, hosted/payment URLs, invoices, webhooks, Get Payment Details, authorization/capture/release, refunds, and recurring where enabled.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-24
- Source confidence: High for official MyFatoorah docs.
- Sources: MyFatoorah get started, ExecutePayment, Webhook v2, Get Payment Details, Updating Payment Status Guidelines, Authorization and Capture, Update Payment.

## Use When

Use for MyFatoorah invoice/payment URL flows, webhook handling, redirection handling, status inquiry, auth/capture, release, and refund status reconciliation.

## Source Map

- Get started: `https://docs.myfatoorah.com/docs/get-started`
- ExecutePayment: `https://docs.myfatoorah.com/docs/execute-payment`
- Webhook v2: `https://docs.myfatoorah.com/docs/webhook-v2`
- Get Payment Details: `https://docs.myfatoorah.com/docs/get-payment-details`
- Status update guidance: `https://docs.myfatoorah.com/docs/v3-updating-payment-status-guidelines`

## Integration Paths

- ExecutePayment creates an invoice/payment URL and returns invoice/payment identifiers.
- Redirection URL returns a PaymentId for inquiry.
- Webhook v2 sends structured event data for payment/refund/capture/release and other events.
- Auth/capture flow is available when enabled.

## Setup Prerequisites

- API token, base country environment, callback/error URLs, webhook URL and secret, payment method id/session id, and auth/capture enablement if needed.
- Localhost callback URLs are not valid for production redirect setup.

## Auth And Secret Boundary

- Keep bearer tokens, webhook secret key, and capture/release credentials server-side.
- Frontend may receive only payment URL and display status derived from backend state.

## Callback Or Webhook Contract

- Webhook v2 includes unique event reference, event type, country ISO code, creation date, and data.
- MyFatoorah recommends using both webhook and Get Payment Details for latest transaction status.
- Redirection should call Get Payment Details, but webhook is more resilient when customers close the browser.

## Signature Or HMAC

- Webhook v2 uses a mandatory webhook secret and the `myfatoorah-signature` header.
- Verify signature before processing event data.
- If signature verification details are not available in local context, load the official signature page or merchant docs before code.

## Idempotency Keys

- Use webhook `Event.Reference`, invoice id/reference, transaction id, and PaymentId.
- A successful payment status should override weaker duplicate events, and success must not be overwritten by later non-final signals.

## Amount And Currency

- Compare invoice value, display/pay/base currency, and local order reference.
- If using invoice items, ensure the total matches `InvoiceValue`.

## Status Mapping

- Invoice `PAID` with transaction `SUCCESS` maps to paid after signature/inquiry confirmation.
- `PENDING`, `FAILED`, `INPROGRESS`, `AUTHORIZE`, and `CANCELED` require distinct local states.
- `AUTHORIZE` is not captured settlement unless capture is completed.

## Refunds Voids And Subscriptions

- Auth/capture flow uses Update Payment with `CAPTURE` or `RELEASE`; only one capture or release operation is allowed per invoice per current docs.
- Refund webhooks and refund APIs require separate local operation records.
- Recurring payments require explicit docs and merchant enablement.

## Sandbox And Test Notes

- Use MyFatoorah test token/environment and country-specific base URL.
- Test redirection-before-webhook and webhook-before-redirection sequences.

## Unknowns And Do Not Invent

- Do not invent PaymentMethodId, status enum, signature formula, country URL, or recurring semantics.
- Confirm current v2/v3 endpoint version before implementation.

## Agent Checklist

- Store InvoiceId/PaymentId and local order reference.
- Verify webhook signature.
- Use Get Payment Details as fallback/confirmation.
- Compare amount/currency/reference.
- Keep success final and idempotent.

## Fail If

- You mark paid only because the customer returned to CallBackUrl.
- You skip `myfatoorah-signature` verification.
- You treat `AUTHORIZE` as captured.
- You ignore duplicate webhook behavior.
