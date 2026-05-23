# PaySky

- Provider: PaySky
- Scope: Egypt/MENA OMNI Gateway, PayForm Plus, notification services, PayButton SDKs, SecureHash, cards, Meeza, wallets, QR channels, refunds, and void notifications.
- Priority: P1
- Readiness: B+ for public PayForm Plus and notification docs; merchant and terminal details remain partner-provided.
- Public docs status: public partial.
- Last checked: 2026-05-23
- Source confidence: High for public notification SecureHash, amount/currency handling, transaction type, and ActionCode mapping; medium for endpoint-level merchant setup because partner bank details are required.
- Sources:
  - https://paysky.io/docs/
  - https://paysky.io/docs/paysky-omni-gateway-payform-plus-integration-guide/
  - https://paysky.io/docs/paysky-omni-gateway/
  - https://paysky.io/docs/paysky-paybutton-sdk-android-guide/
  - https://paysky.io/docs/paysky-paybutton-sdk-ios-guide/

## Use When

Use for PaySky PayForm Plus checkout, OMNI Gateway Notification Services, PayButton Android/iOS SDKs, PaySky plugin integrations, Meeza cards, wallets, QR payments, SecureHash verification, numeric EGP currency handling, and ActionCode mapping.

## Source Map

- PayForm Plus guide covers LightBox/web checkout, partner-bank prerequisites, supported channels, and request/callback SecureHash concepts.
- Notification Services guide covers merchant REST endpoint requirements, notification payload, SecureHash verification, amount/currency units, transaction types, and ActionCode meanings.
- Android and iOS PayButton guides cover mobile SDK usage and should be loaded before mobile integration work.
- Public docs do not replace partner-provided merchant ID, terminal ID, SID/token, or secret key details.

## Integration Paths

- PayForm Plus LightBox checkout embedded in a merchant website.
- OMNI Gateway Notification Services to receive transaction notifications.
- Android PayButton SDK.
- iOS PayButton SDK.
- Ecommerce plugins such as WooCommerce.
- Partner-bank configured terminals for card, digital QR, wallet, Meeza, and pay-on-delivery channels where enabled.

## Setup Prerequisites

- Merchant ID assigned by partner bank or PaySky integration consultant.
- Terminal ID for the enabled acceptance channel.
- Merchant secret key, Terminal SID, token, or other partner-provided values stored securely.
- Notification REST endpoint implemented by merchant and reachable.
- Local order stores MerchantReference, expected amount in smallest currency units, numeric ISO currency, provider references, and transaction type.
- ActionCode mapping table is present in code/tests before fulfillment.

## Auth And Secret Boundary

Merchant ID, Terminal ID, Terminal SID, token, merchant secret key, and SecureHash material are sensitive. Keep them in backend secret storage or secure native/plugin configuration. Do not expose merchant secret key or terminal credentials in browser code, public mobile bundles, logs, screenshots, or GitHub.

## Callback Or Webhook Contract

Notification Services allow merchants to receive transaction notifications by implementing a REST API. Treat all notification payloads as untrusted until SecureHash is verified. Return the documented acknowledgement response only after the payload is safely parsed and persisted.

PayForm Plus complete/error callbacks are UX signals unless the operation-specific SecureHash and server reconciliation pass. SDK callback success is not enough for order fulfillment without SecureHash-backed notification or server-side verification.

## Signature Or HMAC

PaySky SecureHash uses SHA-256 HMAC:

- For Notification Services, hash fields are `DateTimeLocalTrxn`, `MerchantId`, `TerminalId`, `Amount`, and `Currency`.
- Sort fields ascending by parameter name: `Amount`, `Currency`, `DateTimeLocalTrxn`, `MerchantId`, `TerminalId`.
- Join each pair as `name=value`, then join pairs with `&`.
- Use the hex-decoded merchant secret key as the HMAC key.
- Encode the HMAC as uppercase hexadecimal and compare it to `SecureHash`.

PayForm Plus request and callback SecureHash field sets differ by operation. Load the PayForm Plus page and use the exact field list for that operation.

## Idempotency Keys

Use local order ID, `MerchantReference`, `SystemReference`, `NetworkReference`, `TerminalId`, `MerchantId`, `TxnType`, and `ActionCode`. Add uniqueness around provider references and the local merchant reference. Duplicate transmission (`ActionCode` 94) and notification retries must not create duplicate paid state.

## Amount And Currency

Notification docs state `Amount` is in the smallest currency units. `Currency` uses ISO 4217 numeric code; EGP is `818`. Convert local decimal amounts to the correct minor-unit integer before comparison. Reject payloads where amount, currency, merchant, terminal, or reference does not match local state.

## Status Mapping

- Local `paid`: verified SecureHash, `TxnType` sale, `ActionCode` `00`, and matching amount/currency/reference.
- Local `pending`: request created, no verified approval yet, issuer/request in progress codes, or awaiting notification.
- Local `failed`: declined, invalid amount, issuer unavailable, system malfunction, suspected fraud, or any non-approved ActionCode.
- Local `refunded`: verified `TxnType` refund with approved ActionCode.
- Local `voided`: verified `TxnType` void sale or void refund with approved ActionCode.
- Local `duplicate_ignored`: duplicate transmission or repeated provider reference that was already processed.

Do not treat all notifications as successful; ActionCode must be mapped.

## Refunds Voids And Subscriptions

Notification `TxnType` includes sale, refund, void sale, and void refund. Model each as a separate state transition. Refund or void notifications must never create a new paid event. PaySky public docs here do not establish subscription APIs; require official docs before subscription implementation.

## Sandbox And Test Notes

PayForm Plus docs include integration examples, but merchant and terminal data are partner-provided. Test SecureHash sorting, hex-decoded secret handling, uppercase digest comparison, EGP numeric `818`, smallest-unit amount conversion, ActionCode `00`, non-approved ActionCodes, duplicate references, refund, void sale, and void refund.

## Unknowns And Do Not Invent

- Do not invent Merchant ID, Terminal ID, SID, token, or secret key values.
- Do not assume major EGP units where docs require smallest currency units.
- Do not accept ActionCode without mapping.
- Do not reuse Notification Services SecureHash fields for every PayForm Plus operation.
- Do not treat SDK callback alone as paid.

## Agent Checklist

- Confirm integration path: PayForm Plus, notification service, SDK, or plugin.
- Keep partner-provided secrets out of frontend and GitHub.
- Verify SecureHash with operation-specific fields.
- Convert and compare amount in smallest currency units.
- Compare numeric currency code, especially EGP `818`.
- Map ActionCode and TxnType before state transition.
- Enforce idempotency by provider references and local order.
- Add tests for non-`00` ActionCodes, duplicate transmission, amount mismatch, and wrong SecureHash.

## Fail If

- The agent skips SecureHash verification.
- The agent treats ActionCode other than `00` as paid without documented approval semantics.
- The agent handles EGP as alphabetic `EGP` where PaySky notification docs require numeric `818`.
- The agent compares major-unit amount to smallest-unit amount without conversion.
- The agent exposes merchant secret key, SID, token, Merchant ID, or Terminal ID in frontend code or public repo material.
- The agent treats refund or void notifications as new sale payments.
