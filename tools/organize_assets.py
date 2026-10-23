#!/usr/bin/env python3
"""Anmay Defence asset organiser.
Gives every image and video a clear name and a clean folder, then writes
ASSET_MAP.md, TREE_OLD.txt and TREE_NEW.txt, and makes small web copies for the site.
Run from anywhere:  python tools/organize_assets.py   (safe to run twice)"""
import os, re, shutil, subprocess
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
IMG, VID = {'jpg', 'jpeg', 'png', 'webp'}, {'mp4', 'webm'}
NEW_DIRS = ('assets/images/', 'assets/videos/', 'assets/docs/', 'assets/models-3d/', 'assets/web/')
SKIP_OLD = {'.git', 'tools', 'legacy', 'css', 'js', 'ASSET_MAP.md', 'REPO_SUMMARY.md', 'TREE_OLD.txt', 'TREE_NEW.txt', 'assets/web'}

# (regex on the lower-case old path, folder, label). First match wins.
RULES = [
 (r'robonut project logo', 'branding', 'robonut-logo-hexagon'),
 (r'anmay defence \(wip\)', 'branding', 'anmay-trishul-emblem-wip'),
 (r'assmebly', 'renders', 'strike-gen1-exploded-assembly-diagram'),
 (r'prototype-w', 'renders', 'strike-prototype-turret-white-bg'),
 (r'strike 2 with radar', 'renders', 'strike-gen2-radar-concept-render'),
 (r'strike gen 2\.png', 'renders', 'strike-gen2-concept-render'),
 (r'strike m with lmg', 'renders', 'strike-m-lmg-concept-render'),
 (r'strike 2 m lmg', 'renders', 'strike-gen2-m-lmg-concept-render'),
 (r'meta ai', 'renders', 'ai-render-turret-desert-concept'),
 (r'20260919-wa0001', 'renders', 'strike-m-rover-brochure-graphic'),
 (r'shb3mz', 'renders', 'ai-render-strike-truck-dusk'),
 (r'removebg', 'renders', 'ai-render-strike-turret-cutout'),
 (r'gemini_generated', 'renders', 'ai-render-strike-turret'),
 (r'remote front', 'controller-and-software', 'remote-controller-front-buttons'),
 (r'20260705-wa00(23|34)|20260715-wa0045', 'controller-and-software', 'remote-controller-closeup'),
 (r'20260715-wa0088', 'controller-and-software', 'remote-controller-u-shape'),
 (r'rpi desktop', 'controller-and-software', 'raspberry-pi-desktop-screenshot'),
 (r'steps to run', 'controller-and-software', 'run-code-steps-notes'),
 (r'20260715-wa00(02|69|84|85)', 'exhibition', 'info-board-photo'),
 (r'screen-capture', 'ai-tracking-screens', 'operator-screen-capture'),
 (r'/video[68]\.mp4|20260918-wa001[23]|20260919-wa000[23]|20261005-wa00(44|54|57)|20260918_112150', 'ai-tracking-screens', 'operator-screen-ai-tracking'),
 (r'automation rpi', 'automation-demos', 'rpi-camera-auto-tracking-footage'),
 (r'truck video with rifle', 'automation-demos', 'truck-rifle-mounting-automation'),
 (r'truck video automation', 'automation-demos', 'truck-automation'),
 (r'strike m videos', 'strike-m', 'strike-m-test-trial'),
 (r'/video1\.mp4', 'field-trials', 'product-reveal-camo-turret'),
 (r'/video3\.mp4', 'field-trials', 'on-field-tested'),
 (r'/video7\.mp4', 'field-trials', 'autonomous-operation'),
 (r'/video[245]\.mp4', 'field-trials', 'shortlisted-turret-field-test'),
 (r'anmay strike trial', 'field-trials', 'strike-trial-footage-compilation'),
 (r'firing video', 'field-trials', 'firing-test'),
 (r'dji_fly', 'aerial-drone-shots', 'dji-aerial-field-trial'),
 (r'/1789709095', 'aerial-drone-shots', 'aerial-truck-mounted-strike-gen1'),
 (r'20250702', 'build-process', 'part-closeup'),
 (r'20250704', 'build-process', 'servo-trigger-wiring-and-measuring'),
 (r'20250712', 'build-process', 'raspberry-pi-case'),
 (r'20250713', 'build-process', 'servo-fitted-to-rifle'),
 (r'20250714', 'build-process', 'servo-trigger-assembly-hands-on'),
 (r'20250725', 'build-process', 'servo-bracket-fitting'),
 (r'2025072[78]', 'build-process', 'shaft-bearing-and-coupler-parts'),
 (r'20250729', 'build-process', 'rifle-servo-mount-fitting'),
 (r'20250730', 'build-process', 'metal-frame-fabrication'),
 (r'20250803_', 'field-trials', 'mast-antenna-test'),
 (r'202508', 'build-process', 'motor-and-frame-fabrication'),
 (r'20250906', 'field-trials', 'vehicle-structure-closeup'),
 (r'20251001_180630', 'field-trials', 'turret-on-mast-evening'),
 (r'20251002-wa', 'field-trials', 'truck-mounted-demo-with-people'),
 (r'20251002_10', 'field-trials', 'truck-mounted-turret-with-laptop'),
 (r'20251002_14', 'field-trials', 'turret-barrels-sky-view'),
 (r'20251004', 'field-trials', 'turret-yard-test'),
 (r'20260110', 'field-trials', 'turret-on-mast-test'),
 (r'shortlisted photo video/img/img\d', 'field-trials', 'shortlisted-turret-field-photo'),
 (r'installation image', 'field-trials', 'strike-gen1-fixed-base-installation'),
 (r'photos/imgs/', 'field-trials', 'strike-gen1-turret-closeup'),
 (r'20261005', 'field-trials', 'strike-gen1-truck-mounted-2026-10'),
 (r'2026091[789]', 'field-trials', 'strike-gen1-field-2026-09'),
 (r'20260705|20260702|20260715', 'field-trials', 'strike-gen1-field-2026-07'),
 (r'202606', 'field-trials', 'strike-gen1-field-2026-06'),
 (r'strike gen 1 shots|drone shot', 'field-trials', 'strike-gen1-field-trial'),
]
DOCS = {'strike product catalogue': 'strike-product-catalogue-gen1-gen2.pptx', 'prahar netra': 'prahar-netra-product-catalogue.pptx',
        'changes .pptx': 'video-edit-change-requests.pptx', 'anmay_drone_defence_video_script': 'anmay-drone-defence-video-script.docx',
        'strike_video_creation': 'strike-video-storyboard.docx', 'new video script': 'strike-launch-film-script.docx'}
# Small copies for the website: a piece of the old path -> (file name in assets/web, max width)
WEB = {'1789709095880.jpg': ('hero-aerial-truck-mounted-strike-gen1.jpg', 2000), '1789709095867.jpg': ('aerial-truck-field-trial-wide.jpg', 1600),
       '1789709095896.jpg': ('aerial-truck-field-trial-angle.jpg', 1600), 'img-20260715-wa0008.jpg': ('strike-gen1-truck-mounted-side.jpg', 1600),
       'img-20260715-wa0056.jpg': ('strike-gen1-turret-field-view.jpg', 1600), 'img-20260715-wa0082.jpg': ('strike-gen1-turret-landscape.jpg', 1600),
       'img-20251002-wa0026.jpg': ('truck-mounted-demo-with-team.jpg', 1600), 'installation image 1.jpeg': ('strike-gen1-fixed-base-installation.jpg', 1600),
       'photos/img/assmebly.jpg': ('strike-gen1-exploded-assembly.jpg', 1400), 'img-20260705-wa0034.jpg': ('remote-controller-closeup.jpg', 1000),
       'dji_fly_20260918_104626': ('aerial-field-trial-loop.mp4', 0)}


def tree(skip):
    out = ['.']
    def walk(d, pre):
        names = [(n, os.path.normpath(os.path.join(d, n)).replace('\\', '/')) for n in sorted(os.listdir(d))]
        names = [(n, r) for n, r in names if r not in skip and not (skip is SKIP_OLD and '/' not in r and r.endswith('.html') and r != 'index.html')]
        for i, (n, r) in enumerate(names):
            end = i == len(names) - 1
            out.append(pre + ('└── ' if end else '├── ') + n)
            if os.path.isdir(r): walk(r, pre + ('    ' if end else '│   '))
    walk('.', ''); return '\n'.join(out) + '\n'


def plan(p):
    low = p.lower(); ext = low.rsplit('.', 1)[-1]
    if low == 'assets/index.html': return 'legacy/assets-index-empty.html'
    if ext in ('docx', 'pptx'):
        for k, v in DOCS.items():
            if k in low: return 'assets/docs/' + v
    if ext in ('obj', 'mtl', 'mlt'):
        return 'assets/models-3d/next-gen-design-%s/%s' % ('1' if 'design_1' in low else '2', os.path.basename(p))
    kind = 'images' if ext in IMG else 'videos' if ext in VID else None
    if not kind: return None
    for pat, grp, lab in RULES:
        if re.search(pat, low): return (kind, grp, lab, ext)
    return (kind, 'unsorted', 'unsorted-media', ext)


def mv(a, b):
    os.makedirs(os.path.dirname(b), exist_ok=True)
    try: ok = subprocess.run(['git', 'mv', a, b], capture_output=True).returncode == 0
    except OSError: ok = False
    if not ok: shutil.move(a, b)


def web_copy(src, name, w):
    dst = 'assets/web/' + name; os.makedirs('assets/web', exist_ok=True)
    if os.path.exists(dst): return dst
    if name.endswith('.mp4'):   # 9 s muted loop + poster
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '1', '-t', '9', '-i', src, '-vf', 'scale=1280:-2,fps=24', '-an', '-c:v', 'libx264',
                        '-crf', '29', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', dst])
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '3', '-i', src, '-frames:v', '1', '-vf', 'scale=1280:-2', '-q:v', '4', dst.replace('.mp4', '-poster.jpg')])
    else:
        from PIL import Image, ImageOps
        im = Image.open(src); im.draft('RGB', (w, w)); im = ImageOps.exif_transpose(im).convert('RGB'); im.thumbnail((w, w))
        im.save(dst, 'JPEG', quality=78, optimize=True, progressive=True)
    return dst


files = sorted(f for f in (os.path.join(d, n).replace('\\', '/') for d, _, ns in os.walk('assets') for n in ns) if not f.startswith(NEW_DIRS))
if not os.path.exists('TREE_OLD.txt'): open('TREE_OLD.txt', 'w', encoding='utf-8').write(tree(SKIP_OLD))
cnt, moves = Counter(), {}
for p in files:
    r = plan(p)
    if r is None: continue
    if isinstance(r, tuple):
        kind, grp, lab, ext = r; cnt[(kind, grp, lab)] += 1
        r = 'assets/%s/%s/%s-%02d.%s' % (kind, grp, lab, cnt[(kind, grp, lab)], ext)
    moves[p] = r
if not moves: raise SystemExit('Nothing to move. Assets are already organised.')

for old, new in moves.items(): mv(old, new)
for d, _, _ in sorted(os.walk('assets'), reverse=True):
    try: os.rmdir(d)
    except OSError: pass

if os.path.exists('.gitattributes'):   # keep Git LFS tracking on the moved files
    fix = {o.replace(' ', '[[:space:]]'): n for o, n in moves.items()}
    lines = [l.replace(l.split(' filter=')[0], fix[l.split(' filter=')[0]]) if l.split(' filter=')[0] in fix else l for l in open('.gitattributes').read().splitlines()]
    open('.gitattributes', 'w').write('\n'.join(lines) + '\n')

web = {}
for old, new in moves.items():
    for k, (name, w) in WEB.items():
        if k in old.lower():
            try: web[new] = web_copy(new, name, w)
            except Exception as e: print('web copy skipped:', name, e)

md = ['# Asset map', '', 'Old path → new path. Made by `tools/organize_assets.py`. %d files moved or renamed.' % len(moves), '',
      '## Web copies (small files the website uses)', '', '| Source (new path) | Web copy |', '|---|---|']
md += ['| `%s` | `%s` |' % (s, w) for s, w in sorted(web.items(), key=lambda x: x[1])]
last = None
for old, new in sorted(moves.items(), key=lambda x: x[1]):
    g = os.path.dirname(new)
    if g != last: md += ['', '## `%s/`' % g, '', '| Old path | New name |', '|---|---|']; last = g
    md.append('| `%s` | `%s` |' % (old.replace('assets/', '', 1), os.path.basename(new)))
open('ASSET_MAP.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
open('TREE_NEW.txt', 'w', encoding='utf-8').write(tree({'.git'}))
print('Moved %d files. Web copies: %d. See ASSET_MAP.md, TREE_OLD.txt, TREE_NEW.txt' % (len(moves), len(web)))
