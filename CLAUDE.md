# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a skills repository for Claude Code. Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. Each skill acts as an "onboarding guide" for specific domains or tasks.

## Repository Structure

The repository has two primary skill directories:

- **`.claude/skills/`** - Skills that are installed and loaded by Claude Code for this session. These are the active skills that Claude has access to when working in this repository.
- **`skills/`** - Source directory for skills being developed. Skills are developed here, then packaged and installed to `.claude/skills/` for use.

Each skill follows this structure:
```
skill-name/
├── SKILL.md (required)        # Metadata + instructions for Claude
├── scripts/                    # Executable Python/Bash scripts
├── references/                 # Documentation loaded into context as needed
└── assets/                     # Files used in output (templates, boilerplate)
```

## Skill Development Workflow

### 1. Initialize a New Skill

```bash
.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path skills
```

This creates a template skill with:
- SKILL.md with TODO placeholders
- Example `scripts/`, `references/`, and `assets/` directories
- Example files that should be customized or deleted

### 2. Develop the Skill

Edit the generated skill files:

1. **Update SKILL.md frontmatter:**
   - `name`: hyphen-case identifier (lowercase, hyphens, max 64 chars)
   - `description`: Complete explanation of what the skill does AND when to use it (max 1024 chars)

2. **Add reusable resources:**
   - `scripts/`: Executable code for deterministic operations
   - `references/`: Documentation loaded into context as needed
   - `assets/`: Templates, boilerplate, images used in output

3. **Write SKILL.md body:** Instructions for using the skill and its resources

**Important:** Test any scripts by actually running them to ensure they work correctly.

### 3. Validate the Skill

The validation happens automatically during packaging, but you can run it standalone:

```bash
.claude/skills/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

Validation checks:
- YAML frontmatter format and required fields (name, description)
- Naming conventions (hyphen-case)
- Description completeness (no angle brackets, max 1024 chars)
- File organization

### 4. Package the Skill

```bash
.claude/skills/skill-creator/scripts/package_skill.py skills/<skill-name>
```

Or specify output directory:

```bash
.claude/skills/skill-creator/scripts/package_skill.py skills/<skill-name> ./dist
```

This:
1. Validates the skill first
2. Creates a `.skill` file (zip format with .skill extension) in the specified directory
3. Includes all files while maintaining directory structure

### 5. Install the Skill (if testing locally)

To test the skill in Claude Code, install it to `.claude/skills/`:

```bash
# Copy the skill directory directly
cp -r skills/<skill-name> .claude/skills/
```

## Skill Design Principles

### Keep Skills Concise

The context window is shared between all skills, system prompts, conversation history, and user requests. Only include information Claude doesn't already have. Challenge each piece: "Does Claude really need this?" and "Does this justify its token cost?"

### Progressive Disclosure

Skills use a three-level loading system:
1. **Metadata (name + description)** - Always loaded (~100 words)
2. **SKILL.md body** - Loaded when skill triggers (<5k words, keep under 500 lines)
3. **Bundled resources** - Loaded as needed by Claude

When SKILL.md approaches 500 lines, split content into `references/` files and reference them from SKILL.md.

### Set Appropriate Degrees of Freedom

- **High freedom (text instructions)**: Multiple valid approaches, context-dependent decisions
- **Medium freedom (pseudocode/parameterized scripts)**: Preferred pattern exists, some variation acceptable
- **Low freedom (specific scripts)**: Operations are fragile, consistency critical, specific sequence required

### Avoid Duplication

Information should live in either SKILL.md or reference files, not both. Prefer reference files for detailed information unless it's core to the skill.

## Current Skills in Repository

### oya
A planning skill that helps users start their day or week with intention and clarity. Supports weekly planning (10-15 min) and daily planning (5 min) workflows with automatic task carry-forward and optional coaching.

### skill-creator
Guide for creating effective skills. Provides the skill creation workflow, design patterns, and bundled scripts for initialization, validation, and packaging.

## Skill Script Locations

All skill management scripts are in `.claude/skills/skill-creator/scripts/`:
- `init_skill.py` - Initialize new skill from template
- `package_skill.py` - Validate and package skill into .skill file
- `quick_validate.py` - Validate skill structure and metadata

## Best Practices

1. **Start with concrete examples** - Understand how the skill will be used before building it
2. **Test scripts** - Run any scripts to ensure they work correctly
3. **Keep SKILL.md under 500 lines** - Split into references/ files if longer
4. **Delete unused example files** - Remove any `scripts/`, `references/`, or `assets/` examples that aren't needed
5. **Write clear descriptions** - Include both what the skill does AND when to use it (this determines triggering)
6. **Use imperative form** - Write instructions in imperative/infinitive form
7. **Iterate based on usage** - Test skills on real tasks and refine based on what struggles or works well
