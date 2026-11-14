#!/usr/bin/env python3
"""Render the card faces to PNG straight from build.py's own SVG.

The images on the site must be the same artwork the 3D card shows, so this
pulls card_face() out of build.py rather than keeping a second copy. The
page is sized to the SVG's viewBox exactly, so nothing is cropped.
"""
import os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
sys.path.insert(0, SITE)
import build  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VB_W, VB_H = 342, 216          # the SVG's own viewBox
SCALE = 4                       # 1368 x 864 — plenty for a 2x retina card


def svg_only(markup):
    """card_face() returns the face div; we only want the <svg> inside it."""
    m = re.search(r"<svg.*?</svg>", markup, re.S)
    if not m:
        raise SystemExit("no <svg> found in card_face() output")
    return m.group(0)


def render(svg, out_path):
    # Width only. The face SVG carries width="100%%" height="100%%" of its own,
    # and pinning a CSS height as well makes Chrome resolve the two against
    # each other and render the card ~10%% short — the stars get guillotined.
    # Given just a width, the viewBox sets the height and the ratio is exact.
    page = """<!doctype html><meta charset="utf-8">
<style>
  html,body{margin:0;padding:0;background:transparent}
  svg{display:block;width:%dpx}
</style>
%s""" % (VB_W * SCALE, svg)

    with tempfile.TemporaryDirectory() as tmp:
        html = os.path.join(tmp, "card.html")
        with open(html, "w", encoding="utf-8") as fh:
            fh.write(page)
        subprocess.run([
            CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--default-background-color=00000000",
            # Taller than the card so nothing can be cut off; cropped after.
            "--window-size=%d,%d" % (VB_W * SCALE, VB_H * SCALE + 400),
            "--screenshot=%s" % out_path,
            "file://" + html,
        ], check=True, capture_output=True)

    crop_to_card(out_path)


def crop_to_card(path):
    """Trim the transparent filler the taller window leaves below the card."""
    from PIL import Image
    im = Image.open(path).convert("RGBA")
    box = im.getbbox()                      # bounds of everything non-transparent
    if box:
        im = im.crop(box)
    im.save(path)


def main():
    out_dir = os.path.join(SITE, "assets", "img")
    for dark, name in ((False, "card-front.png"), (True, "card-back.png")):
        dest = os.path.join(out_dir, name)
        render(svg_only(build.card_face(dark)), dest)
        from PIL import Image
        w, h = Image.open(dest).size
        print("%-16s %d x %d  (ratio %.4f, viewBox %.4f)"
              % (name, w, h, w / h, VB_W / VB_H))


if __name__ == "__main__":
    main()
