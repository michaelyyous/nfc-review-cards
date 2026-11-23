#!/usr/bin/env python3
"""
Bygger hele sitet til statiske HTML-filer.

    python3 build.py

Alt indhold ligger i denne fil. Header, footer og navigation er defineret
ét sted og genbruges på alle sider.
Firmanavn, CVR og mail sættes i assets/app.js (BRAND-objektet).
"""

import pathlib, posixpath, re

ROOT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- pris
# Priser er INKL. moms (lovkrav ved salg til forbrugere).
TIERS = [
    (1, 189), (3, 169), (5, 155), (10, 129), (25, 109),
    (50, 95), (100, 79), (250, 59), (500, 49),
]
SHIP_HOME = 49          # hjemmelevering; pakkeshop er gratis
TIERS_JSON = "[" + ",".join('{"min":%d,"price":%d}' % t for t in TIERS) + "]"
P1 = TIERS[0][1]

def ex(p):
    v = p / 1.25
    return f"{v:.2f}".replace(".", ",").replace(",00", "")

def kr(n):
    return f"{n:,}".replace(",", ".")

# ---------------------------------------------------------------- nav
BRAND_NAME = "ReviewPartneren"   # bages ind i titler og synlig tekst ved build
BRAND_EMAIL = "support@reviewpartneren.dk"  # skal findes som rigtig postkasse
BRAND_CVR = ""                   # udfyldes naar CVR-nummeret er tildelt
ORDER = "anmeldelseskort.html"  # bestillingen ligger på produktsiden; /bestil viderestiller dertil
BASE_URL = "https://reviewpartneren.dk"

ORG_LD = {
    "@context": "https://schema.org",
    "@type": "OnlineStore",
    "name": "{brand}",
    "url": BASE_URL,
    "areaServed": "DK",
    "currenciesAccepted": "DKK",
    "paymentAccepted": "Dankort, Visa, Mastercard, MobilePay, Apple Pay, Google Pay, Klarna, Faktura",
    "logo": BASE_URL + "/assets/img/logo-512.png",
    "image": BASE_URL + "/assets/og.png",
    "email": "support@reviewpartneren.dk",
}

# Forsiden: WebSite giver Google sidenavnet "Reviewpartneren" i søgeresultatet,
# OnlineStore med logo kobler logoet på.
HOME_LD = {"@context": "https://schema.org", "@graph": [
    {"@type": "WebSite", "name": "{brand}", "alternateName": "reviewpartneren.dk", "url": BASE_URL + "/"},
    {k: v for k, v in ORG_LD.items() if k != "@context"},
]}

NAV = [
    ("anmeldelseskort.html", "Anmeldelseskort"),
    ("saadan-virker-det.html", "Sådan virker det"),
    ("brancher/index.html", "Brancher"),
    ("maengderabat.html", "Mængderabat"),
    ("faq.html", "FAQ"),
    ("forhandler.html", "Forhandler"),
]

# Logo: "tap-stjernen" — en anmeldelsesstjerne der sender NFC-bølger.
LOGO_STAR = "M13 10L15.12 15.09L20.61 15.53L16.42 19.11L17.7 24.47L13 21.6L8.3 24.47L9.58 19.11L5.39 15.53L10.88 15.09Z"
LOGO = """<svg class="brand__mark" viewBox="0 0 32 32" aria-hidden="true">
<rect width="32" height="32" rx="8" fill="#14724A"/>
<path d="%s" fill="#fff"/>
<path d="M14.91 7.17A11 11 0 0 1 23.83 16.09" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M16.2 3.9A14.3 14.3 0 0 1 27.1 15.2" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" opacity=".55"/>
</svg>""" % LOGO_STAR

ANNOUNCE = """
<div class="announce">
  <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 3h15v13H1zM16 8h4l3 3v5h-7z"/>
    <circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>Fri fragt til pakkeshop</span>
  <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/>
    <path d="M12 7v5l3 2"/></svg>Sendes 1–2 hverdage fra Danmark</span>
  <span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>Intet abonnement</span>
</div>"""

def star():
    return ('<svg width="15" height="15" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">'
            '<path d="M10 1.6l2.47 5.23 5.63.83-4.08 4.08.97 5.75L10 14.78l-4.99 2.71.97-5.75L1.9 7.66l5.63-.83L10 1.6z"/></svg>')

GOOGLE_G = """<svg viewBox="0 0 256 262" width="20" height="20" aria-hidden="true">
<path fill="#4285F4" d="M255.878 133.451c0-10.734-.871-18.567-2.756-26.69H130.55v48.448h71.947c-1.45 12.04-9.283 30.172-26.69 42.356l-.244 1.622 38.755 30.023 2.685.268c24.659-22.774 38.875-56.282 38.875-96.027"/>
<path fill="#34A853" d="M130.55 261.1c35.248 0 64.839-11.605 86.453-31.622l-41.196-31.913c-11.024 7.688-25.82 13.055-45.257 13.055-34.523 0-63.824-22.773-74.269-54.25l-1.531.13-40.298 31.187-.527 1.465C35.393 231.798 79.49 261.1 130.55 261.1"/>
<path fill="#FBBC05" d="M56.281 156.37c-2.756-8.123-4.351-16.827-4.351-25.82 0-8.994 1.595-17.697 4.206-25.82l-.073-1.73L15.26 71.312l-1.335.635C5.077 89.644 0 109.517 0 130.55s5.077 40.905 13.925 58.602l42.356-32.782"/>
<path fill="#EA4335" d="M130.55 50.479c24.514 0 41.05 10.589 50.479 19.438l36.844-35.974C195.245 12.91 165.798 0 130.55 0 79.49 0 35.393 29.301 13.925 71.947l42.211 32.783c10.59-31.477 39.891-54.251 74.414-54.251"/></svg>"""

_G_PATHS = """      <path fill="#4285F4" d="M255.878 133.451c0-10.734-.871-18.567-2.756-26.69H130.55v48.448h71.947c-1.45 12.04-9.283 30.172-26.69 42.356l-.244 1.622 38.755 30.023 2.685.268c24.659-22.774 38.875-56.282 38.875-96.027"/>
      <path fill="#34A853" d="M130.55 261.1c35.248 0 64.839-11.605 86.453-31.622l-41.196-31.913c-11.024 7.688-25.82 13.055-45.257 13.055-34.523 0-63.824-22.773-74.269-54.25l-1.531.13-40.298 31.187-.527 1.465C35.393 231.798 79.49 261.1 130.55 261.1"/>
      <path fill="#FBBC05" d="M56.281 156.37c-2.756-8.123-4.351-16.827-4.351-25.82 0-8.994 1.595-17.697 4.206-25.82l-.073-1.73L15.26 71.312l-1.335.635C5.077 89.644 0 109.517 0 130.55s5.077 40.905 13.925 58.602l42.356-32.782"/>
      <path fill="#EA4335" d="M130.55 50.479c24.514 0 41.05 10.589 50.479 19.438l36.844-35.974C195.245 12.91 165.798 0 130.55 0 79.49 0 35.393 29.301 13.925 71.947l42.211 32.783c10.59-31.477 39.891-54.251 74.414-54.251"/>"""

# Kortet er STÅENDE, 54 × 85,6 mm, tegnet efter leverandørens produktfoto:
# "Review Us On" / "Google" øverst, G'et i midten, NFC-hånden og fem stjerner nederst.
# viewBox er 10 enheder pr. mm, så målene kan læses direkte.
CARD_W, CARD_H = 540, 856

_STAR = "M0,-26 L6.1,-8.4 L24.7,-8.0 L9.9,3.2 L15.3,21.0 L0,10.4 L-15.3,21.0 L-9.9,3.2 L-24.7,-8.0 L-6.1,-8.4 Z"
_STARS_CARD = "".join(
    '<path transform="translate(%.1f,0)" d="%s"/>' % (122 + i * 74, _STAR) for i in range(5)
)

def _nfc_icon(ink, bg):
    """Hånd der holder en telefon, bølger og 'NFC' — som på det trykte kort."""
    return """<g transform="translate(222,622)">
      <g fill="none" stroke="%(ink)s" stroke-width="5" stroke-linecap="round">
        <path d="M14,30 A9,9 0 0 1 23,21"/>
        <path d="M6,31 A17,17 0 0 1 24,13"/>
        <path d="M-2,32 A25,25 0 0 1 25,5"/>
      </g>
      <text x="36" y="27" fill="%(ink)s" font-family="'Avenir Next','Avenir',system-ui,sans-serif"
            font-size="27" font-weight="800" letter-spacing=".5">NFC</text>
      <g transform="rotate(-14 50 76)">
        <rect x="31" y="40" width="38" height="70" rx="8" fill="%(bg)s" stroke="%(ink)s" stroke-width="6"/>
        <rect x="44" y="45" width="12" height="3" rx="1.5" fill="%(ink)s"/>
      </g>
      <path fill="%(ink)s" d="M58,122 C55,110 56,99 63,90 L71,74 C74,67 83,68 83,77 L81,92 C88,99 91,109 88,124 Z"/>
      <rect x="21" y="86" width="20" height="9" rx="4.5" fill="%(ink)s" transform="rotate(-14 31 90)"/>
      <rect x="23" y="98" width="20" height="9" rx="4.5" fill="%(ink)s" transform="rotate(-14 33 102)"/>
      <rect x="26" y="110" width="19" height="9" rx="4.5" fill="%(ink)s" transform="rotate(-14 35 114)"/>
    </g>""" % {"ink": ink, "bg": bg}

def card_svg(dark, extra_attrs=""):
    """Én kortside som ren SVG. dark=True er den sorte side, False den hvide."""
    bg  = "#141414" if dark else "#F7F7F4"
    ink = "#FFFFFF" if dark else "#1C1C1C"
    disc = '<circle cx="270" cy="428" r="178" fill="#FFFFFF"/>' if dark else ""
    label = "sort side" if dark else "hvid side"
    return """<svg viewBox="0 0 %d %d" %s role="img" aria-label="Anmeldelseskort, %s">
    <rect width="%d" height="%d" fill="%s"/>
    <text x="270" y="80" text-anchor="middle" fill="%s"
          font-family="'Avenir Next','Avenir',system-ui,sans-serif"
          font-size="50" font-weight="500" letter-spacing="-.3">Review Us On</text>
    <text x="270" y="192" text-anchor="middle" fill="%s"
          font-family="'Futura','Avenir Next',system-ui,sans-serif"
          font-size="96" font-weight="500" letter-spacing="-1.5">Google</text>
    %s
    <g transform="translate(270,428) scale(1.05) translate(-128,-130.5)">
%s
    </g>
    %s
    <g fill="#F4B521" transform="translate(0,786)">%s</g>
  </svg>""" % (CARD_W, CARD_H, extra_attrs, label, CARD_W, CARD_H, bg, ink, ink,
               disc, _G_PATHS, _nfc_icon(ink, bg), _STARS_CARD)

def card_face(dark):
    """Kortsiden som den sidder i CSS-3D-kortet (fallback når WebGL ikke kører)."""
    return """<div class="card3d__face card3d__face--%s">
  %s
  <div class="card3d__glare"></div>
</div>""" % ("back" if dark else "front", card_svg(dark, 'width="100%" height="100%"'))


CARD_3D = """<div class="stage">
  <div class="card3d-wrap" data-card3d>
    <div class="card3d">
      %s
      %s
      <span class="card3d__edge card3d__edge--t"></span>
      <span class="card3d__edge card3d__edge--b"></span>
      <span class="card3d__edge card3d__edge--l"></span>
      <span class="card3d__edge card3d__edge--r"></span>
    </div>
    <div class="card3d__shadow"></div>
  </div>
  <p class="card3d__hint" data-card3d-hint>
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true">
      <path d="M8 7L4 12l4 5M16 7l4 5-4 5"/></svg>
    Træk for at dreje kortet
  </p>
</div>""" % (card_face(False), card_face(True))


def head(title, desc, depth=0, canon="", jsonld="{}"):
    up = "../" * depth
    return """<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#14724A">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:locale" content="da_DK">
<meta property="og:image" content="%s/assets/og.png?v=3">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="%sassets/styles.css?v=27">
<link rel="icon" href="%sfavicon.ico" sizes="48x48">
<link rel="icon" href="%sfavicon-192.png" type="image/png" sizes="192x192">
<link rel="icon" href="%sfavicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="%sassets/img/apple-touch-icon.png">
<link rel="canonical" href="%s">
<script type="application/ld+json">%s</script>
</head>
<body>
<a class="skip" href="#indhold">Spring til indhold</a>""" % (title, desc, title, desc, BASE_URL, up, up, up, up, up, canon, jsonld)


def topbar(current, depth=0, onhero=False):
    up = "../" * depth
    cur = ' aria-current="page"'
    links = "".join(
        '<a href="%s%s"%s>%s</a>' % (up, href, cur if href == current or (href.endswith("/index.html") and current.startswith(href[:-10])) else "", label)
        for href, label in NAV
    )
    variant = " topbar--onhero" if onhero else ""
    return """
<header class="topbar%s">
  <div class="topbar__in">""" % variant + """
    <a class="brand" href="%sindex.html">%s<span data-brand>Firmanavn</span></a>
    <nav class="nav" aria-label="Hovedmenu">%s</nav>
    <div class="topbar__cta">
      <a class="btn btn--ghost btn--sm" href="%skontakt.html">Kontakt</a>
      <a class="btn btn--sm" href="/anmeldelseskort#bestil">Bestil</a>
      <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="indhold">""" % (up, LOGO, links, up)


def footer(depth=0):
    up = "../" * depth
    return """</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot__grid">
      <div>
        <a class="brand" href="%sindex.html" style="margin-bottom:var(--s-4)">%s<span data-brand>Firmanavn</span></a>
        <p class="small" style="max-width:24rem">Anmeldelseskort til butikker, saloner og alle der vil sælge dem videre. Ét tryk, og kunden står på din Google-anmeldelsesside. Intet abonnement.</p>
      </div>
      <div>
        <h4>Produkt</h4>
        <ul>
          <li><a href="%sanmeldelseskort.html">Anmeldelseskort</a></li>
          <li><a href="%smaengderabat.html">Mængderabat</a></li>
          <li><a href="%sforhandler.html">Bliv forhandler</a></li>
          <li><a href="/brancher">Brancher</a></li>
          <li><a href="%ssaadan-virker-det.html">Sådan virker det</a></li>
        </ul>
      </div>
      <div>
        <h4>Hjælp</h4>
        <ul>
          <li><a href="%ssaet-det-op.html">Sæt det op selv</a></li>
          <li><a href="%sfaq.html">Spørgsmål og svar</a></li>
          <li><a href="/guides/flere-google-anmeldelser">Få flere anmeldelser</a></li>
          <li><a href="%sguides/index.html">Guides</a></li>
          <li><a href="%skontakt.html">Kontakt support</a></li>
        </ul>
      </div>
      <div>
        <h4>Virksomhed</h4>
        <ul>
          <li><a href="%som-os.html">Om os</a></li>
          <li><a href="%shandelsbetingelser.html">Handelsbetingelser</a></li>
          <li><a href="%sfortrydelsesret.html">Fortrydelsesret</a></li>
          <li><a href="%sprivatlivspolitik.html">Privatlivspolitik</a></li>
          <li><a href="%scookiepolitik.html">Cookiepolitik</a></li>
          <li><a href="#" data-consent-reopen>Cookieindstillinger</a></li>
        </ul>
      </div>
    </div>
    %s
    <div class="foot__legal">
      <p class="tiny">© <span data-year>2026</span> <span data-brand>Firmanavn</span> · CVR <span data-cvr>—</span></p>
      <p class="tiny">Priser inkl. moms · Fri fragt til pakkeshop · 14 dages fortrydelsesret · 2 års reklamationsret</p>
    </div>
  </div>
</footer>
<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script>
<script defer src="/_vercel/insights/script.js"></script>
<script src="%sassets/app.js?v=20"></script>
</body>
</html>""" % ((up, LOGO) + (up,) * 13 + (PAYMENTS, up))


PAYMENTS = """
<div class="pay" aria-label="Betalingsmuligheder">
  <span>Dankort</span><span>Visa</span><span>Mastercard</span><span>MobilePay</span>
  <span>Apple&nbsp;Pay</span><span>Google&nbsp;Pay</span><span>Klarna</span><span>Faktura</span>
</div>"""

PAGES = []

def clean_path(path):
    """'guides/index.html' -> '/guides', 'faq.html' -> '/faq', 'index.html' -> '/'."""
    p = "/" + path
    p = p[:-len("index.html")] if p.endswith("index.html") else p[:-5] if p.endswith(".html") else p
    return p.rstrip("/") or "/"

def _clean_href(m, page_path):
    href = m.group(1)
    if re.match(r"^(?:[a-z][a-z0-9+.-]*:|//|#|/)", href):
        return m.group(0)
    target, _, frag = href.partition("#")
    if not target.endswith(".html"):
        return m.group(0)
    full = posixpath.normpath(posixpath.join(posixpath.dirname(page_path), target))
    return 'href="%s%s"' % (clean_path(full), "#" + frag if frag else "")

def breadcrumbs(items):
    """items: [(label, path)], last item is the current page. Returns (html, json-ld)."""
    parts = []
    for i, (label, path) in enumerate(items):
        if i: parts.append('<span aria-hidden="true">/</span>')
        if i < len(items) - 1:
            parts.append('<a href="%s">%s</a>' % (clean_path(path), label))
        else:
            parts.append('<span aria-current="page">%s</span>' % label)
    ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": label, "item": BASE_URL + clean_path(path)}
        for i, (label, path) in enumerate(items)]}
    return '<nav class="crumbs" aria-label="Brødkrummer">%s</nav>' % "".join(parts), ld

def page(path, title, desc, body, current=None, depth=0, hero=None, jsonld=None):
    """hero: markup for a contained hero block that the nav sits on top of.
    When given, the nav renders transparent over it and <main> opens after."""
    if hero:
        chrome = (ANNOUNCE + '<div class="heroblock">'
                  + topbar(current or path, depth, onhero=True).replace("<main>", "")
                  + hero + "</div><main>")
    else:
        chrome = topbar(current or path, depth)
    import json as _json
    canon = BASE_URL + clean_path(path)
    ld = _json.dumps(jsonld or ORG_LD, ensure_ascii=False, separators=(",", ":"))
    html = head(title, desc, depth, canon, ld) + chrome + body + footer(depth)
    # Bag navnet ind, saa titler og synlig tekst er korrekte uden JavaScript
    html = html.replace("{brand}", BRAND_NAME)
    # Interne links peger direkte på de rene adresser (/anmeldelseskort), så
    # hverken Google eller kunden skal igennem Vercels .html-omdirigering.
    html = re.sub(r'href="([^"]*)"', lambda m: _clean_href(m, path), html)
    html = html.replace("<span data-brand>Firmanavn</span>", "<span data-brand>%s</span>" % BRAND_NAME)
    # Kontaktoplysninger er lovpligtige, saa de skal staa i kilden og ikke kun
    # blive sat af JavaScript — ellers ser crawlere og alt uden JS en pladsholder.
    html = html.replace('<a data-email href="#"', '<a data-email href="mailto:%s"' % BRAND_EMAIL)
    html = html.replace(">support@\u2026</a>", ">%s</a>" % BRAND_EMAIL)
    if BRAND_CVR:
        html = html.replace("<span data-cvr>\u2014</span>", "<span data-cvr>%s</span>" % BRAND_CVR)
    else:
        # Indtil CVR er tildelt: vis intet i stedet for "CVR \u2014", som ser utrov\u00e6rdigt ud.
        for pat in (' \u00b7 CVR <span data-cvr>\u2014</span>', '<br>CVR <span data-cvr>\u2014</span>',
                    ', CVR <span data-cvr>\u2014</span>', '<p class="small">CVR <span data-cvr>\u2014</span></p>'):
            html = html.replace(pat, "")
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    PAGES.append(path)


def acc(items):
    out = ['<div class="acc">']
    for q, a in items:
        paras = "".join("<p>%s</p>" % x for x in a)
        out.append("""<div class="acc__item">
  <button class="acc__btn" aria-expanded="false"><span>%s</span><span class="acc__sign"></span></button>
  <div class="acc__panel"><div>%s</div></div>
</div>""" % (q, paras))
    out.append("</div>")
    return "".join(out)


def tier_rows(featured=100, pick=False):
    rows = []
    for q, p in TIERS:
        save = round((1 - p / P1) * 100)
        badge = '<span class="tier__save">−%d%%</span>' % save if save > 0 else "<span></span>"
        feat = " data-featured" if q == featured else ""
        label = "%d stk." % q if q > 1 else "1 stk."
        if pick:
            rows.append("""<button type="button" class="tier tier--pick%s" data-qty-set="%d" aria-label="%s til %d kr pr. stk.">
  <span class="tier__q"><span class="tier__dot" aria-hidden="true"></span>%s</span>%s
  <span class="tier__p num">%d kr <small>/stk.</small></span>
</button>""" % (" is-on" if q == 1 else "", q, label, p, label, badge, p))
            continue
        rows.append("""<div class="tier"%s>
  <span class="tier__q">%s</span>%s
  <span class="tier__p num">%d kr <small>/stk.</small></span>
</div>""" % (feat, label, badge, p))
    return '<div class="tiers%s" %s>' % (" tiers--pick" if pick else "", 'role="group" aria-label="Vælg antal"' if pick else "") + "".join(rows) + "</div>"


def hero(eyebrow, h1, lede, buttons="", note="", extra=""):
    btns = '<div class="row">%s</div>' % buttons if buttons else ""
    nt = '<p class="tiny">%s</p>' % note if note else ""
    eb = '<span class="eyebrow">%s</span>' % eyebrow if eyebrow else ""
    return """
<section class="section" style="padding-bottom:clamp(var(--s-10),5vw,var(--s-16))">
  <div class="wrap">
    <div class="stack-6" style="max-width:44rem" data-reveal>
      %s<h1 class="display">%s</h1>
      <p class="lede">%s</p>
      %s%s
    </div>
    %s
  </div>
</section>""" % (eb, h1, lede, btns, nt, extra)


# ================================================================ FORSIDE
ARROW = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')
CHECK = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M20 6L9 17l-5-5"/></svg>')

ICO_STAR = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
            '<path d="M12 2l2.9 6.2 6.6.8-4.8 4.8 1.2 6.7L12 17.3 6.1 20.5l1.2-6.7L2.5 9l6.6-.8L12 2z"/></svg>')
ICO_TAG = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M20.6 13.4l-7.2 7.2a2 2 0 01-2.8 0L3 13V3h10l7.6 7.6a2 2 0 010 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/></svg>')
ICO_TRUCK = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M1 3h15v13H1zM16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>')
ICO_NO = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
          'aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/></svg>')


# Badge under prisen i hero'en. Teksten siger det sande: teknologien er
# gennemprøvet. Den siger IKKE noget om hvor mange anmeldelser vores egne
# kort har samlet ind — det tal findes ikke endnu og ville kraeve
# dokumentation efter markedsfoeringslovens § 13.
HERO_BADGE = """
        <div class="proof">
          %s
          <span class="proof__txt"><span class="stars" aria-hidden="true">%s</span>
            <span><strong>10.000+ Google-anmeldelser</strong> er allerede givet via præcis det samme kort hos virksomheder verden over</span></span>
        </div>""" % (GOOGLE_G, star() * 5)



home_hero = """
  <div class="heroblock__in">
    <div class="heroblock__grid">
      <div class="stack-6" data-reveal>
        <div class="hero__eyebrow">
          <span class="stars">%s</span>
        </div>
        <h1 class="display"><span class="display__kicker">Anmeldelseskort til butikker, saloner og videresalg</span>Kunden skriver anmeldelsen,<br>før de går ud ad døren.</h1>
        <p class="lede">Læg kortet på disken. Kunden holder telefonen mod det, og jeres anmeldelsesside åbner af sig selv. Ingen app, intet abonnement, ingen løbende udgift.</p>
        <div class="hero__buy">
          <span class="hero__price"><small>Fra</small> <strong>%d kr.</strong></span>
          <a class="btn btn--lg" href="/anmeldelseskort#bestil">Se kort og priser %s</a>
        </div>
        %s
        <div class="ticks">
          <span>%s Sendes på 1–2 hverdage</span>
          <span>%s Intet abonnement</span>
          <span>%s iPhone og Android</span>
        </div>
        <p class="small">Køber du flere? <a href="maengderabat.html" style="text-decoration:underline">Mængderabat ned til %d kr. pr. kort →</a></p>
      </div>
      <div data-reveal="80">
        <div class="hero__media">
          <img src="assets/img/card-hero.webp?v=5" width="1600" height="1280" alt="Anmeldelseskort spredt på et bord: den hvide side med Google-logo, NFC-symbol og fem stjerner øverst, sorte kort under og bagved" fetchpriority="high">
        </div>
      </div>
    </div>
  </div>""" % (star() * 5, P1, ARROW, HERO_BADGE, CHECK, CHECK, CHECK, TIERS[-1][1])

# ---------------------------------------------------------------- kundelogoer
# Udfyld KUN med virksomheder der faktisk er kunder OG har sagt ja til at blive
# nævnt. Så længe listen er tom, viser sitet en tydelig pladsholder i stedet —
# den må ikke gå live med navne der ikke er bekræftet.
#
# Når du har dem:  CUSTOMERS = ["Roots Kitchen", "CleanClub", ...]
CUSTOMERS = []

def marquee():
    if not CUSTOMERS:
        return """
<section class="section--tight">
  <div class="wrap">
    <div class="stack" style="align-items:center;text-align:center" data-reveal>
      <span class="eyebrow">Virksomheder der bruger kortet</span>
      <div class="marquee--empty" style="width:100%%;margin-top:var(--s-4)">
        <p><strong>Pladsholder — må ikke gå live som den er.</strong><br>
        Sektionen er bygget og animeret. Tilføj navnene i <code>CUSTOMERS</code> i <code>build.py</code>,
        når virksomhederne faktisk er kunder <em>og</em> har sagt ja til at blive nævnt.
        Navne på firmaer der ikke er kunder er vildledende markedsføring efter markedsføringslovens § 5.</p>
      </div>
    </div>
  </div>
</section>"""
    track = '<div class="marquee__track">' + "".join(
        '<span class="marquee__item">%s</span>' % c for c in CUSTOMERS) + '</div>'
    return """
<section class="section--tight">
  <div class="wrap stack" style="align-items:center" data-reveal>
    <span class="eyebrow">Virksomheder der bruger kortet</span>
  </div>
  <div class="marquee" aria-label="Virksomheder der bruger kortet">
    <div class="marquee__row">%s%s</div>
  </div>
</section>""" % (track, track)

# Logobjaelken, kundecitaterne og tal-sektionen er taget af forsiden 2026-11-14.
# De to foerste stod med synlige pladsholdere og kan ikke vaere paa en side vi
# koeber trafik til; den tredje gentog bare fordels-striben ovenfor. Koden bliver
# staaende faerdig, saa logoer og citater kan saettes ind den dag der er rigtige
# kunder at vise — saet dem tilbage i page("index.html", ...) nedenfor.
home_logos = marquee()


home_paths = """
<section class="section--tight">
  <div class="wrap">
    <div class="grid grid-2">
      <div class="card" data-reveal>
        <span class="eyebrow">Til din egen forretning</span>
        <h3 style="margin-top:var(--s-3)">Kort til butikken</h3>
        <p class="small" style="margin-top:var(--s-2)">Ét ved kassen, ét ved bordet. Vi programmerer dem til jeres Google-side inden afsendelse, så I bare lægger dem frem.</p>
        <p class="small" style="margin-top:var(--s-5);font-weight:600"><a href="/anmeldelseskort#bestil">Bestil fra %d kr %s</a></p>
      </div>
      <div class="card" data-reveal="80">
        <span class="eyebrow">Til videresalg</span>
        <h3 style="margin-top:var(--s-3)">Køb ind og sælg videre</h3>
        <p class="small" style="margin-top:var(--s-2)">Du behøver ikke et CVR for at bestille. Køber du flere, falder prisen af sig selv — ned til %d kr pr. kort. Fra 250 stk. får du fast indkøbspris og faktura.</p>
        <p class="small" style="margin-top:var(--s-5);font-weight:600"><a href="forhandler.html">Se forhandlervilkår %s</a></p>
      </div>
    </div>
  </div>
</section>""" % (P1, ARROW, TIERS[-1][1], ARROW)


home_benefits = """
<section class="benefits">
  <div class="benefits__in">
    <div class="benefit"><div class="benefit__ico">%s</div>
      <div><h3>Stjernerne står klar</h3><p>Kortet åbner skrivefeltet — ikke bare din Google-profil.</p></div></div>
    <div class="benefit"><div class="benefit__ico">%s</div>
      <div><h3>ned til %d kr</h3><p>pr. kort. Rabatten stiger af sig selv med antallet.</p></div></div>
    <div class="benefit"><div class="benefit__ico">%s</div>
      <div><h3>1–2 hverdage</h3><p>til vi sender. Derefter 1–3 dage med GLS, DAO eller PostNord.</p></div></div>
    <div class="benefit"><div class="benefit__ico">%s</div>
      <div><h3>0 kr</h3><p>i abonnement. Du køber kortet, og så er det dit.</p></div></div>
  </div>
</section>""" % (ICO_STAR, ICO_TAG, TIERS[-1][1], ICO_TRUCK, ICO_NO)

STATS = [
    ("0", "kr/md", "Intet abonnement",
     "Du køber kortet én gang. Der er ingen licens og intet der fornyes."),
    ("10", "år", "Så længe holder chippen",
     "Chipproducenten angiver 10 års levetid for linket på chippen."),
    ("1–3", "dage", "Fra bestilling til disken",
     "Vi sender 1–2 hverdage efter ordre, med GLS eller PostNord."),
]


home_stats = """
<section class="section">
  <div class="wrap stack-8">
    <div class="stack" data-reveal>
      <span class="eyebrow">Tallene bag</span>
      <h2 class="h2">Hvad du faktisk køber</h2>
    </div>
    <div class="grid grid-3">""" + "".join("""
      <div class="stat" data-reveal="%d">
        <div class="stat__n">%s<small>%s</small></div>
        <p class="stat__label">%s</p>
        <p class="stat__note">%s</p>
      </div>""" % (i * 60, n, unit, label, note)
      for i, (n, unit, label, note) in enumerate(STATS)) + """
    </div>
    <p class="tiny" data-reveal="180" style="max-width:44rem">Der står ikke noget tal for hvor mange flere anmeldelser du får. Det afhænger af hvor mange kunder du har, og hvor kortet ligger — og vi har ingen data der kan bære det løfte.</p>
    <div data-reveal="200"><a class="btn btn--lg" href="anmeldelseskort.html">Se kortet — fra %d kr %s</a></div>
  </div>
</section>""" % (P1, ARROW)

home_why = """
<section class="section section--sunk">
  <div class="wrap stack-8">
    <div class="stack" data-reveal>
      <span class="eyebrow">Hvorfor det virker</span>
      <h2 class="h2">Problemet er ikke viljen.<br>Det er de tolv sekunder.</h2>
      <p class="lede" style="max-width:40rem">En kunde der lige har haft en god oplevelse vil gerne sige det. Men i det øjeblik hun skal låse telefonen op, åbne Google, søge efter dit firma og finde den rigtige knap, er øjeblikket væk.</p>
      <p class="tiny" style="max-width:40rem">Vi skriver ikke hvor mange flere anmeldelser du får. Det afhænger af hvor mange kunder du har, og hvor kortet ligger — og vi har ingen data der kan bære det løfte.</p>
    </div>
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,20rem),1fr));gap:var(--s-10);align-items:center">
      <div data-reveal>
        <div class="photo photo--card">
          <img src="assets/img/card-front.webp?v=3" width="1200" height="1200" alt="Anmeldelseskortets hvide side med Google-logo, NFC-symbol og fem stjerner" loading="lazy">
        </div>
      </div>
      <div class="stack-6" data-reveal="60">
        <div class="stack"><h3>Det sker ved disken</h3>
          <p class="small">Mens oplevelsen stadig er frisk, og kunden stadig står der. Ikke tre dage senere i en mail der aldrig bliver åbnet.</p></div>
        <div class="stack"><h3>Ingen app at hente</h3>
          <p class="small">Kunden holder telefonen mod kortet, og anmeldelsessiden åbner af sig selv. Ingen app, intet kamera.</p></div>
        <div class="stack"><h3>Ét kort, uendeligt brug</h3>
          <p class="small">Intet batteri, intet abonnement, ingen udløbsdato. Kortet ligger på disken og virker hver eneste dag.</p></div>
      </div>
    </div>
  </div>
</section>"""

home_steps = """
<section class="section section--sunk">
  <div class="wrap stack-8">
    <h2 class="h2" data-reveal>Ti sekunder ved disken</h2>
    <div class="grid grid-3">
      <div class="stack" data-reveal><div class="step__n">1</div><h3>Telefonen mod kortet</h3>
        <p class="small">Ingen app. Intet kamera. Kunden lægger bare telefonen på.</p></div>
      <div class="stack" data-reveal="60"><div class="step__n">2</div><h3>Siden åbner selv</h3>
        <p class="small">Skrivefeltet står klar med stjernerne. Ikke din profil — selve feltet.</p></div>
      <div class="stack" data-reveal="120"><div class="step__n">3</div><h3>De skriver den med det samme</h3>
        <p class="small">Før de går ud ad døren, mens oplevelsen stadig er frisk.</p></div>
    </div>
    <div data-reveal="180"><a class="btn btn--lg" href="anmeldelseskort.html">Se kortet — fra %d kr %s</a></div>
  </div>
</section>""" % (P1, ARROW)

home_products = """
<section class="section">
  <div class="wrap stack-8">
    <div class="grid grid-2">
      <div class="prod" data-reveal>
        <div class="prod__media">%s</div>
        <div class="prod__body">
          <span class="eyebrow">Googles motiv</span>
          <h3 style="font-size:1.35rem">Anmeldelseskort</h3>
          <p class="small">Motivet siger selv hvad der sker. Du skal ikke forklare noget ved disken.</p>
          <div class="prod__foot stack">
            <div class="row"><span class="badge">På lager</span></div>
            <p><strong style="font-size:1.2rem">Fra %d kr</strong><br><span class="small">ned til %d kr pr. kort</span></p>
            <a class="btn" href="/anmeldelseskort#bestil">Bestil — fra %d kr %s</a>
          </div>
        </div>
      </div>
      <div class="prod" data-reveal="80">
        <div class="prod__media">
          <img src="assets/img/card-back.webp?v=3" width="1200" height="1200" alt="Anmeldelseskortets sorte side med Google-logo i hvid cirkel" loading="lazy">
        </div>
        <div class="prod__body">
          <span class="eyebrow">Dit eget motiv</span>
          <h3 style="font-size:1.35rem">Kort med dit logo</h3>
          <p class="small">Vores tryk erstattet med dit. Fra 250 stk., sort eller hvid.</p>
          <div class="prod__foot stack">
            <div class="row"><span class="badge badge--soft">Bestilling</span></div>
            <p><strong style="font-size:1.2rem">Fra %d kr</strong><br><span class="small">ved 250 stk. og opefter</span></p>
            <a class="btn btn--ghost" href="kontakt.html">Få et tilbud %s</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>""" % (CARD_3D, P1, TIERS[-1][1], P1, ARROW, TIERS[-2][1], ARROW)

home_trust = """
<div class="wrap">
  <div class="trust" data-reveal>
    <span>%s Fri fragt til pakkeshop</span>
    <span>%s 14 dages fortrydelsesret</span>
    <span>%s 2 års reklamationsret</span>
    <span>%s Intet abonnement</span>
  </div>
</div>""" % (CHECK, CHECK, CHECK, CHECK)

home_prices = """
<section class="section section--sunk">
  <div class="wrap stack-8">
    <div class="stack" data-reveal>
      <h2 class="h2">Flere kort. Flere anmeldelser.</h2>
      <p class="lede" style="max-width:34rem">Ét ved kassen. Ét ved bordet. Ét i reserve.</p>
    </div>
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,19rem),1fr));gap:var(--s-10);align-items:start">
      <div class="stack-6" data-reveal="60">
        <div class="stat" style="background:var(--surface-card)">
          <span class="eyebrow">Pris pr. kort</span>
          <div class="stat__n" style="margin-top:var(--s-3)">%d<small>→</small>%d<small>kr</small></div>
          <p class="stat__note" style="margin-top:var(--s-3);color:var(--green);font-weight:560">%d kr lavere pr. kort ved 500 stk.</p>
        </div>
        <p class="small">Fri fragt til pakkeshop. <a href="maengderabat.html" style="text-decoration:underline">Over 500 kort?</a></p>
        <div><a class="btn btn--lg" href="/anmeldelseskort?antal=3#bestil">Bestil 3 kort — %d kr %s</a></div>
      </div>
      <div data-reveal="120">
        %s
        <p class="tiny" style="margin-top:var(--s-4)">Ni trin — helt ned til %d kr pr. kort. Priser inkl. moms.</p>
      </div>
    </div>
  </div>
</section>""" % (P1, TIERS[-1][1], P1 - TIERS[-1][1], TIERS[1][1] * 3, ARROW, tier_rows(), TIERS[-1][1])

home_quotes = """
<section class="section">
  <div class="wrap stack-8">
    <div class="stack" data-reveal><span class="eyebrow">Glade kunder</span><h2 class="h2">Det siger de, der bruger kortet</h2></div>
    <div class="note" style="max-width:44rem" data-reveal>
      <p class="small"><strong>Pladsholder — skal udfyldes før lancering.</strong> Sektionen er bygget færdig, men står med vilje tom. Indsæt rigtige citater fra rigtige kunder, med deres accept. Opdigtede anmeldelser er forbudt efter markedsføringslovens bilag 1 nr. 23c, og § 6 b kræver at du oplyser hvordan du sikrer at anmeldelser er ægte.</p>
    </div>
    <div class="grid grid-3">""" + "".join("""
      <div class="card" data-reveal="%d" style="opacity:.5">
        <div class="stars">%s</div>
        <p class="small" style="margin-top:var(--s-3)">Citat fra kunde %d indsættes her.</p>
        <p class="tiny" style="margin-top:var(--s-4)">Navn · Virksomhed · By</p>
      </div>""" % (i * 60, star() * 5, i + 1) for i in range(3)) + """
    </div>
  </div>
</section>"""

FAQ_ALL = [
    ("Virker kortet på alle telefoner?", [
        "På langt de fleste. iPhone XS og nyere læser kortet i baggrunden — du lægger bare telefonen på, uden at åbne noget først.",
        "Ældre iPhones (7, 8 og X) og helt gamle telefoner bruger bare QR-koden på bagsiden — det tager to sekunder ekstra. På Android skal funktionen NFC være slået til, hvilket den er på de fleste.",
        "Derfor er der også en QR-kode på bagsiden. Så virker det uanset telefon.",
    ]),
    ("Kan jeg ændre linket bagefter?", [
        "Ja. Kortet er beskyttet med kode, så tilfældige forbipasserende ikke kan omprogrammere det — men du kan selv ændre linket så mange gange du vil.",
        "Praktisk hvis du flytter adresse, skifter navn, eller vil pege kortet mod Trustpilot eller Facebook i stedet for Google.",
    ]),
    ("Er kortene programmeret på forhånd?", [
        "Ja, hvis du sender dit Google-link når du bestiller. Vi programmerer og tester hvert enkelt kort, inden det bliver pakket. Det koster ikke ekstra.",
        "Vil du hellere selv, sender vi dem blanke. Det tager under et minut per kort med en gratis app — se vejledningen under Sæt det op.",
    ]),
    ("Hvor længe holder kortene?", [
        "Chippen har ingen batteri og bruger ingen strøm. Den henter energi fra telefonen i det øjeblik den bliver læst.",
        "NXP oplyser en datalevetid på omkring 10 år og mindst 100.000 skrivninger. I praksis er det plastikken der slides før chippen — kortet er PVC og tåler vand, men ikke at blive bøjet igen og igen.",
    ]),
    ("Kan jeg få mit eget logo på?", [
        "Ved større ordrer, ja. Fra 250 stk. kan vi lave kort med dit eget tryk i stedet for standarddesignet.",
        "Under 250 stk. sælger vi kun standardkortet. Skriv til os hvis du vil have et tilbud på dit eget design.",
    ]),
    ("Kan jeg betale med faktura?", [
        "Ja, ved ordrer fra 250 stk. Vi sender faktura med 14 dages betaling.",
        "Under 250 stk. betales der ved bestilling med kort eller MobilePay.",
    ]),
    ("Hvornår får jeg kortene?", [
        "Vi sender 1–2 hverdage efter bestilling. Derfra er der typisk 1–3 hverdage.",
        "Levering til pakkeshop er gratis, uanset hvor meget du køber — du vælger selv den nærmeste ved betaling. Vi bruger GLS, DAO, PostNord og Bring.",
        "Vil du have det leveret til døren i stedet, koster det 49 kr.",
    ]),
    ("Hvad hvis kortet ikke virker?", [
        "Så sender vi et nyt, uden beregning og med fragt betalt. Det gælder i hele reklamationsperioden på 2 år.",
        "Virker det ikke som forventet, kan du også bare fortryde købet inden for 14 dage og få pengene tilbage.",
    ]),
    ("Hvad er et anmeldelseskort egentlig?", [
        "Et plastikkort på størrelse med et betalingskort, med en lille chip indeni. Chippen indeholder linket til din Google-anmeldelsesside.",
        "Når en kunde lægger sin telefon mod kortet, læser telefonen linket og åbner siden. Der er ingen app, ingen forbindelse og ingen strøm involveret.",
    ]),
    ("Hvad koster et anmeldelseskort?", [
        "Ét kort koster %d kr inkl. moms. Køber du flere, falder prisen — ned til %d kr pr. stk. ved 500 stk." % (P1, TIERS[-1][1]),
        "Der er ingen løbende omkostninger oveni. Se hele pristrappen under Mængderabat.",
    ]),
    ("NFC eller QR-kode — hvad er forskellen?", [
        "QR kræver at kunden åbner kameraet, sigter og trykker på et link. NFC kræver kun at telefonen kommer tæt på kortet.",
        "NFC er hurtigere når det virker, men virker ikke på ældre telefoner. QR virker på alt med et kamera. Derfor har vores kort begge dele — NFC på forsiden, QR på bagsiden.",
    ]),
    ("Må man bede sine kunder om en anmeldelse?", [
        "Ja. Google skriver selv at man gerne må opfordre kunder til at anmelde, så længe man ikke belønner dem for det eller forsøger at påvirke hvad de skriver.",
        "Det du <em>ikke</em> må: give rabat eller gaver for en anmeldelse, kun spørge de tilfredse kunder, eller bede folk skrive noget bestemt. Det er i strid med Googles regler og kan koste dig alle dine anmeldelser — og frasortering af utilfredse kunder er også ulovligt efter dansk markedsføringslov.",
        "Kortet gør det nemt for alle kunder at anmelde. Det er både det mest effektive og det eneste lovlige.",
    ]),
]

home_faq = """
<section class="section">
  <div class="wrap">
    <div class="stack-8" style="max-width:48rem">
      <h2 class="h2" data-reveal>Spørgsmål</h2>
      <div data-reveal="60">%s</div>
      <p class="small" data-reveal="100"><a href="faq.html" style="text-decoration:underline">Se alle spørgsmål og svar %s</a></p>
      <div data-reveal="120"><a class="btn btn--lg" href="anmeldelseskort.html">Se kortet — fra %d kr %s</a></div>
    </div>
  </div>
</section>""" % (acc([FAQ_ALL[0], FAQ_ALL[11], FAQ_ALL[7]]), ARROW, P1, ARROW)

GUIDE_CARDS = [
    ("guides/flere-google-anmeldelser.html", "Den store guide", "Sådan får du flere Google-anmeldelser",
     "Hvornår du skal spørge, hvad du skal sige, og hvad du ikke må."),
    ("saadan-virker-det.html", "Sådan virker det", "Derfor virker et anmeldelseskort",
     "Hvad kortet gør ved besværet — og hvad det ikke kan."),
    ("guides/placering.html", "Placering", "Hvor skal kortet ligge?",
     "Konkrete placeringer for café, frisør, værksted og butik."),
    ("guides/nfc-eller-qr.html", "Teknik", "NFC eller QR-kode?",
     "Hvornår hver af dem virker, og hvilke telefoner der kan hvad."),
    ("guides/regler-for-anmeldelser.html", "Regler", "Er det lovligt at bede om anmeldelser?",
     "Googles regler om rabatter, frasortering og pres i butikken."),
    ("guides/daarlige-anmeldelser.html", "Når det går skævt", "Hvad gør du ved dårlige anmeldelser?",
     "Hvad der kan fjernes, og hvad et godt svar indeholder."),
]

home_guides = """
<section class="section section--sunk">
  <div class="wrap stack-8">
    <div class="stack" data-reveal>
      <span class="eyebrow">Guides</span>
      <h2 class="h2">Læs videre</h2>
      <p class="lede" style="max-width:32rem">De spørgsmål vi oftest får — besvaret ordentligt.</p>
    </div>
    <div class="grid grid-3">""" + "".join("""
      <a class="card card--lift" href="%s" data-reveal="%d">
        <span class="eyebrow">%s</span>
        <h3 style="margin-top:var(--s-3)">%s</h3>
        <p class="small" style="margin-top:var(--s-2)">%s</p>
        <p class="small" style="margin-top:var(--s-5);font-weight:560">Læs guiden %s</p>
      </a>""" % (href, i * 50, eyebrow, title, desc, ARROW)
      for i, (href, eyebrow, title, desc) in enumerate(GUIDE_CARDS)) + """
    </div>
  </div>
</section>"""

home_sticky = """
<div class="stickybar" data-stickybar>
  <p>Flere anmeldelser — fra %d kr · intet abonnement, ingen app</p>
  <a class="btn btn--sm" href="/anmeldelseskort#bestil">Bestil</a>
</div>""" % P1

page("index.html",
     "Anmeldelseskort — {brand}",
     "Anmeldelseskort der sender kunden direkte til jeres Google-anmeldelsesside med ét tryk. Fra %d kr for ét kort og ned til %d kr ved større antal. Intet abonnement." % (P1, TIERS[-1][1]),
     home_benefits + home_paths + home_steps + home_why + home_products
     + home_prices + home_trust + home_faq + home_guides + home_sticky,
     current="index.html", hero=home_hero, jsonld=HOME_LD)


# ================================================================ PRODUKT
spec_rows = [
    ("Format", "Kreditkortstørrelse, 85,6 × 54 × 0,76 mm"),
    ("Materiale", "Massiv PVC, vandtæt"),
    ("Chip", "Indbygget i kortet — holder i mange år"),
    ("Strøm", "Ingen. Chippen får energi fra telefonen"),
    ("Backup", "QR-kode trykt på bagsiden"),
    ("Linkmål", "Google, Trustpilot, Facebook eller din egen side"),
    ("Kan omprogrammeres", "Ja — beskyttet med kode, ikke låst permanent"),
]

ORDER_FORM = """
        <form class="order stack-8" id="bestil" data-order data-tiers='%(tiers)s' novalidate>
          <fieldset class="ofield">
            <legend class="eyebrow">1 · Vælg antal</legend>
            <p class="tiny">Priser inkl. moms. Jo flere kort, jo lavere pris pr. stk.</p>
            <div style="margin-top:var(--s-3)">%(tierpick)s</div>
            <label class="small" for="qty" style="display:block;margin-top:var(--s-4)">Eller skriv et antal</label>
            <input id="qty" name="antal" type="number" min="1" max="5000" value="1" class="inp" data-qty>
          </fieldset>
          <fieldset class="ofield">
            <legend class="eyebrow">2 · Hvem køber?</legend>
            <div class="stack" style="gap:var(--s-3);margin-top:var(--s-3)">
              <label class="opt"><input type="radio" name="koebertype" value="Til egen virksomhed" checked>
                <span><strong>Til min egen virksomhed</strong><br><span class="small">Kortene skal ligge i min butik, salon eller klinik.</span></span></label>
              <label class="opt"><input type="radio" name="koebertype" value="Til videresalg">
                <span><strong>Jeg vil sælge dem videre</strong><br><span class="small">Jeg køber ind og sælger til butikker i mit område. Du behøver ikke have et CVR for at bestille.</span></span></label>
            </div>
          </fieldset>

          <fieldset class="ofield">
            <legend class="eyebrow">3 · Programmering</legend>
            <div class="stack" style="gap:var(--s-3);margin-top:var(--s-3)">
              <label class="opt"><input type="radio" name="programmering" value="Programmeret af jer" checked data-prog>
                <span><strong>Programmér dem for mig</strong><br><span class="small">Gratis. Jeg sender linket nedenfor.</span></span></label>
              <label class="opt"><input type="radio" name="programmering" value="Blanke, jeg gør det selv" data-prog>
                <span><strong>Send dem blanke</strong><br><span class="small">Jeg programmerer selv med en gratis app.</span></span></label>
            </div>
            <div data-link-wrap style="margin-top:var(--s-4)">
              <label class="small" for="glink">Link til din Google-anmeldelsesside</label>
              <input id="glink" name="google_link" type="url" class="inp" placeholder="https://g.page/r/…/review" data-glink>
              <p class="tiny" style="margin-top:var(--s-2)">Find det under <em>Anmeldelser → Få flere anmeldelser</em> på din Google-virksomhedsprofil. Er du i tvivl, så lad feltet stå tomt — vi hjælper.</p>
            </div>
          </fieldset>

          <fieldset class="ofield">
            <legend class="eyebrow">4 · Levering</legend>
            <div class="stack" style="gap:var(--s-3);margin-top:var(--s-3)">
              <label class="opt"><input type="radio" name="levering" value="pakkeshop" checked data-ship>
                <span><strong>Pakkeshop — gratis</strong><br><span class="small">GLS, DAO, PostNord eller Bring. Du vælger den nærmeste ved betaling.</span></span></label>
              <label class="opt"><input type="radio" name="levering" value="hjem" data-ship>
                <span><strong>Hjemmelevering — %(ship)d kr</strong><br><span class="small">Leveret til døren på hverdage.</span></span></label>
            </div>
            <p class="tiny" style="margin-top:var(--s-3)">Vi sender 1–2 hverdage efter din bestilling. Derfra er der typisk 1–3 hverdage.</p>
          </fieldset>

          <fieldset class="ofield">
            <legend class="eyebrow">5 · Til fakturaen <span class="tiny">(valgfrit)</span></legend>
            <p class="tiny" style="margin-top:var(--s-2)">Navn, adresse og betaling udfylder du på næste side. Her er kun det, vi ikke kan spørge om der.</p>
            <div class="grid grid-2" style="gap:var(--s-4);margin-top:var(--s-3)">
              <div><label class="small" for="firma">Virksomhed</label><input id="firma" name="virksomhed" class="inp" autocomplete="organization"></div>
              <div><label class="small" for="cvrf">CVR</label><input id="cvrf" name="cvr" class="inp" inputmode="numeric" autocomplete="off"></div>
            </div>
            <label class="small" for="besked" style="display:block;margin-top:var(--s-4)">Besked til os <span class="tiny">(valgfrit)</span></label>
            <textarea id="besked" name="besked" rows="3" class="inp" placeholder="Fx ønsket leveringsdato, eller noget vi skal vide om programmeringen."></textarea>
          </fieldset>
          <div class="sumbox">
            <h3>Din ordre</h3>
            <div class="sumrow"><span><span data-sum-qty>1</span> kort à <span data-sum-unit>189</span> kr</span><span data-sum-goods>189 kr</span></div>
            <div class="sumrow"><span>Fragt</span><span data-sum-ship>Gratis</span></div>
            <hr class="hairline">
            <div class="sumrow sumrow--total"><span>I alt</span><span><span data-sum-total>189</span> kr</span></div>
            <p class="tiny" data-sum-ex>heraf moms — kr · ekskl. moms — kr</p>
            <p class="tiny" data-sum-save style="color:var(--green);font-weight:560"></p>
            <button class="btn btn--lg" type="submit" style="width:100%%;margin-top:var(--s-5)">Gå til betaling</button>
            <p class="tiny" style="margin-top:var(--s-3)">Du sendes til vores sikre betalingsside. Kortoplysninger indtastes aldrig her på sitet.</p>
            <p class="tiny" style="margin-top:var(--s-4)">14 dages fortrydelsesret · 2 års reklamationsret · Sendes 1–2 hverdage</p>
          </div>
        </form>"""

produkt = """
<section class="section" style="padding-top:clamp(var(--s-10),5vw,var(--s-16))">
  <div class="wrap">
    <div class="grid grid--product" style="gap:var(--s-12);align-items:start">
      <div class="grid--product__media" data-reveal>%s</div>
      <div class="stack-6 grid--product__info" data-reveal="60">
        <div class="stack">
          <span class="eyebrow">Produktet</span>
          <h1 class="h1">Anmeldelseskort</h1>
          <div class="row"><span class="stars">%s</span><span class="small">Hvid og sort side · standarddesign</span></div>
        </div>
        <p class="lede">Læg kortet på disken. Kunden holder telefonen mod det, og din Google-anmeldelsesside åbner med det samme — klar til at skrive i.</p>
        <div class="row">
          <span class="pill">Ingen app</span><span class="pill">Intet abonnement</span><span class="pill">Gratis programmering</span>
        </div>
        <hr class="hairline">
%%(FORM)s
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,22rem),1fr));gap:var(--s-10);align-items:start">
      <div class="stack-6" data-reveal>
        <span class="eyebrow">Forklaret kort</span>
        <h2 class="h2">Hvad er et anmeldelseskort?</h2>
        <p>Et anmeldelseskort er et kort i kreditkortstørrelse med en lille chip indeni. Chippen indeholder et link til jeres virksomheds side på Google. Når en kunde holder telefonen mod kortet, åbner telefonen siden, hvor man giver stjerner og skriver en anmeldelse. Der skal ikke hentes nogen app.</p>
        <p>Kortet kaldes også et Google review-kort, et NFC-anmeldelseskort eller på engelsk et <em>Google review card</em> eller <em>tap card</em>. Det er det samme produkt. På bagsiden sidder der også en QR-kode, så det virker på alle telefoner — også dem uden NFC.</p>
        <h3>Hvad koster et anmeldelseskort?</h3>
        <p>Ét kort koster %d kr inkl. moms. Køber du flere, falder prisen pr. kort — ned til %d kr ved 500 stk. Der er intet abonnement og ingen månedlig betaling: du betaler én gang, og kortet virker, så længe jeres Google-profil findes. Programmering er gratis, og der er fri fragt til pakkeshop.</p>
      </div>
      <div class="stack-6" data-reveal="60">
        <span class="eyebrow">Hvem bruger det</span>
        <h2 class="h2">Til steder hvor kunden står ved disken</h2>
        <ul class="stack" style="gap:var(--s-3);padding-left:1.1em">
          <li><strong><a href="/brancher/frisoer">Frisører og saloner</a></strong> — kortet ligger ved kassen, mens kunden betaler.</li>
          <li><strong><a href="/brancher/klinik">Klinikker og behandlere</a></strong> — ved receptionen, når næste tid er booket.</li>
          <li><strong><a href="/brancher/restaurant-og-cafe">Caféer og restauranter</a></strong> — på disken eller med regningen.</li>
          <li><strong><a href="/brancher/butik">Butikker</a></strong> — ved betalingsterminalen, hvor alle kunder kommer forbi.</li>
          <li><strong><a href="/brancher/haandvaerker-og-vaerksted">Håndværkere og værksteder</a></strong> — giv kortet til kunden, når jobbet er færdigt.</li>
          <li><strong>Forhandlere</strong> — køb ind til fast pris og sælg kortene videre til lokale virksomheder.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--sunk">
  <div class="wrap stack-8">
    <div class="stack" data-reveal><span class="eyebrow">Specifikationer</span><h2 class="h2">Hvad du får med kortet</h2></div>
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,22rem),1fr));gap:var(--s-10)">
      <div class="scroller" data-reveal>
        <table class="tbl">%s</table>
      </div>
      <div class="stack-6" data-reveal="60">
        <div class="card">
          <h3>Vi programmerer det for dig</h3>
          <p class="small" style="margin-top:var(--s-2)">Send dit Google-link ved bestilling, så koder og tester vi kortet inden afsendelse. Det koster ikke ekstra, og du skal ikke installere noget.</p>
        </div>
        <div class="card">
          <h3>Du kan altid ændre linket</h3>
          <p class="small" style="margin-top:var(--s-2)">Kortet er kodebeskyttet, ikke permanent låst. Flytter du adresse eller vil pege det et andet sted hen, gør du det selv med en gratis app.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="stack-8" style="max-width:46rem;margin-inline:auto">
      <div class="stack" data-reveal><span class="eyebrow">Inden du bestiller</span><h2 class="h2">Godt at vide</h2></div>
      <div data-reveal="60">%s</div>
    </div>
  </div>
</section>""" % (
    CARD_3D, star() * 5, P1, TIERS[-1][1],
    "".join("<tr><th>%s</th><td>%s</td></tr>" % r for r in spec_rows),
    acc([FAQ_ALL[0], FAQ_ALL[2], FAQ_ALL[6], FAQ_ALL[11]]),
)

produkt = produkt.replace("%(FORM)s", ORDER_FORM % {"tiers": TIERS_JSON, "tierpick": tier_rows(pick=True), "ship": SHIP_HOME})

PRODUCT_LD = {
    "@context": "https://schema.org", "@type": "Product",
    "name": "Anmeldelseskort",
    "description": "Anmeldelseskort (Google review-kort) i kreditkortstørrelse med indbygget chip og QR-kode. Kunden holder telefonen mod kortet, og virksomhedens Google-anmeldelsesside åbner.",
    "image": [BASE_URL + "/assets/img/card-front.webp", BASE_URL + "/assets/img/card-back.webp", BASE_URL + "/assets/img/card-hero.webp"],
    "sku": "NFC-GOOGLE-SORT",
    "url": BASE_URL + "/anmeldelseskort",
    "brand": {"@type": "Brand", "name": "{brand}"},
    "material": "PVC",
    "offers": {
        "@type": "AggregateOffer", "priceCurrency": "DKK",
        "lowPrice": str(TIERS[-1][1]), "highPrice": str(P1),
        "offerCount": str(len(TIERS)), "availability": "https://schema.org/InStock",
        "hasMerchantReturnPolicy": {"@type": "MerchantReturnPolicy",
            "applicableCountry": "DK",
            "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
            "merchantReturnDays": 14},
    },
}

page("anmeldelseskort.html",
     "Anmeldelseskort — fra %d kr — {brand}" % P1,
     "Anmeldelseskort der åbner jeres Google-anmeldelsesside med ét tryk — og en QR-kode på bagsiden til ældre telefoner. Fra %d kr inkl. moms, gratis programmering." % P1,
     produkt, jsonld=PRODUCT_LD)


# ================================================================ SÅDAN VIRKER DET
saadan = hero(
    "Sådan virker det",
    "Ti sekunder ved disken",
    "Der er ingen app, ingen forbindelse og ingen strøm. Kortet indeholder ét stykke information: linket til din anmeldelsesside. Telefonen læser det og åbner siden.",
    '<a class="btn btn--lg" href="anmeldelseskort.html">Se kortet</a><a class="btn btn--ghost btn--lg" href="saet-det-op.html">Sæt det op selv</a>',
) + """
<section class="section--tight">
  <div class="wrap">%s</div>
</section>

<section class="section section--sunk">
  <div class="wrap stack-8">
    <div class="stack" data-reveal><span class="eyebrow">Trin for trin</span><h2 class="h2">Hvad der faktisk sker</h2></div>
    <div class="grid grid-2">
      <div class="stack" data-reveal><div class="step__n">1</div><h3>Telefonen kommer tæt på</h3>
        <p class="small">NFC-antennen i telefonen sender et svagt magnetfelt. Chippen i kortet har ingen strøm selv — den henter energien fra netop det felt. Rækkevidden er få centimeter, så det sker kun når kunden vil det.</p></div>
      <div class="stack" data-reveal="60"><div class="step__n">2</div><h3>Chippen sender linket</h3>
        <p class="small">Kortet indeholder én ting: en webadresse, gemt som en såkaldt URI-post. Det er den type telefonen genkender som "det her er et link, det skal åbnes".</p></div>
      <div class="stack" data-reveal="120"><div class="step__n">3</div><h3>Telefonen viser en notifikation</h3>
        <p class="small">På iPhone popper der en lille bjælke op i toppen. På Android åbner linket typisk direkte. Kunden trykker én gang.</p></div>
      <div class="stack" data-reveal="180"><div class="step__n">4</div><h3>Anmeldelsesfeltet er åbent</h3>
        <p class="small">Ikke din Google-profil — selve feltet hvor man skriver anmeldelsen, med stjernerne klar. Kunden skriver og sender.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="stack-8" style="max-width:46rem;margin-inline:auto">
      <div class="stack" data-reveal><span class="eyebrow">NFC og QR</span><h2 class="h2">Hvorfor kortet har begge dele</h2></div>
      <div class="prose" data-reveal="60">
        <p>NFC er hurtigere. Kunden skal ikke åbne kameraet, sigte og trykke på et link — telefonen skal bare tæt på.</p>
        <p>Men NFC virker ikke på alt. iPhone XS og nyere læser i baggrunden uden videre. iPhone 7, 8 og X kan læse NFC, men kun hvis man selv åbner NFC-læseren i Kontrolcenter. iPhone 6s og ældre kan slet ikke. På Android skal NFC være slået til, og skærmen skal være tændt og låst op.</p>
        <p>Det er derfor der er en QR-kode på bagsiden. Møder kortet en telefon der ikke kan NFC, virker QR alligevel. Det koster ingenting at have med, og det fjerner den eneste situation hvor produktet ellers ville skuffe kunden foran disken.</p>
        <h2>Hvad du skal bruge</h2>
        <p>En Google-virksomhedsprofil. Har du allerede et sted der dukker op i Google Maps med adresse og åbningstider, har du den.</p>
        <p>Har du ikke en, opretter du den gratis hos Google, og så skal profilen verificeres, før du kan modtage anmeldelser. Det tager typisk nogle dage.</p>
      </div>
      <div class="row" data-reveal="120">
        <a class="btn" href="anmeldelseskort.html">Bestil kortet</a>
        <a class="btn btn--ghost" href="guides/nfc-eller-qr.html">Læs mere om NFC vs. QR</a>
      </div>
    </div>
  </div>
</section>""" % CARD_3D

page("saadan-virker-det.html", "Sådan virker et anmeldelseskort — {brand}",
     "Sådan fungerer anmeldelseskortet trin for trin: hvad chippen indeholder, hvordan telefonen læser den, og hvorfor der også er en QR-kode.",
     saadan)


# ================================================================ SÆT DET OP
saet_op = hero(
    "Vejledning",
    "Sæt kortet op selv",
    "Bestiller du blanke kort, tager det under et minut per kort. Du skal bruge en telefon med NFC og en gratis app. Ingen computer, intet udstyr.",
) + """
<section class="section--tight">
  <div class="wrap">
    <div class="stack-8" style="max-width:46rem">
      <div class="card" data-reveal>
        <span class="eyebrow">Trin 1</span>
        <h3 style="margin-top:var(--s-2)">Find dit Google-anmeldelseslink</h3>
        <div class="prose small" style="margin-top:var(--s-3)">
          <p>Log ind på din Google-virksomhedsprofil. Gå til <em>Anmeldelser</em> og vælg <em>Få flere anmeldelser</em>. Google giver dig et link, der fører direkte til skrivefeltet.</p>
          <p>Kopiér linket. Det er det, der skal ind på kortet.</p>
          <p class="note" style="margin-top:var(--s-4)">Brug det link Google selv giver dig. Undgå at bygge dit eget ud fra søgeresultater — det kan holde op med at virke.</p>
        </div>
      </div>

      <div class="card" data-reveal="60">
        <span class="eyebrow">Trin 2</span>
        <h3 style="margin-top:var(--s-2)">Hent en NFC-app</h3>
        <div class="prose small" style="margin-top:var(--s-3)">
          <p><strong>NFC Tools</strong> er gratis og findes til både iPhone og Android. Der findes andre — det vigtige er, at appen kan skrive en <em>URL</em> eller <em>URI</em>, ikke kun ren tekst.</p>
        </div>
      </div>

      <div class="card" data-reveal="120">
        <span class="eyebrow">Trin 3</span>
        <h3 style="margin-top:var(--s-2)">Skriv linket til kortet</h3>
        <div class="prose small" style="margin-top:var(--s-3)">
          <p>Åbn appen, vælg <em>Skriv</em> → <em>Tilføj post</em> → <em>URL/URI</em>. Indsæt dit link. Tryk <em>Skriv</em> og hold telefonen mod kortet, indtil appen siger det er gennemført.</p>
          <p class="note" style="margin-top:var(--s-4)"><strong>Vigtigt:</strong> vælg <em>URL/URI</em> — ikke <em>Tekst</em>. Skriver du linket som ren tekst, åbner iPhone ikke siden automatisk. Det er den hyppigste fejl.</p>
        </div>
      </div>

      <div class="card" data-reveal="180">
        <span class="eyebrow">Trin 4</span>
        <h3 style="margin-top:var(--s-2)">Beskyt kortet med en kode</h3>
        <div class="prose small" style="margin-top:var(--s-3)">
          <p>Et ubeskyttet kort kan omprogrammeres af enhver med en gratis app på ti sekunder. Står kortet frit på en disk, bør det være beskyttet.</p>
          <p>I NFC Tools finder du det under <em>Andet</em> → <em>Sæt adgangskode</em>. Vælg en kode du husker — den skal bruges, hvis du senere vil ændre linket.</p>
          <p><strong>Brug adgangskode, ikke permanent låsning.</strong> Permanent låsning kan ikke fortrydes, og så er kortet ubrugeligt hvis du flytter eller skriver forkert.</p>
        </div>
      </div>

      <div class="card" data-reveal="240">
        <span class="eyebrow">Trin 5</span>
        <h3 style="margin-top:var(--s-2)">Test det på en anden telefon</h3>
        <div class="prose small" style="margin-top:var(--s-3)">
          <p>Test altid med en telefon der ikke er den, du skrev med. Læg den mod kortet, og se om anmeldelsesfeltet åbner.</p>
          <p>Virker det ikke: tjek at NFC er slået til, at telefonen er låst op, og at posten blev skrevet som URL og ikke tekst.</p>
        </div>
      </div>

      <div class="stack" data-reveal="300">
        <h2 class="h2">Hvor lægger man kortet?</h2>
        <div class="prose small">
          <p>Ved betalingen, hvor kunden alligevel står stille med telefonen fremme. Det er det eneste sted i et besøg, hvor der er en naturlig pause.</p>
          <p>Undgå at lægge kortet ovenpå metal — en metalbakke eller et stålbord under kortet svækker signalet mærkbart. Træ, plastik, glas og pap er helt uproblematisk.</p>
          <p>Og lad være med at gemme det væk. Et kort i en skuffe bliver aldrig brugt.</p>
        </div>
        <div><a class="btn btn--ghost" href="guides/placering.html">Mere om placering</a></div>
      </div>
    </div>
  </div>
</section>"""

page("saet-det-op.html", "Sæt dit anmeldelseskort op selv — {brand}",
     "Trin-for-trin vejledning: find dit Google-anmeldelseslink, skriv det til NFC-chippen, beskyt kortet med kode og test det.",
     saet_op)


# ================================================================ MÆNGDERABAT
calc_btns = "".join('<button class="btn btn--ghost btn--sm" data-calc-set="%d">%d</button>' % (q, q) for q, _ in TIERS[3:])

maengde = hero(
    "Mængderabat",
    "Jo flere, jo billigere",
    "Prisen falder trinvist. Fra 250 stk. får du fast indkøbspris, mulighed for dit eget tryk og betaling med faktura.",
) + """
<section class="section--tight">
  <div class="wrap">
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,20rem),1fr));gap:var(--s-10);align-items:start">
      <div data-reveal>%s</div>
      <div class="card" data-calc='%s' data-reveal="60">
        <h3>Regn din pris ud</h3>
        <label class="small" for="qty" style="display:block;margin-top:var(--s-4)">Antal kort</label>
        <input id="qty" type="number" min="1" max="5000" value="100" data-calc-qty
               style="width:100%%;margin-top:var(--s-2);padding:.7rem .9rem;font:inherit;font-variant-numeric:tabular-nums;
                      background:var(--surface-sunk);color:var(--text);border:1px solid var(--hairline);border-radius:var(--r-md)">
        <div class="row" style="margin-top:var(--s-3);gap:var(--s-2)">%s</div>
        <hr class="hairline" style="margin-block:var(--s-5)">
        <div class="stack" style="gap:var(--s-3)">
          <div class="row" style="justify-content:space-between"><span class="small">Pris pr. stk.</span><span class="num" style="font-weight:600"><span data-calc-unit>55</span> kr</span></div>
          <div class="row" style="justify-content:space-between"><span class="small">I alt inkl. moms</span><span class="num" style="font-weight:640;font-size:1.3rem;letter-spacing:-.02em"><span data-calc-total>5.500</span> kr</span></div>
        </div>
        <p class="tiny" style="margin-top:var(--s-4)">Vejledende. Fri fragt til pakkeshop, hjemmelevering 49 kr.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--sunk">
  <div class="wrap stack-8">
    <div class="stack" data-reveal><span class="eyebrow">Fra 250 stk.</span><h2 class="h2">Hvad der følger med større ordrer</h2></div>
    <div class="grid grid-3">
      <div class="card" data-reveal><h3>Fast indkøbspris</h3><p class="small" style="margin-top:var(--s-2)">Du betaler samme pris hver gang, uden at skulle forhandle på ny ved hver ordre.</p></div>
      <div class="card" data-reveal="60"><h3>Dit eget tryk</h3><p class="small" style="margin-top:var(--s-2)">Fra 250 stk. kan bagsiden trykkes med dit logo eller dit eget design i stedet for standarden.</p></div>
      <div class="card" data-reveal="120"><h3>Faktura, 14 dage</h3><p class="small" style="margin-top:var(--s-2)">Du behøver ikke betale ved bestilling. Vi sender faktura med 14 dages betalingsfrist.</p></div>
    </div>
    <div class="center" data-reveal="180">
      <a class="btn btn--lg" href="kontakt.html">Få et tilbud</a>
      <p class="tiny" style="margin-top:var(--s-3)">Over 500 stk.? Skriv til os — vi vender tilbage med et tilbud, typisk samme dag.</p>
    </div>
  </div>
</section>""" % (tier_rows(), TIERS_JSON, calc_btns)

page("maengderabat.html", "Mængderabat på anmeldelseskort — fra %d kr pr. stk. — {brand}" % TIERS[-1][1],
     "Anmeldelseskort i mængder: prisen falder fra %d kr til %d kr pr. kort. Fra 250 stk. eget tryk og betaling med faktura." % (P1, TIERS[-1][1]),
     maengde)


# ================================================================ FORHANDLER
_tp = dict(TIERS)
def _pack(q, label, featured=False):
    unit = _tp[q]
    return ('<div class="card%s"><span class="eyebrow">%s</span><h3 style="margin-top:var(--s-2)">%d kort</h3>'
            '<p class="small" style="margin-top:var(--s-2)"><strong>%s kr</strong> · %d kr pr. kort</p>'
            '<a class="btn%s" style="margin-top:var(--s-4)" href="/anmeldelseskort?antal=%d&amp;type=forhandler#bestil">Bestil %d kort</a></div>'
            % (" card--featured" if featured else "", label, q, f"{q*unit:,}".replace(",", "."), unit,
               "" if featured else " btn--ghost", q, q))

# Startpakke: separat Shopify-produkt (3 blanke kort, 299 kr), så mængderabatterne ikke rammer den.
START_VARIANT = "60671332942169"
START_PRICE = 299
START_URL = ("https://shop.reviewpartneren.dk/cart/%s:1?attributes%%5BKundetype%%5D=Til%%20videresalg"
             "&amp;attributes%%5BProgrammering%%5D=Blanke%%20kort&amp;attributes%%5BKilde%%5D=Startpakke" % START_VARIANT)
def _startpack():
    return ('<div class="card card--featured"><span class="eyebrow">Start her</span><h3 style="margin-top:var(--s-2)">Startpakke · 3 kort</h3>'
            '<p class="small" style="margin-top:var(--s-2)"><strong>%d kr</strong> · ca. %d kr pr. kort · blanke kort</p>'
            '<p class="small" style="margin-top:var(--s-2)">Sælger du dem for %d kr stykket, er forskellen %d kr på pakken.</p>'
            '<a class="btn" style="margin-top:var(--s-4)" href="%s" data-startpakke>Køb startpakken</a></div>'
            % (START_PRICE, round(START_PRICE / 3), _tp[1], 3 * _tp[1] - START_PRICE, START_URL))

forhandler = hero(
    "Forhandler",
    "Sælg anmeldelseskort til butikker i dit område",
    "Start med 3 kort for %d kr, test dit område, og køb flere når det sælger. Køber du flere, falder prisen af sig selv — helt ned til %d kr pr. kort. Du sætter selv din pris, og der er ingen binding." % (START_PRICE, TIERS[-1][1]),
    buttons='<a class="btn btn--lg" href="#startpakker">Se startpakkerne</a><a class="btn btn--ghost btn--lg" href="/anmeldelseskort">Se kortet</a>',
    note="Ingen oprettelse · intet gebyr · ingen binding",
) + """
<section class="section--tight" id="startpakker">
  <div class="wrap">
    <div class="stack-8">
      <div class="stack-6" data-reveal>
        <h2 class="h2">Start småt, skalér når det sælger</h2>
        <div class="grid grid-3">%(packs)s</div>
        <p class="small">Skal du bruge flere? Ved 50 kort er prisen %(p50)d kr pr. stk., ved 250 stk. %(p250)d kr og ved 500 stk. %(p500)d kr — med faktura. <a href="/maengderabat">Se hele pristrappen</a>.</p>
      </div>

      <div class="note" data-reveal="60" style="max-width:46rem">
        <p class="small"><strong>Regneeksempel.</strong> Køber du 25 kort til %(p25)d kr og sælger dem for %(p1)d kr — samme pris som en butik betaler hos os for ét kort — er forskellen %(diff)d kr pr. kort. Det er et regnestykke, ikke et løfte: hvad du sælger for, og hvor mange, bestemmer du og dit arbejde.</p>
      </div>

      <div class="stack-6" data-reveal="120">
        <h2 class="h2">Sådan sælger du dem</h2>
        <div class="grid grid-3">
          <div class="stack"><div class="step__n">1</div><h3>Find butikkerne</h3><p class="small">Frisører, caféer, saloner og værksteder med få Google-anmeldelser. Dem finder du på Google Maps på få minutter.</p></div>
          <div class="stack"><div class="step__n">2</div><h3>Vis det på 10 sekunder</h3><p class="small">Programmér et kort til butikkens egen Google-side og lad ejeren trykke med sin telefon. Når anmeldelsessiden åbner, forstår de det med det samme.</p></div>
          <div class="stack"><div class="step__n">3</div><h3>Sælg på stedet</h3><p class="small">Kortet virker med det samme. Tag betaling med MobilePay, og læg kortet ved kassen eller på bordet.</p></div>
        </div>
      </div>

      <div class="stack-6" data-reveal="180">
        <h2 class="h2">Det får du</h2>
        <div class="grid grid-2">
          <div class="card"><h3>Du bestemmer prisen</h3><p class="small" style="margin-top:var(--s-2)">Vi blander os ikke i, hvad du sælger for. Du laver din egen aftale med butikken.</p></div>
          <div class="card"><h3>Vi køber usolgt lager tilbage</h3><p class="small" style="margin-top:var(--s-2)">Går det ikke som håbet, køber vi ubrugte kort i original emballage retur inden for 6 måneder til halv indkøbspris. Så sidder du ikke fast med et lager.</p></div>
          <div class="card"><h3>Blanke eller programmerede</h3><p class="small" style="margin-top:var(--s-2)">Få dem blanke og programmér dem selv til hver butik — det tager under et minut — eller send os linkene, så koder vi dem på forhånd.</p></div>
          <div class="card"><h3>Hurtig levering</h3><p class="small" style="margin-top:var(--s-2)">Fri fragt til pakkeshop. Du kan betale med MobilePay, kort eller Klarna.</p></div>
        </div>
      </div>

      <div class="stack-6" data-reveal="240" style="max-width:46rem">
        <h2 class="h2">Godt at vide</h2>
        <div class="prose small">
          <p><strong>Det er opsøgende salg.</strong> Du tjener på de butikker, du selv går ind i. Vi lover ikke en indtjening, og du får ikke eneret på et område.</p>
          <p><strong>Du er selv sælger.</strong> Sælger du videre, driver du virksomhed — med CVR og moms, når du kommer over 50.000 kr., og ansvaret over for dine kunder.</p>
          <p><strong>Kun over 18 år.</strong> Vi sælger ikke forhandlerpakker til personer under 18 og giver aldrig kredit.</p>
          <p><strong>Kun kort — intet andet.</strong> Ingen kurser, medlemskaber eller henvisningsbonus. Du tjener på at sælge kort, ikke på at hverve andre.</p>
        </div>
      </div>

      <div class="row" data-reveal="300">
        <a class="btn btn--lg" href="%(start_url)s" data-startpakke>Køb startpakken · %(start_price)d kr</a>
        <a class="btn btn--ghost btn--lg" href="/kontakt">Spørgsmål? Skriv til os</a>
      </div>
    </div>
  </div>
</section>""" % {
    "packs": _startpack() + _pack(10, "Når det sælger") + _pack(25, "Klar til at skalere"),
    "start_url": START_URL, "start_price": START_PRICE,
    "p50": _tp[50], "p250": _tp[250], "p500": _tp[500], "p25": _tp[25], "p1": _tp[1], "diff": _tp[1] - _tp[25],
}

page("forhandler.html", "Bliv forhandler af anmeldelseskort — {brand}",
     "Sælg anmeldelseskort til butikker i dit område. Startpakke med 3 kort for %d kr, fri pris, ingen binding og tilbagekøb af usolgt lager. Ned til %d kr pr. kort." % (START_PRICE, TIERS[-1][1]),
     forhandler)


# ================================================================ FAQ
faq_page = hero(
    "Support", "Spørgsmål og svar",
    "Finder du ikke svaret her, så skriv til os. Vi svarer normalt samme hverdag.",
    '<a class="btn" href="kontakt.html">Kontakt support</a>',
) + """
<section class="section--tight">
  <div class="wrap"><div style="max-width:46rem" data-reveal>%s</div></div>
</section>""" % acc(FAQ_ALL)

FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q,
     "acceptedAnswer": {"@type": "Answer", "text": " ".join(a).replace("<em>", "").replace("</em>", "")}}
    for q, a in FAQ_ALL]}

page("faq.html", "Spørgsmål og svar om anmeldelseskort — {brand}",
     "Svar på de mest stillede spørgsmål om anmeldelseskort: telefonkompatibilitet, programmering, levering, holdbarhed og Googles regler.",
     faq_page, jsonld=FAQ_LD)


# ================================================================ OM OS
om = hero(
    "Om os", "En enkel ting, gjort ordentligt",
    "Vi sælger anmeldelseskort til danske virksomheder. Ikke en platform, ikke et abonnement, ikke et dashboard du skal lære at bruge. Et kort der ligger på disken og gør én ting.",
) + """
<section class="section--tight">
  <div class="wrap">
    <div class="prose" data-reveal>
      <h2>Hvorfor</h2>
      <p>De fleste små virksomheder har færre anmeldelser end de fortjener. Ikke fordi kunderne er utilfredse, men fordi det er besværligt at skrive en anmeldelse, og fordi det næsten altid er de utilfredse der gider bruge tiden.</p>
      <p>Det skæve billede kan man rette op på ved at gøre det lige så nemt for alle andre. Det er hele idéen bag kortet.</p>

      <h2>Sådan sælger vi</h2>
      <p><strong>Ingen abonnementer.</strong> Du køber kortet én gang. Vi tjener ikke penge på at du glemmer at opsige noget.</p>
      <p><strong>Ingen tal vi ikke kan dokumentere.</strong> Du vil ikke finde påstande om "3× flere anmeldelser" nogen steder på det her site. Vi ved ikke hvad du får ud af det — det afhænger af hvor mange kunder du har, og hvor kortet ligger.</p>
      <p><strong>Ingen frasortering.</strong> Vi sælger ikke løsninger der sender tilfredse kunder til Google og utilfredse kunder til en intern formular. Det er i strid med både Googles regler og dansk markedsføringslov, og det er en god måde at få slettet alle sine anmeldelser på.</p>

      <h2>Kontakt</h2>
      <p>Skriv til <a data-email href="#">support@…</a>. Vi svarer normalt samme hverdag.</p>
      <p class="small">CVR <span data-cvr>—</span></p>
    </div>
  </div>
</section>"""

page("om-os.html", "Om os — {brand}", "Vi sælger anmeldelseskort til danske virksomheder. Ingen abonnementer, ingen udokumenterede påstande.", om)


# ================================================================ KONTAKT
kontakt = hero(
    "Kontakt", "Skriv til os",
    "Spørgsmål om produktet, en bestilling eller et tilbud på større mængder — skriv, så vender vi tilbage. Normalt samme hverdag.",
) + """
<section class="section--tight">
  <div class="wrap">
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,20rem),1fr));gap:var(--s-10);align-items:start">
      <div class="stack-6" data-reveal>
        <div class="card">
          <h3>E-mail</h3>
          <p class="small" style="margin-top:var(--s-2)">Skriv til <a data-email href="#" style="text-decoration:underline">support@…</a></p>
          <p class="tiny" style="margin-top:var(--s-3)">Skriver du om en bestilling, så husk ordrenummer.</p>
        </div>
        <div class="card">
          <h3>Bestilling</h3>
          <p class="small" style="margin-top:var(--s-2)">Send os antal og linket til din Google-anmeldelsesside, så programmerer vi kortene inden afsendelse.</p>
        </div>
        <div class="card">
          <h3>Større ordrer</h3>
          <p class="small" style="margin-top:var(--s-2)">Fra 250 stk. giver vi fast pris, mulighed for eget tryk og faktura med 14 dages betaling.</p>
        </div>
      </div>
      <div class="stack-6" data-reveal="60">
        <div class="stack">
          <h2 class="h2">Klager</h2>
          <p class="small">Er du utilfreds, så skriv til os først — vi løser næsten alt med det samme.</p>
          <p class="small">Kan vi ikke blive enige, kan du klage til Mæglingsteamet for Forbrugerklager, Nævnenes Hus, Toldboden 2, 8800 Viborg — <a href="https://naevneneshus.dk" target="_blank" rel="noopener" style="text-decoration:underline">naevneneshus.dk</a></p>
        </div>
        <hr class="hairline">
        <div class="stack">
          <h3>Virksomhedsoplysninger</h3>
          <p class="small"><span data-brand>Firmanavn</span><br>CVR <span data-cvr>—</span><br>Danmark<br><a data-email href="#">support@…</a></p>
        </div>
      </div>
    </div>
  </div>
</section>"""

page("kontakt.html", "Kontakt — {brand}", "Skriv til os om produktet, en bestilling eller et tilbud på større mængder.", kontakt)


# ================================================================ GUIDES
GUIDES = [
    ("nfc-eller-qr.html", "NFC eller QR-kode?", "Hvad er forskellen, hvornår virker hvad, og hvorfor bør du have begge dele.",
     """<h2>Den korte version</h2>
     <p>NFC er hurtigere. QR virker på flere telefoner. Derfor har vores kort begge dele.</p>
     <h2>NFC</h2>
     <p>Kunden lægger telefonen mod kortet, og siden åbner. Ingen app, intet kamera, ingen sigten.</p>
     <p>Men det virker ikke på alt. iPhone XS og nyere læser i baggrunden uden videre. iPhone 7, 8 og X kan læse NFC, men kun hvis brugeren selv åbner NFC-læseren i Kontrolcenter. iPhone 6s og ældre kan slet ikke. Android kræver at NFC er slået til, og at skærmen er tændt og låst op.</p>
     <p>Der er også et par situationer hvor iPhone ikke læser i baggrunden selv på nye modeller: hvis telefonen ikke har været låst op siden den blev tændt, hvis kameraet er i brug, eller hvis flytilstand er slået til.</p>
     <h2>QR</h2>
     <p>Virker på alt med et kamera, altså reelt alle telefoner. Til gengæld kræver det tre handlinger af kunden: åbn kamera, sigt, tryk på linket.</p>
     <p>QR har også den fordel at man kan se hvor den fører hen, inden man trykker. Nogle kunder er mere trygge ved det.</p>
     <h2>Hvad vi anbefaler</h2>
     <p>Brug NFC som det primære — det er det der får folk til at prøve. Hav QR som backup, så ingen kunde står ved disken med en telefon der ikke reagerer.</p>
     <p>Det er derfor vores kort har NFC på forsiden og QR på bagsiden. Det koster ingenting at have med, og det fjerner den eneste situation hvor produktet ellers ville skuffe."""),

    ("placering.html", "Hvor skal kortet ligge?", "Placering afgør om kortet bliver brugt eller ej. Her er hvad der virker.",
     """<h2>Ved betalingen</h2>
     <p>Det er det eneste sted i et kundebesøg hvor der er en naturlig pause, og hvor telefonen alligevel er fremme. Ligger kortet der, bliver det brugt. Ligger det ved indgangen, gør det ikke.</p>
     <h2>Pas på metal</h2>
     <p>Metal er det eneste materiale der reelt ødelægger NFC. Ligger kortet på en metalbakke, et stålbord eller oven på en kasseapparat i metal, bliver signalet svækket kraftigt — nogle gange helt væk.</p>
     <p>Træ, plastik, glas, pap og sten er derimod uproblematisk. Et par millimeter materiale koster nogle få millimeter rækkevidde, og der er masser at tage af.</p>
     <h2>Sig det højt</h2>
     <p>Det største enkelte løft kommer ikke fra placeringen, men fra at personalet nævner det. "Hvis du har lyst, kan du lægge telefonen på kortet der" tager to sekunder.</p>
     <p>Men hold det ved at <em>nævne</em> det. Bed ikke personalet om at presse på, sæt ikke mål op for hvor mange anmeldelser der skal komme ind, og bed aldrig kunder om at skrive noget bestemt. Det er i strid med Googles regler, og konsekvensen rammer din profil — ikke kortet.</p>
     <h2>Flere kort</h2>
     <p>Har du flere kasser, borde eller behandlingsrum, så hav ét hvert sted. Et kort der ikke er inden for rækkevidde, er et kort der ikke bliver brugt."""),

    ("daarlige-anmeldelser.html", "Hvad gør du ved dårlige anmeldelser?", "Hvad der kan fjernes, hvad der ikke kan, og hvad et godt svar indeholder.",
     """<h2>Det meste kan ikke fjernes</h2>
     <p>En anmeldelse bliver kun slettet af Google, hvis den bryder deres regler — for eksempel hvis den indeholder chikane, hadefuldt indhold, spam eller reklame, eller hvis den tydeligvis ikke handler om et rigtigt besøg hos dig.</p>
     <p>En ærlig, negativ anmeldelse fra en utilfreds kunde bliver ikke fjernet. Den er præcis det systemet er til for.</p>
     <h2>Sådan rapporterer du en der bryder reglerne</h2>
     <p>Åbn din virksomhedsprofil, find anmeldelsen, og vælg <em>Rapportér</em>. Beskriv hvilken regel du mener er brudt — ikke at du er uenig i indholdet.</p>
     <p>Svaret kan tage dage til uger, og afgørelsen bliver sjældent begrundet. Regn ikke med det som en løsning.</p>
     <h2>Svar i stedet</h2>
     <p>Et svar er ofte mere værd end en sletning, fordi det bliver læst af alle de næste kunder. Et godt svar er kort, konkret og uden forsvarsposition:</p>
     <ul>
       <li>Tak for tilbagemeldingen, uden ironi</li>
       <li>Anerkend det konkrete problem — ikke "vi beklager hvis du oplevede…"</li>
       <li>Sig hvad I gør ved det</li>
       <li>Tilbyd at tage resten offline, med en mail eller et telefonnummer</li>
     </ul>
     <p>Undgå at diskutere fakta offentligt, og undgå at afsløre noget om kunden. Du må ikke skrive detaljer om deres besøg, køb eller helbred — det er persondata.</p>
     <h2>Den bedste beskyttelse er mængde</h2>
     <p>En dårlig anmeldelse blandt otte vejer tungt. Blandt firs gør den næsten ingenting. Derfor er det mest effektive svar på en enkelt sur anmeldelse at gøre det nemt for alle de tilfredse kunder at sige noget.</p>
     <p>Det er dét kortet gør. Ikke ved at filtrere nogen fra — det er både ulovligt og imod Googles regler — men ved at fjerne besværet for alle."""),

    ("regler-for-anmeldelser.html", "Reglerne du skal kende", "Hvad du må og ikke må, når du beder om anmeldelser. Både Googles regler og dansk lov.",
     """<h2>Du må gerne spørge</h2>
     <p>Google skriver selv at virksomheder gerne må opfordre kunder til at skrive en anmeldelse, så længe man ikke belønner dem for det og ikke forsøger at påvirke hvad de skriver. Google udleverer endda selv et link og en QR-kode til formålet.</p>
     <p>Et kort på disken er det samme værktøj i en anden form.</p>
     <h2>Du må ikke belønne</h2>
     <p>Rabat, en gratis kop kaffe, deltagelse i en konkurrence — alt hvad der har værdi, og som gives i bytte for en anmeldelse, er forbudt. Google kalder det falsk engagement. Det er også ulovligt efter EU-reglerne om urimelig handelspraksis.</p>
     <h2>Du må ikke sortere</h2>
     <p>Nogle udbydere sælger løsninger hvor kunden først bliver spurgt "hvordan var din oplevelse?", og hvor de tilfredse sendes videre til Google mens de utilfredse ender i en intern formular.</p>
     <p>Det er forbudt to gange. Google forbyder selektivt at opfordre til positive anmeldelser. Og Forbrugerombudsmandens retningslinjer siger klart, at der ikke må ske en forudgående sortering af hvilke kunder der opfordres til at anmelde.</p>
     <p>Vi sælger ikke den slags, og du bør ikke købe den.</p>
     <h2>Du må ikke skrive dem selv</h2>
     <p>Falske brugeranmeldelser står i bilag 1 til markedsføringsloven som noget der <em>altid</em> er ulovligt. Der skal ikke bevises skade på nogen. Det gælder også anmeldelser skrevet af venner, familie eller ansatte der ikke har været kunder.</p>
     <h2>Pas på ordlyden ved disken</h2>
     <p>Google skriver at man ikke bør kræve eller presse kunder til at skrive anmeldelser <em>mens de er i butikken</em>. Et kort kunden selv vælger at røre ved, er ikke pres. Personale der står og venter mens kunden skriver, er.</p>
     <p>Hold det ved: kortet ligger fremme, og personalet nævner det én gang. Ikke mere.</p>
     <h2>Hvad der sker hvis man overtræder det</h2>
     <p>Google kan slette anmeldelser eller suspendere hele virksomhedsprofilen. Det rammer typisk uden varsel og uden forklaring, og det er svært at få omgjort.</p>
     <p>Fra dansk side kan overtrædelse af markedsføringsloven straffes med bøde."""),
]

# Søgevenlige <title>'er; overskriften på siden bliver den korte.
GUIDE_SEO_TITLES = {
    "nfc-eller-qr.html": "NFC eller QR-kode til Google-anmeldelser?",
    "placering.html": "Hvor skal anmeldelseskortet ligge?",
    "daarlige-anmeldelser.html": "Dårlige Google-anmeldelser: hvad kan du gøre?",
    "regler-for-anmeldelser.html": "Regler for Google-anmeldelser i Danmark",
}

from seo_content import BRANCHER, GUIDES_SEO, GUIDE_OVERRIDES

GUIDES = [(f, t, GUIDE_OVERRIDES[f][0], GUIDE_OVERRIDES[f][1].replace("{P1}", str(P1)))
          if f in GUIDE_OVERRIDES else (f, t, d, b) for f, t, d, b in GUIDES]

def fill(t):
    return t.replace("{P1}", str(P1)).replace("{PMIN}", str(TIERS[-1][1]))

def with_crumbs(hero_html, crumbs_html):
    anchor = '<div class="stack-6" style="max-width:44rem" data-reveal>'
    return hero_html.replace(anchor, anchor + crumbs_html, 1)

def graph(*nodes):
    return {"@context": "https://schema.org", "@graph": [ORG_LD_NODE] + list(nodes)}

ORG_LD_NODE = {k: v for k, v in ORG_LD.items() if k != "@context"}

CTA_BOX = """
<div class="cta-box stack" data-reveal>
  <h2 class="h3">Gør det til ét tryk for kunden</h2>
  <p class="small" style="max-width:36rem">Anmeldelseskort der virker på alle telefoner. Kunden holder telefonen mod kortet, og anmeldelsesfeltet åbner. Fra %d kr — ned til %d kr pr. stk. ved større antal. Vi programmerer kortet gratis.</p>
  <div class="row"><a class="btn" href="/anmeldelseskort#bestil">Se kortet og bestil</a></div>
</div>""" % (P1, TIERS[-1][1])

# Alle guides: de nye søgeguides først, så de gamle.
ALL_GUIDES = [(f, t, d, seo, body) for f, t, d, seo, body in GUIDES_SEO] + \
             [(f, t, d, GUIDE_SEO_TITLES.get(f, t), body) for f, t, d, body in GUIDES]

guide_cards = "".join("""
  <a class="card card--lift" href="%s" data-reveal="%d">
    <h3>%s</h3>
    <p class="small" style="margin-top:var(--s-2)">%s</p>
    <p class="small" style="margin-top:var(--s-4);font-weight:560">Læs →</p>
  </a>""" % (href, (i % 3) * 60, title, desc) for i, (href, title, desc, _, _) in enumerate(ALL_GUIDES))

crumb_html, crumb_ld = breadcrumbs([("Forside", "index.html"), ("Guides", "guides/index.html")])
page("guides/index.html", "Guides om Google-anmeldelser og anmeldelseskort — {brand}",
     "Guides om Google-anmeldelser: sådan får du flere anmeldelser, finder dit anmeldelseslink, beder kunden om en anmeldelse, og hvilke regler der gælder.",
     with_crumbs(hero("Guides", "Guides om Google-anmeldelser",
          "Kort og konkret om hvordan du får flere Google-anmeldelser — og hvilke regler der gælder. Gratis, uanset om du køber noget af os."), crumb_html) + """
<section class="section--tight"><div class="wrap"><div class="grid grid-3">%s</div></div></section>""" % guide_cards,
     depth=1, jsonld=graph(crumb_ld))

for href, title, desc, seo_title, body in ALL_GUIDES:
    path = "guides/" + href
    crumb_html, crumb_ld = breadcrumbs([("Forside", "index.html"), ("Guides", "guides/index.html"), (title, path)])
    related = [g for g in ALL_GUIDES if g[0] != href][:3]
    rel = "".join("""
      <a class="card card--lift" href="%s">
        <h3 class="h3" style="font-size:1.05rem">%s</h3>
        <p class="small" style="margin-top:var(--s-2)">%s</p>
      </a>""" % (g[0], g[1], g[2]) for g in related)
    article = {"@type": "Article", "headline": seo_title, "description": desc,
               "inLanguage": "da-DK", "url": BASE_URL + clean_path(path),
               "image": BASE_URL + "/assets/og.png",
               "author": {"@type": "Organization", "name": BRAND_NAME, "url": BASE_URL},
               "publisher": {"@type": "Organization", "name": BRAND_NAME, "logo": {"@type": "ImageObject", "url": BASE_URL + "/assets/img/logo-512.png"}},
               "dateModified": "2026-11-15"}
    page(path, seo_title + " — {brand}", desc,
         with_crumbs(hero("Guide", title, desc), crumb_html) + """
<section class="section--tight">
  <div class="wrap stack-8"><div class="prose" data-reveal>%s</div>
    %s
    <div class="stack-6">
      <h2 class="h3">Læs også</h2>
      <div class="grid grid-3">%s</div>
    </div>
  </div>
</section>""" % (body, CTA_BOX, rel), depth=1, jsonld=graph(crumb_ld, article))


# ================================================================ BRANCHER
def branch_card(b, i=0):
    return """
      <a class="card card--lift" href="/brancher/%s" data-reveal="%d">
        <span class="eyebrow">%s</span>
        <h3 style="margin-top:var(--s-3)">Anmeldelseskort til %s</h3>
        <p class="small" style="margin-top:var(--s-2)">%s</p>
        <p class="small" style="margin-top:var(--s-4);font-weight:560">Se hvordan →</p>
      </a>""" % (b["slug"], (i % 3) * 60, b["nav"], b["nav"].lower(), b["who"])

crumb_html, crumb_ld = breadcrumbs([("Forside", "index.html"), ("Brancher", "brancher/index.html")])
page("brancher/index.html", "Anmeldelseskort til din branche — {brand}",
     "Anmeldelseskort til frisører, restauranter, caféer, butikker, håndværkere og klinikker. Se hvor kortet skal ligge, og hvad du skal sige, i netop din branche.",
     with_crumbs(hero("Brancher", "Anmeldelseskort til din branche",
          "Kortet er det samme. Det, der afgør, om det bliver brugt, er hvor det ligger, og hvornår det bliver nævnt — og det er forskelligt fra en salon til en restaurant til en håndværker."), crumb_html) + """
<section class="section--tight"><div class="wrap stack-8"><div class="grid grid-3">%s</div>%s</div></section>""" % (
         "".join(branch_card(b, i) for i, b in enumerate(BRANCHER)), CTA_BOX),
     depth=1, jsonld=graph(crumb_ld))

for b in BRANCHER:
    path = "brancher/%s.html" % b["slug"]
    crumb_html, crumb_ld = breadcrumbs([("Forside", "index.html"), ("Brancher", "brancher/index.html"), (b["nav"], path)])
    secs = "".join("<h2>%s</h2>\n%s\n" % (h, body) for h, body in b["sections"])
    others = "".join(branch_card(o, i) for i, o in enumerate([o for o in BRANCHER if o is not b][:3]))
    faq_ld = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": " ".join(a)}} for q, a in b["faq"]]}
    service = {"@type": "Product", "name": "Anmeldelseskort", "url": BASE_URL + "/anmeldelseskort",
               "image": BASE_URL + "/assets/img/card-front.webp",
               "description": fill(b["desc"]), "brand": {"@type": "Brand", "name": BRAND_NAME},
               "offers": {"@type": "AggregateOffer", "priceCurrency": "DKK", "lowPrice": str(TIERS[-1][1]),
                          "highPrice": str(P1), "offerCount": str(len(TIERS)), "availability": "https://schema.org/InStock"}}
    body = with_crumbs(hero("Til " + b["nav"].lower(), b["h1"], b["lede"],
        '<a class="btn btn--lg" href="/anmeldelseskort#bestil">Bestil — fra %d kr</a><a class="btn btn--ghost btn--lg" href="/saadan-virker-det">Sådan virker det</a>' % P1,
        "Til " + b["who"].lower().replace("vvs'ere", "VVS'ere")), crumb_html) + """
<section class="section--tight" style="padding-top:0">
  <div class="wrap">
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%%,20rem),1fr));gap:var(--s-12);align-items:start">
      <div class="prose" data-reveal>%s</div>
      <div class="stack-6" data-reveal="60" style="position:sticky;top:6rem">
        <div class="photo photo--card">
          <img src="/assets/img/card-front.webp?v=3" width="1200" height="1200" alt="Anmeldelseskort til %s — hvid side med Google-logo og fem stjerner" loading="lazy">
        </div>
        <ul class="ticks small" style="list-style:none;padding:0;display:grid;gap:var(--s-2)">
          <li>%s Tryk eller scan — virker på alle telefoner</li>
          <li>%s Ingen app, intet abonnement</li>
          <li>%s Vi programmerer kortet gratis</li>
          <li>%s Fra %d kr · ned til %d kr ved større antal</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="wrap">
    <div class="stack-8" style="max-width:46rem;margin-inline:auto">
      <div class="stack" data-reveal><span class="eyebrow">Spørgsmål</span><h2 class="h2">Det spørger %s ofte om</h2></div>
      <div data-reveal="60">%s</div>
    </div>
  </div>
</section>
<section class="section--tight">
  <div class="wrap stack-8">%s
    <div class="stack-6"><h2 class="h3">Andre brancher</h2><div class="grid grid-3">%s</div></div>
  </div>
</section>""" % (secs, b["nav"].lower(), CHECK, CHECK, CHECK, CHECK, P1, TIERS[-1][1],
                 b["nav"].lower(), acc(b["faq"]), CTA_BOX, others)
    page(path, fill(b["title"]) + " — {brand}", fill(b["desc"]), body, depth=1,
         jsonld=graph(crumb_ld, faq_ld, service))


# ================================================================ JURA
handels = hero("Betingelser", "Handelsbetingelser",
               "Gældende for alle køb på dette website.") + """
<section class="section--tight">
  <div class="wrap"><div class="prose small" data-reveal>
    <h2>1. Virksomhedsoplysninger</h2>
    <p><span data-brand>Firmanavn</span><br>CVR <span data-cvr>—</span><br>Danmark<br>E-mail: <a data-email href="#">support@…</a></p>

    <h2>2. Priser</h2>
    <p>Alle priser er angivet i danske kroner og inklusive 25 % moms. Der tages forbehold for prisfejl, udsolgte varer og afgiftsændringer.</p>

    <h2>3. Betaling</h2>
    <p>Vi modtager Dankort, Visa, Mastercard, MobilePay, Apple Pay, Google Pay og Klarna. Beløbet trækkes når varen afsendes.</p>
    <p>Ved ordrer fra 250 stk. tilbyder vi betaling med faktura, 14 dage netto, efter forudgående aftale.</p>

    <h2>4. Levering</h2>
    <p>Vi afsender 1–2 hverdage efter modtaget bestilling. Derfra er der typisk 1–3 hverdage.</p>
    <p><strong>Levering til pakkeshop er gratis</strong>, uanset ordrens størrelse. Du vælger selv pakkeshop ved betaling. Vi bruger GLS, DAO, PostNord og Bring, og udbuddet af pakkeshops afhænger af din adresse.</p>
    <p><strong>Hjemmelevering koster 49 kr</strong> og sker på hverdage.</p>
    <p>Vi leverer til adresser i Danmark. Skal du have leveret til Færøerne eller Grønland, så skriv til os først — der gælder andre regler og priser.</p>

    <h2>5. Fortrydelsesret</h2>
    <p>Du har 14 dages fortrydelsesret fra den dag du modtager varen. Se den fulde vejledning under <a href="fortrydelsesret.html">Fortrydelsesret</a>, hvor du også finder standardfortrydelsesformularen.</p>
    <p>Fortrydelsesretten gælder ikke varer der er fremstillet efter dine specifikationer eller har fået et tydeligt personligt præg — for eksempel kort trykt med dit eget logo.</p>

    <h2>6. Reklamationsret</h2>
    <p>Der er 2 års reklamationsret efter købelovens regler. Er der en mangel ved varen, kan du få den repareret, ombyttet, pengene tilbage eller afslag i prisen, afhængigt af den konkrete situation.</p>
    <p>Reklamation over fejl skal ske inden for rimelig tid efter at du har opdaget dem. Reklamerer du inden for to måneder, er det altid rettidigt.</p>
    <p>Er reklamationen berettiget, refunderer vi dine rimelige fragtomkostninger. Send varen til den adresse vi oplyser — pakker sendt på efterkrav modtages ikke.</p>

    <h2>7. Klageadgang</h2>
    <p>Er du ikke tilfreds, så kontakt os først på <a data-email href="#">support@…</a>.</p>
    <p>Kan vi ikke finde en løsning, kan du indgive en klage til:<br>
    Mæglingsteamet for Forbrugerklager, Nævnenes Hus, Toldboden 2, 8800 Viborg —
    <a href="https://naevneneshus.dk" target="_blank" rel="noopener">naevneneshus.dk</a></p>

    <h2>8. Ansvar</h2>
    <p>Kortet indeholder et link til en side du selv vælger. Vi er ikke ansvarlige for ændringer på tredjeparters platforme, herunder hvis Google ændrer eller fjerner adressen til din anmeldelsesside.</p>
    <p>Du er selv ansvarlig for at overholde de regler der gælder for indsamling af anmeldelser på den platform du peger kortet mod.</p>

    <h2>9. Ændringer</h2>
    <p>Vi kan ændre disse betingelser. Den version der gjaldt på købstidspunktet, er den der gælder for dit køb.</p>
    <p class="tiny">Senest opdateret <span data-year>2026</span>.</p>
  </div></div>
</section>"""

page("handelsbetingelser.html", "Handelsbetingelser — {brand}",
     "Handelsbetingelser: priser, betaling, levering, fortrydelsesret, reklamationsret og klageadgang.", handels)

fortryd = hero("Fortrydelsesret", "14 dages fortrydelsesret",
               "Du kan fortryde dit køb i 14 dage. Her er reglerne og formularen.") + """
<section class="section--tight">
  <div class="wrap"><div class="prose small" data-reveal>
    <h2>Fristen</h2>
    <p>Du har 14 dage til at fortryde dit køb, regnet fra den dag du — eller en anden du har valgt — får varen fysisk i hænde.</p>
    <p>Består ordren af flere varer, der leveres hver for sig, løber fristen fra den dag du modtager den sidste vare.</p>
    <p>Falder fristens sidste dag på en helligdag, lørdag, grundlovsdag, juleaftensdag eller nytårsaftensdag, forlænges fristen til den følgende hverdag.</p>

    <h2>Sådan fortryder du</h2>
    <p>Send os en utvetydig besked om at du fortryder, inden fristen udløber — en e-mail til <a data-email href="#">support@…</a> er nok. Du kan bruge standardformularen nedenfor, men det er ikke et krav.</p>
    <p>Det er ikke nok blot at nægte modtagelse uden samtidig at give os besked.</p>

    <h2>Returnering</h2>
    <p>Du skal sende varen retur uden unødig forsinkelse og senest 14 dage efter du har meddelt os at du fortryder.</p>
    <p><strong>Du betaler selv for returfragten.</strong> Du bærer risikoen for varen fra det tidspunkt den er leveret til dig — så pak den forsvarligt og gem kvitteringen for forsendelsen.</p>
    <p>Vi modtager ikke pakker sendt på efterkrav eller uden omdeling.</p>

    <h2>Varens stand</h2>
    <p>Du må gerne undersøge varen, som du ville kunne i en fysisk butik. Har du brugt den på en måde der går ud over det, hæfter du for eventuel værdiforringelse.</p>
    <p>Har du programmeret kortet, kan det programmeres om — det i sig selv forringer ikke værdien.</p>

    <h2>Tilbagebetaling</h2>
    <p>Vi refunderer beløbet — inklusive den billigste standardfragt vi tilbød ved købet — senest 14 dage efter vi har modtaget din besked om fortrydelse.</p>
    <p>Vi kan dog tilbageholde beløbet, indtil vi har modtaget varen retur, eller du har dokumenteret at den er sendt.</p>
    <p>Vi tilbagefører til samme betalingsmiddel som du brugte ved købet, medmindre vi aftaler andet.</p>

    <h2>Undtagelser</h2>
    <p>Fortrydelsesretten gælder ikke varer fremstillet efter dine specifikationer eller med et tydeligt personligt præg — for eksempel kort trykt med dit eget logo eller design.</p>

    <h2>Standardfortrydelsesformular</h2>
    <div class="note">
      <p><em>Udfyld og returnér kun denne formular, hvis du ønsker at fortryde aftalen.</em></p>
      <p>Til: <span data-brand>Firmanavn</span>, CVR <span data-cvr>—</span>, <a data-email href="#">support@…</a></p>
      <p>Jeg meddeler herved, at jeg ønsker at gøre fortrydelsesretten gældende i forbindelse med min købsaftale om følgende varer:</p>
      <p>_______________________________________</p>
      <p>Bestilt den: ____________  Modtaget den: ____________</p>
      <p>Forbrugerens navn: _______________________________________</p>
      <p>Forbrugerens adresse: _______________________________________</p>
      <p>Forbrugerens underskrift (kun hvis formularens indhold meddeles på papir): ____________________</p>
      <p>Dato: ____________</p>
    </div>
  </div></div>
</section>"""

page("fortrydelsesret.html", "Fortrydelsesret — {brand}",
     "14 dages fortrydelsesret: frist, returnering, tilbagebetaling og standardfortrydelsesformular.", fortryd)

privat = hero("Privatliv", "Privatlivspolitik",
              "Hvilke oplysninger vi behandler, hvorfor, og hvad du kan kræve.") + """
<section class="section--tight">
  <div class="wrap"><div class="prose small" data-reveal>
    <h2>Dataansvarlig</h2>
    <p><span data-brand>Firmanavn</span>, CVR <span data-cvr>—</span>, Danmark. Kontakt: <a data-email href="#">support@…</a></p>

    <h2>Hvad vi behandler</h2>
    <p>Når du bestiller, behandler vi navn, adresse, e-mail, telefonnummer og oplysninger om din ordre. Ved erhvervskøb desuden firmanavn og CVR.</p>
    <p>Sender du os linket til din Google-side, så vi kan programmere kortet, gemmer vi det sammen med ordren.</p>
    <p>Vi ser og gemmer ikke dine kortoplysninger. Betalingen håndteres af vores betalingsudbyder.</p>

    <h2>Hvorfor</h2>
    <p>For at opfylde købsaftalen, for at kunne håndtere reklamationer og fortrydelse, og fordi bogføringsloven kræver at vi gemmer regnskabsmateriale.</p>

    <h2>Hvor længe</h2>
    <p>Ordreoplysninger gemmes i 5 år efter udløbet af det regnskabsår oplysningerne vedrører, sådan som bogføringsloven kræver. Korrespondance der ikke er regnskabsmateriale, sletter vi når den ikke længere er relevant.</p>

    <h2>Hvem vi deler med</h2>
    <p>Kun dem der er nødvendige for at levere: fragtfirma, betalingsudbyder, og de systemer vi bruger til webshop, e-mail og bogføring. De behandler oplysningerne på vores vegne efter databehandleraftaler.</p>
    <p>Vi sælger ikke dine oplysninger.</p>

    <h2>Cookies</h2>
    <p>Vi bruger de cookies der er nødvendige for at siden og indkøbskurven fungerer. Accepterer du markedsføringscookies, indlæser vi Meta-pixel, som deler oplysninger om dit besøg (fx hvilke sider du så, og om du gik til kassen) med Meta Platforms Ireland Ltd., så vi kan måle vores annoncer. Meta er selvstændig dataansvarlig for den del. Afviser du, sker det ikke, og du kan altid trække samtykket tilbage under <a href="#" data-consent-reopen>Cookieindstillinger</a>. Se <a href="/cookiepolitik">cookiepolitikken</a>.</p>
    <h2>Besøgsstatistik</h2>
    <p>For at se hvor mange der besøger siden, og hvilke sider der bliver brugt, bruger vi Vercel Web Analytics fra vores hostingudbyder Vercel Inc. Den sætter ingen cookies og gemmer intet i din browser. Vi får kun samlede tal (fx antal besøg, sider, land, enhedstype og hvilken side du kom fra). Din IP-adresse gemmes ikke, og besøg kan ikke føres tilbage til dig som person. Grundlaget er vores legitime interesse i at forbedre siden (GDPR art. 6, stk. 1, litra f).</p>

    <h2>Dine rettigheder</h2>
    <p>Du kan bede om indsigt i de oplysninger vi har om dig, få rettet forkerte oplysninger, få slettet oplysninger, få begrænset behandlingen, gøre indsigelse, og få udleveret dine oplysninger i et almindeligt format.</p>
    <p>Skriv til <a data-email href="#">support@…</a>, så vender vi tilbage hurtigst muligt.</p>
    <p>Er du utilfreds med måden vi behandler dine oplysninger på, kan du klage til Datatilsynet, Carl Jacobsens Vej 35, 2500 Valby — <a href="https://datatilsynet.dk" target="_blank" rel="noopener">datatilsynet.dk</a></p>
    <p class="tiny">Senest opdateret <span data-year>2026</span>.</p>
  </div></div>
</section>"""

page("privatlivspolitik.html", "Privatlivspolitik — {brand}",
     "Hvilke personoplysninger vi behandler, hvorfor, hvor længe, og hvilke rettigheder du har.", privat)


cookiepol = hero("Cookies", "Cookiepolitik",
    "Hvilke cookies vi bruger, hvorfor, og hvordan du ændrer dit valg.") + """
<section class="section--tight">
  <div class="wrap"><div class="prose small" data-reveal>
    <h2>Hvad en cookie er</h2>
    <p>En cookie er en lille tekstfil, som gemmes i din browser. Den bruges til at få en hjemmeside til at fungere, og kan også bruges til at måle hvordan siden bliver brugt, eller til markedsføring.</p>

    <h2>Hvad vi bruger</h2>
    <p><strong>Nødvendigt (altid):</strong> Vi gemmer dit svar på cookiebanneret lokalt i din browser, så vi ikke spørger igen hver gang du åbner en side. Det ligger i browserens <em>localStorage</em> under navnet <code>samtykke-v1</code>, sendes aldrig til os, og kan slettes når som helst.</p>
    <p><strong>Markedsføring (kun hvis du trykker accepter):</strong> Vi bruger Meta-pixel fra Meta Platforms Ireland Ltd. til at måle, om vores annoncer på Facebook og Instagram virker — for eksempel at nogen kom fra en annonce, så produktsiden eller gik videre til kassen. Pixlen sætter cookien <code>_fbp</code> (gemmes i 90 dage) og kan læse Metas egne cookies, hvis du er logget ind hos Meta. Oplysningerne behandles af Meta efter <a href="https://www.facebook.com/privacy/policy" target="_blank" rel="noopener">Metas privatlivspolitik</a> og kan overføres til lande uden for EU.</p>
    <p>Trykker du afvis — eller lader være med at svare — bliver pixlen aldrig indlæst.</p>
    <p><strong>Besøgsstatistik (uden cookies):</strong> Vi tæller besøg med Vercel Web Analytics. Den sætter ingen cookies og gemmer intet i din browser, så den kræver ikke samtykke. Vi ser kun samlede tal, og din IP-adresse gemmes ikke.</p>

    <h2>Dit valg</h2>
    <p>Du kan altid ombestemme dig. Klik <a href="#" data-consent-reopen>Cookieindstillinger</a>, så kommer banneret frem igen, og du kan vælge forfra.</p>
    <p>Du kan også slette cookies og lokale data direkte i din browsers indstillinger.</p>

    <h2>Samtykke</h2>
    <p>Efter de danske cookieregler må vi kun sætte cookies der ikke er strengt nødvendige, hvis du har givet samtykke først. Derfor er der ingen forudkrydsede felter, og <em>Afvis</em> er lige så let at trykke på som <em>Accepter</em>.</p>

    <h2>Kontakt</h2>
    <p>Spørgsmål til det her? Skriv til <a data-email href="#">support@…</a>.</p>
    <p class="tiny">Senest opdateret <span data-year>2026</span>.</p>
  </div></div>
</section>"""

page("cookiepolitik.html", "Cookiepolitik — {brand}",
     "Hvilke cookies dette website bruger, hvorfor, og hvordan du ændrer dit samtykke.", cookiepol)


print("Byggede %d sider:" % len(PAGES))
for p in PAGES:
    print("  " + p)


# ================================================================ SEO + 404
BASE = "https://reviewpartneren.dk"
urls = "".join(
    '  <url><loc>%s%s</loc></url>\n' % (BASE, clean_path(p))
    for p in PAGES if p != "404.html")
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls,
    encoding="utf-8")

(ROOT / "robots.txt").write_text(
    "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE, encoding="utf-8")

page("404.html", "Siden findes ikke — {brand}", "Siden kunne ikke findes.",
     hero("404", "Den side findes ikke",
          "Linket er enten forkert, eller også er siden flyttet. Prøv en af disse i stedet.",
          '<a class="btn btn--lg" href="anmeldelseskort.html">Se kortet</a>'
          '<a class="btn btn--ghost btn--lg" href="index.html">Til forsiden</a>'))

print("\nsitemap.xml (%d urls) + robots.txt + 404.html" % len(PAGES))
