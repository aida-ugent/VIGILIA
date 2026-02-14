#!/usr/bin/env python3
"""Fetch VIGILIA publications from UGent biblio API into _data/publications.yml."""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_FILE = REPO_ROOT / "_data" / "publications.yml"
BASE_URL = "https://biblio.ugent.be/publication"
DEFAULT_Q = "project = vigilia"
DEFAULT_SORT = ["year.desc", "relevance.desc"]


@dataclass
class Publication:
    title: str
    authors: str
    venue: str
    year: int | None
    url: str


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": "VIGILIA-site-bot/1.2"})
    with urlopen(req, timeout=30) as resp:  # nosec B310
        return resp.read().decode("utf-8", errors="replace")


def stringify_authors(value: object) -> str:
    if isinstance(value, list):
        names: list[str] = []
        for a in value:
            if isinstance(a, dict):
                names.append(str(a.get("full_name") or a.get("name") or a.get("name_last_first") or "").strip())
            else:
                names.append(str(a).strip())
        return ", ".join(n for n in names if n)
    return str(value or "").strip()


def extract_year(item: dict) -> int | None:
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


def extract_venue(item: dict) -> str:
    for key in ("journal_title", "journal", "book_title", "booktitle", "event_title", "publisher", "type"):
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def canonical_url(item: dict) -> str:
    for key in ("url", "handle", "permalink"):
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    bid = item.get("biblio_id") or item.get("id")
    return f"https://biblio.ugent.be/publication/{bid}" if bid else ""


def parse_json(payload: str) -> tuple[list[Publication], int, int]:
    data = json.loads(payload)
    records = []
    total = 0
    size = 0
    if isinstance(data, dict):
        records = data.get("results") or data.get("hits") or data.get("items") or []
        total = int(data.get("total") or 0)
        size = int(data.get("size") or len(records))
    elif isinstance(data, list):
        records = data
        size = len(records)

    pubs: list[Publication] = []
    for item in records:
        if not isinstance(item, dict):
            continue
        pubs.append(
            Publication(
                title=str(item.get("title") or item.get("name") or "Untitled").strip(),
                authors=stringify_authors(item.get("authors") or item.get("author") or ""),
                venue=extract_venue(item),
                year=extract_year(item),
                url=canonical_url(item),
            )
        )
    return pubs, total, size


def fetch_all() -> list[Publication]:
    publications: list[Publication] = []
    start = 0
    limit = 100
    sort_params = "".join(f"&sort={quote(sort)}" for sort in DEFAULT_SORT)

    while True:
        url = f"{BASE_URL}?format=json&q={quote(DEFAULT_Q)}{sort_params}&limit={limit}&start={start}"
        page, total, size = parse_json(fetch(url))
        if not page:
            break
        publications.extend(page)
        start += size or len(page)
        if (total and start >= total) or (size == 0):
            break
    return publications


def deduplicate(publications: list[Publication]) -> list[Publication]:
    seen: set[str] = set()
    unique: list[Publication] = []
    for pub in publications:
        key = (pub.url or pub.title).strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(pub)
    return unique


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
    pubs = deduplicate(fetch_all())
    OUT_FILE.write_text(to_yaml(pubs), encoding="utf-8")
    print(f"Wrote {len(pubs)} publication(s) to {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
