import subprocess, pathlib
from PIL import Image
D = pathlib.Path(__file__).parent
CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HEAD = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;600;700;800&display=block" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:'Schibsted Grotesk',sans-serif;-webkit-font-smoothing:antialiased;position:relative}
.brand{position:absolute;left:80px;top:72px;display:flex;align-items:center;gap:16px;font-weight:700;font-size:32px}
.brand img{width:58px;height:58px;border-radius:14px}
.card{position:absolute;border-radius:30px;box-shadow:0 50px 100px rgba(0,0,0,.35),0 10px 24px rgba(0,0,0,.2)}
STAR{fill:#F5B301}
</style></head>"""
STAR = '<svg viewBox="0 0 24 24" width="44" height="44"><path fill="#F5B301" d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
POSTS = {
"1-hero": HEAD + """<body style="background:radial-gradient(120% 90% at 50% 100%,#1B8A5B 0%,#14724A 45%,#0E5637 100%);color:#fff">
<div class="brand"><img src="logo-512.png">ReviewPartneren</div>
<h1 style="position:absolute;left:80px;right:80px;top:200px;font-size:112px;line-height:.98;font-weight:800;letter-spacing:-.04em">Ét tap.<br><span style="color:#FFD25A">Én Google-<br>anmeldelse.</span></h1>
<img class="card" src="tex-back.png" style="height:600px;left:170px;top:660px;transform:rotate(-12deg)">
<img class="card" src="tex-front.png" style="height:640px;left:470px;top:610px;transform:rotate(9deg)">
</body></html>""",
"2-saadan": HEAD + """<body style="background:#F6F7F6;color:#0E1110">
<div class="brand"><img src="logo-512.png">ReviewPartneren</div>
<div style="position:absolute;left:80px;top:180px;font-size:30px;font-weight:600;letter-spacing:.08em;color:#14724A">SÅDAN VIRKER DET</div>
<h1 style="position:absolute;left:80px;right:80px;top:230px;font-size:88px;line-height:1;font-weight:800;letter-spacing:-.035em">Fra glad kunde til Google-anmeldelse.</h1>
<div style="position:absolute;left:80px;top:560px;width:520px;display:flex;flex-direction:column;gap:46px">
 <div style="display:flex;gap:26px;align-items:flex-start"><div style="flex:none;width:76px;height:76px;border-radius:50%;background:#14724A;color:#fff;display:grid;place-items:center;font-size:40px;font-weight:800">1</div><div><b style="font-size:40px;display:block;letter-spacing:-.02em">Kunden tapper</b><span style="font-size:28px;color:#5A6260">Telefonen holdes mod kortet ved kassen</span></div></div>
 <div style="display:flex;gap:26px;align-items:flex-start"><div style="flex:none;width:76px;height:76px;border-radius:50%;background:#14724A;color:#fff;display:grid;place-items:center;font-size:40px;font-weight:800">2</div><div><b style="font-size:40px;display:block;letter-spacing:-.02em">Google åbner</b><span style="font-size:28px;color:#5A6260">Direkte på jeres anmeldelsesside – ingen app</span></div></div>
 <div style="display:flex;gap:26px;align-items:flex-start"><div style="flex:none;width:76px;height:76px;border-radius:50%;background:#14724A;color:#fff;display:grid;place-items:center;font-size:40px;font-weight:800">3</div><div><b style="font-size:40px;display:block;letter-spacing:-.02em">Stjernerne lander</b><span style="font-size:28px;color:#5A6260">Og næste kunde finder jer på Google</span></div></div>
</div>
<img class="card" src="tex-back.png" style="height:560px;left:650px;top:600px;transform:rotate(8deg)">
<div style="position:absolute;left:80px;bottom:80px;display:flex;gap:4px">""" + STAR*5 + """</div>
</body></html>""",
}
for name, html in POSTS.items():
    f = D / f"{name}.html"; f.write_text(html)
    out = D / f"{name}.png"
    subprocess.run([CH,"--headless=new","--hide-scrollbars","--disable-gpu","--virtual-time-budget=4000","--window-size=1080,1650",f"--screenshot={out}",f.as_uri()],capture_output=True,timeout=60)
    Image.open(out).crop((0,0,1080,1350)).convert("RGB").save(D/f"{name}.jpg",quality=93)
print("ok")
