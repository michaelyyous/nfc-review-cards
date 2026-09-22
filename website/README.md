# Websitet

Statisk site. Ingen framework, ingen build-værktøjer at installere. Kun Python.

## Sådan bygger du

```bash
cd website
python3 build.py
```

Genererer alle 16 HTML-filer. Kør det igen hver gang du har ændret noget i `build.py`.

## Sådan ser du det lokalt

```bash
python3 -m http.server 4175 --directory website
```

Åbn så http://localhost:4175

## 🔴 Sæt firmanavnet ind

Alt navnestof styres ét sted: **`assets/app.js`**, øverst i filen.

```js
const BRAND = {
  name: '',              // ← Sæt navnet her
  placeholder: 'Firmanavn',
  cvr: '',               // ← CVR-nummer
  email: '',             // ← support-mail
  city: 'Danmark',
};
```

Så længe `name` er tom, vises "Firmanavn" **markeret med gul** overalt på sitet, så du kan se hvor det står. I det øjeblik du udfylder feltet, forsvinder markeringen og navnet slår igennem på alle sider på én gang. Du skal ikke bygge om — det sker i browseren.

Det samme gælder CVR og e-mail. De står i handelsbetingelser, privatlivspolitik, fortrydelsesformular, kontaktside og footer, og udfyldes alle sammen herfra.

## Sådan ændrer du priser

Øverst i `build.py`:

```python
TIERS = [
    (1, 189), (3, 169), (5, 155), (10, 129), (25, 109),
    (50, 95), (100, 79), (250, 59), (500, 49),
]
```

Priserne er **inkl. moms** (lovkrav ved salg til forbrugere). Ændrer du dem, opdateres pristrappen, beregneren, produktsiden, forsiden og forhandlersiden automatisk. Kør `python3 build.py` bagefter.

## Sider

| Fil | Indhold |
|---|---|
| `index.html` | Forside |
| `anmeldelseskort.html` | Produktside med pristrappe |
| `saadan-virker-det.html` | Sådan virker NFC, trin for trin |
| `saet-det-op.html` | Vejledning til selv at programmere kort |
| `maengderabat.html` | Pristrappe + priskalkulator |
| `forhandler.html` | Forhandlervilkår |
| `faq.html` | 12 spørgsmål og svar |
| `om-os.html` | Om virksomheden |
| `kontakt.html` | Kontakt og klageadgang |
| `guides/` | Oversigt + 3 guides |
| `handelsbetingelser.html` | Handelsbetingelser |
| `fortrydelsesret.html` | Fortrydelsesret + standardformular |
| `privatlivspolitik.html` | Privatlivspolitik |

## Shopify

Shopify er kasseapparat, ikke butik. Sitet bliver hvor det er; `/bestil` afleverer kurven videre.

Udfyld to felter i `assets/app.js`:

```js
const SHOPIFY = {
  domain: '',        // dit-shop.myshopify.com
  variantId: '',     // tallet sidst i variantens URL i Shopify-admin
};
```

Så skifter bestillingsformularen automatisk fra mail-flow til rigtig checkout. Den bygger et cart-permalink:

```
/cart/VARIANT:ANTAL?attributes[Google-link]=…&attributes[Levering]=…
```

Google-linket, programmeringsvalget, virksomhed, CVR og leveringsmetode følger med som cart attributes, så de lander på ordren i Shopify.

**Mængderabatten sættes op i Shopify** under *Rabatter → Automatisk rabat* — ikke som separate varianter. Pristrappen i `build.py` skal matche dem, ellers viser sitet én pris og checkout en anden.

## Cookies

Banneret er bygget efter reglen, ikke efter branchekutymen: **Afvis og Accepter er præcis samme størrelse og vægt** (målt 179×38 begge), intet ikke-nødvendigt indlæses før samtykke, og valget kan trækkes tilbage via *Cookieindstillinger* i footeren.

Sitet sætter i dag **ingen cookies**. Det eneste der gemmes er selve samtykkevalget i `localStorage` under `samtykke-v1`.

Tilføjer du statistik eller et Meta-pixel, skal loaderen ind i `runTracking()` i `app.js` — den kaldes kun efter et aktivt accepter. Husk at opdatere `cookiepolitik.html` samtidig, for den beskriver lige nu korrekt at der intet er.

## 🔴 Skal gøres før lancering

**Venter kun på tre ting:**

- [ ] **Firmanavn, CVR og support-mail** i `assets/app.js`
- [ ] **Domæne** — peges på Vercel-projektet
- [ ] **Shopify `domain` + `variantId`** i `assets/app.js`

**Efter launch, men med frist:**

- [ ] **Producentansvar registreret** (elektronik + emballage) — **14 dages frist før første salg**. Se `../research/TJEKLISTE-OPSTART.md`
- [ ] **CVR + momsregistrering** — senest 8 dage før du starter aktiviteten
- [ ] **GPSR-oplysninger på produktsiden**: producentens navn, postadresse og e-mail, plus dine egne som ansvarlig importør. Krav ved fjernsalg, skal stå på dansk. Kan først udfyldes når leverandøren er endeligt valgt.

**Når du har noget at sætte ind:**

- [ ] **Kundeudtalelser på forsiden.** Sektionen er bygget færdig men står tom med vilje. Rigtige citater fra rigtige kunder, med deres accept. Opdigtede anmeldelser er forbudt efter markedsføringslovens bilag 1 nr. 23c — per se-overtrædelse, ingen skade skal bevises.
- [ ] **Produktfotos** — `.photo`-slots står klar i "hvorfor"-sektionen og på det andet produktkort
- [ ] Tjek at leveringstider passer med det du faktisk kan holde

## 3D-kortet

Kortet i hero'en er et rigtigt 3D-objekt, ikke et billede. To sider — hvid mat forside og sort NFC-bagside, som på det fysiske kort — plus fire kantstrimler der giver det tykkelse. Du kan trække det hele vejen rundt med musen, fingeren eller piletasterne.

Bevægelsen kører på ægte fjedre i `app.js`, ikke CSS-transitions. En transition kan ikke gribes og vendes midt i flugten — den er hele grunden til at gesture-drevet UI føles dødt.

`Spring`-klassen er parametriseret som Apple gør det, ikke som masse/stivhed/dæmpning:

| | Betydning |
|---|---|
| **damping** `1.0` | kritisk dæmpet, ingen overshoot — til flytning |
| **damping** `0.8` | let overshoot — kun når bevægelsen bar momentum |
| **response** | sekunder til målet. **Ikke** en varighed — en fjeder har ingen fast varighed |

Kortet bruger `damping 1.0 / response 0.4` på hældningen (ren repositionering) og `damping 0.8 / response 0.4` på drejningen (momentumbåret). To uafhængige fjedre — én 2D-fjeder ville desynkronisere når akserne har forskellig hastighed.

Interaktionen følger hele kæden:

- Feedback på **pointer-down**, ikke ved slip
- **~10px hysterese** før et træk bliver til et træk
- **1:1-sporing** via `setPointerCapture`, så den følger med uden for elementet
- **Hastighedshistorik** over ~90 ms, ikke én frame — et enkelt delta er støj
- **Momentum projiceres frem** med Apples eksponentielle henfald, `(v/1000)·d/(1−d)`, `d = 0.998` — og *derefter* vælges nærmeste side. Snap fra sluppositionen ville ignorere kastet helt
- **Hastigheden overleveres** til fjederen, så der ikke er en søm mellem træk og animation
- **Afbrydelig** — griber du fat midt i flugten, re-targeter den til den aktuelle værdi. Målt spring ved greb: 0,000°
- **Rubber-banding** på hældningen i stedet for et hårdt stop
- **Haptik** på samme frame som det visuelle snap, kun på touch

Ved `prefers-reduced-motion` slås idle-svajet fra og kortet står stille.

**Testet numerisk** (`damping 1.0` → 0 % overshoot, settle 0,80 s · `damping 0.8` → overshoot, settle 0,42 s · projektion 600°/s → 299° → snapper til 360° · velocity-overlevering giver 21,1° på første frame mod 12,3° uden · greb midt i flugten springer 0,000°).

**Bemærk:** browsere suspenderer `requestAnimationFrame` i skjulte faner. Ser kortet frosset ud i en baggrundsfane, er det forventet — det starter igen når fanen bliver synlig.

## Layout

Sidens struktur følger chippy.dk, med værdier målt direkte i deres CSS 26-08-2026:

| | Værdi |
|---|---|
| Sidebaggrund | `rgb(244,244,242)` |
| H1 | 44px / vægt 600 / tracking −0,03em |
| H2 | 46px / vægt 700 / tracking −0,035em |
| Hero-blok | afrundet 30px, indrykket, nav ligger indeni |
| Nav-kapsel | `rgba(18,18,16,.42)`, radius 999px, 6px polstring |
| Nav-links | 8px 14px, 14px / vægt 500, `rgba(255,255,255,.82)` |
| Logo-pille | 10px 20px 10px 14px, radius 999px |
| Header-polstring | 18px lodret |
| Stat-kort | radius 22px, hvid 1px kant, grøn tone |

Sektionsrækkefølge: annoncebjælke → hero → Tallene bag → Ti sekunder ved disken → Glade kunder → produktkort → priser → trust-række → Spørgsmål → Guides → sticky bundbar.

Nav-kapslerne har `backdrop-filter` som chippy ikke har. Det er bevidst: kapslen ligger over et foto, og tekstlæsbarhed over en skiftende baggrund er præcis hvad vibrancy findes til.

Nav'en skifter først fra mørk til lys chrome når hero-blokken faktisk er scrollet forbi — ikke ved `scrollY > 8`. Ellers står der bleg tekst på mørk baggrund i hele hero'ens højde.

## Noter om indholdet

Der står ingen tal på sitet som ikke kan dokumenteres. Ingen "3× flere anmeldelser", ingen procenter, ingen påstande om resultater. Det er bevidst — markedsføringslovens § 13 kræver at du kan dokumentere faktiske oplysninger **på det tidspunkt du fremsætter dem**, og du har ingen data endnu.

Får du senere rigtige tal fra rigtige kunder, kan de sættes ind. Indtil da sælger sitet på hvad produktet **er**, ikke på hvad det påstås at gøre.

Forhandlersiden indeholder bevidst ingen indtjeningspåstande, intet henvisningsled og en tilbagekøbsgaranti. Se `../research/BRIEF.md` afsnit 8 for hvorfor.
