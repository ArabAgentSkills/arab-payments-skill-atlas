# Private Watcher Setup

Use a private companion repository to run full provider documentation monitoring without exposing unreviewed findings or full snapshots publicly. A suggested name is `arab-payments-skill-atlas-watch`.

## Why Private

Public GitHub issues, pull requests, Actions logs, and artifacts can be visible to the public. Provider documentation changes should remain private until a human approves public guidance updates.

## Repository Setup

1. Create a private GitHub repository.
2. Add this public repository as a checkout target in the workflow.
3. Add a fine-scoped token or GitHub App credential as a private repository secret if the watcher needs to open issues or pull requests in the private repo.
4. Do not store provider credentials, merchant dashboard exports, or private merchant docs in the watcher repo.
5. The workflow below creates the `source-watch` label if it does not already exist.

## Workflow Template

Save this in the private repository as `.github/workflows/private-source-watch.yml`.

```yaml
name: Private Provider Source Watch

on:
  workflow_dispatch:
  schedule:
    - cron: "37 5 * * 1"

permissions:
  contents: read
  issues: write
  actions: read

jobs:
  watch:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout public skill repo
        uses: actions/checkout@v4
        with:
          repository: ArabAgentSkills/arab-payments-skill-atlas
          path: skill

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Capture source changes
        id: watch
        working-directory: skill
        run: |
          set +e
          python scripts/check_source_changes.py --check --output-dir ../source-watch-artifacts
          code=$?
          echo "exit_code=$code" >> "$GITHUB_OUTPUT"
          exit 0

      - name: Check links
        id: links
        working-directory: skill
        run: |
          set +e
          python scripts/check_source_links.py
          code=$?
          echo "exit_code=$code" >> "$GITHUB_OUTPUT"
          exit 0

      - name: Upload private snapshots
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: source-watch-artifacts
          path: source-watch-artifacts
          if-no-files-found: warn
          retention-days: 14

      - name: Create private owner issue
        if: steps.watch.outputs.exit_code != '0' || steps.links.outputs.exit_code != '0'
        uses: actions/github-script@v7
        with:
          script: |
            try {
              await github.rest.issues.getLabel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                name: 'source-watch'
              });
            } catch (error) {
              if (error.status === 404) {
                await github.rest.issues.createLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  name: 'source-watch',
                  color: '0E8A16',
                  description: 'Private provider documentation watch findings'
                });
              } else {
                throw error;
              }
            }
            const title = 'Provider source watch review required';
            const body = [
              'Private source watcher requires maintainer review.',
              '',
              `Source changes exit code: ${'${{ steps.watch.outputs.exit_code }}'}`,
              `Source links exit code: ${'${{ steps.links.outputs.exit_code }}'}`,
              'Review the workflow log and the private `source-watch-artifacts` artifact.',
              'Do not publish provider guidance until a human has reviewed the changes.',
              '',
              `Run: ${context.serverUrl}/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId}`
            ].join('\n');
            const { data: issues } = await github.rest.issues.listForRepo({
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open',
              labels: 'source-watch'
            });
            const existing = issues.find(issue => issue.title === title);
            if (existing) {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: existing.number,
                body
              });
            } else {
              await github.rest.issues.create({
                owner: context.repo.owner,
                repo: context.repo.repo,
                title,
                body,
                labels: ['source-watch']
              });
            }
```

## Human Approval Flow

1. Review the private issue and artifact.
2. Open a public PR only with curated summaries, baseline metadata, changelog updates, and version updates.
3. Run all validators.
4. Merge and publish a public release.

Installed user copies can then update from that approved public release through `scripts/install_or_update_skill.py`.
