/* STRIKE radar hero. An orange beam sweeps the sky, finds hostile drones, turns to follow the closest one,
   locks on and neutralises it. Click the radar to launch a test drone. Pauses off-screen; static frame if motion is reduced. */
(() => {
  const c = document.getElementById('radar'); if (!c) return;
  const g = c.getContext('2d'), TAU = Math.PI * 2, hud = document.getElementById('hud'), hero = c.parentElement;
  const still = matchMedia('(prefers-reduced-motion:reduce)').matches, O = '255,147,0', E = '255,120,40', C = '247,242,238';
  let W, H, dpr, cx, cy, R, sw = -1.2, aim = null, ds = [], booms = [], uid = 6, wait = 0, run = false, vis = true, last = 0, hudT = 0;
  const wrap = a => ((a + Math.PI) % TAU + TAU) % TAU - Math.PI, pad = n => String(n).padStart(2, '0');

  function fit() {
    const b = c.getBoundingClientRect(), wide = b.width > 820;
    dpr = Math.min(devicePixelRatio || 1, 2); W = b.width; H = b.height; c.width = W * dpr; c.height = H * dpr; g.setTransform(dpr, 0, 0, dpr, 0, 0);
    cx = W * (wide ? .7 : .5); cy = H * (wide ? .5 : .4); R = Math.min(wide ? W * .34 : W * .44, H * (wide ? .44 : .36));
  }
  function spawn(a, r) {
    ds.push({ id: uid++, a: a == null ? Math.random() * TAU : a, r: r == null ? R * 1.02 : r, v: R * (.032 + Math.random() * .02),
      ph: Math.random() * TAU, sp: (Math.random() - .5) * .1, x: cx, y: cy, seen: 0, lock: 0, dead: false, trail: [] });
  }
  function step(dt) {
    if (aim) sw = wrap(sw + wrap(aim.a - sw) * Math.min(1, dt * 4)); else sw = wrap(sw + .9 * dt);   // follow the target, or keep sweeping
    const now = performance.now();
    for (const d of ds) {
      d.r -= d.v * dt; d.a += d.sp * dt;
      const w = Math.sin(now / 700 + d.ph) * R * .012;
      d.x = cx + Math.cos(d.a) * d.r - Math.sin(d.a) * w; d.y = cy + Math.sin(d.a) * d.r + Math.cos(d.a) * w;
      if (Math.abs(wrap(d.a - sw)) < .1) d.seen = 1; else if (d !== aim) d.seen = Math.max(0, d.seen - dt * .45);
      const t = d.trail[d.trail.length - 1];
      if (!t || Math.hypot(d.x - t[0], d.y - t[1]) > 4) { d.trail.push([d.x, d.y]); if (d.trail.length > 36) d.trail.shift(); }
    }
    if (!aim) aim = ds.filter(d => d.seen > .9 && d.r < R * .95).sort((a, b) => a.r - b.r)[0] || null;
    if (aim) { aim.lock += dt; if (aim.lock > 2.4 && aim.r < R * .6) { aim.dead = true; booms.push({ x: aim.x, y: aim.y, t: 0 }); aim = null; } }
    for (const d of ds) if (d.r < R * .1) { d.dead = true; if (d === aim) aim = null; }
    ds = ds.filter(d => !d.dead);
    for (const b of booms) b.t += dt;
    booms = booms.filter(b => b.t < 1);
    if (ds.length < 3) { wait -= dt; if (wait <= 0) { spawn(); wait = 1.5 + Math.random() * 2; } }
  }
  function reticle(d) {
    const q = Math.min(1, d.lock / .8), r = 24 - 10 * q, st = d.lock > 2 ? 'ENGAGING' : d.lock > .8 ? 'LOCKED' : 'TRACKING';
    g.save(); g.translate(d.x, d.y); g.rotate(performance.now() / 700 * (1 - q)); g.strokeStyle = `rgb(${E})`; g.lineWidth = 1.5;
    for (let i = 0; i < 4; i++) { g.rotate(Math.PI / 2); g.beginPath(); g.moveTo(r, r * .4); g.lineTo(r, r); g.lineTo(r * .4, r); g.stroke(); }
    g.restore(); g.font = '500 11px "Inter Tight",sans-serif';
    g.fillStyle = `rgb(${C})`; g.fillText(`T-${pad(d.id)}  ${Math.round(d.r / R * 800)} m`, d.x + 30, d.y - 6);
    g.fillStyle = `rgba(${C},.6)`; g.fillText(st, d.x + 30, d.y + 9);
  }
  function draw() {
    g.clearRect(0, 0, W, H); g.lineWidth = 1;
    for (let i = 1; i <= 4; i++) { g.strokeStyle = `rgba(${C},${i === 4 ? .3 : .12})`; g.beginPath(); g.arc(cx, cy, R * i / 4, 0, TAU); g.stroke(); }
    g.strokeStyle = `rgba(${C},.1)`; g.beginPath(); g.moveTo(cx - R, cy); g.lineTo(cx + R, cy); g.moveTo(cx, cy - R); g.lineTo(cx, cy + R); g.stroke();
    for (let i = 0; i < 72; i++) {
      const a = i * TAU / 72, l = i % 6 ? 5 : 12; g.strokeStyle = `rgba(${C},${i % 6 ? .25 : .55})`;
      g.beginPath(); g.moveTo(cx + Math.cos(a) * R, cy + Math.sin(a) * R); g.lineTo(cx + Math.cos(a) * (R + l), cy + Math.sin(a) * (R + l)); g.stroke();
    }
    const L = 1;   // length of the beam tail, in radians
    if (g.createConicGradient) {
      const k = g.createConicGradient(sw - L, cx, cy);
      k.addColorStop(0, `rgba(${O},0)`); k.addColorStop(L / TAU, `rgba(${O},.32)`); k.addColorStop(Math.min(1, L / TAU + .001), `rgba(${O},0)`);
      g.fillStyle = k; g.beginPath(); g.moveTo(cx, cy); g.arc(cx, cy, R, sw - L, sw); g.fill();
    }
    g.save(); g.strokeStyle = `rgb(${O})`; g.lineWidth = 2; g.shadowColor = `rgb(${O})`; g.shadowBlur = 14;
    g.beginPath(); g.moveTo(cx, cy); g.lineTo(cx + Math.cos(sw) * R, cy + Math.sin(sw) * R); g.stroke(); g.restore();
    g.fillStyle = `rgb(${C})`; g.beginPath(); g.arc(cx, cy, 3, 0, TAU); g.fill();   // the protected site
    for (const d of ds) {
      if (d.seen <= 0) continue;
      const me = d === aim;
      if (me || d.seen > .3) { g.strokeStyle = `rgba(${O},${.55 * d.seen})`; g.lineWidth = 1.5; g.beginPath(); d.trail.forEach((p, i) => i ? g.lineTo(p[0], p[1]) : g.moveTo(p[0], p[1])); g.stroke(); }
      g.fillStyle = `rgba(${me ? E : C},${.35 + .65 * d.seen})`; g.beginPath(); g.arc(d.x, d.y, me ? 4 : 3, 0, TAU); g.fill();
      if (me) reticle(d);
    }
    for (const b of booms) { g.strokeStyle = `rgba(${O},${1 - b.t})`; g.lineWidth = 2; g.beginPath(); g.arc(b.x, b.y, 6 + b.t * 54, 0, TAU); g.stroke(); }
  }
  function ui() {
    if (!hud) return;
    const set = (id, v) => { const e = document.getElementById(id); if (e) e.textContent = v; };
    set('h1', ds.filter(d => d.seen > .2).length);
    set('h2', aim && aim.lock > .8 ? 'T-' + pad(aim.id) : '—');
    set('h3', aim ? Math.round(aim.r / R * 800) : '—');
  }
  function loop(ts) {
    if (!vis || document.hidden) { run = false; return; }
    const dt = Math.min(.05, (ts - last) / 1000 || 0); last = ts;
    step(dt); draw(); if ((hudT += dt) > .25) { hudT = 0; ui(); }
    requestAnimationFrame(loop);
  }
  function go() { if (!run && vis && !document.hidden) { run = true; last = performance.now(); requestAnimationFrame(loop); } }

  fit(); spawn(null, R * .92); spawn(null, R * .75); spawn();
  addEventListener('resize', fit); document.addEventListener('visibilitychange', go);
  hero.addEventListener('pointerdown', e => {   // click the radar to launch a test drone
    if (e.target.closest('a,button') || ds.length > 5) return;
    const b = c.getBoundingClientRect(), x = e.clientX - b.left - cx, y = e.clientY - b.top - cy, r = Math.hypot(x, y);
    if (r < R * 1.05 && r > R * .3) spawn(Math.atan2(y, x), r);
  });
  if (still) { for (let i = 0; i < 260; i++) step(.05); draw(); ui(); return; }
  new IntersectionObserver(e => { vis = e[0].isIntersecting; go(); }).observe(hero);
  go();
})();
