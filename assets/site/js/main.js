
const b=document.getElementById('menuBtn'),m=document.getElementById('mnav');if(b)b.onclick=()=>m.style.display=m.style.display==='block'?'none':'block';
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});document.querySelectorAll('.rv').forEach(e=>io.observe(e));
document.querySelectorAll('[data-car]').forEach(w=>{let t=w.querySelector('.carousel');w.querySelectorAll('[data-dir]').forEach(x=>x.onclick=()=>t.scrollBy({left:+x.dataset.dir*360,behavior:'smooth'}))});
document.querySelectorAll('[data-count]').forEach(el=>{let end=+el.dataset.count,suf=el.dataset.suffix||'';new IntersectionObserver((en,o)=>{if(en[0].isIntersecting){let st=performance.now();(function f(n){let p=Math.min(1,(n-st)/1500);el.textContent=Math.round(end*p)+suf;if(p<1)requestAnimationFrame(f)})(st);o.disconnect()}},{threshold:.4}).observe(el)});

// Product: Gen1/Gen2 switch
document.querySelectorAll('[data-genbtn]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-genbtn]').forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('[data-gen]').forEach(p=>p.classList.toggle('on',p.dataset.gen===b.dataset.genbtn))});
// Product: addon tabs, auto-advance 6s (progress bar), pause on hover
document.querySelectorAll('[data-atabs]').forEach(w=>{const tis=[...w.querySelectorAll('.ati')],ps=[...w.querySelectorAll('.apanel')];let cur=0,timer;
function go(n){cur=n;tis.forEach((t,i)=>{t.classList.remove('on');if(i===n){void t.offsetWidth;t.classList.add('on')}});ps.forEach((p,i)=>p.classList.toggle('on',i===n))}
function auto(){clearInterval(timer);timer=setInterval(()=>go((cur+1)%tis.length),6000)}
tis.forEach((t,i)=>t.onclick=()=>{go(i);auto()});w.addEventListener('pointerenter',()=>clearInterval(timer));w.addEventListener('pointerleave',auto);if(tis.length){go(0);auto()}});
