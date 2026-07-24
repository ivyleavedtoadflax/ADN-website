"""Polite, GET-only scraper for adn.gob.do construction-permit pages.

Reads a list of URLs, fetches each once (cached to cache/), extracts the main
content, and writes clean markdown to pages/. Rate-limited and identifies itself.

    uv run scrape.py            # scrape the construction-permit URL set
    uv run scrape.py URL ...    # scrape specific URLs

ponytail: WordPress serves static HTML — httpx + selectolax, no browser needed.
Never POSTs; the mayor's inbox / checkout forms stay untouched.
"""

import hashlib
import re
import sys
import time
from pathlib import Path

import httpx
from selectolax.parser import HTMLParser

UA = "ADN-content-review-bot (matt@mattupson.com; polite, read-only)"
DELAY = 1.5  # seconds between requests — be gentle
CACHE = Path(__file__).parent / "cache"
PAGES = Path(__file__).parent / "pages"

# The permisos-de-construcción cluster (planeamiento urbano), from the sitemap.
CONSTRUCTION_URLS = [
    "https://adn.gob.do/planeamiento-urbano/",
    "https://adn.gob.do/planeamiento-urbano-2/",
    "https://adn.gob.do/servicios-planeamiento-urbano/",
    "https://adn.gob.do/servicios-planeamiento-urbano/",
    "https://adn.gob.do/construccion/",
    "https://adn.gob.do/solicitud-de-anteproyecto/",
    "https://adn.gob.do/solicitud-de-certificacion-de-uso-de-suelo-2/",
    "https://adn.gob.do/solicitud-de-certificacion-cambio-de-uso-de-suelo-2/",
    "https://adn.gob.do/solicitud-de-certificacion-de-antena/",
    "https://adn.gob.do/solicitud-de-reformulacion/",
    "https://adn.gob.do/solicitud-de-remodelacion-y-o-anexos/",
    "https://adn.gob.do/solicitud-de-remodelacion-y-cambio-de-uso-de-suelo/",
    "https://adn.gob.do/solicitud-de-demolicion/",
    "https://adn.gob.do/solicitud-de-verja/",
    "https://adn.gob.do/solicitud-de-resellado-planos-por-cambio-de-propietario/",
    "https://adn.gob.do/solicitud-de-resellado-planos-por-carta-de-mived/",
    "https://adn.gob.do/vaciados-de-hormigon/",
    "https://adn.gob.do/convocatoria-vista-publica/",
    "https://adn.gob.do/notificacion-a-colindantes/",
    "https://adn.gob.do/formulario-solicitud-tramite/",
    "https://adn.gob.do/normativas-urbanas/",
    "https://adn.gob.do/planos-pot-plan-de-ordenamiento-territorial/",
    "https://adn.gob.do/proyectos-en-discusion/",
    "https://adn.gob.do/servicios/",
]


def slug(url: str) -> str:
    s = url.rstrip("/").split("/")[-1] or "home"
    return re.sub(r"[^a-z0-9-]", "-", s.lower())[:80]


def fetch(client: httpx.Client, url: str) -> str:
    """Fetch a URL, caching raw HTML by URL hash. Returns HTML."""
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    cached = CACHE / f"{key}.html"
    if cached.exists():
        return cached.read_text(encoding="utf-8")
    time.sleep(DELAY)
    r = client.get(url, follow_redirects=True)
    r.raise_for_status()
    cached.write_text(r.text, encoding="utf-8")
    return r.text


def extract(html: str, url: str) -> str:
    """Pull title + main content into markdown-ish text."""
    tree = HTMLParser(html)
    for tag in tree.css("script, style, nav, footer, header, .elementor-widget-nav-menu"):
        tag.decompose()
    title = (tree.css_first("h1") or tree.css_first("title"))
    title = title.text(strip=True) if title else url

    # Prefer WordPress/Elementor main content containers; fall back to <main>/body.
    main = (
        tree.css_first("main")
        or tree.css_first("article")
        or tree.css_first(".elementor-section-wrap")
        or tree.body
    )
    lines = []
    for node in main.css("h1, h2, h3, h4, li, p, td, a"):
        text = node.text(strip=True)
        if not text or len(text) < 2:
            continue
        tag = node.tag
        if tag.startswith("h"):
            lines.append(f"\n{'#' * int(tag[1])} {text}")
        elif tag == "li":
            lines.append(f"- {text}")
        elif tag == "a":
            href = node.attributes.get("href", "")
            if href and (href.endswith(".pdf") or "wp-file-download" in href):
                lines.append(f"- [PDF] {text} → {href}")
        else:
            lines.append(text)

    # De-dupe consecutive repeats (Elementor duplicates content across breakpoints).
    out, prev = [], None
    for ln in lines:
        if ln != prev:
            out.append(ln)
        prev = ln
    return f"# {title}\n\n<{url}>\n\n" + "\n".join(out)


def main(urls):
    CACHE.mkdir(exist_ok=True)
    PAGES.mkdir(exist_ok=True)
    seen = set()
    with httpx.Client(headers={"User-Agent": UA}, timeout=30) as client:
        for url in urls:
            if url in seen:
                continue
            seen.add(url)
            try:
                html = fetch(client, url)
            except Exception as e:  # noqa: BLE001
                print(f"FAIL {url}: {e}", file=sys.stderr)
                continue
            md = extract(html, url)
            out = PAGES / f"{slug(url)}.md"
            out.write_text(md, encoding="utf-8")
            print(f"OK   {url} -> pages/{out.name} ({len(md)} chars)")


if __name__ == "__main__":
    main(sys.argv[1:] or CONSTRUCTION_URLS)
