---
name: oya
description: Plan and stay on track. Fast. Practical. Intentional.
---

# Oya

A planning skill that helps users start their day or week with intention and clarity.

## Core Workflow

```
┌─────────────────────────────────────────────────────┐
│              WEEKLY (10-15 min)                     │
│   Review last week → Set goals for this week        │
│   File: Mon DD-Fri DD.md                            │
└─────────────────────┬───────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│              DAILY (5 min)                          │
│   Copy tasks from weekly → Set today's focus        │
│   Appended to weekly note                           │
└─────────────────────────────────────────────────────┘
```

## Step 0: Onboarding (First Run Only)

**Detection:** Check if `.claude/oya.md` exists.

| Condition        | Action                   |
| ---------------- | ------------------------ |
| No config exists | Run this onboarding flow |
| Config exists    | Skip to Step 1           |

### Part 1: Welcome & Branding

Display this welcome message:

```
.
            ██████╗  ██╗   ██╗  █████╗
           ██╔═══██╗ ╚██╗ ██╔╝ ██╔══██╗
           ██║   ██║  ╚████╔╝  ███████║
           ██║   ██║   ╚██╔╝   ██╔══██║
           ╚██████╔╝    ██║    ██║  ██║
            ╚═════╝     ╚═╝    ╚═╝  ╚═╝

             🌀 Let's move. Let's go.

     A planning companion for intentional days
```

Then show the origin:

> *Named for the Yoruba goddess of winds and change—Oya clears\n
> what no longer serves, making space for transformation.*

Then explain the workflow:

```
                 ┌─────────────┐
                 │   WEEKLY    │  Set goals for the week
                 │  (10-15m)   │  Review what's ahead
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │    DAILY    │  Pick today's focus
                 │    (5m)     │  From your weekly list
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │  REFLECT    │  What worked? What didn't?
                 │   (2m)      │  Tasks sync automatically
                 └─────────────┘
```

**Key concepts:**
- 🌀 Tasks carry forward automatically until done
- 🌀 Optional coaching helps you spot planning patterns
- 🌀 Optional values & nudges keep priorities visible

---

*Let's set up your planning system...*

### Part 2: Setup Wizard

Use a single AskUserQuestion prompt to gather all setup information at once.

**Prompt:**

```
Let's personalize your planning experience. Answer what you'd like—you can
skip any question and add it later in .claude/oya.md

1. What should I call you?

2. What's your guiding phrase (mantra)?
   Examples: "Give Everything." • "Make it happen." • "One day at a time."

3. What values guide your decisions? (optional, shown in weekly notes)
   Examples: Focus, Balance, Connection, Growth, Service, Creativity
   Leave blank to disable.

4. What life areas do you want to track? (comma-separated)
   Examples: home, work, personal, health, creative

5. How should tasks show their context?
   Options: "hidden" (default) • "[context] - task" • "edit template yourself"

6. Any personal nudges? (optional, shown in daily entries)
   Examples: "If not now, when?" • "Focus on service" • "What would future you thank you for?"
   Leave blank to disable.

7. Enable coaching? (yes/no)
   Coaching helps spot patterns like overloading or vague goals.
```

Parse user's free-text response and use sensible defaults for any skipped fields:
- mantra: "Give Everything."
- contexts: home, work, personal
- context_display: hidden
- coaching: true

**Write Config**

Generate `.claude/oya.md` with user's choices in this format:

```yaml
name: "{user_name}"
mantra: "{chosen_mantra}"

# Optional - only include if user provided values
values:
  enabled: true
  list:
    - {value_1}
    - {value_2}

# Optional - only include if user provided nudges
nudges:
  enabled: true
  list:
    - "{nudge_1}"
    - "{nudge_2}"

contexts:
  - home
  - work
  - personal

context_display: hidden  # options: hidden, prefix, custom

coaching:
  enabled: {true|false}
```

**How to use Oya:**

After setup, explain the daily workflow:

```
How Oya works:

1. Run /oya each day - it creates or updates your notes
2. Edit the notes it proposes - make them yours
3. Come back anytime:
   • /oya         → continue planning
   • /oya critique → get feedback on your notes
```

Show success message:

```
🌀 Setup complete!

Your config has been saved to .claude/oya.md

Run /oya anytime to start planning.
```

**Exit after onboarding** - do not auto-start weekly planning.

---

## Step 1: Detection

1. **Get current date**: Run `date` in terminal - do not rely on system date
2. **Check if weekend**: Saturday/Sunday → Use Weekend Flow
3. **Check what exists**:
   - Does current week's note exist? → If NO: Create weekly note
   - Does today's entry exist in weekly note? → If NO: Add daily entry
4. **Report findings**:
   ```
   "Good morning! Here's what I found:
   - [✓/✗] This week's note (Mon Nth - Fri Nth)
   - [✓/✗] Today's entry (Day, Month Nth)

   Let's set up what's missing..."
   ```

## Step 2: Load Config

Read `.claude/oya.md` (created during onboarding).

See `references/config-guide.md` for configuration options.

**Fallback defaults (if config missing):**
- mantra: "Give Everything."
- contexts: home, work, personal
- paths.base: "planning"
- coaching.enabled: true

## Step 3: Gather Context

Before proposing notes, read:
1. **Previous day's entry** - carry forward uncompleted `[ ]` and `[-]` items verbatim
2. **Last week's note** - unchecked items for carry-forward (if new week)
3. **Monthly goals** - if they exist, use as north star

## Flow A: Weekly Note (FAST approach)

**Propose directly** based on context gathered. Use template from `assets/templates/weekly.md`.

**Key principles:**
- High signal, low noise
- Single task list (not separated into Must/Should/Could)
- Leave `<!-- comments -->` where unsure
- Include tasks from all contexts (home, work, personal)

**After proposing:**
1. User edits the note
2. Offer coaching critique based on config patterns

## Flow B: Daily Entry (FAST approach)

**Propose directly.** Append to weekly note. Use template from `assets/templates/daily.md`.

**Key principles:**
- Copy tasks VERBATIM from weekly list (same wording, same emoji)
- Preserve task state: `[-]` stays `[-]`, `[ ]` stays `[ ]`, `[x]` stays `[x]`
- Only include today's relevant tasks
- Include values nudge from config (if enabled)
- Balance work AND home/personal tasks (2-4 personal items per day)

## Flow C: Weekend Flow

Skip work planning. Instead:
1. Make ONE tailored suggestion (rest, connection, or creative pursuit)
2. End with: "Enjoy your weekend - truly rest, truly connect, truly play."

## Task State Notation

- `[ ]` - Not started → carry forward
- `[-]` - In progress → carry forward
- `[x]` - Completed → don't carry

**Default task emojis:**
- 🔥 - Urgent (time-sensitive)
- ❗ - Important/must do
- ☀️ - Creation/creative work
- 😃 - People-focused
- 🕚 - Carried forward
- 🧠 - Protected thinking time

## Coaching Mode

After user edits their note, check for patterns:

| Pattern         | Challenge                                          |
| --------------- | -------------------------------------------------- |
| Overloaded      | "What can you delegate or defer?"                  |
| Vague goals     | "What exactly would success look like?"            |
| Missing balance | "Where's rest or creative time?"                   |
| Too safe        | "What would this look like if you thought bigger?" |

Only coach if `coaching.enabled: true` in config.

## File Paths

| Type   | Default Path                      |
| ------ | --------------------------------- |
| Base   | `{paths.base}/{Year}/{MM}-{Mon}/` |
| Weekly | `{Mon} {DD}-{Fri} {DD}.md`        |
| Config | `.claude/oya.md`                  |

## Reflection (End of Day)

When user returns in evening or next morning:
1. Ask what went well, what didn't
2. Keep it minimal - bullet points only
3. Append under **Reflections** in that day's entry
4. Sync completed tasks back to weekly list
