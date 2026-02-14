# VIGILIA website

Professional GitHub Pages website for the ERC Advanced Grant **VIGILIA**.

## Make the site live on GitHub Pages (beginner-friendly)

1. Push this repository to GitHub.
2. Open **Settings → Pages** in your repository.
3. Under **Build and deployment**, choose **Source: GitHub Actions**.
4. Push any commit to your default branch (`main`, `master`, or `work`).
5. Wait for the workflow **"Deploy Jekyll site to GitHub Pages"** to finish.
6. Open your live URL shown in:
   - **Settings → Pages**, or
   - the completed deploy workflow summary.

> First deployment can take a few minutes.

---

## Why preview may not work right now

The preview failed in the current environment because Ruby gems could not be downloaded from `rubygems.org` (network 403). So Jekyll could not be installed locally.

### Reliable preview options

- **Recommended:** use GitHub Actions deploy preview (the live Pages URL).
- **Local (when network works):**
  ```bash
  bundle install
  bundle exec jekyll serve
  ```
  Then open <http://127.0.0.1:4000>.

---

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
