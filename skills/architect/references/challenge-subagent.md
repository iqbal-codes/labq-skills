# Challenge Subagent

A fresh perspective on a design before the human reviews it. Spawned by `architect` at the design review gate (Step 4.7) and at the start of persistence mode (Step 5.5 Phase A).

## Purpose

Surface decisions the original model and the developer may have both missed. A second pass from a model with different weights, given the design but **not** the prior conversation, catches blind spots that self-review cannot.

## What it gets

The challenge subagent receives:
1. **The original developer prompt** — what was asked for
2. **The Design Summary** — what the model proposed (language, decisions, assumptions, out-of-scope)
3. **Repo context** — file paths, relevant existing code, conventions

The challenge subagent does NOT receive:
- The developer's prior answers to language/decisions
- The full conversation history
- Access to write or edit files (read-only role)

## What it produces

A **Risk Register** with three sections. Use the template below exactly.

```markdown
## Risk Register

### Showstoppers
- **[Decision or assumption]** — [what would have to be true for this to be wrong, and why you believe it might be]. Impact: [scope change / blocking issue].

### Concerns
- **[Decision or assumption]** — [what could go wrong, in a survivable way]. Impact: [extra work / risk if ignored].

### Acceptable
- [Minor notes that don't change scope but show the design was actually engaged with. e.g. "Decision X is fine for v1 but won't scale to 10k users."]
```

If the subagent finds no showstoppers, the Showstoppers section is empty (not absent). Same for Concerns and Acceptable — all three headers are always present.

## What it does NOT do

- Rewrite the design
- Propose alternatives (a one-sentence hint is fine; full rewrites are the original model's job)
- Score the design
- Run the implementation
- Edit any file

## Output handling

The original model (architect) reads the Risk Register and:
1. **If Showstoppers is non-empty:** revise the design to address them, re-spawn the challenge subagent with the revised design, and re-present. Loop until Showstoppers is empty.
2. **If Showstoppers is empty:** append the Risk Register to the Design Summary (inline) or to the design file (persistence) and present to the human.

## Invocation

```
Spawn a challenge subagent with the following inputs:
- Original prompt: [verbatim developer request]
- Design summary: [the proposed Design Summary]
- Repo context: [file paths and conventions the subagent needs]

Read the resulting Risk Register. Address Showstoppers or append the register to the design.
```

Use the `task` tool with `agent: "task"` and a read-only instruction set. The subagent returns the Risk Register as its final output.

## Fallback when no real subagent is available

Some environments (e.g., Claude.ai, or sessions where the `task` tool is restricted) cannot spawn a true isolated subagent. In that case, the architect model must fall back to a self-administered challenge — running the same critical pass on its own design, from the subagent's prompt contract (no prior conversation context, read-only stance, three-section output).

**This fallback is weaker than a real subagent** because the same weights and blind spots are doing the review. You MUST flag it explicitly in the Risk Register header so the human knows what kind of review produced the register:

```markdown
## Risk Register
> **Source:** self-administered challenge (no isolated subagent available in this environment). Treat as a sanity check, not an independent review.

### Showstoppers
...
```

The human can then decide whether to proceed or to retry in an environment with a real subagent. Do NOT silently substitute self-review for subagent review — that defeats the whole point of the mechanism.
