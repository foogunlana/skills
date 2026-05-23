---
name: disk-cleanup
description: Scan macOS disk for space hogs, propose cleanup actions, and execute approved cleanups with before/after reporting. Use when the user asks to clean up disk space, free up storage, check what's using disk space, or says "disk cleanup", "clean up my mac", "free up space", "what's taking up space".
---

# Disk Cleanup

Scan, propose, clean, report. Always follow the three phases in order.

## Phase 1: Scan & Report

Run scans directly from the main thread using multiple parallel Bash calls in a single message. Do NOT use backgrounded subagents for scans — they often get Bash permission denied.

**Do NOT use `du -sh ~`** — it traverses the entire home directory and frequently hangs on macOS permission-denied paths.

Launch these scan commands in parallel (single message, multiple Bash tool calls):

1. **Disk overview**: `diskutil info / | grep -E "Free|Available|Used|Total"` + `du -sh ~/Library ~/code ~/Documents ~/.cache ~/.nvm ~/.cargo ~/.rustup ~/.docker ~/Downloads ~/.local ~/go ~/.rvm 2>/dev/null | sort -hr`
2. **Tier 1 caches**: All Tier 1 scan commands from [macos-cleanup-targets.md](references/macos-cleanup-targets.md)
3. **Tier 2 targets**: Docker, nvm versions, pyenv versions, Downloads top 20, Xcode
4. **Tier 1.5 sandboxed downloads**: Scan all Containers for hidden app downloads (see reference)
5. **Electron app internal caches**: `bash -c 'find ~/Library/Application\ Support -maxdepth 2 -name "Cache" -exec du -sh {} \; 2>/dev/null | sort -hr | head -15'` and same for `Service Worker`, `CachedData`, `CachedExtensionVSIXs`
6. **Applications**: `bash -c 'du -sh /Applications/*.app 2>/dev/null | sort -hr | head -20'`

Present a summary table:
- Disk total and free space (from `diskutil`)
- Top space consumers with sizes
- Tier 1 (safe caches) total reclaimable
- Tier 1.5 (sandboxed app downloads) findings
- Electron app internal caches total
- Tier 2 items worth investigating

End with: **"Estimated reclaimable: ~X GB. Want me to proceed with the safe cleanups, or review the full list first?"**

## Phase 2: Propose & Confirm

Based on what the scan found (skip targets that are absent or <10 MB), present numbered cleanup actions grouped by risk:

```
## Safe cleanups (Tier 1) — ~X GB
1. UV cache (X GB)
2. npm cache (X MB)
...

## Review recommended (Tier 2) — ~X GB
N. Docker images (X GB) — removes all unused images
N+1. Old Node v10, v16 (X MB) — keeps v18, v22
...
```

Wait for user approval before executing anything. User may say "all", specific numbers, or "safe only".

## Phase 3: Execute & Report

1. Record the starting free space: `df -h / | tail -1 | awk '{print $4}'`
2. Run approved cleanup commands in parallel where independent (see reference for commands)
3. Record the ending free space: `df -h / | tail -1 | awk '{print $4}'`
4. Present final report:

```
## Cleanup Complete

| Action | Freed |
|--------|-------|
| UV cache | 4.4 GB |
| npm cache | 891 MB |
| ... | ... |
| **Total freed** | **X GB** |

Free space: X GB -> Y GB
```

## Gotchas

### Use `df -h /System/Volumes/Data` not `df -h /`
`df -h /` shows the sealed system volume (`/dev/disk3s1s1`) which is only ~10 GB. The actual user data lives on `/dev/disk3s5` mounted at `/System/Volumes/Data`. Always use `df -h /System/Volumes/Data` for real used/available numbers.

### APFS free space fluctuates
APFS reports "available" conservatively due to purgeable space and snapshots. After deleting 20 GB, `df` might only show 15 GB freed. This is normal — the space is reclaimed but APFS accounting is lazy. Don't worry if numbers don't add up exactly.

### `du -sh ~` hangs on macOS
Never use it. macOS denies access to many `~/Library` subdirectories, causing `du` to stall indefinitely. Use `df -h /System/Volumes/Data` for disk totals and targeted `du` for specific directories.

### macOS "Documents" category is misleading
The Storage settings "Documents" category (often 30-40 GB) does NOT correspond to `~/Documents` (often only 1-2 GB). macOS classifies app data, databases, and files across `~/Library/Application Support`, containers, etc. as "Documents". Always scan `~/Library/Application Support` — that's where the real bulk is.

### macOS "System Data" is mostly ~/Library
The 90+ GB "System Data" category is largely `~/Library` (Containers, Application Support, Caches). Breaking down `~/Library` subdirectories is the key to understanding this number.

### Library/Containers sizes are inflated by hardlinks
macOS sandboxed apps (Slack, WhatsApp, Excel, etc.) each get hardlinks to `~/Desktop`, `~/Music`, `~/Downloads`, `~/Pictures` inside their container. These show up as ~903 MB, ~215 MB, ~53 MB, ~4.4 MB respectively in **every** container — but they're the same data on disk, not duplicates. When scanning Containers:
- **Ignore** the Desktop/, Music/, Downloads/, Pictures/ subdirs (hardlinks to real home folders)
- **Drill into** `Data/Library/` and app-specific dirs for actual unique data
- **Check `Data/Downloads/`** separately — sandboxed apps like Slack store files downloaded *through the app* here, which can grow large (e.g. Slack accumulated 5.6 GB)

### Sandboxed app downloads are hidden space hogs
Apps like Slack store downloaded files in `~/Library/Containers/<bundle-id>/Data/Downloads/`. These don't show up in `~/Downloads` and are easy to miss. Scan with:
```bash
bash -c 'for d in ~/Library/Containers/*/; do size=$(du -sh "$d/Data/Downloads" 2>/dev/null | cut -f1); [ -n "$size" ] && [ "$size" != "0B" ] && echo "$size\t$(basename $d)"; done | sort -hr | head -10'
```

### Electron apps hide GB of caches inside Application Support
Every Electron app (Claude, Slack, Discord, VS Code, Cursor, Arc, etc.) stores `Cache/`, `Service Worker/`, `Code Cache/`, `CachedData/`, `CachedExtensionVSIXs/`, and `GPUCache/` inside `~/Library/Application Support/<AppName>/`. These are invisible to the user but can total 5-10 GB across all apps. Service Workers are the worst offenders (Superhuman had 1.5 GB, Comet 1 GB). All regenerate on next app launch. Scan with:
```bash
bash -c 'find ~/Library/Application\ Support -maxdepth 2 -name "Cache" -exec du -sh {} \; 2>/dev/null | sort -hr | head -15'
bash -c 'find ~/Library/Application\ Support -maxdepth 3 -name "Service Worker" -exec du -sh {} \; 2>/dev/null | sort -hr | head -10'
bash -c 'find ~/Library/Application\ Support -maxdepth 2 \( -name "CachedData" -o -name "CachedExtensionVSIXs" \) -exec du -sh {} \; 2>/dev/null | sort -hr'
```

### When uninstalling apps, always clean up leftover data
Moving an app to Trash only removes the `.app` bundle. The real bulk lives in up to 4 locations:
1. `~/Library/Application Support/<AppName>/` — app data, caches, databases (often 1-3 GB)
2. `~/Library/Caches/<bundle-id>/` — HTTP and update caches
3. `~/Library/Containers/<bundle-id>/` — sandboxed app data
4. `~/.<appname>` or `~/.config/<appname>` — home directory config/extensions (e.g. `~/.windsurf` was 950 MB)

After trashing an app, scan all 4 locations and offer to remove them. The leftover data is often larger than the app itself.

### Clearing `com.apple.mediaanalysisd` can cause other apps to reset
Deleting `~/Library/Containers/com.apple.mediaanalysisd/Data` (Apple's photo/video ML cache, often 5-15 GB) can trigger APFS purgeable space reclamation and sandbox re-evaluation on reboot. This has been observed to cause Electron apps (e.g. ChatGPT Atlas) to lose their local state — tabs, profiles, conversation cache — because macOS reclaims their purgeable data during the restart maintenance pass, and the app interprets the missing data as corruption and resets.

**Mitigation:** After clearing mediaanalysisd (or any large cleanup that frees 10+ GB), before rebooting:
1. Quit important Electron apps (ChatGPT, Arc, Slack, etc.) gracefully
2. Relaunch them so they rebuild their caches while the system is stable
3. Quit them again gracefully
4. *Then* reboot

This gives apps a chance to re-persist their state before macOS runs post-reboot maintenance. Always warn the user about this before clearing mediaanalysisd.

### Use `diskutil info /` for accurate free space, not `df`
`df -h /` shows the sealed system volume which can report misleading numbers. Use `diskutil info / | grep -E "Free|Available|Used|Total"` for the real Container Free Space. For quick checks during cleanup, `df -h /` is fine for relative before/after comparisons.

## Reference

See [references/macos-cleanup-targets.md](references/macos-cleanup-targets.md) for the full list of scan commands, cleanup commands, and tier classifications.
