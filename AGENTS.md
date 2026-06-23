# AGENTS.md

Project context for this repository. The `using-skills` skill is the entry point for non-trivial work and operates independently of this file — it does not read or depend on `AGENTS.md`. This file is for humans, for context, and for tools that want project-specific overrides.

If a project-specific rule is in conflict with a universal rule in `using-skills/SKILL.md`, the project rule wins. If a rule is only in `using-skills`, it still applies here.

## Process first

`using-skills` is the entry point. Its routing map decides which specialized skill applies. Its chains section defines the canonical sequence for each trigger. Its universal guards (HITL gates, verify-before-claim, branch lifecycle, destructive-action confirmation) are the floor for this project.

This file is **not** the entry point. `using-skills` is.

## Context read order

Read these files in this exact order before implementation:

1. `context/project-overview.md`
2. `context/architecture.md`
3. `context/ui-tokens.md`
4. `context/ui-rules.md`
5. `context/ui-registry.md`
6. `context/code-standards.md`
7. `context/library-docs.md`
8. `context/build-plan.md`
9. `context/progress-tracker.md`

If any file is missing or clearly stale, repair context first before trusting implementation work. Use `bootstrap` (refresh mode) or `syncdocs` (small drift) for this.

`using-skills` delegates the read-order mechanic to `bootstrap`; the canonical 9-file order lives here in this project, not in `using-skills`.

## Project-specific rules

Universal rules (verification, branch lifecycle, HITL gates, testing discipline) are in `using-skills` and apply on top of these. The rules below are the project-specific overrides.

- Use token-based styling from `@admin-template/ui`; no hardcoded hex or raw Tailwind palette classes.
- Prefer existing package boundaries and shared utilities over new abstractions. Check `context/architecture.md` before introducing a new abstraction.
- Update `context/progress-tracker.md` after every meaningful feature (handled by `syncdocs`).
- Update `context/ui-registry.md` after every new reusable UI pattern or component (handled by `impeccable` / `syncdocs`).
- Before changing third-party-library-backed code, load the matching domain skill first when available, then check `context/library-docs.md`. The known domain library list:
  - `hono`
  - `ai-sdk`
  - `mastra`
  - `better-auth`
  - `shadcn`
  Plus anything else in `skills/` whose name matches a library or framework.
- `recover` is root-cause-first; if root-cause work stalls, the skill escalates internally. Do not guess fixes when `recover` is still working.
- `review` is mandatory after any non-trivial feature, before `syncdocs` or `remember save`. Critical-severity issues block the feature until resolved.
- For new features touching 3+ files or 2+ packages, `architect` runs in persistence mode — writes the design to `docs/designs/YYYY-MM-DD-<feature-slug>-design.md` and the plan to `docs/plans/YYYY-MM-DD-<feature-slug>-plan.md`, in that order, with the two-phase gate (design approval, then plan approval).

## Current repo reality

- Modular internal-tools platform: shell app + CRM/Inventory remote modules
- pnpm workspace with Vite+ task runner
- Backend: Hono + oRPC on apps/api
- Frontend: Vite React apps (shell-web, crm-web, inventory-web)
- Auth: Better Auth with Organization plugin
- DB: Drizzle ORM + PostgreSQL with RLS
- All code under `@admin-template/*` workspace scope

Future sessions should trust `context/` first, then verify older docs before reusing them.
