# Discovery Reset: Booking App

## Situation Assessment

It sounds like you're mid-implementation but the ground keeps shifting underneath you — the target user and their core need aren't locked down. That's a classic sign we need to stop building and re-anchor on **who this is for** and **what problem we're solving**, before writing another line.

Let me lay out what we likely know vs. what we need to nail down.

---

## What We Know (Facts)

- A booking app exists in some half-built state
- The target user has changed at least once during development
- The current framing is unclear enough that continuing to build risks wasting effort
- There's at least one existing implementation to evaluate against

---

## What's Unclear (Assumptions to Validate)

| Assumption | Why It Matters |
|---|---|
| We're still building a single product, not pivoting to a different app | Defines whether we salvage existing code |
| The "target user" refers to the end consumer who books, or the business/merchant offering the service | Completely changes the MVP |
| The core action is scheduling or reserving a specific time/slot | Could be asset rental, space booking, appointment setting, etc. |
| There's existing code we want to build on top of | Determines scope of reset |
| The app is mobile-first, web-first, or both | Affects UX decisions early |

---

## Needs Decision

Before we go further, I need your answers on these — they're the pillars everything else rests on:

### 1. Who is the primary user?
The person we're building for first. Pick one — not "everyone."
- A **service provider** (hairdresser, tutor, consultant) who wants to manage their availability?
- A **customer** (pet owner, student, patient) who wants to book an appointment?
- A **platform operator** who connects providers and customers?

### 2. What is the core problem this app solves?
One sentence. Example patterns:
- "I can't find available slots for [X] without calling/texting."
- "I spend hours each week manually managing my calendar and bookings."
- "I lose clients because I don't have a simple way for them to self-serve."

### 3. What does "booking" mean in your context?
- A time slot on a calendar (e.g., doctor appointment)?
- A resource or room for a window (e.g., co-working space)?
- An event ticket or slot reservation?

### 4. What's out of scope for the first release?
Equally important to define what we're NOT building yet:
- **Non-goals for V1:**
  - Payment processing
  - Multi-provider / marketplace
  - Native mobile apps
  - Cancellation/refund workflows
  - Complex availability rules (recurring schedules, blackout dates)

### 5. How will we know this works?
Success criteria we can measure:
- A specific user type can complete a booking in under 2 minutes
- The provider can see and manage incoming bookings from a dashboard
- At least N real users (e.g., 5) have used it in a real workflow

---

## Proposed Core Flow (V1)

Until you confirm, here's my best guess at the simplest useful version:

```
Provider sets availability → Customer picks a time → Both get confirmation → Done
```

That's it. No payments, no reminders, no complex scheduling. Just: **can someone book a slot with someone else?**

---

## What I Need From You

Before I move to architecture or start writing a project overview, I need you to confirm:

1. **Primary user** — who are we building for first?
2. **Core problem** — one sentence, the pain we're solving
3. **Booking type** — time slot, resource, or event?
4. **Non-goals** — what's explicitly out of scope for V1?
5. **Success metric** — how do we know this works?

Once you answer those, I'll draft a concrete product summary and we can figure out what from the existing half-built app is salvageable vs. what needs to be rethought.

Don't skip this step — building the wrong thing a second time costs more than building the right thing once.
