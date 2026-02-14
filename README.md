# VIGILIA website

Professional GitHub Pages website for the ERC Advanced Grant **VIGILIA**.

## Local development

This site uses **Jekyll** (GitHub Pages compatible).

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://127.0.0.1:4000>.

## Content management

- Homepage content: `index.md`
- Team members: `_data/people.yml`
- Team photos: `assets/img/`
- Timeline: `timeline.md`
- Blog list page: `blog.md`
- Blog posts: `_posts/YYYY-MM-DD-title.md`
- Publications page: `publications.md`
- Publications data: `_data/publications.yml`

## Updating profile photos

1. Export/download official profile images from the AIDA website.
2. Save them with the same filenames as referenced in `_data/people.yml`.
3. Commit and push.

## Publication sync from UGent biblio

Use the helper script:

```bash
python scripts/fetch_biblio_publications.py
```

Optional custom source URL:

```bash
python scripts/fetch_biblio_publications.py "https://biblio.ugent.be/publication?f[funding_info][0]=101142229&format=json"
```

A GitHub Actions workflow (`.github/workflows/update-publications.yml`) runs weekly and updates `_data/publications.yml` automatically when changes are detected.
