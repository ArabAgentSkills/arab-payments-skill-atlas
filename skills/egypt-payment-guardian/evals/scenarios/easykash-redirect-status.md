# Eval: EasyKash Redirect Status

## User Prompt

"EasyKash redirects to `/success?status=success&providerRefNum=123`. Unlock the course there."

## Required Skill Use

Load `references/providers/easykash.md` and `references/patterns/webhook-first-fulfillment.md`.

## Expected Agent Behavior

- Treats redirect status as display-only.
- Uses verified Callback Service or server-side Payment Inquiry before unlocking.
- Verifies EasyKash HMAC SHA-512 callback with documented field order.
- Uses `customerReference` and `easykashRef` for idempotency.
- Handles pending, failed, cancelled, expired, refunded, and paid inquiry states.

## Fail If

- Frontend redirect unlocks the course.
- Voucher/reference generation is treated as paid.
- HMAC verification uses an invented field order.

## Automated Checks

- must: redirect status as display-only
- must: Callback Service
- must: Payment Inquiry
- must: HMAC SHA-512
- must: customerReference
- must: idempotency
- must-not: frontend redirect unlocks
