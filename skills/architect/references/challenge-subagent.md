# Challenge Subagent

A fresh perspective on an artifact before the human reviews it. Spawned by `architect` to pressure-test the design doc (Step 4.6) and the plan doc (Step 5.1). The subagent always reads the file directly — there is no chat-only Design Summary anymore.

## Purpose

Surface decisions the original model and the developer may have both missed. A second pass from a model with different weights, given the file but **not** the prior conversation, catches blind spots that self-review cannot.

## What it gets

The challenge subagent receives:
1. **The original developer prompt** — what was asked for
2. **The file path** of the design or plan doc to review — the subagent reads it directly
3. **Repo context** — file paths, relevant existing code, conventions

The challenge subagent does NOT receive:
- The developer's prior answers to language/decisions
- The full conversation history
- A pasted copy of the document (it reads the file, you don't inline it)
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

- Rewrite the artifact
- Propose alternatives (a one-sentence hint is fine; full rewrites are the original model's job)
- Score the artifact
- Run the implementation
- Edit any file

## Output handling

The original model (architect) reads the Risk Register and decides the next move:

1. **Edit the file directly** when a finding is resolvable with information already in scope.
2. **Ask one focused clarification question** when a finding needs developer input, then update the file after the answer.
3. **Surface an `## Open Showstoppers` section** when a finding cannot be resolved in this session.
4. **Append the Risk Register** to the design or plan file and update the `## Status` block.

The challenge subagent does not edit the file, does not propose a rewritten artifact, and is not re-spawned in a loop. One review pass per artifact. Run another pass only if the developer explicitly asks for one.

## Invocation

```
Spawn a challenge subagent with the following inputs:
- Original prompt: [verbatim developer request]
- File path: [absolute path of the design or plan file to review]
- Repo context: [file paths and conventions the subagent needs]

The subagent reads the file directly — do not paste its contents.
Read the resulting Risk Register. Inline-edit the file, then hand off at the gate.
```

Use the `task` tool with `agent: "task"` and a read-only instruction set. The subagent returns the Risk Register as its final output.

## Fallback when no real subagent is available

Some environments (e.g., Claude.ai, or sessions where the `task` tool is restricted) cannot spawn a true isolated subagent. In that case, the architect model must fall back to a self-administered challenge — running the same critical pass on its own artifact, from the subagent's prompt contract (no prior conversation context, read-only stance, three-section output).

**This fallback is weaker than a real subagent** because the same weights and blind spots are doing the review. You MUST flag it explicitly in the Risk Register header so the human knows what kind of review produced the register:

```markdown
## Risk Register
> **Source:** self-administered challenge (no isolated subagent available in this environment). Treat as a sanity check, not an independent review.

### Showstoppers
...
```

The human can then decide whether to proceed or to retry in an environment with a real subagent. Do NOT silently substitute self-review for subagent review — that defeats the whole point of the mechanism.
