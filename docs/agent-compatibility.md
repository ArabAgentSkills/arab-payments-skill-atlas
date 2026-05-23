# Agent Compatibility

Arab Payments Skill Atlas currently ships the Egypt Payment Guardian V1 skill pack. The canonical source for the installed skill is `skills/egypt-payment-guardian/SKILL.md`. Every adapter in this repository is a thin loader that points agents back to that skill and its provider references.

## Compatibility Matrix

| Agent or runtime | Native file | Confidence | Notes |
| --- | --- | --- | --- |
| Codex | `AGENTS.md` | High | Codex-style agents can read root project instructions. |
| OpenCode and AGENTS.md-compatible agents | `AGENTS.md` | High | Keep this file at the target project root. |
| Claude Code | `CLAUDE.md` plus `.claude/skills/egypt-payment-guardian/SKILL.md` | High | Use `CLAUDE.md` as project memory and copy the skill folder when native skills are available. |
| Cursor | `.cursor/rules/egypt-payment-guardian.mdc` | High | Agent Requested rule; the agent loads it when payment work is relevant. |
| GitHub Copilot | `.github/copilot-instructions.md` | Medium | Copilot instructions are concise; keep provider detail in the skill files. |
| OpenClaw, Hermes, and custom agents | `adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md` | Medium | Paste the generic prompt into the agent's project, memory, or system instructions. |

## Install Snippets

Codex or AGENTS.md-compatible project:

```powershell
$target = "C:\path\to\your-project"
Copy-Item .\AGENTS.md "$target\AGENTS.md" -Force
```

Claude Code project-local skill:

```powershell
$target = "C:\path\to\your-project"
New-Item -ItemType Directory -Force "$target\.claude\skills" | Out-Null
Copy-Item -Recurse .\skills\egypt-payment-guardian "$target\.claude\skills\egypt-payment-guardian" -Force
Copy-Item .\CLAUDE.md "$target\CLAUDE.md" -Force
```

Cursor:

```powershell
$target = "C:\path\to\your-project"
New-Item -ItemType Directory -Force "$target\.cursor\rules" | Out-Null
Copy-Item .\.cursor\rules\egypt-payment-guardian.mdc "$target\.cursor\rules\egypt-payment-guardian.mdc" -Force
```

GitHub Copilot:

```powershell
$target = "C:\path\to\your-project"
New-Item -ItemType Directory -Force "$target\.github" | Out-Null
Copy-Item .\.github\copilot-instructions.md "$target\.github\copilot-instructions.md" -Force
```

macOS/Linux generic skill install:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R ./skills/egypt-payment-guardian "$HOME/.agents/skills/egypt-payment-guardian"
```

Manual fallback:

```text
Paste adapters/generic/EGYPT_PAYMENT_GUARDIAN_PROMPT.md into the agent's project instructions, then tell the agent where this repository lives.
```

All project-local adapters at once:

```powershell
$target = "C:\path\to\your-project"
python .\scripts\install_or_update_skill.py --agent all --target $target
```

This command does not update the global Codex skill unless `--include-global-codex` is supplied. Use `--agent codex` for a dedicated global Codex install.

## Adapter Rules

- Adapters are not the source of truth.
- Adapters must point to `skills/egypt-payment-guardian/SKILL.md`.
- Adapters must stay short and avoid copied provider docs.
- Provider-specific details stay in `skills/egypt-payment-guardian/references/providers/`.
- Unknown or custom agents should use `AGENTS.md` first, then the generic prompt if they cannot read project files automatically.

## Compatibility Promise

This repository provides native adapters where common agents support them and a generic prompt for everything else. It does not guarantee that every proprietary runtime auto-discovers every file. If an agent cannot auto-load the adapter, paste the generic prompt into that agent's project instructions and keep the skill folder available as reference material.
