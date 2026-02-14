# VIGILIA website

Professional GitHub Pages website for the ERC Advanced Grant **VIGILIA**.

## Use GitHub Pages only (no local setup needed)

You do **not** need to install Ruby, Jekyll, or run anything on your own computer.

### One-time setup

1. Push this repository to GitHub.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.

### Publish updates

1. Edit files directly on GitHub (or via commits pushed to the default branch).
2. Commit/push your changes.
3. GitHub automatically runs **Deploy Jekyll site to GitHub Pages**.
4. After it finishes, your site is live at the Pages URL shown in **Settings → Pages**.

---

## If GitHub says there are merge conflicts

If a pull request shows conflicts, use GitHub’s web flow:

1. Open the PR.
2. Click **Resolve conflicts**.
3. Keep the newer versions of these files when in doubt:
   - `.github/workflows/deploy-pages.yml`
   - `README.md`
   - `_config.yml`
4. Mark as resolved and commit.
5. Re-run/complete the merge.

If conflicts are complex, create a fresh branch from the latest default branch, copy over the wanted files, and open a new PR.

---

## Content files you will edit most

- Homepage: `index.md`
- People data: `_data/people.yml`
- Team photos: `assets/img/`
- Timeline: `timeline.md`
- Blog index: `blog.md`
- Blog posts: `_posts/YYYY-MM-DD-title.md`
- Publications page: `publications.md`
- Publication data cache: `_data/publications.yml`

## Automatic publication updates

A GitHub Actions workflow (`.github/workflows/update-publications.yml`) runs weekly to refresh publications from UGent biblio and commits updates automatically when data changes.

---


## If GitHub says "There isn't anything to compare"

This simply means your feature branch and `main` currently contain the same commits.

To create a new PR:
1. Make a small new commit on your branch (even docs-only is fine).
2. Push the branch again.
3. Re-open the compare URL.

