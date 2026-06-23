I checked the project state.

What exists:
- context/project-overview.md
- context/architecture.md
- context/ui-tokens.md
- context/ui-rules.md
- context/ui-registry.md
- context/code-standards.md
- context/library-docs.md
- context/build-plan.md
- context/progress-tracker.md

What is missing or drifting:
- AGENTS.md — not present; canonical read order must be inferred
- .agents/skills/ — not present; no local skills directory
- skills-lock.json — not present; no lockfile for skill registry
- memory.md — not present; no cross-session handoff file

Mode selected: **bootstrap**

Why:
All nine context files exist and form a complete context backbone. The main job is to read and validate them, not to create or repair them. The absence of AGENTS.md, .agents/skills/, skills-lock.json, and memory.md means some wiring components are missing, but the core context system is intact and the correct mode is bootstrap.

---

Reading context files in canonical order (AGENTS.md absent, using default order):

1. `context/project-overview.md` — present
2. `context/architecture.md` — present
3. `context/ui-tokens.md` — present
4. `context/ui-rules.md` — present
5. `context/ui-registry.md` — present
6. `context/code-standards.md` — present
7. `context/library-docs.md` — present
8. `context/build-plan.md` — present
9. `context/progress-tracker.md` — present

### Wiring validation

- **AGENTS.md**: Not present. Without AGENTS.md, the documented context read order cannot be verified against actual files. The canonical order used above is the skill's default. Recommendation: create AGENTS.md that documents the context read order and lists the project's skills.
- **.agents/skills/**: Not present. No local skill directory exists. If the project uses local skills, this directory should be created.
- **skills-lock.json**: Not present. No lockfile to compare against actual skill directories.
- **memory.md**: Not present. No cross-session handoff file. If the project needs session continuity, consider adding one.
- **build-plan.md vs progress-tracker.md**: Should be checked for agreement on current phase and status. Both files exist; their consistency depends on their contents (not verified here as this is a stateless simulation).

### Recommended repairs

1. Create `AGENTS.md` to document the context read order and list installed skills.
2. Create `.agents/skills/` directory if local skills will be used.
3. Create `skills-lock.json` to track skill versions.
4. Consider adding `memory.md` if cross-session state handoff is needed.

---

## Bootstrap Report — [Project Name]

### Context files

- project-overview.md — present
- architecture.md — present
- ui-tokens.md — present
- ui-rules.md — present
- ui-registry.md — present
- code-standards.md — present
- library-docs.md — present
- build-plan.md — present
- progress-tracker.md — present

### Skills and wiring

- AGENTS.md — missing
- .agents/skills — missing
- skills-lock.json — missing

### Current execution state

- Current phase: Unable to determine without reading progress-tracker.md contents
- Last completed: Unable to determine without reading progress-tracker.md contents
- Next: Unable to determine without reading progress-tracker.md contents
- Memory state: absent

### Risks or drift

- No AGENTS.md means future sessions cannot rely on a documented read order or skill list — each session must re-derive context from the skill defaults.
- No skills-lock.json means skill versions are not tracked; a skill update could drift silently.
- No memory.md means no cross-session handoff; each session starts from scratch.
- build-plan.md and progress-tracker.md agreement cannot be validated without reading their contents.

### Recommended next action

Create `AGENTS.md` as the first follow-up. It should document the context read order, list the project's skills, and reference the skills-lock.json file. This closes the biggest gap in the wiring and gives future sessions a reliable entry point.
