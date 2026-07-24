# Consolidated assumptions

Every prototype surfaces its own assumptions in a toggleable panel. This is the
cross-prototype view — what the team must confirm before any of this becomes an
alpha. Tags: who needs to confirm.

## Must verify with the institución (ADN / Planeamiento Urbano)

- **Fees are current.** RD$4,500 (Uso de Suelo), RD$9,500 / RD$14,500
  (Anteproyecto, ≤2 niveles / todo tipo). Scraped 2026-07-24; may be stale.
  `[VERIFY WITH INSTITUCIÓN]`
- **The shorter Uso de Suelo requirement list is real, not a scrape artefact.**
  Uso de Suelo genuinely omits architect ID, CODIA, No Carga y Gravamen, ADN
  solvency, and AutoCAD plans that the construction trámites require. Confirm
  that's policy. `[VERIFY WITH INSTITUCIÓN]`
- **The back office can accept a digital package** (prototype 3). Planeamiento
  Urbano currently reviews physical CDs; digital-only intake is an operational
  change, not just a front-end one. `[VERIFY WITH INSTITUCIÓN]`
- **Whether ADN's own solvency certificate could be looked up** instead of the
  citizen fetching it from Recaudación. `[VERIFY WITH INSTITUCIÓN]`

## Must verify with policy / legal

- **Digital-only submission is permitted** — that the physical CD + in-person
  hand-off isn't mandated by regulation. This is the load-bearing assumption of
  prototype 3. `[VERIFY WITH POLICY]`
- **A delegate (not only the owner) may follow a solicitation.** The live site
  restricts follow-up to "única y exclusivamente por el propietario o
  solicitante". Prototype 3 assumes SMS/email updates and delegate access are
  allowed. `[VERIFY WITH POLICY]`
- **Poder notarizado business rules** — when a notarised power of attorney is
  and isn't required. `[VERIFY WITH POLICY]`

## Must verify with OGTIC / platform

- **GobID identity lookup** (cédula via JCE, RNC via DGII) is available to ADN.
  `[VERIFY WITH OGTIC]`
- **An online payment gateway** ADN can use for the fee. `[VERIFY WITH OGTIC]`
- **X-Road / interoperability** could pull *Certificación de No Carga y
  Gravamen* from the Jurisdicción Inmobiliaria and the MIVED construction
  licence, instead of the citizen carrying paper between institutions.
  `[VERIFY WITH OGTIC]`

## Must verify with users

- Whether applicants understand terms like *Mensura Catastral*, *No Carga y
  Gravamen*, *layout (dwg)* without a plain-language gloss. `[VERIFY WITH USERS]`
- Whether the readiness checklist (prototype 2) is reached *before* people start
  gathering documents, or too late to help. `[VERIFY WITH USERS]`
- Whether the real applicant is the owner or a gestor/architect acting for them
  — this changes who every screen is addressed to. `[VERIFY WITH USERS]`

## Verify with data

- Volume per trámite (which permits dominate the queue) to prioritise.
  `[VERIFY WITH DATA]`
- Realistic file sizes for AutoCAD plan sets, to size upload limits.
  `[VERIFY WITH DATA]`

## Known gaps (not modelled yet)

- Edge cases — *heredero fallecido*, *fideicomiso*, *condominio*,
  Zona Colonial / DNPM no-objection, multi-inmueble — appear in prototype 1's
  disclosure and partly in prototype 2, but the online flow (prototype 3)
  covers the **common path only**. `[KNOWN GAP]`
- No save/resume across sessions; a real permit takes days to assemble.
  `[KNOWN GAP]`
- Real ADN contact details and the real *formulario de solicitud* / *modelo de
  poder* documents aren't linked — no canonical URLs were in the scrape.
  `[KNOWN GAP]`
- The three prototypes aren't wired to each other (checklist → online form).
  `[KNOWN GAP]`
