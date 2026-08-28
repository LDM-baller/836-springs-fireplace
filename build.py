# -*- coding: utf-8 -*-
import os, sys, glob, subprocess, json, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plates import PLATES, SECTIONS, HISTORY

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = "/Users/ldm/Library/CloudStorage/GoogleDrive-lbmann@gmail.com/My Drive/Programs/Property Manager/Documents/836 Reference/Photos"
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
        if "pixelWidth" in l: w=int(l.split(":")[1])
        if "pixelHeight" in l: h=int(l.split(":")[1])
    return w,h

D = {}
for n in sorted(PLATES):
    src = FILES[n]
    small, large = os.path.join(IMG,"%02d-800.jpg"%n), os.path.join(IMG,"%02d-1600.jpg"%n)
    if not os.path.exists(small): sips(src, small, 800, 60)
    if not os.path.exists(large): sips(src, large, 1600, 62)
    w,h = dims(large)
    D[n] = {"w":w, "h":h, "s":"img/%02d-800.jpg"%n, "l":"img/%02d-1600.jpg"%n}

# span: portrait pairs at 6, features at 12, else per section rhythm
SPAN = {1:12,2:12,3:12,4:7,5:5,6:6,7:6,8:12,9:6,10:6,11:12,12:7,13:5,14:12,
        15:6,16:6,17:12,18:6,19:6,20:6,21:6,22:12,23:6,24:6,25:12}

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def fig(n):
    t, cap = PLATES[n]; d = D[n]
    return f'''<figure class="plate" style="--span:{SPAN[n]}">
<button class="shot" type="button" data-n="{n}" aria-label="Enlarge plate {n:02d}, {esc(t)}">
<img src="{d['s']}" srcset="{d['s']} 800w, {d['l']} 1600w"
 sizes="(max-width:820px) 100vw, {int(SPAN[n]/12*100)}vw"
 width="{d['w']}" height="{d['h']}" alt="{esc(t)}" loading="lazy" decoding="async"></button>
<figcaption><span class="pno">{n:02d}</span><span class="ptext"><span class="ptitle">{t}</span><span class="pcap">{cap}</span></span></figcaption>
</figure>'''

def slug(name):
    return name.replace("&amp;","and").lower().replace(" ","-").replace("--","-").strip("-")

secs, nav = [], []
for name, blurb, ps in SECTIONS:
    s = slug(name); nav.append(f'<a href="#{s}">{name}</a>')
    secs.append(f'''<section class="sec" id="{s}">
<header class="sechead"><h2>{name}</h2><p>{blurb}</p></header>
<div class="grid">{"".join(fig(n) for n in ps)}</div></section>''')

hist = []
for kind, head, body in HISTORY:
    tag = ('<span class="tag tag-u">Owners&rsquo; account &middot; unverified</span>'
           if kind == "U" else '')
    hist.append(f'<article class="hitem{" hitem-u" if kind=="U" else ""}"><h3>{head}</h3>{tag}<p>{body}</p></article>')

META = json.dumps({str(n): {"t":PLATES[n][0], "c":PLATES[n][1], "l":D[n]["l"]} for n in PLATES})
ORDER = json.dumps([n for _,_,ps in SECTIONS for n in ps])
hero = D[1]

HTML = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>836 Springs Fireplace Road</title>
<meta name="description" content="Photographs of the finished house at 836 Springs Fireplace Road, Springs, East Hampton — on Accabonac Harbor, next to the Merrill Lake Sanctuary.">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="836 Springs Fireplace Road">
<meta property="og:description" content="Twenty-five photographs of the finished house on Accabonac Harbor.">
<meta property="og:type" content="website">
<meta name="theme-color" content="#EBEEF1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E1216" media="(prefers-color-scheme: dark)">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500&family=IBM+Plex+Mono:wght@400;500&family=Public+Sans:wght@300;400;500&display=swap">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='26' font-size='26'>&#127969;</text></svg>">
<style>
:root {{
  --ground:#EBEEF1; --surface:#F8F9FA; --ink:#12171C; --muted:#5E6873;
  --accent:#1D3C61; --rule:#CDD3D9;
  --shadow:0 1px 2px rgba(18,23,28,.06),0 12px 32px rgba(18,23,28,.09);
  --serif:"Bodoni Moda",Georgia,"Times New Roman",serif;
  --sans:"Public Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --ground:#0E1216; --surface:#161B21; --ink:#E4E8EC; --muted:#939DA8;
    --accent:#82A6CC; --rule:#28303A;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 14px 40px rgba(0,0,0,.5);
  }}
}}
*,*::before,*::after {{ box-sizing:border-box; }}
html {{ -webkit-text-size-adjust:100%; scroll-behavior:smooth; }}
body {{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:var(--sans); font-weight:300; line-height:1.6;
  -webkit-font-smoothing:antialiased; overflow-x:hidden;
}}
img {{ display:block; max-width:100%; height:auto; }}
:focus-visible {{ outline:2px solid var(--accent); outline-offset:3px; }}

.titleblock {{
  position:sticky; top:0; z-index:40;
  display:flex; flex-wrap:wrap; gap:.2rem 1.5rem; justify-content:space-between; align-items:baseline;
  padding:.55rem clamp(1rem,4vw,3rem);
  padding-left:max(1rem,env(safe-area-inset-left)); padding-right:max(1rem,env(safe-area-inset-right));
  background:var(--surface); border-bottom:1px solid var(--rule);
  font-family:var(--mono); font-size:.62rem; letter-spacing:.08em; text-transform:uppercase; color:var(--muted);
}}
.titleblock b {{ color:var(--ink); font-weight:500; }}

.hero {{ position:relative; }}
.hero img {{ width:100%; height:min(74vh,760px); object-fit:cover; }}
.hero .scrim {{
  position:absolute; inset:0; display:flex; flex-direction:column; justify-content:flex-end;
  padding:clamp(1.25rem,5vw,4rem);
  background:linear-gradient(to top,rgba(8,12,16,.88) 0%,rgba(8,12,16,.45) 36%,rgba(8,12,16,0) 70%);
  color:#F4F6F8;
}}
.hero .eyebrow {{ font-family:var(--mono); font-size:.62rem; letter-spacing:.2em; text-transform:uppercase; color:#B9C6D4; margin:0 0 .8rem; }}
.hero h1 {{ font-family:var(--serif); font-weight:400; font-size:clamp(2rem,7vw,5.4rem); line-height:1.03; letter-spacing:-.015em; margin:0; text-wrap:balance; color:#FFF; }}
.hero .sub {{ margin:.9rem 0 0; max-width:50ch; font-size:clamp(.88rem,1.6vw,1.05rem); color:#D3DCE5; line-height:1.55; }}

.secnav {{
  display:flex; gap:1.2rem; overflow-x:auto; -webkit-overflow-scrolling:touch;
  padding:.95rem clamp(1rem,4vw,3rem); border-bottom:1px solid var(--rule);
  font-family:var(--mono); font-size:.64rem; letter-spacing:.12em; text-transform:uppercase;
  scrollbar-width:none;
}}
.secnav::-webkit-scrollbar {{ display:none; }}
.secnav a {{ color:var(--muted); text-decoration:none; white-space:nowrap; padding:.4rem 0; border-bottom:1px solid transparent; }}
.secnav a:hover {{ color:var(--accent); border-bottom-color:var(--accent); }}

main {{ padding:0 clamp(1rem,4vw,3rem) 2rem; }}
.sec {{ padding:clamp(2.4rem,6vw,5rem) 0 0; scroll-margin-top:3.5rem; }}
.sechead {{ display:grid; gap:.3rem; padding-bottom:1.4rem; margin-bottom:1.7rem; border-bottom:1px solid var(--rule); }}
.sechead h2 {{ font-family:var(--serif); font-weight:400; font-size:clamp(1.5rem,3.4vw,2.5rem); margin:0; letter-spacing:-.01em; text-wrap:balance; }}
.sechead p {{ margin:0; color:var(--muted); font-size:.92rem; max-width:62ch; }}
@media (min-width:820px) {{
  .sechead {{ grid-template-columns:minmax(0,1fr) minmax(0,26rem); align-items:baseline; gap:2rem; }}
  .sechead p {{ text-align:right; }}
}}
.grid {{ display:grid; grid-template-columns:repeat(12,1fr); gap:clamp(1.5rem,3vw,2.6rem); align-items:start; }}
.plate {{ grid-column:span 12; margin:0; display:flex; flex-direction:column; gap:.7rem; }}
@media (min-width:820px) {{ .plate {{ grid-column:span var(--span); }} }}
.shot {{ display:block; width:100%; padding:0; border:0; background:none; cursor:zoom-in; box-shadow:var(--shadow); overflow:hidden; line-height:0; }}
.shot img {{ width:100%; transition:transform .5s cubic-bezier(.2,.7,.3,1); }}
@media (hover:hover) {{ .shot:hover img {{ transform:scale(1.018); }} }}
figcaption {{ display:flex; gap:.8rem; align-items:baseline; }}
.pno {{ font-family:var(--mono); font-size:.7rem; font-weight:500; color:var(--accent); flex:0 0 auto; padding-top:.15rem; font-variant-numeric:tabular-nums; }}
.ptext {{ display:flex; flex-direction:column; gap:.2rem; min-width:0; }}
.ptitle {{ font-family:var(--serif); font-size:1.02rem; line-height:1.3; }}
.pcap {{ font-size:.82rem; color:var(--muted); line-height:1.55; }}

.history {{ padding:clamp(2.4rem,6vw,5rem) 0 0; }}
.hgrid {{ display:grid; gap:2rem; }}
@media (min-width:760px) {{ .hgrid {{ grid-template-columns:repeat(2,minmax(0,1fr)); gap:2.4rem 3rem; }} }}
.hitem h3 {{ font-family:var(--serif); font-weight:400; font-size:1.2rem; margin:0 0 .5rem; }}
.hitem p {{ margin:0; font-size:.9rem; color:var(--muted); max-width:60ch; }}
.hitem-u {{ border-left:2px solid var(--accent); padding-left:1rem; }}
.tag {{ display:inline-block; font-family:var(--mono); font-size:.58rem; letter-spacing:.12em; text-transform:uppercase; color:var(--accent); border:1px solid var(--rule); padding:.16rem .45rem; margin-bottom:.55rem; }}

.colophon {{ margin-top:clamp(3rem,8vw,6rem); padding:clamp(1.5rem,4vw,3rem); background:var(--surface); border:1px solid var(--rule); }}
.colophon h2 {{ font-family:var(--mono); font-size:.64rem; letter-spacing:.18em; text-transform:uppercase; color:var(--accent); margin:0 0 1rem; font-weight:500; }}
.colophon p {{ margin:0 0 .8rem; font-size:.86rem; color:var(--muted); max-width:64ch; }}
.colophon p:last-child {{ margin-bottom:0; }}

.lb {{ position:fixed; inset:0; z-index:100; display:none; background:rgba(8,12,16,.97); flex-direction:column; gap:.75rem; padding:clamp(.5rem,2vw,2rem); padding-top:max(.5rem,env(safe-area-inset-top)); padding-bottom:max(.75rem,env(safe-area-inset-bottom)); touch-action:pan-y; }}
.lb.on {{ display:flex; }}
.lb .frame {{ flex:1; min-height:0; display:flex; align-items:center; justify-content:center; }}
.lb .frame img {{ max-width:100%; max-height:100%; object-fit:contain; }}
.lb .bar {{ display:flex; flex-wrap:wrap; gap:.3rem .9rem; align-items:baseline; justify-content:center; color:#D3DCE5; text-align:center; }}
.lb .bar .n {{ font-family:var(--mono); font-size:.66rem; color:#8FB0D2; }}
.lb .bar .t {{ font-family:var(--serif); font-size:1rem; color:#F4F6F8; }}
.lb .bar .c {{ font-size:.78rem; color:#96A4B3; width:100%; max-width:60ch; margin:0 auto; }}
.lb button {{ position:absolute; width:3rem; height:3rem; min-width:44px; min-height:44px; border:1px solid rgba(244,246,248,.3); background:rgba(8,12,16,.6); color:#F4F6F8; font-size:1.1rem; cursor:pointer; line-height:1; }}
.lb .prev, .lb .next {{ top:50%; transform:translateY(-50%); }}
.lb .prev {{ left:clamp(.4rem,2vw,1.5rem); }}
.lb .next {{ right:clamp(.4rem,2vw,1.5rem); }}
.lb .close {{ top:max(.5rem,env(safe-area-inset-top)); right:clamp(.4rem,2vw,1.5rem); width:2.75rem; height:2.75rem; }}
@media (max-width:700px) {{ .lb .prev, .lb .next {{ display:none; }} }}
@media (prefers-reduced-motion: reduce) {{
  html {{ scroll-behavior:auto; }}
  *,*::before,*::after {{ transition-duration:.01ms !important; animation-duration:.01ms !important; }}
}}
</style>
</head>
<body>

<div class="titleblock">
  <span><b>836 Springs Fireplace Rd.</b> &nbsp;Springs, East Hampton, NY</span>
  <span>25 plates &nbsp;&middot;&nbsp; Photographs <b>Tim Williams</b></span>
</div>

<header class="hero">
  <img src="{hero['s']}" srcset="{hero['s']} 800w, {hero['l']} 1600w" sizes="100vw"
       width="{hero['w']}" height="{hero['h']}" fetchpriority="high"
       alt="Aerial view of 836 Springs Fireplace Road, with Accabonac Harbor beyond">
  <div class="scrim">
    <p class="eyebrow">Springs &middot; East Hampton &middot; Accabonac Harbor</p>
    <h1>836 Springs Fireplace Road</h1>
    <p class="sub">Twenty-five photographs of the finished house — a salt-marsh property on Accabonac Harbor, next door to the Merrill Lake Sanctuary and a few hundred feet from the barn where Jackson Pollock made the drip paintings.</p>
  </div>
</header>

<nav class="secnav">{"".join(nav)}<a href="#history">History</a></nav>

<main>
{"".join(secs)}

<section class="history" id="history">
  <header class="sechead"><h2>Where this is</h2><p>The neighbourhood does a lot of the work here. Four notes, with the one that is hearsay marked as hearsay.</p></header>
  <div class="hgrid">{"".join(hist)}</div>
</section>

<section class="colophon">
  <h2>About this set</h2>
  <p>Photographs by Tim Williams. Sequenced as a walkthrough rather than in shooting order; each caption names the finishes legible in the frame. The images here are web-resolution exports — the full-resolution originals sit with the photographer.</p>
  <p>Private record for the owners of 836 Springs Fireplace Road. Not for republication.</p>
</section>
</main>

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Enlarged photograph">
  <div class="frame"><img id="lbimg" alt=""></div>
  <div class="bar"><span class="n" id="lbn"></span><span class="t" id="lbt"></span><span class="c" id="lbc"></span></div>
  <button class="prev" id="lbprev" aria-label="Previous">&#8592;</button>
  <button class="next" id="lbnext" aria-label="Next">&#8594;</button>
  <button class="close" id="lbclose" aria-label="Close">&#10005;</button>
</div>

<script>
(function(){{
  var META = {META}, ORDER = {ORDER};
  var lb=document.getElementById("lb"), im=document.getElementById("lbimg");
  var en=document.getElementById("lbn"), et=document.getElementById("lbt"), ec=document.getElementById("lbc");
  var i=-1, last=null;
  function pad(n){{ return (n<10?"0":"")+n; }}
  function show(k){{
    if(k<0) k=ORDER.length-1; if(k>=ORDER.length) k=0; i=k;
    var n=ORDER[k], m=META[String(n)];
    im.src=m.l; im.alt=m.t; en.textContent="Plate "+pad(n); et.textContent=m.t; ec.textContent=m.c;
  }}
  function open(n){{
    last=document.activeElement; lb.classList.add("on");
    show(ORDER.indexOf(n)); document.body.style.overflow="hidden";
    document.getElementById("lbclose").focus();
  }}
  function close(){{ lb.classList.remove("on"); im.src=""; document.body.style.overflow=""; if(last) last.focus(); }}
  document.querySelectorAll(".shot").forEach(function(b){{
    b.addEventListener("click", function(){{ open(parseInt(b.dataset.n,10)); }});
  }});
  document.getElementById("lbprev").addEventListener("click", function(){{ show(i-1); }});
  document.getElementById("lbnext").addEventListener("click", function(){{ show(i+1); }});
  document.getElementById("lbclose").addEventListener("click", close);
  lb.addEventListener("click", function(e){{ if(e.target===lb||e.target.className==="frame") close(); }});
  document.addEventListener("keydown", function(e){{
    if(!lb.classList.contains("on")) return;
    if(e.key==="Escape") close();
    else if(e.key==="ArrowLeft") show(i-1);
    else if(e.key==="ArrowRight") show(i+1);
  }});
  var x0=null, y0=null;
  lb.addEventListener("touchstart", function(e){{ x0=e.touches[0].clientX; y0=e.touches[0].clientY; }}, {{passive:true}});
  lb.addEventListener("touchend", function(e){{
    if(x0===null) return;
    var dx=e.changedTouches[0].clientX-x0, dy=e.changedTouches[0].clientY-y0;
    if(Math.abs(dx)>50 && Math.abs(dx)>Math.abs(dy)) show(dx<0 ? i+1 : i-1);
    else if(dy>90 && Math.abs(dy)>Math.abs(dx)) close();
    x0=y0=null;
  }}, {{passive:true}});
}})();
</script>
</body>
</html>
'''
open(os.path.join(ROOT,"index.html"),"w",encoding="utf-8").write(HTML)
tot = sum(os.path.getsize(f) for f in glob.glob(os.path.join(IMG,"*.jpg")))
print("index.html %.0f KB | %d images | img/ %.1f MB" %
      (os.path.getsize(os.path.join(ROOT,"index.html"))/1024, len(glob.glob(os.path.join(IMG,"*.jpg"))), tot/1e6))
