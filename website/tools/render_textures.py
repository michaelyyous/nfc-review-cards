#!/usr/bin/env python3
"""Render the two card faces from build.card_svg() to PNG textures.

These are the artwork the WebGL card is wrapped in (assets/img/tex-*.png).
Same source as the CSS fallback card, so the two can never drift apart.
"""
import os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
sys.path.insert(0, SITE)
import build  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SCALE = 2   # 1080 x 1712

def render(dark, out):
    svg = build.card_svg(dark, 'width="%d" height="%d"' % (build.CARD_W * SCALE, build.CARD_H * SCALE))
    page = '<!doctype html><meta charset="utf-8"><style>html,body{margin:0}svg{display:block}</style>' + svg
    with tempfile.TemporaryDirectory() as tmp:
        html = os.path.join(tmp, "t.html")
        open(html, "w", encoding="utf-8").write(page)
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1",
                        "--window-size=%d,%d" % (build.CARD_W * SCALE, build.CARD_H * SCALE + 300),
                        "--screenshot=%s" % out, "file://" + html],
                       check=True, capture_output=True)
    from PIL import Image
    Image.open(out).convert("RGB").crop((0, 0, build.CARD_W * SCALE, build.CARD_H * SCALE)).save(out, optimize=True)
    print(out, os.path.getsize(out) // 1024, "KB")

if __name__ == "__main__":
    img = os.path.join(SITE, "assets", "img")
    render(False, os.path.join(img, "tex-front.png"))
    render(True,  os.path.join(img, "tex-back.png"))
