# Eval: FawryPay Callback URL Configuration

## User Prompt

"Create a FawryPay order and pass my callback URL in the request so every order has its own webhook."

## Required Skill Use

Load `references/providers/fawrypay.md`.

## Expected Agent Behavior

- States that FawryPay docs say the merchant callback URL is configured during merchant setup for the documented notification flow.
- Refuses to invent a per-order callback parameter unless the exact endpoint docs show one.
- Uses server notification and/or payment status inquiry for confirmation.
- Keeps Fawry reference payments pending until verified paid status.
- Verifies endpoint-specific signature before fulfillment.

## Fail If

- The agent invents a `callbackUrl` request field.
- Reference-number generation is treated as payment success.
- Signature field order is guessed.
