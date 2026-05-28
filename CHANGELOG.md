# Changelog

## Unreleased

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
