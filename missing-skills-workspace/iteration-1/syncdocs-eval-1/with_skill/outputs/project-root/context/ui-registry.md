# UI Registry

**Last Updated:** 2026-06-23

## Shared UI Components (`src/components/ui/`)

| Component | File | Token Usage | Notes |
|-----------|------|-------------|-------|
| Button | `src/components/ui/Button.tsx` | `--color-primary`, `--radius-md` | Variants: primary, secondary, ghost, danger |
| Card | `src/components/ui/Card.tsx` | `--color-surface`, `--shadow-sm` | Used for settings panels and content containers |
| Badge | `src/components/ui/Badge.tsx` | `--color-*`, `--radius-full` | Generic status badge; base for status-specific badges |
| **InvoiceStatusBadge** | **`src/components/ui/InvoiceStatusBadge.tsx`** | **`--color-success`, `--color-warning`, `--color-danger`, `--color-muted`** | **Reusable status indicator for invoices. Variants: `paid`, `pending`, `overdue`, `void`. Accepts `amount` and `dueDate` optional props for tooltip context.** |
| Table | `src/components/ui/Table.tsx` | `--color-border`, `--color-surface` | Sortable, paginated; used for lists across modules |
| EmptyState | `src/components/ui/EmptyState.tsx` | `--color-muted`, `--spacing-*` | Illustration + CTA pattern for empty views |
| Modal | `src/components/ui/Modal.tsx` | `--color-overlay`, `--radius-lg` | Focus-trapped, escape-to-close |
| Toast | `src/components/ui/Toast.tsx` | `--color-*`, `--shadow-lg` | Auto-dismiss, stacked positioning |

## Form Fields (`src/components/forms/fields/`)

| Field | File | Notes |
|-------|------|-------|
| TextField | `src/components/forms/fields/TextField.tsx` | Label, hint, error state |
| SelectField | `src/components/forms/fields/SelectField.tsx` | Keyboard-navigable dropdown |
| ToggleField | `src/components/forms/fields/ToggleField.tsx` | Boolean on/off with label |
| DateField | `src/components/forms/fields/DateField.tsx` | Uses `formatDate` from shared utils |

## Page Patterns

| Pattern | Module | File | Notes |
|---------|--------|------|-------|
| Settings page (card layout) | notifications | `src/modules/notifications/pages/NotificationPreferences.tsx` | Card-per-section, toggle fields |
| **Settings page (card layout)** | **billing** | **`src/modules/billing/pages/BillingSettings.tsx`** | **Same card-based layout as notification preferences. Sections: payment method, invoice delivery, billing contact. Uses InvoiceStatusBadge in a recent-invoices preview row.** |
| List page (table + filters) | team | `src/modules/team/pages/TeamMembers.tsx` | Table component + search + role filter |
| Detail page | team | `src/modules/team/pages/TeamMemberDetail.tsx` | Back nav, sections, edit modal |

## Conventions

- All shared components live in `src/components/ui/` — module-local components stay in their module directory.
- Badge variants use token-mapped colors (`--color-success` for positive, `--color-warning` for attention, `--color-danger` for negative).
- Settings pages reuse the `Card` component for visual grouping and follow a consistent vertical spacing of `--spacing-lg` between sections.
