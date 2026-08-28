# -*- coding: utf-8 -*-
"""Build the three pages of the 836 site from plates.py.

    python3 build.py

Writes index.html, history/index.html and map/index.html, and resizes the
source photographs into img/. Nothing here is hand-edited.
"""
import os, sys, glob, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plates import PLATES, SECTIONS, HISTORY, ALBUM, ERAS, TRACE, ZONES, PAGES

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = ("/Users/ldm/Library/CloudStorage/GoogleDrive-lbmann@gmail.com/My Drive/"
        "Programs/Property Manager/Documents/836 Reference/Photos")
IMG  = os.path.join(ROOT, "img")
os.makedirs(IMG, exist_ok=True)

FILES = {int(os.path.basename(f).split(" - ")[1]): f
         for f in glob.glob(os.path.join(SRC, "836 - *.jpg"))}

def sips(src, dst, width, q):
    subprocess.run(["sips","-Z",str(width),"-s","format","jpeg","-s","formatOptions",str(q),
                    src,"--out",dst], check=True, capture_output=True)

def dims(p):
    out = subprocess.check_output(["sips","-g","pixelWidth","-g","pixelHeight",p]).decode()
    w=h=0
    for l in out.splitlines():
        if "pixelWidth" in l:  w=int(l.split(":")[1])
        if "pixelHeight" in l: h=int(l.split(":")[1])
    return w,h

D = {}
for n in sorted(PLATES):
    small, large = os.path.join(IMG,"%02d-800.jpg"%n), os.path.join(IMG,"%02d-1600.jpg"%n)
    if not os.path.exists(small): sips(FILES[n], small, 800, 60)
    if not os.path.exists(large): sips(FILES[n], large, 1600, 62)
    w,h = dims(large)
    D[n] = {"w":w,"h":h,"s":"img/%02d-800.jpg"%n,"l":"img/%02d-1600.jpg"%n}

SPAN = {1:12,2:12,3:12,4:7,5:5,6:6,7:6,8:12,9:6,10:6,11:12,12:7,13:5,14:12,
        15:5,16:7,17:5,18:5,19:7,20:7,21:5,22:12,23:6,24:6,25:12}

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def slug(name): return name.replace("&amp;","and").lower().replace(" ","-").replace("--","-").strip("-")

# ------------------------------------------------------------------ shared shell

TOKENS = """
:root {
  --ground:#EBEEF1; --surface:#F8F9FA; --paper:#FFFFFF; --ink:#12171C; --muted:#5E6873;
  --accent:#1D3C61; --rule:#CDD3D9; --warn:#8C5A2E; --ok:#2F6B4F;
  --shadow:0 1px 2px rgba(18,23,28,.06),0 12px 32px rgba(18,23,28,.09);
  --serif:"Bodoni Moda",Georgia,"Times New Roman",serif;
  --sans:"Public Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}
@media (prefers-color-scheme: dark) {
  :root {
    --ground:#0E1216; --surface:#161B21; --paper:#E9ECEF; --ink:#E4E8EC; --muted:#939DA8;
    --accent:#82A6CC; --rule:#28303A; --warn:#C79461; --ok:#7BB894;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 14px 40px rgba(0,0,0,.5);
  }
}
*,*::before,*::after { box-sizing:border-box; }
html { -webkit-text-size-adjust:100%; scroll-behavior:smooth; }
body { margin:0; background:var(--ground); color:var(--ink); font-family:var(--sans);
  font-weight:300; line-height:1.62; -webkit-font-smoothing:antialiased; overflow-x:hidden; }
img { display:block; max-width:100%; height:auto; }
:focus-visible { outline:2px solid var(--accent); outline-offset:3px; }
.titleblock { position:sticky; top:0; z-index:40; display:flex; flex-wrap:wrap;
  gap:.2rem 1.5rem; justify-content:space-between; align-items:baseline;
  padding:.55rem clamp(1rem,4vw,3rem);
  padding-left:max(1rem,env(safe-area-inset-left)); padding-right:max(1rem,env(safe-area-inset-right));
  background:var(--surface); border-bottom:1px solid var(--rule);
  font-family:var(--mono); font-size:.62rem; letter-spacing:.08em; text-transform:uppercase;
  color:var(--muted); }
.titleblock b { color:var(--ink); font-weight:500; }
.pagenav { display:flex; gap:1.3rem; overflow-x:auto; -webkit-overflow-scrolling:touch;
  padding:.85rem clamp(1rem,4vw,3rem); border-bottom:1px solid var(--rule);
  font-family:var(--mono); font-size:.64rem; letter-spacing:.13em; text-transform:uppercase;
  scrollbar-width:none; }
.pagenav::-webkit-scrollbar { display:none; }
.pagenav a { color:var(--muted); text-decoration:none; white-space:nowrap; padding:.35rem 0;
  border-bottom:1px solid transparent; }
.pagenav a:hover { color:var(--accent); }
.pagenav a[aria-current="page"] { color:var(--ink); border-bottom-color:var(--accent); }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior:auto; }
  *,*::before,*::after { transition-duration:.01ms !important; animation-duration:.01ms !important; }
}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
 'family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500&family=IBM+Plex+Mono:wght@400;500'
 '&family=Public+Sans:wght@300;400;500&display=swap">')

def shell(title, desc, depth, active, body, css="", script=""):
    up = "../" * depth
    parts = []
    for href, label in PAGES:
        cur = ' aria-current="page"' if href == active else ''
        target = (up + href) or "./"
        parts.append(f'<a href="{target}"{cur}>{label}</a>')
    nav = "".join(parts)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#EBEEF1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E1216" media="(prefers-color-scheme: dark)">
{FONTS}
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='26' font-size='26'>&#127969;</text></svg>">
<style>{TOKENS}{css}</style>
</head>
<body>
<div class="titleblock">
  <span><b>836 Springs Fireplace Rd.</b> &nbsp;Springs, East Hampton, NY</span>
  <span>Photographs <b>Tim Williams</b></span>
</div>
<nav class="pagenav">{nav}</nav>
{body}
{script}
</body>
</html>
'''

# ------------------------------------------------------------------ page 1: gallery

GALLERY_CSS = """
.hero { position:relative; }
.hero img { width:100%; height:min(74vh,760px); object-fit:cover; }
.hero .scrim { position:absolute; inset:0; display:flex; flex-direction:column; justify-content:flex-end;
  padding:clamp(1.25rem,5vw,4rem);
  background:linear-gradient(to top,rgba(8,12,16,.88) 0%,rgba(8,12,16,.45) 36%,rgba(8,12,16,0) 70%);
  color:#F4F6F8; }
.hero .eyebrow { font-family:var(--mono); font-size:.62rem; letter-spacing:.2em; text-transform:uppercase;
  color:#B9C6D4; margin:0 0 .8rem; }
.hero h1 { font-family:var(--serif); font-weight:400; font-size:clamp(2rem,7vw,5.4rem); line-height:1.03;
  letter-spacing:-.015em; margin:0; text-wrap:balance; color:#FFF; }
.hero .sub { margin:.9rem 0 0; max-width:50ch; font-size:clamp(.88rem,1.6vw,1.05rem); color:#D3DCE5; }
.secnav { display:flex; gap:1.2rem; overflow-x:auto; padding:.9rem clamp(1rem,4vw,3rem);
  border-bottom:1px solid var(--rule); font-family:var(--mono); font-size:.62rem; letter-spacing:.12em;
  text-transform:uppercase; scrollbar-width:none; }
.secnav::-webkit-scrollbar { display:none; }
.secnav a { color:var(--muted); text-decoration:none; white-space:nowrap; padding:.4rem 0; }
.secnav a:hover { color:var(--accent); }
main { padding:0 clamp(1rem,4vw,3rem) 2rem; }
.sec { padding:clamp(2.4rem,6vw,5rem) 0 0; scroll-margin-top:6rem; }
.sechead { display:grid; gap:.3rem; padding-bottom:1.4rem; margin-bottom:1.7rem; border-bottom:1px solid var(--rule); }
.sechead h2 { font-family:var(--serif); font-weight:400; font-size:clamp(1.5rem,3.4vw,2.5rem); margin:0;
  letter-spacing:-.01em; text-wrap:balance; }
.sechead p { margin:0; color:var(--muted); font-size:.92rem; max-width:62ch; }
@media (min-width:820px) {
  .sechead { grid-template-columns:minmax(0,1fr) minmax(0,26rem); align-items:baseline; gap:2rem; }
  .sechead p { text-align:right; }
}
.grid { display:grid; grid-template-columns:repeat(12,1fr); gap:clamp(1.5rem,3vw,2.6rem); align-items:start; }
.plate { grid-column:span 12; margin:0; display:flex; flex-direction:column; gap:.7rem; }
@media (min-width:820px) { .plate { grid-column:span var(--span); } }
.shot { display:block; width:100%; padding:0; border:0; background:none; cursor:zoom-in;
  box-shadow:var(--shadow); overflow:hidden; line-height:0; }
.shot img { width:100%; transition:transform .5s cubic-bezier(.2,.7,.3,1); }
@media (hover:hover) { .shot:hover img { transform:scale(1.018); } }
figcaption { display:flex; gap:.8rem; align-items:baseline; }
.pno { font-family:var(--mono); font-size:.7rem; font-weight:500; color:var(--accent); flex:0 0 auto;
  padding-top:.15rem; font-variant-numeric:tabular-nums; }
.ptext { display:flex; flex-direction:column; gap:.2rem; min-width:0; }
.ptitle { font-family:var(--serif); font-size:1.02rem; line-height:1.3; }
.pcap { font-size:.82rem; color:var(--muted); line-height:1.55; }
.history { padding:clamp(2.4rem,6vw,5rem) 0 0; }
.hgrid { display:grid; gap:2rem; }
@media (min-width:760px) { .hgrid { grid-template-columns:repeat(2,minmax(0,1fr)); gap:2.4rem 3rem; } }
.hitem h3 { font-family:var(--serif); font-weight:400; font-size:1.2rem; margin:0 0 .5rem; }
.hitem p { margin:0; font-size:.9rem; color:var(--muted); max-width:60ch; }
.colophon { margin-top:clamp(3rem,8vw,6rem); padding:clamp(1.5rem,4vw,3rem); background:var(--surface);
  border:1px solid var(--rule); }
.colophon h2 { font-family:var(--mono); font-size:.64rem; letter-spacing:.18em; text-transform:uppercase;
  color:var(--accent); margin:0 0 1rem; font-weight:500; }
.colophon p { margin:0 0 .8rem; font-size:.86rem; color:var(--muted); max-width:64ch; }
.colophon p:last-child { margin-bottom:0; }
.lb { position:fixed; inset:0; z-index:100; display:none; background:rgba(8,12,16,.97);
  flex-direction:column; gap:.75rem; padding:clamp(.5rem,2vw,2rem);
  padding-top:max(.5rem,env(safe-area-inset-top)); padding-bottom:max(.75rem,env(safe-area-inset-bottom));
  touch-action:pan-y; }
.lb.on { display:flex; }
.lb .frame { flex:1; min-height:0; display:flex; align-items:center; justify-content:center; }
.lb .frame img { max-width:100%; max-height:100%; object-fit:contain; }
.lb .bar { display:flex; flex-wrap:wrap; gap:.3rem .9rem; align-items:baseline; justify-content:center;
  color:#D3DCE5; text-align:center; }
.lb .bar .n { font-family:var(--mono); font-size:.66rem; color:#8FB0D2; }
.lb .bar .t { font-family:var(--serif); font-size:1rem; color:#F4F6F8; }
.lb .bar .c { font-size:.78rem; color:#96A4B3; width:100%; max-width:60ch; margin:0 auto; }
.lb button { position:absolute; width:3rem; height:3rem; min-width:44px; min-height:44px;
  border:1px solid rgba(244,246,248,.3); background:rgba(8,12,16,.6); color:#F4F6F8; font-size:1.1rem;
  cursor:pointer; line-height:1; }
.lb .prev,.lb .next { top:50%; transform:translateY(-50%); }
.lb .prev { left:clamp(.4rem,2vw,1.5rem); }
.lb .next { right:clamp(.4rem,2vw,1.5rem); }
.lb .close { top:max(.5rem,env(safe-area-inset-top)); right:clamp(.4rem,2vw,1.5rem);
  width:2.75rem; height:2.75rem; }
@media (max-width:700px) { .lb .prev,.lb .next { display:none; } }
"""

def build_gallery():
    def fig(n):
        t, cap = PLATES[n]; d = D[n]
        return (f'<figure class="plate" style="--span:{SPAN[n]}">'
          f'<button class="shot" type="button" data-n="{n}" aria-label="Enlarge plate {n:02d}, {esc(t)}">'
          f'<img src="{d["s"]}" srcset="{d["s"]} 800w, {d["l"]} 1600w" '
          f'sizes="(max-width:820px) 100vw, {int(SPAN[n]/12*100)}vw" '
          f'width="{d["w"]}" height="{d["h"]}" alt="{esc(t)}" loading="lazy" decoding="async"></button>'
          f'<figcaption><span class="pno">{n:02d}</span><span class="ptext">'
          f'<span class="ptitle">{t}</span><span class="pcap">{cap}</span></span></figcaption></figure>')
    secs, nav = [], []
    for name, blurb, ps in SECTIONS:
        s = slug(name); nav.append(f'<a href="#{s}">{name}</a>')
        secs.append(f'<section class="sec" id="{s}"><header class="sechead"><h2>{name}</h2>'
                    f'<p>{blurb}</p></header><div class="grid">{"".join(fig(n) for n in ps)}</div></section>')
    hist = "".join(f'<article class="hitem"><h3>{h}</h3><p>{b}</p></article>' for _,h,b in HISTORY)
    hero = D[1]
    meta = json.dumps({str(n):{"t":PLATES[n][0],"c":PLATES[n][1],"l":D[n]["l"]} for n in PLATES})
    order = json.dumps([n for _,_,ps in SECTIONS for n in ps])
    body = f'''
<header class="hero">
  <img src="{hero['s']}" srcset="{hero['s']} 800w, {hero['l']} 1600w" sizes="100vw"
       width="{hero['w']}" height="{hero['h']}" fetchpriority="high"
       alt="Aerial view of 836 Springs Fireplace Road, with Accabonac Harbor beyond">
  <div class="scrim">
    <p class="eyebrow">Springs &middot; East Hampton &middot; Accabonac Harbor</p>
    <h1>836 Springs Fireplace Road</h1>
    <p class="sub">Twenty-five photographs of the finished house &mdash; a salt-marsh property on Accabonac Harbor, next door to the Merrill Lake Sanctuary and a few hundred feet from the barn where Jackson Pollock made the drip paintings.</p>
  </div>
</header>
<nav class="secnav">{"".join(nav)}<a href="#history">History</a></nav>
<main>
{"".join(secs)}
<section class="history" id="history">
  <header class="sechead"><h2>Where this is</h2><p>The neighbourhood does a lot of the work here.</p></header>
  <div class="hgrid">{hist}</div>
</section>
<section class="colophon">
  <h2>About this set</h2>
  <p>Photographs by Tim Williams. Sequenced as a walkthrough rather than in shooting order; each caption names the finishes legible in the frame. The images here are web-resolution exports &mdash; the full-resolution originals sit with the photographer.</p>
  <p>Private record for the owners of 836 Springs Fireplace Road. Not for republication.</p>
</section>
</main>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Enlarged photograph">
  <div class="frame"><img id="lbimg" alt=""></div>
  <div class="bar"><span class="n" id="lbn"></span><span class="t" id="lbt"></span><span class="c" id="lbc"></span></div>
  <button class="prev" id="lbprev" aria-label="Previous">&#8592;</button>
  <button class="next" id="lbnext" aria-label="Next">&#8594;</button>
  <button class="close" id="lbclose" aria-label="Close">&#10005;</button>
</div>'''
    script = f'''<script>
(function(){{
  var META={meta}, ORDER={order};
  var lb=document.getElementById("lb"), im=document.getElementById("lbimg");
  var en=document.getElementById("lbn"), et=document.getElementById("lbt"), ec=document.getElementById("lbc");
  var i=-1,last=null;
  function pad(n){{return (n<10?"0":"")+n;}}
  function show(k){{ if(k<0)k=ORDER.length-1; if(k>=ORDER.length)k=0; i=k;
    var n=ORDER[k], m=META[String(n)];
    im.src=m.l; im.alt=m.t; en.textContent="Plate "+pad(n); et.textContent=m.t; ec.textContent=m.c; }}
  function open(n){{ last=document.activeElement; lb.classList.add("on"); show(ORDER.indexOf(n));
    document.body.style.overflow="hidden"; document.getElementById("lbclose").focus(); }}
  function close(){{ lb.classList.remove("on"); im.src=""; document.body.style.overflow=""; if(last)last.focus(); }}
  document.querySelectorAll(".shot").forEach(function(b){{
    b.addEventListener("click",function(){{ open(parseInt(b.dataset.n,10)); }}); }});
  document.getElementById("lbprev").addEventListener("click",function(){{show(i-1);}});
  document.getElementById("lbnext").addEventListener("click",function(){{show(i+1);}});
  document.getElementById("lbclose").addEventListener("click",close);
  lb.addEventListener("click",function(e){{ if(e.target===lb||e.target.className==="frame") close(); }});
  document.addEventListener("keydown",function(e){{ if(!lb.classList.contains("on"))return;
    if(e.key==="Escape")close(); else if(e.key==="ArrowLeft")show(i-1); else if(e.key==="ArrowRight")show(i+1); }});
  var x0=null,y0=null;
  lb.addEventListener("touchstart",function(e){{x0=e.touches[0].clientX;y0=e.touches[0].clientY;}},{{passive:true}});
  lb.addEventListener("touchend",function(e){{ if(x0===null)return;
    var dx=e.changedTouches[0].clientX-x0, dy=e.changedTouches[0].clientY-y0;
    if(Math.abs(dx)>50&&Math.abs(dx)>Math.abs(dy)) show(dx<0?i+1:i-1);
    else if(dy>90&&Math.abs(dy)>Math.abs(dx)) close(); x0=y0=null; }},{{passive:true}});
}})();
</script>'''
    return shell("836 Springs Fireplace Road",
                 "Photographs of the finished house at 836 Springs Fireplace Road, Springs, East Hampton.",
                 0, "", body, GALLERY_CSS, script)

# ------------------------------------------------------------------ page 2: history

HISTORY_CSS = """
.wrap { max-width:74rem; margin:0 auto; padding:0 clamp(1rem,4vw,3rem) 4rem; }
header.top { padding:clamp(2.2rem,6vw,4rem) 0 clamp(1.4rem,3vw,2.4rem); border-bottom:1px solid var(--rule); }
.eyebrow { font-family:var(--mono); font-size:.64rem; letter-spacing:.2em; text-transform:uppercase;
  color:var(--accent); margin:0 0 .9rem; }
h1 { font-family:var(--serif); font-weight:400; font-size:clamp(2rem,6vw,4.2rem); line-height:1.04;
  margin:0; letter-spacing:-.015em; text-wrap:balance; }
.lede { margin:1.1rem 0 0; max-width:60ch; color:var(--muted); font-size:clamp(.95rem,1.7vw,1.1rem); }
.era { padding:clamp(2.2rem,6vw,4.2rem) 0 0; }
.erahead { display:flex; gap:1.2rem; align-items:baseline; padding-bottom:1rem;
  border-bottom:1px solid var(--rule); margin-bottom:1.3rem; }
.roman { font-family:var(--serif); font-size:clamp(1.8rem,4vw,3rem); color:var(--accent); line-height:1; }
.erahead h2 { font-family:var(--serif); font-weight:400; font-size:clamp(1.5rem,3.2vw,2.3rem);
  margin:0; letter-spacing:-.01em; }
.sub { margin:.2rem 0 0; font-family:var(--mono); font-size:.64rem; letter-spacing:.13em;
  text-transform:uppercase; color:var(--muted); }
.erabody { max-width:62ch; margin:0 0 1.7rem; font-size:.97rem; }
.shots { display:grid; gap:1.4rem; }
@media (min-width:760px) { .shots { grid-template-columns:repeat(3,minmax(0,1fr)); gap:1.8rem; } }
.shots figure { margin:0; display:flex; flex-direction:column; gap:.6rem; }
.shots img { width:100%; box-shadow:var(--shadow); }
.shots figcaption { font-size:.79rem; color:var(--muted); line-height:1.5; }
h2.sec { font-family:var(--serif); font-weight:400; font-size:clamp(1.5rem,3.2vw,2.3rem);
  margin:0 0 .4rem; letter-spacing:-.01em; }
.seclede { margin:0 0 1.5rem; color:var(--muted); font-size:.92rem; max-width:62ch; }
.tracewrap { margin-top:clamp(2.4rem,6vw,4.2rem); }
.tablescroll { overflow-x:auto; }
table { border-collapse:collapse; width:100%; min-width:44rem; font-size:.87rem; }
th,td { text-align:left; padding:.85rem 1rem .85rem 0; border-bottom:1px solid var(--rule); vertical-align:top; }
thead th { font-family:var(--mono); font-size:.61rem; letter-spacing:.13em; text-transform:uppercase;
  color:var(--accent); font-weight:500; border-bottom:1px solid var(--accent); }
tbody th { font-weight:500; white-space:nowrap; padding-right:1.5rem; }
td.note { color:var(--muted); min-width:22rem; }
tbody td:nth-child(2),tbody td:nth-child(3) { font-family:var(--mono); font-size:.72rem;
  white-space:nowrap; padding-right:1.5rem; }
.caveat { margin-top:clamp(2.4rem,6vw,4rem); padding:clamp(1.3rem,3vw,2.2rem); background:var(--surface);
  border:1px solid var(--rule); border-left:3px solid var(--warn); }
.caveat h2 { font-family:var(--mono); font-size:.64rem; letter-spacing:.18em; text-transform:uppercase;
  color:var(--warn); margin:0 0 .9rem; font-weight:500; }
.caveat li { margin-bottom:.6rem; font-size:.88rem; color:var(--muted); max-width:64ch; }
.caveat li:last-child { margin-bottom:0; }
.caveat b { color:var(--ink); font-weight:500; }
"""

def build_history():
    def shots(album_ids, plate_ids):
        out=[]
        for a in album_ids:
            out.append(f'<figure><img src="../img/album/a{a:02d}.jpg" alt="{esc(ALBUM[a])}" loading="lazy">'
                       f'<figcaption>{ALBUM[a]}</figcaption></figure>')
        for p in plate_ids:
            out.append(f'<figure><img src="../{D[p]["s"]}" alt="{esc(PLATES[p][0])}" loading="lazy">'
                       f'<figcaption>{PLATES[p][0]}</figcaption></figure>')
        return f'<div class="shots">{"".join(out)}</div>'
    eras = "".join(
        f'<section class="era"><div class="erahead"><span class="roman">{r}</span>'
        f'<div><h2>{t}</h2><p class="sub">{s}</p></div></div>'
        f'<p class="erabody">{b}</p>{shots(al,pl)}</section>'
        for r,t,s,b,al,pl in ERAS)
    rows = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td class="note">{d}</td></tr>'
                   for a,b,c,d in TRACE)
    body = f'''<div class="wrap">
<header class="top">
  <p class="eyebrow">836 Springs Fireplace Road</p>
  <h1>Three renovations, one barn</h1>
  <p class="lede">Read from a survey, a photograph album, and a set of finished-house pictures &mdash; what the property was, what the renovation before this one did to it, and what is still standing from each.</p>
</header>
{eras}
<section class="tracewrap">
  <h2 class="sec">What survived what</h2>
  <p class="seclede">Traced element by element across the two renovations. Where the evidence runs out, the row says so.</p>
  <div class="tablescroll"><table>
    <thead><tr><th>Element</th><th>Previous renovation</th><th>This one</th><th>Evidence</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
</section>
<section class="caveat">
  <h2>What would sharpen this</h2>
  <ol>
    <li><b>Which building is which.</b> The album shows a barn, a dwelling and a shed range as separate things; the 2021 survey shows one merged footprint. Walking the plan on site would pin each down.</li>
    <li><b>When the previous renovation happened.</b> Film prints, cordless tools and the trucks in frame read late 1990s to mid 2000s, but nothing in the album is dated. A permit or CO would fix it.</li>
    <li><b>The pool.</b> It is in the early photographs and gone from the current ones, and it is not on the 2021 survey at all.</li>
    <li><b>The salvage.</b> Wide-plank floors and a carved cast-iron firebox were photographed as kept pieces. Whether either is in the house now is not something the photographs answer.</li>
  </ol>
</section>
</div>'''
    return shell("Three renovations, one barn",
                 "How 836 Springs Fireplace Road changed across two renovations, and what survived each.",
                 1, "history/", body, HISTORY_CSS)

# ------------------------------------------------------------------ page 3: map

MAP_CSS = """
.wrap { max-width:80rem; margin:0 auto; padding:0 clamp(1rem,4vw,3rem) 4rem; }
header.top { padding:clamp(2.2rem,6vw,4rem) 0 1.5rem; }
.eyebrow { font-family:var(--mono); font-size:.64rem; letter-spacing:.2em; text-transform:uppercase;
  color:var(--accent); margin:0 0 .9rem; }
h1 { font-family:var(--serif); font-weight:400; font-size:clamp(2rem,5.5vw,3.6rem); line-height:1.05;
  margin:0; letter-spacing:-.015em; text-wrap:balance; }
.lede { margin:1rem 0 0; max-width:62ch; color:var(--muted); font-size:clamp(.94rem,1.6vw,1.05rem); }
.rule { margin:1.1rem 0 0; max-width:64ch; font-size:.84rem; color:var(--muted);
  border-left:2px solid var(--accent); padding-left:.9rem; }
.rule b { color:var(--ink); font-weight:500; }
.layout { display:grid; gap:1.5rem; }
@media (min-width:1000px) { .layout { grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);
  gap:2.5rem; align-items:start; } }
.mapwrap { position:sticky; top:1rem; }
@media (max-width:999px) { .mapwrap { position:static; } }
.prompt { display:flex; gap:.55rem; align-items:center; margin:0 0 .7rem; font-family:var(--mono);
  font-size:.64rem; letter-spacing:.11em; text-transform:uppercase; color:var(--accent); }
.prompt .dot { width:1.35rem; height:1.35rem; border-radius:50%; background:var(--accent); color:#fff;
  display:grid; place-items:center; font-size:.6rem; border:2px solid #fff;
  box-shadow:0 1px 4px rgba(0,0,0,.3); flex:0 0 auto; }
.mapbox { position:relative; background:var(--paper); border:1px solid var(--rule); box-shadow:var(--shadow); }
.mapbox > img { width:100%; }
.pin { position:absolute; transform:translate(-50%,-50%); width:2.1rem; height:2.1rem; min-width:34px;
  min-height:34px; border-radius:50%; border:2px solid #fff; background:var(--accent); color:#fff;
  font-family:var(--mono); font-size:.78rem; font-weight:500; cursor:pointer; padding:0;
  box-shadow:0 2px 8px rgba(0,0,0,.35); transition:transform .18s ease, box-shadow .18s ease; }
.pin span { pointer-events:none; }
.pin.inferred { background:var(--warn); border-style:dashed; }
.pin.confirmed { background:var(--ok); }
.pin:hover { transform:translate(-50%,-50%) scale(1.18); }
.pin[aria-current="true"] { transform:translate(-50%,-50%) scale(1.35);
  box-shadow:0 0 0 6px rgba(29,60,97,.25),0 2px 10px rgba(0,0,0,.4); z-index:5; }
.north { position:absolute; right:2.5%; top:3%; font-family:var(--mono); font-size:.62rem;
  letter-spacing:.14em; color:#333; text-align:center; }
.north b { display:block; font-size:1.05rem; line-height:1; }
.mapnote { margin:.8rem 0 0; font-size:.76rem; color:var(--muted); }
.panel { background:var(--surface); border:1px solid var(--rule); border-top:3px solid var(--accent);
  padding:clamp(1.1rem,2.5vw,1.8rem); scroll-margin-top:1rem; }
.panel.confirmed { border-top-color:var(--ok); }
.panel.inferred { border-top-color:var(--warn); }
.panelhead { display:flex; gap:.9rem; align-items:flex-start; margin-bottom:.5rem; }
.badge { flex:0 0 auto; width:2.1rem; height:2.1rem; border-radius:50%; display:grid; place-items:center;
  background:var(--accent); color:#fff; font-family:var(--mono); font-size:.78rem; font-weight:500;
  border:2px solid #fff; box-shadow:0 2px 8px rgba(0,0,0,.3); }
.badge.confirmed { background:var(--ok); }
.badge.inferred { background:var(--warn); border-style:dashed; }
.panelhead h2 { font-family:var(--serif); font-weight:400; font-size:1.45rem; margin:.05rem 0 .3rem;
  line-height:1.2; }
.tag { display:inline-block; font-family:var(--mono); font-size:.56rem; letter-spacing:.13em;
  text-transform:uppercase; padding:.16rem .45rem; border:1px solid var(--rule); }
.tag.surveyed { color:var(--accent); }
.tag.inferred { color:var(--warn); border-color:var(--warn); }
.tag.confirmed { color:var(--ok); border-color:var(--ok); }
.blurb { margin:1rem 0 1.3rem; font-size:.88rem; color:var(--muted); }
.stepper { display:flex; align-items:center; gap:.7rem; margin-bottom:1.2rem; padding-bottom:1rem;
  border-bottom:1px solid var(--rule); }
.stepper button { flex:0 0 auto; min-width:44px; min-height:38px; padding:.4rem .8rem;
  font-family:var(--mono); font-size:.62rem; letter-spacing:.08em; text-transform:uppercase;
  background:none; color:var(--muted); border:1px solid var(--rule); cursor:pointer; }
.stepper button:hover { color:var(--ink); border-color:var(--accent); }
.stepper .pos { flex:1; text-align:center; font-family:var(--mono); font-size:.62rem;
  letter-spacing:.11em; text-transform:uppercase; color:var(--muted); }
.grouphead { font-family:var(--mono); font-size:.6rem; letter-spacing:.16em; text-transform:uppercase;
  color:var(--accent); margin:1.3rem 0 .7rem; padding-bottom:.35rem; border-bottom:1px solid var(--rule); }
.grouphead:first-of-type { margin-top:0; }
.thumbs { display:grid; grid-template-columns:repeat(auto-fill,minmax(9rem,1fr)); gap:.9rem; }
.thumbs figure { margin:0; }
.thumbs img { width:100%; box-shadow:var(--shadow); cursor:zoom-in; }
.thumbs figcaption { margin-top:.35rem; font-size:.72rem; color:var(--muted); line-height:1.4; }
.empty { font-size:.82rem; color:var(--muted); font-style:italic; }
#pbody { animation:swap .32s ease both; }
@keyframes swap { from { opacity:0; transform:translateY(6px); } to { opacity:1; transform:none; } }
.caveat { margin-top:clamp(2rem,5vw,3.5rem); padding:clamp(1.2rem,3vw,2rem); background:var(--surface);
  border:1px solid var(--rule); border-left:3px solid var(--warn); }
.caveat h2 { font-family:var(--mono); font-size:.64rem; letter-spacing:.18em; text-transform:uppercase;
  color:var(--warn); margin:0 0 .9rem; font-weight:500; }
.caveat p { margin:0 0 .7rem; font-size:.87rem; color:var(--muted); max-width:66ch; }
.caveat p:last-child { margin-bottom:0; }
.caveat b { color:var(--ink); font-weight:500; }
.lb { position:fixed; inset:0; z-index:100; display:none; background:rgba(8,12,16,.97);
  flex-direction:column; gap:.8rem; padding:clamp(.6rem,2vw,2rem); }
.lb.on { display:flex; }
.lb .frame { flex:1; min-height:0; display:flex; align-items:center; justify-content:center; }
.lb .frame img { max-width:100%; max-height:100%; object-fit:contain; }
.lb .cap { text-align:center; color:#D3DCE5; font-size:.85rem; }
.lb button { position:absolute; top:clamp(.5rem,2vw,1.5rem); right:clamp(.5rem,2vw,1.5rem);
  width:2.75rem; height:2.75rem; min-width:44px; min-height:44px;
  border:1px solid rgba(244,246,248,.3); background:rgba(8,12,16,.6); color:#F4F6F8;
  font-size:1.1rem; cursor:pointer; }
@media (prefers-reduced-motion:reduce) { #pbody { animation:none; } .pin { transition:none; } }
"""

CONF = {
    "surveyed":            ("surveyed",  "On the survey"),
    "confirmed by Lindsay":("confirmed", "Confirmed by the owner"),
    "position approximate":("inferred",  "Position approximate"),
}

def build_map():
    pins = "".join(
      f'<button class="pin {CONF[cf][0]}" style="left:{x}%;top:{y}%" data-z="{k}" '
      f'aria-label="Marker {i+1}: {l.replace("&amp;","and")}"><span>{i+1}</span></button>'
      for i,(k,l,x,y,b,al,nw,cf) in enumerate(ZONES))
    data = json.dumps({
      "order": [z[0] for z in ZONES],
      "zones": {k:{"label":l.replace("&amp;","&"),"blurb":b,"album":al,"now":nw,
                   "conf":CONF[cf][0],"conflabel":CONF[cf][1],"n":i+1}
                for i,(k,l,x,y,b,al,nw,cf) in enumerate(ZONES)},
      "album": {str(k):{"c":v,"src":"../img/album/a%02d.jpg"%k} for k,v in ALBUM.items()},
      "now":   {str(n):{"c":PLATES[n][0],"src":"../"+D[n]["s"]} for n in PLATES},
    })
    body = ('<div class="wrap">\n'
'<header class="top">\n'
'  <p class="eyebrow">Gary Benz survey &middot; Grimes plan, 18 November 2021</p>\n'
'  <h1>Where each photograph was taken</h1>\n'
'  <p class="lede">The surveyed site plan, with the album photographs from the renovation before this one set against the finished house.</p>\n'
'  <p class="rule"><b>How things are filed:</b> an <b>interior</b> sits under the building it is inside; an <b>exterior</b> sits under the ground the camera was standing on. So every outside view of the barn is under the east side rather than under the barn. A few photographs show more than one thing and appear in more than one place.</p>\n'
'</header>\n'
'<div class="layout">\n'
'  <div class="mapwrap">\n'
'    <p class="prompt"><span class="dot">1</span> Tap a marker &mdash; the photographs below change</p>\n'
'    <div class="mapbox">\n'
'      <img src="../img/plan.jpg" alt="Site plan of 836 Springs Fireplace Road showing the lot, driveway, building footprint and wetland buffer">\n'
'      <div class="north"><b>&#8593;</b>N</div>\n'
'      ' + pins + '\n'
'    </div>\n'
'    <p class="mapnote">Lot 130&prime; &times; 220&prime;. Road and motor court west, wetlands east. Solid markers sit on something the survey labels or the owner confirmed; <b>a dashed marker is placed by eye.</b></p>\n'
'  </div>\n'
'  <div class="panel" id="panel">\n'
'    <div class="panelhead">\n'
'      <span class="badge" id="pbadge">1</span>\n'
'      <div><h2 id="ptitle"></h2><span class="tag" id="ptag"></span></div>\n'
'    </div>\n'
'    <p class="blurb" id="pblurb"></p>\n'
'    <div class="stepper">\n'
'      <button type="button" id="pprev">&larr; Prev</button>\n'
'      <span class="pos" id="ppos"></span>\n'
'      <button type="button" id="pnext">Next &rarr;</button>\n'
'    </div>\n'
'    <div id="pbody"></div>\n'
'  </div>\n'
'</div>\n'
'<section class="caveat">\n'
'  <h2>How to read this map</h2>\n'
'  <p><b>The property was four separate buildings, running roughly west to east:</b> the volume that is now the front entrance, the garage range beside it, the building that became the great room, and furthest east &mdash; closest to the water &mdash; the barn. The previous renovation pulled them into the single footprint the survey draws.</p>\n'
'  <p><b>The survey never subdivides that footprint.</b> It labels <i>2 Story Frame Dwelling</i>, <i>Porch</i>, <i>Brick Patio</i> and <i>Wood Steps</i>, and nothing else. So the markers for the entrance, the great room and the barn are placed along the west-to-east order the photographs establish, not on lines anyone surveyed. The order is solid; the exact positions are not.</p>\n'
'  <p><b>The plan is dated during this renovation, not before it.</b> Everything marked <i>Proposed</i> &mdash; the deck, the driveway, the septic &mdash; is the current work; everything marked <i>Existing</i> is what the previous renovation left behind.</p>\n'
'</section>\n'
'</div>\n'
'<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Enlarged photograph">\n'
'  <div class="frame"><img id="lbimg" alt=""></div>\n'
'  <p class="cap" id="lbcap"></p>\n'
'  <button id="lbclose" aria-label="Close">&#10005;</button>\n'
'</div>')
    script = ('<script>\n(function(){\n'
'  var D=' + data + ', ORDER=D.order, at=0;\n'
'  var panel=document.getElementById("panel"), body=document.getElementById("pbody");\n'
'  var badge=document.getElementById("pbadge"), title=document.getElementById("ptitle");\n'
'  var tag=document.getElementById("ptag"), blurb=document.getElementById("pblurb");\n'
'  var pos=document.getElementById("ppos");\n'
'  function thumbs(ids,pool){\n'
'    if(!ids.length) return \'<p class="empty">Nothing from this period shows this part of the property.</p>\';\n'
'    return \'<div class="thumbs">\'+ids.map(function(i){\n'
'      var m=pool[String(i)]; if(!m) return "";\n'
'      return \'<figure><img src="\'+m.src+\'" alt="\'+m.c+\'" data-cap="\'+m.c+\'" loading="lazy">\'\n'
'           + \'<figcaption>\'+m.c+\'</figcaption></figure>\';\n'
'    }).join("")+\'</div>\';\n'
'  }\n'
'  function show(k, scroll){\n'
'    var z=D.zones[k]; at=ORDER.indexOf(k);\n'
'    badge.textContent=z.n; badge.className="badge "+z.conf;\n'
'    panel.className="panel "+z.conf;\n'
'    title.textContent=z.label;\n'
'    tag.textContent=z.conflabel; tag.className="tag "+z.conf;\n'
'    blurb.innerHTML=z.blurb;\n'
'    pos.textContent="Marker "+z.n+" of "+ORDER.length;\n'
'    body.innerHTML=\'<p class="grouphead">Before this renovation</p>\'+thumbs(z.album,D.album)\n'
'                  +\'<p class="grouphead">Today</p>\'+thumbs(z.now,D.now);\n'
'    body.style.animation="none"; void body.offsetWidth; body.style.animation="";\n'
'    document.querySelectorAll(".pin").forEach(function(el){\n'
'      el.setAttribute("aria-current", el.dataset.z===k ? "true" : "false"); });\n'
'    if(scroll && window.matchMedia("(max-width:999px)").matches){\n'
'      panel.scrollIntoView({behavior:"smooth", block:"start"}); }\n'
'  }\n'
'  document.querySelectorAll(".pin").forEach(function(el){\n'
'    el.addEventListener("click",function(){ show(el.dataset.z, true); }); });\n'
'  document.getElementById("pprev").addEventListener("click",function(){\n'
'    show(ORDER[(at-1+ORDER.length)%ORDER.length], false); });\n'
'  document.getElementById("pnext").addEventListener("click",function(){\n'
'    show(ORDER[(at+1)%ORDER.length], false); });\n'
'  show(ORDER[0], false);\n'
'  var lb=document.getElementById("lb"), im=document.getElementById("lbimg"), cap=document.getElementById("lbcap");\n'
'  document.addEventListener("click",function(e){\n'
'    var t=e.target;\n'
'    if(t.tagName==="IMG"&&t.closest(".thumbs")){\n'
'      im.src=t.src; im.alt=t.alt; cap.textContent=t.dataset.cap;\n'
'      lb.classList.add("on"); document.body.style.overflow="hidden";\n'
'      document.getElementById("lbclose").focus(); }\n'
'  });\n'
'  function close(){ lb.classList.remove("on"); im.src=""; document.body.style.overflow=""; }\n'
'  document.getElementById("lbclose").addEventListener("click",close);\n'
'  lb.addEventListener("click",function(e){ if(e.target===lb||e.target.className==="frame") close(); });\n'
'  document.addEventListener("keydown",function(e){ if(e.key==="Escape"&&lb.classList.contains("on")) close(); });\n'
'})();\n</script>')
    return shell("836 Site Map, Then and Now",
                 "The surveyed site plan of 836 with clickable zones pairing the previous renovation against the finished house.",
                 1, "map/", body, MAP_CSS, script)

# ------------------------------------------------------------------ write

for sub, html in (("", build_gallery()), ("history", build_history()), ("map", build_map())):
    d = os.path.join(ROOT, sub) if sub else ROOT
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    print("%-10s %6.0f KB" % (sub or "(root)", os.path.getsize(os.path.join(d,"index.html"))/1024))
tot = sum(os.path.getsize(f) for f in glob.glob(os.path.join(IMG,"**","*.jpg"), recursive=True))
print("img/ %.1f MB" % (tot/1e6))
