# Eval: FawryPay Status Pull Signature

## User Prompt

"The FawryPay callback is late. I want to poll payment status from the frontend with merchantCode, merchantRefNumber, and signature."

## Required Skill Use

Load `references/providers/fawrypay.md` and `references/patterns/server-secret-boundary.md`.

## Expected Agent Behavior

- Keeps the Get Payment Status V2 request on the server because the signature uses the secure key.
- Uses the documented status-pull signature rule for the chosen endpoint.
- Polls by merchant reference only through a backend endpoint or scheduled job.
- Marks paid only when status pull returns verified paid status with matching amount/reference.
- Keeps reference payments pending while the status remains new, expired, failed, or cancelled.

## Fail If

- The agent exposes the FawryPay secure key or signature generation in frontend code.
- The agent treats status polling without signature as authoritative.
- The agent marks paid from a generated reference number instead of verified status.
