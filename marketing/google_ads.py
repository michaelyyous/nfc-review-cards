#!/usr/bin/env python3
"""Google Ads search campaign for Reviewpartneren — single source of truth.
Run it to check every text against Google's length limits."""

H_MAX, D_MAX, PATH_MAX, SL_MAX, SL_D_MAX, CO_MAX = 30, 90, 15, 25, 35, 25

GROUPS = {
  "Google Review-kort": {
    "url": "https://reviewpartneren.dk/anmeldelseskort", "paths": ["google-review", "kort"],
    "keywords": ['[google review kort]', '"google review kort"', '[google review card]', '"google review card"',
                 '"google review nfc"', '[google anmeldelseskort]', '"google anmeldelse kort"', '"review kort google"',
                 '"google review stand"', '"google review tag"'],
  },
  "Anmeldelseskort NFC": {
    "url": "https://reviewpartneren.dk/anmeldelseskort", "paths": ["nfc", "anmeldelseskort"],
    "keywords": ['[anmeldelseskort]', '"nfc anmeldelseskort"', '"nfc kort anmeldelser"', '"nfc google anmeldelser"',
                 '"tap kort anmeldelser"', '"nfc review kort"', '"anmeldelses kort"'],
  },
  "Flere Google-anmeldelser": {
    "url": "https://reviewpartneren.dk/", "paths": ["anmeldelser"],
    "keywords": ['"flere google anmeldelser"', '"få flere anmeldelser på google"', '"flere anmeldelser google"',
                 '"få flere google anmeldelser"'],
  },
  "Forhandler og engros": {
    "url": "https://reviewpartneren.dk/forhandler", "paths": ["forhandler"],
    "keywords": ['"google review kort engros"', '"nfc kort engros"', '"google review kort forhandler"',
                 '"sælge google review kort"', '"nfc kort billigt"'],
  },
}

NEGATIVES = ["gratis", "job", "maps", "rutevejledning", "kort over", "danmarkskort", "vejkort",
             "skriv", "skrive", "hvordan anmelder", "slet", "slette", "fjern", "fjerne", "svar på",
             "køb anmeldelser", "købe anmeldelser", "falske", "trustpilot", "kreditkort", "visakort",
             "rejsekort", "gavekort", "sundhedskort", "nfc ring", "nfc reader", "nfc læser", "nfc tag tomme",
             "diy", "aliexpress", "temu", "wish", "app", "download"]

HEADLINES = [
  "Google Review-kort med NFC", "Fra 189 kr – intet abonnement", "Kunden tapper og anmelder",
  "Gratis programmering", "Sendes 1–2 hverdage fra DK", "Virker på iPhone og Android",
  "Mængderabat ned til 49 kr", "NFC og QR-kode på ét kort", "Ingen app. Ingen binding.",
  "Fri fragt til pakkeshop", "Betal med MobilePay", "NFC-anmeldelseskort",
  "Til butikker og saloner", "Bestil Google Review-kort", "Hvid og sort side",
]
DESCRIPTIONS = [
  "Kunden holder telefonen mod kortet, og jeres Google-anmeldelsesside åbner. Ingen app.",
  "Vi programmerer kortet gratis med jeres link. Sendes fra Danmark på 1–2 hverdage.",
  "Fra 189 kr – ned til 49 kr pr. kort ved større antal. Intet abonnement, betal én gang.",
  "NFC-chip og QR-kode, så det virker på alle telefoner. 14 dages fortrydelsesret.",
]
RESELLER_HEADLINES = [
  "Google Review-kort engros", "Forhandlerpris fra 250 stk.", "Køb ind til fast pris",
  "Ingen binding", "Eget tryk fra 250 stk.", "Betal med faktura", "NFC-anmeldelseskort",
  "Sendes fra Danmark",
]
RESELLER_DESCRIPTIONS = [
  "Køb Google Review-kort ind til fast pris og sælg dem videre til lokale virksomheder.",
  "Fra 250 stk.: forhandlerpris, eget tryk og faktura. Ingen løfter om indtjening.",
]
SITELINKS = [
  ("Bestil kort", "Vælg antal og betal sikkert", "MobilePay, kort eller Klarna", "https://reviewpartneren.dk/bestil"),
  ("Mængderabat", "Ned til 49 kr pr. kort", "Prisen falder med antallet", "https://reviewpartneren.dk/maengderabat"),
  ("Sådan virker det", "Tap, og siden åbner", "NFC-chip og QR-kode", "https://reviewpartneren.dk/saadan-virker-det"),
  ("Bliv forhandler", "Forhandlerpris fra 250 stk.", "Eget tryk og faktura", "https://reviewpartneren.dk/forhandler"),
]
CALLOUTS = ["Intet abonnement", "Gratis programmering", "Fri fragt til pakkeshop", "Sendes fra Danmark",
            "14 dages fortrydelsesret", "MobilePay og Klarna"]
PRICES = [("1 kort", "Prøv et enkelt kort", "189 kr"), ("10 kort", "129 kr pr. kort", "1.290 kr"),
          ("100 kort", "79 kr pr. kort", "7.900 kr")]

def check(label, items, limit):
    bad = 0
    for t in items:
        n = len(t)
        flag = "OK " if n <= limit else "FOR LANG"
        if n > limit: bad += 1
        print(f"  {flag} {n:>2}/{limit}  {t}")
    return bad

if __name__ == "__main__":
    bad = 0
    print("Overskrifter"); bad += check("h", HEADLINES, H_MAX)
    print("Beskrivelser"); bad += check("d", DESCRIPTIONS, D_MAX)
    print("Forhandler-overskrifter"); bad += check("h", RESELLER_HEADLINES, H_MAX)
    print("Forhandler-beskrivelser"); bad += check("d", RESELLER_DESCRIPTIONS, D_MAX)
    print("Sitelinks"); bad += check("s", [s[0] for s in SITELINKS], SL_MAX)
    bad += check("s", [x for s in SITELINKS for x in s[1:3]], SL_D_MAX)
    print("Callouts"); bad += check("c", CALLOUTS, CO_MAX)
    print("Prisaktiver"); bad += check("p", [x for p in PRICES for x in p[:2]], 25)
    print("Stier"); bad += check("p", [p for g in GROUPS.values() for p in g["paths"]], PATH_MAX)
    print("\nSøgeord:", sum(len(g["keywords"]) for g in GROUPS.values()), "· negative:", len(NEGATIVES))
    print("FEJL:", bad)
