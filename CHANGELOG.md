# Changelog

## Unreleased

## 1.2.0 - 2026-07-06

- Updated Tabby guidance for the current payment-webhook/dispute-webhook split, the documented 180-day refund initiation window, and refund/dispute handling tests.
- Updated Tamara guidance for the current authorisation and capture lifecycle, including the documented 21-day auto-capture behavior for authorised but uncaptured orders.
- Refreshed public-safe source-watch metadata after reviewing private watcher issue #13 and run 28774155853.
- Kept Tap Payments, Geidea, MyFatoorah, and HyperPay guidance unchanged after review found docs formatting, index, or source fingerprint churn rather than unsupported payment guidance deltas.

## 1.1.3 - 2026-06-22

- Hardened source-watch normalization for docs copy-action chrome, EasyKash-style `Last updated ... ago` relative ages, and GitHub repository `updated_at` metadata churn.
- Refreshed the public-safe source-watch baseline and report after reviewing private watcher run 27935465599 / issue #12.
- Kept provider guidance unchanged after maintainer review found docs-index, relative-age, copy-action, and repository metadata drift rather than new payment behavior.
- Added regression coverage for the new source-watch normalization cases.

## 1.1.2 - 2026-06-15

- Treated source-watch OK-to-JavaScript-challenge degradations as maintainer review warnings instead of payment documentation changes, matching the existing source-link checker behavior.
- Treated transient HTTP 408, 429, and 5xx fetch failures as review warnings in source-change comparison while preserving non-transient HTTP failures as changes requiring review.
- Added regression coverage for runner-only GitHub API JavaScript challenges and transient HTTP fetch failures.

## 1.1.1 - 2026-06-15

- Hardened source-watch normalization to strip common provider docs navigation/sidebar/footer chrome, AI-index notices, GitBook Markdown notices, recent-request widgets, and approximate relative update ages before hashing.
- Added regression coverage so docs-site chrome churn does not trigger release review while real payment guidance changes still do.
- Refreshed the public-safe source-watch baseline with the improved normalizer.

## 1.1.0 - 2026-06-15

- Added Moyasar guidance for standalone 3D Secure card-authentication webhook events after private source-watch run 27529717585.
- Clarified that `card_auth_authenticated` and `card_auth_failed` are card-authentication outcomes, not payment fulfillment states, and still require Moyasar secret-token validation plus idempotent event handling.
- Added Moyasar card-authentication source URLs and an eval scenario covering the new webhook event handling.
- Refreshed public-safe source-watch metadata after reviewing concurrent docs-site navigation/chrome changes.

## 1.0.10 - 2026-06-10

- Refreshed the public-safe source-watch baseline for FawryPay, MyFatoorah, Tabby, Tamara, and EasyKash after private watcher runs 27294185835 and 27294164650.
- Kept provider guidance unchanged after maintainer review found documentation-site chrome, navigation, and agent-readable index churn rather than new payment behavior.
- Classified the one-run Kashier GitHub API HTTP 504 as a transient fetch warning because the same source was reachable in link checking and did not recur in the paired watcher run.

## 1.0.9 - 2026-06-08

- Hardened source-watch automation so private snapshot capture runs before link-failure judgment, transient provider-side HTTP errors are review-required `SERVER_ERROR` findings instead of confirmed broken links, and recurring maintainer review can use a dedicated source-watch subagent.
- Added regression coverage for source-link HTTP status classification and review-required exit behavior.

## 1.0.8 - 2026-06-08

- Refreshed the public-safe source-watch baseline for an EasyKash Pay API fingerprint change after private watcher run 27130472493.
- Kept provider guidance unchanged after maintainer review found the existing EasyKash redirect, callback HMAC, inquiry, amount/currency, and idempotency guidance still matched the public docs.
- Preserved Paymob manual browser verification status for current public docs that still require browser/TLS review.

## 1.0.7 - 2026-06-08

- Replaced the HyperPay webhook tutorial source URL after the official route began returning HTTP 500, using the reachable official HyperPay Webhooks FAQ and existing API notification parameter reference instead.
- Verified GitHub organization/repository-root source links through the GitHub API to avoid treating transient GitHub HTML 5xx responses as broken official demo sources.
- Refreshed public-safe source-watch metadata for current Tap Payments, Tabby, Tamara, PayTabs, PaySky, HyperPay, and Kashier source chrome/API metadata without changing provider behavior guidance.

## 1.0.6 - 2026-06-01

- Treated transient source-watch fetch exceptions such as `URLError` and `TimeoutError` as degraded hash evidence when the previous public baseline was OK; `check_source_links.py` remains the gate for actual broken public source URLs.
- Documented the failed v1.0.5 workflow-dispatch validation as a FawryPay runner fetch flake after source-link reachability had already passed.

## 1.0.5 - 2026-06-01

- Normalized volatile provider-docs page chrome such as `Updated 3 months ago` and transient HyperPay navigation labels so scheduled source-watch CI does not fail on chrome drift.
- Refreshed the public-safe source-watch baseline after confirming the MyFatoorah scheduled CI failure and HyperPay validation drift were page chrome noise, not new payment behavior.
- Added regression coverage so real provider-content changes still change the source-watch fingerprint.

## 1.0.4 - 2026-06-01

- Refreshed public-safe source-watch fingerprints for Tap Payments, Geidea, MyFatoorah, Tamara, and Kashier after private watcher run 26740307429.
- Kept provider guidance unchanged after maintainer review found documentation-site chrome and agent-readable docs notices rather than new payment behavior.
- Preserved Paymob manual browser verification status for current public docs that still require browser/TLS review.

## 1.0.3 - 2026-05-29

- Added public-safe official agent-readable docs indexes for Tap Payments, Geidea, MyFatoorah, Tabby, and Tamara where providers publish `llms.txt`.
- Added separate latest-docs fetch guidance to `mena-payment-guardian` and `egypt-payment-guardian` so agents preserve Arab/MENA vs Egypt skill boundaries.
- Updated MENA provider references for Tap Payments, Geidea, MyFatoorah, Tabby, Tamara, HyperPay, and PSP-routed valU/Souhoola without copying full provider docs.
- Updated Egypt provider references only for Geidea Egypt and Egypt BNPL method source discovery, avoiding unrelated MENA-only provider assumptions.
- Added routing validation so MENA-only provider sources cannot leak into the Egypt provider index and provider references cannot claim official agent-readable docs without matching indexed source URLs.

## 1.0.2 - 2026-05-28

- Refreshed public-safe source-watch fingerprints for Tap Payments, Geidea, MyFatoorah, Tabby, Tamara, and HyperPay after private watcher run 26599965590.
- Kept provider guidance unchanged after maintainer review found documentation fingerprint drift rather than new payment behavior.
- Refreshed the HyperPay source-watch baseline from the validated watcher environment and normalized local TLS verification fallback handling.

## 1.0.1 - 2026-05-25

- Added an executable eval scenario harness with automated `must` / `must-not` checks.
- Added MENA pressure scenarios for PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, and Amazon Payment Services.
- Wired eval validation, unit tests, and source-change detection into maintainer/CI workflows.
- Fixed private source-watch snapshot filenames for provider ids that contain punctuation unsafe for artifact paths.
- Reviewed Tap, Tamara, and EasyKash public source changes and refined public-safe guidance for webhook hash validation, auto-authorisation, and inquiry statuses.

## 1.0.0 - 2026-05-24

- Added `mena-payment-guardian` as a second installable skill for Arab/MENA PSP and BNPL work.
- Covered Paymob, FawryPay, Geidea, PayTabs, Tap Payments, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, EasyKash, Kashier, PaySky, Tabby, Tamara, valU, and Souhoola.
- Kept `egypt-payment-guardian` stable for existing Egypt-only users.
- Updated adapters, README, source-watch tooling, and updater behavior for two installable skills.
- Deferred non-payment workbook rows to future packs.

## 0.1.1 - 2026-05-23

- Added `npx skills` install and update documentation.
- Polished the public GitHub storefront presentation and repository install path.

## 0.1.0 - 2026-05-23

- Initial Arab Payments Skill Atlas public package, starting with the Egypt Payment Guardian V1 skill pack.
- Added Egypt provider references for Paymob, FawryPay, Geidea Egypt, EasyKash, PaySky, Kashier, valU, and Souhoola.
- Added multi-agent adapters for Codex, Claude Code, Cursor, GitHub Copilot, and generic agents.
- Added validation, secret scanning, source link checking, and source-watch tooling.

## Release Policy

Only approved public changes are listed here. Private watcher findings, full provider snapshots, and unreviewed provider documentation changes must not be published in this changelog.
