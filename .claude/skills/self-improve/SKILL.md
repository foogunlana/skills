---
name: self-improve
description: Run after completing any substantive task. Reflects on what knowledge gaps existed, recommends fixes, and applies them to skills/config. Runs as a subagent to avoid blocking the main conversation.
---

# Self-Improvement Retrospective

Run this skill after completing any substantive task (feature implementation, bug fix, debugging session, configuration work, etc.). It runs as a background subagent so it doesn't block the user.

## Trigger

After completing any task where you encountered friction, discovered something non-obvious, or had to retry/fail before succeeding. Do NOT trigger for trivial tasks (reading a file, answering a simple question).

## Execution

Launch a subagent with the following prompt structure. Pass it the context of what just happened (the task, what you struggled with, what you learned).

```
You are a self-improvement agent. Analyze the task that was just completed and produce three outputs:

### 1. Knowledge Gaps (bullet points)
What information would have improved execution if known beforehand?
- Only include non-obvious things (not "I should have read the file first")
- Focus on project-specific knowledge that won't change often
- Include tooling quirks, conventions, hidden requirements

### 2. Recommendations (table)
For each gap, what's the best fix?

| Gap | Fix location | Why there |
|-----|-------------|-----------|
| ... | skill / CLAUDE.md / config | ... |

Decision criteria:
- Favour skills over CLAUDE.md (skills are contextual, CLAUDE.md is global)
- Favour CLAUDE.md over memory (CLAUDE.md is shared, memory is personal)
- Only use memory for user preferences that don't belong in project config

### 3. Propose Changes
Write all proposed edits to a single file: `.claude/self-improve-proposal.md`
Format as:
- File path
- Section to edit (or "new section")
- Exact addition (1-2 lines per item)

Then notify the user: "Self-improvement retrospective complete. Review proposed changes in `.claude/self-improve-proposal.md`"

Do NOT apply changes directly. Wait for user confirmation.
```

## Subagent Launch

The main conversation should spawn this as a background agent:

```
Agent(
  subagent_type="general-purpose",
  run_in_background=true,
  description="self-improvement retrospective",
  prompt="<context about what just happened and what was learned>"
)
```

## What NOT to do

- Don't block the user waiting for this to complete
- Don't create new skills just for one-off learnings
- Don't add obvious things ("remember to read files before editing")
- Don't duplicate information already in CLAUDE.md or existing skills
- Don't modify code files — only propose changes to skills, CLAUDE.md, and config
- **NEVER apply changes without user confirmation** — always write proposals to `.claude/self-improve-proposal.md` and ask the user to review
