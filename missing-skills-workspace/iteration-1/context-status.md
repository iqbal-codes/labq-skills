# Context Status — Iteration 1

Checked during missing-skill eval work on 2026-06-23.

## Present

- `AGENTS.md`
- `skills/`
- New eval files for local non-vendored skills that lacked evals

## Missing / drift

- `context/` directory is absent.
- Required context files are absent:
  - `context/project-overview.md`
  - `context/architecture.md`
  - `context/ui-tokens.md`
  - `context/ui-rules.md`
  - `context/ui-registry.md`
  - `context/code-standards.md`
  - `context/library-docs.md`
  - `context/build-plan.md`
  - `context/progress-tracker.md`
- `skills-lock.json` is absent.
- `AGENTS.md` mentions `caveman-commit`; no matching local skill exists in `skills/`.
- `skills/imprint` exists but is not listed in the README layout section.

## Handling

No context scaffolding was performed during this eval pass. Treat context repair as a separate bootstrap/setup task.
