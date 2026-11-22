import subprocess, pathlib
from PIL import Image
D = pathlib.Path(__file__).parent
ADS = [
 ("1 Frisør","1-frisoer","Dine kunder elsker deres nye hår. De glemmer bare at skrive det på Google. ✂️<br>Læg et anmeldelseskort ved kassen. Kunden holder telefonen mod det, og anmeldelsen åbner med det samme. Ingen app, intet abonnement.","Flere Google-anmeldelser til salonen","189 kr · intet abonnement","/brancher/frisoer"),
 ("2 Restaurant","2-restaurant","Gæsterne vælger restaurant på Google Maps – stående på gaden med telefonen i hånden. 🍽️<br>Læg et anmeldelseskort med regningen. Ét tap, og jeres Google-side er åben. Ingen app, intet abonnement.","Anmeldelser med regningen","Fra 189 kr · gratis levering","/brancher/restaurant-og-cafe"),
 ("3 Generel","3-generel","Konkurrenten har 300 anmeldelser. Du har 12. Og dine kunder er mindst lige så glade. ⭐<br>Forskellen er, hvem der beder om dem. Et anmeldelseskort gør det for dig: kunden holder telefonen mod kortet, og Google åbner.","Gør det nemt at give en anmeldelse","Virker på iPhone og Android","/anmeldelseskort"),
 ("4 Pris","4-pris","Ét kort. Intet abonnement. Ingen app. 189 kr – og så virker det i årevis. 💳<br>Kunden holder telefonen mod kortet ved kassen, og din Google-anmeldelsesside åbner med det samme. Gratis levering til pakkeshop.","Anmeldelseskort – 189 kr, intet abonnement","Gratis levering til pakkeshop","/anmeldelseskort"),
 ("5 Forhandler","5-forhandler","Frisører, caféer og butikker vil have flere Google-anmeldelser. Anmeldelseskortet klarer det med ét tap. 📲<br>Køb ind til forhandlerpris – 59 kr/stk ved 250, 49 kr ved 500 – og sælg videre til din egen pris. Ingen binding, intet gebyr.","Bliv forhandler af anmeldelseskort","18+ · ingen binding","/forhandler"),
 ("6 Start småt","6-start-smaat","Vil du prøve at sælge anmeldelseskort uden at købe et stort lager?<br>Start med 10 kort til 129 kr/stk, gå ind i butikkerne i dit område, og se hvordan det går. Vi koder kortene gratis til hver butik.","Start med 10 kort","129 kr/stk · gratis kodning","/anmeldelseskort?antal=10"),
]
posts = "".join(f'''<div class="post"><div class="tag">{n}</div><div class="hd"><img src="logo-512.png"><div><b>ReviewPartneren</b><span>Sponsoreret · 🌐</span></div></div>
<p class="txt">{t}</p><img class="cr" src="png/{f}-feed.png"><div class="lk"><div><span>REVIEWPARTNEREN.DK</span><b>{h}</b><i>{d}</i></div><button>Se detaljer</button></div><div class="url">→ reviewpartneren.dk{u}</div></div>''' for n,f,t,h,d,u in ADS)
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0}}body{{width:1800px;background:#F0F2F5;font-family:-apple-system,Helvetica,Arial,sans-serif;padding:40px;color:#050505}}
h1{{font-size:34px}}.sum{{margin:14px 0 30px;font-size:19px;line-height:1.6;color:#333;background:#fff;border-radius:12px;padding:18px 24px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}}.post{{background:#fff;border-radius:10px;box-shadow:0 1px 2px rgba(0,0,0,.15);overflow:hidden;position:relative}}
.tag{{position:absolute;top:10px;right:10px;background:#14724A;color:#fff;font-size:14px;font-weight:700;padding:4px 10px;border-radius:999px}}
.hd{{display:flex;gap:10px;align-items:center;padding:12px 14px}}.hd img{{width:40px;height:40px;border-radius:50%}}.hd b{{display:block;font-size:15px}}.hd span{{font-size:13px;color:#65676B}}
.txt{{padding:0 14px 12px;font-size:15px;line-height:1.35}}.cr{{width:100%;display:block}}
.lk{{display:flex;justify-content:space-between;align-items:center;background:#F0F2F5;padding:10px 14px;gap:10px}}.lk span{{display:block;font-size:12px;color:#65676B}}.lk b{{display:block;font-size:16px}}.lk i{{display:block;font-style:normal;font-size:13px;color:#65676B}}
.lk button{{background:#E4E6EB;border:0;border-radius:6px;padding:9px 14px;font-weight:700;font-size:14px;white-space:nowrap}}.url{{font-size:13px;color:#14724A;padding:8px 14px 12px}}
</style></head><body><h1>ReviewPartneren · Meta-kampagne · klar til start</h1>
<div class="sum"><b>Kampagne:</b> RP | Trafik | Test nov26 &nbsp;·&nbsp; <b>Mål:</b> flest besøg på landingssiden &nbsp;·&nbsp; <b>Målgruppe:</b> Danmark, 18–65+, bred &nbsp;·&nbsp; <b>Placeringer:</b> Facebook + Instagram (feed, stories, reels)<br>
<b>Budget:</b> 50 kr/dag (+25 % moms ≈ 62,50 kr) — Meta må max bruge 87,50 kr på én dag og 350 kr/uge (+moms) &nbsp;·&nbsp; <b>Afsender/betaler:</b> ReviewPartneren &nbsp;·&nbsp; <b>AI-forbedringer:</b> slået fra<br>
Hver annonce har også en 2. tekstvariant og eget 9:16-billede til stories/reels. Meta viser automatisk mest af de annoncer, der virker.</div>
<div class="grid">{posts}</div></body></html>'''
(D/"preview.html").write_text(html)
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([CH,"--headless=new","--hide-scrollbars","--disable-gpu","--virtual-time-budget=3000","--window-size=1800,4000",f"--screenshot={D}/oversigt-kampagne.png",(D/"preview.html").as_uri()],capture_output=True,timeout=60)
im=Image.open(D/"oversigt-kampagne.png").convert("RGB")
# crop bottom whitespace
px=im.load(); h=im.height
while h>100 and all(px[x,h-1]==(240,242,245) for x in range(0,im.width,40)): h-=1
im.crop((0,0,im.width,h+40)).save(D/"oversigt-kampagne.png")
print(im.size,h)
