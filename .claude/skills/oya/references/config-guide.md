# Configuration Guide

Create `.claude/oya.md` in your project to customize the oya skill.

## Full Configuration Example

```yaml
name: "Your Name"
mantra: "Give Everything."

values:
  - Connection & Contribution
  - Focus & Balance

nudges:
  - "If not now, when?"
  - "Focus on service"
  - "What would future you thank you for?"

contexts:
  - home
  - work
  - personal

emojis:
  urgent: "🔥"
  important: "❗"
  creative: "☀️"
  people: "😃"
  carried: "🕚"
  protected: "🧠"

paths:
  base: "Planning"
  weekly: "{year}/{month}/{mon} - {fri}.md"

coaching:
  enabled: true
  patterns:
    - name: "Overloaded"
      prompt: "What can you delegate or defer?"
    - name: "Vague goals"
      prompt: "What exactly would success look like?"
    - name: "Missing balance"
      prompt: "Where's Sharpen the Saw time?"
```

## Configuration Fields

### Identity

| Field | Description | Default |
|-------|-------------|---------|
| `name` | Your name for daily entries | "" |
| `mantra` | Displayed at top of notes | "Give Everything." |

### Values & Nudges

| Field | Description |
|-------|-------------|
| `values` | List of core values (used in coaching) |
| `nudges` | Random lines surfaced in daily entries |

### Contexts

Contexts organize your tasks. Default: `home`, `work`, `personal`.

Daily entries will have a "Todo" section for each context.

### Emojis

Customize task type indicators:

| Key | Meaning | Default |
|-----|---------|---------|
| `urgent` | Time-sensitive | 🔥 |
| `important` | Must do | ❗ |
| `creative` | Creation work | ☀️ |
| `people` | People-focused | 😃 |
| `carried` | Carried forward | 🕚 |
| `protected` | Thinking time | 🧠 |

### Paths

| Field | Description | Default |
|-------|-------------|---------|
| `paths.base` | Root folder for planning notes | "Planning" |
| `paths.weekly` | Weekly note path pattern | "{year}/{month}/{mon} - {fri}.md" |

**Path variables:**
- `{year}` - 4-digit year (2025)
- `{month}` - Month name with number (01-Jan)
- `{mon} - {fri}` - Week span (Jan 19th - Jan 23rd)

### Coaching

| Field | Description | Default |
|-------|-------------|---------|
| `coaching.enabled` | Enable coaching prompts | true |
| `coaching.patterns` | Custom coaching patterns | (see defaults) |

**Default coaching patterns:**
- Overloaded → "What can you delegate or defer?"
- Vague goals → "What exactly would success look like?"
- Missing balance → "Where's rest or creative time?"

## Minimal Configuration

For most users, this is enough:

```yaml
name: "Your Name"
mantra: "Make it happen."
```

Everything else uses sensible defaults.
