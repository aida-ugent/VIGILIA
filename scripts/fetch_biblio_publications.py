#!/usr/bin/env python3
"""Fetch VIGILIA publications from UGent biblio and write _data/publications.yml.

Preferred source: UGent biblio JSON endpoint:
  https://biblio.ugent.be/publication?format=json&text=<query>

This endpoint is used with VIGILIA-related project/grant identifiers. If the JSON
endpoint becomes unavailable or returns non-JSON, the script falls back to a small
HTML parser as a last resort.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_FILE = REPO_ROOT / "_data" / "publications.yml"
BASE_URL = "https://biblio.ugent.be/publication"
DEFAULT_IDENTIFIERS = [
    "101142229",  # ERC grant id
    "VIGILIA",  # project acronym
    "ERC Advanced Grant VIGILIA",
    "Tijl De Bie",  # PI fallback to keep page populated while grant tagging catches up
]


@dataclass
class Publication:
    title: str
    authors: str
    venue: str
    year: int | None
    url: str


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": "VIGILIA-site-bot/1.1"})
    with urlopen(req, timeout=30) as resp:  # nosec B310
        return resp.read().decode("utf-8", errors="replace")


def _stringify_authors(value: object) -> str:
    if isinstance(value, list):
        rendered: list[str] = []
        for author in value:
            if isinstance(author, dict):
                rendered.append(
                    str(
                        author.get("full_name")
                        or author.get("name")
                        or author.get("name_last_first")
                        or ""
                    ).strip()
                )
            else:
                rendered.append(str(author).strip())
        return ", ".join(x for x in rendered if x)
    if isinstance(value, dict):
        return str(value.get("name") or value.get("full_name") or "").strip()
    return str(value or "").strip()


def _extract_venue(item: dict) -> str:
    for key in (
        "journal_title",
        "journal",
        "journal_abbreviation",
        "book_title",
        "booktitle",
        "event_title",
        "publisher",
        "type",
    ):
        venue = item.get(key)
        if isinstance(venue, str) and venue.strip():
            return venue.strip()

    external = item.get("external")
    if isinstance(external, dict):
        for key in ("source", "journal", "title"):
            venue = external.get(key)
            if isinstance(venue, str) and venue.strip():
                return venue.strip()
    return ""


def _extract_year(item: dict) -> int | None:
    for key in ("year", "publication_year", "date_published", "publication_date"):
        value = item.get(key)
        if value is None:
            continue
        if isinstance(value, int):
            return value
        match = re.search(r"(19|20)\d{2}", str(value))
        if match:
            return int(match.group(0))
    return None


def _canonical_url(item: dict) -> str:
    candidates = [
        item.get("url"),
        item.get("handle"),
        item.get("permalink"),
    ]
    for candidate in candidates:
        if isinstance(candidate, str) and candidate.strip():
            return candidate.strip()

    biblio_id = item.get("biblio_id") or item.get("id") or item.get("_id")
    if biblio_id:
        return f"https://biblio.ugent.be/publication/{biblio_id}"
    return ""


def parse_json(payload: str) -> list[Publication]:
    raw = json.loads(payload)
    if isinstance(raw, dict):
        raw = raw.get("results") or raw.get("hits") or raw.get("items") or []
    if not isinstance(raw, list):
        return []

    pubs: list[Publication] = []
    for item in raw:
        if not isinstance(item, dict):
            continue

        title = str(item.get("title") or item.get("name") or "Untitled").strip()
        authors = _stringify_authors(item.get("authors") or item.get("author") or "")
        venue = _extract_venue(item)
        year = _extract_year(item)
        url = _canonical_url(item)

        pubs.append(
            Publication(
                title=title,
                authors=authors,
                venue=venue,
                year=year,
                url=url,
            )
        )
    return pubs


def parse_html(payload: str) -> list[Publication]:
    pubs: list[Publication] = []
    for match in re.finditer(
        r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>',
        payload,
        flags=re.I,
    ):
        href, title = match.groups()
        if "/publication/" not in href:
            continue
        pubs.append(Publication(title=title.strip(), authors="", venue="", year=None, url=href.strip()))
    return pubs


def deduplicate(publications: list[Publication]) -> list[Publication]:
    unique: list[Publication] = []
    seen: set[str] = set()
    for pub in publications:
        key = (pub.url or "").strip().lower() or (pub.title or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(pub)
    return unique


def sort_publications(publications: list[Publication]) -> list[Publication]:
    return sorted(
        publications,
        key=lambda p: (-(p.year or 0), p.title.casefold()),
    )


def fetch_json_for_query(query: str, limit: int = 100) -> list[Publication]:
    publications: list[Publication] = []
    start = 0
    while True:
        url = f"{BASE_URL}?format=json&limit={limit}&start={start}&text={quote(query)}"
        payload = fetch(url)
        page_items = parse_json(payload)
        if not page_items:
            # Stop if the endpoint did not return parseable JSON/records.
            break

        publications.extend(page_items)

        data = json.loads(payload)
        total = int(data.get("total") or 0) if isinstance(data, dict) else 0
        size = int(data.get("size") or len(page_items)) if isinstance(data, dict) else len(page_items)

        start += size
        if size == 0 or (total and start >= total):
            break
    return publications


def to_yaml(publications: list[Publication]) -> str:
    lines: list[str] = []
    for pub in publications:
        d = asdict(pub)
        lines.append('- title: "{}"'.format(d["title"].replace('"', '\\"')))
        lines.append('  authors: "{}"'.format(d["authors"].replace('"', '\\"')))
        lines.append('  venue: "{}"'.format(d["venue"].replace('"', '\\"')))
        lines.append(f"  year: {d['year'] if d['year'] is not None else 'null'}")
        lines.append('  url: "{}"'.format(d["url"].replace('"', '\\"')))
    return "\n".join(lines) + ("\n" if lines else "[]\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--identifier",
        action="append",
        dest="identifiers",
        help="Project/grant identifier or search term (can be provided multiple times)",
    )
    args = parser.parse_args()

    identifiers = args.identifiers or DEFAULT_IDENTIFIERS

    all_pubs: list[Publication] = []
    for identifier in identifiers:
        try:
            all_pubs.extend(fetch_json_for_query(identifier))
        except json.JSONDecodeError:
            # JSON endpoint failed for this query; fall back to html extraction for that query.
            html_url = f"{BASE_URL}?text={quote(identifier)}"
            all_pubs.extend(parse_html(fetch(html_url)))

    pubs = sort_publications(deduplicate(all_pubs))
    OUT_FILE.write_text(to_yaml(pubs), encoding="utf-8")
    print(f"Wrote {len(pubs)} publication(s) to {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
