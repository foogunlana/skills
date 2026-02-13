# Integrations

This skill is intentionally simple: you call a local script with a hook name, and it plays a sound.

## Claude Code (Prompt-Level Hooks)

If you want sounds to happen reliably, keep the hook names consistent and call the script at the end of the relevant step.

Examples:

```bash
python3 .claude/skills/agent-sounds/scripts/agent_sounds.py emit plan.done
python3 .claude/skills/agent-sounds/scripts/agent_sounds.py emit task.done
python3 .claude/skills/agent-sounds/scripts/agent_sounds.py emit error
```

Recommended usage patterns:

- After presenting a final plan: emit `plan.done`.
- After finishing implementation and verification: emit `task.done`.
- After reporting an error and next action: emit `error`.

### Project-Wide Always-On (Optional)

If you want this behavior even when you are not explicitly invoking `/agent-sounds`, add a short section to your project's `CLAUDE.md` telling the agent to emit hook sounds.

Minimal snippet:

```text
## Agent Sounds

After producing a final plan, run:
python3 .claude/skills/agent-sounds/scripts/agent_sounds.py emit plan.done
```

## Shell / CLI Workflows

You can use `agent_sounds.py` in any shell script:

```bash
set -euo pipefail

do_work || {
  python3 .claude/skills/agent-sounds/scripts/agent_sounds.py emit error
  exit 1
}

python3 .claude/skills/agent-sounds/scripts/agent_sounds.py emit run.done
```

## Other Agent Frameworks

The portable interface is:

```text
agent_sounds.py emit <hook-name> [--message "..."]
```

Any framework that supports lifecycle callbacks can integrate by calling that command on:

- Plan finalized
- Task completed
- Tool error / exception
- Waiting for user input
