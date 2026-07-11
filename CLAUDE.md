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
   **Excepție — senologia (Sân):** intervenționalul mamar (Tip `I`/`A`) rămâne în
   capitolul **Sân**, în situația de origine (senologia e specialitate proprie — analog
   excepției „cancerul de sân rămâne în Sân"). Vezi „Decizii deja luate".
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
   **Radiologie intervențională** (subcapitol de organ). Excepții: **ERCP** (Tip `D`)
   rămâne în capitolul de origine; **intervenționalul mamar** (biopsie percutanată,
   biopsie ganglionară axilară, localizare preoperatorie, drenaj abces) rămâne în
   capitolul **Sân** (senologie = specialitate proprie, analog cancerului de sân — regula 3).
3. **Determinată de malignitate** cunoscută/suspectată (stadializare, urmărire oncologică)
   → **Cancer**. Excepție: **cancerul de sân** rămâne în capitolul **Sân** (subcapitol
   „Cancer de sân") — Sânul e un capitol de specialitate (senologie), nu doar un aparat
   anatomic, și diagnosticul/stadializarea/urmărirea oncologică mamară sunt indisolubil
   legate de restul conținutului lui (screening, evaluare simptomatică). Analog excepției
   ERCP de la regula 2.
4. **Leziune traumatică acută** → **Traumatisme** (subcapitol **pe regiune anatomică**).
5. **Altfel** → **capitolul anatomic** (organ/aparat).

**Axa de nivel 2 (subcapitole) diferă pe fiecare capitol-context și e intențional așa:**
Traumatisme = **regiune anatomică + un set FIX de fațete cross-region** (vezi mai jos);
Cancer = **organ / sediu primar**; RI = **aparat / sistem**.
**Pediatrie = aparat / sistem + sub-bucket de context** pentru
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
- **Sub-axa Traumatisme = regiune anatomică + un set ÎNCHIS de fațete cross-region.**
  Capitolul e fundamental regional (cap, față, [gât], torace, abdomen, bazin și sacru,
  coloană cervicală, coloană toraco-lombară, membru superior, membru inferior). Se
  admit **doar 4 fațete non-regiune**, fiecare pentru că **traversează regiuni și are un
  workup coerent**: **Sistem vascular** (aortă + membre + cerebrovascular), **Politraumatism**
  (multi-regiune prin definiție), **Corp străin** (mecanism — poate fi oriunde), **Aparat
  urogenital** (renal + vezică + uretră + scrot; workup urologic unitar). **Setul e închis:**
  NU adăuga alte subcapitole organ-sistem în Traumatisme (dizolvarea unei fațete în regiuni
  ar fragmenta un topic coerent — ex. trauma urogenitală pe abdomen/bazin/perineu). Un
  organ care nu e una dintre aceste 4 fațete → merge la **regiunea** anatomică.

> **De reconfirmat de editori** (impact practic aproape nul): ordinea **Cancer vs
> Traumatisme** (pasul 3 înaintea pasului 4). Dacă un rând ar fi simultan oncologic și
> traumatic, câștigă contextul oncologic. Vezi `EDITORIAL-decisions.md`.

## Invarianți — trebuie să rămână adevărați după orice modificare

Rulează `python3 tools/validate.py` și verifică:

- `NR.CRT` **unic** și întreg pozitiv. Contiguitatea 1..N **nu** e obligatorie între
  sesiuni (găurile de după ștergeri sunt tolerate — vezi regula 3); `validate.py` o
  raportează ca avertisment. Se reface contiguitatea doar la o renumerotare cerută explicit.
- Fiecare rând are exact **13 coloane**.
- **0** rânduri cu Tip `I`/`A` în afara capitolului „Radiologie intervențională" **sau**
  „Sân" (excepția de senologie — intervenționalul mamar rămâne în Sân; `validate.py` acceptă
  ambele capitole-gazdă pentru Tip `I`/`A`).
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

## Plan de lucru — review pe capitol (checklist)

Procedura standard când se „analizează" un capitol (aplicată la Cardiovascular,
2026-07-08; refolosibilă la orice capitol). Ordinea contează: întâi lucruri mecanice
sigure, apoi normalizări verificate pe tot fișierul, apoi cazuri editoriale (flag, nu
decizie unilaterală).

1. **Corecturi ortografice.** Diacritice lipsă (`si`→`și`, `in`→`în`, `stang`→`stâng`,
   `redusa`→`redusă`, `diferential`→`diferențial` etc.) și typo-uri (`substațe`→
   `substanțe`, `bilațul`→`bilanțul`) — **doar** unde forma corectă e neambiguă. Cedila
   se verifică cu `validate.py` (invariant dur).
2. **Normalizare.** Spații parazite (inițiale/finale/duble) în `Tip`, `Examen`,
   `Situația Clinică`, `Comentarii`. Denumiri de examene aliniate la **convenția dominantă
   pe tot fișierul** (verificată statistic, nu doar în capitol): ex. `Echo`→`Eco`,
   `Echografie`→`Ecografie`, `Ecografia`→`Ecografie`, `toracală`→`toracică`. Anglicisme
   evitabile (`shunt`→`șunt`) doar dacă forma românească e deja folosită în capitol.
3. **Concordanță `Tip` ↔ `Examen`** (corectitudine): codul modalității trebuie să se
   potrivească denumirii (ex. `Eco Doppler` = `E`, `IRM` = `M`, `CT` = `T`). Coduri
   inversate = eroare de date, se corectează (nu e reordonare de examene).
4. **De-duplicare.** Situații identice ca sens dar scrise diferit **în același subcapitol**
   (variante de scriere, ex. „popliteale"/„poplitee") → se unifică eticheta situației
   (fără a comasa rândurile de examene, dacă examenele diferă). Duplicatele exacte de rând
   → `validate.py` le prinde; cele intenționate se listează în `DUPLICATE-review.md`.
5. **Reducerea exprimărilor redundante & repartizarea pe coloane.** Note clinice în
   `Comentarii` (col. 9), coduri/referințe în `Alte informații` (col. 10). Breadcrumb-urile
   („(vezi și …)") se scot din date (regula „un singur home / fără breadcrumb-uri").
   Comentariile identice legitime (aceeași situație) **se păstrează** (vezi „Decizii").
   **Informația clinică valabilă pentru toată situația se copiază în `Comentarii` pe
   fiecare investigație a situației** — rândurile se afișează separat (per examen), deci
   fiecare trebuie să fie auto-suficient pentru cititorul care vede o singură investigație.
   **Excepție:** nota strict specifică unei investigații (ce arată / cum se face *acea*
   modalitate) rămâne doar pe rândul ei. Practic: partea „despre boală / când se
   investighează / cadență de monitorizare" = pe toate; partea „despre acest examen" = doar
   pe el. (Complement al deciziei „comentariile identice se păstrează".)
6. **Consecvența subcapitolelor și situațiilor.** Verifică încadrarea pe ierarhia de
   capitole; etichete de situație bloatate cu note clinice de tip parantetic → propune
   mutarea notei în `Comentarii` (dacă e o notă pe toată situația, e caz editorial → flag).
7. **Ordonarea situațiilor clinice în cadrul unui subcapitol** urmează un **flux clinic**,
   nu ordinea alfabetică: **urgență/acut → cronic → screening/populații speciale**, cu
   `ALTĂ SITUAȚIE CLINICĂ` mereu ultima. Reordonare **fizică** a rândurilor (NR.CRT rămân
   atașate rândului, deci pot deveni necontigue până la o renumerotare cerută explicit —
   vezi regula 3). **Nu confunda cu ordinea *examenelor* în interiorul unei situații**, care
   rămâne intangibilă (vezi „Decizii deja luate").
8. **Verificarea corectitudinii informațiilor** față de practica curentă (ACR AC, RCR
   iRefer, ESC). **NU** se modifică grade sau doze; discrepanțele → `EDITORIAL-decisions.md`.
9. **Consemnare.** Fiecare modificare în `CHANGELOG.md` (la capitolul respectiv, cu
   etichetele din Legendă); fiecare chestiune lăsată deschisă în `EDITORIAL-decisions.md`.
   La final: `python3 tools/validate.py` verde + verificare diacritice.

**Reguli de aur reafirmate pe acest flux:** nu modific grade/doze/ordinea examenelor; nu
comasez comentarii identice legitime; nu decid singur cazuri clinice/editoriale ambigue
(le flag în `EDITORIAL-decisions.md`); dry-run înainte de orice operație în masă.

## Decizii deja luate (nu le relua fără a întreba)

- **ERCP (Tip `D`) rămâne în capitolele de origine** (nu se mută la RI), deși e
  intervențional. Marcat `Terapeutic = Da`.
- **Intervenționalul mamar rămâne în capitolul Sân** (nu se mută la RI), deși e Tip `I`/`A`.
  Senologia e specialitate proprie — procedurile mamare (biopsie percutanată, biopsie
  ganglionară axilară, localizare preoperatorie a leziunilor nepalpabile, drenaj de abces)
  stau în situația de origine din **Sân**, lângă restul workup-ului senologic (analog
  excepției „cancerul de sân rămâne în Sân"). Aplicat 2026-07-10: NR 1178 („Adenopatie
  axilară suspectă") și NR 1192 („Diagnosticul cancerului de sân…") mutate din `RI ›
  Oncologie` în `Sân › Paciente cu simptome și semne sugestive de cancer` (cod `RI - PC6`
  scos). `validate.py` acceptă Tip `I`/`A` și în Sân. Vezi `EDITORIAL-decisions.md` §15.B.
- **Cancerul de sân rămâne în capitolul Sân** (subcapitol „Cancer de sân"), nu se mută
  la Cancer, deși e determinat de malignitate. Excepție analogă ERCP — vezi ierarhia
  capitolelor, regula 3.
- **Coloana `Terapeutic`**: Da = are rol terapeutic *chiar dacă e și diagnostic*
  (fără o a treia valoare „mixt"). Ex: embolizare/ablație/drenaj = Da; biopsie/PCAFGE/
  angiografie diagnostică = Nu; reducerea invaginației prin clismă = Da.
- **Perechi duplicate păstrate intențional** (de studiat de editori — NU comasa):
  Ecografie „Suspiciune de masă pelvină" (grad C vs A) și Infiltrație „Rahialgie /
  Radiculalgie" (coduri PC5 vs PC7).
- **Ordinea indicațiilor (examenelor) în cadrul unei situații este intențională** —
  NU o reordona (nici „standardizat după iradiere"). Reflectă prioritatea clinică.
- **Ordonarea situațiilor clinice într-un subcapitol**: flux **urgență/acut → cronic →
  screening/populații speciale**, cu `ALTĂ SITUAȚIE CLINICĂ` mereu ultima — NU alfabetic
  (vezi checklist, pasul 7). Distinct de regula de mai sus: aici se reordonează *situațiile*
  (grupuri de rânduri), nu *examenele* din interiorul uneia. Aplicat prima dată la Aparat
  uro-genital, 2026-07-09 (reordonare fizică, NR.CRT neschimbate).
- **Comentariile identice pe rânduri diferite se păstrează.** Fiecare comentariu
  aparține unei situații; e normal ca rânduri (examene) diferite din aceeași situație
  să aibă comentariu identic. NU dedublica / rezuma — fiecare rând rămâne auto-suficient.
- **Informația clinică de nivel-situație se copiază pe toate investigațiile situației.**
  Reversul regulii de mai sus: dacă o notă descrie *situația clinică* (boala, când se
  investighează, cadența de monitorizare, echivalența dintre examene) și e prezentă doar
  pe unele rânduri, se **copiază în `Comentarii` pe toate rândurile situației** — fiindcă
  investigațiile se afișează separat. **Excepție:** nota strict specifică unei investigații
  (ce arată / cum se face acea modalitate) rămâne doar pe rândul ei.
- **Diagnosticul diferențial (și orice notă clinică) merge în coloana `Comentarii`
  (col. 9), NU în `Alte informații` (col. 10).** Per schemă: `Comentarii` = note clinice;
  `Alte informații` = coduri interne (ex. „RI - PCx") și referințe. O listă de diferențial
  e conținut clinic → `Comentarii` (căutarea o găsește oricum, indiferent de coloană).
- **Gradele de indicație NU se modifică.** Dacă un grad pare evident greșit, NU-l
  schimba singur — notează-l în `EDITORIAL-decisions.md` pentru decizia editorilor.

## Decizii încă deschise (în `EDITORIAL-decisions.md`)

- Artrografia articulației temporo-mandibulare (ATM): încadrare subcapitol (Sistem
  nervos vs Aparat locomotor) și dacă se păstrează (e „Neindicat", înlocuită de IRM).
- Cardiovascular (§12): ordinea examenelor la „Anevrisme vase periferice" după
  de-duplicare (Eco întâi?), nota clinică din eticheta „Arteriopatii periferice
  simptomatice", și gradul scintigrafiei osoase la amiloidoza transtiretină (NR 589).
- **MACRO — restructurarea capitolelor (§44):** întrebare de board, post-review. Propunere
  concretă de reparare a fragmentărilor transversale (fuziune `Cap›Neuro`+`Coloană` →
  „Sistem nervos"; `Cap›ORL`+`Gât` → „Cap și gât"; 14→13 capitole). NU se decide/începe
  înainte de aplicarea deciziilor editoriale pe conținut — ar fi ⛔ BREAKING și ar invalida
  maparea pachetelor. Vezi `EDITORIAL-decisions.md` §44.

## Maparea capitol origine → subcapitol RI (pentru mutări viitoare de intervențional)

Traumatisme→Traumatisme · Cancer→Oncologie · Aparat cardiovascular→Aparat cardiovascular ·
Torace→Aparat respirator · Aparat digestiv→Aparat digestiv · Aparat uro-genital→Aparat urogenital ·
Obstetrică-ginecologie→Aparat urogenital · **Sân→rămâne în Sân** (excepție de senologie —
NU se mută la RI; vezi „Decizii deja luate") · Cap→Sistem nervos ·
Gât→Aparat endocrin (dar „Masă cervicală"→Oncologie) · Coloană→Aparat locomotor (dar
embolizări spinale→Sistem nervos) · Aparat locomotor→Aparat locomotor.
