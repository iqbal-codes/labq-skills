# Progress Tracker

**Last updated:** 2025-06-22
**Current phase:** Phase 2 — Feature Development

## Completed Features

- ✅ Project scaffolding and build pipeline (Phase 1)
- ✅ Authentication system with JWT and refresh tokens
- ✅ Database schema design and migrations
- ✅ Base UI component library (buttons, inputs, modals)
- ✅ Dashboard layout and navigation shell
- ✅ User profile settings page

## Pending Features

- ⬜ Notification system — Depends on WebSocket infrastructure.
- ⬜ Data export functionality — CSV and PDF generation.
- ⬜ Admin role management panel

## Current Status

- **Phase:** 2 — Feature Development
- **Last completed:** User profile settings page
- **Next:** Notification system (blocked on WebSocket infrastructure)

## Decisions Made During Build

1. **Auth pattern:** JWT with HttpOnly refresh cookies, access token in memory. Chosen over session-based auth for SPA compatibility.
2. **State management:** Server state via React Query, local state via Zustand. No Redux.
3. **Form system:** Shared form context using React Hook Form + Zod validation. All forms must use this pattern.
4. **Table system:** Shared table component with React Table v8. All list views must use this.
5. **CSS approach:** Tailwind utility classes with design tokens in `tailwind.config.ts`. No inline styles.

## Known Issues

- Auth token refresh race condition needs investigation (low priority)
