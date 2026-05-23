---
name: md-frontmatter
description: Add provenance frontmatter to every .md file Claude creates. MUST activate whenever Claude uses the Write tool to create a NEW .md file. Ensures every Claude-generated markdown file has frontmatter recording authorship, creation date, purpose, context provided, and source references. Does NOT apply when editing existing files or writing non-.md files.
---

# Markdown Frontmatter Provenance

When creating any new `.md` file, include YAML frontmatter with these fields:

```yaml
---
author: claude
created: YYYY-MM-DD
purpose: |
  <1-2 sentence summary of why this file was created — what the user asked for>
context: |
  <Brief description of what information or instructions the user provided that led to this file>
references:
  - <file paths, URLs, conversation context, or tools consulted to produce this content>
  - <additional sources as needed>
---
```

## Rules

1. **Always add frontmatter** when using the Write tool to create a new `.md` file
2. **Never add frontmatter** when editing an existing file (Edit tool) — do not retroactively stamp files
3. **Never add frontmatter** to non-`.md` files
4. **Preserve existing frontmatter** — if a file already has frontmatter (e.g. from a template), merge the provenance fields into it rather than duplicating the `---` block
5. **Be specific in `purpose`** — "Created daily review note" not "Created a file the user asked for"
6. **Be specific in `context`** — mention the key inputs: "User provided their weekly goals and asked for a structured review template"
7. **List real references** — file paths read, URLs fetched, tools/MCPs consulted. Use `- conversation context` only when no external sources were used
8. **Use today's date** for `created` (from the system date, not guessed)
9. **Author is always `claude`** — if a file was not created by Claude (i.e. the author would be the user), use their configured name or "user"

## Example

User asks: "Create a note summarizing the key ideas from Naked Statistics chapter 3"

```yaml
---
author: claude
created: 2026-05-02
purpose: |
  Summary of key ideas from Naked Statistics chapter 3, as requested by user.
context: |
  User asked for a chapter summary. Content drawn from user's existing notes in the vault.
references:
  - "L&D - Growth/Books/Naked Statistics.md"
---
```