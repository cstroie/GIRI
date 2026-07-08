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

> ⚠️ **NR.CRT au fost renumerotate integral 1..1524** (renumerotare la cerere, 2026-07, după
> finalizarea lucrului pe capitolele Pediatrie și Traumatisme). Numerotarea veche nu se
> păstrează — referințele se fac prin capitol + situație clinică. **Referințele NR.CRT din
> intrările istorice de mai jos reflectă starea de la momentul modificării** (înainte de această
> renumerotare) și nu mai corespund ID-urilor curente.

---

## Structura ghidului (după modificări — 14 capitole, 1470 rânduri, 13 coloane)

> **NR.CRT nu mai e contiguu** de la consolidarea oncologiei (2026-07-08): rândurile mutate
> între capitole și-au păstrat ID-ul original (fără renumerotare — vezi `CLAUDE.md` regula 3),
> iar rândurile noi au primit ID-uri la finalul secvenței (NR 1525). Coloana „NR.CRT" de mai
> jos e **doar orientativă** (intervalul dominant din capitol); pentru intervalul exact rulează
> `tools/validate.py` sau interoghează CSV-ul. Referă rândurile prin **Capitol + Situație
> clinică**, nu prin NR.CRT.

| # | Capitol | NR.CRT (orientativ) | Rânduri |
|---|---|---|---|
| 1 | [Pediatrie](#1-pediatrie) | 1–196 | 196 |
| 2 | [Traumatisme](#2-traumatisme) | 197–317 | 121 |
| 3 | [Cancer](#3-cancer) | 318–553 + mutate din alte capitole + 1525 | 256 |
| 4 | [Aparat cardiovascular](#4-aparat-cardiovascular) | 554–640 | 87 |
| 5 | [Torace](#5-torace) | 641–715 | 75 |
| 6 | [Aparat digestiv](#6-aparat-digestiv) | 716–842 | 70 |
| 7 | [Aparat uro-genital și glande suprarenale](#7-aparat-uro-genital-și-glande-suprarenale) | 843–911 | 69 |
| 8 | [Obstetrică și ginecologie](#8-obstetrică-și-ginecologie) | 912–938 | 27 |
| 9 | [Sân](#9-sân) | 939–994 | 56 |
| 10 | [Cap](#10-cap) | 995–1114 | 116 |
| 11 | [Gât (părți moi)](#11-gât-părți-moi) | 1115–1132 | 18 |
| 12 | [Coloană vertebrală](#12-coloană-vertebrală) | 1133–1187 | 55 |
| 13 | [Aparat locomotor](#13-aparat-locomotor) | 1188–1274 | 74 |
| 14 | [Radiologie intervențională](#14-radiologie-intervențională) | 1275–1524 | 250 |

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

### ⛔ BREAKING — Consolidarea oncologiei diagnostice în capitolul Cancer (2026-07-08)

**Problema:** stadializarea/urmărirea oncologică (malignitate cunoscută sau suspectată)
era împrăștiată și în capitole anatomice — mai ales **Aparat digestiv**, care conținea
un set aproape complet (și parțial fragmentat în variante de denumire) de situații
identice sau cvasi-identice cu subcapitole deja existente în **Cancer** (esofag, stomac,
colorectal/rect/anal, colangiocarcinom, tumoră hepatică primară, tumoră pancreatică).
Suprapuneri mai mici existau și în **Aparat locomotor** (tumori osoase/părți moi) și
**Cap** (tumori cerebrale). Încalcă regula „un singur home per rând" (CLAUDE.md).

**Ce s-a făcut** (script Python, dry-run → apply, `tools/validate.py` verde după fiecare pas):

1. **Excepție documentată — cancerul de sân** rămâne în capitolul **Sân** (subcapitol
   „Cancer de sân"), analog excepției ERCP; consemnat explicit în `CLAUDE.md` (ierarhia
   capitolelor, regula 3, + „Decizii deja luate"). Sânul e capitol de specialitate
   (senologie), nu doar un aparat anatomic.
2. **Aparat digestiv → Cancer: 24 rânduri mutate, 32 eliminate** (duplicate exacte/cvasi-exacte
   ale conținutului deja existent în Cancer — vezi detaliu pe capitole mai jos).
3. **Aparat locomotor → Cancer: 13 rânduri mutate** (restructurare os/părți moi, înlocuind
   10 rânduri generice vechi din Cancer cu structura mai precisă, deja existentă în
   Aparat locomotor, care separă osos de părți moi).
4. **Cap → Cancer: 1 rând mutat, 3 eliminate** (conflict de grad cu conținutul deja
   existent în Cancer — semnalat mai jos, nu rezolvat unilateral).
5. **Subcapitol nou în Cancer — „Tumori neuroendocrine gastro-entero-pancreatice
   (GEP-NET)"** (11 rânduri, NR 765–770 + 774–776 + 838, plus rând Z nou NR 1525):
   conținut real, absent anterior din Cancer, „ascuns" în Aparat digestiv sub tumoră
   endocrină pancreatică + suspiciune de tumoră endocrină intestinală. Grupate împreună
   (terminologie ESMO — GEP-NET) pentru că workup-ul (scintigrafie/PET-CT cu analogi de
   somatostatină) e comun, indiferent de sediu.
6. **Duplicat intern eliminat** (nu doar cross-capitol): NR 837 din Aparat digestiv era
   identic cu NR 775 (aceeași situație, examen și comentariu; doar Doza diferea) —
   păstrat NR 775, eliminat 837.
7. **Rânduri-husk vechi din Cancer, eliminate și înlocuite cu conținut mai bogat, mutat din
   Aparat digestiv** (fără schimbare de grad clinic, doar text mai detaliat/specific):
   „Tumori maligne primare hepatice" (Detectare + Stadializare) și „Tumori maligne
   secundare hepatice" (Detectare) — conținutul din Aparat digestiv acoperea explicit
   ciroza/carcinomul hepatocelular și bilanțul de rezecabilitate al metastazelor, absent
   din formularea generică veche.
8. **ELIMINAT — subcapitol-husk preexistent „Aparat digestiv › Abdomen"** (doar rândul-placeholder
   Z; semnalat deja în `EDITORIAL-decisions.md` §5 ca „de eliminat când se ajunge la capitol").
   (−1 rând; NR 716)

**Conflicte de grad găsite la comparație — NEREZOLVATE, semnalate pentru editor**
(gradele nu se modifică unilateral — regulă `CLAUDE.md`; s-a păstrat gradul din Cancer,
varianta din capitolul anatomic a fost eliminată ca duplicat, nu editată):

- Cancer esofagian, CT stadializare: Cancer *Indicat B* vs Aparat digestiv *Indicat A*.
- Cancer gastric, Ecoendoscopie: Cancer *Indicat B* vs Aparat digestiv *Doar în cazuri particulare B*.
- Cancer de colon, colonoscopie virtuală CT: Cancer *Indicat A* vs Aparat digestiv *Doar în
  cazuri particulare B* (scris ca „Colo-CT cu apă" / „Colonoscopie virtuală CT").
- Tumori cerebrale, IRM/CT diagnostic: Cancer *Indicat B* vs Cap *Indicat A* (IRM), respectiv
  Cancer *Indicat B* vs Cap *Doar în cazuri particulare A* (CT).

Vezi `DUPLICATE-review.md` secțiunea D pentru detalii complete.

**Rânduri mutate/eliminate, pe capitol de origine:** Aparat digestiv 24 mutate + 33
eliminate (32 duplicate + 1 husk preexistent) · Aparat locomotor 13 mutate + 10 eliminate
(rândurile generice vechi din Cancer) · Cap 1 mutat + 3 eliminate.

### MODIFICAT — Corecturi ortografice, punctuație și uniformizare (capitolul Cancer)

- **Diacritice** — 113 corecții de tip cuvânt-întreg (ex. „electie"→„elecție",
  „acuratete"→„acuratețe", „hepatica"→„hepatică", „toracica"→„toracică", „in"→„în",
  „si"→„și"), aplicate doar unde varianta corectă cu diacritice exista deja verificabil
  în capitol; excluse cuvintele ambigue („an" ≠ „ân", „faza" ca formă articulată).
  174 câmpuri modificate. Corectat și un typo izolat („ân caz de" → „în caz de", NR 1208
  — mutat din Aparat locomotor) și „faza tardiva"→„faza tardivă" (NR 726).
- **Spații parazite** — eliminate spații inițiale/finale și duble pe 54 câmpuri
  (Situație, Examen, Comentarii, Alte informații), fără schimbare de sens.
- **Uniformizare „PET-CT"** — 7 variante de scriere („PET - CT", „PET -CT", „PET-CT")
  pentru același examen, unificate la forma canonică „PET-CT (F18-FDG)" (24 câmpuri,
  Examen + text liber).
- **Uniformizare capitalizare examene** — „Ecografia"→„Ecografie", „radiografia
  toracică"/„Radiografia toracică"→„Radiografie toracică", „Radiografia pulmonară"→
  „Radiografie pulmonară" (11 câmpuri Examen).
- **Uniformizare spațiere cratimă** — „Eco- endoscopie"→„Ecoendoscopie", „eso- gastro-
  duodenal"→„eso-gastro-duodenal", „iod -131"→„iod-131", „cervico- toracal"→„cervico-toracal"
  (4 câmpuri Examen).

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
_NR 1–196_

### Rafinări `Pediatrie › Traumatisme`
- **ADĂUGAT — „Traumatism de coloană toraco-lombară la copil"** (3 rânduri, NR 1528–1530):
  Radiografie (*Indicat, B* — atenție la fracturile Chance / centură de siguranță), CT
  (*Doar în cazuri particulare, B*), IRM (*Doar cu aviz specializat, B* — deficit / SCIWORA).
  Completează axa spinală (exista doar coloana cervicală).
- **REFACTOR — eliminată situația-orfan „Traumatism unilateral de membru – comparativ"**
  (NR 64); nota (radiografia comparativă doar la indicația radiologului) a fost **contopită**
  în comentariul situației generale „Traumatism de membru – suspiciune de fractură" (NR 1499).
  (−1 rând; gaură la NR 64.)
- **MODIFICAT — PECARN la traumatismul cranian.** La CT (NR 111): adăugată referința explicită
  la regula **PECARN** + explicație; criteriile detaliate de indicație CT **mutate din
  „Alte informații" în „Comentarii"** (conținut clinic, per regula din CLAUDE.md).
- **MODIFICAT — NAI / skeletal survey.** La „Traumatism nonaccidental" (NR 59): eticheta Examen
  „Radiografie standard" → „**Radiografie – schelet complet (skeletal survey)**"; comentariul
  precizează protocolul standardizat (serie definită) și repetarea la 11–14 zile.

### Oncologie
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
_NR 197–317_

- **ELIMINAT — breadcrumb adult → Pediatrie.** Situația „Traumatism cranio-cerebral
  (pentru copii – vezi capitolul Pediatrie)" → „Traumatism cranio-cerebral" (subcapitol
  Cap, 4 rânduri). Trauma cranio-cerebrală pediatrică are propriul subcapitol în Pediatrie;
  navigarea încrucișată e treaba aplicației, nu a datelor (per CLAUDE.md).
- **ADĂUGAT — „Leziune cerebrovasculară posttraumatică (disecție carotidiană / vertebrală)"**
  în subcapitolul „Sistem vascular" (3 rânduri, NR 1531–1533): Angio-CT cervico-cerebral
  (*Indicat, B* — screening după criteriile Denver/Memphis), Angio-RM (*Doar în cazuri
  particulare, B*), Ecografie Doppler cervicală (*Doar în cazuri particulare, C* — rol
  limitat). Acoperă o lacună (subcapitolul avea doar aorta toracică și membrele).
  _Angiografia convențională (DSA) — reper istoric, invazivă — nu se include aici (Tip A → RI)._
- _Granița **Abdomen vs Bazin** (suprapunerea „Traumatism abdominal major și/sau de bazin"
  cu „Traumatism izolat de bazin") → decizie editorială deschisă, `EDITORIAL-decisions.md` §7._
- **MODIFICAT — clarificată granița Abdomen vs Bazin** (fosta chestiune editorială §7,
  acum rezolvată). Situația „Traumatism abdominal **major și/sau de bazin**" → „Traumatism
  abdominal **major**" (NR 156–158). Cele două rămân **distincte** (viscere abdominale ±
  bazin pe același CT vs inel pelvin osos izolat — „Bazin și sacru"); nu s-au comasat.
  Comentariul CT (NR 158) precizează că achiziția trebuie să includă bazinul, pentru a
  surprinde o eventuală leziune pelvină asociată.
- **RESTRUCTURAT — consolidarea subcapitolului „Coloană cervicală"** (9 situații suprapuse
  → **5 rungi clinice clare**; 21 → 14 rânduri, −7). Comentariile bogate au fost **contopite,
  nu pierdute**; recomandările de modalitate ale ghidului au fost **păstrate** (radiografie-întâi
  la risc scăzut — modernizarea „CT-întâi" e o decizie editorială separată).
  - **„Traumatism cervical — evaluare inițială (reguli NEXUS / Canadian C-Spine Rule)"** —
    contopește „Cervicalgii posttraumatice" + „Pacient conștient cu leziune cap/față" +
    „Traumatism cervical benign".
  - **„…durere persistentă cu bilanț radiografic normal (suspiciune de leziune ligamentară)"** —
    contopește cele două situații identice (bilanț normal + simptome algice/ligamentar).
  - **„Pacient inconștient / obnubilat cu traumatism cranian"** — păstrată; radiografia
    coborâtă Indicat → *Doar în cazuri particulare* (CT preferat, cf. propriilor comentarii).
  - **„Traumatism cervical sever cu deficit neurologic"** — contopește sinonimele „cu afectare
    neurologică" și „cu deficit neurologic" (aveau recomandări **contradictorii**); rezolvat:
    CT **și** IRM = Indicat, Radiografie = Neindicat (A).
  - **„Traumatism cervical sever, fără deficit neurologic"** — păstrată (redenumită din
    „fără afectare neurologică").
  - **Referințe** (NEXUS — Hoffman, NEJM 2000; Canadian C-Spine Rule — Stiell, JAMA 2001;
    ACR Appropriateness Criteria – Suspected Spine Trauma) adăugate în **„Alte informații"**.
  - Bonus: două rânduri (fostele IRM/dinamice) aveau **note clinice greșit plasate în „Alte
    informații"** → mutate în „Comentarii" (per regula din CLAUDE.md).
  - Șterse 7 rânduri (fără renumerotare; găuri la NR 187, 190, 191, 192, 194, 197, 198).
- **MODIFICAT — completate 6 grade „?" (neprecizat)** pe rânduri „Neindicat" (nivelul de
  evidență lipsea; recomandarea era deja corectă). Aliniere la ACR Appropriateness Criteria /
  RCR iRefer / NICE: Radiografie de craniu (traumatism cranian) = **A**; Radiografie nazală,
  radiografia oaselor faciale, radiografia orbitelor (penetrant + contondent) = **B**; IRM
  toracic (traumatism aortă, în urgență) = **C** (limitare practică, nu dovezi de risc).
  (NR 180, 232, 223, 236, 240, 271.)

- **MUTAT —** 18 rânduri intervenționale (Tip I/A) relocate la RI › Traumatisme.
- **MODIFICAT (terminologie) —** „Traumatism cranio-**encefalic**" → „Traumatism
  cranio-**cerebral**" (subcapitol Cap, 4 rânduri), pentru consecvență cu capitolul
  Pediatrie (preferință editor: „cranio-cerebral").
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
_NR 318–553 + rânduri mutate din Aparat digestiv/locomotor/Cap + NR 1525 (nou)_

- **MUTAT —** 19 rânduri intervenționale relocate la RI › Oncologie.
- **MODIFICAT (date) —** subcapitol „Ficat, colecist şi pancreas" normalizat (vezi Modificări globale).
- **RESTRUCTURAT — consolidarea oncologiei diagnostice** (vezi „Modificări globale" mai
  sus pentru detaliu complet): +24 rânduri mutate din Aparat digestiv (Ficat/colecist/
  pancreas + Tub digestiv), +13 din Aparat locomotor, +1 din Cap; −19 rânduri-husk vechi
  (generice, înlocuite cu conținut mai bogat); subcapitol nou „Tumori neuroendocrine
  gastro-entero-pancreatice (GEP-NET)" (11 rânduri + Z, NR 1525). Rezultat net: 236 → 256 rânduri.
- **ADĂUGAT — excepție documentată pentru cancerul de sân** (rămâne în capitolul Sân,
  subcapitol „Cancer de sân"), consemnată în `CLAUDE.md`.
- **MODIFICAT — corecturi ortografice, punctuație, uniformizare** (diacritice, spații
  parazite, denumiri „PET-CT"/Ecografie/Radiografie, spațiere cratimă) — vezi „Modificări
  globale" pentru detaliu complet.
- **Grade de indicație divergente găsite la consolidare — semnalate, nerezolvate**
  (4 cazuri: cancer esofagian/CT, cancer gastric/ecoendoscopie, cancer de colon/
  colonoscopie virtuală, tumori cerebrale/IRM+CT) → `DUPLICATE-review.md` secțiunea D.

## 4. Aparat cardiovascular
_NR 554–640_

- **MUTAT —** 54 rânduri intervenționale (embolizări, angioplastii, protezări,
  angiografie invazivă) relocate la RI › Aparat cardiovascular. Capitolul se reduce
  substanțial (rămân investigațiile diagnostice).

## 5. Torace
_NR 641–715_

- **MUTAT —** 11 rânduri intervenționale relocate la RI › Aparat respirator.

## 6. Aparat digestiv
_NR 716–842_

- **ELIMINAT — subcapitol-husk „Traumatisme abdominale"** (conținea doar rândul-placeholder
  Tip Z). Anti-pattern context-în-anatomie: trauma abdominală stă în capitolul Traumatisme,
  nu în Aparat digestiv. (Vezi Modificări globale › Ierarhia capitolelor.) (−1 rând)
- **ELIMINAT — subcapitol-husk „Abdomen"** (doar rândul-placeholder Z; era semnalat în
  `EDITORIAL-decisions.md` §5). (−1 rând, NR 716)
- **MUTAT / ELIMINAT — consolidare oncologie → Cancer** (vezi „Modificări globale"):
  24 rânduri mutate (cholangiocarcinom, tumoră hepatică primară pe fond de ciroză,
  metastaze hepatice/bilanț rezecabilitate, tumoră endocrină pancreatică, suspiciune
  tumoră neuroendocrină intestinală, ecoendoscopie pancreatică) + 32 rânduri eliminate ca
  duplicate ale conținutului deja existent în Cancer (cancer esofagian, gastric,
  colorectal/rect/anal — inclusiv un duplicat intern, NR 837 == NR 775). (−56 rânduri)

- **MUTAT —** 62 rânduri intervenționale relocate la RI › Aparat digestiv.
- **MODIFICAT (date) —** eticheta „Aparat digestiv " (spațiu în plus, 5 rânduri) unificată sub „Aparat digestiv".

## 7. Aparat uro-genital și glande suprarenale
_NR 843–911_

- **MUTAT —** 19 rânduri intervenționale relocate la RI › Aparat urogenital.

## 8. Obstetrică și ginecologie
_NR 912–938_

- **MUTAT —** 3 rânduri intervenționale relocate la RI › Aparat urogenital.
- **MODIFICAT (date) —** subcapitol „Sarcina"/„Sarcină" unificat la „Sarcină" (majoritar).

## 9. Sân
_NR 939–994_

- **MUTAT —** 4 rânduri intervenționale relocate la RI › Oncologie.
- **MODIFICAT (date) —** spații finale parazite pe „…cancer  " eliminate (12 rânduri).

## 10. Cap
_NR 995–1114_

- **MUTAT —** 25 rânduri intervenționale (neurovasculare) relocate la RI › Sistem nervos.
- **MUTAT / ELIMINAT — consolidare oncologie → Cancer** (vezi „Modificări globale"):
  subcapitolul „Neuro › Tumori cerebrale" dubla parțial „Cancer › Tumori cerebrale și
  medulare" (conflict de grad pe IRM/CT — semnalat, nerezolvat unilateral). 1 rând mutat
  (scintigrafie cerebrală cu traceri de viabilitate, conținut absent din Cancer) + 3
  eliminate ca duplicate/conflict de grad. (−3 rânduri)

## 11. Gât (părți moi)
_NR 1115–1132_

- **MUTAT —** 8 rânduri intervenționale (PCAFGE) relocate la RI: tiroidă/paratiroidă
  → Aparat endocrin; „Masă cervicală" → Oncologie.

## 12. Coloană vertebrală
_NR 1133–1187_

- **MUTAT —** 7 rânduri intervenționale relocate la RI: vertebroplastie / biopsie /
  infiltrație → Aparat locomotor; embolizări spinale → Sistem nervos.

## 13. Aparat locomotor
_NR 1188–1274_

- **MUTAT —** 13 rânduri intervenționale relocate la RI › Aparat locomotor.
- **MUTAT — consolidare oncologie → Cancer** (vezi „Modificări globale"): subcapitolul
  „Diverse" avea deja o structură os/părți moi mai precisă decât varianta generică din
  Cancer › „Tumori ale aparatului locomotor". Toate cele 13 rânduri (Diagnostic +
  bilanț de extensie, os și părți moi separat) mutate în Cancer, înlocuind cele 10
  rânduri generice vechi. (−13 rânduri)

## 14. Radiologie intervențională
_NR 1275–1524 (250 rânduri)_

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
