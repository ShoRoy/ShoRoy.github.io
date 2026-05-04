# Shobhan Roy — personal website

Source for [shoroy.github.io](https://shoroy.github.io). Built with [Quarto](https://quarto.org) and deployed via GitHub Actions to GitHub Pages.

## Local development

Requires Quarto (>=1.4) on `PATH`. The project was built using a conda env named `website`:

```bash
conda activate website
pip install quarto-cli   # if not already installed

# render once
quarto render

# live preview with hot reload
quarto preview
```

Output lives in `_site/` and is git-ignored.

## Project layout

```
_quarto.yml             # site config, navbar, theme, metadata
styles.css              # typography, hero, focus-strip, cards
index.qmd               # home (hero, feature, featured projects, selected pubs)
research.qmd            # research-area narrative
publications.qmd        # full publication list with profile strip
cv.qmd                  # resume summary + PDF download link
contact.qmd             # email + profiles
projects/
  index.qmd             # projects landing grid
  scimitar3d.qmd        # solver case study
  hpc-dns-campaigns.qmd # production HPC case study
  heds.qmd              # HEDS framework case study
  physics-aware-ml.qmd  # PARC / D-PARC benchmarks case study
assets/
  headshot.jpg
  shock-pore-collapse.gif
  Shobhan_Roy_Industry_Resume.pdf  # downloadable resume (replace as needed)
.github/workflows/
  publish.yml           # Quarto render -> GitHub Pages deploy
```

## Adding a new project

1. Copy any file in `projects/` (e.g. `scimitar3d.qmd`) to a new `projects/<slug>.qmd`.
2. Keep the Problem / Technical Approach / Scale / Validation / Outcome / Links template.
3. Add a card block in `projects/index.qmd` and (optionally) in the home page Featured Projects grid in `index.qmd`.
4. Re-render and commit.

## Updating the resume download

Replace `assets/Shobhan_Roy_Industry_Resume.pdf` with the latest export. Filename is referenced from `index.qmd`, `cv.qmd`, `publications.qmd`, and the navbar in `_quarto.yml` — keep the filename stable, or update those four references.

## Deployment

A push to `main` triggers `.github/workflows/publish.yml`, which:

1. Checks out the repo on an Ubuntu runner.
2. Installs Quarto.
3. Runs `quarto render` to produce `_site/`.
4. Uploads `_site/` as a Pages artifact.
5. Deploys via `actions/deploy-pages`.

### One-time GitHub setup

After pushing to `ShoRoy/ShoRoy.github.io`:

1. Repo **Settings → Pages → Build and deployment**: set **Source** to **GitHub Actions** (not "Deploy from branch").
2. Repo **Settings → Actions → General → Workflow permissions**: confirm **Read and write permissions** (the workflow already declares the minimum scopes it needs).
3. Push to `main`. The first run takes ~2 minutes; the deployment URL appears on the workflow summary.

The site will be served from `https://shoroy.github.io/`.

## Roadmap (post phase 1)

- PDF CV export (requires LaTeX or a separate render pipeline).
- Notes / blog section once there is content to populate it.
- Custom domain (configure `CNAME` and DNS, then update `site-url` in `_quarto.yml`).
- Pinned GitHub repos + restored GitHub link in `contact.qmd` once one or two showcase repos exist.
