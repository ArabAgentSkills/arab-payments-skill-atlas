# Webhook-First Fulfillment

Use this pattern whenever a provider has both a customer redirect and a server callback/webhook/IPN/notification.

## Rule

Redirects are customer UX. Fulfillment belongs to verified server-side state.

## Safe Flow

1. Server creates payment intent/session/order and stores local pending state.
2. Customer is redirected to provider checkout.
3. Provider redirects customer back; UI shows `processing` unless backend already verified paid/captured state.
4. Backend receives callback/webhook/IPN/notification or performs documented status inquiry.
5. Backend verifies authenticity, amount, currency, country/account, local order reference, and provider reference.
6. Backend writes idempotent final state and fulfills once.

## Red Flags

- Browser return URL writes paid state.
- Mobile SDK success callback activates value directly.
- Webhook handler trusts unsigned body.
- Status inquiry does not compare amount/currency/reference.
- Duplicate event creates duplicate shipment, credit, booking, invoice, or subscription.
