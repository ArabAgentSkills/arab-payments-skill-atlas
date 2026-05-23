# Eval: PaySky SecureHash And EGP

## User Prompt

"Implement PaySky notification handling. The notification has ActionCode 00, Amount 200000, Currency 818, and SecureHash."

## Required Skill Use

Load `references/providers/paysky.md`.

## Expected Agent Behavior

- Verifies SecureHash before processing.
- Uses the operation-specific sorted field list from PaySky docs.
- Treats Currency `818` as EGP where documented.
- Treats amount as smallest currency units for notification docs.
- Maps ActionCode `00` as approved only after verification and local reference match.
- Makes SystemReference/NetworkReference idempotent.

## Fail If

- The agent ignores SecureHash.
- The agent treats 200000 as 200000 EGP without checking smallest-unit rules.
- The agent treats all ActionCodes as paid.
