# CHANGELOG — GHID (versiunea „update")

Jurnal de modificări pentru **`update/GHID.csv`**, ramura de lucru a ghidului de
indicații radioimagistice.

> ⚠️ **ATENȚIE — versiune divergentă.** Această variantă se îndepărtează **mult** de
> versiunea aprobată. Modificările sunt **majore și incompatibile** cu ghidul
> canonic (`data/source/Ghid indicatii radioimagistice.csv`). Nu înlocuiește
> versiunea aprobată până la finalizarea review-ului.

- **Bază de plecare (baseline):** sursa canonică la 2026-07-06, după normalizarea
  abrevierii „Rg" → „Radiografie" / „Radiografia" (vezi `data/CHANGELOG-datasource.md`;
  inclusă în baseline, **nu** e o divergență a acestei versiuni).
- **Fișiere însoțitoare:**
  - `DUPLICATE-review.md` — evidența cvasi-duplicatelor (rezolvate + rămase de studiat).
  - `THERAPEUTIC-review.md` — cazurile duale/pe muchie pentru coloana nouă „Terapeutic".
  - `EDITORIAL-decisions.md` — chestiuni lăsate deschise pentru decizia comună a editorilor.
- **Scop document:** organizat **pe capitole**, ca fiecare capitol să poată fi trimis
  independent la review.

---

## Legendă

- **ADĂUGAT** — situație / examen / rând nou.
- **MODIFICAT** — schimbare de conținut într-un rând existent.
- **ELIMINAT / COMASAT** — rând scos, respectiv contopit cu un duplicat identic.
- **MUTAT** — rând relocat în alt capitol (fără schimbare de conținut clinic).
- **RESTRUCTURAT** — reorganizare (subcapitole, ordine).
- **⛔ BREAKING** — schimbare incompatibilă cu versiunea aprobată.

> ⚠️ **NR.CRT au fost renumerotate integral 1..1488.** Numerotarea veche (din versiunea
> aprobată) nu se mai păstrează — referințele se fac prin capitol + situație clinică.

---

## Structura ghidului (după modificări — 14 capitole, 1526 rânduri, 13 coloane)

> **NR.CRT nu se renumerotează automat** (vezi `CLAUDE.md`). Ștergerile lasă găuri, iar
> inserțiile primesc ID-uri la finalul secvenței — deci coloana NR.CRT de mai jos e
> **indicativă** și unele capitole au și ID-uri neconsecutive. Referă rândurile prin
> **Capitol + Situație clinică**, nu prin NR.CRT.

| # | Capitol | NR.CRT | Rânduri |
|---|---|---|---|
| 1 | [Pediatrie](#1-pediatrie) | 1–155 (fără 113) · 1488–1527 | 194 |
| 2 | [Traumatisme](#2-traumatisme) | 156–278 · 1486–1487 | 125 |
| 3 | [Cancer](#3-cancer) | 279–514 | 236 |
| 4 | [Aparat cardiovascular](#4-aparat-cardiovascular) | 515–601 | 87 |
| 5 | [Torace](#5-torace) | 602–676 | 75 |
| 6 | [Aparat digestiv](#6-aparat-digestiv) | 677–803 | 127 |
| 7 | [Aparat uro-genital și glande suprarenale](#7-aparat-uro-genital-și-glande-suprarenale) | 804–872 | 69 |
| 8 | [Obstetrică și ginecologie](#8-obstetrică-și-ginecologie) | 873–899 | 27 |
| 9 | [Sân](#9-sân) | 900–955 | 56 |
| 10 | [Cap](#10-cap) | 956–1075 | 120 |
| 11 | [Gât (părți moi)](#11-gât-părți-moi) | 1076–1093 | 18 |
| 12 | [Coloană vertebrală](#12-coloană-vertebrală) | 1094–1148 | 55 |
| 13 | [Aparat locomotor](#13-aparat-locomotor) | 1149–1235 | 87 |
| 14 | [Radiologie intervențională](#14-radiologie-intervențională) | 1236–1485 | 250 |

---

## Modificări globale (cross-capitol)

### RESTRUCTURAT — Ierarhia capitolelor (regula de încadrare) + eliminare husk-uri

- **Consemnată explicit ierarhia de încadrare** (unde „trăiește" un rând) în `CLAUDE.md`:
  capitole-context (Pediatrie, Traumatisme, Cancer, RI) au prioritate față de anatomie,
  în cascada Pediatrie → RI (Tip I/A) → Cancer → Traumatisme → anatomic. Un rând stă
  într-**un singur** loc; fără breadcrumb-uri în date; fără subcapitole-husk; fără fațeta
  greșită ca subcapitol (ex. „Traumatisme" într-un capitol anatomic).
- **ELIMINAT — subcapitole-husk** (conțineau doar rândul-placeholder Tip `Z`, fără nicio
  situație clinică reală — rămășițe după mutarea conținutului):
  - „Traumatisme › **Aparat digestiv**" (conținutul de traumă abdominală e în „Abdomen").
  - „Aparat digestiv › **Traumatisme abdominale**" (trauma abdominală stă în capitolul
    Traumatisme — anti-pattern context-în-anatomie). (−2 rânduri; renumerotare 1..1485)
- **Semnalate, de confirmat** (alte 2 husk-uri, în capitole încă nerevizuite): „Aparat
  digestiv › Abdomen" și „Aparat uro-genital › Uter și anexe" (conținut uter în
  Obstetrică-ginecologie / Cancer). Vezi `EDITORIAL-decisions.md` §5.1.

### ADĂUGAT — Coloană nouă „Terapeutic" (Da/Nu)

- Adăugată coloana **„Terapeutic"** la **finalul** rândului (coloana 13), pentru un
  label în aplicație. Valori: **Da / Nu**, gol pentru placeholder-ele „situație
  neîncadrabilă". Regula: **Da = are rol terapeutic**, chiar dacă e *și* diagnostic —
  astfel cazurile duale (ERCP, „Angiografie cu sau fără embolizare", colangiografie cu
  drenaj) sunt Da fără a inventa o a treia valoare.
- Ortogonală pe Tip: printre intervenționale, biopsiile / PCAFGE / angiografia
  diagnostică / artrografia rămân **Nu**; embolizare / ablație / angioplastie / drenaj /
  vertebroplastie / TIPS etc. sunt **Da**.
- Singurul caz terapeutic **în afara** intervenționalului: reducerea invaginației prin
  clismă sub control eco/fluoroscopic (Pediatrie) → **Da**.
- Rezultat: **140 Da · 1246 Nu · 102 gol**. Cazurile duale/pe muchie de validat →
  `THERAPEUTIC-review.md`.

### ⛔ BREAKING — Consolidarea radiologiei intervenționale (2026-07-06)

**Problema:** proceduri **terapeutice** (embolizare, ablație, angioplastie, protezare,
drenaj, vertebroplastie, PCAFGE etc.) erau împrăștiate în **toate** capitolele
diagnostice, deseori prezentate ca **prima sau singura** opțiune — periculos, fiind
tratamente, nu investigații diagnostice.

**Ce s-a făcut:**

1. **Identificare.** Semnalul intervențional e purtat curat de codurile din coloana
   **Tip**: `I` (intervențional) și `A` (angiografie invazivă). Verificat că nicio
   procedură terapeutică nu se ascunde sub coduri diagnostice.
2. **Mutare — 243 rânduri** relocate din cele 12 capitole diagnostice în
   **Radiologie intervențională**, remapate pe subcapitolul de organ corespunzător.
   Nu a rămas **niciun** rând intervențional (I/A) în afara capitolului RI (verificat = 0).
   - **Tip A** (angiografie invazivă) mutat integral la RI (decizie de review).
   - **Tip D** (ecoendoscopie, osteodensitometrie, videocapsulă, ERCP) **nelăsat neatins**
     în capitolele de origine (decizie de review; sunt majoritar diagnostice).
   - Cele **136 situații clinice pur-terapeutice** (unde intervenționalul era singura
     opțiune) s-au mutat **integral** la RI; nu rămâne breadcrumb în capitolul de origine.
3. **Comasare duplicate exacte — 160 rânduri** eliminate: rânduri identice pe toate
   coloanele (cu excepția NR.CRT). Majoritatea (148) erau proceduri deja prezente în RI
   **și** duplicate în capitolul de origine; 11 erau identice între două capitole de
   origine; 1 redundanță preexistentă. Cvasi-duplicatele **nu** s-au atins → `DUPLICATE-review.md`.
4. **Renumerotare** NR.CRT 1..1488 (secvențial; numerotarea veche nu se păstrează).

**Mapare capitol origine → subcapitol RI:**
Traumatisme→Traumatisme · Cancer→Oncologie · Ap. cardiovascular→Ap. cardiovascular ·
Torace→Ap. respirator · Ap. digestiv→Ap. digestiv · Ap. uro-genital→Ap. urogenital ·
Obstetrică-ginecologie→Ap. urogenital · Sân→Oncologie · Cap→Sistem nervos ·
Ap. locomotor→Ap. locomotor. **Excepții pe rând** (plasare clinică, nu pe capitol):
Gât→Ap. endocrin (tiroidă/paratiroidă), dar „Masă cervicală" → Oncologie;
Coloană→Ap. locomotor (vertebroplastie, biopsie, infiltrație), dar embolizările
spinale (MAV, tumori hipervascularizate) → Sistem nervos.

**Rânduri mutate, pe capitol de origine:** Traumatisme 18 · Cancer 19 ·
Ap. cardiovascular 54 · Torace 11 · Ap. digestiv 62 · Ap. uro-genital 19 ·
Obstetrică-ginecologie 3 · Sân 4 · Cap 25 · Gât 8 · Coloană 7 · Ap. locomotor 13.

### MODIFICAT — Erori de date corectate

- **Angio-RM** era etichetat `Tip=A` (fals intervențional; e angio-RM neinvaziv,
  diagnostic) → corectat la `Tip=M`; în consecință **nu** s-a mutat la RI. (1 rând)
- **Ecoendoscopie** — variante de scriere „Echoendoscopia" / „Ecoendoscopia" /
  „Ecoendoscopie " (spațiu) → unificate la „Ecoendoscopie". (3 rânduri)
- **Rânduri-junk** cu artefact software în coloana Examen („Refaceti selectia: …!")
  → golit textul parazit; rândul-punte de trimitere către alt capitol rămâne. (3 rânduri)

### MODIFICAT — Normalizarea coloanei Subcapitol

- „Ficat, colecist și pancreas" (Cancer + Aparat digestiv): 90 rânduri cu cedila „şi"
  unificate la „și" — 102 rânduri total. Vezi și intrările pe capitole.

### ⛔ BREAKING — Diacritice pe tot documentul

- Normalizate la forma corectă cu virgulă **ș/Ș, ț/Ț** (nu cedilă), pe întregul fișier.
  **2123 caractere** înlocuite. Neutru semantic, dar diff masiv.

### MODIFICAT — Rezolvarea cvasi-duplicatelor

După consolidarea intervenționalului au rămas perechi aproape identice (același rând
 dublat la mutare: o versiune cu diacritice și una veche fără; codul intern „RI - PCx"
 uneori doar pe una). Decizii luate cu editorul:

- **7 perechi comasate** (păstrând textul cu diacritice + codul „RI - PCx" ne-gol):
  PCAFGE masă cervicală · Angiografie convențională (tumori vasculare) · Arteriografie cu
  embolizare (traumatisme hepatice) · PCAFGE hipertiroidie · PCAFGE hipotiroidie ·
  Biopsie formațiune părți moi · Biopsie formațiune osoasă. (−7 rânduri)
- **2 perechi păstrate ca duplicate** (de studiat de editor, lăsate neatinse):
  - Ecografie „Suspiciune de masă pelvină" (NR 889 și 890) — comentarii și grad diferite
    (C vs A), par două intrări legitime.
  - Infiltrație „Rahialgie / Radiculalgie" (NR 1472 și 1473) — coduri diferite PC5 vs PC7.

### MODIFICAT — Uniformizarea formulărilor din „Situația Clinică"

**16 grupuri** de situații scrise diferit în același subcapitol au fost uniformizate la o
formă canonică (cu diacritice, majusculă inițială, fără spații parazite). Nu s-au comasat
rânduri — doar textul situației. Exemple:

- „monitorizare" → „Monitorizare"; „stadializare" → „Stadializare"; „diagnostic" → „Diagnostic";
  „urmarire" → „Urmărire"
- „Anevrism aorta abdominală…" → „Anevrism aortă abdominală…"; „Stenoza carotidiana…" →
  „Stenoză carotidiană…"; „Necroza aseptica de cap femural" → „Necroza aseptică…"
- „Bilant fractura vertebrala spontana" → „Bilanț fractură vertebrală spontană"; „Fasceita
  plantara" → „Fasceita plantară"; „Artropatie inflamatorie – bilant initial" → „…bilanț inițial"
- eliminare spații inițiale/finale la „ Hemoragie gastro-intestinală ocultă – bilanț",
  „ Stadializarea cancerului de sân: metastaze la distanță", „ Suspiciune clinică de cancer…"

---

## 1. Pediatrie
_NR 1–155 · 1488–1505_

- **RESTRUCTURAT — subcapitol nou „Oncologie"** (al doilea bucket de context, ca la
  Traumatisme). Relocate cele **4 rânduri** „Masă abdominală sau pelvină palpabilă"
  (workup de neuroblastom / nefroblastom) din „Aparat digestiv" → `Pediatrie › Oncologie`.
  Adăugat placeholder structural (NR 1505). NR.CRT păstrate (fără renumerotare).
  - **Rămâne în „Gât și coloană"**: „Adenopatii cervicale" (NR 66) — la copil e încadrată
    ca patologie **inflamatorie/infecțioasă** (vezi comentariul), nu oncologică; nu se mută.
- **ADĂUGAT — 4 situații de oncologie pediatrică** în `Pediatrie › Oncologie` (11 rânduri
  noi, NR 1506–1516; indicații/grade aliniate la ACR AC pediatric, RCR iRefer — accent pe
  IRM și limitarea iradierii):
  - **Tumori cerebrale și medulare** (2): IRM cerebral ± medular cu contrast (*Indicat, A* —
    referință, cranio-spinal la risc de diseminare), CT cerebral (*Doar în cazuri
    particulare, B* — urgență / IRM indisponibil).
  - **Limfom (Hodgkin / non-Hodgkin) – bilanț și stadializare** (4): CT cervico-toraco-abdomino-pelvin
    (*Indicat, B*), PET-CT F18-FDG (*Indicat, B*), Ecografie (*Doar în cazuri particulare, B*),
    IRM (*Doar în cazuri particulare, B*).
  - **Tumori osoase (osteosarcom, sarcom Ewing)** (4): Radiografie (*Indicat, A*), IRM segment +
    os întreg (*Indicat, A*), CT toracic (*Indicat, B* — metastaze pulmonare), Scintigrafie
    osoasă / PET-CT (*Doar cu aviz specializat, B*).
  - **Neuroblastom – stadializare** (1): Scintigrafie MIBG I-123 (*Indicat, A* — trasor specific).
- **ELIMINAT — breadcrumb-ul NR 113** („Tumori – vezi Capitolul Cancer", rând-stub Tip Z fără
  conținut) — înlocuit de situația reală „Tumori cerebrale și medulare la copil". Ștergere
  fără renumerotare → NR.CRT are o gaură la 113 (tolerată; `validate.py` o semnalează ca
  avertisment).
- **ADĂUGAT — încă 3 situații de oncologie pediatrică** în `Pediatrie › Oncologie` (11 rânduri
  noi, NR 1517–1527):
  - **Retinoblastom (leucocorie / strabism)** (3): IRM orbite și cerebral cu contrast
    (*Indicat, A* — referință), Ecografie oculară (*Indicat, B*), **CT orbite (*Neindicat, B*)** —
    de evitat la copil (iradiere oculară + risc de a doua neoplazie la purtătorii RB1).
  - **Rabdomiosarcom / sarcom de părți moi** (4): IRM regiune primară (*Indicat, A*), CT toracic
    (*Indicat, B* — metastaze pulmonare), PET-CT (*Doar cu aviz specializat, B*), Ecografie
    (*Doar în cazuri particulare, B*).
  - **Histiocitoză cu celule Langerhans (LCH)** (4): Radiografie os/craniu (*Indicat, B*),
    IRM regiune + SNC (*Indicat, B* — axă hipotalamo-hipofizară / diabet insipid), PET-CT
    (*Doar cu aviz specializat, B*), Radiografie toracică (*Doar în cazuri particulare, C*).
- **MODIFICAT — enriched „Masă abdominală sau pelvină palpabilă"** (NR 22–25): adăugat în
  „Comentarii" diagnosticul diferențial (nefroblastom/Wilms, neuroblastom, hepatoblastom,
  limfom Burkitt, tumori germinale/teratom, nefrom mezoblastic) — astfel o **căutare** după numele
  tumorii întoarce situația de masă abdominală. Plasat în „Comentarii" (note clinice, per schemă),
  nu în „Alte informații" (rezervat codurilor interne / referințelor). (4 rânduri modificate.)

- **ADĂUGAT — 5 situații de traumă pediatrică lipsă** în `Pediatrie › Traumatisme`
  (16 rânduri noi, NR 1489–1504; indicații/grade aliniate la ACR Appropriateness
  Criteria pediatric, RCR iRefer, PECARN, Image Gently — accent pe eco/IRM și limitarea
  iradierii la copil):
  - **Traumatism abdominal major** (4): Ecografie FAST (*Indicat, B*), CT abdomino-pelvin
    cu contrast (*Indicat, B*), CEUS (*Doar cu aviz specializat, B*), Radiografie
    abdominală (*Neindicat, C*). _O eco FAST negativă nu exclude leziunea de organ solid._
  - **Traumatism de coloană cervicală** (3): Radiografie (*Indicat, B*), CT (*Doar în
    cazuri particulare, B*), IRM (*Doar cu aviz specializat, B* — deficit / ligamentar /
    SCIWORA).
  - **Traumatism toracic** (3): Radiografie (*Indicat, B*), Ecografie eFAST (*Doar în
    cazuri particulare, B*), CT (*Doar cu aviz specializat, B*).
  - **Traumatism de membru – suspiciune de fractură** (3): Radiografie (*Indicat, A* —
    Salter-Harris), Ecografie (*Doar în cazuri particulare, B*), IRM (*Doar cu aviz
    specializat, B*).
  - **Politraumatism pediatric** (3): Ecografie eFAST (*Indicat, B*), Radiografie torace+bazin
    (*Indicat, B*), CT țintit pe regiuni (*Indicat, B* — mai selectiv decât whole-body CT).
- **MODIFICAT — retras breadcrumb-ul** de pe „Traumatism abdominal minor" (trimitea la
  capitolul adult pentru forma majoră); acum forma majoră e subcapitol-soră pediatric.
  Perechea redenumită simetric: „Traumatism abdominal minor / major la copil".
- **RESTRUCTURAT** — subcapitolul reordonat cranio-caudal (cap → coloană → torace →
  abdomen → membre → politraumatism → maltratare).

- **RESTRUCTURAT — subcapitol nou „Traumatisme"** (context bucket, ca la capitolele-meta):
  trauma pediatrică era împrăștiată pe aparate; s-au **relocat 12 rânduri** (fără schimbare
  de conținut clinic) în noul subcapitol `Pediatrie › Traumatisme`:
  - `Traumatism cranio-cerebral la copil` (4 rânduri, din „Sistem nervos central");
  - `Traumatism nonaccidental – Maltratare` (5 rânduri, din „Aparat locomotor");
  - `Traumatism abdominal minor` (2 rânduri, din „Aparat digestiv");
  - `Traumatism unilateral de membru – comparativ` (1 rând, din „Aparat locomotor").
  Eliminat **breadcrumb-ul intern** (Sistem nervos → Aparat locomotor pentru NAI) — situația
  „Traumatism cranio-cerebral la copil" e curățată de paranteza de trimitere, NAI fiind acum
  subcapitol-soră. Adăugat placeholder-ul structural (NR 1488). NR.CRT păstrate (fără
  renumerotare). Motivație și ierarhie → `CLAUDE.md` › „Ierarhia capitolelor".
- **MODIFICAT (date) —** corecturi ortografice și de tipar pe ~25 de rânduri
  (ex. „Examentul"→„Examenul", „Apatrat"→„Aparat" în titlurile NR 109–112,
  „paraverterale"→„paravertebrale", „documnetată"→„documentată", „hipetricoza"→
  „hipertricoza") și diacritice-ț lipsă („mictional"→„micțional", „infectie"→„infecție",
  „functie"→„funcție", „in"→„în"). Fără schimbare de sens clinic.
- **MODIFICAT (date) —** normalizat câmpul „Examen" multi-linie la scintigrafii
  (NR 47, 55, 61, 71 — osoasă; NR 130, 137, 140 — renală): eliminat newline-urile și
  liniile goale reziduale, „WB si"→„WB și".
- _Analiza editorială și omisiunile de patologie → `EDITORIAL-decisions.md` §3–4
  (propuneri de adăugat + întrebări de stil; nicio inserare de rânduri noi în date)._

## 2. Traumatisme
_NR 156–278 · 1486–1487_

- **MUTAT —** 18 rânduri intervenționale (Tip I/A) relocate la RI › Traumatisme.
- **MODIFICAT (date) —** subcapitol „Bazin și/şi sacru" unificat la forma majoritară cu cedilă „şi".
- **MODIFICAT (date) — corecturi ortografice și de tipar (10 rânduri).** Diacritice
  lipsă: „si"→„și" (NR 178, 179 — Examen; NR 206 — Comentarii), „Daca"→„Dacă"
  (NR 205 Comentarii, NR 222 Alte informații), „electie"→„elecție" (NR 206);
  proper noun „Otawa"→„Ottawa" (criteriile Ottawa; NR 249, 250, aliniat la NR 251);
  spațiere: „prealabilă ,timpi"→„prealabilă, timpi" (NR 167 Examen),
  „toraco - lombară"→„toraco-lombară" (NR 212 Examen, aliniat la rândurile-soră).
  Fără schimbare de sens clinic.
- **MODIFICAT (date) — normalizare whitespace pe câmpuri-cheie** (Situație / Examen):
  eliminate spații finale la „…esofagian înalt" (NR 218–220), „Traumatism de pumn"
  (NR 258–261) și „Ecografie" (NR 266). Nu afectează gruparea (spațiul era pe toate
  rândurile din grup).
- **ELIMINAT / COMASAT —** cvasi-duplicatul **NR 178/179** (Cap, „Traumatism cranio-encefalic",
  PET-CT/SPECT) comasat: rândurile difereau doar prin „PET-CT" vs „PET" în Comentarii; s-a
  păstrat varianta „PET-CT" (aliniată la eticheta Examen). (−1 rând)
- **ELIMINAT — subcapitol-husk „Aparat digestiv"** (conținea doar rândul-placeholder
  Tip Z, fără situație reală). Trauma abdominală stă în subcapitolul „Abdomen".
  (Vezi Modificări globale › Ierarhia capitolelor.) (−1 rând)
- **ADĂUGAT — „Traumatism vascular al membrelor"** (subcapitol „Sistem vascular", care
  acoperea doar aorta toracică): Angio-CT de membru = *Indicat, grad B* (doza 2/3);
  Ecografie Doppler de membru = *Doar în cazuri particulare, grad B* (doza 0/0). Ambele
  diagnostice (Terapeutic = Nu). Rânduri noi **NR 1486/1487** (ID-uri la finalul secvenței —
  fără renumerotare, vezi CLAUDE.md). (+2 rânduri)
- **VERIFICAT (nemodificat) — „lemn pictat"** (Corp străin, NR 219/220). Sursa canonică
  originală conține **deliberat** „lemn pictat" (nu e typo — lemnul vopsit are altă
  radioopacitate decât cel simplu); formularea se **păstrează**.
- **REVIZUIT — fără rânduri noi** pentru: stratificarea traumatismului cranian (Canadian
  CT Head Rule — opțiunile imagistice sunt aceleași, stratificarea e clinică, nu un rând
  nou); fractura de bazin instabilă (deja acoperită — stabil în „Traumatism izolat de
  bazin", instabil → embolizare la RI); granularitate membre (claviculă / mână / femur /
  gambă — acoperite implicit de radiografia regională).

## 3. Cancer
_NR 279–514_

- **MUTAT —** 19 rânduri intervenționale relocate la RI › Oncologie.
- **MODIFICAT (date) —** subcapitol „Ficat, colecist şi pancreas" normalizat (vezi Modificări globale).

## 4. Aparat cardiovascular
_NR 515–601_

- **MUTAT —** 54 rânduri intervenționale (embolizări, angioplastii, protezări,
  angiografie invazivă) relocate la RI › Aparat cardiovascular. Capitolul se reduce
  substanțial (rămân investigațiile diagnostice).

## 5. Torace
_NR 602–676_

- **MUTAT —** 11 rânduri intervenționale relocate la RI › Aparat respirator.

## 6. Aparat digestiv
_NR 677–803_

- **ELIMINAT — subcapitol-husk „Traumatisme abdominale"** (conținea doar rândul-placeholder
  Tip Z). Anti-pattern context-în-anatomie: trauma abdominală stă în capitolul Traumatisme,
  nu în Aparat digestiv. (Vezi Modificări globale › Ierarhia capitolelor.) (−1 rând)
- _Semnalat, de confirmat: subcapitol-husk „Abdomen" (doar placeholder) → `EDITORIAL-decisions.md` §5.1._

- **MUTAT —** 62 rânduri intervenționale relocate la RI › Aparat digestiv.
- **MODIFICAT (date) —** eticheta „Aparat digestiv " (spațiu în plus, 5 rânduri) unificată sub „Aparat digestiv".

## 7. Aparat uro-genital și glande suprarenale
_NR 804–872_

- **MUTAT —** 19 rânduri intervenționale relocate la RI › Aparat urogenital.

## 8. Obstetrică și ginecologie
_NR 873–899_

- **MUTAT —** 3 rânduri intervenționale relocate la RI › Aparat urogenital.
- **MODIFICAT (date) —** subcapitol „Sarcina"/„Sarcină" unificat la „Sarcină" (majoritar).

## 9. Sân
_NR 900–955_

- **MUTAT —** 4 rânduri intervenționale relocate la RI › Oncologie.
- **MODIFICAT (date) —** spații finale parazite pe „…cancer  " eliminate (12 rânduri).

## 10. Cap
_NR 956–1075_

- **MUTAT —** 25 rânduri intervenționale (neurovasculare) relocate la RI › Sistem nervos.

## 11. Gât (părți moi)
_NR 1076–1093_

- **MUTAT —** 8 rânduri intervenționale (PCAFGE) relocate la RI: tiroidă/paratiroidă
  → Aparat endocrin; „Masă cervicală" → Oncologie.

## 12. Coloană vertebrală
_NR 1094–1148_

- **MUTAT —** 7 rânduri intervenționale relocate la RI: vertebroplastie / biopsie /
  infiltrație → Aparat locomotor; embolizări spinale → Sistem nervos.

## 13. Aparat locomotor
_NR 1149–1235_

- **MUTAT —** 13 rânduri intervenționale relocate la RI › Aparat locomotor.

## 14. Radiologie intervențională
_NR 1236–1485 (250 rânduri)_

- **RESTRUCTURAT —** capitolul primește cele 243 rânduri mutate din restul ghidului,
  grupate pe cele 9 subcapitole de organ. După comasarea a 160 duplicate exacte (mutare)
  + 7 cvasi-duplicate rezolvate ulterior, totalul RI = **250 rânduri**.
- Subcapitole (rânduri): Traumatisme 19 · Oncologie 30 · Ap. cardiovascular 57 ·
  Ap. respirator 13 · Ap. digestiv 53 · Ap. urogenital 23 · Sistem nervos 28 ·
  Ap. endocrin 7 · Ap. locomotor 20.

---

## De discutat / decizii deschise pentru reviewer

- **ERCP rămas în origine (decizie luată).** ERCP (Tip D) **nu** se mută la RI, rămâne
  în capitolele de origine; în coloana „Terapeutic" e marcat **Da**. Vezi `EDITORIAL-decisions.md`.
- **Artrografia ATM — decizie editorială deschisă.** Rândurile de artrografie temporo-
  mandibulară (NR 1460, 1461 în RI›Sistem nervos; NR 1358 în RI›Aparat digestiv) au
  încadrarea de subcapitol discutabilă (ATM = articulație → probabil Aparat locomotor)
  și sunt marcate **Neindicat** (înlocuite de IRM). **Lăsate neatinse** — încadrarea și
  păstrarea lor se decid în echipă. Vezi `EDITORIAL-decisions.md`.
- **Cvasi-duplicate păstrate** (2 perechi de studiat): NR 889/890 (masă pelvină) și
  NR 1472/1473 (rahialgie). Vezi `DUPLICATE-review.md`.
- **Plasările pe muchie** din Gât și Coloană (vezi maparea) — de validat clinic.
