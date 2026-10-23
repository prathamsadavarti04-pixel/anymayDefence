# Anmay Defence — product-led static website

This is a framework-free, multi-route website for **Anmay Defence**, identified in the supplied catalogues as a brand of **Anmay Autonomous Systems Pvt. Ltd.** The visual direction follows the supplied inspiration clips: warm ivory/pale-blush surfaces, charcoal/black cinematic chapters, amber/orange calls to action, generous whitespace, product imagery, compact metadata and long-form scroll transitions. The original radar/tracking identity remains in the hero, paired with product trial footage.

## Routes

- `/` — Home, radar/tracking hero, sticky four-stage story, generation cards, mission-package interaction and separately marked roadmap.
- `/products/` — Interactive STRIKE Gen 1 / Gen 2 selector, specification grid, side-by-side comparison, mission packages, STRIKE M and PRAHAR NETRA.
- `/technology/` — Sensing, tracking, edge processing, operator workflow and configured response architecture.
- `/solutions/` — Site, platform, infrastructure and evaluation contexts.
- `/about/` — Company and engineering story.
- `/clients/` — Intended sectors and partner workflow.
- `/projects/` — Engineering/evaluation context without unapproved customer deployment claims.
- `/faq/` — Source-based product and deployment questions.
- `/contact/` — Briefing-request draft builder; copy, download or open a prefilled email draft.

No build step is required. Shared presentation and interactions are in `site.css`, `site-effects.css` and `site.js`. The hero uses a Canvas radar simulation and source trial-footage window; reduced-motion preferences are respected and the video pauses when out of view.

## Source files and inspiration-video audit

The `inspiration_video/` folder holds the ten original MOV clips in their supplied serial order. Source Office documents include:
- `ANMAY_Drone_Defence_Video_Script.docx`
- `STRIKE_Video_Creation_Storyboard_Anmay_Defence.docx`
- `New Video Script.docx`
- `STRIKE Product Catalogue Gen1 and 2.pptx`
- `PRAHAR NETRA Product Catalogue.pptx`
- `Changes .pptx` in the shortlisted-media folder

The workflow **Audit source documents and inspiration videos** uses sparse checkout to fetch those files, extracts DOCX paragraphs/tables and PPTX slide text/tables/notes, samples clips at 2 frames per second with FFmpeg, creates timestamp-labelled contact sheets and estimates an approximate sampled palette. It uploads an audit artifact and commits the generated files under `source-review/`.

Run it from **GitHub → Actions → Audit source documents and inspiration videos → Run workflow**. The workflow is an analysis aid; contact sheets are not production artwork.

## Asset cleanup and structure

- `ASSET_MAP.md` contains all 223 old-to-new media path mappings.
- `OLD_REPO_TREE.md` captures the source tree before cleanup.
- `NEW_REPO_TREE.md` captures the implementation tree.
- `REPO_SUMMARY.md` records company/product facts and source-based publication caveats.

Non-media Office documents and OBJ/MTL model files remain at their source paths. Inspiration clips keep their original filenames and order. Four video paths originally used Git LFS; their patterns are updated in `.gitattributes`.

```sh
git lfs install
git clone --branch feat/anmay-defence-multipage-site https://github.com/prathamsadavarti04-pixel/anymayDefence.git
cd anymayDefence
git lfs pull
```

## Publication guardrails

Numeric figures on the product page are reference values transcribed from the supplied catalogues/storyboards—not independent test results. Confirm exact product revision, conditions and compatible modules against the current approved specification before procurement or acceptance decisions. Future swarm/network/EMP/directed-energy concepts are separated from current capabilities. Public pricing is intentionally omitted until approved by a commercial owner.

The product catalogue lists `ANMAYDEFENCE@GMAIL.COM`, `+91 8828959943` and Mumbai, India. Confirm these are current before use. The Contact form only prepares a local draft; the email action opens the user's mail client and does not transmit form data to a website server.
