# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains skills for Claude Code — productivity tools that extend Claude with structured workflows.

## Skills

| Skill | Location | Command | Purpose |
|-------|----------|---------|---------|
| Oya | `.claude/skills/oya/` | `/oya` | Planning companion — weekly, daily, reflect |
| Calendar Audit | `.claude/skills/calendar-audit/` | `/calendar-audit` | Protect deep work — score and rank meetings |
| Trip Planner | `.claude/skills/trip-planner/` | `/trip-planner` | Flight recommendations from natural language |

---

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

```
.claude/skills/oya/
├── SKILL.md                      # Core workflow and instructions
├── references/
│   ├── branding.md              # Visual assets and branding
│   ├── config-guide.md          # Configuration options
│   └── future.md                # Future enhancements
└── assets/
    └── templates/
        ├── daily.md             # Daily planning template
        └── weekly.md            # Weekly planning template
```

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

---

## Trip Planner Skill

**Location:** `.claude/skills/trip-planner/`

Trip Planner turns natural language into flight recommendations — assumes everything, shows everything.

- **Assumption-first** - Only needs a destination. Fills in dates, class, budget, passengers from config or smart defaults
- **Instant search** - WebSearch for pricing + direct Skyscanner booking links
- **Multi-city** - "London → Paris → Rome → London" decomposes into per-leg searches
- **Corrections loop** - User adjusts assumptions, re-search runs automatically

### Core Workflow

```
Describe trip → Assume & show → Search & rank → Correct & book
```

### Skill Structure

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

### Configuration

Users configure trip-planner by creating `.claude/trip-planner.md` in their working directory with:
- Home airport
- Preferred class, budget, currency
- Stop preferences
- Preferred airlines
- Booking platform (Skyscanner, Google Flights, Kayak)

### Usage Patterns

When `/trip-planner` is invoked:
1. Check if onboarding is needed (no `.claude/trip-planner.md` exists)
2. Parse destination and constraints from natural language
3. Load config for defaults
4. Run Assumption Engine (user input > config > context inference > smart defaults)
5. Show assumption card for review
6. Search with WebSearch + construct booking URLs
7. Present 3 categories: Best Value, Cheapest, Fastest
8. Corrections loop until user is satisfied

### Important Implementation Notes

- Always run `date` command to get current date
- Only hard requirement is destination — everything else has a default
- Show assumption card before every search (every assumption visible with source)
- WebFetch on booking URLs is optional — graceful fallback to WebSearch data
- Multi-city trips: search each leg independently, present combined itinerary
