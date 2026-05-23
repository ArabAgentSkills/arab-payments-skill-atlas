---
name: egypt-payment-guardian
description: Use when building or reviewing Egypt payment flows, including Paymob, FawryPay, Geidea Egypt, EasyKash, Kashier, PaySky, valU, Souhoola, callbacks, webhooks, HMAC, redirects, refunds, pending payments, duplicate events, or payment secret boundaries.
---

# Egypt Payment Guardian

## Mission

Use this skill for Egypt payment integrations where provider redirects, callbacks, signatures, currency handling, and duplicate events can break production. Treat the provider reference files as source-linked field notes, not a replacement for official docs.

## Decision Path

Always follow this order:

1. Identify the provider, integration path, environment, and payment method.
2. Load the provider reference and any shared pattern that matches the risk.
3. Confirm the server boundary and list secret env var names only.
4. Verify the provider authenticity signal: HMAC, signature, SecureHash, webhook signature, or documented server-side inquiry.
5. Compare local order reference, provider reference, amount, currency, and status fields.
6. Store the provider event/reference idempotently before fulfillment.
7. Fulfill only from verified server-side state.
8. Add tests or manual QA for duplicate events, invalid signatures, delayed callbacks, and stale state.

## Non-Negotiables

- Treat all money movement as high risk.
- Never fulfill from a browser redirect, hosted checkout result, SDK callback, or frontend-only status alone.
- Verify provider signatures, HMACs, or secure hashes exactly as documented.
- Keep merchant credentials, HMAC secrets, secret keys, and service role keys server-side only.
- Compare provider amount, currency, order reference, and transaction reference before creating paid state.
- Make callbacks, webhooks, retries, inquiry responses, and page refreshes idempotent.
- Store provider event/reference uniqueness before activating subscriptions, enrollments, bookings, credits, or invoices.
- Log safe identifiers only: order id, provider reference, status, timestamp. Never log tokens, card data, signatures, HMAC secrets, or raw credentials.

## Required Audit

Before implementing or reviewing payment code, identify:

1. Provider and integration path.
2. Sandbox/test vs live environment.
3. Amount unit and currency rules.
4. Server endpoint receiving callbacks or webhooks.
5. Signature/HMAC/SecureHash method and raw-body requirements.
6. Unique payment, order, event, and provider reference fields.
7. Status mapping for pending, paid, failed, cancelled, expired, refunded, voided, and duplicate.
8. Ordering behavior when callback/webhook arrives before or after client redirect.
9. What happens on duplicate callback, retry, refresh, refund, void, missing user, or missing order.
10. Env var names by name only, never values.

## Provider References

Load only the provider file needed for the task:

- Paymob: `references/providers/paymob.md`
- FawryPay: `references/providers/fawrypay.md`
- Geidea Egypt: `references/providers/geidea-egypt.md`
- EasyKash: `references/providers/easykash.md`
- Kashier: `references/providers/kashier.md`
- PaySky: `references/providers/paysky.md`
- valU and Souhoola through PSPs: `references/providers/egypt-bnpl-methods.md`

Use `references/provider-index.json` to check source URLs, readiness, public/gated status, and last verification dates.

## Shared Patterns

Load these when the implementation touches the matching risk:

- Fulfillment flow: `references/patterns/webhook-first-fulfillment.md`
- Idempotency and state transitions: `references/patterns/idempotency-state-transitions.md`
- Secret and server boundary: `references/patterns/server-secret-boundary.md`
- Private docs policy: `references/patterns/private-docs-policy.md`

## Implementation Bias

- Prefer server-confirmed activation. Redirect pages should show `processing` unless server state is already paid.
- Use a payment transaction table plus a payment event table or equivalent durable records.
- Enforce unique constraints on provider transaction/event references and merchant order references.
- Never overwrite `paid` with `pending`, `failed`, or `cancelled` from an older or weaker signal.
- For Supabase, privileged payment writes belong in Edge Functions or server routes with service role isolated from browser code.
- If official docs are unavailable or gated, state that and ask for merchant docs. Do not invent endpoints, status names, headers, signatures, or test cards.
- For providers with full-depth coverage, use the provider file as a checklist and still link to the official docs for endpoint-level details.
- For providers with conservative coverage, stop before custom endpoint work unless official merchant docs are provided.

## Required Output

When answering a payment implementation or review request, return:

1. Current payment architecture.
2. Provider contract and source confidence.
3. Server boundary and secret handling.
4. Idempotency strategy.
5. Risk points and safe fix plan.
6. Test matrix including duplicate events, invalid signature, amount/currency mismatch, callback-before-redirect, and redirect-before-callback.
7. Remaining unknowns and deployment/rollback notes.
