# Code Standards

**Last Updated:** 2026-06-23

## Naming Conventions

- **Components:** PascalCase, descriptive (`InvoiceStatusBadge`, not `StatusBadge` when scoped to invoices)
- **Hooks:** `use` prefix + PascalCase (`useAuth`, `useBilling`)
- **Utilities:** camelCase, verb-first (`formatDate`, `validateEmail`)
- **Constants:** UPPER_SNAKE_CASE for true constants; camelCase for config objects
- **Files:** Match the default export name (`InvoiceStatusBadge.tsx` exports `InvoiceStatusBadge`)

## Component Patterns

- Shared UI components in `src/components/ui/` — module-local components stay in their module directory.
- Status badges use a `variant` prop (not `color` or `type`) with predefined string literals.
- Settings pages use the `Card` component for section grouping; no bare `<div>` containers for visual sections.
- Form fields are composed from the shared field library in `src/components/forms/fields/`.

## Dependency Rules

- Modules do not import from each other directly — shared state goes through hooks in `src/hooks/`.
- Shared UI components are imported from `src/components/ui/`, never from a module's local directory.
- Date formatting uses the shared `formatDate` utility — no inline `Intl.DateTimeFormat` or `.toLocaleDateString()`.

## Error Handling

- Settings pages use optimistic updates with rollback on error.
- API errors surface via Toast component, not inline alerts.
- Form validation errors appear below the relevant field via the field component's error state.
