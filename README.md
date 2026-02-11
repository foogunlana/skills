# Skills

A collection of skills for [Claude Code](https://claude.ai/code) — productivity tools that extend Claude with structured workflows.

| Skill | Command | What it does |
|-------|---------|--------------|
| [Oya](#oya) | `/oya` | Planning companion — weekly, daily, reflect |
| [Calendar Audit](#calendar-audit) | `/calendar-audit` | Protect deep work — score and rank meetings |
| [Trip Planner](#trip-planner) | `/trip-planner` | Flight recommendations from natural language |

---

# Oya

> *Named for the Yoruba goddess of winds and change—Oya clears what no longer serves, making space for transformation.*

**🌀 Let's move. Let's go.**

A planning companion that helps you start your day or week with intention and clarity.
```
            ██████╗  ██╗   ██╗  █████╗
           ██╔═══██╗ ╚██╗ ██╔╝ ██╔══██╗
           ██║   ██║  ╚████╔╝  ███████║
           ██║   ██║   ╚██╔╝   ██╔══██║
           ╚██████╔╝    ██║    ██║  ██║
            ╚═════╝     ╚═╝    ╚═╝  ╚═╝

             🌀 Let's move. Let's go.

     A planning companion for intentional days
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

---

# Trip Planner

> *Every trip starts with a destination and a mess of unknowns. Trip Planner fills in the blanks so you don't have to.*

**Assume first. Show your work. Book the flight.**

A flight recommendation skill that turns natural language into structured options with direct booking links.

```
████████╗██████╗ ██╗██████╗
╚══██╔══╝██╔══██╗██║██╔══██╗
   ██║   ██████╔╝██║██████╔╝
   ██║   ██╔══██╗██║██╔═══╝
   ██║   ██║  ██║██║██║
   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝

██████╗ ██╗      █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔══██╗██║     ██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ███████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

       Assume first. Show your work. Book the flight.
```

## How It Works

```
           ┌──────────────────┐
           │   DESCRIBE TRIP  │  "Flights to Tokyo next month"
           │   (10 seconds)   │  Natural language, any detail level
           └────────┬─────────┘
                    │
                    v
           ┌──────────────────┐
           │  ASSUME & SHOW   │  Fill every gap with smart defaults
           │   (instant)      │  Show assumption card for review
           └────────┬─────────┘
                    │
                    v
           ┌──────────────────┐
           │  SEARCH & RANK   │  WebSearch + booking URLs
           │   (30 seconds)   │  Best Value / Cheapest / Fastest
           └────────┬─────────┘
                    │
                    v
           ┌──────────────────┐
           │  CORRECT & BOOK  │  Adjust anything, re-search
           │   (you decide)   │  Direct booking links provided
           └──────────────────┘
```

## What is Trip Planner?

Trip Planner is a skill for [Claude Code](https://claude.ai/code) that provides assumption-first flight search. It helps you:

- **Find flights fast** - Just name a destination, everything else is assumed
- **See every assumption** - Transparent table shows what was assumed and why
- **Get structured options** - Best Value, Cheapest, and Fastest categories
- **Book directly** - Skyscanner/Google Flights links for every option
- **Plan multi-city** - "London → Paris → Rome → London" just works

## Getting Started

### Installation

1. Install Claude Code if you haven't already (see [claude.ai/code](https://claude.ai/code))
2. Clone this repository or download the trip-planner skill
3. The skill is located in `.claude/skills/trip-planner/` and will be automatically loaded by Claude Code

### First Use

Simply run `/trip-planner` in Claude Code or describe a trip naturally:

1. **Describe** - "I need flights to Barcelona in April"
2. **Review** - See the assumption card with every inferred detail
3. **Search** - Flights found and ranked automatically
4. **Setup** - Optionally save preferences for faster searches next time

After setup, just describe any trip and Trip Planner handles the rest.

## The Flows

### Describe a Trip

Say anything natural:
- "Flights to Tokyo next month"
- "London to Paris, March 15-18, 2 adults"
- "Cheapest flights to Barcelona in April"
- "London → Paris → Rome → London in April"

### Assumption Card

Every search shows what was assumed:

| Field | Value | Source |
|-------|-------|--------|
| Destination | Tokyo (NRT/HND) | You said |
| Origin | London (LHR) | Config |
| Dates | Mar 10 - Mar 17 | "next month" + 7 days |
| Passengers | 1 adult | Default |
| Class | Economy | Config |

Correct anything that's wrong — the search re-runs automatically.

### Flight Recommendations

Results come in three categories:
- **Best Value** - Best balance of price, duration, and convenience
- **Cheapest** - Lowest price regardless of stops or timing
- **Fastest** - Shortest total travel time

Each option includes a direct booking link.

### Multi-City

Multi-city trips are first-class:
- Decomposed into individual legs
- Each leg searched independently
- Combined itinerary overview with total cost
- Per-leg booking links

## Configuration

Your preferences are stored in `.claude/trip-planner.md` in your working directory.

### Basic Settings

```yaml
home_airport: "LHR"
preferences:
  class: "economy"
  budget: "flexible"
  currency: "GBP"
```

### Full Settings

```yaml
name: "Your Name"
home_airport: "LHR"
preferences:
  class: "economy"
  budget: "flexible"
  currency: "GBP"
  stops: "any"
  preferred_airlines:
    - "British Airways"
  time_preference: "any"
platform:
  primary: "skyscanner"
```

See `.claude/skills/trip-planner/references/config-guide.md` for full configuration options.

## Commands

- `/trip-planner` - Start a new flight search

## Repository Structure

```
.claude/skills/trip-planner/
├── SKILL.md                      # Core workflow and instructions
├── references/
│   ├── branding.md              # Visual assets and branding
│   ├── config-guide.md          # Configuration options
│   └── future.md                # Future enhancements
└── assets/
    └── templates/
        └── trip-recommendation.md  # Output template
```

## Philosophy

Trip Planner is designed around one principle:

**Assume everything, show everything.** The user corrects what's wrong — not fills in what's missing. A destination is all you need. Everything else has a sensible default, and every default is visible.

---

## License

See the license information in individual skill directories.
