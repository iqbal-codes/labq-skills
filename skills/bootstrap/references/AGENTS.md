# Reference — AGENTS.md

## Purpose

`AGENTS.md` is the project-level override file. It sits at the repo root and is loaded by the agent as **passive context** — always in scope, but not the entry point. The entry point for any non-trivial work is the `using-skills` skill.

Its job is to record the project-specific rules that are not universal — the things this particular project has decided, that no other project would assume. Universal rules (verify-before-claim, branch lifecycle, HITL gates, destructive-action confirmation, the routing map, the chains) live in the skills themselves; `AGENTS.md` is only for the project-specific overrides.

## When to create

Create `AGENTS.md` when bootstrapping a greenfield project (`bootstrap` setup mode) and the developer wants project-level context. If the developer does not want a `AGENTS.md` for this project, do not create one — the skills work standalone without it.

If `AGENTS.md` already exists in the project, **read it and respect it** (it overrides the defaults). Do not silently rewrite.

## What must be factual

These sections should be grounded in observable repo or user-provided facts:

- the project's actual stack (frameworks, languages, package manager)
- the project's actual folder structure
- the project's actual workspace boundary (if a monorepo, which packages own what)
- the project's actual auth, database, and deployment model — only if known
- the project's actual domain library list (frameworks / SDKs / tools that need a domain skill loaded before changes)

## What may be proposed for confirmation

These can be drafted as hypotheses and marked for confirmation if they are not obvious:

- exact tooling beyond what is observable
- success criteria for the project
- team conventions (commit-message format, branch naming) unless already documented in `context/code-standards.md`

## Suggested sections

- Project entry point — `using-skills` is the entry point; this file is project context, not a router
- Context read order — the 9-file order from `bootstrap`, or a project-specific override
- Project-specific rules — overrides to the universal guards in `using-skills`
- Current repo reality — the stack, the layout, the workspace boundary

## Starter template

```markdown
# AGENTS.md

Project context for this repository. The `using-skills` skill is the entry point for non-trivial work and operates independently of this file — it does not read or depend on `AGENTS.md`. This file is for humans, for context, and for project-specific overrides.

If a project-specific rule is in conflict with a universal rule in `using-skills`, the project rule wins. If a rule is only in `using-skills`, it still applies here.

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

- [Add project-specific styling rules, e.g., "Use token-based styling from <UI library>; no hardcoded hex or raw palette classes."]
- [Add package boundary rules, e.g., "Prefer existing package boundaries and shared utilities over new abstractions."]
- [Add domain library list — frameworks / SDKs / tools that need a domain skill loaded before changes. Example: `hono`, `ai-sdk`, `mastra`, `better-auth`, `shadcn`.]
- [Add test discipline, e.g., "E2E + targeted unit; no TDD mandate."]
- [Add commit / branch conventions, e.g., "Conventional Commits; feature branches off `main`; squash-merge."]
- [Add any rule that is project-specific and would not apply to other projects.]

## Current repo reality

- [Stack: languages, frameworks, package manager]
- [Layout: monorepo or single-package; workspace boundary if monorepo]
- [Auth, database, deployment if known]
- [Workspace scope, e.g., "All code under `@<scope>/*`"]

Future sessions should trust `context/` first, then verify older docs before reusing them.
```

## Drafting rule

`AGENTS.md` is **project documentation for the consumer project**, not for the skills distribution. Do not copy this skills repo's content into it. Pull facts from the consumer project's actual code, structure, and conventions. If something is unknown, mark it for confirmation — do not invent.

`AGENTS.md` is the only file that should contain project-specific overrides to the universal guards in `using-skills`. If a rule is universal (applies to every project), it belongs in `using-skills`, not here. If a rule is project-specific, it belongs here, not in `using-skills`.
