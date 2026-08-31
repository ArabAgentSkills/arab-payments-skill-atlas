# HyperPay

- Provider: HyperPay
- Scope: Saudi Arabia / MENA PSP with COPYandPAY widget, Server-to-Server APIs, mobile SDKs, transaction status queries, back-office operations, and encrypted webhooks.
- Priority: P0
- Readiness: A
- Public docs status: public-tls-manual-verify
- Last checked: 2026-08-31
- Source confidence: High for HyperPay/OPPWA docs; endpoint host and entity IDs are account/environment-specific. Simple Python checks may report manual TLS verification for OPPWA pages. No public `llms.txt` endpoint was available during review. The older public webhook tutorial route returned HTTP 500 during this review, so the source map now uses the official HyperPay Webhooks FAQ plus API notification parameters.
- Sources: HyperPay integration guide, COPYandPAY widget, Server-to-Server guide, Webhooks FAQ, result codes, API parameters.

## Use When

Use for HyperPay COPYandPAY, direct Server-to-Server card flows, transaction status query, webhook notifications, refunds, captures, and back-office operations.

## Source Map

- Integration guide: `https://www.hyperpay.com/integration-guide/`
- COPYandPAY: `https://hyperpay.docs.oppwa.com/integrations/widget`
- Server-to-Server: `https://hyperpay.docs.oppwa.com/integrations/server-to-server`
- Webhooks FAQ: `https://hyperpay.docs.oppwa.com/support/webhooks`
- Webhook notification parameters: `https://hyperpay.docs.oppwa.com/reference/parameters#notifications`
- Result codes: `https://hyperpay.docs.oppwa.com/reference/resultCodes`
- Agent-readable docs: none found; use official HyperPay/OPPWA docs and transaction status query pages directly.

## Integration Paths

- COPYandPAY prepares checkout server-to-server, renders payment widget, then redirects with `resourcePath`.
- Server-to-Server supports pre-authorization, capture, debit, asynchronous redirect, and back-office operations.
- Mobile SDKs follow similar server preparation and status verification patterns.

## Setup Prerequisites

- Entity id, auth credentials, test/live base URL, webhook configuration, TLS/certificate compatibility, and payment brand enablement.
- Server-to-Server card collection increases PCI scope; use COPYandPAY when possible.

## Auth And Secret Boundary

- Keep bearer/auth credentials and entity ids requiring secrecy server-side.
- Widget checkout id may be used by frontend only after server-side preparation.

## Callback Or Webhook Contract

- COPYandPAY redirect includes `resourcePath`; the server must call `baseUrl + resourcePath` with auth to get status.
- Webhooks are asynchronous, can be delayed, retried, out of order, and may produce multiple final messages.
- HyperPay webhooks can be encrypted; configured secret is used for AES-GCM decryption with IV/auth tag headers.

## Signature Or HMAC

- For encrypted webhooks, decrypt and authenticate using the configured 64-character hex secret and documented headers before trusting payload.
- If real-time fulfillment/capture is needed, use the Transaction Status query API rather than relying solely on asynchronous webhook timing.

## Idempotency Keys

- Use checkout id, payment id, transaction id, `ndc`, and merchant reference/custom parameters.
- Deduplicate by payment id plus result/status and guard against out-of-order final messages.

## Amount And Currency

- Compare returned `amount`, `currency`, presentation amount/currency, and merchant reference/custom order fields.
- Reject fulfillment when status is successful but amount/currency does not match local order.

## Status Mapping

- Use official result code patterns and transaction status query response.
- Successful result codes map to paid/captured only after amount/currency/reference checks.
- Current result-code docs include `000.000.001` as succeeded but partially approved. Treat it as success-like only for the provider-approved amount; do not fulfill a full-order obligation unless the approved amount, local order policy, and merchant reconciliation support that state.
- Pending/async statuses remain pending; rejected/failed codes remain non-fulfillment.

## Refunds Voids And Subscriptions

- Server-to-Server/back-office operations include capture, refund, rebill, chargeback, and reversal-related flows depending on transaction type.
- Pre-authorization and debit flows have different operation sequences.
- Subscriptions and tokenization require separate docs and explicit merchant enablement.

## Sandbox And Test Notes

- Use test base URL and HyperPay regression testing docs.
- Test checkout id reuse/refresh because a checkout id can produce multiple transaction attempts before finalization.

## Unknowns And Do Not Invent

- Do not invent entity ids, base URLs, result-code regexes, webhook secret, or payment brand support.
- Ask for merchant docs when account-specific connector behavior changes result codes or operation availability.
- Re-check official HyperPay/OPPWA pages manually when endpoint-level details are needed because no public `llms.txt` manifest was available.

## Agent Checklist

- Prepare checkout server-side.
- Verify status via `resourcePath` or transaction status API.
- Decrypt/verify webhooks before use.
- Compare amount, currency, brand, type, and references.
- Handle partial-approval success codes without over-fulfilling the order.
- Deduplicate out-of-order events.

## Fail If

- You fulfill only because shopper reached `shopperResultUrl`.
- You skip transaction status query after redirect.
- You ignore encrypted webhook authentication.
- You treat a partially approved success code as full payment without checking amount and order policy.
- You treat multiple final webhook messages as separate fulfillments.
