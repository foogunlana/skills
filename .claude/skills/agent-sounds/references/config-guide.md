# Agent Sounds Config Guide

Agent Sounds reads configuration from `.claude/agent-sounds.json` (searching upward from the current working directory). If no config exists, built-in defaults are used.

## Minimal Config (Recommended)

```json
{
  "enabled": true,
  "cooldown_ms": 1200,
  "hooks": {
    "plan.done": "ding",
    "task.done": "success",
    "run.done": "success",
    "error": "error",
    "waiting": "ping"
  },
  "sounds": {
    "ding": "system:Glass",
    "success": "system:Hero",
    "error": "system:Basso",
    "ping": "system:Ping"
  }
}
```

## Fields

- `enabled` (boolean, default: `true`)
  - Master switch. If `false`, `emit` is a no-op (exits 0).
- `cooldown_ms` (number, default: `1200`)
  - Debounce per hook to avoid rapid repeated chimes.
- `hooks` (object: hook -> sound key/spec)
  - Map hook names (e.g. `plan.done`) to either:
    - A key in `sounds` (e.g. `"ding"`)
    - A sound spec directly (e.g. `"system:Glass"` or `"bell"`)
- `sounds` (object: key -> sound spec)
  - Named sound specs referenced by `hooks`.

## Sound Specs

Agent Sounds supports these sound spec formats:

- `system:<Name>`
  - macOS: resolves to `/System/Library/Sounds/<Name>.aiff` if present
  - Other OS: falls back to `bell` unless you use `file:` explicitly
- `file:/absolute/or/relative/path/to/sound.(aiff|wav|mp3)`
  - Relative paths are resolved from the directory containing the config file.
- `bell`
  - Terminal bell (`\a`) fallback.
- `say:<text>`
  - macOS only: uses `say "<text>"` (fallback to `bell` if unavailable).

### Convenience

- If you set a sound spec to just `Glass` (no prefix), it is treated as `system:Glass`.

## Example: Quiet Mode

```json
{
  "enabled": true,
  "cooldown_ms": 2000,
  "hooks": {
    "plan.done": "system:Glass",
    "error": "system:Basso"
  }
}
```

## Example: Custom File For The Oven Ding

```json
{
  "enabled": true,
  "hooks": { "plan.done": "ding" },
  "sounds": { "ding": "file:assets/oven-ding.wav" }
}
```

