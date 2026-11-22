import subprocess, pathlib
D = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
STAR = '<svg viewBox="0 0 24 24" class="st"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
TAP = '<svg class="tap" viewBox="-4 -42 48 84" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linecap="round"><path d="M0 -12A12 12 0 0 1 0 12"/><path d="M0 -24A24 24 0 0 1 0 24" opacity=".7"/><path d="M0 -36A36 36 0 0 1 0 36" opacity=".4"/></svg>'

ADS = {
 "1-frisoer": dict(theme="tint", eyebrow="Til frisører og saloner",
   h="Glade kunder.<br>Få anmeldelser?",
   sub="Læg kortet ved kassen. Kunden holder telefonen mod det – og Google-anmeldelsen åbner.",
   badge="189 kr · intet abonnement", cards=["tex-back.png"]),
 "2-restaurant": dict(theme="dark", eyebrow="Til restauranter og caféer",
   h="Ét tap.<br>Én anmeldelse.",
   sub="Læg anmeldelseskortet med regningen. Gæsten tapper med telefonen – jeres Google-side åbner.",
   badge="Fra 189 kr · gratis levering", cards=["tex-front.png"]),
 "3-generel": dict(theme="light", eyebrow="Google-anmeldelser",
   h="Dine kunder er lige så glade.<br><span class='g'>De bliver bare ikke spurgt.</span>",
   sub="Anmeldelseskortet spørger for dig. Kunden tapper, Google åbner. Ingen app.",
   badge="Fra 189 kr", cards=["tex-back.png"], vs=True),
 "5-forhandler": dict(theme="dark", eyebrow="Sidehustle",
   h="Sælg dem videre<br>til butikkerne.",
   sub="Køb anmeldelseskort til forhandlerpris og sælg dem til frisører, caféer og butikker i dit område – til din egen pris.",
   badge="49 kr/stk ved 500 stk · ingen binding", cards=["tex-back.png","tex-front.png","tex-back.png","tex-front.png"], fan=True),
 "6-start-smaat": dict(theme="green", eyebrow="Vil du prøve at sælge dem?",
   h="Start med 10 kort.",
   sub=None, ticks=["129 kr/stk ved 10 stk","Vi koder kortene gratis til hver butik","Ingen binding, intet gebyr"],
   badge="Gå ind i 10 butikker. Se hvordan det går.", cards=["tex-front.png","tex-back.png"]),
 "4-pris": dict(theme="green", eyebrow="Anmeldelseskort",
   h="189 kr.<br>Og så er det det.",
   sub=None, ticks=["Intet abonnement","Ingen app – virker på iPhone og Android","Gratis levering til pakkeshop"],
   badge="Ned til 49 kr/stk ved 500 stk", cards=["tex-back.png","tex-front.png"]),
}

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{font-family:'Schibsted Grotesk',system-ui,sans-serif;display:flex;flex-direction:column;
 padding:%(pt)dpx 84px %(pb)dpx;position:relative;-webkit-font-smoothing:antialiased}
.light{background:#F6F7F6;color:#0E1110}.tint{background:#EAF6EF;color:#0E1110}
.dark{background:#0E1110;color:#fff}.green{background:#14724A;color:#fff}
.brand{display:flex;align-items:center;gap:18px;font-weight:700;font-size:34px;letter-spacing:-.01em}
.brand img{width:64px;height:64px;border-radius:16px}
.eyebrow{margin-top:%(gap1)dpx;font-size:30px;font-weight:600;text-transform:uppercase;letter-spacing:.08em;opacity:.65}
h1{margin-top:18px;font-size:%(hs)dpx;line-height:1.0;font-weight:800;letter-spacing:-.035em}
h1 .g{color:#14724A}
.sub{margin-top:30px;font-size:%(ss)dpx;line-height:1.3;max-width:880px;opacity:.82;font-weight:500}
.stage{flex:1 1 0;min-height:0;position:relative;display:flex;align-items:center;justify-content:center;margin-top:24px}
.cw{height:min(%(ch)dpx,90%%);position:relative}.cw.c0{transform:rotate(-7deg)}.cw.c1{transform:rotate(8deg);margin-left:-120px}
.card{height:100%%;display:block;border-radius:28px;box-shadow:0 40px 80px rgba(0,0,0,.28),0 8px 20px rgba(0,0,0,.15)}
.dark .card{box-shadow:0 40px 90px rgba(0,0,0,.6),0 0 0 2px rgba(255,255,255,.08)}
.tap{position:absolute;width:%(tw)dpx;left:calc(100%% + 24px);top:22%%;color:#14724A;transform:rotate(7deg)}
.dark .tap,.green .tap{color:#F5B301}
.badge{align-self:flex-start;margin-top:26px;background:#14724A;color:#fff;font-weight:700;font-size:%(bs)dpx;padding:20px 34px;border-radius:999px}
.dark .badge{background:#F5B301;color:#0E1110}.green .badge{background:#fff;color:#14724A}
.stars{display:flex;gap:6px}.st{width:%(sw)dpx;fill:#F5B301}
.vs{display:flex;gap:28px;margin-top:%(gap1)dpx}
.vs>div{flex:1;background:#fff;border-radius:28px;padding:28px 34px;box-shadow:0 2px 0 rgba(0,0,0,.04),0 0 0 1px rgba(14,17,16,.08)}
.vs .n{font-size:%(vn)dpx;font-weight:800;letter-spacing:-.04em;line-height:1}
.vs .l{font-size:28px;font-weight:600;opacity:.6;margin-top:10px}
.vs .you .n{color:#14724A}
.ticks{list-style:none;margin-top:34px;display:flex;flex-direction:column;gap:16px}
.ticks li{font-size:%(ss)dpx;font-weight:600;display:flex;gap:18px;align-items:center}
.ticks li:before{content:'✓';width:48px;height:48px;border-radius:50%%;background:rgba(255,255,255,.18);display:grid;place-items:center;font-size:28px;flex:none}
"""

def html(ad, fmt):
    story = fmt == "story"
    w, h = (1080, 1920) if story else (1080, 1350)
    p = dict(w=w, h=h, pt=280 if story else 72, pb=300 if story else 72,
             gap1=56 if story else 46, hs=104 if story else 96, ss=38 if story else 34,
             ch=(760 if story else 540) if not ad.get("vs") else (620 if story else 400),
             tw=150 if story else 120, bs=34 if story else 30, sw=40 if story else 34, vn=120 if story else 96)
    if ad.get("vs"): p["hs"] = 76 if story else 66
    if len(ad["cards"]) > 1: p["ch"] = 700 if story else 470
    fh = 640 if story else 470; ml = 230 if story else 170
    tap1 = TAP if len(ad["cards"]) == 1 else ""
    if ad.get("fan"):
        rots = [-18, -6, 6, 18]; ys = [40, 8, 8, 40]
        cards = "".join(f'<div class="cw" style="transform:translateY({ys[i]}px) rotate({rots[i]}deg);margin-left:{0 if i==0 else -ml}px;height:min({fh}px,88%)"><img class="card" src="{c}"></div>' for i, c in enumerate(ad["cards"]))
    else:
        cards = "".join(f'<div class="cw c{i}"><img class="card" src="{c}">{tap1}</div>' for i, c in enumerate(ad["cards"]))
    vs = ""
    if ad.get("vs"):
        vs = f'<div class="vs"><div><div class="stars">{STAR*5}</div><div class="n">300</div><div class="l">Konkurrenten</div></div><div class="you"><div class="stars">{STAR*5}</div><div class="n">12</div><div class="l">Dig</div></div></div>'
    sub = f'<p class="sub">{ad["sub"]}</p>' if ad.get("sub") else ""
    ticks = "<ul class='ticks'>" + "".join(f"<li>{t}</li>" for t in ad.get("ticks", [])) + "</ul>" if ad.get("ticks") else ""
    b = f'<div class="badge">{ad["badge"]}</div>'
    badge_top, badge_bot = (b, "") if story else ("", b)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;600;700;800&display=block" rel="stylesheet">
<style>{CSS % p}</style></head><body class="{ad['theme']}">
<div class="brand"><img src="logo-512.png">ReviewPartneren</div>
{vs}<div class="eyebrow">{ad['eyebrow'] if not ad.get('vs') else ''}</div>
<h1>{ad['h']}</h1>{sub}{ticks}
{badge_top}<div class="stage">{cards}</div>
{badge_bot}
</body></html>"""

out = D / "png"; out.mkdir(exist_ok=True)
import sys
only = sys.argv[1:]
for name, ad in ADS.items():
    if only and name not in only: continue
    for fmt in ("feed", "story"):
        f = D / f"{name}-{fmt}.html"; f.write_text(html(ad, fmt))
        w, h = (1080, 1920) if fmt == "story" else (1080, 1350)
        subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--disable-gpu",
            "--virtual-time-budget=4000", f"--window-size={w},{h+300}",
            f"--screenshot={out}/{name}-{fmt}.png", f.as_uri()],
            capture_output=True, timeout=60)
        from PIL import Image
        im = Image.open(out / f"{name}-{fmt}.png"); im.crop((0, 0, w, h)).save(out / f"{name}-{fmt}.png")
        print(name, fmt, Image.open(out / f"{name}-{fmt}.png").size)
