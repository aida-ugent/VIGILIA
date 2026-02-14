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

---

## If your Pages URL shows 404

Use this quick checklist in GitHub:

1. **Settings → Pages**
   - Source must be **GitHub Actions**.
2. **Actions tab**
   - Confirm workflow **Deploy Jekyll site to GitHub Pages** ran successfully on your active branch.
3. **Repository branch**
   - This repo currently deploys on pushes to `main`, `master`, or `work`.
4. **Project site path**
   - Open: `https://aida-ugent.github.io/VIGILIA/` (with trailing slash).
5. **Wait 2–5 minutes** after first successful deploy.

For project pages (`aida-ugent.github.io/VIGILIA`), `_config.yml` must keep:
- `url: "https://aida-ugent.github.io"`
- `baseurl: "/VIGILIA"`

