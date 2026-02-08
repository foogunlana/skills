# Configuration Guide

Create `.claude/calendar-audit.md` in your project to customize the calendar-audit skill.

## Full Configuration Example

```yaml
name: "Your Name"
role: "CTO"
direct_reports: 6

focus_ratio: 60  # Target percentage of work week as focus time (60 = 60% focus / 40% meetings)
work_hours: 40   # Hours in your work week
min_daily_focus: 4  # Minimum contiguous hours of uninterrupted deep work per day

maker_days:
  - Tuesday
  - Thursday

priorities:
  - "Ship ML project"
  - "Write technical content"
  - "Complete Fast AI course"

calendar:
  tool: "google-calendar-mcp"  # screenshot | copy-paste | ics-file | google-calendar-mcp | apple-calendar-mcp | icalbuddy | gcalcli | manual
  primary_id: "primary"
  ics_path: null  # path to .ics file (for ics-file tool only)

framework:
  name: "5-dimension"  # 5-dimension | eisenhower | raci | value-effort | custom

scoring:
  overrides:
    - meeting: "Abdul 1:1"
      zone: "green"
      reason: "Key direct report, always keep"
    - meeting: "Virtual Hangout"
      zone: "red"
      reason: "Social, skip when busy"

meeting_memory: ".claude/modules/meeting-scores.md"
```

## Configuration Fields

### Identity & Role

| Field | Description | Default |
|-------|-------------|---------|
| `name` | Your name | "" |
| `role` | Your role title | "Engineering Leader" |
| `direct_reports` | Number of direct reports (affects 1:1 scoring) | 0 |

### Focus Targets

| Field | Description | Default |
|-------|-------------|---------|
| `focus_ratio` | Target % of work week as focus time | 60 |
| `work_hours` | Total hours in work week | 40 |
| `min_daily_focus` | Minimum contiguous hours of uninterrupted deep work per day | 4 |
| `maker_days` | Preferred days for fewer meetings | ["Tuesday", "Thursday"] |

**Recommended ratios by role:**

| Role | Focus | Meetings | Notes |
|------|-------|----------|-------|
| IC Engineer | 70-80% | 20-30% | Mostly deep work |
| Tech Lead | 60-70% | 30-40% | Mix of building and coordinating |
| Player-Coach / EM | 50-60% | 40-50% | Balance hands-on with people |
| Director+ | 40-50% | 50-60% | More coordination, less building |
| Founder / CTO (small) | 50-60% | 40-50% | Must protect building time |

### Priorities

List your top 3-5 priorities that require deep work this quarter. These are used to estimate deep work needs and propose calendar slots.

```yaml
priorities:
  - "Ship ML project"
  - "Write weekly blog posts"
  - "Complete course"
```

### Calendar Tool

| Field | Description | Default |
|-------|-------------|---------|
| `calendar.tool` | How to access your calendar | "screenshot" |
| `calendar.primary_id` | Calendar ID for MCP/CLI tools | "primary" |
| `calendar.ics_path` | Path to .ics file (ics-file tool only) | null |

**Supported tools:**

| Tool | Setup | Automation | Platform |
|------|-------|------------|----------|
| `screenshot` | None | Manual each time | Any |
| `copy-paste` | None | Manual each time | Any |
| `ics-file` | None | Manual export each time | Any |
| `google-calendar-mcp` | One-time OAuth | Fully automated | Any |
| `apple-calendar-mcp` | One-time binary install | Fully automated | macOS |
| `icalbuddy` | `brew install` | Fully automated | macOS |
| `gcalcli` | GCP project + OAuth | Fully automated | Any |
| `manual` | None | User provides list each time | Any |

See `references/calendar-setup.md` for detailed setup instructions.

### Decision Framework

| Field | Description | Default |
|-------|-------------|---------|
| `framework.name` | Which scoring model to use | "5-dimension" |

**Built-in frameworks:**

| Framework | Dimensions | Speed | Best For |
|-----------|-----------|-------|----------|
| `5-dimension` | 5 | Medium | Comprehensive weekly audits |
| `eisenhower` | 2 | Fast | Quick decisions, simplicity |
| `raci` | 1 (role) | Fast | Cutting "Informed" meetings |
| `value-effort` | 2 | Fast | ROI thinkers, identifying traps |
| `custom` | User-defined | Varies | Power users |

See `references/frameworks.md` for complete scoring rules.

**Custom framework config:**

```yaml
framework:
  name: "custom"
  custom:
    dimensions:
      - name: "Dimension Name"
        scale: [1, 3]
        labels:
          1: "Best case"
          3: "Worst case"
    zones:
      green: [min, max]
      yellow: [min, max]
      orange: [min, max]
      red: [min, max]
```

### Scoring Overrides

Pre-set overrides for meetings you always want to keep or skip, regardless of score:

```yaml
scoring:
  overrides:
    - meeting: "Team 1:1"
      zone: "green"
      reason: "Always keep direct report 1:1s"
    - meeting: "Company All-Hands"
      zone: "orange"
      reason: "Attend monthly, skip other weeks"
```

### Meeting Memory

| Field | Description | Default |
|-------|-------------|---------|
| `meeting_memory` | Path to meeting scores history | ".claude/modules/meeting-scores.md" |

## Minimal Configuration

For most users, this is enough:

```yaml
name: "Your Name"
role: "Engineering Manager"
```

Everything else uses sensible defaults (screenshot input, 5-dimension framework, 60/40 ratio).
