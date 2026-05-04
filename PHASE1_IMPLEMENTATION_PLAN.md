# Phase 1 Website Implementation Plan

Goal: build a fast, credible first-version research website for `ShoRoy.github.io` with minimal user intervention.

## Route

- Use Quarto as a low-maintenance static-site generator for GitHub Pages.
- Keep the site physics-first and SciML-enabled, adapted from the master CV rather than copied verbatim.
- Reuse the current assets: headshot for the home page, simulation GIF for the featured technical visual and project pages.
- Build only complete pages: Home, Projects, Research, Publications, CV, Contact.
- Defer custom domain, blog/notes, analytics, and deep visual polish to a later phase.

## Phase A

- Use the existing `website` conda environment.
- Prefer `pip` for dependency installation where available.
- Install or verify Quarto tooling.
- Create a clean site folder structure under `website/`.
- Move images into `assets/` for stable paths.

## Phase B Preview

- Add Quarto config, navigation, theme, metadata, and CSS.
- Create first-pass content pages from the master CV.
- Add GitHub Pages deployment workflow.
- Render locally and fix broken links or asset paths.

## Guardrails

- Do not fabricate links, metrics, repositories, datasets, or deployment claims.
- Keep HEDS and SCIMITAR3D attribution scoped to verified CV language.
- Tie HPC scale to the physical resolution and validation it enabled.
- Avoid generic AI branding; present ML as part of the computational-physics pipeline.