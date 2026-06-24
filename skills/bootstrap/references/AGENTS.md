# Reference — AGENTS.md

## Purpose

`AGENTS.md` is the project-level override file. It sits at the repo root and is loaded by the agent as passive context. Use it for project-local facts, constraints, and conventions — not as the workflow entry point.

Its job is to record what this project has decided that other projects would not assume. Universal routing, chains, and shared guardrails live in the skills themselves; `AGENTS.md` is only for the project-specific overrides.

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

- Context read order — the 9-file order from `bootstrap`, or a project-specific override
- Project-specific rules — only project-local overrides, facts, and conventions
- Current repo reality — the stack, the layout, the workspace boundary

## Starter template

```markdown
# AGENTS.md

Project context for this repository. Record only project-specific facts, constraints, and overrides here. Do not restate universal routing, skill chains, or guardrails from the shared skills.

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

Use this section only when the project needs a concrete read order.

## Project-specific rules

List only project-specific overrides, facts, and conventions below. Do not repeat shared rules from `using-skills`.

- [Add project-specific styling rules, e.g., "Use token-based styling from <UI library>; no hardcoded hex or raw palette classes."]
- [Add package boundary rules, e.g., "Prefer existing package boundaries and shared utilities over new abstractions."]
- [Add domain library list — frameworks / SDKs / tools that need a domain skill loaded before changes. Example: `hono`, `ai-sdk`, `mastra`, `better-auth`, `shadcn`.]
- [Add test discipline, e.g., "E2E + targeted unit; no TDD mandate."]
- [Add solution-quality posture, e.g., "Prefer the best correct maintainable solution over the cheapest-by-human-effort shortcut. Agent-assisted development makes iteration cheap, so optimize for quality, maintainability, and user value unless I explicitly ask for a temporary patch or narrower scope."]
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
