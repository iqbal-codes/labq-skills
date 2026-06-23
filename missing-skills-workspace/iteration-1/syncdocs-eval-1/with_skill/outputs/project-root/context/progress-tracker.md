# Progress Tracker

**Last Updated:** 2026-06-23

## Current Status

- **Phase:** Billing & Subscription
- **Last Completed:** Billing settings page, InvoiceStatusBadge component
- **Next:** Subscription plan management, payment method persistence

## Completed Features

- [x] Project scaffolding and module structure
- [x] Authentication flow (login, signup, session management)
- [x] Dashboard layout and navigation shell
- [x] User profile settings page
- [x] Team management module (invite, roles, permissions)
- [x] Notification preferences page
- [x] Billing settings page — added 2026-06-23
- [x] InvoiceStatusBadge reusable component — added 2026-06-23

## Pending Features

- [ ] Subscription plan management (upgrade/downgrade/cancel)
- [ ] Payment method persistence (add/edit/remove cards)
- [ ] Invoice history and PDF export
- [ ] Tax configuration per region
- [ ] Webhook endpoint for payment events

## Decisions Made During Build

- Badge component uses variant prop (`paid`, `pending`, `overdue`, `void`) mapped to token colors.
- Billing settings page follows the same card-based layout as notification preferences for consistency.
- InvoiceStatusBadge is placed in `src/components/ui/` (not module-local) because it is reused across billing and accounting views.
- Date formatting on billing pages uses the shared `formatDate` utility from `src/lib/utils/dates.ts`.

## Drift Log

| Date | File | Drift | Resolution |
|------|------|-------|------------|
| 2026-06-23 | progress-tracker.md | Billing settings page and InvoiceStatusBadge were not marked complete | Moved from pending to completed |
