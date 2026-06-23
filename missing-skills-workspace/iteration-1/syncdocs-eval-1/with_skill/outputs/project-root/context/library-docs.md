# Library Docs

**Last Updated:** 2026-06-23

## Core Dependencies

| Library | Version | Why | Must Know |
|---------|---------|-----|-----------|
| React | 18.x | UI framework | Strict mode enabled; concurrent features safe |
| TypeScript | 5.x | Type safety | Strict mode; no `any` in new code |
| React Router | 6.x | Client routing | File-based conventions; nested layouts |
| React Query | 4.x | Server state | Cache invalidation via query keys; optimistic updates for settings |
| Vite | 5.x | Build tool | ESM-first; no CommonJS in source |

## UI Libraries

| Library | Version | Why | Must Know |
|---------|---------|-----|-----------|
| CSS Custom Properties | — | Design tokens | All colors, spacing, radii via tokens; never hardcode |

## Testing Libraries

| Library | Version | Why | Must Know |
|---------|---------|-----|-----------|
| Vitest | 1.x | Unit testing | ESM-native; use `vi.fn()` not `jest.fn()` |
| React Testing Library | latest | Component testing | Test user behavior, not implementation |

## Date/Formatting

| Library | Version | Why | Must Know |
|---------|---------|-----|-----------|
| Intl.DateTimeFormat | built-in | Date display | Wrapped by shared `formatDate` in `src/lib/utils/dates.ts`; do not use directly |
