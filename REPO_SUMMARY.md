# REPO_SUMMARY — Anmay Defence

## Source coverage and confidence

This summary uses the original root page and README, repository paths, all three readable DOCX scripts/storyboards, representative product and assembly imagery, .gitattributes, and the original media inventory. The large Gen 1/Gen 2 and PRAHAR NETRA PPTX catalogues still need a full slide-text and specification review. A source-audit workflow is included to extract slide text and notes and create timestamped FFmpeg contact sheets for all ten inspiration clips.

## Company profile

| Field | Source-backed information |
|---|---|
| Public brand | **Anmay Defence** |
| Registered legal name | Not established in the text extracted so far; confirm before legal publication. |
| Relationship | Existing page footer says “An initiative by Robonut”; one video script refers to “Robonut Project.” Confirm the exact legal/brand relationship. |
| Positioning line | “Engineering the Future of Autonomous Airspace Security.” The legacy footer also uses “Securing the skies. Defending the future.” |
| Main product story | Indigenous Counter-UAS platform family, described as modular and designed to evolve with the threat. |
| Workflow | Detect, identify, track, assess and support the configured response workflow. |
| Intended audiences in the product story | Defence organisations, technology partners, system integrators, R&D partners, procurement/evaluation teams and private-sector operators. These are audience categories, not proof of specific customer deployments. |
| Public contact endpoint | No verified public email, phone or online enquiry endpoint is established. The Contact route currently creates a local text draft only. |

## Product information extracted from DOCX sources

### STRIKE platform family

The STRIKE storyboard expands S.T.R.I.K.E. as **Smart Targeting, Reconnaissance, Intelligent Kill Engagement**. It positions STRIKE as a modular Counter-UAS platform family with generational evolution and mission-specific configurations.

The supplied storyboard includes editorial guardrails:
- Do not claim existing defence systems cannot stop swarms or that every drone cannot be jammed/spoofed.
- Do not present future swarm-defeat, autonomous-network or directed-energy ideas as current Gen 1 / Gen 2 features.
- Do not present shipboard deployment as already qualified; say “designed for adaptation” only if approved.
- Keep pricing and lead time out of the core product narrative.
- Tie numeric performance claims to the latest product catalogue and approved test conditions.

### STRIKE Gen 1 — foundation platform

The material describes a foundation platform story built around electro-optical / computer-vision tracking, auto/manual operating concepts and modular mission packages.

| Attribute | Value stated in the supplied narrative | Release note |
|---|---|---|
| Detection range | 700 m | Confirm product revision, test conditions and approved catalogue. |
| Horizontal movement | 360° continuous azimuth | Confirm the delivered movement envelope. |
| Vertical elevation | Up to 75° in the first script | Confirm the final hardware and movement envelope. |
| Operating concept | Auto / manual | Confirm current modes and operational constraints. |
| Deployment target | Under 10 minutes | Treat as a narrative target until the procedure is approved. |
| Architecture | One-layer defence | Use the approved definition. |
| Mission packages | STRIKE RF, STRIKE OF, STRIKE EW, STRIKE SP and STRIKE M | Generation compatibility and availability depend on configuration. |

Package terms in the material: **RF** — RF early warning; **OF** — optical fibre; **EW** — electronic warfare; **SP** — solar power; **M** — mounted / multi-payload variant. Confirm exact scope against approved product documents.

The first video script also describes computer-vision tracking, day/night-ready architecture and manual/automatic operating concepts. These are narrative statements and require current hardware/configuration confirmation before numeric claims are published. Website copy avoids describing weapon-operating procedures.

### STRIKE Gen 2 — expanded sensing and layered architecture

The supplied STRIKE storyboard positions Gen 2 as an expanded sensing / processing stack and a two-layer system concept. The values and modules below require catalogue-level confirmation.

| Attribute | Value/item stated | Release note |
|---|---|---|
| Optical system | Day/night PTZ, 30× optical zoom | Confirm camera model and environmental rating. |
| Sensor integration | LiDAR | Confirm delivered configuration. |
| Edge processing | NVIDIA Edge AI | Confirm compute module and software revision. |
| Movement envelope | 360° azimuth / 80° elevation | Confirm movement and installation limits. |
| Video / communication | 2 km wireless video / 5 km fibre | Confirm test conditions, link performance and system version. |
| Power | 24 VDC | Confirm power-input requirements. |
| Deployment target | Under 10 minutes | Confirm deployment procedure. |
| Layered defence | Kinetic and electronic-warfare layers described | Clarify actual implementation and authorised use. |
| Mission ecosystem | Radar, GNSS countermeasure, solar, multi-weapon | Confirm compatibility and availability. |

### Roadmap / future concepts

The materials mention future night/thermal sensing, expanded training data, mechanical protection, additional payload concepts, longer communication links and soft-kill/jamming. The storyboard expressly asks that swarm-defeat, autonomous-network and directed-energy concepts be labelled **FUTURE / R&D**, not presented as current Gen 1 / Gen 2 capabilities. The website keeps them separate.

### Other families

- **STRIKE M:** represented in product imagery and a separate testing-footage collection. Integration and configuration require confirmation.
- **PRAHAR NETRA:** a separate catalogue is present; detailed public capabilities need review against that current catalogue.

## Original source-file inventory

| Original path | Purpose |
|---|---|
| README.md | Git LFS instructions and repository notes. |
| .gitattributes | LFS patterns; updated for the four renamed paths that originally used LFS. |
| index.html | Previous one-page site; source of the radar identity, palette and typography direction. |
| assets/Drone detection Videos and Photos/ANMAY_Drone_Defence_Video_Script.docx | Emerging-threat story, company intro, current-system concept and future roadmap. |
| assets/Drone detection Videos and Photos/Shortlisted Photo Video/Changes .pptx | Shortlisted-media/change deck; detailed slide extraction to review from generated source text. |
| assets/StrikeGenOne_videos/STRIKE GEN 1 shots/STRIKE_Video_Creation_Storyboard_Anmay_Defence.docx | Gen 1/Gen 2 product narrative, reference values, mission options and public-claim guardrails. |
| assets/StrikeGenOne_videos/StrikeGenVideos/New Video Script.docx | Launch-film story and generational evolution. |
| assets/StrikeGenOne_videos/STRIKE GEN 1 shots/STRIKE Product Catalogue Gen1 and 2.pptx | Primary Gen 1 / Gen 2 catalogue; source-audit output should be reviewed to validate current specifications. |
| assets/StrikeGenOne_videos/StrikeGenVideos/PRAHAR NETRA Product Catalogue.pptx | Separate catalogue; review its extraction before writing detailed capability claims. |
| assets/**/img/, assets/**/Photos/, assets/**/Drone Shot/ | Product photos, models, drone/platform footage, operator UI and engineering/installation references; renamed and mapped in ASSET_MAP.md. |
| inspiration_video/ | Ten serial MOV segments of the owner-provided reference site, retained unchanged. |

## Website architecture and motion

- Static routes: Home, Products, About, Technology, Solutions, Clients, Projects, FAQ and Contact.
- Shared runtime: site.js; global styling and animation: site.css; supporting effects: site-effects.css.
- Home: Canvas radar sweep, real product trial-footage slot, sticky scroll-step visual, Gen 1/Gen 2 cards, mission-package interaction and separate roadmap.
- Product route: Gen 1 / Gen 2 selectors, reference-spec block, side-by-side / single-generation comparison, mission packages, STRIKE M and PRAHAR NETRA.
- Media cleanup: 223 images/videos moved to descriptive camelCase paths; ASSET_MAP.md maps every old media path. The ten inspiration clips retain their original filenames and order.
- Source-audit workflow: sparse-checkout Office files and reference videos, extract slide text, sample video frames with FFmpeg and create timestamped contact sheets.

## Visual direction from existing materials

- Graphite / near-black for the hero and system visuals; white and pale-neutral content surfaces.
- Electric-blue tracking accent (#1e5af9) and restrained scan-line / glow effects.
- Inter Tight headings, Inter body, JetBrains Mono technical labels.
- Long-form editorial scroll: chapter labels, visual handoffs, sticky explanatory panel, progressive reveals and interactive generation comparison.
- Actual product and assembly photographs instead of generic stock imagery; future roadmap concepts remain clearly separated from current product descriptions.

## Release gates

1. Review extracted PPTX text against the current approved catalogue and product revision; resolve every public numeric claim.
2. Inspect FFmpeg contact sheets for the reference palette, typography, section timing and scroll-animation progression; tune CSS to match actual observations.
3. Confirm registered legal name, the Robonut relationship, approved customer references, contact details and publication restrictions.
4. Connect an approved secure submission endpoint only if live lead capture is wanted. The contact draft helper currently transmits nothing.
