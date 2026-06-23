# UI Rules

**Last Updated:** 2026-06-23

## Layout Rules

- Settings pages use a single-column card layout with `--spacing-lg` between cards.
- Each card contains a heading, description (optional), and form fields or controls.
- Back navigation is placed above the page title using the shared `BackLink` pattern.

## Component Rules

- Badge variants must use token-mapped colors — never hardcode hex values in component code.
- `InvoiceStatusBadge` accepts optional `amount` and `dueDate` props for tooltip context; if only `variant` is provided, it renders as a simple label.
- Table columns must be sortable unless explicitly marked as non-sortable.
- Modals must trap focus and close on Escape.

## Form Rules

- Every form field must display a label, optional hint text, and error state.
- Toggle fields must have an accessible label — no toggle without a description.
- Save actions must be disabled while a save is in progress (optimistic update pattern).

## Accessibility Rules

- All interactive elements must have visible focus indicators.
- Status badges must include `aria-label` for screen readers (e.g., `aria-label="Invoice status: paid"`).
- Color is never the sole indicator — status badges include text labels alongside color.
