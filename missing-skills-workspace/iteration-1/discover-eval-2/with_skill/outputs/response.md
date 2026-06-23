# Discovery Session — Half-Built Booking App Reset

## Discovery framing

- **Project state:** Reset — existing half-built product needs product re-clarification before continuing
- **What we already know:** There is a half-built booking app. The target user has been changing. Implementation has already started but is directionally unstable.
- **What is still unclear:** Who the target user actually is, what problem the booking app solves for them, what the first useful version must do, and what is explicitly out of scope.
- **What this session needs to produce:** Approved product framing — target user, problem, core flow, MVP scope, non-goals, and success criteria — before any further architecture or implementation.

---

## Clarifying questions (one at a time)

I'll work through these one question at a time. Here is the first:

> **Who is the primary user of this booking app?**
>
> a) Service providers (e.g., consultants, freelancers, repair shops) who manage their own availability and accept bookings
> b) Consumers (e.g., people looking to book appointments, reservations, or classes) who search and book
> c) An internal team (e.g., a company's front desk) that books on behalf of customers
> d) A marketplace — both providers and consumers interact through the app
> e) Something else (please describe)

---

## Candidate directions

Based on the information available, here are three plausible framings — each leads to a different first useful version:

### Direction A: Provider-First MVP (Recommended)

Focus on service providers who need to manage availability and accept bookings from existing clients. The first useful version is a scheduling tool with a shareable booking link.

- **Target user:** Solo or small-team service providers (consultants, therapists, repair shops)
- **Core problem:** Scattered scheduling, back-and-forth messages to book, missed appointments
- **MVP:** Availability management + shareable booking page + basic confirmation
- **Why recommended:** Tightest scope, fastest to validate, clear revenue path (freemium scheduling tool)

### Direction B: Consumer-Facing Booking Search

Focus on end users who search for and book services by location or category. The first useful version is a search-and-book experience for a specific vertical.

- **Target user:** Consumers looking to book services (e.g., fitness classes, salon appointments)
- **Core problem:** Difficulty finding and booking available slots across providers
- **MVP:** Provider listings + availability search + one-click booking
- **Trade-off:** Requires supply (providers) before consumers get value — classic chicken-and-egg marketplace risk

### Direction C: Internal Booking Tool

Focus on a specific organization's team that manages bookings on behalf of their customers (e.g., a hotel front desk, a clinic's reception).

- **Target user:** Internal staff at a single organization
- **Core problem:** Manual booking management, no self-service for customers
- **MVP:** Staff dashboard + customer booking link + calendar integration
- **Trade-off:** Narrowest market, but simplest to build and sell to a specific org

---

## Discovery sections

### Project framing

This is a **reset** session. The booking app exists in half-built form, but the target user has been changing, which means implementation has been proceeding without stable product intent. Before more code is written, the framing needs to be locked down.

### Target user

*Needs decision.* The primary user has not been confirmed. The three candidate directions above represent the main options. The user must select one before architecture or implementation continues.

### Problem statement

*Needs decision.* The specific pain point depends on who the user is:

- **Providers:** "I lose time and bookings because scheduling is manual and scattered."
- **Consumers:** "I can't easily find and book available slots for the services I need."
- **Internal staff:** "Managing bookings manually is slow, error-prone, and doesn't scale."

### Core user flow

*Tentative, pending target user selection.* The primary flow will likely be:

1. User sets up or discovers available time slots
2. Booking is made (by provider themselves, customer, or staff)
3. Confirmation is sent
4. Appointment appears in a calendar or dashboard

The exact shape depends on Direction A, B, or C.

### MVP scope

#### In scope (common to all directions)

- Availability/scheduling management
- Booking creation (via link or direct entry)
- Basic confirmation (email or in-app notification)
- A minimal dashboard showing upcoming bookings

#### In scope (direction-dependent)

- **Direction A:** Shareable booking link, provider-side availability editor
- **Direction B:** Search/browse by service or location, consumer-facing booking UI
- **Direction C:** Staff-facing admin panel, customer-facing booking page

#### Out of scope (for this first release)

- Payments or invoicing
- Multi-tenant marketplace or directory
- Mobile native apps
- Advanced analytics or reporting
- Recurring/subscription bookings
- Integrations with third-party calendars (Google, Outlook) — unless this is the core value proposition, which needs confirmation
- Real-time features (live chat, instant notifications)
- Review/rating system
- Provider onboarding or verification flows (if marketplace)

#### First release standard

The MVP must allow a user to **set availability and have a booking completed end-to-end** with a confirmation. Without that, nothing else matters.

### Constraints and preferences

- Preferred stack: **Undecided** — this should be addressed in architecture, not here
- Fixed constraints: **None confirmed** — the half-built repo may have implicit constraints, but those belong in architecture review
- Soft preferences: **None confirmed**
- Delivery bias: **Unknown** — whether the priority is speed to validate, polish for launch, or flexibility to pivot

### Gaps and assumptions

#### Confirmed

- The app is half-built — some implementation exists
- The target user has changed at least once
- The developer wants to reset before continuing

#### Assumed

- The booking concept is stable (we are building *some* kind of booking app)
- The developer has a general domain in mind even if the specific user is fuzzy
- The existing code may need to be partially or fully discarded depending on the chosen direction

#### Needs decision

1. Who is the primary user? (Direction A, B, or C)
2. What specific domain or vertical is this for? (e.g., healthcare, fitness, consulting, restaurants, general?)
3. What does "half-built" include? (Is there existing code worth preserving, or is this closer to greenfield?)
4. What is the delivery priority — speed to validate, or a polished launch?
5. Are there hard constraints from a stakeholder, deadline, or existing tech choice?

### Recommended next step

- **Next skill:** `/architect` (after approval)
- **Why:** Once product framing is approved, the system shape needs to be designed before implementation continues. The half-built repo needs architectural review to determine what can be reused and what must be rebuilt.
- **What should be produced next:** Architecture plan including repo structure decisions, stack selection, and whether to reuse or replace existing code

---

## Approval required

> **This discovery framing is a proposal, not a decision.**
>
> Before I write the `context/project-overview.md` or recommend moving to architecture, I need you to:
>
> 1. Select a target user direction (A, B, or C) — or tell me none of them fit
> 2. Confirm or adjust the MVP scope and out-of-scope list
> 3. Surface any constraints or preferences I may have missed
>
> Once you approve, I will write the project overview and we can move to architecture.
