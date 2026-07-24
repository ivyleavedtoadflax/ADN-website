# Test plan — ADN construction-permit prototypes

The prototypes exist to produce signal, not applause. This plan says who to
recruit, what to make them do, and what counts as a real result.

## Who to recruit

The permit journey has three distinct users. Test with all three — they read
every screen differently.

| Cohort | Why | Target |
|--------|-----|--------|
| Property owners filing their first permit | The plain-language layer is for them; they don't know the jargon | 5 |
| Architects / gestores who file often | They know the process — test whether the online flow is *faster*, not just clearer | 4 |
| ADN Planeamiento Urbano counter staff | They see where applications fail today; they'll spot the back-office assumptions | 2–3 |

11–12 sessions total. That's enough to see the same problems repeat; you don't
need statistical significance at alpha.

## What to test, per prototype

Give each participant a real task, not a tour. Watch what they do, not what
they say.

**Prototype 1 — service page.** Task: "Averigüe cuánto cuesta y qué documentos
necesita para una Certificación de Uso de Suelo." Good signal: they find cost
and time in under 15 seconds; they can list the common documents without
opening the edge-case disclosures. Bad signal: they scroll past the metadata
strip; they can't tell which requirements apply to them.

**Prototype 2 — readiness checklist.** Task: "Compruebe si tiene todo lo
necesario para solicitar una remodelación." Good signal: they correctly reach a
"le faltan N documentos" state and can name what's missing and which
institution issues it. Bad signal: they think the checklist *is* the
application; they miss that No Carga y Gravamen comes from the Jurisdicción
Inmobiliaria, not ADN.

**Prototype 3 — online submission + tracking.** Task: "Solicite la
certificación en línea y luego revise en qué paso va su solicitud." Good signal:
they complete Start → confirmation without help; they understand the reference
number and that updates come by SMS/email. Bad signal: they look for somewhere
to "print and bring in a CD"; they don't trust the online payment; they can't
find the tracking page.

## What to record

- Where each participant hesitates or backtracks (the friction, not the finish).
- Every word they read aloud and stumble on — feeds the plain-language list.
- Any moment they say "but normally I would…" — that's a real-world constraint
  the prototype missed.
- Which of the tagged assumptions in each panel a participant confirms or
  breaks. Cross off `[VERIFY WITH USERS]` items as you go.

## The comparison that matters

These three aren't polish variants — they're escalating bets:
fix-the-words → fix-the-prep → fix-the-whole-service. The decision this testing
informs is **how far ADN needs to go.** If owners succeed with prototype 1
alone, the cheap fix may be enough. If they only succeed with prototype 3, the
service — not the page — is the problem.

## After testing

Bring the findings into `/drimstack:iterate` on the winning variant. Confirm
the institución- and policy-tagged assumptions in `assumptions.md` in parallel —
those need conversations, not user sessions, and prototype 3 can't become an
alpha until the digital-submission policy question is answered.
