# Architecture

**Last Updated:** 2026-06-23

## Stack

- **Framework:** React 18 + TypeScript 5
- **Routing:** React Router v6 (file-based conventions)
- **State:** React Query (server state), React Context (UI state)
- **Styling:** CSS custom properties (design tokens) + utility classes
- **Build:** Vite 5
- **Testing:** Vitest + React Testing Library

## Module Structure

```
src/
├── components/
│   ├── ui/              # Shared UI components (Button, Card, Badge, InvoiceStatusBadge, Table, etc.)
│   └── forms/
│       └── fields/      # Shared form field components
├── modules/
│   ├── auth/            # Login, signup, session
│   ├── billing/         # Billing settings, invoice preview ← NEW MODULE
│   │   └── pages/
│   │       └── BillingSettings.tsx
│   ├── dashboard/       # Main dashboard layout
│   ├── notifications/   # Notification preferences
│   ├── team/            # Team management
│   └── user/            # User profile settings
├── lib/
│   └── utils/
│       └── dates.ts     # formatDate shared utility
├── integrations/        # External API wrappers
├── routes/              # Route definitions
└── db/                  # Schema files
```

## System Boundaries

- **Auth boundary:** `src/modules/auth/` owns login, signup, and session refresh. All other modules consume auth state via `useAuth()` hook.
- **Billing boundary:** `src/modules/billing/` owns payment settings and invoice display. Consumes auth for user context. Provides `InvoiceStatusBadge` as a shared UI component (exported from `src/components/ui/`).
- **Settings pages boundary:** `billing`, `notifications`, and `user` modules each have settings-style pages that share the Card-based layout pattern and common form fields.

## Data Model

- **users** — id, email, name, team_id, role
- **teams** — id, name, plan
- **team_members** — team_id, user_id, role, invited_at
- **notifications** — user_id, channel, enabled
- **billing** — team_id, payment_method_id, invoice_email, billing_cycle
- **invoices** — id, team_id, amount, status (paid|pending|overdue|void), issued_at, due_at

## Operational Invariants

- Session tokens refresh automatically before expiry via the auth boundary.
- All settings pages save optimistically and revert on error.
- Badge color variants (`paid`→green, `pending`→amber, `overdue`→red, `void`→gray) are token-mapped and must not be hardcoded.
