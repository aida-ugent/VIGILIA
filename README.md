# VIGILIA website

Jekyll website for the ERC Advanced Grant **VIGILIA**.

## Keep the site up to date

1. Edit content files:
   - Home: `index.md`
   - People: `_data/people.yml`
   - Publications cache: `_data/publications.yml`
   - News: `_posts/`
2. Refresh publications from UGent biblio:
   - `python3 scripts/fetch_biblio_publications.py`
3. Commit and push to GitHub.
4. GitHub Pages deploys automatically via Actions.

## GitHub Pages settings

- `url: "https://aida-ugent.github.io"`
- `baseurl: "/VIGILIA"`
