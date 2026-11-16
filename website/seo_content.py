# -*- coding: utf-8 -*-
"""Indhold til branchesider og søgeguides. Kun tekst og data — build.py
står for opsætningen. {P1} og {PMIN} bliver erstattet med priserne ved build.

Regler for teksten (gælder også fremover):
  * Intet opdigtet: ingen procentsatser, kundecitater eller resultater vi ikke
    kan dokumentere. Hellere konkrete råd end store tal.
  * Hver side skal være brugbar for nogen, der aldrig køber noget. Det er det,
    Google belønner, og det er det, der får folk til at stole på os.
"""

# ---------------------------------------------------------------- brancher
# slug, kort navn, <title>, H1, meta, lede, sektioner [(h2, html)], faq [(q, [svar])]
BRANCHER = [
    dict(
        slug="frisoer",
        nav="Frisører og saloner",
        title="Google Review-kort til frisører og saloner — fra {P1} kr",
        h1="Google Review-kort til frisører og saloner",
        desc="Få flere Google-anmeldelser i din salon. Kunden holder telefonen mod kortet ved kassen, og anmeldelsen er åben. Til frisører, barbershops, negle- og skønhedssaloner. Fra {P1} kr.",
        lede="Kunden går fra stolen med nyt hår og et spejlbillede, de er glade for. Det er det bedste øjeblik for en anmeldelse, og det varer cirka lige så længe, som det tager at betale.",
        who="Frisører, barbershops, negle- og vippesaloner, skønhedsklinikker og spa",
        sections=[
            ("Hvorfor anmeldelser betyder ekstra meget for en salon",
             """<p>Når nogen flytter til byen, eller deres faste frisør stopper, søger de på "frisør" og et bynavn i Google. Det, de ser først, er kortet med de nærmeste saloner — og ved hver salon et antal stjerner og et antal anmeldelser.</p>
<p>Google skriver selv, at antallet af anmeldelser og bedømmelsen indgår, når de rangerer virksomheder i de lokale resultater. For en salon, hvor næsten alle nye kunder starter med en søgning, er anmeldelserne derfor ikke pynt. De er en del af, om du overhovedet bliver set.</p>
<p>Udfordringen er, at tilfredse kunder sjældent skriver af sig selv. De mener det godt, men når de er kommet hjem, er det glemt. Kortet flytter anmeldelsen til det øjeblik, hvor kunden stadig står i salonen.</p>"""),
            ("Hvor kortet skal ligge i salonen",
             """<ul>
<li><strong>Ved kassen eller betalingsterminalen.</strong> Det er det eneste sted, hver eneste kunde kommer forbi med telefonen fremme. Læg kortet lige ved siden af terminalen.</li>
<li><strong>Ved hver arbejdsplads, hvis I tager betaling ved stolen.</strong> Mange saloner tager MobilePay ved stolen. Så skal kortet være der — ikke ved en disk, kunden aldrig går hen til.</li>
<li><strong>Ikke ved indgangen.</strong> Når kunden kommer ind, har de intet at anmelde endnu.</li>
<li><strong>Ikke på en metalhylde.</strong> Metal svækker NFC-signalet. Træ, glas, plastik og sten er helt fint.</li>
</ul>"""),
            ("Hvad du kan sige — uden at det bliver akavet",
             """<p>Det største løft kommer, når den, der har klippet, selv nævner det. Én gang, venligt, og uden at stå og vente:</p>
<ul>
<li><em>"Hvis du er glad for resultatet, må du meget gerne lægge telefonen på kortet her. Så åbner Google med det samme."</em></li>
<li><em>"Vi er en lille salon, så en anmeldelse på Google hjælper os rigtig meget. Det tager ti sekunder."</em></li>
</ul>
<p>Sig ikke, hvad kunden skal skrive, og spørg alle — ikke kun dem, du tror er tilfredse. At udvælge, hvem der bliver spurgt, er imod både Googles regler og Forbrugerombudsmandens retningslinjer. Læs mere i <a href="../guides/regler-for-anmeldelser.html">reglerne for Google-anmeldelser</a>.</p>"""),
            ("Hvor mange kort skal en salon bruge?",
             """<p>Ét kort pr. sted, hvor der bliver betalt. En lille salon med én kasse klarer sig med ét eller to kort (ét i reserve). Har I fem stole og tager betaling ved hver, så tag fem.</p>
<p>Har du flere saloner, eller vil du give kortet til dine stylister, kan det betale sig at se på <a href="../maengderabat.html">mængderabatten</a>.</p>"""),
        ],
        faq=[
            ("Kan kunden anmelde den enkelte frisør?",
             ["Anmeldelsen havner på salonens Google-profil, ikke på den enkelte medarbejder. Kunden kan selvfølgelig nævne navnet i teksten, og det gør mange af sig selv, når de er glade for den, der har klippet dem."]),
            ("Må jeg give rabat på næste klip for en anmeldelse?",
             ["Nej. Alt, der har værdi, og som gives i bytte for en anmeldelse, er forbudt efter Googles regler og kan være ulovligt efter markedsføringsloven. Du må gerne spørge — bare ikke betale for det."]),
            ("Virker kortet, hvis kunden har en ældre telefon?",
             ["iPhone XS og nyere samt de fleste Android-telefoner læser kortet med det samme. Til de ældre telefoner er der en QR-kode på bagsiden, så ingen står med en telefon, der ikke reagerer."]),
        ],
    ),
    dict(
        slug="restaurant-og-cafe",
        nav="Restauranter og caféer",
        title="Google Review-kort til restauranter og caféer — fra {P1} kr",
        h1="Google Review-kort til restauranter og caféer",
        desc="Flere Google-anmeldelser til din restaurant, café eller bar. Læg kortet med regningen eller på disken, og gæsten anmelder med ét tryk. Ingen app, intet abonnement. Fra {P1} kr.",
        lede="Gæsterne vælger restaurant på Google Maps — ofte stående på gaden med telefonen i hånden. Stjernerne og antallet af anmeldelser er det første, de ser.",
        who="Restauranter, caféer, barer, bagerier, takeaway og food trucks",
        sections=[
            ("Det rigtige øjeblik er regningen",
             """<p>Et restaurantbesøg har ét naturligt stop, hvor gæsten har telefonen fremme: når der skal betales. Maden er spist, oplevelsen er frisk, og de venter alligevel på terminalen.</p>
<p>Det er dér, kortet skal være. Ikke på en plakat ved toilettet og ikke i en mail tre dage senere, hvor gæsten for længst har glemt, hvad de spiste.</p>"""),
            ("Hvor kortet skal ligge",
             """<ul>
<li><strong>Med regningen.</strong> Kommer regningen i en mappe eller på en bakke, så læg kortet i den. Det er den mest effektive placering i en restaurant.</li>
<li><strong>Ved disken i caféen.</strong> Bestiller og betaler man ved disken, så læg kortet ved terminalen. Et kort pr. kasse.</li>
<li><strong>Ved udleveringen til takeaway.</strong> Kunden står og venter på maden — et oplagt sted at vise kortet.</li>
<li><strong>Pas på metalbakker.</strong> En regning på en stålbakke svækker NFC-signalet. Læg kortet oven på et stykke papir, en træplade eller i en læder- eller plastikmappe.</li>
</ul>"""),
            ("Sådan får personalet det med",
             """<p>Kortet virker bedst, når tjeneren nævner det, mens regningen bliver sat på bordet:</p>
<ul>
<li><em>"Har I haft en god aften, må I meget gerne lægge telefonen på kortet. Så kommer I direkte til vores Google-side."</em></li>
</ul>
<p>Én gang, til alle borde. Personalet skal ikke stå og vente, mens gæsten skriver, og de skal ikke kun spørge de borde, der virkede glade. Det er både Googles regel og den, der holder anmeldelserne troværdige.</p>"""),
            ("Svar på anmeldelserne",
             """<p>Gæster læser svarene. Et kort, konkret svar på en kritisk anmeldelse — uden at forsvare sig — viser de næste gæster, at der er nogen, der lytter. Vi har skrevet en guide om, <a href="../guides/daarlige-anmeldelser.html">hvad du gør ved dårlige anmeldelser</a>.</p>"""),
        ],
        faq=[
            ("Hvor mange kort skal en restaurant have?",
             ["Ét pr. regningsmappe eller bakke, hvis kortet følger med regningen, og ét pr. kasse i en café. Har I ti mapper, så tag ti kort — så skal ingen lede efter dem midt i servicen."]),
            ("Kan kortet tåle at blive spildt på?",
             ["Kortet er i PVC som et betalingskort, så en klud er nok. Chippen sidder indstøbt og tager ikke skade af vand eller spild."]),
            ("Kan jeg pege kortet mod TripAdvisor i stedet for Google?",
             ["Ja. Kortet åbner det link, der er skrevet på det. Google er det, de fleste danske gæster bruger til at finde et sted at spise, men du kan sagtens vælge en anden platform."]),
        ],
    ),
    dict(
        slug="butik",
        nav="Butikker",
        title="Google Review-kort til butikker — anmeldelser ved kassen",
        h1="Google Review-kort til butikker",
        desc="Få flere Google-anmeldelser i din butik. Kortet ligger ved betalingsterminalen, kunden holder telefonen mod det, og anmeldelsen åbner. Til tøj, kiosk, blomster, cykel og specialbutikker. Fra {P1} kr.",
        lede="I en butik kommer alle kunder forbi det samme sted: kassen. Det gør det nemt — kortet skal bare ligge der, hvor kunden alligevel står med telefonen.",
        who="Tøjbutikker, specialbutikker, blomsterhandlere, cykelhandlere, kiosker, optikere og showrooms",
        sections=[
            ("Hvorfor en butik har brug for Google-anmeldelser",
             """<p>Selv folk, der ender med at handle fysisk, starter ofte med at søge: "cykelhandler i nærheden", "blomster Aarhus", "brugskunst Vesterbro". Google viser de lokale butikker på et kort med stjerner og antal anmeldelser, og det påvirker både hvem der bliver vist, og hvem der bliver valgt.</p>
<p>Butikker har ofte mange tilfredse kunder og forbløffende få anmeldelser. Ikke fordi kunderne er utilfredse, men fordi ingen beder dem om det på det rigtige tidspunkt.</p>"""),
            ("Hvor kortet skal ligge",
             """<ul>
<li><strong>Lige ved betalingsterminalen.</strong> Kunden holder telefonen eller kortet i hånden, mens betalingen går igennem. Det er der, de ser det.</li>
<li><strong>På disken, ikke bag den.</strong> Kortet skal kunne nås uden at spørge.</li>
<li><strong>Ved afhentning af ordrer.</strong> Har du klik-og-hent eller reparationer, så vis kortet, når varen bliver udleveret — det er dér, kunden er gladest.</li>
<li><strong>Ikke på metal.</strong> Mange kasser og diske har metaldele. Læg kortet på træ, glas eller plastik — eller sæt det i en lille holder.</li>
</ul>"""),
            ("Kortet i posen?",
             """<p>Nogle butikker lægger et kort i posen eller pakken. Det koster mere, fordi kortet ikke kommer igen, og effekten er mindre, fordi kunden først opdager det hjemme. Hvis du gør det, så brug QR-koden som hovedsagen, og vælg en billigere løsning end et NFC-kort til hver pose.</p>
<p>Til selve kassen er NFC-kortet det rigtige: ét kort, der bliver brugt hundredvis af gange.</p>"""),
            ("Har du flere butikker?",
             """<p>Hver butik har sin egen Google-profil, så hvert kort skal pege på den rigtige butik. Vi koder kortene for dig og mærker dem, så de ikke bliver blandet sammen. Se <a href="../maengderabat.html">priser ved større antal</a>.</p>"""),
        ],
        faq=[
            ("Kan kortet ligge ved siden af betalingsterminalen uden at forstyrre den?",
             ["Ja. Kortet har ingen strøm og sender intet af sig selv. Det reagerer kun, når en telefon holdes helt tæt på. I praksis ligger det fint ved siden af terminalen — bare ikke oven på dens læseflade."]),
            ("Kan kunden komme til at betale med kortet ved en fejl?",
             ["Nej. Kortet indeholder kun et link. Det kan ikke trække penge, og det kan ikke læse noget fra kundens telefon."]),
            ("Hvad hvis vi skifter adresse eller får en ny Google-profil?",
             ["Så skriver du det nye link til kortet med en gratis app. Kortet er beskyttet med en kode, ikke låst for altid — du skal ikke købe nye kort."]),
        ],
    ),
    dict(
        slug="haandvaerker-og-vaerksted",
        nav="Håndværkere og værksteder",
        title="Google Review-kort til håndværkere og værksteder",
        h1="Google Review-kort til håndværkere og værksteder",
        desc="Flere Google-anmeldelser til elektrikere, VVS'ere, tømrere, malere og autoværksteder. Giv kortet til kunden, når jobbet er færdigt, eller læg det ved værkstedsdisken. Fra {P1} kr.",
        lede="Når et job er godt udført, er kunden aldrig mere tilfreds end i øjeblikket, hvor de ser resultatet. Det er også øjeblikket, hvor anmeldelsen er nemmest at få.",
        who="Elektrikere, VVS'ere, tømrere, malere, murere, rengøring, autoværksteder og cykelværksteder",
        sections=[
            ("Hvorfor anmeldelser betyder så meget for håndværkere",
             """<p>Når nogen skal have skiftet en tagrende eller fundet en elektriker, søger de på Google og ringer typisk til en af de første, de ser. De har ikke prøvet dig før, så det eneste, de kan gå efter, er hvad andre kunder har skrevet.</p>
<p>Mange håndværkere har masser af gode kunder og kun en håndfuld anmeldelser, fordi kunderne skal huske det selv, når de har fået fakturaen. Det sker sjældent.</p>"""),
            ("Når der ikke er en disk: tag kortet med",
             """<p>Har du ikke en butik, er kortet ikke noget, der ligger fremme. Det er noget, du har med:</p>
<ul>
<li><strong>Afslut jobbet med kortet.</strong> Når du viser kunden det færdige arbejde, så tag kortet frem: <em>"Er du tilfreds, må du meget gerne holde telefonen her. Det hjælper os rigtig meget."</em></li>
<li><strong>Ét kort pr. bil eller svend.</strong> Kortet skal være der, hvor jobbet slutter — ikke på kontoret. Har du fire biler, så tag fire kort.</li>
<li><strong>Kunden beholder ikke kortet.</strong> Du bruger det samme kort hos alle kunder. Det er derfor, ét kort holder til hundredvis af anmeldelser.</li>
</ul>
<p>Vil du også nå kunder, du ikke ser, kan du sætte linket eller QR-koden på fakturaen. Det er et godt supplement, men det virker langt bedre, når du står over for kunden.</p>"""),
            ("På værkstedet",
             """<p>Har du et værksted med en disk — bilværksted, cykelværksted, dækcenter — så læg kortet der, hvor kunden henter nøglen og betaler. Det er dér, de ser, at bilen er klar, og at regningen var, som aftalt.</p>
<p>Pas på metal: en værkstedsdisk i stål svækker NFC-signalet. Læg kortet på en gummimåtte eller en træplade.</p>"""),
            ("Hvad med de utilfredse kunder?",
             """<p>Spørg alle — også når du er i tvivl. Det er reglen, og det er også det, der gør dine anmeldelser troværdige. Et par kritiske anmeldelser blandt mange gode får dig til at se ægte ud. Og et godt svar på en kritisk anmeldelse viser, at du står ved dit arbejde. Se <a href="../guides/daarlige-anmeldelser.html">guiden om dårlige anmeldelser</a>.</p>"""),
        ],
        faq=[
            ("Kan kortet tåle at ligge i en arbejdsbil?",
             ["Kortet er i PVC som et betalingskort og har ingen batterier. Varme, kulde og fugt i en bil gør det ikke noget. Undgå bare at opbevare det klemt mod metal, mens du bruger det."]),
            ("Kan jeg sætte mit Google-link på fakturaen i stedet?",
             ["Det kan du og bør du, som et supplement. Men et link på en faktura kræver, at kunden selv gør noget senere. Kortet får anmeldelsen, mens du står der — det er det, der gør forskellen."]),
            ("Hvad hvis jeg har flere afdelinger?",
             ["Har hver afdeling sin egen Google-profil, skal kortene pege på hver deres. Skriv det i bestillingen, så koder vi kortene til de rigtige profiler."]),
        ],
    ),
    dict(
        slug="klinik",
        nav="Klinikker og behandlere",
        title="Google Review-kort til klinikker og behandlere",
        h1="Google Review-kort til klinikker og behandlere",
        desc="Google Review-kort til fysioterapeuter, kiropraktorer, tandlæger, massører, dyrlæger og andre klinikker. Patienten anmelder ved receptionen med ét tryk. Fra {P1} kr.",
        lede="I en klinik sker anmeldelsen bedst ved receptionen, når næste tid er booket. Men en klinik skal også være ekstra omhyggelig med, hvordan der bliver spurgt — og svaret.",
        who="Fysioterapeuter, kiropraktorer, tandlæger, massører, psykologer, dyrlæger og andre behandlere",
        sections=[
            ("Receptionen er stedet",
             """<p>Patienten har været i behandling, booker måske næste tid og betaler. Det er det øjeblik, hvor kortet skal være synligt — lige ved terminalen eller på skranken.</p>
<p>Har I flere behandlerrum, hvor der også bliver betalt, så hav et kort i hvert. Behandleren kan nævne det én gang, når behandlingen er slut.</p>"""),
            ("Sådan spørger du i en klinik",
             """<p>Patienter er et andet sted end kunder i en butik. Nogle er i smerter, nogle er nervøse, og nogle vil helst ikke have, at andre ved, at de har været hos jer. Derfor:</p>
<ul>
<li>Nævn kortet roligt og uden forventning: <em>"Har du lyst til at give os en anmeldelse, kan du holde telefonen her. Det er helt frivilligt."</em></li>
<li>Spørg aldrig, mens patienten er i behandling, eller hvis det tydeligvis ikke passer.</li>
<li>Bed ikke om, at de skriver noget om deres behandling eller diagnose.</li>
</ul>"""),
            ("Når du svarer på anmeldelser: tavshedspligt",
             """<p>Det vigtigste for en klinik er svarene. Du må ikke bekræfte, at en person har været patient hos jer, og du må ikke skrive noget om deres behandling — heller ikke selvom de selv har skrevet om den i anmeldelsen.</p>
<p>Et godt svar er generelt: tak for tilbagemeldingen, og hvis noget er gået galt, en opfordring til at kontakte klinikken direkte. Er I autoriserede sundhedspersoner, gælder sundhedslovens regler om tavshedspligt også her. Læs mere i <a href="../guides/daarlige-anmeldelser.html">guiden om dårlige anmeldelser</a>.</p>"""),
            ("Hygiejne",
             """<p>Kortet er i glat PVC og kan tørres af med en klud eller sprit som en betalingsterminal. Det tager ikke skade, og chippen sidder indstøbt.</p>"""),
        ],
        faq=[
            ("Må en klinik bede patienter om anmeldelser?",
             ["Ja. Google tillader, at virksomheder opfordrer til anmeldelser, så længe der ikke gives noget for det, og alle bliver spurgt — ikke kun de tilfredse. Det gælder også klinikker."]),
            ("Kan patienten anmelde anonymt?",
             ["Anmeldelser på Google vises med navnet på den Google-konto, der skriver dem. Patienter, der ikke vil vises med navn, vælger ofte at lade være — og det skal respekteres. Kortet gør det bare nemt for dem, der gerne vil."]),
            ("Kan kortet tåle afspritning?",
             ["Ja. Kortet er i PVC og kan tørres af med sprit eller rengøringsmiddel som andre overflader ved receptionen."]),
        ],
    ),
]


# ---------------------------------------------------------------- nye guides
# (fil, kort titel, beskrivelse, <title>, html)
GUIDES_SEO = [
    ("flere-google-anmeldelser.html",
     "Sådan får du flere Google-anmeldelser",
     "Den komplette danske guide: hvornår du skal spørge, hvad du skal sige, hvilken kanal der virker bedst, og hvad du ikke må.",
     "Sådan får du flere Google-anmeldelser — guide til danske virksomheder",
     """<h2>Hvorfor tilfredse kunder ikke skriver anmeldelser</h2>
<p>De fleste virksomheder har langt flere tilfredse kunder end anmeldelser. Det skyldes sjældent, at kunderne ikke vil. Det skyldes to ting: <strong>besværet</strong> og <strong>timingen</strong>.</p>
<p>Besværet: for at skrive en Google-anmeldelse skal kunden åbne Google, søge på dit navn, finde din profil, rulle ned til anmeldelserne og trykke på "Skriv en anmeldelse". Det er fem skridt, og hvert skridt er et sted, hvor de giver op.</p>
<p>Timingen: kunden er mest tilfreds, mens de står hos dig. Et par timer senere er oplevelsen stadig god, men lysten til at gøre noget ved det er væk.</p>
<p>Alt, der virker for at få flere anmeldelser, gør én af to ting: fjerner skridt, eller flytter spørgsmålet tættere på øjeblikket.</p>

<h2>Hvorfor Google-anmeldelser betyder noget</h2>
<p>Google skriver selv i sin hjælp til virksomhedsprofiler, at antallet af anmeldelser og bedømmelsen indgår i, hvordan virksomheder rangeres i de lokale søgeresultater. Flere anmeldelser og gode bedømmelser kan altså gøre, at du bliver vist højere, når nogen søger på det, du laver, i dit område.</p>
<p>Og når du først bliver vist, er stjernerne og antallet af anmeldelser det første, folk sammenligner på.</p>

<h2>1. Find dit direkte anmeldelseslink</h2>
<p>Udgangspunktet for alt andet er linket, der åbner selve anmeldelsesfeltet — ikke bare din profil. Google giver dig det gratis i din virksomhedsprofil under <em>Få flere anmeldelser</em> (eller <em>Bed om anmeldelser</em>). Vi har skrevet en trin-for-trin-guide: <a href="find-google-anmeldelseslink.html">Sådan finder du dit Google-anmeldelseslink</a>.</p>
<p>Med det link er de fem skridt blevet til ét.</p>

<h2>2. Spørg i det rigtige øjeblik</h2>
<p>Det rigtige øjeblik er, når kunden har oplevet det, de kom for, og stadig er hos dig. I praksis:</p>
<ul>
<li><strong>Butik, café, salon:</strong> ved betalingen.</li>
<li><strong>Restaurant:</strong> når regningen kommer på bordet.</li>
<li><strong>Håndværker:</strong> når du viser kunden det færdige arbejde.</li>
<li><strong>Klinik:</strong> ved receptionen, når næste tid er booket.</li>
<li><strong>Webshop:</strong> når varen er modtaget og prøvet — ikke når ordren er afgivet.</li>
</ul>
<p>Se konkrete råd for din branche under <a href="../brancher/index.html">Google Review-kort til din branche</a>.</p>

<h2>3. Gør det til ét tryk</h2>
<p>Et link er godt i en mail. Ved disken er et link ubrugeligt — kunden kan ikke klikke på noget, der står på et skilt. Der er to måder at gøre det til ét skridt:</p>
<ul>
<li><strong>En QR-kode</strong>, som kunden scanner med kameraet. Virker på alle telefoner, men kræver tre handlinger: åbn kamera, sigt, tryk på linket.</li>
<li><strong>Et NFC-kort</strong>, som kunden holder telefonen mod. Ingen app, intet kamera — siden åbner bare. Det er det hurtigste, der findes.</li>
</ul>
<p>Vores <a href="../anmeldelseskort.html">Google Review-kort</a> har begge dele: NFC på forsiden og QR-kode på bagsiden. Læs mere om forskellen i <a href="nfc-eller-qr.html">NFC eller QR-kode?</a></p>

<h2>4. Sig det højt — én gang</h2>
<p>Et kort, der ligger fremme, bliver brugt. Et kort, som personalet nævner, bliver brugt markant mere. Det behøver ikke være mere end:</p>
<ul>
<li><em>"Hvis du har lyst, kan du lægge telefonen på kortet her — så kommer du direkte til vores Google-anmeldelser."</em></li>
</ul>
<p>Flere formuleringer til forskellige situationer finder du i <a href="saadan-beder-du-om-en-anmeldelse.html">Sådan beder du om en anmeldelse</a>.</p>

<h2>5. Spørg alle</h2>
<p>Det er fristende kun at spørge de kunder, der virker glade. Lad være. Google forbyder selektivt at opfordre til positive anmeldelser, og Forbrugerombudsmandens retningslinjer siger, at du ikke må sortere i, hvilke kunder der bliver opfordret til at anmelde.</p>
<p>Det er også bedre for dig. Et par kritiske anmeldelser blandt mange gode får profilen til at virke ægte.</p>

<h2>6. Mail og SMS efter købet</h2>
<p>Har du kundens kontaktoplysninger, kan en kort besked efter besøget supplere kortet. Hold den kort, personlig og med det direkte link.</p>
<p>Vær opmærksom på, at en opfordring sendt pr. mail eller SMS efter omstændighederne kan regnes som markedsføring, og så kræver den samtykke efter markedsføringslovens regler om elektronisk post. Spørg derfor kun kunder, der har sagt ja til at høre fra dig, og send ikke den samme opfordring flere gange.</p>

<h2>7. Svar på anmeldelserne</h2>
<p>Svar på både de gode og de dårlige. Et kort tak til de gode viser, at der er en person bag. Et roligt, konkret svar på de dårlige viser de næste kunder, at du tager det alvorligt. Læs <a href="daarlige-anmeldelser.html">Hvad gør du ved dårlige anmeldelser?</a></p>

<h2>Det du ikke må</h2>
<ul>
<li><strong>Give noget for anmeldelsen</strong> — rabat, gratis kaffe, lodtrækning. Forbudt efter Googles regler.</li>
<li><strong>Sortere kunderne</strong> og kun sende de tilfredse til Google.</li>
<li><strong>Skrive anmeldelser selv</strong> eller bede venner, familie eller ansatte om det. Falske anmeldelser er altid ulovlige efter markedsføringsloven.</li>
<li><strong>Presse kunden</strong> ved at stå og vente, mens de skriver.</li>
</ul>
<p>Hele gennemgangen står i <a href="regler-for-anmeldelser.html">Regler for Google-anmeldelser i Danmark</a>.</p>

<h2>Hvor mange anmeldelser skal man have?</h2>
<p>Der er ikke noget magisk tal. Det, der betyder noget, er hvordan du ser ud sammenlignet med de andre i dit område, og om anmeldelserne er nye. En profil med mange anmeldelser, hvor den seneste er to år gammel, ser mindre levende ud end én med færre, men nye.</p>
<p>Målet er derfor ikke et bestemt antal, men et jævnt flow: nogle nye anmeldelser hver måned, hele tiden.</p>

<h2>Sådan ser du, om det virker</h2>
<p>Skriv antallet af anmeldelser ned, den dag du begynder. Tjek igen efter fire uger. I din Google-virksomhedsprofil kan du også se, hvor mange der har set din profil, og hvor mange der har klikket på ruter, opkald og hjemmeside.</p>
<p>Kommer der ingen nye anmeldelser, er det næsten altid ét af tre problemer: kortet ligger det forkerte sted, ingen nævner det, eller linket fører til profilen i stedet for anmeldelsesfeltet.</p>"""),

    ("find-google-anmeldelseslink.html",
     "Find dit Google-anmeldelseslink",
     "Trin for trin: sådan finder du det link, der åbner anmeldelsesfeltet direkte — og hvad du gør, hvis det ikke virker.",
     "Find dit Google-anmeldelseslink — trin for trin",
     """<h2>Hvad er et Google-anmeldelseslink?</h2>
<p>Det er et link, der fører kunden direkte til feltet, hvor man giver stjerner og skriver en anmeldelse af din virksomhed. Ikke til din profil, hvor kunden selv skal finde knappen — men direkte til skrivefeltet.</p>
<p>Det er det link, du skal bruge på et Google Review-kort, en QR-kode, i en mail eller på din hjemmeside.</p>

<h2>Det skal du bruge</h2>
<p>En Google-virksomhedsprofil, som du har adgang til, og som er verificeret. Har du en virksomhed, der vises på Google Maps med adresse og åbningstider, findes profilen sandsynligvis allerede — spørgsmålet er bare, om du har adgang til den.</p>
<p>Har du ingen profil, kan du oprette den gratis hos Google. Den skal verificeres, før du kan få anmeldelser, og det tager typisk nogle dage.</p>

<h2>Sådan finder du linket på computeren</h2>
<ol>
<li>Log ind på den Google-konto, der administrerer din virksomhedsprofil.</li>
<li>Søg på din virksomheds navn i Google. Din profil vises øverst med værktøjer til at redigere den.</li>
<li>Find <em>Bed om anmeldelser</em> eller <em>Få flere anmeldelser</em>. Knappen kan ligge under <em>Anmeldelser</em> eller i menuen, alt efter hvordan Google viser profilen den dag.</li>
<li>Google viser et kort link. Tryk på <em>Kopiér</em>.</li>
</ol>
<p>Linket ser typisk sådan ud: <code>https://g.page/r/…/review</code>. Det er det, du skal bruge.</p>

<h2>Sådan finder du linket på telefonen</h2>
<ol>
<li>Åbn Google Maps-appen eller Google-appen, logget ind med kontoen, der administrerer profilen.</li>
<li>Gå til din virksomhedsprofil.</li>
<li>Find <em>Bed om anmeldelser</em> eller <em>Få flere anmeldelser</em>, og kopiér linket.</li>
</ol>

<h2>Test linket, før du bruger det</h2>
<p>Åbn linket i et privat browservindue eller på en telefon, der ikke er logget ind som dig. Det skal åbne anmeldelsesfeltet for din virksomhed — eventuelt efter at Google beder kunden logge ind, hvilket er normalt.</p>
<p>Står der et forkert firma, eller kommer du kun til profilen, så har du ikke det rigtige link.</p>

<h2>Hvis linket ikke virker</h2>
<ul>
<li><strong>Profilen er ikke verificeret.</strong> Uverificerede profiler kan ikke modtage anmeldelser. Færdiggør verificeringen først.</li>
<li><strong>Du har kopieret linket til profilen.</strong> Et link fra adresselinjen, mens du kigger på profilen, er ikke det samme som anmeldelseslinket. Brug knappen <em>Få flere anmeldelser</em>.</li>
<li><strong>Kunden er ikke logget ind på Google.</strong> Så beder Google dem logge ind først. Det er normalt, og det kan ikke undgås — man skal have en Google-konto for at skrive en anmeldelse.</li>
<li><strong>Linket er skrevet som tekst på et NFC-kort.</strong> Skal linket på et NFC-kort, skal det skrives som <em>URL/URI</em>, ikke som tekst. Ellers åbner iPhone ikke siden. Se <a href="../saet-det-op.html">Sæt kortet op selv</a>.</li>
</ul>

<h2>Reserveløsningen: link med Place ID</h2>
<p>Kan du ikke finde knappen, kan du bygge et anmeldelseslink ud fra din virksomheds <em>Place ID</em> — et id, Google giver hvert sted på kortet. Du finder det med Googles eget værktøj <em>Place ID Finder</em> i Google Maps-dokumentationen. Linket ser sådan ud:</p>
<p><code>https://search.google.com/local/writereview?placeid=DIT_PLACE_ID</code></p>
<p>Brug det kun som reserve. Det link, Google selv giver dig i profilen, er det sikreste.</p>

<h2>Lad os gøre det</h2>
<p>Bestiller du kort hos os, kan du bare sende os linket — eller navnet og adressen på din virksomhed — så finder vi det, koder kortene og tester dem, inden de bliver sendt. Det koster ikke ekstra.</p>"""),

    ("saadan-beder-du-om-en-anmeldelse.html",
     "Sådan beder du om en anmeldelse",
     "Formuleringer der virker ved disken, i en SMS og i en mail — og dem du skal undgå.",
     "Sådan beder du om en Google-anmeldelse — med eksempler",
     """<h2>Det korte svar</h2>
<p>Spørg, mens kunden er hos dig. Gør det til ét skridt. Sig det én gang, og spørg alle. Resten er formuleringer.</p>

<h2>Ved disken</h2>
<p>Ved disken handler det om at være kort og ikke stå og vente bagefter. Vælg én formulering, der lyder som dig:</p>
<ul>
<li><em>"Hvis du har lyst, kan du lægge telefonen på kortet her. Så kommer du direkte til vores Google-anmeldelser."</em></li>
<li><em>"Vi er en lille forretning, så en anmeldelse på Google hjælper os rigtig meget. Det tager ti sekunder med kortet her."</em></li>
<li><em>"Var du glad for det i dag? Så må du meget gerne skrive det på Google — bare hold telefonen her."</em></li>
</ul>
<p>Sig det, og gå videre. Kunden skal føle, at det er et tilbud, ikke en forventning.</p>

<h2>Til håndværkere og service ude hos kunden</h2>
<ul>
<li><em>"Så er vi færdige. Er du tilfreds, må du meget gerne give os en anmeldelse — hold bare telefonen her mod kortet."</em></li>
<li><em>"Vi får de fleste af vores nye kunder gennem Google, så hvis du har to minutter, betyder en anmeldelse meget for os."</em></li>
</ul>

<h2>I en SMS efter besøget</h2>
<p>Kort, personlig og med det direkte link. Send den samme dag, mens besøget er friskt:</p>
<blockquote><p>Hej Maria, tak fordi du kom forbi i dag. Hvis du har et øjeblik, vil vi blive rigtig glade for en anmeldelse på Google: [dit link]. Mvh. Sofie, Salon Lys</p></blockquote>
<p>Send kun SMS til kunder, der har sagt ja til at høre fra dig. En opfordring sendt elektronisk kan efter omstændighederne regnes som markedsføring, og så kræver den samtykke.</p>

<h2>I en mail</h2>
<blockquote><p><strong>Emne:</strong> Tak for i dag — har du to minutter?</p>
<p>Hej Jonas</p>
<p>Tak fordi du valgte os til badeværelset. Vi håber, du er glad for resultatet.</p>
<p>Vi får de fleste nye kunder gennem Google, så hvis du vil skrive et par ord om din oplevelse, betyder det meget for os: [dit link]</p>
<p>Og er der noget, du ikke er tilfreds med, så svar bare på denne mail — så ordner vi det.</p>
<p>Mvh. Kasper, Kaspers VVS</p></blockquote>
<p>Bemærk den sidste linje: den tilbyder en vej til at klage <em>ved siden af</em> anmeldelsen, ikke i stedet for. Det er i orden. Det, der ikke er i orden, er at sende utilfredse kunder et andet sted hen end de tilfredse.</p>

<h2>Tekst ved kortet</h2>
<p>Står kortet i en holder eller ved et lille skilt, så hold teksten kort:</p>
<ul>
<li><em>Hold telefonen her og giv os en anmeldelse på Google</em></li>
<li><em>Glad for besøget? Fortæl det på Google</em></li>
</ul>

<h2>Det du ikke skal sige</h2>
<ul>
<li><strong>"Giv os gerne fem stjerner."</strong> Du må ikke bede om en bestemt bedømmelse eller et bestemt indhold.</li>
<li><strong>"Du får 10 % rabat næste gang, hvis du anmelder os."</strong> Belønning for anmeldelser er forbudt.</li>
<li><strong>"Kan du ikke lige gøre det nu, mens jeg venter?"</strong> Det er pres. Google skriver, at man ikke bør presse kunder til at anmelde, mens de er i butikken.</li>
<li><strong>"Hvis du ikke var tilfreds, så skriv hellere til os."</strong> — sagt <em>i stedet for</em> at bede om en anmeldelse. Det er sortering.</li>
</ul>
<p>Læs hele gennemgangen i <a href="regler-for-anmeldelser.html">Regler for Google-anmeldelser i Danmark</a>.</p>

<h2>Gør det nemt at sige ja</h2>
<p>Den bedste formulering hjælper ikke, hvis kunden bagefter skal søge dig frem selv. Derfor virker et <a href="../anmeldelseskort.html">Google Review-kort</a> ved disken: kunden holder telefonen mod kortet, og anmeldelsesfeltet er åbent.</p>"""),
]

GUIDES_SEO += [
    ("qr-kode-til-google-anmeldelser.html",
     "Gratis QR-kode til Google-anmeldelser",
     "Sådan laver du en gratis QR-kode, der åbner dine Google-anmeldelser — og hvordan du undgår de fejl, der får den til at holde op med at virke.",
     "Gratis QR-kode til Google-anmeldelser — sådan laver du den",
     """<h2>Hvad er en QR-kode til Google-anmeldelser?</h2>
<p>Det er en almindelig QR-kode, der indeholder dit direkte Google-anmeldelseslink. Kunden scanner den med telefonens kamera, trykker på linket, og feltet til stjerner og anmeldelse åbner.</p>
<p>Koden er kun så god som linket i den. Start derfor med at finde det rigtige link: <a href="find-google-anmeldelseslink.html">Sådan finder du dit Google-anmeldelseslink</a>.</p>

<h2>Sådan laver du QR-koden gratis</h2>
<h3>1. Fra din Google-virksomhedsprofil</h3>
<p>Når du åbner <em>Bed om anmeldelser</em> eller <em>Få flere anmeldelser</em> i din profil, tilbyder Google i nogle visninger selv at hente en QR-kode. Er muligheden der, så brug den — så er du sikker på, at linket er rigtigt.</p>
<h3>2. Med Chrome eller Edge på computeren</h3>
<ol>
<li>Åbn dit anmeldelseslink i browseren.</li>
<li>Højreklik på siden, eller tryk på del-ikonet i adresselinjen.</li>
<li>Vælg <em>Opret QR-kode</em> (Chrome) eller <em>QR-kode til denne side</em> (Edge), og download billedet.</li>
</ol>
<p>Det er gratis, kræver ingen konto, og koden udløber aldrig.</p>
<h3>3. Med en QR-generator på nettet</h3>
<p>Der findes mange gratis generatorer. Vælg en, der laver en <strong>statisk</strong> QR-kode, og læs det med småt, før du bruger den.</p>

<h2>Statisk eller dynamisk QR-kode — den fælde du skal undgå</h2>
<p>En <strong>statisk</strong> QR-kode indeholder selve dit link. Den virker for evigt og kan ikke slukkes af nogen.</p>
<p>En <strong>dynamisk</strong> QR-kode indeholder et link til generatorens egen server, som så sender kunden videre. Fordelen er, at du kan ændre målet bagefter. Ulempen er, at koden holder op med at virke, hvis prøveperioden udløber, eller du stopper med at betale. Mange gratis generatorer laver dynamiske koder som standard og opkræver betaling senere.</p>
<p>Til et skilt eller et klistermærke, der skal sidde i årevis, er statisk det sikre valg.</p>

<h2>Hvor stor skal QR-koden være?</h2>
<p>En god tommelfingerregel: koden skal være mindst en tiendedel så bred som afstanden, den skal scannes fra. Skal kunden scanne fra 30 cm, er 3 × 3 cm nok. Hænger koden på en væg, kunden ser fra to meter, skal den være omkring 20 × 20 cm.</p>
<p>Under 2 × 2 cm bliver det besværligt for ældre telefoner.</p>

<h2>Det der ødelægger en QR-kode</h2>
<ul>
<li><strong>For lidt kontrast.</strong> Mørk kode på lys baggrund. Lys kode på mørk baggrund kan nogle kameraer ikke læse.</li>
<li><strong>Ingen kant.</strong> Koden skal have en hvid ramme hele vejen rundt — mindst fire af kodens små firkanter bred.</li>
<li><strong>Logo midt i koden.</strong> Det kan fungere, men jo større logoet er, jo flere telefoner giver op.</li>
<li><strong>Blank laminering.</strong> Genskin fra loftslys gør koden ulæselig fra visse vinkler. Mat er bedre.</li>
<li><strong>Bøjede overflader.</strong> En kode på en kop eller en flaske bliver forvrænget.</li>
</ul>

<h2>Test koden, før du trykker den</h2>
<p>Scan den med mindst to forskellige telefoner — gerne en iPhone og en Android — og fra den afstand, kunderne vil stå. Tjek at den åbner anmeldelsesfeltet for din virksomhed, ikke bare din profil eller en forkert virksomhed.</p>

<h2>QR-kode eller NFC?</h2>
<p>En QR-kode er gratis og virker på stort set alle telefoner. Men den kræver tre handlinger af kunden: åbn kamera, sigt, tryk på linket. Ved en travl disk er det ofte dér, folk giver op.</p>
<p>Med NFC holder kunden bare telefonen mod kortet, og siden åbner. Vores <a href="../anmeldelseskort.html">Google Review-kort</a> har begge dele — NFC på forsiden og QR-kode på bagsiden — så du får det hurtige uden at miste de ældre telefoner. Læs mere i <a href="nfc-eller-qr.html">NFC eller QR-kode?</a></p>"""),

    ("anmeldelseslink-virker-ikke.html",
     "Google-anmeldelseslinket virker ikke",
     "Linket åbner den forkerte side, kunden skal logge ind, eller NFC-kortet reagerer ikke? Her er de almindelige fejl, og hvordan du løser dem.",
     "Google-anmeldelseslink virker ikke? Sådan løser du det",
     """<h2>Find fejlen hurtigt</h2>
<p>Åbn linket i et privat browservindue — eller på en telefon, der ikke er logget ind som dig — og se, hvad der sker. Næsten alle problemer falder i en af grupperne herunder.</p>

<h2>Linket åbner din profil, men ikke anmeldelsesfeltet</h2>
<p>Du har sandsynligvis kopieret adressen fra adresselinjen, mens du kiggede på din profil. Det er et link til profilen, ikke til anmeldelsen. Kunden skal så selv finde knappen, og det gør de færreste.</p>
<p><strong>Løsning:</strong> Brug knappen <em>Få flere anmeldelser</em> eller <em>Bed om anmeldelser</em> i din virksomhedsprofil, og kopiér det link, Google giver dig der. Se <a href="find-google-anmeldelseslink.html">Find dit Google-anmeldelseslink</a>.</p>

<h2>Linket åbner en forkert virksomhed</h2>
<p>Det sker, når linket er bygget ud fra et forkert Place ID, eller når der findes to profiler for samme sted — for eksempel en gammel, som ingen har fjernet.</p>
<p><strong>Løsning:</strong> Hent linket igen fra den profil, du selv administrerer. Findes der en dubletprofil, kan du anmode Google om at fjerne den via <em>Foreslå en ændring</em> på Google Maps.</p>

<h2>Kunden bliver bedt om at logge ind</h2>
<p>Det er ikke en fejl. Man skal have en Google-konto for at skrive en anmeldelse, og er kunden ikke logget ind på telefonen, beder Google dem gøre det først. De fleste Android-telefoner er logget ind i forvejen. På iPhone sker det oftere, især i Safari.</p>
<p><strong>Det du kan gøre:</strong> Ingenting ved selve linket. Men det er en god grund til at bede om anmeldelsen ved disken, hvor kunden har tid, frem for i en mail de åbner i farten.</p>

<h2>Der står "Siden findes ikke", eller linket giver en fejl</h2>
<ul>
<li><strong>Profilen er ikke verificeret.</strong> Uverificerede profiler kan ikke modtage anmeldelser. Færdiggør verificeringen.</li>
<li><strong>Profilen er suspenderet.</strong> Så er anmeldelser lukket, indtil sagen er løst. Du kan se status i din virksomhedsprofil.</li>
<li><strong>Linket er kortet ned med en tjeneste, der er udløbet.</strong> Gælder også dynamiske QR-koder. Brug Googles eget link direkte.</li>
<li><strong>Linket er skrevet forkert af.</strong> Et enkelt manglende tegn er nok. Kopiér, skriv aldrig af.</li>
</ul>

<h2>NFC-kortet gør ingenting</h2>
<ul>
<li><strong>Telefonen er for gammel.</strong> iPhone 6s og ældre kan ikke læse NFC. iPhone 7, 8 og X kan kun, hvis brugeren selv åbner NFC-læseren i Kontrolcenter. Til dem er der QR-koden på bagsiden af kortet.</li>
<li><strong>NFC er slået fra (Android).</strong> Det slås til under indstillinger, typisk under <em>Forbindelser</em>.</li>
<li><strong>Skærmen er slukket eller låst.</strong> Telefonen skal være tændt og låst op.</li>
<li><strong>Telefonen holdes forkert.</strong> På iPhone sidder antennen i toppen. Hold toppen af telefonen mod kortet. På de fleste Android-telefoner sidder den midt på bagsiden.</li>
<li><strong>Tykt cover eller metal.</strong> Et cover med metalplade eller magnet kan blokere. Det samme gør et kort, der ligger på metal.</li>
<li><strong>Linket er skrevet som tekst.</strong> Er kortet programmeret med linket som <em>Tekst</em> i stedet for <em>URL/URI</em>, åbner iPhone ikke siden. Skriv det om — se <a href="../saet-det-op.html">Sæt kortet op selv</a>.</li>
</ul>

<h2>Anmeldelsen blev skrevet, men den kan ikke ses</h2>
<p>Google kontrollerer anmeldelser, før og efter de bliver vist. En anmeldelse kan være forsinket eller blive fjernet, hvis Googles systemer vurderer, at den bryder deres regler. Google oplyser sjældent hvorfor.</p>
<p>Det du kan gøre er at holde dig til reglerne: bed alle kunder — ikke kun de glade — giv aldrig noget for en anmeldelse, og bed aldrig om bestemte ord eller stjerner. Se <a href="regler-for-anmeldelser.html">Regler for Google-anmeldelser i Danmark</a>.</p>

<h2>Har du købt kort hos os?</h2>
<p>Så skriv til os, hvis kortet ikke virker. Vi har kodet og testet det før afsendelse, så vi finder fejlen sammen med dig — og omprogrammerer eller erstatter kortet, hvis det er os, der har lavet fejlen.</p>"""),
]

# Udvidet version af den korte NFC/QR-guide (erstatter brødteksten i build.py's GUIDES).
GUIDE_OVERRIDES = {
    "nfc-eller-qr.html": (
        "NFC eller QR-kode til Google-anmeldelser? Hvordan de virker, hvilke telefoner der kan hvad, rækkevidde, sikkerhed — og hvorfor du bør have begge dele.",
        """<h2>Den korte version</h2>
<p>NFC er hurtigere for kunden. QR virker på flere telefoner. Har du begge dele, får du det bedste fra hver — derfor har vores kort NFC på forsiden og en QR-kode på bagsiden.</p>

<h2>Sådan virker de to</h2>
<h3>NFC</h3>
<p>NFC står for <em>near field communication</em> — den samme teknik, der bruges til at betale med telefonen. Inde i kortet sidder en lille chip og en antenne uden batteri. Når telefonen kommer tæt på, giver telefonens felt chippen strøm nok til at sende det, den indeholder: dit anmeldelseslink. Telefonen viser linket, og kunden trykker én gang.</p>
<h3>QR-kode</h3>
<p>En QR-kode er et trykt mønster, som telefonens kamera kan aflæse. Kunden åbner kameraet, sigter, og telefonen viser linket, som kunden trykker på.</p>

<h2>Hvilke telefoner kan hvad?</h2>
<ul>
<li><strong>iPhone XS og nyere:</strong> Læser NFC i baggrunden. Kunden holder bare telefonen mod kortet.</li>
<li><strong>iPhone 7, 8 og X:</strong> Kan læse NFC, men kun hvis brugeren selv åbner NFC-læseren i Kontrolcenter. I praksis: brug QR-koden.</li>
<li><strong>iPhone 6s og ældre:</strong> Ingen NFC-læsning. QR-koden virker.</li>
<li><strong>Android:</strong> Langt de fleste har NFC. Det skal være slået til, og skærmen skal være tændt og låst op.</li>
<li><strong>QR-kode:</strong> Virker på reelt alle telefoner med kamera.</li>
</ul>
<p>Selv på nye iPhones læser telefonen ikke NFC i baggrunden, hvis den ikke har været låst op siden den blev tændt, hvis kameraet er i brug, eller hvis flytilstand er slået til.</p>

<h2>Hvor sidder antennen?</h2>
<p>På iPhone sidder NFC-antennen i toppen af telefonen. Kunden skal holde toppen mod kortet. På de fleste Android-telefoner sidder den midt på bagsiden. Rækkevidden er få centimeter — det er med vilje, så kortet kun reagerer, når kunden vil det.</p>

<h2>Hvornår NFC er bedst</h2>
<p>Ved disken, i receptionen og ved bordet — alle steder, hvor kunden står med telefonen i hånden og kun har få sekunder. Ét tryk i stedet for tre handlinger er forskellen på, at kunden gør det, og at de mener at ville gøre det senere.</p>

<h2>Hvornår QR-koden redder dig</h2>
<ul>
<li>Kunden har en ældre iPhone eller har NFC slået fra.</li>
<li>Koden skal ses på afstand — på en plakat, et vindue eller et menukort.</li>
<li>Den skal på tryksager: fakturaer, kvitteringer, flyers og emballage.</li>
</ul>

<h2>Kræver det internet?</h2>
<p>Kortet selv bruger hverken strøm eller internet. Men telefonen skal have internet for at åbne anmeldelsessiden, uanset om linket kommer fra NFC eller QR.</p>

<h2>Er det sikkert?</h2>
<p>Kortet indeholder kun et link. Det kan ikke læse noget fra kundens telefon, og det kan ikke trække penge. Kunden ser linket, før det åbner.</p>
<p>Kortet kan i princippet omprogrammeres af andre, hvis det ikke er beskyttet. Vores kort er låst med en kode, så kun du kan ændre linket — men du kan stadig selv ændre det, hvis du får brug for det.</p>

<h2>Hvad koster det?</h2>
<p>En QR-kode kan du lave gratis — se <a href="qr-kode-til-google-anmeldelser.html">Gratis QR-kode til Google-anmeldelser</a>. Et NFC-kort koster lidt mere, men holder i årevis og bliver brugt af hundredvis af kunder. Vores <a href="../anmeldelseskort.html">Google Review-kort</a> koster fra {P1} kr og har begge dele."""),
}
