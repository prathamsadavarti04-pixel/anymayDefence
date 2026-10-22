# REPO_SUMMARY — Anmay Defence

## Scope and source confidence

This summary is grounded in the repository branch `moved_everything_assetsINTO_assetsFolder` at the start of this change. The readable source page was `index.html`; repository metadata and `.gitattributes` were also inspected. Media files were inventoried, and representative smaller images were viewed. Large binary Office documents and the ten MOV inspiration clips were not accessible as decoded content through the available GitHub text interface in this run. Treat this as a source-backed inventory, not a final technical or legal approval of all content.

## Company information

| Item | What the repository supports |
|---|---|
| Public brand | **Anmay Defence** |
| Legal registered name | **Not identified** in the readable source page or root README. Confirm with the company before legal / footer publication. |
| Relationship stated in current page | Existing footer says “An initiative by Robonut.” The role of Robonut and the precise legal entity should be confirmed. |
| Public tagline | Existing source footer: “Securing the skies. Defending the future.” |
| Main positioning | Existing title / meta description positions Anmay Defence around AI-powered counter-drone defence, real-time airspace awareness and rapid response. |
| Core workflow stated in current page | Detection, tracking, threat prioritisation and response support. |
| Use cases in existing page | Defence installations, airports, borders, critical infrastructure, industrial facilities and public events. These are presented as use-case categories, not proof that every deployment has occurred. |
| Customer / deployment references | The project brief supplied by the repository owner says the company has worked with private companies, Indian Military and other defence clients. No named customer organisations or approved logos were identified in the readable source file inventory. |
| Public contact details | No verified email address, phone number or enquiry endpoint was found in the readable source page. |

## Product and technology vocabulary found

- **STRIKE** — described by the current page as the flagship AI-powered counter-drone system.
- **STRIKE Gen 1 and Gen 2** — a product catalogue with both generations is present in the asset library.
- **STRIKE M** — separate imagery and a “testing trail” video collection indicate a related mounted platform/configuration.
- **PRAHAR NETRA** — a separate product catalogue is present.
- **Operator interface / RPI** — desktop screenshot, remote-control references and setup images are present.
- **Mechanical / product models** — a Tinkercad OBJ model and material files exist in the “Next_gen” folders.
- **System concepts found in the original page** — real-time awareness, tracking, threat prioritisation, modular deployment language and response support.

The numeric performance specifications, sensor-model list, effective range, accuracy, latency, endurance, and product configuration matrix were not present in the readable HTML. Do not infer these values from image/video filenames or renders.

## Initial repository file-by-file inventory

| Original path | Purpose / interpretation |
|---|---|
| `README.md` | Git LFS cloning and media checkout instructions. |
| `.gitattributes` | Git LFS filters for four specific media paths; updated in the cleanup to follow those tracked media after renaming. |
| `index.html` | Existing single-page marketing site; includes shared color/type tokens, responsive layout, the rotating radar sweep, track blips, interaction scripts, STRIKE messaging, use cases, and footer. |
| `assets/Drone detection Videos and Photos/ANMAY_Drone_Defence_Video_Script.docx` | Video script document; binary document content still needs a local review. |
| `assets/Drone detection Videos and Photos/Shortlisted Photo Video/Changes .pptx` | Shortlisted-media / change deck, per file name; binary deck content still needs a local review. |
| `assets/StrikeGenOne_videos/STRIKE GEN 1 shots/STRIKE Product Catalogue Gen1 and 2.pptx` | Product catalogue for STRIKE Gen 1 and Gen 2; detailed specifications should be extracted and verified from the local deck. |
| `assets/StrikeGenOne_videos/STRIKE GEN 1 shots/STRIKE_Video_Creation_Storyboard_Anmay_Defence.docx` | STRIKE video storyboard; local text review still required. |
| `assets/StrikeGenOne_videos/StrikeGenVideos/New Video Script.docx` | Additional video script; local text review still required. |
| `assets/StrikeGenOne_videos/StrikeGenVideos/PRAHAR NETRA Product Catalogue.pptx` | Separate PRAHAR NETRA catalogue; local review required before writing a detailed product page. |
| `assets/Drone detection Videos and Photos/Shortlisted Photo Video/Next_gen_design_1_zipfile/tinker.obj` | Large Tinkercad OBJ geometry file. |
| `assets/Drone detection Videos and Photos/Shortlisted Photo Video/Next_gen_design_1_zipfile/obj.mtl` | Tinkercad material definitions. |
| `assets/Drone detection Videos and Photos/Shortlisted Photo Video/Next_gen_part_two_zipfileExtration/tinkerPart2.obj` | Additional / second-part Tinkercad OBJ geometry. |
| `assets/Drone detection Videos and Photos/Shortlisted Photo Video/Next_gen_part_two_zipfileExtration/objPart2.mlt` | Additional material definitions; file extension is `.mlt` in the source. |
| `assets/**/img/`, `assets/**/Photos/`, `assets/**/Drone Shot/` | Photo references, drone/platform footage and operator-interface assets, renamed and mapped in `ASSET_MAP.md`. |
| `inspiration_video/` | Ten numbered MOV segments of the owner-provided design reference. Retained unchanged in original serial order. |

## Structure after implementation

- `site.js` renders the nine static routes and their accessible navigation / interactions.
- `site.css` contains the shared typography, palette, responsive layout and reveal styles.
- `site-effects.css` contains radar/product-placeholder presentation details.
- The home route includes a Canvas tracking simulation inspired by the existing blue sweep and track-blip identity.
- `products/`, `about/`, `technology/`, `solutions/`, `clients/`, `projects/`, `faq/` and `contact/` each contain `index.html`.
- Media has been consolidated into descriptive `assets/images/<category>/` and `assets/videos/<category>/` paths. Non-media source documents and OBJ/MTL models remain at their source paths to avoid breaking any model/material references or losing originals.

## Design tokens retained from the existing page

- Graphite: `#232121`
- Electric blue: `#1e5af9`
- Dark hero: `#101216`
- White / neutral greys for content surfaces and dividers
- Typography: Inter Tight display, Inter body, JetBrains Mono labels
- Motion signature: rotating blue radar sweep, target/blip markers, restrained reveal transitions and hover micro-interactions.

## Important review items before production

1. Review all three DOCX documents and both PPTX catalogues locally, then replace product-page qualification text with only approved data.
2. Reconfirm the reference site's exact colors, typography, spacing and scroll animation against the ten MOV clips. The current execution environment exposed their file inventory but not decodable clip bytes, so frame-by-frame inspection could not be completed.
3. Confirm registered legal name, Robonut relationship, public contact channels, approved client references and any export/security/publication restrictions.
4. Connect the contact draft helper to an approved secure form endpoint if online submissions are required. No user-entered contact information is transmitted by the current static demo.
