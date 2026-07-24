# ADN construction-permit prototypes

Three clickable HTML prototypes for the Ayuntamiento del Distrito Nacional
(ADN) *permisos de construcción* journey, in the gob.do / drimstack house
style. They answer the content review in `../REVIEW.md` — each fixes a
different cluster of problems found on the live site.

**These are throwaway alpha prototypes, not production.** Copy is plain
Spanish (usted); the framework docs here are English. Mock data is labelled
"simulado" / `.fake`. Nothing here talks to the live adn.gob.do site.

## The three hypotheses

| # | Folder | Hypothesis | Fixes (from REVIEW.md) |
|---|--------|-----------|------------------------|
| 1 | `prototype-1-pagina-de-servicio/` | **Fix the page, not the process.** The trámite stays presencial, but the service page is rebuilt: headings bound to content, requirements de-duplicated, cost/time at the top, edge cases behind progressive disclosure. | #1 empty headings, #2 duplication, #5 price typos, #6 hidden prerequisites, #7 no plain language |
| 2 | `prototype-2-reune-documentos/` | **Readiness before the form.** An interactive "reúne estos documentos" checklist that branches on what you're applying for and surfaces the full cross-institution prerequisite chain *before* you travel to Planeamiento Urbano. | #6 invisible prerequisite chain, #7 no plain-language layer |
| 3 | `prototype-3-solicitud-en-linea/` | **Take it online end-to-end.** Replaces "quemar los documentos en un CD y entregar en persona" with an online submission (GobID lookup, document upload, online payment) plus a status-tracking page for the 30–45 day wait. | #3 physical CD hand-off, #4 100% presencial + owner-only, no-visibility follow-up |

They're deliberately different bets — from "just fix the words" to "rebuild the
service". Test them to find out how far ADN needs to go.

## How to test

1. Open each `index.html` in a browser. Click through it.
2. Open it on a phone. The chrome is mobile-first; the flows should hold.
3. Toggle the **"Ver supuestos"** button (charcoal drimstack banner) to see
   every assumption the prototype makes, tagged by who needs to confirm it.
4. Run `../REVIEW.md` and `test-plan.md` with real applicants — architects,
   gestores, and property owners who've filed a permit at ADN.

Consolidated assumptions across all three: `assumptions.md`.
User-testing plan: `test-plan.md`.

## Provenance

- Source content scraped read-only from adn.gob.do on 2026-07-24 (see
  `../pages/`, `../scrape.py`).
- Built with the drimstack `brief-to-prototypes` skill and `developer` agent.
- House style: `references/house-style.md` (drimstack). Shared chrome/tokens
  in `_house-style.html`.
- Next: collect feedback, then `/drimstack:iterate` on the winning variant.
