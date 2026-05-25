# Tamara

- Provider: Tamara
- Scope: Saudi Arabia / GCC BNPL with online checkout sessions, webhook registration, approved-to-authorised acknowledgment, capture, cancel, simplified refund, and order status inquiry.
- Priority: P0
- Readiness: A
- Public docs status: public
- Last checked: 2026-05-25
- Source confidence: High for official Tamara docs.
- Sources: Tamara docs home, online checkout, webhook registration and order authorisation, order status flow, capture order, simplified refund, get order details.

## Use When

Use for Tamara online checkout, BNPL approval/authorisation/capture lifecycle, webhook registration, capture, cancel, refund, and order status inquiry.

## Source Map

- Docs: `https://docs.tamara.co/`
- Online checkout: `https://docs.tamara.co/docs/direct-online-checkout`
- Webhook/order authorisation: `https://docs.tamara.co/docs/transaction-authorisation`
- Status flow: `https://docs.tamara.co/docs/online-order-status-flow`
- Capture: `https://docs.tamara.co/reference/captureorder`
- Get order details: `https://docs.tamara.co/reference/getorderdetails`

## Integration Paths

- Create checkout session server-side, redirect to Tamara checkout URL, receive approved notification, call Authorise Order unless documented auto-authorisation is explicitly enabled for the merchant, then capture when shipped/fulfilled.
- Cancel is available before capture in the authorized stage.
- Simplified refund applies after capture.

## Setup Prerequisites

- API bearer credential, sandbox/live environment, webhook URL in Partner Portal or API, checkout URLs, country/currency support, and order reference strategy.
- Webhook approved event is mandatory for the documented flow unless merchant-specific auto-authorisation has been confirmed in current docs/account settings.

## Auth And Secret Boundary

- Keep bearer credentials and webhook validation tokens server-side.
- Frontend receives checkout URL and safe order ids only.

## Callback Or Webhook Contract

- Tamara sends notifications to the merchant webhook URL; an approved notification must be acknowledged by calling Authorise Order unless documented auto-authorisation is explicitly enabled.
- Docs note server-to-server notification helps avoid frontend redirection failures.
- Store Tamara order id, checkout id, order reference, notification event, authorised state, capture state, and refund ids.

## Signature Or HMAC

- Tamara webhook registration/authorization flow includes `tamaraToken` query parameter and bearer authorization behavior in docs.
- Validate the webhook token/header according to current docs before calling Authorise Order or changing local state.

## Idempotency Keys

- Use merchant `order_reference_id`, Tamara `order_id`, capture id/reference, and refund id.
- Authorise/capture/refund should be stored as idempotent local operations so retries do not duplicate state.

## Amount And Currency

- Compare checkout total, item totals, capture amount, refund amount, country, and currency.
- Do not capture or refund amounts inconsistent with local fulfillment/refund records.

## Status Mapping

- `approved` is not enough; merchant must authorise, which moves order to `authorised`, unless confirmed auto-authorisation moves the order through the documented states automatically.
- Capture moves toward `partially_captured` or `fully_captured`.
- Cancel is valid only from the authorized stage; refunds apply after capture.
- Declined and expired orders are non-fulfillment states. Docs note orders left at `approved` indicate a sync issue and should be authorised, cancelled, or captured according to the intended flow.

## Refunds Voids And Subscriptions

- Cancel is for authorized but not captured orders.
- Capture is required for settlement; non-captured orders are not settled and may be auto-captured after the documented window when that behavior applies.
- Simplified refund can be full or partial after capture, with refund ids stored locally.
- No subscription behavior should be invented.

## Sandbox And Test Notes

- Test missing frontend redirect, approved webhook, authorise call, capture, cancel-before-capture, refund-after-capture, and Get Order Details fallback.

## Unknowns And Do Not Invent

- Do not invent webhook token validation, auto-authorisation enablement, status names, country/currency availability, capture windows, or refund limits beyond current docs.
- Ask for merchant docs when integrating through a PSP wrapper instead of direct Tamara.

## Agent Checklist

- Create checkout session server-side.
- Verify webhook token/header.
- Call Authorise Order after approved notification unless confirmed auto-authorisation applies.
- Capture only after fulfillment/shipment decision.
- Use Get Order Details fallback.
- Separate cancel from refund.

## Fail If

- You treat approved redirect as final paid.
- You skip Authorise Order without confirmed auto-authorisation.
- You capture before authorization.
- You cancel after capture instead of refunding.
