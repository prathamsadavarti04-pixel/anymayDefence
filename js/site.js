/* Anmay Defence: menu, tabs, drag-scroll rails, heading reveal, contact form. */
(() => {
  const d = document, $ = (s, r = d) => [...r.querySelectorAll(s)];
  const hd = $('header')[0], mb = $('.mbtn')[0];
  mb && mb.addEventListener('click', () => { const o = hd.classList.toggle('open'); mb.setAttribute('aria-expanded', o); mb.textContent = o ? 'Close' : 'Menu'; });
  $('.tabs').forEach(t => t.addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) return;
    [...t.children].forEach(x => { x.setAttribute('aria-selected', x === b); d.getElementById(x.getAttribute('aria-controls')).hidden = x !== b; });
  }));
  $('.rail').forEach(r => {
    let s = 0, x = 0, on = false;
    r.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; s = r.scrollLeft; x = e.clientX; on = true; r.style.scrollSnapType = 'none'; });
    addEventListener('pointermove', e => { if (on) r.scrollLeft = s - (e.clientX - x); });
    addEventListener('pointerup', () => { if (on) { on = false; r.style.scrollSnapType = ''; } });
  });
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .2 });
  $('.head').forEach(e => { e.classList.add('rv'); io.observe(e); });
  $('video').forEach(v => { if (matchMedia('(prefers-reduced-motion:reduce)').matches) { v.pause(); v.removeAttribute('autoplay'); } });
  const f = $('form')[0];
  f && f.addEventListener('submit', e => {
    e.preventDefault(); const o = $('output', f)[0], to = f.dataset.to;
    if (!to) { o.textContent = 'This form is not connected yet. Add the contact email in tools/build_site.py.'; return; }
    const v = Object.fromEntries(new FormData(f));
    location.href = 'mailto:' + to + '?subject=' + encodeURIComponent('Briefing request: ' + v.name) +
      '&body=' + encodeURIComponent(`Name: ${v.name}\nOrganisation: ${v.org}\nEmail: ${v.email}\nInterest: ${v.interest}\n\n${v.message}`);
  });
})();
