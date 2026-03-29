# Oya Plugin

Oya is a planning companion for intentional weekly and daily planning. It is packaged here as a Claude-compatible plugin bundle with a plugin manifest and the `oya` skill assets.

## What It Does

Oya helps users:

- plan the week with a short, structured review
- create daily focus lists from weekly priorities
- carry unfinished tasks forward until they are complete
- optionally use coaching, values, and nudges to stay aligned

## Package Contents

```text
oya-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── oya/
        ├── SKILL.md
        ├── assets/
        └── references/
```

## Installation

### Option 1: Install from source

1. Clone this repository.
2. Keep the `oya-plugin` directory intact so the manifest and skill files stay together.
3. Install or copy the package using your Claude plugin loading workflow.

### Option 2: Install as a released bundle

1. Download the packaged `oya-plugin` release archive.
2. Extract it without changing the internal folder structure.
3. Install the extracted folder using your Claude plugin loading workflow.

### Skill-only fallback

If you are loading Claude skills directly instead of using a plugin bundle, copy `skills/oya` into your local `.claude/skills/` directory.

## Usage

Run `oya` in Claude after installation.

On first run, Oya will:

1. create a weekly note
2. ask the user to personalize the planning setup
3. create a daily entry from the weekly plan

After onboarding, Oya switches to a fast regular flow:

- create the current weekly note if it is missing
- append today's daily entry if needed
- carry forward unfinished tasks
- optionally provide critique and coaching

## Configuration

Oya stores user-specific settings in `.claude/oya.md` inside the user's working directory.

Common settings include:

- name
- mantra
- planning contexts
- values
- nudges
- coaching preferences
- optional custom note paths

See `skills/oya/references/config-guide.md` for the full configuration reference.

## Versioning

This plugin uses semantic versioning.

- `MAJOR`: incompatible workflow or packaging changes
- `MINOR`: backward-compatible features or expanded planning behavior
- `PATCH`: backward-compatible fixes, copy updates, or packaging corrections

The current manifest version is `0.1.0`, which marks this package as an early distributable release.

## Distribution

Use the files in this folder as the source of truth for distribution.

- keep `.claude-plugin/plugin.json` and `skills/oya/` in the same package
- publish packaged archives from `oya-plugin/`
- document changes for each release
- test with a small team before promoting the release broadly

See `PUBLISHING.md` for the release checklist.
