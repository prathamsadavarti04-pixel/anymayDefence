#!/usr/bin/env python3
"""Builds the 9 pages of the Anmay Defence website. Edit the text below, then run:  python tools/build_site.py"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTACT = {"email": "", "phone": ""}   # add the real email and phone here, then run this script again
YEAR = 2026
SYM = re.search(r'<symbol id="lg".*?</symbol>', open(os.path.join(ROOT, "legacy/index-v1.html"), encoding="utf-8").read(), re.S).group(0)
NAV = [("Product", "product.html"), ("Technology", "technology.html"), ("Solutions", "solutions.html"),
       ("Deployments", "deployments.html"), ("About", "about.html"), ("FAQ", "faq.html")]
W = lambda f: "assets/web/" + f
ICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%2316160F'/%3E%3Cpath d='M7 25 16 7l9 18' fill='none' stroke='%23FF9300' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"


def shell(fn, title, desc, body, js=""):
    links = "".join('<a href="%s"%s>%s</a>' % (h, " aria-current=page" if h == fn else "", t) for t, h in NAV)
    home = ' aria-current=page' if fn == "index.html" else ""
    mail, tel = CONTACT["email"], CONTACT["phone"]
    contact = (f'<a href="mailto:{mail}">{mail}</a>' if mail else "") + (f'<a href="tel:{tel}">{tel}</a>' if tel else "")
    return f"""<!doctype html>
<html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | Anmay Defence</title><meta name="description" content="{desc}"><meta name="theme-color" content="#F7F2EE">
<link rel="icon" href="{ICON}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500&display=swap" rel="stylesheet"><link rel="stylesheet" href="css/site.css"></head>
<body><svg width="0" height="0" style="position:absolute" aria-hidden="true">{SYM}</svg><a class="skip" href="#main">Skip to content</a>
<header><a class="logo" href="index.html" aria-label="Anmay Defence, home"><svg viewBox="0 0 138.4 48" role="img" aria-label="Anmay Defence"><use href="#lg"/><circle class="lp" cx="24" cy="9" r="6.5"/></svg></a>
<button class="mbtn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main"><a href="index.html"{home}>Home</a>{links}<a class="btn" href="contact.html">Request a briefing</a></nav></header>
<main id="main">{body}</main>
<footer><h2>Ready to protect your airspace?</h2><a class="btn" href="contact.html">Request a briefing</a><div class="big" aria-hidden="true">anmay</div>
<div class="fcols"><div><b>Anmay Defence</b><p>Securing the skies. Defending the future.</p></div>
<div><h4>Product</h4><a href="product.html">STRIKE</a><a href="technology.html">Technology</a><a href="solutions.html">Solutions</a></div>
<div><h4>Company</h4><a href="about.html">About</a><a href="clients.html">Clients</a><a href="deployments.html">Deployments</a><a href="faq.html">FAQ</a></div>
<div><h4>Contact</h4><a href="contact.html">Request a briefing</a>{contact}</div></div>
<div class="fine"><span>Anmay Defence is a brand of Anmay Autonomous Systems Pvt. Ltd. An initiative by Robonut.</span><span>© {YEAR}</span></div></footer>
<script src="js/site.js" defer></script>{js}</body></html>"""


def hero(img, h, p): return f'<section class="hero page-hero"><img src="{W(img)}" alt="" fetchpriority="high"><div class="txt"><h1>{h}</h1><p>{p}</p></div></section>'
def head(h, p=""): return f'<div class="head"><h2>{h}</h2><p>{p}</p></div>'
def sec(body, cls="", style=""): return f'<section class="sec {cls}"{f" style={chr(34)}{style}{chr(34)}" if style else ""}><div class="wrap">{body}</div></section>'
def tiles(items): return '<div class="grid">' + "".join(f'<div class="tile"><h3>{a}</h3><p>{b}</p></div>' for a, b in items) + "</div>"
def specs(d): return '<div class="specs">' + "".join(f"<div><b>{k}</b><span>{v}</span></div>" for k, v in d.items()) + "</div>"
def card(i, t, c): return f'<figure class="card"><img src="{W(i)}" alt="{t}" loading="lazy"><figcaption><h3>{t}</h3><p>{c}</p></figcaption></figure>'
def faq(qs): return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qs) + "</div>"
def tabs(panes):
    b = "".join(f'<button role="tab" aria-selected="{str(i == 0).lower()}" aria-controls="p{i}">{l}</button>' for i, (l, _) in enumerate(panes))
    p = "".join(f'<div class="pane" id="p{i}" role="tabpanel"{"" if i == 0 else " hidden"}>{h}</div>' for i, (_, h) in enumerate(panes))
    return f'<div class="tabs" role="tablist">{b}</div>{p}'


G1 = {"Detection range": "700 m for a drone of 10 ft or more", "Drone types": "Quadcopter, VTOL, fixed wing", "Communication": "LoRa (+1 km), WiFi, BLE",
      "Power": "24 VDC", "Mounting": "Vehicle or static mount", "Rotation": "360°, continuous", "Elevation": "75°", "Trigger units": "5, independent",
      "Deployment time": "Under 10 minutes", "Operation": "Auto or manual", "Protection": "1 layer (kinetic)", "Origin": "Made in India"}
G2 = {"Cameras": "Day and night PTZ", "Optical zoom": "30×", "Detection range": "Extended (catalogue figure: +1.5 km)", "LiDAR": "Integrated",
      "AI computing": "NVIDIA edge", "Trigger units": "5, independent", "Rotation / elevation": "360° / 80°", "Control link": "LoRa 2 km, optical fiber 5 km",
      "Video link": "2 km wireless", "Power / deployment": "24 VDC / under 10 minutes", "Protection": "2 layers (kinetic + jamming)", "Origin": "Made in India"}
PKG = [("RF Early Warning", "Senses a drone’s radio link from over 2 km and wakes the AI tracker. Saves power."),
       ("Optical Fiber", "A secure link over 5 km or more with live HD video. It resists jamming."),
       ("Electronic Warfare", "Multi-band jamming on configurable frequencies. A second, non-kinetic layer."),
       ("Solar Power", "Solar charging and smart battery care for 24×7 work in remote areas."),
       ("Multi-Weapon", "A modular mount with independent trigger control, so you can match the mission."),
       ("Radar Surveillance (Gen 2)", "Long-range radar for early detection and automatic cueing of the cameras."),
       ("GPS Spoofing (Gen 2)", "Disrupts hostile drone navigation with controlled GNSS signal manipulation."),
       ("EMP (Gen 2)", "Electromagnetic payloads for advanced electronic threat neutralisation.")]
USES = [("Defence installations", "Perimeter airspace awareness and unauthorised drone detection."), ("Airports", "Airspace monitoring support around sensitive operational zones."),
        ("Borders", "Wide-area awareness for remote or difficult terrain."), ("Critical infrastructure", "Monitoring for power, ports, refineries and industrial assets."),
        ("Industrial facilities", "Site-level monitoring for unauthorised aerial activity."), ("Public events", "Temporary deployment for venue and crowd airspace awareness.")]
FAQ = {
 "product": ("Product", [
  ("What is STRIKE?", "STRIKE (Smart Targeting, Reconnaissance and Intelligent Kill Engagement) is a family of AI-powered counter-UAS platforms from Anmay Defence. It detects, tracks and responds to hostile drones."),
  ("What is the difference between Gen 1 and Gen 2?", "Gen 1 has one kinetic protection layer, AI vision, autonomous tracking and 360° coverage. Gen 2 adds a jamming layer, day and night optics, LiDAR-assisted identification and edge AI."),
  ("What are mission packages?", "Modules you add to a platform: RF early warning, optical fiber link, electronic warfare, solar power and multi-weapon mounting. Gen 2 also offers radar surveillance, GPS spoofing and EMP payloads."),
  ("Is Gen 3 available?", "No. Gen 3 is in research and development."),
  ("Is STRIKE made in India?", "Yes. It is developed in India, which supports supply-chain security.")]),
 "technology": ("Technology", [
  ("How far can STRIKE detect a drone?", "Gen 1 detects a drone of 10 ft or more at up to 700 m. The RF early warning package senses drone radio signals from over 2 km. Gen 2 extends the optical range."),
  ("Which drones can it track?", "Quadcopters, VTOL drones and fixed-wing drones."),
  ("Does it work at night?", "Gen 2 has day and night PTZ cameras with 30× optical zoom."),
  ("How does it communicate?", "Gen 1 uses LoRa (+1 km), WiFi and BLE. Gen 2 adds a 5 km optical fiber control link that resists jamming and a 2 km wireless video link."),
  ("Does an operator stay in control?", "Yes. STRIKE works in auto mode or manual mode."),
  ("What power does it need?", "24 VDC. The solar power package supports 24×7 operation in remote areas.")]),
 "deployment": ("Deployment", [
  ("How fast can it be deployed?", "In under 10 minutes."),
  ("Can it be mounted on a vehicle?", "Yes. STRIKE supports vehicle and static mounting. Our field trials used truck-mounted systems."),
  ("Can it work without grid power?", "Yes, with the solar power package.")]),
 "company": ("Company", [
  ("Who is Anmay Defence?", "Anmay Defence is a brand name of Anmay Autonomous Systems Pvt. Ltd. We develop indigenous AI-powered autonomous defence technology."),
  ("What is Robonut?", "Robonut is the engineering-led initiative behind our product design, electronics and prototyping work."),
  ("Who do you work with?", "The Indian armed forces, other defence organisations and private companies. Client names are not listed here."),
  ("How do I get pricing?", "Pricing and lead times are shared in a briefing. Use the contact page to ask for one.")])}
TOP = "padding-top:clamp(130px,15vw,210px)"
P = {}

P["index.html"] = ("Counter-drone defence", "Anmay Defence builds STRIKE, an AI-powered counter-drone platform that detects, tracks and responds to hostile drones.", f"""
<section class="hero" id="top"><img src="{W('hero-aerial-truck-mounted-strike-gen1.jpg')}" alt="" fetchpriority="high"><canvas id="radar" aria-hidden="true"></canvas>
<div class="txt"><h1>Detect. Track. Respond.</h1><p>STRIKE is an AI-powered counter-drone platform. It finds small drones, follows them in real time and helps operators respond fast.</p>
<div class="row"><a class="btn" href="contact.html">Request a briefing</a><a class="btn ghost" href="product.html">Explore STRIKE</a></div></div>
<span class="hint">Click the radar to launch a test drone</span>
<div class="hud" id="hud"><div><b id="h1">0</b>tracks</div><div><b id="h2">—</b>locked</div><div><b id="h3">—</b>range, m</div></div></section>"""
+ sec(head("Drones are small, fast and low. Defence has to keep up.", "Modern drones fly below many radars, move in groups and can navigate on their own. One sensor or one countermeasure may not be enough.")
      + tiles([("Swarm attacks", "Many drones at once, from more than one direction."), ("Low altitude", "Flying close to the ground, under normal coverage."),
               ("Small radar cross-section", "Small bodies that are hard for radar to see."), ("Autonomous navigation", "Flight that does not depend on a radio link."),
               ("Long range", "Threats that start far from the site they target."), ("Electronic warfare", "Contested signals, jamming and spoofing.")]))
+ f"""<section class="expand"><video src="{W('aerial-field-trial-loop.mp4')}" poster="{W('aerial-field-trial-loop-poster.jpg')}" autoplay muted loop playsinline preload="metadata" aria-label="Aerial view of a vehicle-mounted STRIKE system in a field trial"></video>
<div class="in"><h2>Built in India. Tested in the field.</h2><div class="stats"><div><b>360°</b>continuous rotation</div><div><b>&lt;10 min</b>to deploy</div><div><b>700 m</b>Gen 1 detection range</div></div></div></section>"""
+ sec(head("One platform. Three generations.", "STRIKE is a modular family. Start with Gen 1 and add what each mission needs.")
      + tiles([("STRIKE Gen 1", "One kinetic layer with AI vision, autonomous tracking and 360° coverage."),
               ("STRIKE Gen 2", "Two layers: kinetic and jamming. Day and night optics, LiDAR-assisted identification and edge AI."),
               ("Gen 3 (research)", "Directed energy, swarm-defeat logic and autonomous networks. In research and development.")])
      + '<p style="margin-top:32px"><a class="btn" href="product.html">See the specifications</a></p>', "sand")
+ sec(head("Mission packages", "Add only what the mission needs.") + '<div class="mq"><div>' + "".join(f"<span>{n}</span>" for n, _ in PKG * 2) + "</div></div>")
+ f"""<section class="sec sand"><div class="wrap">{head("From our field trials", "Photos from trials of vehicle-mounted and fixed-base systems.")}</div><div class="rail">"""
+ card("strike-gen1-truck-mounted-side.jpg", "Vehicle-mounted STRIKE Gen 1", "Side view of the system on a truck bed during a field trial.")
+ card("aerial-truck-field-trial-wide.jpg", "Aerial view", "A drone view of the vehicle-mounted system in the field.")
+ card("strike-gen1-turret-field-view.jpg", "Turret in the field", "The turret during a field trial.")
+ card("strike-gen1-fixed-base-installation.jpg", "Fixed-base installation", "STRIKE on a static base.")
+ card("truck-mounted-demo-with-team.jpg", "Demonstration with operators", "Operators with the vehicle-mounted system.")
+ card("remote-controller-closeup.jpg", "Remote controller", "The handheld remote controller.") + "</div></section>",
 '<script src="js/hero.js" defer></script>')

P["product.html"] = ("STRIKE product family", "STRIKE Gen 1, Gen 2 and mission packages: specifications of the AI-powered counter-UAS platform family from Anmay Defence.",
 hero("strike-gen1-truck-mounted-side.jpg", "STRIKE", "AI-powered counter-UAS platforms. Designed and built in India.")
 + sec(head("One platform that grows with the threat", "S.T.R.I.K.E. means Smart Targeting, Reconnaissance and Intelligent Kill Engagement. The design is open and upgradeable.")
       + tabs([("Gen 1", specs(G1)), ("Gen 2", specs(G2)),
               ("Gen 3", '<p style="max-width:40em;font-size:1.2rem">Gen 3 is in research and development. We are studying directed energy, swarm-defeat logic and fully autonomous networks. These are not features of Gen 1 or Gen 2.</p>')]))
 + sec(head("Mission packages", "Add modules to fit the mission. Pricing and lead times are shared in a briefing.") + tiles(PKG), "sand"))

P["about.html"] = ("About", "Anmay Defence is a brand of Anmay Autonomous Systems Pvt. Ltd. We build indigenous AI-powered counter-drone technology in India.",
 hero("truck-mounted-demo-with-team.jpg", "Engineering the future of autonomous airspace security", "Anmay Defence builds indigenous, AI-powered counter-drone technology in India.")
 + sec(head("Who we are", "Anmay Defence is a brand name of Anmay Autonomous Systems Pvt. Ltd. We develop indigenous AI-powered autonomous defence technology for airspace security: intelligent surveillance, autonomous tracking and modular counter-UAS platforms.")
       + tiles([("Counter-UAS systems", "Detect, track and respond to hostile drones."), ("Artificial intelligence", "Models that find and follow small aerial targets."),
                ("Embedded electronics", "Controllers, drivers and sensors built in-house."), ("Autonomous systems", "Platforms that work with or without constant input."),
                ("Computer vision", "Cameras and software that see and classify."), ("Defence communications", "LoRa, WiFi, BLE and optical fiber links."),
                ("Electronic warfare integration", "Jamming and signal control as a second layer.")]))
 + sec(head("Built on Robonut engineering", "STRIKE grew out of Robonut, an engineering-led defence initiative. Every system is designed, built and tested by our own team, from prototype to product.")
       + tiles([("Jul 2025", "First hardware builds: servo trigger units, motors and a Raspberry Pi controller."), ("Oct 2025", "Vehicle-mounted demonstrations with operators and laptop control."),
                ("Jun–Jul 2026", "STRIKE Gen 1 field trials, including a handheld remote controller."), ("Sep–Oct 2026", "Truck-mounted trials with aerial drone footage.")]), "sand"))

P["technology.html"] = ("Technology", "How STRIKE detects, tracks and responds: AI vision, edge computing, RF early warning, secure links and electronic warfare.",
 hero("aerial-truck-field-trial-angle.jpg", "Technology", "From the first sensor signal to the operator’s decision, in one connected system.")
 + sec(head("How STRIKE works", "Four steps run in one loop. STRIKE works in auto mode or manual mode.")
       + tiles([("1. Detect", "Identify aerial activity inside the protected airspace."), ("2. Track", "Keep live awareness of each object and its movement."),
                ("3. Prioritise", "Help operators tell routine activity from a real threat."), ("4. Respond", "Give alerts and insight for fast decisions, with kinetic and jamming layers.")]))
 + sec(head("The technology stack", "Sensing, AI, communications and response. Each part can be upgraded on its own.")
       + tiles([("AI vision and tracking", "Cameras and AI models find a drone, then keep it in view as it moves."), ("Edge AI computing", "Gen 2 runs its AI on an NVIDIA edge computer, close to the sensors."),
                ("Electro-optics and LiDAR", "Gen 2 adds day and night PTZ cameras, 30× zoom and LiDAR-assisted identification."), ("RF early warning", "Senses a drone’s radio link from over 2 km and wakes the AI tracker."),
                ("Secure communications", "LoRa, WiFi and BLE, plus a 5 km optical fiber link that resists jamming."), ("Electronic warfare", "Multi-band jamming on configurable frequencies, as a second, non-kinetic layer."),
                ("Servo-driven turret", "360° rotation, up to 80° elevation and five independent trigger units."), ("Power", "Runs on 24 VDC. A solar package gives 24×7 operation in remote areas.")]), "sand")
 + sec(head("Inside the system", "An exploded view of the Gen 1 assembly, and the handheld remote controller.")
       + f'<div class="duo"><figure><img src="{W("strike-gen1-exploded-assembly.jpg")}" alt="Exploded view of the STRIKE Gen 1 assembly" style="object-fit:contain" loading="lazy"><figcaption>STRIKE Gen 1 exploded assembly</figcaption></figure>'
         f'<figure><img src="{W("remote-controller-closeup.jpg")}" alt="Handheld remote controller" loading="lazy"><figcaption>Handheld remote controller</figcaption></figure></div>'))

P["solutions.html"] = ("Solutions", "Counter-drone detection, tracking and response for defence sites, borders, airports, infrastructure and events.",
 hero("aerial-truck-field-trial-wide.jpg", "Solutions", "Detection, tracking and response for places that cannot afford a gap in the sky.")
 + sec(head("Layered protection", "Each layer gives the operator more time and more choice.")
       + tiles([("Detect", "RF early warning senses a drone’s radio link from over 2 km. AI vision, and radar on Gen 2, confirm what is out there."),
                ("Track", "The turret follows the drone through 360° while the AI keeps the target locked."),
                ("Respond", "A kinetic layer on Gen 1. A second, jamming layer on Gen 2. Auto or manual operation.")]))
 + sec(head("Ways to deploy", "The platform fits the site, not the other way round.")
       + tiles([("Vehicle-mounted", "On a truck bed, ready in under 10 minutes. Used in our field trials."), ("Static mount", "On a fixed base for permanent protection."),
                ("Remote and solar", "With the solar package, for areas without grid power.")]), "sand")
 + sec(head("Where it protects", "Typical sites for counter-drone cover.") + tiles(USES)))

P["clients.html"] = ("Clients", "Anmay Defence works with the Indian armed forces, other defence organisations and private companies.",
 hero("truck-mounted-demo-with-team.jpg", "Who we work with", "Defence forces and private companies that need to protect their airspace.")
 + sec(head("Our clients", "We build for the Indian armed forces, other defence organisations and private companies. Client names are not listed here.")
       + tiles([("Indian armed forces", "Counter-drone systems made in India, for field use."), ("Defence organisations", "Platforms and mission packages for other defence users."),
                ("Private sector", "Airspace protection for critical infrastructure and industrial sites.")])
       + '<p style="margin-top:40px"><a class="btn" href="contact.html">Talk to our team</a></p>'))

P["deployments.html"] = ("Deployments", "Field trials and installations of the STRIKE counter-drone system.",
 hero("aerial-truck-field-trial-angle.jpg", "Deployments", "Field trials and installations of STRIKE.")
 + sec(head("From the field", "Photos and notes from our trials.") + '<div class="grid">'
       + card("strike-gen1-truck-mounted-side.jpg", "Vehicle-mounted STRIKE Gen 1", "A STRIKE turret on a truck bed. Trials covered 360° rotation, AI tracking and operator control.")
       + card("aerial-truck-field-trial-angle.jpg", "Aerial view of a field trial", "A drone filmed the vehicle-mounted system from above in the field.")
       + card("strike-gen1-fixed-base-installation.jpg", "Fixed-base installation", "STRIKE on a static base for permanent protection.")
       + card("strike-gen1-turret-field-view.jpg", "Built and tested in-house", "The turret, built by our team, during a field trial.") + "</div>"))

P["faq.html"] = ("FAQ", "Answers about STRIKE: range, drones it can track, power, deployment time, and about Anmay Defence.",
 sec("<h1>Frequently asked questions</h1>" + '<div class="grid" style="margin-top:48px">'
     + "".join(f'<a class="tile" href="#{k}"><h3>{t}</h3><p>{len(q)} questions</p></a>' for k, (t, q) in FAQ.items()) + "</div>"
     + '<div class="faq">' + "".join(f'<h2 id="{k}">{t}</h2>' + faq(q) for k, (t, q) in FAQ.items()) + "</div>", style=TOP))

P["contact.html"] = ("Contact", "Request a briefing on STRIKE from Anmay Defence.",
 sec('<div class="split"><div><h1>Request a briefing</h1><p style="margin:24px 0;font-size:1.15rem;max-width:26em">Tell us about your site and your airspace concerns. Pricing and lead times are shared in the briefing.</p>'
     + "".join(f"<p>{x}</p>" for x in [CONTACT["email"], CONTACT["phone"]] if x)
     + f'</div><form data-to="{CONTACT["email"]}"><input name="name" placeholder="Name" aria-label="Name" required><input name="org" placeholder="Organisation" aria-label="Organisation">'
       '<input name="email" type="email" placeholder="Email" aria-label="Email" required><select name="interest" aria-label="Interest"><option>STRIKE Gen 1</option><option>STRIKE Gen 2</option><option>Mission packages</option><option>Not sure yet</option></select>'
       '<textarea name="message" placeholder="Your message" aria-label="Message" required></textarea><button class="btn" type="submit">Prepare email</button>'
       '<p style="font-size:.85rem">This opens your email app with your message ready to send.</p><output></output></form></div>', style=TOP))

for fn, (title, desc, body, *js) in P.items():
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(shell(fn, title, desc, body, *js))
print("Built %d pages: %s" % (len(P), ", ".join(P)))
if not CONTACT["email"]: print("Note: CONTACT email is empty. Add it in tools/build_site.py so the contact form works.")
