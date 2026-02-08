# Calendar Setup Guide

How to get your calendar data into Calendar Audit. Options are ordered by friction — start with Tier 1 (zero setup) and upgrade when you want automation.

---

## Tier 1 — Zero Setup (always available)

No tools to install. Works immediately.

### Screenshot

Take a screenshot of your calendar week view and paste it into the conversation.

**Works with:** Any calendar app (Google, Apple, Outlook, Fantastical, etc.)

**How:**
1. Open your calendar in week view
2. Take a screenshot (macOS: `Cmd+Shift+4`, Windows: `Win+Shift+S`)
3. Paste the image when Calendar Audit asks for your calendar

**Tips:**
- Week view works best — day view misses context, month view is too small
- Make sure event titles are readable
- If your week is split across two screens, paste both images

**Limitations:** Manual each time. Claude extracts events via vision — occasional misreads on small text.

---

### Copy-Paste

Copy your schedule as text and paste it.

**Works with:** Any calendar app that lets you select and copy events.

**How:**
1. Select your week's events in your calendar app
2. Copy as text (`Cmd+C` / `Ctrl+C`)
3. Paste when Calendar Audit asks for your calendar

**Format examples Claude can parse:**

```
Monday 9 Feb
9:00 - 9:30  Team standup
10:00 - 11:00  Design review
14:00 - 14:30  1:1 with Sarah

Tuesday 10 Feb
9:00 - 9:30  Team standup
11:00 - 12:00  Sprint planning
```

Or a simple list:

```
Mon: Standup 9-9:30, Design review 10-11, 1:1 Sarah 2-2:30
Tue: Standup 9-9:30, Sprint planning 11-12
```

**Limitations:** Manual each time. Requires your calendar app to support text copy.

---

### ICS File

Export your calendar as an `.ics` file and provide the path.

**Works with:** Google Calendar, Apple Calendar, Outlook, any CalDAV-compatible app.

**How to export:**

**Google Calendar:**
1. Go to [calendar.google.com](https://calendar.google.com)
2. Settings (gear icon) → Import & export → Export
3. Downloads a `.zip` containing `.ics` files
4. Unzip and provide the path to the relevant `.ics` file

**Apple Calendar:**
1. File → Export → Export...
2. Choose location, save as `.ics`
3. Provide the file path

**Outlook (Desktop):**
1. File → Save Calendar
2. Choose date range, save as `.ics`
3. Provide the file path

**Outlook (Web):**
1. Settings → View all Outlook settings → Calendar → Shared calendars
2. Publish a calendar → Get ICS link
3. Provide the URL or download the file

**Limitations:** Manual export each time. Some exports include all events (not just the current week) — Claude will filter by date.

---

## Tier 2 — One-Time Setup (then automated)

Install once, then Calendar Audit pulls your events automatically.

### Google Calendar MCP

**Best for:** Google Calendar users who want fully automated audits.

**Setup:**

1. Add to your MCP config (`.mcp.json` or Claude settings):

```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "npx",
      "args": ["-y", "@cocal/google-calendar-mcp"]
    }
  }
}
```

2. Restart Claude Code
3. On first use, complete the OAuth flow in your browser
4. Set in your calendar-audit config:

```yaml
calendar:
  tool: "google-calendar-mcp"
  primary_id: "primary"
```

**Commands used:** `list-events`, `list-calendars`, `get-freebusy`

**Multiple calendars:** Set `primary_id` to a specific calendar ID, or use `"primary"` for your main calendar.

---

### Apple Calendar MCP (CheICalMCP)

**Best for:** macOS users with iCloud, Google, or Exchange calendars synced to Apple Calendar.

**Setup:**

1. Download the CheICalMCP binary from the releases page
2. Place it in `~/bin/` (or any directory):
   ```bash
   chmod +x ~/bin/CheICalMCP
   ```
3. Add to Claude Code:
   ```bash
   claude mcp add --scope user --transport stdio che-ical-mcp -- ~/bin/CheICalMCP
   ```
4. Set in your calendar-audit config:

```yaml
calendar:
  tool: "apple-calendar-mcp"
```

**Works with:** Any calendar synced to macOS Calendar app (iCloud, Google, Exchange, CalDAV).

**Note:** Requires macOS. The binary reads from the local Calendar database.

---

### icalBuddy / icalPal

**Best for:** macOS CLI users who prefer shell tools.

**Setup:**

```bash
brew install icalbuddy
```

Or for the newer alternative:

```bash
brew install icalpal
```

**Verify:** `icalBuddy -f "" eventsFrom:today to:+5d`

Set in your calendar-audit config:

```yaml
calendar:
  tool: "icalbuddy"
```

**Commands Calendar Audit will run:**
- `icalBuddy -f "" -nc -nrd -df "%Y-%m-%d" -tf "%H:%M" eventsFrom:today to:+5d` — list events for the week
- `icalBuddy -f "" calendars` — list available calendars

**Note:** macOS only. Reads from the same Calendar database as Apple Calendar.

---

## Tier 3 — More Setup

These require more configuration but offer additional flexibility.

### gcalcli

**Best for:** Google Calendar power users comfortable with GCP setup.

**Setup:**

1. Install:
   ```bash
   pip install gcalcli
   ```

2. Create a GCP project:
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create a new project
   - Enable the Google Calendar API
   - Create OAuth 2.0 credentials (Desktop app)
   - Download the credentials JSON

3. Authenticate:
   ```bash
   gcalcli --client-id=YOUR_CLIENT_ID init
   ```

4. Verify:
   ```bash
   gcalcli agenda
   ```

5. Set in your calendar-audit config:

```yaml
calendar:
  tool: "gcalcli"
```

**Commands Calendar Audit will run:**
- `gcalcli agenda "$(date +%Y-%m-%d)" "$(date -v+5d +%Y-%m-%d)" --details all --tsv` — list events for the week

---

### Outlook

**Best for:** Microsoft 365 / Outlook users.

**Option A — Sync to Mac Calendar (recommended):**
1. Open macOS System Settings → Internet Accounts → Add Microsoft Exchange
2. Sign in with your work account
3. Enable Calendar sync
4. Use Apple Calendar MCP or icalBuddy (Tier 2) to access events

**Option B — Manual export:**
1. Use the ICS file method from Tier 1
2. Export weekly from Outlook

**Option C — Microsoft Graph API (advanced):**
1. Register an app in Azure AD
2. Grant Calendar.Read permission
3. Use the REST API or PowerShell to pull events
4. This is the highest friction option — only recommended if you need full automation and can't sync to Mac Calendar

---

## Choosing a Tool

| If you... | Use |
|-----------|-----|
| Want to try Calendar Audit right now | Screenshot |
| Use Google Calendar | Google Calendar MCP |
| Use macOS with any calendar | Apple Calendar MCP or icalBuddy |
| Use Outlook on Mac | Sync to Mac Calendar → Apple Calendar MCP |
| Use Outlook on Windows | ICS file export |
| Want maximum control | gcalcli |
| Don't want to install anything | Screenshot or Copy-paste |

---

## Config Reference

In `.claude/calendar-audit.md`:

```yaml
calendar:
  tool: "screenshot"  # screenshot | copy-paste | ics-file | google-calendar-mcp | apple-calendar-mcp | icalbuddy | gcalcli | manual
  primary_id: "primary"  # calendar ID (for MCP/gcalcli tools)
  ics_path: null  # path to .ics file (for ics-file tool)
```
