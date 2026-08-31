# Tabby

- Provider: Tabby
- Scope: UAE / Saudi Arabia BNPL with checkout sessions, payment verification, webhooks, capture, close, refund, idempotent reference ids, and payment status inquiry.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-08-31
- Source confidence: High for official Tabby docs.
- Sources: Tabby introduction, create session, checkout flow, payment processing, payment statuses, payment webhooks, dispute webhooks, retrieve payment, and official Tabby `llms.txt` index.

## Use When

Use for Tabby Pay in 4/custom integration, hosted checkout, BNPL authorization/capture lifecycle, webhook handling, retrieve payment, close, and refunds.

## Source Map

- What is Tabby: `https://docs.tabby.ai/introduction/what-is-tabby`
- Create checkout session: `https://docs.tabby.ai/api-reference/checkout/create-a-session`
- Checkout flow: `https://docs.tabby.ai/pay-in-4-custom-integration/checkout-flow`
- Payment processing: `https://docs.tabby.ai/pay-in-4-custom-integration/payment-processing`
- Payment webhooks: `https://docs.tabby.ai/pay-in-4-custom-integration/webhooks`
- Dispute webhooks: `https://docs.tabby.ai/pay-in-4-custom-integration/dispute-webhooks`
- Retrieve payment: `https://docs.tabby.ai/api-reference/payments/retrieve-a-payment`
- Agent-readable docs: `https://docs.tabby.ai/llms.txt`

## Integration Paths

- Create checkout session server-side and redirect customer to the Tabby checkout URL from `configuration.available_products.installments[0].web_url`.
- Use eligibility/background pre-scoring only as a pre-check; the order session created at place-order time still needs the full checkout payload.
- Use retrieve payment and payment webhooks to verify status after redirect.
- Capture authorized payments from OMS/backend.
- Close/cancel and refund through documented APIs.
- Keep dispute notifications separate from payment fulfillment events.

## Setup Prerequisites

- Secret key, merchant code, merchant URLs, current country/currency support, payment webhook registration, dispute webhook opt-in status, auth header/IP allowlist strategy, and sandbox/live separation.
- Current public docs list UAE/AED and Saudi Arabia/SAR for the custom integration pages reviewed on 2026-08-31; do not assume Kuwait/KWD support without current merchant-specific confirmation.
- Confirm auto-capture settings with Tabby if the merchant account behavior differs from custom integration docs.

## Auth And Secret Boundary

- Secret key and webhook auth header are server-side only.
- Frontend receives checkout URL and safe payment/session ids only.

## Callback Or Webhook Contract

- Payment webhooks are notifications; Tabby docs instruct merchants to verify status by retrieving payment with `payment_id`.
- Webhook delivery order is not guaranteed; duplicate webhook notifications must be ignored after first processing.
- Webhook registration is per merchant code and current docs show `X-Merchant-Code` as a required registration header.
- The webhook can arrive before the local order is saved; persist incoming verified events and reconcile once the order exists.
- Treat a webhook with an already populated captures array as capture confirmation, not a new command to capture again.
- Dispute webhooks are separate opt-in notifications for dispute lifecycle changes; route them to dispute handling and do not treat them as payment authorization, capture, refund, or fulfillment events.
- Store payment id, checkout/session id, order reference, status, captures, refunds, and webhook receipt data.

## Signature Or HMAC

- Public docs describe webhook protection options including a merchant-configured static auth header and status verification via retrieve payment.
- Verify the configured auth header/IP policy and then call retrieve payment before fulfillment/capture.

## Idempotency Keys

- Tabby supports idempotent capture/refund requests using `reference_id`.
- Use local order id and operation id as `reference_id` for safe retries.
- Derive capture/refund `reference_id` values from stable order and operation identifiers, not timestamps.
- When both a success redirect handler and an authorized webhook handler can capture, use a local capture-in-progress guard and the same provider `reference_id` so only one path wins.

## Amount And Currency

- Compare payment amount, capture amount, refund amount, currency, and order reference.
- Current public docs list AED and SAR on the reviewed custom integration pages; reject or pause KWD/Kuwait assumptions until the merchant account or current Tabby docs prove support.
- Capture request amount should match the verified payment amount unless partial capture is explicitly intended and documented.

## Status Mapping

- `AUTHORIZED` means Tabby approved/authorized payment, but merchant capture is still required for successful order completion unless account settings prove otherwise.
- `CLOSED` after capture indicates completion/confirmation in Tabby flow.
- `CREATED`, `AUTHORIZED`, `CLOSED`, `REJECTED`, `EXPIRED`, and refund/capture arrays must be mapped carefully. Normalize local casing if needed, but do not invent extra status values.

## Refunds Voids And Subscriptions

- Capture can only be performed from authorized status; capture against created/expired/closed/rejected should fail.
- Close cancels an uncaptured payment.
- Refunds apply to captured/closed payments and cannot exceed captured amount.
- Current public docs state refunds can be initiated within 180 days from payment creation; confirm account-specific exceptions before hard-coding a longer or shorter window.
- No subscription behavior should be invented.

## Sandbox And Test Notes

- Test payment webhooks out of order, duplicate webhook, redirect missing, authorization without capture, capture retry with same `reference_id`, close, refund within and outside the documented refund window, and dispute webhook routing.

## Unknowns And Do Not Invent

- Do not invent merchant_code, country support, auto-capture behavior, webhook auth header value, dispute webhook enablement, refund-window exceptions, or payment status transitions.
- If account-specific settings differ, ask for merchant docs or Tabby integration manager confirmation.
- Fetch the current Tabby `llms.txt` index before endpoint-level checkout, status, capture, or webhook work.

## Agent Checklist

- Create session server-side.
- Store payment id.
- Treat payment webhook as notification.
- Register webhooks for the correct `merchant_code` and verify the configured static auth header.
- Keep dispute webhook handling separate.
- Retrieve payment before fulfillment/capture.
- Use stable `reference_id` idempotency and a local capture-in-progress guard for capture/refund.
- Separate authorization, capture, close, and refund.

## Fail If

- You ship after Tabby redirect alone.
- You treat authorization as captured settlement.
- You skip retrieve payment after webhook.
- You retry capture/refund without idempotency.
- You assume Kuwait/KWD support from older docs without current merchant confirmation.
- You capture from both redirect and webhook paths with different `reference_id` values.
- You treat dispute webhook delivery as payment success or refund confirmation.
