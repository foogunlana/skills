# Claude Code Skills

A collection of skills that extend Claude Code's capabilities with specialized knowledge, workflows, and tools.

## What are Skills?

Skills are modular, self-contained packages that transform Claude from a general-purpose agent into a specialized agent equipped with domain-specific knowledge. Think of them as "onboarding guides" that provide:

- **Specialized workflows** - Multi-step procedures for specific domains
- **Tool integrations** - Instructions for working with specific file formats or APIs
- **Domain expertise** - Company-specific knowledge, schemas, business logic
- **Bundled resources** - Scripts, references, and assets for complex tasks

## Available Skills

### oya
Plan and stay on track. Fast. Practical. Intentional.

A planning companion that helps you start your day or week with intention and clarity through:
- **Weekly planning** (10-15 min) - Review last week, set goals for this week
- **Daily planning** (5 min) - Copy tasks from weekly, set today's focus
- **Automatic task carry-forward** - Uncompleted tasks move forward automatically
- **Optional coaching** - Pattern detection to help spot overloading or vague goals

**Usage:** Run `/oya` in Claude Code to start planning.

### skill-creator
Guide for creating effective skills.

Provides comprehensive guidance for building new skills, including:
- Skill creation workflow and best practices
- Design patterns for different skill types
- Scripts for initialization, validation, and packaging
- Examples and templates

**Usage:** Automatically triggered when creating or updating skills.

## Using Skills

Skills are automatically loaded by Claude Code from your `.claude/skills/` directory. To use an installed skill:

1. Open Claude Code in a directory with skills installed
2. The skills are automatically available - just ask Claude for help with tasks the skills support
3. You can explicitly invoke a skill using `/skill-name` (e.g., `/oya`)

## Creating New Skills

### Quick Start

1. **Initialize a new skill:**
   ```bash
   .claude/skills/skill-creator/scripts/init_skill.py my-skill --path skills
   ```

2. **Develop your skill:**
   - Edit `skills/my-skill/SKILL.md` to define the skill's behavior
   - Add scripts, references, or assets as needed
   - Delete any example files you don't need

3. **Package the skill:**
   ```bash
   .claude/skills/skill-creator/scripts/package_skill.py skills/my-skill
   ```

4. **Share or install:**
   - The `.skill` file can be shared with others
   - Install locally by copying to `.claude/skills/`

### Skill Structure

```
my-skill/
├── SKILL.md              # Required: Metadata + instructions
├── scripts/              # Optional: Executable Python/Bash scripts
├── references/           # Optional: Documentation loaded as needed
└── assets/               # Optional: Templates, images, boilerplate
```

#### SKILL.md

Every skill requires a `SKILL.md` file with:

**Frontmatter (YAML):**
```yaml
---
name: my-skill
description: What the skill does and when to use it
---
```

**Body (Markdown):**
- Instructions for using the skill
- References to bundled resources
- Workflows, examples, and guidance

#### Bundled Resources (Optional)

- **scripts/** - Executable code for deterministic operations (e.g., `rotate_pdf.py`)
- **references/** - Documentation loaded into context when needed (e.g., API docs, schemas)
- **assets/** - Files used in output (e.g., templates, boilerplate code, images)

## Skill Development Tools

All skill management scripts are located in `.claude/skills/skill-creator/scripts/`:

### init_skill.py
Initialize a new skill from template:
```bash
.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path <output-dir>
```

Creates a skill directory with:
- SKILL.md template with TODO placeholders
- Example scripts/, references/, and assets/ directories
- Placeholder files you can customize or delete

### package_skill.py
Validate and package a skill:
```bash
.claude/skills/skill-creator/scripts/package_skill.py <path/to/skill> [output-dir]
```

Automatically validates the skill first, then creates a `.skill` file (zip format) if validation passes.

### quick_validate.py
Validate a skill without packaging:
```bash
.claude/skills/skill-creator/scripts/quick_validate.py <path/to/skill>
```

Checks:
- YAML frontmatter format and required fields
- Naming conventions (hyphen-case)
- Description completeness and length limits
- File organization

## Design Principles

### Keep Skills Concise
The context window is shared across all skills, system prompts, and conversation history. Only include information Claude doesn't already have.

### Progressive Disclosure
Skills load in three levels:
1. **Metadata** (name + description) - Always loaded
2. **SKILL.md body** - Loaded when skill triggers
3. **Bundled resources** - Loaded as needed

Keep SKILL.md under 500 lines. Split larger content into `references/` files.

### Degrees of Freedom
Match specificity to task fragility:
- **High freedom** - Text instructions for flexible approaches
- **Medium freedom** - Pseudocode for preferred patterns with variation
- **Low freedom** - Specific scripts for fragile, critical operations

## Best Practices

1. **Start with concrete examples** - Understand how the skill will be used
2. **Test all scripts** - Run scripts to ensure they work correctly
3. **Write clear descriptions** - Include both what the skill does AND when to use it
4. **Delete unused examples** - Remove template files you don't need
5. **Use imperative form** - Write instructions as commands (e.g., "Run the script")
6. **Avoid duplication** - Information should live in SKILL.md OR references, not both
7. **Iterate based on usage** - Refine skills based on real-world use

## Repository Structure

```
skills/
├── .claude/
│   └── skills/          # Installed skills (active)
├── skills/              # Skill development source
│   └── oya/            # Example: oya skill source
└── CLAUDE.md           # Guidance for Claude Code instances
```

## Contributing

When creating skills:

1. Follow the naming convention: hyphen-case, lowercase (e.g., `my-skill`)
2. Keep skill names under 64 characters
3. Keep descriptions under 1024 characters
4. Validate before packaging
5. Test the skill on real tasks before sharing

## License

See individual skill licenses in their respective SKILL.md files.
