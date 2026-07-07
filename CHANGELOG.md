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

## Structura ghidului (după modificări — 14 capitole, 1488 rânduri, 13 coloane)

| # | Capitol | NR.CRT | Rânduri |
|---|---|---|---|
| 1 | [Pediatrie](#1-pediatrie) | 1–155 | 155 |
| 2 | [Traumatisme](#2-traumatisme) | 156–280 | 125 |
| 3 | [Cancer](#3-cancer) | 281–516 | 236 |
| 4 | [Aparat cardiovascular](#4-aparat-cardiovascular) | 517–603 | 87 |
| 5 | [Torace](#5-torace) | 604–678 | 75 |
| 6 | [Aparat digestiv](#6-aparat-digestiv) | 679–806 | 128 |
| 7 | [Aparat uro-genital și glande suprarenale](#7-aparat-uro-genital-și-glande-suprarenale) | 807–875 | 69 |
| 8 | [Obstetrică și ginecologie](#8-obstetrică-și-ginecologie) | 876–902 | 27 |
| 9 | [Sân](#9-sân) | 903–958 | 56 |
| 10 | [Cap](#10-cap) | 959–1078 | 120 |
| 11 | [Gât (părți moi)](#11-gât-părți-moi) | 1079–1096 | 18 |
| 12 | [Coloană vertebrală](#12-coloană-vertebrală) | 1097–1151 | 55 |
| 13 | [Aparat locomotor](#13-aparat-locomotor) | 1152–1238 | 87 |
| 14 | [Radiologie intervențională](#14-radiologie-intervențională) | 1239–1488 | 250 |

---

## Modificări globale (cross-capitol)

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
_NR 1–155_

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
_NR 156–280_

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
- _Chestiuni lăsate pentru editori → `EDITORIAL-decisions.md` §5: subcapitolul-shell
  „Aparat digestiv" (doar placeholder), cvasi-duplicatul NR 178/179 (→ `DUPLICATE-review.md` §C),
  omisiuni de patologie (traumatism vascular de membru etc.), „lemn pictat" (NR 221)._

## 3. Cancer
_NR 281–516_

- **MUTAT —** 19 rânduri intervenționale relocate la RI › Oncologie.
- **MODIFICAT (date) —** subcapitol „Ficat, colecist şi pancreas" normalizat (vezi Modificări globale).

## 4. Aparat cardiovascular
_NR 517–603_

- **MUTAT —** 54 rânduri intervenționale (embolizări, angioplastii, protezări,
  angiografie invazivă) relocate la RI › Aparat cardiovascular. Capitolul se reduce
  substanțial (rămân investigațiile diagnostice).

## 5. Torace
_NR 604–678_

- **MUTAT —** 11 rânduri intervenționale relocate la RI › Aparat respirator.

## 6. Aparat digestiv
_NR 679–806_

- **MUTAT —** 62 rânduri intervenționale relocate la RI › Aparat digestiv.
- **MODIFICAT (date) —** eticheta „Aparat digestiv " (spațiu în plus, 5 rânduri) unificată sub „Aparat digestiv".

## 7. Aparat uro-genital și glande suprarenale
_NR 807–875_

- **MUTAT —** 19 rânduri intervenționale relocate la RI › Aparat urogenital.

## 8. Obstetrică și ginecologie
_NR 876–902_

- **MUTAT —** 3 rânduri intervenționale relocate la RI › Aparat urogenital.
- **MODIFICAT (date) —** subcapitol „Sarcina"/„Sarcină" unificat la „Sarcină" (majoritar).

## 9. Sân
_NR 903–958_

- **MUTAT —** 4 rânduri intervenționale relocate la RI › Oncologie.
- **MODIFICAT (date) —** spații finale parazite pe „…cancer  " eliminate (12 rânduri).

## 10. Cap
_NR 959–1078_

- **MUTAT —** 25 rânduri intervenționale (neurovasculare) relocate la RI › Sistem nervos.

## 11. Gât (părți moi)
_NR 1079–1096_

- **MUTAT —** 8 rânduri intervenționale (PCAFGE) relocate la RI: tiroidă/paratiroidă
  → Aparat endocrin; „Masă cervicală" → Oncologie.

## 12. Coloană vertebrală
_NR 1097–1151_

- **MUTAT —** 7 rânduri intervenționale relocate la RI: vertebroplastie / biopsie /
  infiltrație → Aparat locomotor; embolizări spinale → Sistem nervos.

## 13. Aparat locomotor
_NR 1152–1238_

- **MUTAT —** 13 rânduri intervenționale relocate la RI › Aparat locomotor.

## 14. Radiologie intervențională
_NR 1239–1488 (250 rânduri)_

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
