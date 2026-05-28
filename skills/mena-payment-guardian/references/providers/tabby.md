# Tabby

- Provider: Tabby
- Scope: UAE / Saudi Arabia / MENA BNPL with checkout sessions, payment verification, webhooks, capture, close, refund, idempotent reference ids, and payment status inquiry.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-29
- Source confidence: High for official Tabby docs.
- Sources: Tabby introduction, create session, checkout flow, payment processing, payment statuses, webhooks, retrieve payment, and official Tabby `llms.txt` index.

## Use When

Use for Tabby Pay in 4/custom integration, hosted checkout, BNPL authorization/capture lifecycle, webhook handling, retrieve payment, close, and refunds.

## Source Map

- What is Tabby: `https://docs.tabby.ai/introduction/what-is-tabby`
- Create checkout session: `https://docs.tabby.ai/api-reference/checkout/create-a-session`
- Checkout flow: `https://docs.tabby.ai/pay-in-4-custom-integration/checkout-flow`
- Payment processing: `https://docs.tabby.ai/pay-in-4-custom-integration/payment-processing`
- Webhooks: `https://docs.tabby.ai/pay-in-4-custom-integration/webhooks`
- Retrieve payment: `https://docs.tabby.ai/api-reference/payments/retrieve-a-payment`
- Agent-readable docs: `https://docs.tabby.ai/llms.txt`

## Integration Paths

- Create checkout session server-side and redirect customer to Tabby checkout URL.
- Use retrieve payment and webhooks to verify status after redirect.
- Capture authorized payments from OMS/backend.
- Close/cancel and refund through documented APIs.

## Setup Prerequisites

- Secret key, merchant code, merchant URLs, country/currency support, webhook registration, auth header/IP allowlist strategy, and sandbox/live separation.
- Confirm auto-capture settings with Tabby if the merchant account behavior differs from custom integration docs.

## Auth And Secret Boundary

- Secret key and webhook auth header are server-side only.
- Frontend receives checkout URL and safe payment/session ids only.

## Callback Or Webhook Contract

- Webhooks are notifications; Tabby docs instruct merchants to verify status by retrieving payment with `payment_id`.
- Webhook delivery order is not guaranteed; duplicate webhook notifications must be ignored after first processing.
- Store payment id, checkout/session id, order reference, status, captures, refunds, and webhook receipt data.

## Signature Or HMAC

- Public docs describe webhook protection options including static auth header and status verification via retrieve payment.
- Verify the configured auth header/IP policy and then call retrieve payment before fulfillment/capture.

## Idempotency Keys

- Tabby supports idempotent capture/refund requests using `reference_id`.
- Use local order id and operation id as `reference_id` for safe retries.

## Amount And Currency

- Compare payment amount, capture amount, refund amount, currency, and order reference.
- Capture request amount should match the verified payment amount unless partial capture is explicitly intended and documented.

## Status Mapping

- `authorized` means Tabby approved/authorized payment, but merchant capture is still required for successful order completion.
- `closed` after capture indicates completion/confirmation in Tabby flow.
- `created`, `expired`, `closed`, `rejected`, and refund/capture arrays must be mapped carefully.

## Refunds Voids And Subscriptions

- Capture can only be performed from authorized status; capture against created/expired/closed/rejected should fail.
- Close cancels an uncaptured payment.
- Refunds apply to captured/closed payments and cannot exceed captured amount.
- No subscription behavior should be invented.

## Sandbox And Test Notes

- Test webhooks out of order, duplicate webhook, redirect missing, authorization without capture, capture retry with same `reference_id`, close, and refund.

## Unknowns And Do Not Invent

- Do not invent merchant_code, country support, auto-capture behavior, webhook auth header value, or payment status transitions.
- If account-specific settings differ, ask for merchant docs or Tabby integration manager confirmation.
- Fetch the current Tabby `llms.txt` index before endpoint-level checkout, status, capture, or webhook work.

## Agent Checklist

- Create session server-side.
- Store payment id.
- Treat webhook as notification.
- Retrieve payment before fulfillment/capture.
- Use `reference_id` idempotency for capture/refund.
- Separate authorization, capture, close, and refund.

## Fail If

- You ship after Tabby redirect alone.
- You treat authorization as captured settlement.
- You skip retrieve payment after webhook.
- You retry capture/refund without idempotency.
