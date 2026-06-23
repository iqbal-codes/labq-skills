# Imprint Audit — Spacing & Color Drift

## Scope

The audit covers all UI components — cards, buttons, and forms — across the codebase to identify inconsistencies in:

- **Border radius** values
- **Background colors** (solid, transparent, token-based)
- **Text colors**
- **Spacing** (padding, margin, gap)
- **Border** widths, styles, and colors
- **Interactive states** (hover, focus, active, disabled)

## What I Need From You

Before I can run a concrete audit, I need to know **where the UI lives**. Specifically:

1. **Component directory** — which path(s) hold the card, button, and form components? (e.g. `src/components/`, `app/ui/`)
2. **Framework** — are these React, Vue, Svelte, Astro, or plain HTML?
3. **CSS approach** — Tailwind utility classes, CSS modules, styled-components, vanilla CSS, or a design-token system?
4. **Existing design tokens** — is there a `tokens.css`, `theme.ts`, `tailwind.config.*`, or similar that defines the canonical palette, spacing scale, and radius values?

## Audit Plan (once scoped)

| Step | Action |
|------|--------|
| 1 | **Catalog all components** — list every card, button, and form variant found in the target directory. |
| 2 | **Extract token usage** — for each component, record the actual values used for `border-radius`, `background`, `color`, `padding`, `margin`, `gap`, `border`, and interactive pseudo-class styles. |
| 3 | **Detect drift** — compare extracted values against the canonical token set. Flag any hardcoded hex values, raw color classes (`bg-gray-500` instead of `bg-surface`), or non-token spacing (e.g. `13px` instead of a scale value). |
| 4 | **Group conflicts** — list every inconsistency by category (radius, background, text color, spacing, border, interactive states). For each, show which components diverge and from what. |
| 5 | **Recommend baseline** — propose a single canonical value per property based on majority usage and alignment with existing design-system tokens. |
| 6 | **Confirm before applying** — present findings and wait for your approval before writing anything to `ui-registry.md` or making changes. |

## Example Findings Format (preview)

Here's what a typical drift report would look like:

### Border Radius Drift
| Component | Current Value | Recommended | Issue |
|-----------|--------------|-------------|-------|
| Card (default) | `12px` | `8px` | Hardcoded, not from token scale |
| Button (primary) | `6px` | `6px` | Matches token ✓ |
| Button (ghost) | `0px` | `6px` | Missing radius, inconsistent with other buttons |
| Form input | `4px` | `6px` | Below token minimum |

### Color Drift
| Component | Property | Current | Recommended | Issue |
|-----------|----------|---------|-------------|-------|
| Card | background | `#F8F9FA` | `var(--color-surface)` | Hardcoded hex |
| Button (disabled) | text | `#AAAAAA` | `var(--color-text-muted)` | Hardcoded hex |
| Form error | border | `red-500` | `var(--color-danger)` | Raw utility, not token |

### Spacing Drift
| Component | Property | Current | Recommended | Issue |
|-----------|----------|---------|-------------|-------|
| Card padding | padding | `16px 20px` | `16px` | Asymmetric, outside 4px scale |
| Button padding | padding | `10px 24px` | `12px 24px` | `10px` not on spacing scale |
| Form gap | gap | `12px` | `16px` | Below adjacent-card gap standard |

---

**Next step:** Point me at the component directory and I'll run the full audit and produce a concrete drift report with a recommended baseline for your confirmation.
