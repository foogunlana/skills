# Publishing Oya

This file covers the practical steps needed to distribute Oya before a wider launch.

## Release Strategy

Use a staged rollout:

1. distribute privately to a small test group
2. collect feedback on onboarding, note generation, and packaging
3. fix issues and cut a new semver release
4. publish a broader release package

## Versioning Rules

Update `.claude-plugin/plugin.json` for every release.

- `0.x.y`: pre-general-availability builds
- `1.0.0`: first stable public release
- increment `PATCH` for fixes
- increment `MINOR` for backward-compatible feature work
- increment `MAJOR` for breaking changes to plugin packaging or behavior expectations

## Packaging

Create a release archive from the `oya-plugin/` directory so users receive:

- `.claude-plugin/plugin.json`
- `skills/oya/SKILL.md`
- `skills/oya/assets/`
- `skills/oya/references/`

Example packaging command:

```bash
cd oya-plugin
zip -r oya-plugin-v0.1.0.zip .claude-plugin skills
```

## Distribution Channels

Use one of these channels depending on what is available to the team:

- GitHub Releases for downloadable versioned archives
- an internal plugin catalog or shared team distribution folder
- a future plugin marketplace once the target platform documents one

## Team Test Checklist

Ask testers to validate these flows:

- clean install from the packaged bundle
- first-run onboarding with no existing `.claude/oya.md`
- repeat usage with an existing weekly note
- daily task carry-forward behavior for `[ ]`, `[-]`, and `[x]`
- weekend behavior
- optional coaching, values, and nudges
- failure cases such as sparse notes or missing prior context

## Feedback Template

Collect feedback in a consistent format:

- environment used
- install method
- expected behavior
- actual behavior
- screenshots or copied note output
- severity: blocker, major, minor

## Pre-Release Checklist

- confirm `README.md` matches the shipped package
- confirm `.claude-plugin/plugin.json` version is updated
- test installation from a fresh copy of the packaged archive
- verify the `oya` command appears and loads correctly
- validate onboarding and regular flows end to end
- record user-facing changes for the release notes
