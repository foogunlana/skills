---
name: deck
description: "Create and iterate on Slidev presentation decks using a customizable brand theme. Use when the user asks to create a new presentation, slide deck, or slides, or wants to modify/add slides to an existing deck. Triggers on: 'new deck', 'new presentation', 'new slides', 'slide deck', 'make a presentation', or any request involving Slidev markdown slides in the presentations/ directory."
---

# Slidev Deck Builder

Build presentation decks using Slidev with a customizable brand theme, Tailwind CSS, and Vue components.

> **Customize for your brand**: Before first use, update `references/theme-guide.md` with your brand colours, fonts, logos, and naming. Rename components and assets to match your organization.

## Workflow

1. **Brainstorm first** — Understand the narrative before writing code. Ask one question at a time, prefer multiple-choice. Agree on structure (slide count, arc, content per slide) before implementation.
2. **Scaffold the deck** — Copy the brand theme from an existing deck (components, layouts, styles, assets). Create the folder, Makefile targets, and a starter `slides.md`.
3. **Build slide by slide** — Write content, source images, create components. Expect visual iteration via screenshots.
4. **Add flair** — Animations, transitions, and visual polish come after content is solid.
5. **Add speaker notes** — Write talking points as `<!-- -->` comments after each slide's content.

## Theme Setup

Every new deck MUST include the base brand theme files. Copy from an existing deck:

- `components/BrandFooter.vue` — Footer with logo, URL, page number
- `components/ContentFrame.vue` — Standard content frame with dot grid header, title, summary, footer
- `layouts/cover.vue` — Dark cover slide with background image and logo
- `layouts/default.vue` — Wraps ContentFrame
- `layouts/section.vue` — Centered text via ContentFrame
- `layouts/center.vue` — Centered content
- `layouts/two-cols.vue` — Two-column grid
- `styles/index.css` — Print media overrides
- `assets/title-background.png` — Cover background
- `assets/logo.png` — Brand logo (white, for dark backgrounds)

For full theme reference (frontmatter template, component props, Makefile pattern): read [references/theme-guide.md](references/theme-guide.md).

## Critical Rules

### Content Overflow

Slides have a fixed viewport. Content WILL get clipped if it overflows. Design conservatively:
- Start with smaller font sizes than you think you need
- Test visually after every content change
- Use the `summary` frontmatter field for bottom-of-slide text — it renders in a dedicated zone that won't clip

### ContentFrame Style Overrides

ContentFrame applies `:deep()` styles to `ul`, `ol`, `li`, `p`, `h1-h3`, `table`, `blockquote` inside its content area. These override inline Tailwind classes. To force smaller sizes in child components, use `:deep()` with `!important` in the component's scoped styles.

### YAML Frontmatter

- Values containing `#`, `:`, or `"` MUST be wrapped in double quotes
- Escape inner quotes with `\"`
- The `summary` field is especially useful — it renders in a fixed position above the footer

### HTML in Markdown

- NO blank lines inside HTML blocks — blank lines re-enter markdown mode and break rendering
- NO indentation of nested HTML — indented HTML renders as code blocks
- Keep HTML blocks tight and flush-left

## Components & Tailwind

### Always Use Components

Extract any repeated pattern into a Vue component in `components/`. Examples: cards, team members, visual elements, animated widgets. Pass data via props, use slots for flexible content.

### Always Use Tailwind

Use Tailwind utility classes for all styling. Use arbitrary values `[Xpx]` for precise control. Match the existing deck patterns — the theme uses specific spacing scales and colour tokens via CSS variables.

### Theme Colour Tokens

Access via CSS variables in Tailwind arbitrary values:
- `var(--slidev-theme-ink)` — primary text
- `var(--slidev-theme-muted)` — secondary text
- `var(--slidev-theme-muted-2)` — tertiary text
- `var(--slidev-theme-rule)` — divider lines
- `var(--slidev-theme-card-bg)` — card backgrounds
- `var(--slidev-theme-card-border)` — card borders

## Stock Images

When sourcing images:
- Pexels is the most reliable free source. URL pattern: `https://images.pexels.com/photos/{id}/pexels-photo-{id}.jpeg?auto=compress&cs=tinysrgb&w=800`
- Unsplash download pattern: `https://unsplash.com/photos/{id}/download?force=true&w=800` (may 403)
- Always download 3-5 candidates and verify visually before choosing
- Free stock sites lack dramatic/conceptual imagery (robot armies, abstract AI). Flag this early — the user may need to generate images with AI tools or source from paid sites
- Copy chosen images to the deck's `assets/` folder

## Animations

CSS animations work well in Slidev. Keep them subtle and slow:
- **Timing**: 4-12 second cycles feel premium. 1-2 second cycles feel cheap.
- **Stagger**: Offset animation delays across elements so they don't pulse together.
- **Use `scoped`**: Always use `<style scoped>` in components. For slide-level animations, use a raw `<style>` block in markdown.
- **requestAnimationFrame**: For per-element JavaScript animations (e.g. dot grids with per-dot behaviour), use a Vue component with `requestAnimationFrame` for smooth 60fps.

## Iteration Pattern

The user iterates visually:
1. They run `make deck-name` to preview
2. They screenshot issues and describe what's wrong
3. Fix the specific issue they pointed at — don't re-read the whole file
4. Repeat until they're happy

Common iteration issues:
- Content clipped at bottom → reduce font sizes, gaps, padding
- Too much whitespace → tighten padding, reduce gaps
- Text too small/large → adjust font sizes
- Images wrong → source new ones, verify visually
- Needs more flair → add animations, gradients, glows
