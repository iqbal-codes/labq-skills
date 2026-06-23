# labq-skills

Curated, vendored copy of the agentic-coding skills our team uses inside the
labq-modules monorepo. Everything here is self-contained — drop the folder
into another project (or load its skills into a fresh agent session) and the
same workflow contracts travel with it.

## What this is, and why it pays off

Good agentic work is not "prompt the model and hope." It is a **repeatable
workflow** with named handoffs: who scopes the work, who verifies, who keeps
context honest, who handles the handoff to the next session. Each skill in
`skills/` is one node in that graph.

Why this is worth doing:

- **Consistency across sessions.** A new session opens and immediately knows
  how to start (`using-skills`), where to read context from (`AGENTS.md`
  context order), and which skill owns which job. No reinventing the loop.
- **Explicit gates, not vibes.** `AGENTS.md` lists the human-in-the-loop gates
  — architect approval before non-trivial code, `review` before `syncdocs`
  or `remember`, Critical-severity blocks until resolved. Skills make the
  gate enforceable instead of "we should probably check."
- **Design before code, with a second pair of eyes.** The `architect` skill
  does not let the model write the plan that just self-approved the design.
  A challenge subagent produces a Risk Register (Showstoppers / Concerns /
  Acceptable) on the design before it reaches the human, and the plan is only
  drafted after the human approves the design. The check is structural, not
  rhetorical.
- **Verification as a first-class step.** The verification rule is hard:
  quote the actual command output in the same turn as the success claim.
  This is how agentic code stops shipping false "done" reports.
- **Parallel work without collisions.** `dispatching-parallel-agents` and the
  parallel `review` mode let slices land in one batch and still get
  integrated cleanly.
- **Domain-aware.** Library-backed code (Hono, AI SDK, Mastra, Better Auth,
  shadcn, Vercel React) has a matching skill you load **before** touching
  the file — so the agent is current on APIs and known gotchas instead of
  guessing from stale training data.
- **Context that stays true.** `syncdocs` (after every feature) and
  `remember` (across sessions) keep the project's own docs aligned with
  reality. No drift, no "context files that lie."

## How a request flows

```
user request
   │
   ▼
using-skills  ──►  picks the right specialized skill
   │
   ▼
AGENTS.md context read order  ──►  context/ files are the project's OS
   │
   ▼
architect
  ├─ Step 1: research unfamiliar libs (skip for well-known territory)
  ├─ language alignment + decisions
  ├─ challenge subagent  ──►  Risk Register (Showstoppers / Concerns / Acceptable)
  ├─ ★ DESIGN REVIEW GATE  ──►  human approves design before plan is written
  └─ plan + execution mode menu  ──►  ★ PLAN GATE  ──►  human approves plan
   │
   ▼
skill chain (implement → review → impeccable → syncdocs → remember)
   │
   ▼
verification in this turn, output quoted, then "done"
```

`★` marks human-in-the-loop checkpoints. Architect has two of them in sequence:
after the design (with the challenge subagent's Risk Register attached) and
after the plan. Neither checkpoint can be skipped — the next stage's output
is not produced until the human has approved the previous one.

For bugs the chain is `recover → fix → review (lite) → syncdocs`. For UI work
it is `impeccable → implement → review → syncdocs`. The chains are listed
in `AGENTS.md` under *Skill triggers*.

## Layout

```
labq-skills/
├── AGENTS.md                  # session bootstrap + workflow rules
├── README.md                  # this file
└── .agents/skills/
    ├── using-skills/          # entry point; routes to the right skill
    ├── architect/             # design + Risk Register + plan, two HITL gates, persistence mode for big features
    ├── discover/              # fuzzy product ideas → approved framing
    ├── bootstrap/             # load / repair / scaffold project context
    ├── recover/               # root-cause before any fix
    ├── review/                # plan / system / production readiness gates
    ├── impeccable/            # UI polish, motion, a11y, anti-patterns
    ├── imprint/               # extract reusable UI patterns after building
    ├── syncdocs/              # keep context files honest
    └── remember/              # session handoff save / restore
```

Each skill directory contains a `SKILL.md` describing when to trigger it,
what it produces, and the contracts it expects from other skills.

## Using this in another project

1. Copy `labq-skills/` next to (or into) the target repo.
2. Make sure the agent loads skills from `.agents/skills/`.
3. Adopt the `AGENTS.md` context read order — replace `context/` references
   with the target project's own docs (or scaffold them via `bootstrap`).
4. Honor the human-in-the-loop gates. They are the difference between an
   agent that helps and one that ships surprise.

If a needed skill is missing, the workflow still runs — it just routes
around the gap. When you write a new skill that fits the model, vendor it
here so the next session inherits it.
