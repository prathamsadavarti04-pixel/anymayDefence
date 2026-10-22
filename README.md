# Anmay Defence — website and media repository

This repository contains the Anmay Defence public-facing static website, product and engineering references, media assets, and a ten-part design-inspiration screen recording.

## Important: Git LFS

The inspiration recordings and selected original media are stored with Git LFS. Install and enable LFS before cloning or checking out large media:

```sh
git lfs install
git clone --branch feat/anmay-defence-multipage-site https://github.com/prathamsadavarti04-pixel/anymayDefence.git
cd anymayDefence
git lfs pull
```

The ten inspiration clips remain in `inspiration_video/` in their original serial order. They have intentionally not been renamed, so the reference sequence stays intact.

## Website routes

The site is framework-free and has no build step. It can be served by any static web host (including GitHub Pages):

- `/` — Home and animated radar/tracking hero
- `/products/` — STRIKE Gen 1 / Gen 2, STRIKE M and PRAHAR NETRA
- `/about/` — About Anmay Defence
- `/technology/` — High-level system workflow
- `/solutions/` — Solution areas
- `/clients/` — Audience and sectors
- `/projects/` — Representative deployment patterns
- `/faq/` — Frequently asked questions
- `/contact/` — Local-only briefing draft builder

Shared presentation and behavior live in `site.css`, `site-effects.css` and `site.js`. The route folders each contain an `index.html` shell.

## Documentation

- `ASSET_MAP.md` maps each original asset image/video path to its new descriptive path.
- `OLD_REPO_TREE.md` records the repository tree before the cleanup.
- `NEW_REPO_TREE.md` records the tree after the cleanup and website build.
- `REPO_SUMMARY.md` documents the discovered source files and the company/product information that can currently be supported.

## Content and deployment notes

Numeric product-performance values, named customer references, direct contact details and legal registered-entity information were not present in the readable source webpage. The website avoids inventing them. The contact page creates a briefing draft only in the user's browser; connect an approved secure submission endpoint before using the site for online lead capture. Review the product catalogues, storyboard and source video recordings locally before publishing any more detailed specifications or named case studies.
