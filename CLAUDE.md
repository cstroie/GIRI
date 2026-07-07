# CLAUDE.md — GIRI

Context permanent pentru lucrul la ghidul de indicații radioimagistice în Claude Code.
Citește și `README.md` pentru schema completă a datelor.

## Ce este acest proiect

Un **fișier de date** (`GHID.csv`), nu o aplicație. Scopul: menținerea și curățarea
ghidului de indicații radioimagistice, cu istoric versionat pe Git. Aplicația de
consultare („IRIS") e separată și **nu** se regenerează din acest ghid acum.

## Reguli de aur

1. **`GHID.csv` este sursa canonică unică.** Orice modificare trece prin el.
2. **Diacritice românești corecte: ș/Ș, ț/Ț cu virgulă** — niciodată cedilă (ş/ţ).
   Verifică după orice editare masivă.
3. **`NR.CRT` e doar un ID de rând** (secvențial 1..N). Nu are semnificație clinică.
   Nu construi referințe externe pe el. Referă rândurile prin **Capitol + Situație clinică**.
   **NU renumerota automat** după ștergeri/comasări — renumerotarea produce un diff uriaș
   (fiecare rând ulterior se schimbă) și se face **doar la cerere explicită**. Între timp
   `NR.CRT` poate avea **găuri** (ex. după ștergerea unui rând); e acceptabil.
   `validate.py` semnalează găurile ca **avertisment** (nu eroare) — se ignoră; restul
   invarianților trebuie totuși să treacă. IDs trebuie să rămână **unice** și întregi.
4. **Tot ce e intervențional (Tip `I` și `A`) stă în capitolul „Radiologie
   intervențională".** Nu trebuie să reapară intervențional împrăștiat în capitolele
   diagnostice — procedurile terapeutice nu sunt opțiuni de diagnostic.
   (Caz particular al **ierarhiei de încadrare** — vezi secțiunea dedicată mai jos.)
5. **Documentează fiecare modificare în `CHANGELOG.md`**, la capitolul corespunzător.
   Marchează ⛔ BREAKING ce e incompatibil cu versiunea aprobată.
6. **Nu decide singur chestiunile clinice ambigue.** Încadrări de capitol discutabile,
   duplicate cu conținut diferit, cazuri pe muchie → `EDITORIAL-decisions.md` și
   întreabă. (Vezi „Decizii deja luate" mai jos.)

## Ierarhia capitolelor — unde „trăiește" un rând

Ghidul are **capitole anatomice** (organ/regiune) și **capitole-context / meta**:
**Pediatrie, Traumatisme, Cancer, Radiologie intervențională**. Navigarea pornește de la
context când contextul e special („pacientul e copil", „e un traumatism", „are cancer",
„e o procedură"), altfel de la anatomie. Un rând are mai multe fațete (context × anatomie),
dar **stă într-un singur loc**. Home-ul se decide aplicând regulile în ordine — **prima
care se potrivește câștigă**:

1. **Pacient pediatric** (indicațiile diferă pentru că e copil) → **Pediatrie**
   (inclusiv procedurile intervenționale pediatrice — ex. reducerea invaginației prin clismă).
2. **Procedură intervențională / terapeutică** (Tip `I` sau `A`), non-pediatrică →
   **Radiologie intervențională** (subcapitol de organ). Excepție: **ERCP** (Tip `D`)
   rămâne în capitolul de origine.
3. **Determinată de malignitate** cunoscută/suspectată (stadializare, urmărire oncologică)
   → **Cancer**.
4. **Leziune traumatică acută** → **Traumatisme** (subcapitol **pe regiune anatomică**).
5. **Altfel** → **capitolul anatomic** (organ/aparat).

**Axa de nivel 2 (subcapitole) diferă pe fiecare capitol-context și e intențional așa:**
Traumatisme = **regiune anatomică** (cap, față, gât, torace, abdomen, bazin, coloană,
membre, sistem vascular, politraumatism); Cancer = **organ / sediu primar**; RI =
**aparat / sistem**. **Pediatrie = aparat / sistem + sub-bucket de context** pentru
fațetele cross-cutting care nu se împrăștie pe aparate — momentan **„Traumatisme"** (trauma
pediatrică: cranio-cerebral, maltratare/NAI, abdominal, membre). Pediatrie e practic
„ghidul în miniatură": aparate pentru diagnostic + bucket(uri) de context. _De decis analog
pentru **oncologia pediatrică** (azi parțial în „Aparat digestiv" + breadcrumb la Cancer)._

**Consecințe de întreținere (de respectat la orice restructurare):**
- **Un singur home per rând.** Fără breadcrumb-uri („vezi capitolul X") împrăștiate în
  date — navigarea încrucișată după organ (peste capitole) e treaba aplicației de
  consultare (un index), nu a datelor. Consecvent cu eliminarea breadcrumb-urilor la
  consolidarea RI.
- **Fără subcapitole-husk.** Un subcapitol care conține **doar** rândul-placeholder
  Tip `Z` (nicio situație clinică reală) e o rămășiță după mutarea conținutului → se elimină.
- **Fără fațeta greșită ca subcapitol.** Nu crea subcapitole-context într-un capitol
  anatomic (ex. „Traumatisme abdominale" în „Aparat digestiv") — trauma stă în Traumatisme.

> **De reconfirmat de editori** (impact practic aproape nul): ordinea **Cancer vs
> Traumatisme** (pasul 3 înaintea pasului 4). Dacă un rând ar fi simultan oncologic și
> traumatic, câștigă contextul oncologic. Vezi `EDITORIAL-decisions.md`.

## Invarianți — trebuie să rămână adevărați după orice modificare

Rulează `python3 tools/validate.py` și verifică:

- `NR.CRT` **unic** și întreg pozitiv. Contiguitatea 1..N **nu** e obligatorie între
  sesiuni (găurile de după ștergeri sunt tolerate — vezi regula 3); `validate.py` o
  raportează ca avertisment. Se reface contiguitatea doar la o renumerotare cerută explicit.
- Fiecare rând are exact **13 coloane**.
- **0** rânduri cu Tip `I`/`A` în afara capitolului „Radiologie intervențională".
- **0** caractere cedilă (ş/Ş/ţ/Ţ).
- **0** duplicate exacte pe coloanele 2–12 (excluzând NR.CRT), cu excepția perechilor
  păstrate intenționat (vezi mai jos).
- `Terapeutic` ∈ {`Da`, `Nu`, ``(gol)}. Gol doar pentru rânduri placeholder (Tip `Z`).
- CSV valid: câmpurile cu virgulă/ghilimele/newline sunt între `"`, ghilimele interne dublate.

## Cum se editează

- Editări punctuale: direct în `GHID.csv`.
- Operații în masă (mutări, normalizări, coloane): scrie un script Python care
  parsează CSV cu modulul `csv` (nu regex pe linii — câmpurile conțin virgule și
  newline-uri). Fă întâi un **dry-run** care raportează ce s-ar schimba, apoi aplică.
- După orice editare: rulează validarea + verifică diacriticele.

## Decizii deja luate (nu le relua fără a întreba)

- **ERCP (Tip `D`) rămâne în capitolele de origine** (nu se mută la RI), deși e
  intervențional. Marcat `Terapeutic = Da`.
- **Coloana `Terapeutic`**: Da = are rol terapeutic *chiar dacă e și diagnostic*
  (fără o a treia valoare „mixt"). Ex: embolizare/ablație/drenaj = Da; biopsie/PCAFGE/
  angiografie diagnostică = Nu; reducerea invaginației prin clismă = Da.
- **Perechi duplicate păstrate intențional** (de studiat de editori — NU comasa):
  Ecografie „Suspiciune de masă pelvină" (grad C vs A) și Infiltrație „Rahialgie /
  Radiculalgie" (coduri PC5 vs PC7).
- **Ordinea indicațiilor (examenelor) în cadrul unei situații este intențională** —
  NU o reordona (nici „standardizat după iradiere"). Reflectă prioritatea clinică.
- **Comentariile identice pe rânduri diferite se păstrează.** Fiecare comentariu
  aparține unei situații; e normal ca rânduri (examene) diferite din aceeași situație
  să aibă comentariu identic. NU dedublica / rezuma — fiecare rând rămâne auto-suficient.
- **Gradele de indicație NU se modifică.** Dacă un grad pare evident greșit, NU-l
  schimba singur — notează-l în `EDITORIAL-decisions.md` pentru decizia editorilor.

## Decizii încă deschise (în `EDITORIAL-decisions.md`)

- Artrografia articulației temporo-mandibulare (ATM): încadrare subcapitol (Sistem
  nervos vs Aparat locomotor) și dacă se păstrează (e „Neindicat", înlocuită de IRM).

## Maparea capitol origine → subcapitol RI (pentru mutări viitoare de intervențional)

Traumatisme→Traumatisme · Cancer→Oncologie · Aparat cardiovascular→Aparat cardiovascular ·
Torace→Aparat respirator · Aparat digestiv→Aparat digestiv · Aparat uro-genital→Aparat urogenital ·
Obstetrică-ginecologie→Aparat urogenital · Sân→Oncologie · Cap→Sistem nervos ·
Gât→Aparat endocrin (dar „Masă cervicală"→Oncologie) · Coloană→Aparat locomotor (dar
embolizări spinale→Sistem nervos) · Aparat locomotor→Aparat locomotor.
