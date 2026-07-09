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
>
> ⚠️ **A doua renumerotare integrală, 1..1471** (la cerere, 2026-07-08, după finalizarea
> consolidării Cancer și a reviewului Sân). Între cele două renumerotări, NR.CRT a avut găuri
> tolerate (rânduri mutate/eliminate) — vezi CLAUDE.md regula 3. **Referințele NR.CRT din
> intrările Cancer/Sân de mai jos reflectă starea de dinaintea acestei a doua renumerotări**
> (NR 1525–1527 din secțiunea Cancer, de exemplu, nu mai există ca atare — conținutul e
> neschimbat, doar ID-ul).
>
> ⚠️ **Renumerotare la cerere, 2026-07-08 (după reviewul Cardiovascular).** Fișierul era deja
> contiguu 1..1471; renumerotarea a refăcut potrivirea NR.CRT ↔ poziție fizică după
> reordonarea situației „Anevrisme vase periferice" — **doar 2 ID-uri schimbate** (fostul
> NR 648 „Eco Doppler" → 647; fostul NR 647 „Angio-CT periferic" → 648). Restul neschimbate.

---

## Structura ghidului (după modificări — 14 capitole, 1462 rânduri, 13 coloane)

> **NR.CRT nu mai e contiguu** după fuziunea „Neoplasm bronhopulmonar" (2026-07-08):
> Torace 695–705 s-au șters (11 găuri), iar Cancer › Cancer bronho-pulmonar a primit 2
> rânduri noi cu ID-uri la finalul secvenței (1472, 1473). Pe viitor **nu se renumerotează
> automat** (vezi `CLAUDE.md`): ștergerile lasă găuri, iar inserțiile primesc ID-uri la
> finalul secvenței, până la o nouă renumerotare cerută explicit.

| # | Capitol | NR.CRT | Rânduri |
|---|---|---|---|
| 1 | [Pediatrie](#1-pediatrie) | 1–196 | 196 |
| 2 | [Traumatisme](#2-traumatisme) | 197–317 | 121 |
| 3 | [Cancer](#3-cancer) | 318–574 (+1472, 1473) | 259 |
| 4 | [Aparat cardiovascular](#4-aparat-cardiovascular) | 575–661 | 87 |
| 5 | [Torace](#5-torace) | 662–736 (fără 695–705) | 64 |
| 6 | [Aparat digestiv](#6-aparat-digestiv) | 737–806 | 70 |
| 7 | [Aparat uro-genital și glande suprarenale](#7-aparat-uro-genital-și-glande-suprarenale) | 807–875 | 69 |
| 8 | [Obstetrică și ginecologie](#8-obstetrică-și-ginecologie) | 876–902 | 27 |
| 9 | [Sân](#9-sân) | 903–958 | 56 |
| 10 | [Cap](#10-cap) | 959–1074 | 116 |
| 11 | [Gât (părți moi)](#11-gât-părți-moi) | 1075–1092 | 18 |
| 12 | [Coloană vertebrală](#12-coloană-vertebrală) | 1093–1147 | 55 |
| 13 | [Aparat locomotor](#13-aparat-locomotor) | 1148–1221 | 74 |
| 14 | [Radiologie intervențională](#14-radiologie-intervențională) | 1222–1471 | 250 |

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
  - Infiltrație „Rahialgie / Radiculalgie" (NR 1455 și 1456) — coduri diferite PC5 vs PC7.

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

**Conflicte de grad găsite la comparație — semnalate la editor și REZOLVATE (2026-07-08):**

- Cancer esofagian, CT stadializare (NR 385): **ridicat** la grad A (aliniat la ghidul RCR,
  referință adăugată).
- Cancer gastric, Ecoendoscopie stadializare (NR 389): **coborât** la „Doar în cazuri particulare".
- Cancer de colon, colonografie CT (diagnostic): rândul generic „Colonoscopia CT" (NR 350,
  Indicat A) rămâne; **readuse ca situații distincte** „Colo-CT cu apă" și „Colonoscopie
  virtuală CT" (NR 1526/1527, Doar în cazuri particulare, grad B) — erau tehnici/indicații
  diferite, nu duplicat.
- Tumori cerebrale, IRM diagnostic (NR 536): grad B păstrat, **text îmbogățit** cu formularea
  mai completă din fosta versiune Cap.
- Tumori cerebrale, CT diagnostic (NR 537): avea (eroare preexistentă) text identic cu rândul
  de IRM; **adoptate categoria „Doar în cazuri particulare", gradul A și textul specific CT**
  din fosta versiune Cap.

Detalii complete în `DUPLICATE-review.md` secțiunea D. (+2 rânduri nete: NR 1526, 1527)

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
_NR 318–574 (+1472, 1473)_

### ⛔ BREAKING — Fuziunea „Neoplasm bronhopulmonar" din Torace (2026-07-08)

Cancerul pulmonar exista **în dublu exemplar**: subcapitolul canonic **Cancer bronho-pulmonar**
(NR 334–343) și 11 rânduri „Neoplasm bronhopulmonar" în capitolul Torace › Pulmon (NR 695–705).
Per **ierarhia capitolelor (regula 3)** — malignitatea cunoscută → Cancer — cele 11 rânduri au
fost **eliminate din Torace** și reconciliate în Cancer bronho-pulmonar. Maparea fazelor:
Torace „diagnostic – suspiciune clinică" = **Diagnostic**; „bilanț preterapeutic" + „stadializare"
= **Stadializare**; „supraveghere" = **Monitorizare**.

- **ADĂUGAT — faza Monitorizare completată** (avea doar PET-CT). Două rânduri noi (ID **1472**
  Radiografie toracică *Indicat C*, **1473** CT cerebral/torace/abdomen *Indicat C* cu protocolul
  de urmărire 3/6/12 luni → anual 5 ani), preluate din fostele NR 703/704. Ordine G → T → N.
- **ÎMBOGĂȚIT — note clinice unice păstrate din rândurile Torace duplicate** (regula „nu pierde
  conținut clinic la fuziune"): NR **335** (CT diagnostic) — adăugat „se efectuează înaintea
  bronhoscopiei…" (din 700) + corectat „depisteaza"→„depistează"; NR **340** (CT stadializare) —
  adăugat nota „fereastră osoasă… metastaze scheletice" (din 697); NR **341** (IRM mediastinal) —
  comentariul Pancoast îmbogățit cu detaliul anatomic din 698 (plex brahial, vertebre, arteră
  subclaviculară, invazie pericardică) și reparată fraza trunchiată („…contrast iodat").
- **DUPLICATE eliminate** (Cancer acoperea deja identic/mai bine): 696≈337 (PET-CT stadializare,
  comentariu identic), 701≈336 (PET-CT diagnostic), 702≈338 (Scintigrafie osoasă), 705≈342
  (PET-CT monitorizare), 700 (CT diagnostic amplu, redundant cu 335+340).
- **CONFLICTE DE GRAD rezolvate „gradul Cancer prevalează"** (semnalate editorial, vezi
  `EDITORIAL-decisions.md` §13): Radiografie diagnostic **A** păstrat (Torace 699 era C); IRM
  cerebral stadializare **A** păstrat (695 era C); CT stadializare **A** păstrat (697 era C); IRM
  mediastinal **C** păstrat (698 era B). Niciun grad Cancer modificat.

Rezultat net Cancer: **+2 rânduri** (257 → 259).

### MODIFICAT — Verificare față de ghiduri + referințe (Cancer bronho-pulmonar, 2026-07-08)

Pasul 7 al checklist-ului, aplicat subcapitolului fuzionat (iRefer/NICE NG122/ACR AC 2019).
Fără schimbări de grad sau indicație în date.

- **ADĂUGAT (col. 10 „Alte informații") — referințe scurte de ghid** pe rândurile verificate:
  NR 334 (radiografie primă linie), 335 (CT pre-biopsie), 337 (PET-CT stadializare), 338
  (PET-CT vs scintigrafie), 339 (IRM cerebral), 340 (CT stadializare), 341 (IRM torace select).
- **CONFIRMAT — conflictul de grad IRM mediastinal (NR 341) închis la „C"** (decizie editor,
  susținut de ACR AC — instrument select/problem-solving). Celelalte trei (radiografie/IRM
  cerebral/CT = A) confirmate de NICE NG122.
- **MODIFICAT (Indicație) — Scintigrafie osoasă (NR 338): „Indicat" → „Doar în cazuri
  particulare"** (decizie editor). FDG PET-CT a înlocuit în mare scintigrafia osoasă în
  stadializarea de rutină; PET-CT stadializare există deja (NR 337, „Indicat" A). Comentariul
  completat cu „…mai ales atunci când PET-CT nu este disponibil" (+ fix „singura"→„singură").
  **Gradul B rămâne** neschimbat (modificarea privește puterea indicației, nu nivelul de
  evidență). Vezi `EDITORIAL-decisions.md` §13.

- **MUTAT —** 19 rânduri intervenționale relocate la RI › Oncologie.
- **MODIFICAT (date) —** subcapitol „Ficat, colecist şi pancreas" normalizat (vezi Modificări globale).
- **RESTRUCTURAT — consolidarea oncologiei diagnostice** (vezi „Modificări globale" mai
  sus pentru detaliu complet): +24 rânduri mutate din Aparat digestiv (Ficat/colecist/
  pancreas + Tub digestiv), +13 din Aparat locomotor, +1 din Cap; −19 rânduri-husk vechi
  (generice, înlocuite cu conținut mai bogat); subcapitol nou „Tumori neuroendocrine
  gastro-entero-pancreatice (GEP-NET)" (11 rânduri + Z, NR 1525). Rezultat net: 236 → 258 rânduri
  (256 din consolidare + 2 din rezolvarea conflictelor de grad, NR 1526/1527).
- **ADĂUGAT — excepție documentată pentru cancerul de sân** (rămâne în capitolul Sân,
  subcapitol „Cancer de sân"), consemnată în `CLAUDE.md`.
- **MODIFICAT — corecturi ortografice, punctuație, uniformizare** (diacritice, spații
  parazite, denumiri „PET-CT"/Ecografie/Radiografie, spațiere cratimă) — vezi „Modificări
  globale" pentru detaliu complet.
- **Grade de indicație divergente găsite la consolidare — semnalate la editor și
  rezolvate** (5 cazuri: cancer esofagian/CT → ridicat la A; cancer gastric/ecoendoscopie
  → coborât la „Doar în cazuri particulare"; cancer de colon/colonografie CT → readuse ca
  situații distincte NR 1526/1527; tumori cerebrale/IRM → text îmbogățit; tumori
  cerebrale/CT → categorie+grad+text adoptate din fosta versiune Cap) →
  `DUPLICATE-review.md` secțiunea D.
- **RESTRUCTURAT — a doua verificare, după consolidare (2026-07-08):**
  - **MODIFICAT (eroare de date) — NR 383**, Cancer esofagian: Ecoendoscopie era marcată
    `Tip=E` (Ecografie) în loc de `Tip=D` (diagnostic invaziv/endoscopic, ca peste tot
    în rest); corectat.
  - **UNIFORMIZAT — „Cancer bronho-pulmonar"**: 4 rânduri cu etichete de situație
    fragmentate/verboase („Neoplasm bronhopulmonar – diagnostic – suspiciune clinică",
    „…bilanț preterapeutic", „…stadializare", „…supraveghere") contopite în etichetele
    scurte deja folosite în același subcapitol: „Diagnostic", „Stadializare" (×2),
    „Monitorizare". Fără schimbare de conținut clinic; doar gruparea corectă a situației.
  - **MODIFICAT — eticheta rândului ERCP (NR 490)**, subcapitol „Ficat, colecist și
    pancreas": situația era etichetată „Cancer pancreatic" — coliziune derutantă cu
    subcapitolul omonim „Cancer pancreatic". Redenumit „Drenaj biliar / pancreatic (ERCP)".
  - **ELIMINAT / COMASAT — Limfom, NR 498/499** (ambele „Monitorizare, CT, Indicat B",
    conținut redundant): păstrat NR 498 (mai complet), cu nuanța unică din NR 499
    (ritmicitatea urmăririi) adăugată la final. (−1 rând)
  - **MODIFICAT (date) — corecturi ortografice extinse** pe rândurile mutate din Aparat
    digestiv (subcapitolele „Tumori maligne primare/secundare hepatice", „Tumori
    neuroendocrine…"): ~25 câmpuri Comentarii/Alte informații cu diacritice lipsă
    corectate (ex. „reprezinta"→„reprezintă", „interventionala"→„intervențională",
    „evaluarii"→„evaluării", „circulatia"→„circulația"), plus câteva erori de tipar
    („leziunihepatice"→„leziuni hepatice", spații lipsă după punct, „vena cava
    inferioara"→„vena cavă inferioară").
  - **MODIFICAT (corecție gramaticală) — 4 rânduri** (NR 362, 363, 401, 735):
    „poate ajută" → „poate ajuta" (construcția corectă e cu infinitivul scurt după
    verbul modal „a putea"; corectează o supra-corectare introdusă la trecerea
    anterioară de normalizare a diacriticelor).
  - **MODIFICAT (date) — capitalizare/diacritice Examen** (7 câmpuri): „Ecografie
    endoanala"→„Ecografie endoanală" (×2), „clisma baritată…"→„Clisma baritată…",
    „limfoscintigrafia…"→„Limfoscintigrafia…", „Angio CT"→„AngioCT" (consecvent cu
    „AngioRM" din același subcapitol), „Explorari imagistice"→„Explorări imagistice" (×2).
  - Rezultat net: 258 → 257 rânduri (−1, comasarea Limfom).
- **UNIFORMIZAT — axa „Situație Clinică" la 3 faze canonice: Diagnostic → Stadializare →
  Monitorizare** (2026-07-08, la cererea editorului). Etichete-sinonim contopite, fără
  schimbare de conținut clinic sau grad:
  - „Supravegherea cancerelor tratate" (Cancer laringian, tiroidian, căi aero-digestive),
    „Supraveghere" (Cancerul nazofaringian), „Urmărire" (Tumori cerebrale), „Urmărire și
    restadializare" (Cancer de rect), „Recidive" (Cancer de col uterin) → toate **„Monitorizare"**
    (42 rânduri retichetate).
  - „Detectare" (Cancer pancreatic, Tumori maligne primare/secundare hepatice) → **„Diagnostic"**
    (conținutul e workup diagnostic obișnuit, nu screening/detecție incidentală distinctă).
  - **Fragmentare internă rezolvată — Cancer anal**: „Monitorizare" (1 rând, PET-CT pentru
    leziuni echivoce) + „Urmărire" (3 rânduri, protocol general) erau aceeași fază ruptă
    în două situații → contopite într-o singură „Monitorizare" (4 rânduri).
  - Rânduri fizic reordonate (Cancer anal, Tumori cerebrale și medulare) pentru ca
    situațiile identice să fie din nou grupate contiguu în CSV.
- **INVENTARIAT — 9 subcapitole fără fază „Monitorizare"** (Cancer de corp uterin,
  esofagian, gastric, pancreatic, prostatic, vezical; Cancerul parotidian; Tumori
  maligne primare/secundare hepatice) — posibile omisiuni de conținut sau intenționate
  (ex. prostata se urmărește prin PSA). **Nu s-a inventat conținut clinic** →
  `EDITORIAL-decisions.md` §11, pentru decizia editorilor.

## 4. Aparat cardiovascular
_NR 575–661_

- **MUTAT —** 54 rânduri intervenționale (embolizări, angioplastii, protezări,
  angiografie invazivă) relocate la RI › Aparat cardiovascular. Capitolul se reduce
  substanțial (rămân investigațiile diagnostice).

### MODIFICAT — Review capitol Cardiovascular (2026-07-08)

Review complet al capitolului (checklist din `CLAUDE.md` › „Plan de lucru"). **38 rânduri
modificate** (NR 577–658), toate în capitol; fără schimbări de grad, doză sau ordine a
examenelor. Validare verde, 0 cedile.

- **MODIFICAT (Tip ↔ Examen) — coduri de modalitate inversate corectate.** La „Suspiciune
  de valvulopatie dobândită": **NR 631** „Eco Doppler" era Tip `M` → corectat `E`;
  **NR 632** „IRM" era Tip `E` → corectat `M`. Eroare de date (cod inversat), nu reordonare.
- **DE-DUPLICAT (Situație) — „Anevrisme vase periferice".** Situația era **scindată
  accidental** în două etichete care difereau doar prin varianta de scriere
  „popliteale"/„poplitee" (NR 647 vs 648/649), în același subcapitol. Unificată la
  „…(iliace, femorale, **poplitee**, renale, mezenterice sau celiace)"; cele 3 examene
  (Angio-CT periferic, Eco Doppler, Angio-IRM) stau acum sub o singură situație. Ordinea
  examenelor lăsată în starea existentă — vezi `EDITORIAL-decisions.md` §12.
- **MODIFICAT (Situație) — eliminat breadcrumb.** „HTA – evaluarea cardiacă (vezi și
  evaluare vasculară renală)" → „HTA – evaluarea cardiacă" (NR 597–599). Trimiterea
  încrucișată nu stă în date (regula „un singur home / fără breadcrumb-uri"); dangling-ul
  „– vezi)" din comentariul NR 597 a fost și el curățat.
- **MODIFICAT (Situație) — normalizare ortografică.** „amiloidoză transtiretina" →
  „transtiretină" (NR 588/589); „valvulopatie dobandită" → „dobândită" (NR 631–633);
  „Anevrism aortă **toracală**" → „toracică" (NR 643–646, aliniat convenției dominante pe
  fișier — „toracică" 99 vs „toracală" 15).
- **MODIFICAT (Examen) — normalizare la convenția dominantă.** Anglicismul „Echo"/
  „Echografie" → „Eco"/„Ecografie" (forma dominantă global: Eco 195 vs Echo 14) — NR 577,
  590, 597, 600, 624, 631, 639, 644, 648, 650, 653, 654, 657, 658; plus în text liber
  „echografic"/„echo Doppler" → „ecografic"/„eco Doppler" (NR 654, 656). „Ecografia
  cardiacă" → „Ecografie cardiacă" (NR 602, consecvent cu uniformizarea din capitolul
  Cancer). Diacritică lipsă în etichetă: „…si la repaus" → „…și la repaus" (NR 596).
- **MODIFICAT (Comentarii) — diacritice și typo-uri**, doar unde forma corectă e neambiguă
  (≈20 rânduri): „substațe"→„substanțe" (NR 582), „bilațul"→„bilanțul" (NR 585),
  „tulburari"→„tulburări" (NR 578), „in masura in care acestia sunt disponbili"→„în măsura
  în care aceștia sunt disponibili" (NR 580), „stang"→„stâng" (NR 622), „redusa"→„redusă"
  (NR 632), „diferential"→„diferențial" (NR 626), „interventională"→„intervențională"
  (NR 648), „fara"→„fără" (NR 652), „pentru ca"→„pentru că" (NR 630), „shunt"→„șunt"
  (NR 590, forma românească e deja folosită în capitol), plus alte `si`→`și`,
  `fractie`→`fracție`, `incărcare`→`încărcare`, `evidentiere`→`evidențiere`,
  `cinetica`/`fibroza`→`cinetică`/`fibroză` (NR 579, 584, 589, 590, 620, 624, 625).
- **MODIFICAT (normalizare) — spații parazite.** Tip „M " (NR 613) și Examen „Angio-CT "
  (NR 643), „Echo Doppler " (NR 648) → fără spațiu final; comentarii cu spațiu final /
  inițial (NR 587, 615) și `\n` final (NR 616) curățate.
- **VERIFICAT (regula „informația de situație pe toate investigațiile") — conform.**
  Notele de nivel-situație sunt deja copiate pe toate rândurile situației acolo unde există
  (NR 575/576 „CT și IRM au aceeași valoare diagnostică"; NR 594–596 „Examenele au valori
  similare"; NR 634–637 „La un pacient cu insuficiență cardiacă și leziuni coronariene
  extensive…"). Restul comentariilor sunt strict per-investigație (ce arată / cum se face
  fiecare modalitate) și rămân, corect, pe rândul lor. **Nicio propagare necesară.**

### MODIFICAT — Decizii editoriale aplicate (Cardiovascular, 2026-07-08)

Rezolvarea celor trei chestiuni din `EDITORIAL-decisions.md` §12:

- **RESTRUCTURAT (ordine) — „Anevrisme vase periferice": Eco Doppler pe prima poziție.**
  Ordinea rezultată mecanic din fuziune (Angio-CT → Eco → Angio-IRM) a fost reordonată la
  **Eco Doppler (NR 648) → Angio-CT (NR 647) → Angio-IRM (NR 649)**, consecvent cu nota
  „metoda de primă intenție" a Eco Doppler și cu situația-soră „Arteriopatii periferice".
  Reordonare fizică a rândurilor; NR.CRT neschimbate.
- **MODIFICAT (Situație → Comentarii) — notă clinică scoasă din etichetă.** Eticheta
  „Arteriopatii periferice simptomatice **(arteriopatiile asimptomatice nu necesită
  evaluare imagistică!)**" → „Arteriopatii periferice simptomatice". Nota (prag de
  indicație, valabilă pentru toată situația) a fost mutată în `Comentarii` pe **toate cele
  3 investigații** (NR 650–652), per regula „informația de situație pe toate investigațiile".
- **MODIFICAT (Indicație) — scintigrafia osoasă la amiloidoza transtiretină aliniată la
  ghid.** NR 589 (Scintigrafie osoasă Tc99m-pirofosfat/HDP, situația „…suspiciune de
  amiloidoză transtiretină"): Indicație „Doar în cazuri particulare" → **„Indicat"**.
  Motivare: în ghidurile actuale (ESC 2021 pe cardiomiopatii; criteriile Gillmore et al.)
  scintigrafia osoasă e **testul-cheie non-invaziv** pentru ATTR — captarea miocardică
  Perugini 2–3, cu excluderea gamapatiei monoclonale, confirmă diagnosticul fără biopsie
  (recomandare de Clasă I). **Gradul B rămâne** (nivelul de evidență ESC pentru acest test
  este B — modificarea privește puterea indicației, nu nivelul de evidență).

## 5. Torace
_NR 662–736 (fără 695–705)_

- **MUTAT —** 11 rânduri intervenționale relocate la RI › Aparat respirator.

### ⛔ BREAKING — „Neoplasm bronhopulmonar" mutat la Cancer (2026-07-08)

Cele **11 rânduri** „Neoplasm bronhopulmonar" (NR 695–705, subcapitolul Pulmon) au fost
**eliminate** din Torace și reconciliate în **Cancer › Cancer bronho-pulmonar** — malignitatea
cunoscută trăiește în Cancer (ierarhia capitolelor, regula 3). Detaliul reconcilierii
(duplicate eliminate, note păstrate, faza Monitorizare completată cu ID 1472/1473, conflicte
de grad) e la **§3 Cancer**. Rândurile diagnostice de nodul pulmonar (NR 706–708, „Nodul
pulmonar solitar") **rămân în Torace** — nodul indeterminat ≠ malignitate confirmată.
Subcapitolul Pulmon nu rămâne husk (25+ alte situații). Torace: 75 → **64 rânduri**.

### MODIFICAT — Review capitol Torace (2026-07-08)

Review complet al capitolului (checklist din `CLAUDE.md` › „Plan de lucru"). **18 editări
mecanice** pe 11 rânduri (NR 664–729), toate în capitol; fără schimbări de grad, doză,
indicație sau ordine a examenelor. Validare verde, 0 cedile.

- **MODIFICAT (Situație) — diacritice lipsă.** „Bron**s**ita acută" → „Bron**ș**ita acută"
  (NR 677); „Transplant de **ma**duvă osoasă" → „Transplant de **mă**duvă osoasă" (NR 728,
  729; forma corectă „măduvă" e cea standard).
- **MODIFICAT (Examen) — diacritice și aliniere.** „CT cerebral, abdomen **si** pelvis" →
  „…**și** pelvis" (NR 697); „Scintigrafie osoasă … WB **si** \\nSPECT-CT\\n" → „…WB **și**
  \\nSPECT-CT" (NR 702: `si`→`și`, spațiu parazit și `\n` final eliminate, aliniat identic
  cu rândul-soră NR 338 din capitolul Cancer › Cancer bronho-pulmonar).
- **MODIFICAT (Comentarii) — diacritice și typo-uri**, doar unde forma corectă e neambiguă:
  „caracteriza**rii**"→„caracteriză**rii**" și „plămânului sub**j**acent"→„sub**i**acent"
  (NR 664, forma „subiacent" e deja folosită în fișier); la NR 681 curățare masivă de
  diacritice pe descrierea scintigrafiei de ventilație-perfuzie („pe**f**uzie"→„per**f**uzie",
  „Contraindicati**i**"→„Contraindicați**i**", „substanta activa"→„substanța activă",
  „excipienti"→„excipienți", „**in** caz de hipertensiune pulmonara severa"→„**în** caz…
  pulmonară severă", „femeile **in**sarcinate sau potential **in**sarcinate **si** la copii"→
  „**în**sărcinate sau potențial **în**sărcinate **și** la copii"); pe blocul de urmărire
  a nodulilor de la NR 708 „12 luni **si** apoi"→„…**și** apoi", „persoane **fara** risc"→
  „…**fără** risc" și „biopsie/reze**c**tie"→„biopsie/reze**c**ție"; „supliman**ta**ră"→
  „suplimen**ta**ră" și abrevierea „**pt**"→
  „**pentru**" (NR 727).
- **MODIFICAT (normalizare) — spații parazite.** Spațiu final la NR 681 și 709; spațiu
  inițial la NR 696 („ Performanțele"→„Performanțele") — curățate.
- **VERIFICAT (Tip ↔ Examen) — conform.** Toate codurile de modalitate se potrivesc
  denumirii (E=Eco/Doppler/Ecocardiografie, G=Radiografie, T=CT, M=IRM, N=PET-CT/Scintigrafie);
  0 coduri inversate.
- **VERIFICAT (de-duplicare) — fără duplicate exacte în capitol.** Comentariul identic de la
  NR 670 („Aplazie medulară") și NR 729 („Transplant de măduvă osoasă") aparține unor situații
  diferite → păstrat (regula „comentariile identice se păstrează").
- **DE-DUPLICAT (Situație) — eticheta „Nodul pulmonar" unificată la „Nodul pulmonar
  solitar".** Decizie editor. NR 706 (PET-CT) purta eticheta scurtată „Nodul pulmonar", pe
  când NR 707 (CT torace) folosea „Nodul pulmonar solitar" — aceeași situație în același
  subcapitol (Pulmon). Unificată la „Nodul pulmonar solitar"; cele două examene stau acum
  sub o singură situație. **Reordonat** CT torace (NR 707, detecție de primă intenție,
  Indicat B) înaintea PET-CT (NR 706, „Doar în cazuri particulare", nodul solid > 8 mm) —
  ordinea rezulta invers din poziția fizică. Reordonare fizică a rândurilor; NR.CRT
  neschimbate. NR 708 („Nodul pulmonar solitar urmărire") rămâne situație distinctă.
- **DE DECIS (editorial) — vezi `EDITORIAL-decisions.md` §13:** încadrarea rândurilor
  „Neoplasm bronhopulmonar" (NR 695–705) — suprapunere de topic cu subcapitolul existent
  „Cancer bronho-pulmonar" (NR 334–343) din capitolul Cancer; per ierarhie (regula 3)
  malignitatea cunoscută → Cancer. Lăsat neschimbat (nu se decide unilateral).

## 6. Aparat digestiv
_NR 737–806_

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
- **REVIZUIT — trecere completă (2026-07-08),** aceeași metodă ca la Cancer:
  - **MODIFICAT (date) — 25 câmpuri** cu spații parazite (inițiale/finale/duble) eliminate,
    inclusiv 11 caractere spațiu nesecabil (`\xa0`, artefact de copy-paste) în NR 947.
  - **MODIFICAT (date) — corectură ortografică** NR 950: „distanta"→„distanță",
    „pacientii"→„pacientele" (genul corect, consecvent cu restul capitolului),
    „crescuti"→„crescuți", „si"→„și".
  - **RESTRUCTURAT — reordonare fizică** (fără schimbare de conținut): situația
    „Stadializarea cancerului de sân: metastaze la distanță" (Cancer de sân) și
    „Suspiciune clinică de cancer la paciente cu augmentare (implante)" (Paciente cu
    simptome sugestive) erau rupte în două blocuri neadiacente în CSV, întrerupte de alte
    situații — rândurile au fost regrupate contiguu.
  - **UNIFORMIZAT — punctuația etichetelor „Depistare (Screening)"**: 3 situații foloseau
    virgulă („Depistare (Screening), femei…"), 4 foloseau două puncte („Depistare
    (Screening): femei…") — unificate la două puncte (8 rânduri). Redenumit și „Screening,
    femei cu augmentare mamară" → „Depistare (Screening): femei cu augmentare mamară",
    pentru consecvență cu restul situațiilor de screening din același subcapitol.
  - **Semnalat, nemodificat** — NR 961 („Depistare (Screening): femei peste 50 ani, THS",
    Ecografie, *Neindicat* B): comentariul („Ecografia mamară este utilă ca examen
    complementar în cazul unui sân dens și al femeilor cu proteze.") nu explică de ce e
    *Neindicat*, spre deosebire de rândul-soră NR 967 (grup de vârstă 50-70 ani, aceeași
    recomandare, comentariu clar: „Ecografia e indicată în diagnostic, nu în screening.").
    Probabil doar o formulare neclară (logica generală a capitolului — ecografie utilă/
    indicată sub 50 ani, neindicată peste 50 ani, corelat cu densitatea mamară — e
    consecventă în rest), dar merită o a doua opinie a editorului.

## 10. Cap
_NR 959–1074_

- **MUTAT —** 25 rânduri intervenționale (neurovasculare) relocate la RI › Sistem nervos.
- **MUTAT / ELIMINAT — consolidare oncologie → Cancer** (vezi „Modificări globale"):
  subcapitolul „Neuro › Tumori cerebrale" dubla parțial „Cancer › Tumori cerebrale și
  medulare" (conflict de grad pe IRM/CT — semnalat, nerezolvat unilateral). 1 rând mutat
  (scintigrafie cerebrală cu traceri de viabilitate, conținut absent din Cancer) + 3
  eliminate ca duplicate/conflict de grad. (−3 rânduri)

## 11. Gât (părți moi)
_NR 1075–1092_

- **MUTAT —** 8 rânduri intervenționale (PCAFGE) relocate la RI: tiroidă/paratiroidă
  → Aparat endocrin; „Masă cervicală" → Oncologie.

## 12. Coloană vertebrală
_NR 1093–1147_

- **MUTAT —** 7 rânduri intervenționale relocate la RI: vertebroplastie / biopsie /
  infiltrație → Aparat locomotor; embolizări spinale → Sistem nervos.

## 13. Aparat locomotor
_NR 1148–1221_

- **MUTAT —** 13 rânduri intervenționale relocate la RI › Aparat locomotor.
- **MUTAT — consolidare oncologie → Cancer** (vezi „Modificări globale"): subcapitolul
  „Diverse" avea deja o structură os/părți moi mai precisă decât varianta generică din
  Cancer › „Tumori ale aparatului locomotor". Toate cele 13 rânduri (Diagnostic +
  bilanț de extensie, os și părți moi separat) mutate în Cancer, înlocuind cele 10
  rânduri generice vechi. (−13 rânduri)

## 14. Radiologie intervențională
_NR 1222–1471_

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
  NR 1455/1456 (rahialgie). Vezi `DUPLICATE-review.md`.
- **Plasările pe muchie** din Gât și Coloană (vezi maparea) — de validat clinic.
