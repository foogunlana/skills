# Oya

> *Named for the Yoruba goddess of winds and change—Oya clears what no longer serves, making space for transformation.*

**🌀 Let's move. Let's go.**

A planning companion that helps you start your day or week with intention and clarity.

```
 ┌───┐  ┐   ┌  ┌───┐
 │   │   \ /   │   │
 │   │    │    ├───┤
 │   │    │    │   │
 └───┘    ┴    ┴   ┴
```

## How It Works

```
     ┌─────────────┐
     │   WEEKLY    │  Set goals for the week
     │  (10-15m)   │  Review what's ahead
     └──────┬──────┘
            |
            v
     ┌─────────────┐
     │    DAILY    │  Pick today's focus
     │    (5m)     │  From your weekly list
     └──────┬──────┘
            |
            v
     ┌─────────────┐
     │  REFLECT    │  What worked? What didn't?
     │   (2m)      │  Tasks sync automatically
     └─────────────┘
```

## What is Oya?

Oya is a skill for [Claude Code](https://claude.ai/code) that provides fast, practical, intentional planning. It helps you:

- **Plan your week** (10-15 min) - Review last week, set goals for this week
- **Plan your day** (5 min) - Pick today's focus from your weekly list
- **Stay on track** - Tasks carry forward automatically until done
- **Get coaching** (optional) - Spot patterns like overloading or vague goals
- **Align with values** (optional) - Keep priorities visible with personal values and nudges

## Getting Started

### Installation

1. Install Claude Code if you haven't already (see [claude.ai/code](https://claude.ai/code))
2. Clone this repository or download the oya skill
3. The skill is located in `.claude/skills/oya/` and will be automatically loaded by Claude Code

### First Use

Simply run `/oya` in Claude Code and you'll be guided through:

1. **Welcome & Setup** - Learn how Oya works and personalize your experience
2. **Configuration** - Set your name, mantra, life areas, values, and preferences
3. **Ready to Plan** - Your config is saved to `.claude/oya.md` in your working directory

After setup, run `/oya` anytime to start planning.

## The Flows

### Weekly Planning (10-15 min)

Creates a weekly note with:
- Review of last week's accomplishments
- Goals and tasks for the upcoming week
- Tasks from all life areas (work, home, personal, etc.)

### Daily Planning (5 min)

Appends a daily entry to your weekly note with:
- Tasks copied from your weekly list (only today's relevant items)
- Focus areas for the day
- Optional values reminder to keep priorities aligned

### Task Carry-Forward

Tasks automatically move forward until completed:
- `[ ]` Not started → carries forward
- `[-]` In progress → carries forward
- `[x]` Completed → doesn't carry forward

### Weekend Flow

On weekends, Oya keeps it minimal:
- One tailored suggestion (rest, connection, or creative pursuit)
- Encouragement to truly rest, connect, and play

## Configuration

Your personal configuration is stored in `.claude/oya.md` in your working directory.

### Basic Settings

```yaml
name: "Your Name"
mantra: "Your guiding phrase"
contexts:
  - home
  - work
  - personal
coaching:
  enabled: true
```

### Optional Features

**Values** - Displayed in weekly notes to keep priorities visible:
```yaml
values:
  enabled: true
  list:
    - Focus
    - Balance
    - Connection
```

**Nudges** - Personal reminders shown in daily entries:
```yaml
nudges:
  enabled: true
  list:
    - "If not now, when?"
    - "Focus on service"
```

**Custom Paths** - Change where notes are stored:
```yaml
paths:
  base: "planning"  # Default location
```

See `.claude/skills/oya/references/config-guide.md` for full configuration options.

## Commands

- `/oya` - Start planning (creates weekly or daily notes as needed)
- `/oya critique` - Get coaching feedback on your current plans

## Repository Structure

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

## Philosophy

Oya is designed around three principles:

1. **Fast** - Quick planning that respects your time
2. **Practical** - Focus on what actually matters today
3. **Intentional** - Start with clarity, move with purpose

The goal isn't perfect plans—it's consistent momentum. Plans change, and that's okay. What matters is starting each day with intention and adjusting as you go.

## License

See the license information in `.claude/skills/oya/SKILL.md`.
