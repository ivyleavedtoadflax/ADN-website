# ADN construction-permit content review

Scope: the *permisos de construcción* cluster on adn.gob.do (Dirección de
Planeamiento Urbano), scraped read-only on 2026-07-24. Pages in `pages/`,
raw HTML cached in `cache/`. This review is also the brief for the prototypes
in `prototypes/`.

The trámites reviewed: Anteproyecto, Certificación de Uso de Suelo, Cambio de
Uso de Suelo, Certificación de Antena, Reformulación, Remodelación y/o Anexos,
Remodelación + Cambio de Uso, Demolición, Verja, Resellado de Planos (×2).

## What works

- The full list of trámites exists and is linked from one hub
  (`servicios-planeamiento-urbano`).
- Requirements are genuinely detailed — the edge cases (heredero fallecido,
  fideicomiso, condominio, Zona Colonial/Gazcue) are all documented.
- Director, email, phone and extensions are published.

## Problems, worst first

### 1. Every service page has empty section headings
Each page renders the right structure — *Descripción del Servicio*, *A quién va
dirigido*, *Requerimientos*, *Procedimientos*, *Horario*, *Costo*, *Tiempo* —
but the headings are **blank**. The actual content sits in an undifferentiated
blob below them (an Elementor template where content isn't bound to its
headings). A citizen scanning for "cuánto cuesta" or "cuánto tarda" sees empty
headings and has to read the whole wall of text. Screen-reader users get a
heading tree that points to nothing.

### 2. Content is duplicated on the page
Requirements appear twice: once as a bulleted list, once as a paragraph blob
directly underneath. Doubles the reading load and the maintenance burden.

### 3. "Presentar en un CD" — physical media in 2026
Every trámite says: digitise all documents to PDF, put the plans in a single
AutoCAD file… then **burn it to a CD and hand it in in person**. The work is
already digital; the last step forces a physical hand-off. This is the single
biggest opportunity — the content describes a fully digital package delivered
by the least digital channel possible.

### 4. 100% presencial, owner-only follow-up
`Canal de Prestación: Presencial` for every trámite. Payment is presencial at
the caja *after* the application is reviewed. Follow-ups happen "de manera
personal única y exclusivamente por el propietario o solicitante" — no online
status, no delegation, no email update. Response time is 30–45 business days
with no visibility in between.

### 5. Price typos undermine trust
`RD$9,5OO.OO` and `RD$14,5OO.OO` use the letter **O** instead of zeros.
On a government fee schedule this reads as careless.

### 6. The prerequisite chain is invisible
To apply you need, variously: a notarised power of attorney, Certificación de
No Carga y Gravamen (< 6 months old), CODIA card copy, a current MIVED
construction licence, DNPM no-objection for heritage zones, and an ADN
solvency certificate. These are buried inline in a legalese paragraph. A
citizen can't see, up front, "here is everything you must gather before you
start" — so they arrive missing a document and lose a trip.

### 7. No plain-language layer
Requirements are written for someone who already knows the process
(architects, gestores). There's no one-line "what is this and do I need it"
for each trámite, and no distinction between the common path and the rare
edge cases (fideicomiso, heredero fallecido), which are mixed into the same
paragraph as the everyday requirements.

## The opportunity, in one line

The permit package is already digital; the service is not. Bind content to its
headings, split the common path from the edge cases with progressive
disclosure, publish a single "gather these first" checklist per trámite, and
replace the CD-in-person hand-off with an online submission and a status page.

## Prototype brief

Three prototypes in the gob.do / drimstack house style (see `prototypes/`):

1. **Service page, rebuilt** — one trámite (Uso de Suelo) with the empty
   headings filled, requirements de-duplicated, plain-language intro, and
   costs/time surfaced at the top.
2. **"Reúne estos documentos" checklist** — the prerequisite chain made
   visible up front, common path first, edge cases behind disclosure.
3. **Online submission + status** — replace "quemar un CD y entregar en
   persona" with an upload flow and a tracking page for the 30–45 day wait.
