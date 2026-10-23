# Anmay Defence: repo summary

## Company information (from the catalogues, scripts and old `index.html`)
- **Legal name:** Anmay Autonomous Systems Pvt. Ltd. **Brand:** Anmay Defence. **Origin:** an initiative of Robonut (product design, electronics, prototyping).
- **Taglines:** "Securing the skies. Defending the future." / "Engineering the Future of Autonomous Airspace Security" / "Detect. Track. Respond."
- **Business:** indigenous (Made in India), AI-powered counter-UAS (anti-drone) platforms. Core areas: counter-UAS, AI, embedded electronics, autonomous systems, computer vision, defence communications, electronic warfare integration.
- **Product: S.T.R.I.K.E.** (Smart Targeting, Reconnaissance and Intelligent Kill Engagement).
  - **Gen 1:** 1 kinetic layer, 700 m detection (10 ft+ drone), 360° rotation, 75° elevation, 5 independent trigger units, under 10 min deployment, 24 VDC, LoRa/WiFi/BLE, auto/manual.
  - **Gen 2:** adds a jamming layer (2 layers), day/night PTZ with 30× zoom, LiDAR, NVIDIA edge AI, 5 km fiber link, 2 km wireless video, 80° elevation.
  - **Gen 3:** research and development only (directed energy, swarm-defeat logic, autonomous networks).
  - **Mission packages:** RF Early Warning, Optical Fiber, Electronic Warfare, Solar Power, Multi-Weapon. Gen 2 also: Radar Surveillance, GPS Spoofing, EMP.
- **Threats named:** swarm attacks, low altitude, small radar cross-section, autonomous navigation, long range, electronic warfare.
- **Clients (your words):** private companies, Indian armed forces, other defence clients. No client names or logos exist in the repo.
- **Contact details:** none found in the repo.

## Repo structure (full trees: `TREE_OLD.txt`, `TREE_NEW.txt`; renames: `ASSET_MAP.md`)
| Path | What it is |
|---|---|
| `index.html` + 8 pages | The new website (home, product, about, technology, solutions, clients, deployments, faq, contact) |
| `css/site.css`, `js/site.js`, `js/hero.js` | Theme, shared behaviour, canvas radar hero |
| `tools/build_site.py` | Page text and templates. Edit, then run it |
| `tools/organize_assets.py` | Renames and moves media, writes the map and trees |
| `legacy/index-v1.html` | The original page, with the first CSS radar hero |
| `assets/web/` | Small web copies (11 files, about 3.5 MB) used by the site |
| `assets/images/`, `assets/videos/` | 134 images and 89 videos, grouped: branding, renders, field-trials, build-process, aerial-drone-shots, controller-and-software, ai-tracking-screens, automation-demos, strike-m, exhibition |
| `assets/docs/` | Two product catalogues (STRIKE, PRAHAR NETRA), video scripts, storyboard, edit-change list |
| `assets/models-3d/` | Two `.obj` designs. Names kept so the `.mtl` links still work |

## Things to know
- **README (special info):** the repo uses Git LFS. Run `git lfs install` then `git lfs pull`. Four videos are only pointer files without it. `.gitattributes` is updated by the organiser.
- `assets/index.html` was empty (0 bytes). It moved to `legacy/`.
- `objPart2.mlt` is probably a typo for `.mtl`. Not changed.
- Two copies of `Assmebly.jpg` (exploded assembly diagram) exist.
- Build-process and field-trial names describe the content family and date. They were checked on contact sheets, not frame by frame.

## Design source (video: daylightcomputer.com)
Cream `#F7F2EE`, sand `#E1D8D0`, ink `#1B1712`, night `#16160F`, orange `#FF9300`, ember `#C84602`, burnt `#8C3703`. Light tight sans (Inter Tight), 16 px page frame with 22 px rounded hero, floating pill menu, sand cards, scroll rails, dark-to-orange footer.

## Open questions
1. PRAHAR NETRA catalogue looks like the same product family under another name. Left off the public site until you confirm.
2. Prices and lead times were left out on purpose (the storyboard says keep them out of public material).
3. AI-generated renders were not used as product photos.
4. The About timeline comes from file dates. Please check it.
5. Add real email and phone in `tools/build_site.py`.
