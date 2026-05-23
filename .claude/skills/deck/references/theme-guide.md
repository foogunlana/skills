# Slidev Theme Reference

> **Customize this file** for your brand. Replace placeholder values (fonts, colours, logo paths, URLs) with your organization's branding.

## Project Structure

Every presentation lives in `presentations/<deck-name>/` with this structure:

```
presentations/<deck-name>/
├── slides.md            # Main slide file
├── idea.md              # Optional brainstorming notes
├── talking-points.md    # Optional speaker notes reference
├── components/          # Vue components (reusable per-deck)
│   ├── BrandFooter.vue      # REQUIRED — footer with logo + page number
│   └── ContentFrame.vue     # REQUIRED — standard content slide frame
├── layouts/             # Slidev layouts
│   ├── cover.vue        # REQUIRED — dark cover slide
│   ├── default.vue      # REQUIRED — standard content (wraps ContentFrame)
│   ├── section.vue      # REQUIRED — centered text (wraps ContentFrame center)
│   ├── center.vue       # Optional — centered content
│   └── two-cols.vue     # Optional — two-column layout
├── styles/
│   └── index.css        # Print overrides
└── assets/              # Images, logos, SVGs
    ├── title-background.png  # Cover slide background
    └── logo.png              # Brand logo (white, for dark backgrounds)
```

## Frontmatter Template

Customize the font, colours, and theme values to match your brand:

```yaml
---
theme: default
layout: cover
defaults:
  layout: default
title: "Deck Title"
info: |
  Description
fonts:
  sans: Plus Jakarta Sans        # Replace with your brand font
  weights: '400,500,600,700'
  italic: false
themeConfig:
  light-bg: '#ffffff'
  dark-bg: '#020202'
  ink: '#111111'                 # Primary text colour
  muted: 'rgba(0,0,0,0.78)'     # Secondary text colour
  muted-2: 'rgba(0,0,0,0.5)'    # Tertiary text colour
  rule: 'rgba(0,0,0,0.18)'      # Divider lines
  card-bg: 'rgba(255,255,255,0.48)'
  card-border: 'rgba(0,0,0,0.08)'
  summary: 'rgba(0,0,0,0.82)'
drawings:
  persist: false
transition: fade-out
mdc: true
---
```

## ContentFrame Features

The main content frame provides:
- **Dot grid header** — 88px tall, radial-gradient dots
- **Title** — from `title` frontmatter, rendered as h1
- **Summary** — from `summary` frontmatter, rendered at bottom above footer (use for quotes, takeaways)
- **Content area** — between title and summary/footer, clips overflow
- **Footer** — Brand logo, website URL, page number

Content area boundary: starts at ~92px from top, ends at ~58px from bottom (96px if summary present).

## BrandFooter Props

- `dark` (boolean) — dark text for light backgrounds
- `page` (number|string) — override page number

## Slide Frontmatter Options

```yaml
title: "Slide Title"          # Rendered by ContentFrame as h1
summary: "Bottom text"         # Rendered in dedicated zone above footer
footerPage: 3                  # Override page number
layout: section                # Use section/center/two-cols/cover
```

## Makefile Pattern

Add four targets per deck:

```makefile
deck-name: .npm-install-stamp
	npm run dev -- presentations/deck-name/slides.md

build-deck-name: .npm-install-stamp
	npm run build -- presentations/deck-name/slides.md

format-deck-name: .npm-install-stamp
	npm run format -- presentations/deck-name/slides.md

pdf-deck-name: .npm-install-stamp
	mkdir -p dist
	npx slidev export presentations/deck-name/slides.md --output dist/deck-name.pdf
```

Also add to .PHONY line.

## Speaker Notes

Use HTML comments after slide content:

```markdown
# Slide Title

Content here

<!--
- Talking point 1
- Talking point 2
- Talking point 3
-->
```

View in presenter mode: press `P` or navigate to `/presenter`.

## Progressive Reveal

Use `v-click` for content that appears on click:

```html
<div v-click>This appears on click</div>
```
