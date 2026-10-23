// Hero radar — ported verbatim from anmay-home-v1-backup.html (canvas #rc),
// only the blue palette was recoloured to the current amber theme.
var d=document;
(function(){var c=d.getElementById('rc');if(!c||!c.getContext)return;var w=window,x=c.getContext('2d'),W,H,S,rs,cx,cy,vis=1,TP=Math.PI*2,T0=performance.now(),L0=T0,rm=w.matchMedia('(prefers-reduced-motion:reduce)').matches,Q=[],PL=[],sd=11;
function rn(){sd=sd*16807%2147483647;return(sd-1)/2147483646}
function fit(){var b=c.parentNode.getBoundingClientRect(),r=Math.min(w.devicePixelRatio||1,2);W=b.width;H=b.height;c.width=W*r;c.height=H*r;x.setTransform(r,0,0,r,0,0);S=Math.max(110,W*.14);rs=S*1.35;cx=W>760?W*.74:W*.62;cy=H*.5}
function sp(k,pre){var e=rn()*4|0,m=70,x0,y0,tx,ty,v=k=='i'?62+rn()*14:34+rn()*26,dx,dy,l;
if(e==0){x0=-m;y0=rn()*H}else if(e==1){x0=W+m;y0=rn()*H}else if(e==2){x0=rn()*W;y0=-m}else{x0=rn()*W;y0=H+m}
if(k=='i'){tx=cx+(rn()-.5)*S;ty=cy+(rn()-.5)*S}else{tx=W-x0+(rn()-.5)*W*.4;ty=H-y0+(rn()-.5)*H*.5}
dx=tx-x0;dy=ty-y0;l=Math.hypot(dx,dy)||1;return{x:x0+dx/l*v*pre,y:y0+dy/l*v*pre,vx:dx/l*v,vy:dy/l*v,s:k=='i'?11:6+rn()*6,k:k,st:0,tm:0,tr:[],ph:rn()*9}}
function dr(o,col,al,gc,gl,t){x.save();x.translate(o.x,o.y+Math.sin(t*2+o.ph)*1.6);x.rotate(Math.atan2(o.vy,o.vx)+Math.PI/2);var s=o.s,g;
if(gl>.04){g=x.createRadialGradient(0,0,0,0,0,s*3.4);g.addColorStop(0,'rgba('+gc+','+(.6*Math.min(1,gl)).toFixed(2)+')');g.addColorStop(1,'rgba('+gc+',0)');x.fillStyle=g;x.beginPath();x.arc(0,0,s*3.4,0,TP);x.fill()}
x.strokeStyle='rgba('+col+','+al.toFixed(2)+')';x.fillStyle=x.strokeStyle;x.lineWidth=Math.max(1.2,s*.16);x.lineCap='round';
x.beginPath();x.moveTo(-s,-s);x.lineTo(s,s);x.moveTo(-s,s);x.lineTo(s,-s);x.stroke();
[[-1,-1],[1,-1],[1,1],[-1,1]].forEach(function(p,i){var rx=p[0]*s,ry=p[1]*s,ba=t*38+i*1.9;x.globalAlpha=.55;x.beginPath();x.arc(rx,ry,s*.62,0,TP);x.stroke();x.globalAlpha=1;x.beginPath();x.moveTo(rx-Math.cos(ba)*s*.6,ry-Math.sin(ba)*s*.6);x.lineTo(rx+Math.cos(ba)*s*.6,ry+Math.sin(ba)*s*.6);x.stroke()});
x.beginPath();x.arc(0,0,s*.45,0,TP);x.fill();x.fillStyle='rgba(255,195,90,'+Math.min(1,al+.25).toFixed(2)+')';x.beginPath();x.arc(0,-s*.62,Math.max(1.3,s*.17),0,TP);x.fill();x.restore()}
function step(t,dt){Q.forEach(function(o,i){var f=1,dc;
if(o.k=='i'){dc=Math.hypot(o.x-cx,o.y-cy);if(o.st==0&&dc<rs){o.st=1;o.tm=0;o.v0=[o.vx,o.vy];PL.push({t:t,x:o.x,y:o.y})}
if(o.st==1){o.tm+=dt;f=Math.max(.06,1-o.tm/1.2);if(o.tm>1.2){o.st=2;o.vx=-o.v0[0]*1.15;o.vy=-o.v0[1]*1.15;f=1}}}
o.x+=o.vx*dt*f;o.y+=o.vy*dt*f;var l=o.tr[o.tr.length-1];if(!l||Math.hypot(o.x-l.x,o.y-l.y)>5){o.tr.push({x:o.x,y:o.y});if(o.tr.length>26)o.tr.shift()}
if(o.x<-120||o.x>W+120||o.y<-120||o.y>H+120)Q[i]=sp(o.k,0)})}
function draw(t){x.clearRect(0,0,W,H);var a=(t*TP/10)%TP,i,k,g;
for(k=1;k<=7;k++){x.strokeStyle='rgba(255,255,255,'+(.16-k*.016).toFixed(3)+')';x.lineWidth=1;x.beginPath();x.arc(cx,cy,S*k,0,TP);x.stroke()}
g=x.createRadialGradient(cx,cy,0,cx,cy,S*1.7);g.addColorStop(0,'rgba(255,160,10,.3)');g.addColorStop(1,'rgba(255,160,10,0)');x.fillStyle=g;x.beginPath();x.arc(cx,cy,S*1.7,0,TP);x.fill();
for(i=0;i<3;i++){k=(t/6+i/3)%1;x.strokeStyle='rgba(255,195,90,'+(.32*(1-k)).toFixed(3)+')';x.lineWidth=1.5;x.beginPath();x.arc(cx,cy,rs+k*S*5.4,0,TP);x.stroke()}
x.strokeStyle='rgba(255,180,70,.75)';x.lineWidth=1.5;x.setLineDash([2,8]);x.beginPath();x.arc(cx,cy,rs,0,TP);x.stroke();x.setLineDash([]);
for(i=0;i<36;i++){x.fillStyle='rgba(255,160,10,'+(.2*(1-i/36)).toFixed(3)+')';x.beginPath();x.moveTo(cx,cy);x.arc(cx,cy,S*7,a-(i+1)*.04,a-i*.04);x.closePath();x.fill()}
x.strokeStyle='rgba(255,200,110,.45)';x.lineWidth=1.2;x.beginPath();x.moveTo(cx,cy);x.lineTo(cx+S*7*Math.cos(a),cy+S*7*Math.sin(a));x.stroke();
Q.forEach(function(o){var dl=(a-Math.atan2(o.y-cy,o.x-cx)+TP*4)%TP,b=Math.max(0,1-dl/(TP*.5)),red=o.k=='i'&&o.st>0,col=red?'240,70,85':o.k=='i'?'255,200,100':'228,235,250',al=Math.min(1,.34+.66*b+(o.k=='i'?.3:0));
o.tr.forEach(function(p,j){x.fillStyle='rgba('+col+','+(.35*al*j/o.tr.length).toFixed(3)+')';x.beginPath();x.arc(p.x,p.y,1.6,0,TP);x.fill()});
dr(o,col,al,red?'240,70,85':'255,170,40',red?1:b,t)});
PL=PL.filter(function(p){return t-p.t<1.6});PL.forEach(function(p){var q=(t-p.t)/1.6;x.strokeStyle='rgba(240,70,85,'+(.7*(1-q)).toFixed(3)+')';x.lineWidth=2;x.beginPath();x.arc(p.x,p.y,10+q*90,0,TP);x.stroke()})}
function loop(n){var t=(n-T0)/1000,dt=Math.min(.05,(n-L0)/1000);L0=n;if(vis&&!rm){step(t,dt);draw(t)}requestAnimationFrame(loop)}
fit();for(var i=0;i<6;i++)Q.push(sp(i<4?'p':'i',4+rn()*14));
w.addEventListener('resize',fit);new IntersectionObserver(function(e){vis=e[0].isIntersecting}).observe(c.parentNode);
if(rm)draw(6);else requestAnimationFrame(loop)})();
