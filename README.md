# Arab Payments Skill Atlas

Arab Payments Skill Atlas is a payment-safety skill project for AI coding agents. V1 ships with Egypt Payment Guardian, an Egypt-first provider pack for Paymob, FawryPay, Geidea Egypt, EasyKash, PaySky, Kashier, valU, and Souhoola.

Created by Mohamed Waleed and Fady Azzouny with the help of Codex GPT-5.5.

Public home after launch: `https://github.com/ArabAgentSkills/arab-payments-skill-atlas`

GitHub description: AI agent skill atlas for safe Arab-region payment integrations, starting with Egypt provider coverage.

## What This Skill Does

This repository packages source-backed guidance for payment providers and methods, starting with Egypt. The current installed skill is `egypt-payment-guardian`; future Arab-region packs can be added without renaming the Egypt V1 skill. The skill tells an agent what to verify before writing or reviewing payment code:

- which provider and integration path is being used
- where secrets must live
- what confirms payment success
- how to verify callbacks, webhooks, HMACs, signatures, or SecureHash values
- which amount, currency, order, and provider references must match
- how to make callbacks, retries, redirects, and refreshes idempotent
- what the agent must refuse to guess when docs are partial or gated

## V1 Coverage

V1 is Egypt-only. The repository name is intentionally broader because later releases can add more Arab and MENA payment packs after the same source-backed review process.

Full-depth coverage where official public docs support it:

- Paymob
- FawryPay
- Geidea Egypt
- EasyKash
- PaySky

Method-depth coverage:

- valU and Souhoola as PSP-routed BNPL payment methods, especially through Geidea and other enabled PSP accounts

Conservative coverage:

- Kashier, using official site, official GitHub demos, and official plugins until endpoint-level docs are accessible

Deferred to v2:

- Egyptian Tax Authority eInvoicing/eReceipt SDK, Daftra, Bosta, ShipBlu, CEQUENS
- PayTabs, Tap, MyFatoorah, HyperPay, Moyasar, Amazon Payment Services, and other broader MENA providers

## Safety Principles

- Never fulfill from a browser redirect, SDK success callback, hosted checkout event, or frontend-only status.
- Verify provider authenticity first: HMAC, signature, SecureHash, or documented status inquiry.
- Compare amount, currency, local order reference, and provider transaction/order reference.
- Make provider callbacks, retries, status pulls, redirects, and page refreshes idempotent.
- Keep merchant secrets, HMAC secrets, API passwords, terminal secrets, and service role keys server-side.
- If docs are gated or partial, say so and ask for official merchant docs. Do not invent endpoints, fields, signatures, test cards, or status names.

## Repository Layout

```text
AGENTS.md
CLAUDE.md
.cursor/rules/egypt-payment-guardian.mdc
.github/copilot-instructions.md
adapters/generic/
docs/
skill-version.json
skills/egypt-payment-guardian/
  SKILL.md
  references/provider-index.json
  references/providers/
  references/patterns/
  evals/scenarios/
scripts/
  validate_skill.py
  validate_adapters.py
  validate_source_watch.py
  secret_scan.py
  check_source_links.py
  check_source_changes.py
  install_or_update_skill.py
```

## Install

This repo supports practical adapters for multiple agent runtimes. `skills/egypt-payment-guardian/SKILL.md` remains the canonical source of truth.

| Agent or runtime | Adapter | How to use |
| --- | --- | --- |
| Codex, OpenCode, AGENTS.md-compatible agents | `AGENTS.md` | Keep the repo root adapter or copy it into the target project root. |
| Claude Code | `CLAUDE.md` and `skills/egypt-payment-guardian/` | Copy the skill folder into `.claude/skills/egypt-payment-guardian` or use the repo memory shim. |
| Cursor | `.cursor/rules/egypt-payment-guardian.mdc` | Copy the rule into the target project's `.cursor/rules/` directory. |
| GitHub Copilot | `.github/copilot-instructions.md` | Copy or merge the instructions into the target repository's Copilot instructions file. |
| OpenClaw, Hermes, custom agents | `adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md` | Paste the prompt into the agent's system, project, or memory instructions. |

Copy the skill folder into your agent skill directory:

```powershell
Copy-Item -Recurse .\skills\egypt-payment-guardian "$HOME\.agents\skills\egypt-payment-guardian" -Force
```

For Codex, restart or refresh the session after installing so the skill metadata is rediscovered.

Claude Code project-local install:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse .\skills\egypt-payment-guardian .\.claude\skills\egypt-payment-guardian -Force
```

macOS/Linux agent skill install:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R ./skills/egypt-payment-guardian "$HOME/.agents/skills/egypt-payment-guardian"
```

Manual fallback for any agent:

```text
Paste adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md into the agent's project instructions and keep this repo available as reference material.
```

See `docs/agent-compatibility.md` for the full compatibility notes.

## Update Installed Copies

Installed copies cannot be updated remotely without user consent. Users can opt in by running the updater manually, or by scheduling it locally through Windows Task Scheduler or cron.

Dry run the default Codex/global skill update:

```powershell
python .\scripts\install_or_update_skill.py --dry-run
```

Install or update the Codex/global skill from this approved package:

```powershell
python .\scripts\install_or_update_skill.py --agent codex
```

Install project-local adapters into another project:

```powershell
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\your-project
```

This installs project-local adapters only. To also update the global Codex skill, opt in explicitly:

```powershell
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\your-project --include-global-codex
```

After the first GitHub release is published, users can pull the latest approved public release:

```powershell
python .\scripts\install_or_update_skill.py --agent codex --use-latest-release
```

Until the public repository and first GitHub release exist, use local package installs only and do not advertise `--use-latest-release` as available.

The updater refuses to overwrite local user changes unless `--force` is provided.

## First Release Checklist

Before announcing latest-release updates:

1. Create the public GitHub repository at `ArabAgentSkills/arab-payments-skill-atlas`.
2. Set the local git remote to `https://github.com/ArabAgentSkills/arab-payments-skill-atlas.git`.
3. Push `main`.
4. Create the first version tag: `v0.1.0`.
5. Publish a GitHub release from that tag.
6. Run `python .\scripts\install_or_update_skill.py --agent codex --use-latest-release --dry-run`.
7. Update release notes only after the release dry-run succeeds.

## Source Watch And Approval

Provider documentation monitoring is split into public-safe metadata and private review evidence.

- Public repo: stores hashes, statuses, timestamps, short excerpts, and curated summaries only.
- Private watcher repo: may store full fetched snapshots as short-retention private workflow artifacts.
- Public guidance changes: published only after human review through a normal PR and approved release.

Use these local commands:

```powershell
python .\scripts\check_source_changes.py --check
python .\scripts\check_source_changes.py --update-baseline
```

See `docs/source-watch.md` and `docs/private-watcher-setup.md` for the full workflow.

## Validate

Run the local checks before publishing or installing:

```powershell
python .\scripts\validate_skill.py
python .\scripts\validate_adapters.py
python .\scripts\validate_source_watch.py
python .\scripts\secret_scan.py
python .\scripts\check_source_links.py
python .\scripts\check_source_changes.py --check
python .\scripts\install_or_update_skill.py --agent all --target C:\path\to\temp-project --dry-run
python .\scripts\install_or_update_skill.py --agent codex --dry-run
git diff --cached --check
```

`check_source_links.py` uses the network. It reports `JS_CHALLENGE` when a public docs page requires browser or JavaScript verification and fails only on clear breakage such as missing hosts, TLS errors, or `404`.

## Source Policy

This repository stores original summaries, provider contracts, source links, and eval scenarios. It does not vendor or republish full provider documentation.

Private merchant PDFs, screenshots, dashboards, credentials, onboarding emails, or portal exports must stay out of git. Put local-only materials under `private-docs/` or `local-docs/`; both are ignored.

Every provider update must include:

- official or provider-controlled source URLs
- `last_checked` date in `provider-index.json`
- concise source-backed summaries, not copied docs
- clear unknowns and "do not invent" notes
- eval updates when provider behavior changes

Private watcher findings and full fetched snapshots must not be published. Only human-approved summaries, baseline metadata, changelog entries, and releases belong in the public repo.

## Credits

- Co-creators and maintainers: Mohamed Waleed and Fady Azzouny
- Organization home: ArabAgentSkills
- Built with AI implementation assistance from Codex GPT-5.5

## Disclaimer

This project is not affiliated with Paymob, FawryPay, Geidea, EasyKash, Kashier, PaySky, valU, Souhoola, or any listed provider. It is a safety-oriented agent skill and does not replace official provider documentation, merchant agreements, legal advice, PCI DSS guidance, or production payment certification.
