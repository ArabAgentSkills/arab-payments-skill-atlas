# PaySky

- Provider: PaySky
- Scope: Egypt / MENA PSP with PayForm Plus, Omni Gateway notifications, PayButton SDKs, SecureHash verification, ActionCode mapping, and EGP numeric currency handling where documented.
- Priority: P1
- Readiness: B+
- Public docs status: public-partial
- Last checked: 2026-05-24
- Source confidence: Medium-high for public PaySky docs; some merchant/account behavior may be configured privately.
- Sources: PaySky docs home, PayForm Plus, Omni Gateway notification services, Android PayButton SDK, iOS PayButton SDK.

## Use When

Use for PaySky PayForm Plus, PayButton mobile SDKs, notification services, SecureHash validation, ActionCode mapping, and EGP payment flows.

## Source Map

- Docs: `https://paysky.io/docs/`
- PayForm Plus: `https://paysky.io/docs/paysky-omni-gateway-payform-plus-integration-guide/`
- Notification services: `https://paysky.io/docs/paysky-omni-gateway/`
- Android SDK: `https://paysky.io/docs/paysky-paybutton-sdk-android-guide/`
- iOS SDK: `https://paysky.io/docs/paysky-paybutton-sdk-ios-guide/`

## Integration Paths

- PayForm Plus hosted gateway.
- Omni Gateway notification services.
- PayButton SDKs for Android/iOS.

## Setup Prerequisites

- Merchant id, terminal id, secure hash secret, callback/notification URL, currency code, environment, and amount unit rules.

## Auth And Secret Boundary

- Keep terminal secrets, secure hash keys, merchant credentials, and notification verification material server-side.
- SDK/frontend must not contain backend SecureHash secrets.

## Callback Or Webhook Contract

- Treat notification service as server-side source of truth.
- Redirect/SDK success is UX only until notification SecureHash or documented status inquiry verifies payment.
- Store system reference, transaction id, ActionCode, amount, currency, and hash verification result.

## Signature Or HMAC

- Verify SecureHash according to PaySky's sorted field/value rules for the flow in use.
- Use documented fields exactly; field order and exclusions matter.

## Idempotency Keys

- Use merchant reference/system reference plus PaySky transaction id.
- Deduplicate notifications and SDK refreshes.

## Amount And Currency

- Public docs document EGP numeric currency `818` in relevant flows.
- Amounts may use smallest-unit handling; compare exactly to local expected value and unit.

## Status Mapping

- Use documented `ActionCode` and result/status fields.
- Approved/success ActionCode maps to paid only after SecureHash and amount/currency/reference checks.
- Pending, declined, failed, or cancelled statuses must not fulfill.

## Refunds Voids And Subscriptions

- Use only documented PaySky operations or merchant docs for refunds, voids, reversals, and capture.
- No subscription behavior should be inferred from PayForm Plus docs.

## Sandbox And Test Notes

- Test SecureHash failures, ActionCode mapping, duplicate notifications, and EGP `818` handling.

## Unknowns And Do Not Invent

- Do not invent ActionCode meanings, hash fields, local method availability, or reversal endpoints.
- Ask for merchant docs for account-specific PaySky Omni configuration.

## Agent Checklist

- Verify SecureHash before processing.
- Compare EGP numeric currency and amount unit.
- Map ActionCode from official docs.
- Keep terminal/secure hash secrets backend-only.
- Deduplicate notifications.

## Fail If

- You skip SecureHash.
- You handle EGP as a guessed text/numeric variant without checking docs.
- You trust SDK success alone.
- You expose terminal secrets in mobile/web client code.
