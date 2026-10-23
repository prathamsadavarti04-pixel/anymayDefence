# REPO_SUMMARY — Anmay Defence

## Company (extracted from docx/pptx in assets, Step 3)
- **Legal name:** Anmay Autonomous Systems Pvt. Ltd. — brand name **Anmay Defence** (source: PRAHAR NETRA catalogue, slide 2). Initiative by **Robonut Project**.
- **Taglines:** "Engineering the Future of Autonomous Airspace Security" · "Securing the skies. Defending the future." · "Detect. Track. Respond."
- **Contact (from catalogues):** +91 8828959943 · ANMAYDEFENCE@GMAIL.COM · Mumbai, India
- **Products:** STRIKE (S.T.R.I.K.E. = Smart Targeting, Reconnaissance, Intelligent Kill Engagement), formerly catalogued as **PRAHAR NETRA**. Gen1: 700 m detection, 360°/75°, 5 independent trigger units, <10 min deployment, Auto/Manual, 1-layer kinetic. Gen2: Day/Night PTZ 30×, LiDAR, NVIDIA Edge AI, 360°/80°, 2 km wireless / 5 km fiber, 24 VDC, 2-layer (kinetic + EW).
- **Mission packages:** RF (2 km+ early warning), OF (5 km+ fiber), EW (jamming), SP (solar 24×7), M (multi-weapon: INSAS/AK-203/LMG/MMG), Radar, GPS/GNSS spoofing, EMP (future).
- **Future/R&D (not current claims):** swarm defence, autonomous networks, directed energy, thermal 1 km, comms 2 km.
- **Clients/use-cases:** Indian Military/defence installations, borders, airports, critical infrastructure, industrial sites, public events, vehicle/maritime-adapted. No client logos were in the repo; no endorsement is fabricated on the site.
- **Core tech:** Counter-UAS, AI/computer vision, embedded electronics, autonomous systems, defence comms, EW integration.

## Repo structure (see OLD_TREE.txt / NEW_TREE.txt)
- Before: `index.html` (single-page, radar hero), `README.md` (⚠️ SPECIAL: repo uses Git LFS for large videos — clone, don't ZIP; `git lfs install && git lfs pull`), `.gitattributes` (4 LFS videos), `assets/index.html` (0-byte, removed), `assets/` 234 files / 1.6 GB in 2 confusing trees.
- After: same root + 9 pages, `assets/images|videos|documents|models/` semantic folders, `assets/site/` (web CSS/JS + optimised images), `ASSET_MAP.md`, `OLD_TREE.txt`, `NEW_TREE.txt`, this file, `INSPIRATION_VIDEO_ANALYSIS.md`.

## Inspiration video — honest status
Drive file found: `Screen Recording 2026-10-22 at 8.08.04 PM.mov` (355,308,041 bytes) in Drive folder `anmayDefense` (id `1a6-7vx8DTb03bao4zLf9LyPh55vHMK96`), link https://drive.google.com/file/d/1-iLqzEz8REF7LgNcW_NswbIFvc5vrqqx/view — **Arena download limit is 100 MB, so the video could not be downloaded/frame-analysed in this sandbox.** Analysis in INSPIRATION_VIDEO_ANALYSIS.md is therefore derived from the existing index.html, which already embodies that design language (author to confirm). Please upload a compressed <100 MB export to enable true frame-by-frame analysis.

## Media corrections (2026-10-22, frame-verified)
- Catalogue PPTX images are mostly icons/stock (radar trucks, missile launches) — NOT used as Anmay product photos.
- Gen1 = real silver pan-tilt + multi-rifle system (truck/static/jeep, 2025-26 trial photos & videos in assets/site/gen1-* + site/video/strike-* compressed from real archive clips: STRIKE-M trial edit, live firing, truck automation, operator console).
- Gen2 = AI concept renders only (assets/site/gen2-*-render.jpg), always captioned as renders.
- 4 files remain Git-LFS pointers in this sandbox (git-lfs binary could not be installed — outbound hosts restricted): anmay-strike-trial-footages-compilation.mp4, strike-gen1-video-…103217 / …104336 / …104526. They are NOT embedded. Run `git lfs install && git lfs pull` locally to fetch them; all other 80+ videos are real files and were used.
- Hero radar restored to original faef79b CSS radar (conic sweep + 3 white blips, no drone dots/canvas), enlarged to 96rem so the sweep reaches across the headline; centre position formula preserved (right offset compensated by half the size increase).
