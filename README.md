# ADN scraper + content review

Polite, read-only scrape of the **Ayuntamiento del Distrito Nacional**
(adn.gob.do) construction-permit content, a content review of what's there, and
three clickable prototypes of a better version in the gob.do / drimstack style.

## Layout

| Path | What |
|------|------|
| `scrape.py` | Polite GET-only scraper (httpx + selectolax). 1.5s delay, caches raw HTML, respects robots.txt. Never POSTs. |
| `cache/` | Raw HTML cache (gitignored) |
| `pages/` | Extracted markdown, one file per scraped page |
| `REVIEW.md` | Content review of the permit pages — the problems, worst first. Doubles as the prototype brief. |
| `prototypes/` | Three clickable HTML prototypes + README, assumptions, test plan |

## Run the scraper

```bash
uv run scrape.py            # the construction-permit URL set
uv run scrape.py URL ...    # specific URLs
```

Scope: the *permisos de construcción* cluster (Dirección de Planeamiento
Urbano), not the whole 640-post site. Scraped 2026-07-24.

## The short version

The permit pages describe a process that's already digital — everything is
"digitalizado en PDF" — but delivered by the least digital channel possible:
burn it to a CD, hand it in in person, pay at the caja, then wait 30–45 days
with no way to check progress unless you're the owner and you turn up. On top of
that the pages themselves have empty section headings, duplicated content, and
price typos (`RD$9,5OO`).

`REVIEW.md` has the full findings. `prototypes/` shows three escalating fixes —
from rewriting the page to taking the whole trámite online.
