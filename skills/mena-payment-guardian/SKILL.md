---
name: mena-payment-guardian
description: Use when building or reviewing Arab/MENA payment or BNPL flows, including Paymob, FawryPay, Geidea, PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, EasyKash, Kashier, PaySky, Tabby, Tamara, valU, Souhoola, webhooks, signatures, redirects, captures, refunds, or payment secret boundaries.
---

# MENA Payment Guardian

## Mission

Use this skill for Arab/MENA payment and BNPL integrations where redirects, webhook delivery, signature validation, capture timing, local currencies, and duplicate events can break production. Provider references are source-linked field notes; official provider docs and merchant agreements remain the authority for endpoint-level details.

## Decision Path

Always follow this order:

1. Identify the provider, country, integration path, payment method, and environment.
2. Load the matching provider reference and shared pattern.
3. Confirm the server boundary and list secret env var names only.
4. Verify the authenticity signal: HMAC, signature, SecureHash, webhook secret, encrypted webhook payload, static auth header, or documented server-side inquiry.
5. Compare order reference, provider reference, amount, currency, country/account context, and status.
6. Store provider events and provider transaction references idempotently before fulfillment.
7. Fulfill only from verified server-side state.
8. Add tests or manual QA for duplicate events, invalid signatures, delayed callbacks, stale failures, capture/refund/void misuse, and frontend secret exposure.

## Non-Negotiables

- Treat all money movement as high risk.
- Never fulfill from a browser redirect, hosted checkout result, SDK callback, BNPL approval page, or frontend-only status alone.
- Verify provider signatures, HMACs, SecureHash values, webhook secrets, encrypted payloads, or documented server-side inquiry exactly as documented.
- Keep merchant credentials, HMAC secrets, server keys, secret API keys, access codes, terminal secrets, SHA phrases, and service role keys server-side only.
- Compare provider amount, currency, country/account context, local order reference, and provider transaction/reference before creating paid state.
- Make callbacks, webhooks, retries, inquiry responses, capture calls, refunds, voids, and page refreshes idempotent.
- Store provider event/reference uniqueness before activating subscriptions, enrollments, bookings, credits, shipments, or invoices.
- Do not overwrite a stronger final paid/captured state with older pending, failed, cancelled, expired, rejected, or duplicate signals.
- Log safe identifiers only: local order id, provider reference, status, event id, timestamp. Never log tokens, card data, signatures, HMAC secrets, API keys, access codes, SHA phrases, or raw credentials.

## Required Audit

Before implementing or reviewing payment code, identify:

1. Provider, country/account, integration path, and payment method.
2. Sandbox/test vs live environment and any country-specific endpoint.
3. Amount unit and currency rules.
4. Server endpoint receiving callbacks, webhooks, IPNs, or notification feedback.
5. Signature/HMAC/SecureHash/encryption/webhook-secret method and raw-body requirements.
6. Unique payment, order, event, authorization, capture, refund, and provider reference fields.
7. Status mapping for created, authorized, paid, captured, failed, cancelled, expired, rejected, refunded, voided, released, abandoned, duplicate, and pending.
8. Ordering behavior when webhook arrives before or after client redirect.
9. What happens on duplicate webhook, retry, refresh, refund, void, capture failure, missing user, missing order, or provider outage.
10. Env var names by name only, never values.

## Provider References

Load only the provider file needed for the task:

- Paymob: `references/providers/paymob.md`
- FawryPay: `references/providers/fawrypay.md`
- Geidea: `references/providers/geidea.md`
- PayTabs: `references/providers/paytabs.md`
- Tap Payments: `references/providers/tap-payments.md`
- MyFatoorah: `references/providers/myfatoorah.md`
- HyperPay: `references/providers/hyperpay.md`
- Moyasar: `references/providers/moyasar.md`
- Amazon Payment Services: `references/providers/amazon-payment-services.md`
- EasyKash: `references/providers/easykash.md`
- Kashier: `references/providers/kashier.md`
- PaySky: `references/providers/paysky.md`
- Tabby: `references/providers/tabby.md`
- Tamara: `references/providers/tamara.md`
- valU and Souhoola through PSPs: `references/providers/valu-souhoola.md`

Use `references/provider-index.json` to check source URLs, coverage depth, readiness, public/gated status, and last verification dates.

## Shared Patterns

Load these when the implementation touches the matching risk:

- Fulfillment flow: `references/patterns/webhook-first-fulfillment.md`
- Idempotency and state transitions: `references/patterns/idempotency-state-transitions.md`
- Secret and server boundary: `references/patterns/server-secret-boundary.md`
- Capture, void, refund, and BNPL lifecycle: `references/patterns/capture-refund-void-lifecycle.md`
- Private docs policy: `references/patterns/private-docs-policy.md`

## Implementation Bias

- Prefer server-confirmed activation. Redirect pages should show `processing` unless server state is already paid/captured.
- Use a payment transaction table plus a payment event table or equivalent durable records.
- Enforce unique constraints on provider event ids, provider payment ids, provider transaction references, capture/refund ids, and merchant order references.
- For BNPL, separate approval/authorization from capture/settlement. Do not ship or grant final value until the provider state and merchant lifecycle step support it.
- For Supabase, privileged payment writes belong in Edge Functions or server routes with service role isolated from browser code.
- If official docs are unavailable, gated, partial, or country-specific, state that and ask for current merchant docs. Do not invent endpoints, status names, headers, signatures, test cards, local payment methods, or capture windows.
- For providers with full-depth coverage, use the provider file as a checklist and still link to official docs for endpoint-level details.
- For conservative coverage, stop before custom endpoint work unless official merchant docs are provided.

## Required Output

When answering a payment implementation or review request, return:

1. Current payment architecture.
2. Provider contract, country scope, and source confidence.
3. Server boundary and secret handling.
4. Idempotency strategy.
5. Risk points and safe fix plan.
6. Test matrix including duplicate events, invalid signature, amount/currency/country mismatch, callback-before-redirect, redirect-before-callback, capture/refund/void misuse, and stale state.
7. Remaining unknowns and deployment/rollback notes.
