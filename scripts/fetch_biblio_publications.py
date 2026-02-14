#!/usr/bin/env python3
"""Fetch VIGILIA publications from UGent biblio and write _data/publications.yml.

The script is intentionally conservative and works with a configurable source URL.
Default URL targets records mentioning grant id 101142229.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_FILE = REPO_ROOT / "_data" / "publications.yml"
DEFAULT_QUERY = "101142229"
DEFAULT_URL = (
    "https://biblio.ugent.be/publication?f[funding_info][0]="
    + quote_plus(DEFAULT_QUERY)
    + "&format=json"
)


@dataclass
class Publication:
    title: str
    authors: str
    venue: str
    year: int | None
    url: str


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": "VIGILIA-site-bot/1.0"})
    with urlopen(req, timeout=30) as resp:  # nosec B310
        return resp.read().decode("utf-8", errors="replace")


def parse_json(payload: str) -> list[Publication]:
    raw = json.loads(payload)
    if isinstance(raw, dict):
        raw = raw.get("results", [])
    pubs: list[Publication] = []
    for item in raw:
        title = item.get("title") or item.get("name") or "Untitled"
        authors = item.get("authors") or item.get("author") or ""
        if isinstance(authors, list):
            authors = ", ".join(a.get("full_name", str(a)) if isinstance(a, dict) else str(a) for a in authors)
        year = item.get("year") or item.get("publication_year")
        try:
            year = int(year) if year is not None else None
        except (TypeError, ValueError):
            year = None
        venue = item.get("journal") or item.get("booktitle") or item.get("type") or ""
        url = item.get("url") or item.get("handle") or ""
        pubs.append(Publication(str(title), str(authors), str(venue), year, str(url)))
    return pubs


def parse_html(payload: str) -> list[Publication]:
    pubs: list[Publication] = []
    for match in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', payload, flags=re.I):
        href, title = match.groups()
        if "/publication/" not in href:
            continue
        pubs.append(Publication(title=title.strip(), authors="", venue="", year=None, url=href.strip()))
    unique = []
    seen = set()
    for p in pubs:
        if p.url in seen:
            continue
        seen.add(p.url)
        unique.append(p)
    return unique


def to_yaml(publications: list[Publication]) -> str:
    lines = []
    for pub in publications:
        d = asdict(pub)
        lines.append("- title: \"{}\"".format(d["title"].replace('"', "\\\"")))
        lines.append("  authors: \"{}\"".format(d["authors"].replace('"', "\\\"")))
        lines.append("  venue: \"{}\"".format(d["venue"].replace('"', "\\\"")))
        lines.append(f"  year: {d['year'] if d['year'] is not None else 'null'}")
        lines.append("  url: \"{}\"".format(d["url"].replace('"', "\\\"")))
    return "\n".join(lines) + ("\n" if lines else "[]\n")


def main() -> int:
    source_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    payload = fetch(source_url)

    pubs: list[Publication]
    try:
        pubs = parse_json(payload)
    except json.JSONDecodeError:
        pubs = parse_html(payload)

    OUT_FILE.write_text(to_yaml(pubs), encoding="utf-8")
    print(f"Wrote {len(pubs)} publication(s) to {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
