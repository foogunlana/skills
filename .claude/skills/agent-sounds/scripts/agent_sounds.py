#!/usr/bin/env python3
"""
Agent Sounds: play configurable chimes for agent lifecycle hooks.

Design goals:
- Zero dependencies (stdlib only)
- Works out of the box on macOS via system sounds + afplay
- Falls back gracefully on other platforms (bell / common players if present)
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


DEFAULT_CONFIG: Dict[str, Any] = {
    "enabled": True,
    "cooldown_ms": 1200,
    "hooks": {
        "plan.done": "ding",
        "task.done": "success",
        "run.done": "success",
        "error": "error",
        "waiting": "ping",
    },
    "sounds": {
        "ding": "system:Glass",
        "success": "system:Hero",
        "error": "system:Basso",
        "ping": "system:Ping",
    },
}


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)


def _now_ms() -> int:
    return int(time.time() * 1000)


def _state_path() -> Path:
    # Per-user, per-machine state in temp dir; used for cooldown.
    tmp = Path(os.environ.get("TMPDIR") or "/tmp")
    return tmp / "agent-sounds-state.json"


def _load_state() -> Dict[str, Any]:
    p = _state_path()
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_state(state: Dict[str, Any]) -> None:
    p = _state_path()
    try:
        p.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except Exception:
        # Never fail the main action due to state persistence.
        pass


def _find_config_file(start_dir: Path) -> Optional[Path]:
    explicit = os.environ.get("AGENT_SOUNDS_CONFIG")
    if explicit:
        p = Path(explicit).expanduser()
        return p if p.is_file() else None

    cur = start_dir.resolve()
    while True:
        candidate = cur / ".claude" / "agent-sounds.json"
        if candidate.is_file():
            return candidate
        if cur.parent == cur:
            return None
        cur = cur.parent


def _load_config(start_dir: Path) -> Tuple[Dict[str, Any], Optional[Path]]:
    cfg_path = _find_config_file(start_dir)
    if not cfg_path:
        return dict(DEFAULT_CONFIG), None
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        merged = dict(DEFAULT_CONFIG)
        merged.update({k: v for k, v in cfg.items() if k in ("enabled", "cooldown_ms")})
        merged_hooks = dict(DEFAULT_CONFIG.get("hooks", {}))
        merged_hooks.update(cfg.get("hooks", {}) or {})
        merged_sounds = dict(DEFAULT_CONFIG.get("sounds", {}))
        merged_sounds.update(cfg.get("sounds", {}) or {})
        merged["hooks"] = merged_hooks
        merged["sounds"] = merged_sounds
        return merged, cfg_path
    except Exception as ex:
        eprint(f"[agent-sounds] Failed to read config: {cfg_path}: {ex}")
        return dict(DEFAULT_CONFIG), cfg_path


def _resolve_sound_spec(spec: str, *, config_dir: Optional[Path]) -> Tuple[str, Optional[Path], Optional[str]]:
    """
    Returns (kind, path, message):
    - kind in {"file", "bell", "say", "none"}
    - path for kind=="file"
    - message for kind=="say"
    """
    s = (spec or "").strip()
    if not s:
        return ("none", None, None)

    # Convenience: allow "Glass" == system:Glass
    if ":" not in s and not s.startswith(("/", "./", "../", "~")):
        s = f"system:{s}"

    if s == "bell":
        return ("bell", None, None)

    if s.startswith("say:"):
        msg = s[len("say:") :].strip()
        return ("say", None, msg)

    if s.startswith("file:"):
        raw = s[len("file:") :].strip()
        p = Path(raw).expanduser()
        if not p.is_absolute() and config_dir is not None:
            p = (config_dir / p).resolve()
        return ("file", p, None)

    if s.startswith("system:"):
        name = s[len("system:") :].strip()
        sysname = platform.system().lower()
        if sysname == "darwin":
            # macOS: try standard system sound locations.
            candidates = [
                Path("/System/Library/Sounds") / f"{name}.aiff",
                Path("/System/Library/Sounds") / f"{name}.caf",
                Path("/System/Library/Sounds") / f"{name}.wav",
                Path("/Library/Sounds") / f"{name}.aiff",
                Path("/Library/Sounds") / f"{name}.caf",
                Path("/Library/Sounds") / f"{name}.wav",
                Path.home() / "Library/Sounds" / f"{name}.aiff",
                Path.home() / "Library/Sounds" / f"{name}.caf",
                Path.home() / "Library/Sounds" / f"{name}.wav",
            ]
            for c in candidates:
                if c.is_file():
                    return ("file", c, None)
            return ("bell", None, None)

        # Non-macOS: treat as bell unless user uses file: explicitly.
        return ("bell", None, None)

    # If it's an absolute/relative path, try playing it as a file.
    if s.startswith(("/", "./", "../", "~")):
        p = Path(s).expanduser()
        if not p.is_absolute() and config_dir is not None:
            p = (config_dir / p).resolve()
        return ("file", p, None)

    # Unknown format -> bell.
    return ("bell", None, None)


def _pick_player() -> Optional[str]:
    # Preferred: macOS afplay.
    for cmd in ("afplay", "paplay", "aplay", "play"):
        if shutil.which(cmd):
            return cmd
    return None


def _play_file(path: Path, *, volume: Optional[float]) -> bool:
    player = _pick_player()
    if not player:
        return _play_bell()

    if not path.is_file():
        eprint(f"[agent-sounds] Sound file not found: {path}")
        return _play_bell()

    try:
        if player == "afplay":
            args = ["afplay"]
            if volume is not None:
                # afplay volume is 0..1
                args += ["-v", str(volume)]
            args.append(str(path))
        else:
            args = [player, str(path)]
        subprocess.run(args, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return _play_bell()


def _play_bell() -> bool:
    try:
        sys.stdout.write("\a")
        sys.stdout.flush()
        return True
    except Exception:
        return False


def _say(message: str) -> bool:
    if not message:
        return _play_bell()
    if platform.system().lower() != "darwin":
        return _play_bell()
    if not shutil.which("say"):
        return _play_bell()
    try:
        subprocess.run(["say", message], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return _play_bell()


def _cooldown_allows(hook: str, cooldown_ms: int) -> bool:
    if cooldown_ms <= 0:
        return True
    state = _load_state()
    last = 0
    try:
        last = int(state.get("last", {}).get(hook, 0))
    except Exception:
        last = 0

    now = _now_ms()
    if now - last < cooldown_ms:
        return False

    last_map = dict(state.get("last", {}) or {})
    last_map[hook] = now
    state["last"] = last_map
    _save_state(state)
    return True


def cmd_emit(args: argparse.Namespace) -> int:
    cfg, cfg_path = _load_config(Path.cwd())
    if not cfg.get("enabled", True):
        return 0

    hook = args.hook.strip()
    cooldown_ms = int(cfg.get("cooldown_ms", 1200) or 0)
    if not _cooldown_allows(hook, cooldown_ms):
        return 0

    hooks = cfg.get("hooks", {}) or {}
    sounds = cfg.get("sounds", {}) or {}

    mapped = hooks.get(hook)
    if mapped is None:
        # Unknown hook: silent success (keeps callers simple).
        return 0

    # "hooks" may reference a named sound key or be a direct spec.
    spec = sounds.get(mapped, mapped)
    config_dir = cfg_path.parent if cfg_path else None
    kind, path, msg = _resolve_sound_spec(str(spec), config_dir=config_dir)

    if kind == "none":
        return 0
    if kind == "bell":
        return 0 if _play_bell() else 1
    if kind == "say":
        message = args.message if args.message is not None else (msg or "")
        return 0 if _say(message) else 1
    if kind == "file":
        volume = args.volume
        return 0 if _play_file(path or Path(), volume=volume) else 1

    return 0


def cmd_init(args: argparse.Namespace) -> int:
    project_root = Path.cwd()
    target_dir = project_root / ".claude"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "agent-sounds.json"

    if target.exists() and not args.force:
        eprint(f"[agent-sounds] Config already exists: {target}")
        return 2

    target.write_text(json.dumps(DEFAULT_CONFIG, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(str(target))
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    cfg, _ = _load_config(Path.cwd())
    sounds = cfg.get("sounds", {}) or {}
    hooks = cfg.get("hooks", {}) or {}

    print("Hooks:")
    for k in sorted(hooks.keys()):
        v = hooks[k]
        print(f"  {k}: {v}")

    print("\nSounds:")
    for k in sorted(sounds.keys()):
        v = sounds[k]
        print(f"  {k}: {v}")

    return 0


def cmd_test(args: argparse.Namespace) -> int:
    # Play the resolved sound for a hook without requiring it to be mapped by default config.
    ns = argparse.Namespace(hook=args.hook, volume=args.volume, message=args.message)
    return cmd_emit(ns)


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(
        prog="agent_sounds.py",
        description="Play configurable sounds for agent lifecycle hooks.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    p_emit = sub.add_parser("emit", help="Emit a sound for a hook name (e.g. plan.done).")
    p_emit.add_argument("hook", help="Hook name, e.g. plan.done")
    p_emit.add_argument("--volume", type=float, default=None, help="Volume for afplay (0..1).")
    p_emit.add_argument("--message", default=None, help="Message for say:<text> sounds (optional override).")
    p_emit.set_defaults(func=cmd_emit)

    p_init = sub.add_parser("init", help="Create .claude/agent-sounds.json in the current project.")
    p_init.add_argument("--force", action="store_true", help="Overwrite config if it exists.")
    p_init.set_defaults(func=cmd_init)

    p_list = sub.add_parser("list", help="List hooks and sounds from config (or defaults).")
    p_list.set_defaults(func=cmd_list)

    p_test = sub.add_parser("test", help="Emit a hook sound (alias of emit).")
    p_test.add_argument("hook", help="Hook name, e.g. plan.done")
    p_test.add_argument("--volume", type=float, default=None, help="Volume for afplay (0..1).")
    p_test.add_argument("--message", default=None, help="Message for say:<text> sounds (optional override).")
    p_test.set_defaults(func=cmd_test)

    args = p.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
