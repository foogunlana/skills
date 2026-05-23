# macOS Cleanup Targets

## Tier 1: Safe Cache Cleanups (always safe, regenerate on demand)

| Target | Scan Command | Cleanup Command |
|--------|-------------|-----------------|
| UV cache | `du -sh ~/.cache/uv 2>/dev/null` | `uv cache clean` |
| npm cache | `du -sh ~/.npm/_cacache 2>/dev/null` | `npm cache clean --force` |
| pip cache | `du -sh ~/Library/Caches/pip 2>/dev/null` | `pip cache purge` |
| Homebrew cache | `du -sh ~/Library/Caches/Homebrew 2>/dev/null` | `brew cleanup --prune=all` |
| Cargo cache | `du -sh ~/.cargo/registry 2>/dev/null` | `cargo cache -a` (if installed) or `rm -rf ~/.cargo/registry/cache` |
| Yarn cache | `du -sh ~/Library/Caches/Yarn 2>/dev/null` | `yarn cache clean` |
| pnpm cache | `du -sh ~/Library/pnpm/store 2>/dev/null` | `pnpm store prune` |
| Go module cache | `du -sh ~/go/pkg/mod/cache 2>/dev/null` | `go clean -modcache` |
| Ollama update cache | `du -sh ~/Library/Caches/com.electron.ollama.ShipIt 2>/dev/null` | `rm -rf ~/Library/Caches/com.electron.ollama.ShipIt` |
| Cursor update cache | `du -sh ~/Library/Caches/com.todesktop.*.ShipIt 2>/dev/null` | `rm -rf ~/Library/Caches/com.todesktop.*.ShipIt` |
| Puppeteer browsers | `du -sh ~/.cache/puppeteer 2>/dev/null` | `rm -rf ~/.cache/puppeteer` |
| Playwright browsers | `du -sh ~/Library/Caches/ms-playwright 2>/dev/null` | `rm -rf ~/Library/Caches/ms-playwright` |
| HuggingFace cache | `du -sh ~/.cache/huggingface 2>/dev/null` | `rm -rf ~/.cache/huggingface` |
| pre-commit cache | `du -sh ~/.cache/pre-commit 2>/dev/null` | `rm -rf ~/.cache/pre-commit` |

## Tier 1.5: Sandboxed App Downloads (safe but confirm which apps)

Sandboxed macOS apps store downloaded files in `~/Library/Containers/<bundle-id>/Data/Downloads/`. These don't appear in `~/Downloads` and are easy to miss.

| Target | Scan Command | Cleanup Command | Notes |
|--------|-------------|-----------------|-------|
| All sandboxed app downloads | `bash -c 'for d in ~/Library/Containers/*/; do size=$(du -sh "$d/Data/Downloads" 2>/dev/null \| cut -f1); [ -n "$size" ] && [ "$size" != "0B" ] && echo "$size\t$(basename $d)"; done \| sort -hr \| head -10'` | `rm -rf ~/Library/Containers/<bundle-id>/Data/Downloads/*` | Slack, WhatsApp, etc. Can grow to multiple GB |

**Warning on Containers scanning:** macOS creates hardlinks to `~/Desktop`, `~/Music`, `~/Downloads`, `~/Pictures` inside each container's `Data/` dir. These show ~903 MB, ~215 MB, ~53 MB, ~4.4 MB in **every** container but are the same on-disk data. Ignore these when calculating reclaimable space. Only the app's `Data/Library/` and app-specific subdirs contain unique data.

## Tier 2: Review Before Cleaning (user should confirm)

| Target | Scan Command | Cleanup Command | Notes |
|--------|-------------|-----------------|-------|
| Docker | `docker system df 2>/dev/null` | `docker system prune -a -f` | Removes all unused images, containers, volumes |
| Old Node versions (nvm) | `du -sh ~/.nvm/versions/node/* 2>/dev/null \| sort -hr` | `nvm uninstall <version>` | Keep current + one LTS |
| Old Python versions (pyenv) | `du -sh ~/.pyenv/versions/* 2>/dev/null \| sort -hr` | `pyenv uninstall <version>` | Keep actively used versions |
| ~/Downloads | `du -sh ~/Downloads/* 2>/dev/null \| sort -hr \| head -20` | User decides per-file | Show top 20 largest files |
| Xcode derived data | `du -sh ~/Library/Developer/Xcode/DerivedData 2>/dev/null` | `rm -rf ~/Library/Developer/Xcode/DerivedData` | Rebuilds on next Xcode build |
| iOS device support | `du -sh ~/Library/Developer/Xcode/iOS\ DeviceSupport 2>/dev/null` | `rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*` | Re-downloads when device connects |

## Tier 1.7: Dependency/build dirs in code repos (safe, always regeneratable)

These are fully recreatable with `pip install` / `npm install` / `next build`. Scan and nuke in bulk.

| Target | Scan Command | Cleanup Command | Notes |
|--------|-------------|-----------------|-------|
| All .venv, node_modules, etc. | `find ~/code -maxdepth 4 -type d \( -name "node_modules" -o -name ".venv" -o -name "venv" -o -name "__pycache__" -o -name ".next" -o -name "dist" -o -name ".tox" \) -exec du -sh {} + 2>/dev/null \| sort -hr` | `find ~/code -maxdepth 4 -type d \( -name "node_modules" -o -name ".venv" -o -name "venv" -o -name "__pycache__" -o -name ".next" -o -name "dist" -o -name ".tox" \) -exec rm -rf {} + 2>/dev/null` | Typically 5-15 GB across repos. Always safe to delete. |
| Total size | Pipe scan to: `awk '{sum += $1} END {print sum/1024 " GB total"}'` | — | Quick size estimate |

## Tier 2.5: Electron app caches (safe, but apps should be closed first)

Most Electron apps (Claude, Arc, Chrome, Cursor, VS Code, Discord, Slack, Superhuman, etc.) store caches in `~/Library/Application Support/<AppName>/`. These subdirs are safe to delete and rebuild on next launch:

| Subdir | What it is |
|--------|------------|
| `Cache/` | HTTP/asset cache |
| `Code Cache/` | V8 compiled JS cache |
| `GPUCache/` | GPU shader cache |
| `DawnWebGPUCache/` | WebGPU shader cache |
| `DawnGraphiteCache/` | Graphics cache |
| `Service Worker/` | Service worker cache |

**Big hidden hogs in Application Support:**

| Target | Scan Command | Cleanup Command | Notes |
|--------|-------------|-----------------|-------|
| Claude desktop VM | `du -sh "$HOME/Library/Application Support/Claude/vm_bundles" 2>/dev/null` | `rm -rf "$HOME/Library/Application Support/Claude/vm_bundles"/*` | 5-10 GB. Used for computer use / local agent mode. Re-downloads on demand. |
| Claude desktop caches | `du -sh "$HOME/Library/Application Support/Claude/Cache" "$HOME/Library/Application Support/Claude/Code Cache" 2>/dev/null` | `rm -rf "$HOME/Library/Application Support/Claude"/{Cache,Code\ Cache,GPUCache,DawnWebGPUCache,DawnGraphiteCache,local-agent-mode-sessions}/*` | ~800 MB. Always safe. |
| Apple mediaanalysisd | `du -sh ~/Library/Containers/com.apple.mediaanalysisd/ 2>/dev/null` | `rm -rf ~/Library/Containers/com.apple.mediaanalysisd/Data/Library/Caches/*` | 5-15 GB. Photo/video analysis cache. Rebuilds automatically. |
| WhatsApp media cache | `du -sh "$HOME/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/Message/Media" 2>/dev/null` | `rm -rf "$HOME/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/Message/Media"/*` | 5-15 GB. Cached group chat images/videos. WhatsApp re-downloads on demand when you open a chat. |
| Docker VM disk file | `du -sh ~/Library/Containers/com.docker.docker/Data/vms/ 2>/dev/null` | Reset Docker Desktop (Settings → Troubleshoot → Reset to factory defaults) | 5-10 GB. Even after `docker system prune`, the VM disk file stays inflated. Only a factory reset shrinks it. |

## Tier 3: Investigate (large but context-dependent)

| Target | Scan Command | Notes |
|--------|-------------|-------|
| Library/Containers | `du -sh ~/Library/Containers/*/ 2>/dev/null \| sort -hr \| head -10` | App-managed, usually leave alone |
| Library/Application Support | `du -sh "$HOME/Library/Application Support"/*/ 2>/dev/null \| sort -hr \| head -10` | App data — drill into individual apps |
| .docker (Docker VM) | `du -sh ~/.docker 2>/dev/null` | Docker Desktop VM disk |
| IDE extensions (.vscode, .cursor, etc.) | `du -sh ~/.vscode ~/.cursor ~/.windsurf 2>/dev/null` | Extension caches and data |

## Top-Level Scan Command

```bash
du -sh ~/*/ ~/.*/ 2>/dev/null | sort -hr | head -25
```

## Common macOS Space Hogs Scan

```bash
du -sh ~/Library/Caches ~/Library/Developer ~/Library/Application\ Support \
  ~/Library/Containers ~/.docker ~/.npm ~/.cargo ~/.rustup ~/.cache \
  ~/Downloads ~/.local ~/Library/Group\ Containers 2>/dev/null | sort -hr
```
