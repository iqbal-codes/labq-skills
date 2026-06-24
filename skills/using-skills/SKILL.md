---
name: using-skills
description: Use at the start of any non-trivial task. Scans the request, picks the right skill(s) from the available toolbox, and announces the plan. Default entry point that keeps the rest of the toolbox out of your head until it matters. Fully standalone — works on any project, with or without context files.
---

You have a toolbox of specialized skills. Every one of them exists because it does a specific job better than you would ad-hoc. The trap is forgetting they exist, or asking "should I use one?" every turn. This skill removes that trap.

This skill is the **entry point** for any project. It carries the universal rules every project should follow. It does not depend on any project-level config file to function.

## Inter-Skill Awareness

This skill does not work in isolation. A few other skills own concepts `using-skills` only references:

- **`bootstrap`** owns the `context/` system — the canonical read order, the recipes for each context file, the wiring validation between the context files and the skill toolbox, and the project-level `AGENTS.md` (it both reads existing `AGENTS.md` files in projects and creates them via setup mode, using the template at `bootstrap/references/AGENTS.md`). When you need to read, scaffold, or repair context, route to `bootstrap` (route #1, or route #7 via `syncdocs`). Do not specify the read order yourself; do not invent context-file shapes. Note: `bootstrap` is the only skill in this system that knows about `AGENTS.md`. `using-skills` does not — it operates purely against `context/` and the skill toolbox. The boundary is intentional: `using-skills` is universal; `bootstrap` is project-aware.
- **`syncdocs`** owns lightweight context drift repair after a feature lands. `bootstrap` is the heavier refresh or full scaffolding; `syncdocs` is the small fix. `using-skills` routes to `syncdocs` for the small case (route #7) and to `bootstrap` for the heavy case (route #1).
- **`remember`** owns session boundaries — saving state at the end of a session, restoring state at the start of a new one. Route to it for cross-session handoff (route #8).

**Vocabulary across skills is intentional, not fragmented.** Each skill uses its own terminology for the things it owns; the shape is the same even when the words differ. Reference (not a contract — the skills may evolve these names):

| Skill | Ordered sequence | Hard rule | "Don't do this" |
|---|---|---|---|
| `using-skills` | chain | Universal Guards | (anti-patterns table) |
| `architect` | plan | (none — uses HITL gates inline) | When NOT to Use |
| `recover` | phase | The Principle | Failure Mode signs |
| `impeccable` | step | Absolute bans | Anti-patterns (in references) |
| `imprint` | flow / steps | The Rule | (no) |
| `syncdocs` | phase | (rules) | (no) |
| `remember` | (save / restore) | The Rule | Security Boundary |
| `discover` | (questions, then sections) | HARD-GATE | (anti-pattern section) |

Pick the name that fits the skill. The vocabulary is not a contract; it is a signature.

`using-skills` is the router. The other skills are the owners. If a rule lives somewhere else, point at it; do not duplicate it.

## The Rule

**Before responding to any non-trivial task, scan the request against the routing map. If a skill clearly applies, invoke it and announce which one.**

Non-trivial = anything beyond a one-line fix, a question that needs a one-paragraph answer, or pure exploration with no deliverable.

## Detect Project State

Before routing, check what the project actually has:

- `context/` folder — project context files. `bootstrap` owns the canonical read order (and the file shapes). `using-skills` does not specify the order itself — it points at `bootstrap` and stops. If the lists here and in `bootstrap` ever differ, `bootstrap` wins.
- The skill toolbox — wherever the skills are installed (commonly `.agents/skills/` or `skills/`). List what is available before routing.
- `package.json`, `pyproject.toml`, or similar — to understand the stack.

If the project has none of these, the project is greenfield — that's a `bootstrap` trigger, not a free pass to skip structure. `using-skills` does not read context files itself; it routes to `bootstrap` (or another skill) that knows how.

## Routing Map

Read top to bottom; the first match wins. If multiple could apply, run them in the order they appear.

### 1. New repo, missing context, or stale context
- "set up this project", "missing context files", "context is stale", greenfield repo, partial `context/` with stale files
→ **bootstrap** — it owns the context system: the canonical 9-file order, the references for scaffolding each file, and the wiring validation. `using-skills` is the front door; `bootstrap` is the back office.

### 2. Product idea is vague or repo purpose is fuzzy
- "let's brainstorm", "not sure what to build", "help me think this through", mid-build pivot
→ **discover**

### 3. About to build something new and there is no plan yet
- "add X", "build Y", "implement Z", new feature, behavior change, multi-file refactor
→ **architect**

### 4. UI design or polish that is purely visual (no behavior change, no new feature)
- "make it look better", "redesign X" (when X is a visual treatment, not a feature), "this UI feels off", color/spacing/motion/a11y tweaks
→ **impeccable** alone. If the UI work is part of a new feature, behavior change, or multi-file refactor, route #3 (architect) wins — `impeccable` is loaded *during* implementation in the new-feature chain, not as the only destination.

### 5. Just built something and want to verify it
- "did I do this right", "check my work", "review this feature"
→ **review**

### 6. Bug, test failure, or unexpected behavior
- "X is broken", "tests fail", "this used to work", "why is this happening"
→ **recover**

### 7. Just finished a feature or refactor
- "wrap up", "I'm done with X", need to keep context files honest
→ **syncdocs**

### 8. Session boundary
- "save where we are", "continue tomorrow", new session needing prior state
→ **remember**

### 9. Committing
- `git commit`, finishing a chunk of work, history cleanup
→ **inline** — there is no separate commit skill. Follow the commit-format guard in Universal Guards (`git commit` discipline). If the project has a commit-message convention in its `context/code-standards.md` or `context/build-plan.md`, follow that.

### 10. Third-party library, framework, or domain-specific tool
- "use library X", "how do I do Y with framework Z", anything matching a skill name in the available toolbox
→ load that skill directly (e.g., the matching library skill if installed)

### 11. Nothing clearly fits
Skip the skills and proceed using the lightest approach that respects `context/`. Say so briefly so the developer knows you considered the toolbox.

## Skill Chaining

This section defines the canonical sequence for each trigger. Announce each step as you go.

### New feature or behavior change
`architect` → implement (with `impeccable` for UI parts, and `imprint` after the UI lands to capture the visual patterns) → `review` → `syncdocs` → `remember`

If the feature has UI: load `impeccable` *during* implementation (not after `review`) — the UI is part of the feature, not a polish pass. The chain becomes: `architect` → implement (with `impeccable` for UI parts) → `review` → `syncdocs` → `remember`. See the UI chain below for the polish-only case.

**Architect writes to disk by default.** Every `architect` run produces a design file at `docs/designs/YYYY-MM-DD-<feature-slug>-design.md` and a plan file at `docs/plans/YYYY-MM-DD-<feature-slug>-plan.md`, in that order, with two human gates (design approval, then plan approval). The design and plan go through a single pressure-test pass each, with inline edits to the files based on findings — no chat-only summaries. `using-skills` defers to `architect` for the file format and gate wording.

### Bug, test failure, or unexpected behavior
`recover` (finds root cause before any fix) → fix → `review (lite)` → `syncdocs`

`recover` is root-cause-first. It escalates internally if the root cause can't be found in this session — do not start guessing fixes when `recover` is still working. Match the project's actual test discipline (e2e + targeted unit is the norm; TDD is not required).

### UI design, polish, color, motion, or accessibility
`impeccable` → implement → `imprint` (capture new visual patterns) → `review` → `syncdocs`

`impeccable` is the entry point for *visual-only* changes. It covers "build new UI" (during feature implementation, see the new-feature chain above) and "polish existing UI" (standalone). It is also the place where new reusable UI patterns are registered — update `context/ui-registry.md` after `impeccable` lands a new pattern.

### Parallel subagent work
`review (parallel mode)` after each slice + final integration `review`

When the implementation is fanned out across subagents (per the architect plan's execution mode), each independent slice goes through `review` independently before being integrated. A final integration `review` runs over the merged result. Do not skip the per-slice review just because there will be a final one — slice-level issues caught early are cheap; integration-level issues are expensive.

### New repo, missing context, or stale context
`bootstrap` (load / refresh / setup) → start

`bootstrap` is the entry point for any context work: loading existing context, refreshing partial/stale context, or scaffolding a greenfield repo. If the repo has no `context/`, `bootstrap` setup mode creates the full structure from scratch. This chain supersedes "new session" for greenfield repos.

### Product idea still fuzzy
For an existing project with a defined product but a vague feature: `discover` → `architect` → resume

For a greenfield project where the product itself is unclear: `discover` → `bootstrap` (setup mode) → `architect` for the first feature

Use when the developer says "let's brainstorm", "not sure what to build", or "help me think this through". `discover` produces a clearer framing, then either `architect` (existing project) or `bootstrap` (greenfield) takes the next step.

### Mid-session handoff
`remember save` → (new session) `remember restore` → `bootstrap` (only if context has drifted)

The handoff is two-sided: the leaving session runs `remember save` to capture state, and the next session runs `remember restore` to load it. Only run `bootstrap` again if `context/` has drifted since the save — `remember restore` already validates continuity.

### Just finished a feature or refactor
`syncdocs` → optional `remember save` if ending the session

`syncdocs` keeps `context/` honest. After it runs, update `context/progress-tracker.md` with the feature outcome and `context/ui-registry.md` if the feature introduced a reusable UI pattern. Both updates are *part of* `syncdocs`, not separate steps — the skill handles them.

### Git commit
Inline — no separate skill. Use a consistent commit message format (Conventional Commits by default, or whatever the project specifies). State the type, scope, and intent in the subject line. The body explains the why, not the what. Run `git status` and review the diff before committing; do not commit secrets, debug code, or unrelated changes that crept in.

### Domain library, framework, or domain-specific tool
Load the matching skill *first*, *then* check `context/library-docs.md` if it exists, *then* start work.

Common domain skills this routing should fire for: `hono`, `ai-sdk`, `mastra`, `better-auth`, `shadcn`, plus anything else in the toolbox whose name matches a library or framework. Route #10 covers the catch-all case; the named examples above are the project's known set and should be checked first.

If a domain library is involved but no matching skill exists, *surface that* — recommend either installing the skill or registering the project in `context/library-docs.md`. Do not silently proceed without the right context.

### New session on existing repo
`remember restore` (if a prior session saved state) → `bootstrap` (only if context has drifted) → start

If neither a prior save nor drifted context exists, skip both and start the task directly.

## Announcement Format

Before invoking a skill, say one line:

```
Using `architect` to align on the plan before any code.
```

That's the whole announcement. No rationale, no preamble, no apology. One line, then act.

## Universal Guards

These apply to **every project**. The project's own context files may add stricter rules; if so, follow them. These are the floor, not the ceiling.

### Verify before claiming done

Before any "done", "fixed", or "passes" claim, run the verification command in **the current turn** and quote the actual output. If you did not run it, you cannot claim it. This applies to tests, builds, lint, and any other success claim. No exceptions.

The failure mode this prevents: a model says "I added the test and it passes" based on a previous turn's run, or based on reading the code, or based on what should be true. Both are common and both are wrong.

### Respect the branch lifecycle

- Don't commit to `main`. Feature work goes on a branch.
- Don't create a worktree without asking. The developer may not want isolation.
- At the end of a feature, present the merge/PR/keep/discard options — don't assume which they want.

### Use a consistent commit format

Commits should follow a consistent format. The default is Conventional Commits (`<type>(<scope>): <subject>`, e.g., `feat(auth): add OAuth callback handler`). If the project's `context/code-standards.md` or `context/build-plan.md` specifies a different format, follow that.

The subject line is the *what* in imperative mood; the body is the *why*. Review `git status` and the diff before committing. Do not commit secrets, debug code, generated artifacts, or unrelated changes that crept in. If the commit touches shared state (a config file, a schema, a database migration), say so explicitly in the body.

### Confirm before destructive actions

Schema migrations, deletions, force-pushes, bulk operations, anything that touches shared state in an irreversible way: confirm with the developer first. State exactly what you're about to do and what would be lost if it's wrong. Even under time pressure (e.g., production incident), this gate is not skippable.

### Failing test before fix

For behavior changes and bug fixes, the test should fail before the fix and pass after. Match the project's actual test discipline — don't impose TDD if the project doesn't use it, but do not ship a "fix" without evidence the bug existed and is now gone. The `recover` skill is root-cause-first; do not start guessing fixes when `recover` is still working.

### Announce the skill

One line before invoking a skill. Always. The developer is tracking your decisions in real time, and unannounced actions are surprising ones.

### Read project context when it exists
If `context/` exists, read the context files in the order `bootstrap` specifies (it owns the read order; do not specify it yourself). If `context/` does not exist but there is a `README.md`, read that. Context is the operating system for the next decision — skipping it is how features stop fitting together.

### Honor project-specific rules when present

When the project's `context/` files contain project-specific rules, follow them. These are *not* defaults — they are overrides that the project has decided on. Common examples that may live in `context/code-standards.md`, `context/ui-rules.md`, or `context/ui-tokens.md` (do not assume any specific one — read the files):

- Token-based styling from a specific UI library; no hardcoded hex or raw palette classes
- A specific test framework or test discipline
- A specific commit-message format
- A list of domain libraries whose skills must be loaded first
- Workspace boundary rules (which package owns what)

If the rule is in the project's context, the rule wins. Universal guards above are the *floor*; project rules raise the ceiling.

### Human-in-the-loop gates

These cannot be skipped without explicit developer override. When you reach a gate, stop and ask:

- **Before non-trivial code is written** — wait for `architect` approval (design file approved; plan file approved). Do not start implementation against an unapproved plan.
- **Before destructive actions** — schema migrations, deletions, force-pushes, bulk operations. State what you are about to do and what is lost if it is wrong. Wait for confirmation.
- **After Critical-severity issues in `review`** — block the feature until the critical issue is resolved. Do not proceed to `syncdocs` or `remember save` with a Critical still open.
- **Before merging to `main`** — present the merge/PR/keep/discard options. Wait for the developer's call.
- **Before creating or merging a PR** — confirm the branch is ready, the tests pass, and the review is clean. Wait for the developer's go.

The developer can override any of these with an explicit statement in their message ("skip the gate, I trust you on this one"). Without that, the gate holds.

### Update context after features

After `syncdocs` lands, the context system is in sync with the code. Two updates are part of finishing a feature, not optional:

- **`context/progress-tracker.md`** — log the feature outcome, decisions made, what is next. This is the project's memory of what happened.
- **`context/ui-registry.md`** — if the feature introduced a reusable UI pattern, register it. This is how the next feature finds the pattern instead of reinventing it.

Both updates belong to `syncdocs`; the skill handles them. `using-skills` does not duplicate the work.

## Anti-Patterns

| Thought | Reality |
|---|---|
| "This is too small to need a skill" | Skills have skip rules. Invoke and let the skill decide. |
| "I remember the skill, I'll just do it" | Skills evolve. Invoke the current version. |
| "Multiple skills could apply — I'll guess" | Read the routing map top to bottom; first match wins. |
| "Let me explore first, then pick a skill" | Skills tell you how to explore. Invoke first. |
| "I'll skip the announcement" | One line keeps the developer oriented. Always announce. |
| "No context files exist, so I can ignore the rules" | The universal guards are in this skill. They always apply. |
| "No context files exist, so I'll invent project rules" | Don't. Use the universal defaults. |

## When You Skip

If the request is truly trivial (a typo, a one-line answer, a factual lookup with no action), skip the routing. Trivial ≠ everything else. Use judgment; the developer will tell you if you over-route.
