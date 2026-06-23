# Discovery: Customer Churn Understanding Tool

## Discovery framing

- **Project state:** uncertain scope — product idea exists (internal tool for support team to understand customer churn), but target users, MVP scope, core workflows, and success criteria are still vague.
- **What developer already knows:**
  - Tool is for the support team
  - Purpose: understand customer churn
  - It is an internal tool (not customer-facing)
  - Developer knows the general domain but not the MVP shape
- **What is still unclear:**
  - What specific churn questions does the support team need answered?
  - Who exactly uses this — individual support reps, team leads, managers?
  - What data sources exist (CRM, support tickets, billing, product usage)?
  - What does "understand churn" mean operationally — identify at-risk customers, explain why customers left, predict future churn, or something else?
  - What decisions will users make based on this tool's output?
  - What constraints exist (existing stack, deployment, compliance)?
- **What this session needs to produce:** approved product framing — problem statement, target user, core workflow, MVP scope, non-goals, and constraints — before any architecture or implementation.

---

## First clarifying question

Before we go further, I want to understand the core problem more precisely. When you say your support team needs to "understand customer churn," which of these best describes what they'd actually do with the tool?

**A)** **Identify at-risk customers before they leave** — surface signals (dropped usage, repeated complaints, billing issues) so reps can intervene proactively.

**B)** **Explain why customers left after the fact** — analyze churned accounts to find patterns (common complaints, feature gaps, pricing issues) and improve retention strategy.

**C)** **Both** — monitor current customer health AND analyze historical churn patterns.

**D)** Something else entirely — describe what the team would do differently if they had this tool.

One answer is fine; we can refine from there.
