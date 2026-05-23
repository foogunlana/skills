---
name: commit-and-mr
description: Commit changes and create a Merge/Pull Request following project conventions. Use when the user asks to commit, push, create an MR/PR, or ship/land their work. Handles staging, committing (with conventional commit format), pushing, and MR/PR creation with proper descriptions. Single commit per MR/PR; amends if one already has a commit.
---

# Commit and Create MR/PR

## Configuration

This skill supports both GitHub and GitLab. Configure these values for your project:

| Setting | Default | Options |
|---------|---------|---------|
| **VCS platform** | GitHub (`gh`) | GitHub (`gh`), GitLab (`glab`) |
| **Base branch** | `main` | Any branch name (e.g. `develop`, `master`) |
| **Issue tracker** | None | ClickUp, Jira, Linear, GitHub Issues, GitLab Issues |
| **Commit footer format** | None | e.g. `Closes #123`, `Fixes PROJ-456`, `Relates to clickup#abc` |
| **Commit hook** | None | commitizen, commitlint, or custom regex |

## Workflow

### 1. Analyze the full diff from base branch

Run these in parallel:
- `git diff <base-branch>...HEAD` — full diff of all changes on this branch vs base
- `git status` — current working tree state
- `git log <base-branch>..HEAD --oneline` — existing commits on this branch
- `git branch --show-current` — current branch name

The commit message and MR/PR description must reflect ALL changes between the base branch and HEAD (not just the latest unstaged changes). This is critical.

### 2. Stage only relevant files

Stage only files related to the task the user asked to commit. Never stage `.env`, credentials, or unrelated changes. Use `git add <specific-files>`.

### 3. Commit

**Format** (conventional commits):
```
{type}({context}): {short_description}

- {bullet point body item 1}
- {bullet point body item 2}

{footer}
```

Types: `feat`, `fix`, `bug`, `chore`, `refactor`, `perf`, `ci`

- Context is optional (e.g., `feat(search): add filters`)
- Body is optional but must be a bullet list if present
- The short_description must be lowercase, no period
- **Footer**: If your project uses an issue tracker, include a footer linking the issue. Format depends on your tracker:
  - GitHub Issues: `Closes #123`
  - Jira: `Fixes PROJ-456`
  - Linear: `Fixes LIN-789`
  - ClickUp: `Implements clickup#abc123`
  - GitLab Issues: `Closes #123`
- If the project uses a commit hook (e.g. commitizen), ensure the message matches the expected regex

**Commitizen regex (optional, for projects that use it):**
```
(perf|ci|feat|fix|bug|chore|refactor)(\([A-Za-z0-9\-]{1,}\)){0,1}: [\S ]{1,}
(\n(- [\S\n ]{1,}\n)*){0,1}
(footer pattern here)
```

**Single commit per MR/PR rule:**
- If `git log <base-branch>..HEAD --oneline` shows existing commits on the branch, use `git commit --amend --no-edit` after staging, then force-update the message with `git commit --amend` using the new message
- If no existing commits, create a new commit

**Commit message via HEREDOC:**
```bash
git commit -m "$(cat <<'EOF'
type(context): short description

- change detail 1
- change detail 2

Relates to #ID
EOF
)"
```

**Example:**
```
feat(search): add semantic search endpoint

- Add vector similarity integration
- Add /api/v1/search/semantic/ endpoint

Implements #86
```

### 4. Handle commit hook failures

If the project uses pre-commit hooks (e.g. formatters, linters, commitizen):

- If hook fails with auto-fixable issues (e.g., formatter reformatted files): re-stage the fixed files and retry the commit
- If hook fails with non-obvious errors (e.g., complex lint issues, type errors): show the error to the user and ask how to proceed
- Never use `--no-verify`

### 5. Push

```bash
git push -u origin $(git branch --show-current) --force-with-lease
```

Use `--force-with-lease` because we may have amended. This is safe since it's a feature branch.

### 6. Create the MR/PR

Use your platform's CLI tool. If an MR/PR already exists for this branch, update it instead.

**For GitHub (`gh`):**
```bash
# Check for existing PR
gh pr list --head $(git branch --show-current)

# Create
gh pr create --title "the title" --body "$(cat <<'EOF'
...body...
EOF
)" --base <base-branch>

# Update existing
gh pr edit {pr_number} --title "the title" --body "$(cat <<'EOF'
...body...
EOF
)"
```

**For GitLab (`glab`):**
```bash
# Check for existing MR
glab mr list --source-branch=$(git branch --show-current)

# Create
glab mr create --title "the title" --description "$(cat <<'EOF'
...body...
EOF
)" --target-branch <base-branch>

# Update existing
glab mr update {mr_number} --title "the title" --description "$(cat <<'EOF'
...body...
EOF
)"
```

**MR/PR title:** Same as commit subject line (e.g., `feat(context): short description`)

**MR/PR body template:**
```
closes #{issue_id}

## Changes

- {bullet summary of each logical change from the full diff}
- {reference specific files/methods changed using backticks}

## Useful Links

- [Ticket Link]({issue_tracker_url}/{ISSUE_ID})

## Deployment Steps

- [ ] No special deployment steps required

## How to test

- {specific test steps based on what changed}
- {include commands to run if applicable}
- {include URLs to visit if UI changes}

## ScreenShots

{only include if UI changes were made}
```

### 7. Report back

Provide the MR/PR URL to the user when done.
