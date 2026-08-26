# NFC Google-Review Tags — Consolidated Research Brief
**Compiled 26 August 2026.** Sources: live TARIC query, Toldstyrelsen, retsinformation (official XML), Forbrugerombudsmanden, Google support policy pages, supplier listings, freight rate tables.

Flagged throughout: **[V]** = verified from primary source · **[U]** = unverified, needs checking before relying on it.

---

## 1. THE MARKET

> ⚠️ **Correction (26 Aug).** An earlier draft of this brief said stands were an open gap in Denmark because chippy.dk sells cards only. **That was wrong.** Chippy is one of eight vendors and not the leader. Four Danish vendors already sell stands.

**Denmark is already served — 8 vendors, 5 of them incorporated Danish companies with CVR, DK warehousing and 1–3 day delivery.**

| Vendor | Entity | Products | Subscription |
|---|---|---|---|
| **tapnfc.dk** ← leader | TapNFC ApS, CVR 44800438, Roskilde | Kort fra **149 kr**, **bordstander fra 199 kr**, pad fra 179 kr, komplet pakke 680 kr — all **ex. moms**. Eget logo +100 kr | None |
| **trustcard.dk** | bautz.dk, CVR 26806127, Kastrup | Bordskilt **389 kr**, brik 389 kr, visitkort 199 kr — ex. moms | Free QR tier as funnel |
| **taplink.dk** | taplink ApS, CVR 44791544, Aarhus | Reviewkort **399,95 kr incl. moms** | None |
| **tappii.dk** | CVR 45218880, Vejen | Keychains 149–179 kr; stander price didn't render | Free + paid Pro tier |
| **tapstar.dk** | No CVR published | Stand **399 kr**, card 199 kr | **99 kr/md** — only DK subscription |
| **badgeland.dk** | Badgeland A/S, CVR 33241658 | PVC L-skilt 120×140×50mm, NTAG215 — quote only | n/a |
| **chippy.dk** | CVR 46690257 | Cards only. 1=119 · 10=70 · 100=55 · 250=39 · 500=32 kr | None |
| **nfcw.dk** | NFC World B.V. (Dutch) | TikTok-kort 92,43 kr + **blank programmable cards with DIY instructions** | n/a |

**DK retail band: 199–399 kr ex. moms for a stand; 149–399 kr for a card.**

**DK is priced above the EU average**, which invites cross-border undercutting — both of these explicitly ship to Denmark:
- einfachbewertet.de — Aufsteller €39,90 (3 for €99, 5 for €155), logo +€50 once, **DK listed, 5–10 Werktage**
- TAPiTAG (IE) — €34,99, free tracked EU shipping 5–7 days, analytics dashboard included

Nordics: SmartBlipp (SE) 495 SEK · visittkortnorge.no (NO) 790/549/449 NOK at 1/3/5 units — **the clearest volume ladder in the Nordics** · suosittelukortit.fi (FI) €39,90.

Factory-to-DK-retail spread is roughly **10–40×**. The margin is brand, done-for-you programming and distribution — not the chip.

### What is genuinely uncontested
- **Paid media.** Verified in Google Ads Transparency Center (region DK): tapnfc runs **16 ads**; tappii, taplink, trustcard run **zero**. Verified in Meta Ad Library (country DK, active): `google anmeldelser NFC` → *"Ingen annoncer matcher dine søgekriterier"* — **zero Danish advertisers on Meta.**
- **Search intent nobody owns.** See §1b.
- **Recurring revenue.** "Ingen abonnement" is the category's dominant claim, so only tapstar (99 kr/md) and empfehlio (€8.99/mo) have durable revenue. The redirect layer in §5 is the natural hook for this.
- **No DK vendor publishes reseller terms.** Badgeland has an unpublished "Er du videreforhandler?" link. Either an opening or evidence the channel economics don't work.

---

## 1b. SEARCH DEMAND — half the obvious keyword list doesn't exist

Google Trends, google.dk, DuckDuckGo and Ahrefs were all blocked/gated. **Any monthly-volume figure quoted for these terms is an estimate, not a measurement.** What *was* measurable: Google's autocomplete API (hl=da, gl=dk), whose subtype flags distinguish real-query-log suggestions from generated ones.

| Term | Status |
|---|---|
| `google anmeldelse skilt` | ✅ **Real query — this is the term** |
| `google anmeldelser qr kode` | ✅ Real query — **QR out-searches NFC in Danish** |
| `nfc google review card` / `stand` | ✅ Real queries served to DK/Danish users — **Danes search the NFC angle in English, and no Danish vendor owns that intent** |
| `anmeldelsesskilt` | ❌ Does not appear. The `anmeldelses-` prefix is dominated by legal/regulatory senses (anmeldelsespligt, anmeldelsespligtige sygdomme) |
| `NFC anmeldelse`, `NFC skilt anmeldelser` | ❌ Generated variants only, no query-log backing |

Google does generate a Danish "Folk spørger også" cluster (*"Hvad er Google-anmeldelseskort?"*), confirming enough volume for a PAA box.

**No Danish forum discussion found** — nothing on amino.dk, r/dkbusiness or r/Denmark. Closest signal is an r/NFC post from a Barcelona user ~2 weeks ago asking where to source cheap cards to start reselling. The EU spread is happening; it hasn't reached DK.

---

## 2. SUPPLIERS

### Best-verified China options (Made-in-China.com, real tier tables)

| Supplier | Product | 100 | 500 | MOQ | Sample | Signal |
|---|---|---|---|---|---|---|
| **Chongqing Colorful** | Acrylic stand | $0.85 | $0.71 | 100 | $10 | Diamond 2023, 5.0/327 rev, **85% reorder**, 3–4 day production |
| **Chongqing Colorful** | PVC card | $0.50 | $0.40 | 100 | $10 | same |
| **Shenzhen Jianhe** | Acrylic stand, NTAG213 | — | $0.95 | 500 | $3 | Diamond 2023, 4.9, audited, 7–9 days |
| **Chengdu MIND IOT** | PVC card | — | $0.18 | 500 | — | Diamond since 2006, **EU Responsible Person in Düsseldorf** |
| **PUTIAN IDENTTAG** | PVC card | $0.10–0.30 | — | 100 | $0.50 | Diamond 2023, 5.0/58 rev |

⚠️ Alibaba.com itself was CAPTCHA-walled — Alibaba figures in the source research came from aggregators, not listing pages read directly. Verified/Gold badges were never confirmed. **Treat Alibaba supplier metadata as unconfirmed.**

⚠️ Alibaba's own buying guide: **PVC below $0.25 often signals counterfeit chips or poor print.**

### EU alternatives (faster, simpler, no customs)

| Supplier | Product | 500 | Shipping to DK |
|---|---|---|---|
| **ShopNFC (IT)** | Custom-print PVC card | **€1.25** ex-VAT | **Free, 6–10 working days** |
| **NFC21 (DE)** | PVC card NTAG213 | ~€1.90 ex-VAT | €5.50 flat, 3–5 days |
| **Seritag (UK)** | Pro Review Plate | €2.57 ex-VAT | ⚠️ No longer ships to most EU — email mail@seritag.com for larger orders |
| **Badgeland (DK)** | Google review card, NTAG215 | 6.82 kr flat, **no volume discount** | domestic, 5–7 hverdage |

---

## 3. LANDED COST

### Shipping mode — express wins decisively

| Mode | ~10 kg door-to-door | Time |
|---|---|---|
| **Express courier (DHL/FedEx)** | ~$90–150 | 2–5 days |
| Air freight | ~$280–580 | 8–14 days |
| Sea LCL | ~$625–1,290 | 30–45 days |

Air has a **45 kg minimum chargeable weight**. Sea LCL has a **1 CBM minimum plus ~$550–1,100 in flat fees that don't scale down**. Both are structurally wrong at 100–500 units.

DHL Zone 13 (Denmark) ex-Shenzhen: first 0.5 kg $21.56, +$4.88 per additional 0.5 kg; 21–30 kg $8.53/kg; 31 kg+ $8.16/kg. Fuel included, duties excluded. **[U]** — third-party rate table, confirm with a live MyDHL+ quote.

### ⚠️ Volumetric weight is the hidden cost on stands

Couriers bill on **L×W×H ÷ 5000**, i.e. **1 m³ = 200 kg chargeable**. Acrylic stands are mostly air.

100 stands at Seritag's dimensions (14.5 × 10.5 × 6 cm): actual weight ~12 kg, **volumetric ~20 kg** → ~$170–210 freight = **$1.70–2.10/unit, more than the $0.85 stand itself.**

**Levers:** a **flat plate/plaque** instead of a 3D stand collapses volumetric weight (Seritag's plate is cheaper than their stand at every tier). Failing that, demand flat-packed or nested acrylic and get carton dimensions in writing before accepting any freight quote.

### Duty and VAT

### 🔴 Duty is 0% on chipped cards but 6.5% on acrylic stands

All rates queried live in TARIC 26-08-2026, origin China **[V]**:

| Product | CN/TARIC code | Duty |
|---|---|---|
| **Chipped NFC card** ("smart cards") | **8523 52 00 00** | **0%** |
| NFC inlays/tags/stickers not card-shaped | 8523 59 10 00 | **0%** |
| **Acrylic/PMMA display stand, sign holder, plastic plaque** | **3926 90 97 90** | **6.5%** |
| Plastic office/desk supplies | 3926 10 00 00 | 6.5% |
| **Metal** sign-plates / nameplates | 8310 00 00 00 | 2.7% |
| Blank PVC card with **no chip** | 3926 90 97 90 | 6.5% |
| Printed matter, no chip | 4911 99 00 00 | 0% |

Governing rule: Note 6(b) to Chapter 85 — a card with an embedded IC and antenna and *no other active or passive circuit elements*. A passive NFC card fits exactly. No anti-dumping or safeguard measure listed for China on any of these codes.

- Push back if a broker proposes 3919 for a chipped card — that's plastic film as such; the chip gives the article its essential character.
- **8543 70 90 (3.7%)** applies if the tag contains extra circuit elements — capacitor, battery, sensor. Relevant only for active/BLE tags.
- ⚠️ **A stand with an NFC tag embedded is a composite article** — classification turns on essential character and could go either way between 0% and 6.5%. **[U]** Consider a free **BTI (bindende tariferingsoplysning)** from Toldstyrelsen, binding 3 years, if the volume makes the difference material.
- 🔴 **Ask the supplier to invoice chipped cards as a separate line from stands**, so the 0% line isn't dragged into a 6.5% classification.
- ⚠️ **There is no duty-free floor any more.** Pre-1 July 2026 a sub-€150 sample of stands would have been duty-free; now 6.5% applies from the first krone.
- **Import moms 25%**, base = customs value + duty + freight + insurance + broker fees. **Fully reclaimable as købsmoms if VAT-registered** — declared and deducted on the same momsangivelse. Net zero.
- **EUR 150 duty de minimis abolished 1 July 2026** (Council Reg (EU) 2026/382) **[V]**. The replacement EUR 3 flat duty applies only to IOSS or postal consignments — **not** commercial courier B2B imports. Since duty is 0% anyway, this is noise for cards.
### Courier disbursement fees into Denmark — all verified [V]

| Carrier | Fee |
|---|---|
| **DHL Express** (cheapest) | min **112.50 kr** account / **100 kr** non-account, otherwise 2% of duty+VAT. + 75 kr toldbehandling, + 40 kr per extra tariff line |
| **FedEx** (from 20 Jul 2026) | **2.5% or 111.90 kr**, whichever greater. + 17.90 kr inbound handling |
| **UPS** (from 7 Jun 2026) | **182 kr min or 3%** where value > €22. + 55.35 kr entry prep, + 83.05 kr per line beyond 5 |
| **PostNord** | **225 kr** flat |

**→ Ship DHL Express.** Toldstyrelsen also notes you can avoid the fee entirely by declaring the goods yourself: *"Hvis du vil undgå gebyret, skal du kontakte transportøren for at aftale, om du selv kan stå for at toldangive dine varer."*

Carrier handling fees are **not** part of the VAT base (they're the carrier's own service, separately VAT-charged).
- **Toldkredit** (deferred duty/VAT account) lets you clear in your own name and skip the courier disbursement fee entirely. Worth asking a revisor about.

### Estimated landed cost per unit, net of reclaimed VAT

| | 100 units | 250 units | 500 units |
|---|---|---|---|
| Acrylic stand (China) | ~19 kr | ~16 kr | ~15 kr |
| PVC card (China) | ~5 kr | ~4 kr | ~3 kr |
| PVC card (ShopNFC Italy) | ~10 kr | ~10 kr | ~9 kr |

Against 199–299 kr retail on stands, or Chippy's 119 kr / 32 kr on cards. **The margin is there either way.**

### 🔴 Incoterms — ask for DAP, not DDP

Under DDP the supplier is importer of record, the customs bill is not in your company's name, and **you cannot reclaim the 25% import moms.** That silently turns a ~+40% landed uplift into ~+75%. **Insist on being importer of record with your own EORI** (= "DK" + your CVR, issued automatically).

---

## 4. PRODUCT SPEC — non-negotiables for the PO

1. **Genuine NXP NTAG213.** Write into the PO: *"genuine NXP NTAG213, not compatible/clone, not FM11NT021."* Clone chips (Shanghai Fudan FM11NT021) have duplicate UIDs, no GET_VERSION response, no NXP ECDSA originality signature, and unreliable locking. Verify samples with NXP TagInfo before the production run.
2. **NTAG213 is sufficient.** 144 bytes user memory; a Google review URL is 39–79 chars. NTAG215/216 buy memory you have no use for. Take 215 only if it's near price-parity.
3. **Largest inlay the form factor allows.** Antenna size, not chip type, sets read range: 12×20 mm ≈ 18 mm range; card-size 85×54 mm ≈ 65 mm. A small disc inlay in a big stand is the classic "works on Android, not iPhone" failure.
4. **No metal near the antenna.** Metal doesn't attenuate — it destroys (eddy currents detune the antenna). Kills: weighted metal bases, metal feet, mirrored/metallic foil finishes, metallic ink over the antenna. Metal SKUs need ferrite-backed on-metal inlays.
5. **Encode as URI/website NDEF record, never a text record.** A text record silently kills iPhone background reading.
6. **Password-protect (PWD/PACK/AUTH0), do not permanently lock.** Unlocked tags on a public counter can be rewritten in ~10 seconds by anyone with a free Android app — redirecting a client's tag to a competitor or phishing page. But irreversible lock bytes mean one mis-encoded batch is scrap, and a relocating client gets landfill.
7. **Printed QR code on every unit.** iPhone 7/8/X cannot background-read; iPhone 6s and earlier cannot read tags at all. Costs nothing, removes the biggest support burden.
8. Acrylic/PVC/wood/glass do **not** block NFC — 3–5 mm of acrylic costs 3–5 mm of a 40–65 mm range budget. Negligible.

---

## 5. 🔴 THE REDIRECT LAYER — do not skip this

**Never burn a raw Google URL into the chip.** Write `nfc.ditdomæne.dk/a7f3k` → 302 → the shop's review link.

Google's own docs **[V]**: *"Place IDs may change over time"* · *"A place ID may become obsolete if a business closes or moves"* · *"Google recommends refreshing place IDs if they are more than 12 months old."* Custom short names (`g.page/xxx`) are **discontinued** — no longer creatable or editable.

Without a redirect layer, a Place ID rotation, a client relocation, or a Google URL-scheme change **bricks physical inventory already sitting on counters.** With it, every one of those is a database edit.

Bonus: scan analytics, which is a legitimate upsell and something Chippy doesn't offer.

Review link formats:
- Native: Business Profile → Read reviews → Get more reviews → currently `https://g.page/r/{ID}/review`
- Programmatic: `https://search.google.com/local/writereview?placeid={PLACE_ID}`, Place ID from Google's Place ID Finder

---

## 6. GOOGLE'S REVIEW POLICY

This is Google's private terms, not law. Breach = reviews wiped or profile suspended — a **separate risk channel** from Danish law, which fines. A shop can be fully legal and still lose its reviews.

**✅ NFC/QR linking to the review form is explicitly allowed.** Google ships QR codes for this itself and permits merchants to *"solicit or encourage the posting of content that does represent a genuine experience, without offering incentives to do so or attempting to influence the rating or the contents of the review."*

### ⚠️ The one clause sitting under this product

> "When soliciting reviews, merchants should not require or pressure users to leave ratings or write reviews **while on the premises**, nor should they request that specific content be included."

**The Danish version of the same page says "opfordrer" (encourage), not "require".** English bans *require or pressure*; Danish bans *encourage or pressure*. A counter-top tag is unambiguously "encouraging on the premises." Reading the English as controlling, a passive tag a customer chooses to tap is not requiring or pressuring — **but this is a genuine ambiguity, not a settled question.**

Design and copy consequences:
- **Safe:** tag on the counter, table tent, receipt holder; customer taps voluntarily
- **Risky:** copy telling shops to have staff hand it to every customer, or prompt at point of payment
- **Avoid:** framing as a review *station* or *kiosk*; staff quotas; asking customers to name a staff member

### ❌ Review gating — prohibited by Google AND illegal in Denmark
Sentiment pre-screens that route happy customers to Google and unhappy ones to a private form. Many vendors sell exactly this. Google: *"Discourage or prohibit negative reviews, or selectively solicit positive reviews."* Forbrugerombudsmanden: no *"forudgående sortering af de kunder, der opfordres til at indgive en anmeldelse."* **Do not build it, do not market it.**

### ❌ Incentivized reviews — prohibited
No discounts, free goods, or payment in exchange for reviews. Also EU-illegal under UCPD Annex I 23b/23c → bilag 1 to markedsføringsloven.

### ✅ Bulk solicitation — fine
Asking *every* customer is the compliant alternative to gating. Prohibited: selectivity, quotas, scripting.

### Copy verdicts
| Copy | Verdict |
|---|---|
| "Gør det nemt for kunderne at give en anmeldelse" | ✅ |
| "Ét tap – ingen app, ingen skriven adresse" | ✅ |
| "Bed alle dine kunder om en anmeldelse" | ✅ |
| "Få flere 5-stjernede anmeldelser" | ⚠️ implies rating influence → "flere anmeldelser" |
| "Filtrér utilfredse kunder fra" | ❌ gating |
| "Giv 10% rabat for en anmeldelse" | ❌ incentivized |
| "Boost din rating garanteret" | ❌ manipulation + undocumentable (§ 13) |

---

## 7. BUSINESS SETUP & COMPLIANCE

### Entity: enkeltmandsvirksomhed + voluntary VAT registration from day one

- **PMV is unworkable** — it cannot be VAT registered, so the 25% import moms becomes a dead cost.
- **ApS capital is 20,000 kr**, halved effective 27 Feb 2025 (not 40,000).
- **The 50,000 kr threshold is a red herring.** Import moms is due on every non-EU import regardless of turnover, and buying services from abroad (Shopify, Meta/Google ads) triggers registration on the **very first purchase** with no threshold at all, under omvendt betalingspligt.
- **Register no later than 8 days BEFORE starting the activity** at virk.dk. New businesses report quarterly for ~18 months.
- EORI is issued automatically as "DK" + CVR.

### 🔴 Producer-responsibility registrations — both have 14-day advance deadlines

**WEEE / electronics — producentansvar.dk (formerly DPA-System)**
Passive NFC tags **are in scope**: *"Det er IKKE afgørende, om udstyret er aktivt eller passivt"* — scope is anything dependent on electric current **or electromagnetic fields**. BEK nr. 942 af 20/06/2025 § 41(c) makes anyone placing EEE from a third country on the Danish market a *producent*. That's you.
- **§ 6: register no later than 14 days before first placing product on the market.** Selling before registration is illegal — and illegal for your distributors to buy from you.
- § 43: post financial security for household EEE annually unless exempted via a collective scheme (§ 46). **Most-missed cost.**
- Crossed-out wheeled bin pictogram on product.
- Reporting 1 Jan – 31 Mar; auditor/management declaration by 31 May.
- Likely category 6 (small IT/telecom, ≤50 cm) — request a free binding determination under § 10.
- **No de minimis.** ~1,000 kr setup + ~250 kr/year at low volumes.

**Packaging — BEK nr. 1146 af 29/09/2025**
- **§ 21: register 14 days before** placing packaging on the market.
- § 27 stk. 7's 8-tonne figure is a **reporting simplification, not a registration threshold and not an exemption.**
- Micro-enterprise status does **not** exempt you. Responsibility extends to **inbound transport packaging** — the cartons your Chinese shipment arrives in.
- Reporting by 1 June annually. PPWR (EU) 2025/40 applies from 12 August 2026 — already live.

**Batteries: N/A** (passive tag, no battery).

### RoHS / RED / CE

- **RoHS: unambiguously in scope.** Commission RoHS 2 FAQ Q6.7: *"RFID tags (active and passive) are in scope."* As importer (RoHS Art. 9) you must verify the manufacturer's conformity assessment, check CE marking, **put your own name and contact address on the product, packaging or accompanying document**, and **keep the EU DoC for 10 years**.
- **RED: contested.** The Commission's RED Guide § 1.6.3.13 says *"TAG are radio equipment within the scope of the RED."* The common "passive tags are out of scope" claim traces to an industry position paper that quotes the Guide selectively. Counter-arguments exist (RED Art. 2(1)(1) requires *intentional* emission) but a market surveillance authority reaches for the Guide first. **Practical answer: only source from suppliers who provide a RED DoC.** Cheap insurance.
- **EMC: nothing to do** — excluded either way.
- **GPSR:** Art. 11 and Art. 16 are disapplied where RoHS/RED cover the same risks, but **Art. 19 (distance sales) still applies to every product page**: manufacturer's name + postal **and email** address; your name + postal + email as responsible person; product identifiers **including a picture**; warnings/safety info. BEK nr. 1146 af 06/11/2024 § 4 requires these **in Danish**. You don't hire an EU rep — under Reg. 2019/1020 Art. 4(2)(b) **you simply are the responsible person**.
- Note: from January 2026 Sikkerhedsstyrelsen is part of Erhvervsstyrelsen.

### B2C webshop obligations

- **Fortrydelsesret 14 days** from physical possession (forbrugeraftaleloven § 19). **§ 19 stk. 3: failing to inform extends it to ~12 months + 14 days.** The **standardfortrydelsesformular (bilag 3) is mandatory** (§ 8 stk. 1 nr. 11). Return shipping is only the consumer's cost **if told in advance** (§ 24, § 8 stk. 1 nr. 14) — otherwise you pay.
  - ⚠️ § 18 stk. 2 exempts custom-made/personalised goods — personalised tags may fall outside the right entirely.
- **Reklamationsret 2 years**, non-waivable (købeloven § 83). Burden-of-proof presumption is **12 months** since 1 Jan 2022. Keep distinct from fortrydelsesret in the terms.
- **Site info:** name, address, email, **CVR** must be *"let tilgængelig og vedvarende"* (e-handelsloven § 7). Prices incl. moms.
- 🔴 **Do NOT add an ODR link.** Reg. (EU) 2024/3228 repealed Reg. 524/2013; the platform stopped taking complaints 20 March 2025 and **shut down 20 July 2025**. A live link to a dead platform is itself misleading. Use instead: **Mæglingsteamet for Forbrugerklager / Forbrugerklagenævnet, Nævnenes Hus, Toldboden 2, 8800 Viborg.** Many Danish law-firm templates still say "Center for Klageløsning" — outdated, don't copy.
- GDPR: privatlivspolitik, Art. 30 fortegnelse, databehandleraftaler with Shopify/email/analytics, 72-hour breach notification, prior consent for non-essential cookies with reject as prominent as accept. **[U]** — supervisory competence for cookies has shifted between Erhvervsstyrelsen and Datatilsynet; verify current position.

---

## 8. 🔴 THE RESELLER PROGRAMME — highest legal risk in the plan

The tags are the easy part. Marketing resale income to young people is where this gets genuinely dangerous. Forbrugerombudsmanden has published guidance that reads as if written for this scenario.

### § 13 — earnings claims are factual claims requiring documentation

Markedsføringsloven § 13: *"Den erhvervsdrivende skal kunne dokumentere rigtigheden af oplysninger om faktiske forhold."*

FO's MLM/pyramid vejledning, directly on point:
> "Oplysninger om indtjeningsmuligheder er angivelser om faktiske forhold, der skal kunne dokumenteres efter markedsføringslovens § 13. Kan oplysningerne ikke dokumenteres, vil de efter omstændighederne være vildledende og i strid med markedsføringslovens § 5 og/eller § 6."

**Documentation must exist when the claim is made** — not be assembled after a complaint. One lucky reseller's screenshot is not documentation of a *typical* outcome.

### Pyramid boundary — bilag 1 nr. 14

> "14) Etablering, drift eller promovering af en salgsfremmende pyramideordning, hvor forbrugeren erlægger et vederlag og til gengæld stilles kompensation i udsigt, som hovedsageligt er afhængig af, om han har introduceret andre for ordningen og i mindre grad af salg eller forbrug af produkter."

**Straight wholesale — buy tags, sell to shops — is NOT a pyramid scheme.** Real product, real end customers. **It becomes one the moment resellers earn from recruiting other resellers. Never add a referral tier.**

FO also: no *"krav om urimelig investering i varelager"*, and *"Der bør være pligt for udbyderen til at tilbagekøbe et eventuelt varelager."* → **Offer buy-back on unsold stock.**

### Targeting young people — expressly called out

> "Hvis hvervningen udelukkende henvender sig til fx børn, unge, studerende eller letpåvirkelige mennesker, kan der endvidere være tale om socialt uansvarlig markedsføring i strid med markedsføringslovens § 3 og eventuelt § 11."

Markedsføringsloven § 3 stk. 2 requires *særlig hensyntagen* to under-18s' *"naturlige godtroenhed og manglende erfaring og kritiske sans."*

**The threshold is low.** FO: marketing counts as directed at minors if a *"ikke ubetydelig del"* of the audience is under 18 — a case at **12% under-18 followers** was enough. And:
> "Forbrugerombudsmanden er opmærksom på, at 49 % af brugerne på TikTok er 12-18 år. … Opslag på TikTok samt andre medier, hvor et højt antal af brugerne er under 18 år, vil derfor som udgangspunkt være rettet mod børn og unge."

**No effective age filter = presumed directed at minors.** Merely stating "kun for personer over 18 år" is not an effective filter.

Critically, FO extends **consumer-like protection to resellers** despite their trader status:
> "Selv om forhandlerne juridisk anses som erhvervsdrivende … bør der anlægges en vurdering, der også inddrager forbrugerlignende beskyttelseshensyn."

→ **"They're B2B customers, not consumers" will not work as a defence.**

### Can a 16-year-old even buy a reseller pack?

Værgemålsloven § 1: under-18s are *umyndige* and *"kan ikke selv forpligte sig ved retshandler."*
§ 42 lets 15+ dispose of *"hvad de har erhvervet ved eget arbejde"* — **but stk. 2: "Den medfører ikke adgang til at påtage sig gældsforpligtelser."**
§ 45 restitution is **asymmetric against you**: you return the money in full; the minor owes compensation only *"i det omfang det modtagne skønnes at være kommet denne til nytte."* If the pack is opened or used, **you eat the loss.** A false age statement gives only thin, discretionary protection (§ 45 stk. 2), and FO's position is the agreement is void regardless.

**Practical rule: 15+ paying upfront with their own earned money = binding. Any invoice, credit, instalment, or "pay when you've sold them" = void. Never extend credit to under-18s.**

### Influencer / TikTok labelling — § 6 stk. 4

Commercial intent must be clearly disclosed. **Promoting your own products always counts.**

**Insufficient (FO explicit):** a bare tag or hashtag · marking at the end of the post · marking only the first post in a series · "i samarbejde med" / "sponsoreret af" · platform built-in labels.

**Required:** *"reklame for xx"* or *"annonce for xx"* **as the first element**, on **every** post individually. Danish posts must be marked in Danish. Fines cited 15,000–40,000 kr for influencers; liability reaches the advertised business too.

Heightened standard when the audience includes minors: *"Det er Forbrugerombudsmandens vurdering, at det sjældent vil være tydeligt af sammenhængen, at der er tale om reklame, når det er rettet mod børn og unge."*

Bilag 1 pkt. 28 separately bans direct exhortations to children to buy.

### Penalties
Markedsføringsloven § 37 — bøde. Stk. 8 caps cross-border fines at **4% of turnover in affected member states**, or EUR 4m where turnover data is unavailable.

### Claim-by-claim verdict
| Claim | Verdict |
|---|---|
| "Sælg NFC-anmeldelsesskilte til lokale butikker" | ✅ |
| "Vores forhandlere køber til 25 kr. og sælger typisk til 149 kr." | ⚠️ only with § 13 documentation of *actual typical* resale prices |
| "Tjen 5.000 kr. om måneden" | ❌ undocumentable typical-earnings claim — §§ 5, 6, 13 |
| "Perfekt sidehustle for dig på 16" | ❌ socially irresponsible marketing — §§ 3, 11 |
| "Tjen penge når du hverver nye forhandlere" | ❌ bilag 1 nr. 14 — pyramid scheme |
| Unlabelled TikTok promo by a paid teen creator | ❌ skjult reklame — § 6 stk. 4 |
| "Ingen risiko – vi køber usolgt lager tilbage" | ✅ safe *and* aligns with FO guidance |

### Operating rules that follow
1. **Reseller packs sold to 18+ only**, with a real age gate — not a checkbox disclaimer.
2. **Never extend credit to anyone under 18.**
3. **No income claims** without documentation held at the time of the claim.
4. **Never a referral or recruitment tier.**
5. **Offer buy-back on unsold stock** — legally protective and a genuine differentiator.
6. **Label every TikTok post** "reklame for [brand]" as the first element.
7. No unreasonable minimum stock investment.

---

## 9. WHERE A PROFESSIONAL IS ACTUALLY NEEDED

1. **Toldstyrelsen BTI** for classification — free, binding 3 years. Worth it for the acrylic stand question specifically.
2. **Erhvervsstyrelsen/Sikkerhedsstyrelsen in writing on RED applicability** to passive tags — Commission guidance and the statutory definition point opposite ways.
3. **Revisor, one session** — non-EU import moms mechanics, reverse charge on foreign SaaS, and whether to apply for toldkredit.
4. **Advokat on the reseller programme** — reseller terms, the § 13 earnings-claim documentation file, and the age policy. Not a DIY exercise if young buyers are the target.

**Not needed** (self-serviceable): entity choice, standard webshop terms, moms mechanics, DPA registrations.

---

## 10. OPEN ITEMS

**Resolved since first draft:** stand duty rate (6.5%, TARIC 3926 90 97 90) · all four carrier disbursement fees · Toldstyrelsen's B2B position on the 1 July 2026 change (B2B always pays tariff duty, cannot elect the €3) · Danish competitor landscape.

**Still open:**
- [ ] **Live MyDHL+ quote** with real carton dimensions and Danish postcode — settles freight, remote-area surcharge, current fuel %. Biggest remaining unknown.
- [ ] BTI for a **composite stand** (acrylic + embedded NFC) if volume makes 0% vs 6.5% material
- [ ] EU-wide e-commerce handling fee slated for **November 2026** — amount unpublished, watch it
- [ ] Commission's monthly trade-diversion reviews from 1 Oct 2026 could extend the €3 flat duty to all ≤€150 consignments
- [ ] Whether a sub-€150 B2B *postal* consignment attracts €3 or tariff duty — Reg. Art. 2(b) and Toldstyrelsen's FAQ read differently. Toldstyrelsen: 72 22 12 02

---

## 11. THE SIDE-HUSTLE EVIDENCE BASE — read before writing any reseller copy

- **The only documented attempt anywhere made zero sales.** [Fastlane Forum thread 124925](https://www.thefastlaneforum.com/community/threads/documented-attempt-at-a-side-hustle-using-google-nfc-cards.124925/) — a California student bought 30 blank cards for $18 to sell at $50. Zero sales. Other members raised saturation concerns.
- **The famous "costs $0.50, sells for $50" figure has no independent verification.** It traces entirely to vendor-authored SEO and affiliate pages (taprocard.com/blogs, prosperqr.com, rfidtag.com, an AI-generated Vercel site) — i.e. the companies selling the blanks.
- TikTok discover pages on this product exist in volume and claim 540.2K posts, but those pages aggregate loosely and inflate. **No follower or view count for any creator could be verified** (TikTok search is login-walled).
- **Zero Danish, Swedish or Norwegian creators promoting this.** Genuine null result, not a search failure — Nordic-language queries return clean vendor results, so the index works.

**Consequence under markedsføringsloven § 13:** documentation must exist *at the time the claim is made*. Today the honest evidence for "you can resell these profitably in Denmark" is one documented attempt with zero sales, in a market where five Danish ApS companies already deliver to the same shops in 1–3 days from 199 kr. **Any earnings claim in reseller copy is currently undocumentable.**
