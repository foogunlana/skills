# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains the **oya** skill for Claude Code - a planning companion that helps users start their day or week with intention and clarity.

## Oya Skill

**Location:** `.claude/skills/oya/`

Oya is a planning skill that provides:
- **Weekly planning** (10-15 min) - Review last week, set goals for this week
- **Daily planning** (5 min) - Copy tasks from weekly, set today's focus
- **Automatic task carry-forward** - Uncompleted tasks move forward until completed
- **Optional coaching** - Pattern detection to help spot overloading or vague goals
- **Optional values & nudges** - Keep priorities visible and aligned with personal values

### Core Workflow

```
Weekly (10-15 min)
    ↓
Daily (5 min) - Appended to weekly note
    ↓
Reflect (2m) - Tasks sync automatically
```

### Skill Structure

The oya skill follows the standard skill structure:
```
.claude/skills/oya/
├── SKILL.md                      # Core workflow and instructions
├── references/
│   ├── config-guide.md          # Configuration options
│   └── future.md                # Future enhancements
└── assets/
    └── templates/
        ├── daily.md             # Daily planning template
        └── weekly.md            # Weekly planning template
```

### Key Files

- **SKILL.md** - Main workflow instructions including onboarding, detection logic, weekly/daily flows, and task state notation
- **references/config-guide.md** - Detailed configuration options for `.claude/oya.md` user config
- **assets/templates/daily.md** - Template for daily planning entries
- **assets/templates/weekly.md** - Template for weekly planning notes

### Configuration

Users configure oya by creating `.claude/oya.md` in their working directory with settings for:
- Name and personal mantra
- Life contexts (home, work, personal, etc.)
- Optional values to track
- Optional personal nudges
- Coaching preferences
- File paths for notes

### Usage Patterns

When `/oya` is invoked:
1. Check if onboarding is needed (no `.claude/oya.md` exists)
2. Get current date and check if weekend
3. Detect what notes exist (weekly note, today's entry)
4. Load user config from `.claude/oya.md`
5. Gather context from previous notes
6. Propose weekly note or daily entry based on what's missing
7. Offer coaching critique if enabled

### Important Implementation Notes

- Always run `date` command to get current date - don't rely on system date
- Preserve task state notation when carrying forward: `[ ]`, `[-]`, `[x]`
- Copy tasks verbatim from previous entries (same wording, same emoji)
- Balance work AND personal tasks in daily entries
- Weekend flow is minimal - one suggestion + encouragement to rest
