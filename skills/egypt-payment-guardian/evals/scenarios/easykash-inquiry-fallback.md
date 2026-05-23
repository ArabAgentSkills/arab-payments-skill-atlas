# Eval: EasyKash Inquiry Fallback

## User Prompt

"EasyKash callback did not arrive, but I have customerReference. Build a fallback so users do not get stuck."

## Required Skill Use

Load `references/providers/easykash.md`.

## Expected Agent Behavior

- Uses server-side Payment Inquiry by `customerReference`.
- Keeps the API key on the server.
- Maps inquiry statuses explicitly: NEW, PAID, FAILED, EXPIRED, REFUNDED, CANCELED, and DELIVERED.
- Fulfills only when inquiry returns PAID with matching amount/reference.
- Does not treat DELIVERED, voucher, or redirect status as paid without payment-state reconciliation.

## Fail If

- The agent calls EasyKash inquiry from frontend code with the API key.
- The agent marks paid from DELIVERED, voucher, or redirect state without a paid verification.
- The agent ignores amount/reference comparison.
