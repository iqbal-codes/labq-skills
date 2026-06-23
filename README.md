# labq-skills

Personal agentic-coding workflow skills for building software with an AI agent
as a daily driver.

This repo is for my own work first. It is not a shared playbook, not a company
standard, and not a generic prompt pack. The goal is simple: when I ask an
agent to build anything — a new app, a feature, a bug fix, a UI pass, a docs
sync, or a session handoff — it follows the same reliable workflow every time
instead of improvising from vibes.

Everything is self-contained. Copy this repo into another project, expose the
`skills/` directory to the agent, and the workflow travels with me.

## What this is

`labq-skills` is a personal operating system for agentic coding.

The skills are not magic commands. They are small workflow contracts. Each one
answers:

- when the agent should use it
- what context it must read before acting
- what it is allowed to change
- where it must stop and ask me
- what evidence it must produce before saying something is done

Without this, every session starts from scratch. The agent might jump into code
before understanding the product, skip root-cause analysis, forget to review its
own changes, or claim "done" without proof. With this repo, the agent has a
repeatable path.

## The daily-driver loop

For normal work, I want the agent to behave like this:

```text
I ask for something
   │
   ▼
using-skills
   │  routes the request to the right workflow
   ▼
context
   │  reads AGENTS.md and context/*.md when the project has them
   ▼
specialized skill
   │  discover / architect / recover / review / syncdocs / remember / etc.
   ▼
implementation
   │  only after the right planning or recovery step has happened
   ▼
verification
   │  run the specific command or scenario that proves the work
   ▼
cleanup + handoff
      update context, save memory, then report exactly what changed
```

The important part is not the names. The important part is that the agent does
not flatten every request into "edit files immediately." Different work needs
different discipline:

- fuzzy idea → discover first
- new behavior → architect first
- bug or failed test → recover first
- UI polish → impeccable first
- completed feature → review, then syncdocs
- end of session → remember save

## How the main skills work

### `using-skills`

The router. It runs at the start of non-trivial work and picks the right skill
from the request. This is what keeps me from remembering every workflow by hand.

Typical use:

```text
User: add Google login
Agent: use architect, because this is new behavior
```

```text
User: tests are failing
Agent: use recover, because this is unexpected behavior
```

### `discover`

Use this when the product idea is still fuzzy.

It slows the agent down before architecture. It asks one focused question at a
time, separates facts from assumptions, compares a few possible directions, and
turns a rough idea into approved product framing.

Use it for:

- "I want to build something like..."
- "Help me figure out the MVP"
- "This project changed direction"
- "Before we build, let's clarify who this is for"

It should not write code or design architecture. Its output is product clarity.

### `architect`

Use this before non-trivial new behavior or a multi-file refactor.

It designs before code. It aligns language, surfaces decisions, researches
unknown libraries when needed, asks a challenge subagent to produce a Risk
Register, and stops at two human gates:

1. design approval
2. plan approval

This is deliberate friction. The agent should not approve its own design and
then immediately implement it. For larger work, `architect` writes durable
design and plan files so the next session can continue without guessing.

### `bootstrap`

Use this when a project needs its agentic context loaded, checked, repaired, or
created.

It treats context files as infrastructure:

- `context/project-overview.md`
- `context/architecture.md`
- `context/ui-tokens.md`
- `context/ui-rules.md`
- `context/ui-registry.md`
- `context/code-standards.md`
- `context/library-docs.md`
- `context/build-plan.md`
- `context/progress-tracker.md`

If those files exist, bootstrap validates them. If they are missing or stale, it
reports what needs repair. If the repo is new, it can scaffold the context
backbone from repo facts instead of invention.

### `recover`

Use this for bugs, failed tests, broken behavior, and surprising state.

The rule is root cause before fix. The agent should reproduce or inspect the
failure, identify why it happens, then make the smallest real fix. No warning
suppression. No symptom patches unless that is genuinely the correct fix.

### `review`

Use this after meaningful implementation.

It is the second pair of eyes. It checks whether the change matches the plan,
whether behavior is actually covered, whether critical risks remain, and whether
the work is safe to hand back. Critical issues block completion.

### `impeccable`

Use this for frontend quality: UI design, polish, accessibility, typography,
motion, spacing, color, responsive behavior, and anti-pattern cleanup.

This skill is vendored from outside my own skill set, but it is useful in the
daily-driver workflow because visual work needs stricter taste than generic
"make it nice" prompting.

### `imprint`

Use this after building UI components.

It extracts reusable visual patterns from the component and records them in
`ui-registry.md`, so future components match what already exists. This prevents
each session from inventing a slightly different card, button, form, or badge
style.

### `syncdocs`

Use this after a feature or refactor works.

It reconciles `context/*.md` against reality. If a route, module, dependency,
UI pattern, design token, or build phase changed, the context should change too.
The point is that future sessions should read true context, not old plans.

### `remember`

Use this at session boundaries.

- `remember save` writes the essential continuation state to `memory.md`
- `remember restore` reads it at the start of the next session

It stores decisions, current state, next action, and open questions. It must not
store secrets.

## Human gates

The agent is allowed to work autonomously inside a bounded task, but some gates
exist so it does not ship surprises:

- before non-trivial implementation: design/plan approval
- before destructive changes: explicit approval
- after critical review findings: fix before continuing
- before merge or PR actions: explicit approval

These gates are for me. They are not bureaucracy. They keep the agent from
turning "help me think" into unexpected code, or turning "fix this" into a broad
rewrite.

## Verification rule

No proof, no "done."

Before the agent says something passes, it must run the specific command,
scenario, or check in the current turn and quote the actual output. For code,
that might be a unit test, typecheck, E2E flow, browser check, or targeted
script. For docs-only edits, that can be a focused read/search check showing the
requested wording and old framing are gone.

The point is not ceremony. The point is to stop false completion claims.

## How I use this in a project

1. Copy this repo or its `skills/` directory near the project.
2. Make sure the agent can load the skills.
3. Put `AGENTS.md` in the project root or adapt the one from this repo.
4. Run `bootstrap` to create or validate the `context/` backbone.
5. Start every real request normally. `using-skills` should route it.
6. Let the workflow finish: design/recover, implement, verify, review, syncdocs,
   remember.

For a brand-new project, the first path is usually:

```text
discover → architect → bootstrap → build first feature → review → syncdocs → remember
```

For an existing project with a clear request:

```text
using-skills → architect or recover → implement → verify → review → syncdocs
```

For a tiny typo or one-line change, skip the heavy path. The workflow exists to
add discipline where it matters, not to make small edits slow.

## Layout

```text
labq-skills/
├── AGENTS.md                  # session bootstrap + workflow rules
├── README.md                  # this file
├── skills/
│   ├── using-skills/          # entry point; routes to the right skill
│   ├── architect/             # design + Risk Register + plan gates
│   ├── discover/              # fuzzy product ideas → approved framing
│   ├── bootstrap/             # load / repair / scaffold project context
│   ├── recover/               # root cause before any fix
│   ├── review/                # plan / system / production readiness review
│   ├── impeccable/            # UI polish, motion, a11y, anti-patterns
│   ├── imprint/               # extract reusable UI patterns after building
│   ├── syncdocs/              # keep context files honest
│   └── remember/              # session handoff save / restore
└── *-workspace/               # eval workspaces and review artifacts when testing skills
```

Each skill directory contains a `SKILL.md` with the trigger, process, outputs,
and stop conditions for that workflow. Some skills also include `evals/`,
`references/`, `scripts/`, or helper agents.

## Skill evals

Skills should be tested like code.

The `evals/evals.json` files describe realistic prompts and expectations. A
skill-creator run executes each prompt twice:

- with the skill loaded
- without the skill, as a baseline

Then the outputs are graded and shown in an HTML review viewer. This catches two
failure modes:

- the skill does not improve the agent's behavior
- the eval is too easy and the baseline passes anyway

Current eval workspaces are local artifacts. They are useful for reviewing skill
quality, but the skills themselves live under `skills/`.

## Design preference

This repo optimizes for my default way of building:

- boring correctness before cleverness
- product clarity before architecture
- architecture before broad implementation
- root cause before patches
- verification before completion claims
- context updates before handoff
- memory saved before ending a session

That is the daily-driver contract.
