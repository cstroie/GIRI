# Decizii editoriale — de discutat cu ceilalți editori

NR = NR.CRT curent. (Numerotarea veche nu se mai păstrează.)

---

## 1. Artrografia articulației temporo-mandibulare (ATM) — încadrare capitol

✅ **Decizie luată (2026-07-10):** artrografia ATM se **mută la Cap › ORL**, în situația
„Disfuncții ale articulației temporo-mandibulare", la finalul examenelor. Reclasificată
**Tip `I` → `X`** (exam diagnostic cu contrast, nu intervențional). Cele 3 rânduri din RI
consolidate în **unul** (grad `B`, versiunea codată; eliminate dublura de la RI › Aparat
digestiv și varianta grad „?"). Cod `RI - PC8` scos. Vezi `CHANGELOG.md` §10 și §14.
_Rămas de reconfirmat de editori:_ alegerea gradului `B` (vs. „?") și dacă rândul „Neindicat"
se păstrează pe termen lung sau se elimină.

**Context (istoric):**

- **NR 1451** · RI › Sistem nervos · „Disfuncții ale articulației temporo-mandibulare" ·
  Tip I · „Artrografie articulații temporo-mandibulare" · **Neindicat** · grad „?" ·
  _„Artrografia temporo-mandibulară este în prezent înlocuită de examenul IRM."_
- **NR 1452** · RI › Sistem nervos · idem · Tip I · **Neindicat** · grad „B" ·
  aceeași notă · „RI - PC8".
- **NR 1349** · RI › Aparat digestiv · artrografie (existentă în RI, subcapitol aparent greșit).

**De decis:**

1. **Încadrare pe subcapitol.** ATM este anatomic o articulație → logic ar sta la
   **Aparat locomotor**, nu la Sistem nervos (unde a ajuns automat, venind din capitolul
   „Cap"). NR 1349 pare greșit la „Aparat digestiv". Confirmați subcapitolul corect.
2. **Păstrare vs. eliminare.** Ambele rânduri sunt **Neindicat**, cu nota că artrografia
   ATM „este în prezent înlocuită de examenul IRM". De decis dacă se mai păstrează în ghid
   (ca indicație istorică / negativă) sau se elimină.

---

## 2. ERCP (Tip D) rămas în capitolele de origine

✅ **Decizie luată**: ERCP **rămâne** în capitolul de origine (nu se mută la
Radiologie intervențională), deși este o procedură intervențională. În coloana 
„Terapeutic" este marcat **Da**. De reconfirmat la review dacă poziționarea e cea dorită.

---

## 3. Pediatrie — omisiuni de patologie (propuneri de adăugat)

Din analiza capitolului Pediatrie (NR 1–155). Patologii frecvente aparent neacoperite,
propuse pe baza practicii curente și a ghidurilor de referință (ACR Appropriateness
Criteria, RCR iRefer). **Schițe — de validat clinic de editori** înainte de inserare
în `GHID.csv`. Gradele și dozele sunt propuneri.

### 3.1 Aparat digestiv
- **Boală inflamatorie intestinală (Crohn) — bilanț/monitorizare.** Lipsă. Propunere:
  Entero-IRM = *Indicat, grad B* (metoda de referință la copil, neiradiantă); Ecografie
  de anse = *Indicat, grad B* (primă intenție, monitorizare); CT/entero-CT = *Doar în
  cazuri particulare* (acut/ocluziv, când IRM indisponibil).
- **Hernie inghinală / patologie de canal** — de obicei diagnostic clinic; eventual o
  linie „Ecografie — Doar în cazuri particulare" pentru cazuri echivoce. De decis dacă
  merită rând propriu.

### 3.2 Aparat locomotor
- **Artrită septică / osteomielită acută** (situație dedicată, distinctă de „Durere
  osoasă focalizată" și „Șold dureros"). Propunere: Ecografie = *Indicat, grad B*
  (revărsat articular, ghidaj puncție); IRM = *Indicat, grad A* (referință, edem osos
  precoce); Radiografie = *Indicat, grad C* (inițial adesea normală); Scintigrafie =
  *Doar cu aviz specializat*.
- **Artrită idiopatică juvenilă (AIJ)** — bilanț articular. Lipsă. IRM cu contrast =
  *Indicat, grad B*; Ecografie = *Indicat, grad B*.

### 3.3 Torace
- **Bronșiolită acută (sugar).** Lipsă. Mesaj util (evită iradiere): Radiografie
  toracică = *Neindicat, grad B* de rutină în forma tipică; doar în forme severe/atipice
  sau agravare.
- **Malformații pulmonare congenitale (CPAM/sechestrare)** — bilanț postnatal.
  CT toracic cu contrast = *Indicat, grad B*; Radiografie = *Indicat, grad C*.

### 3.4 Uro-nefrologie
- **Hematurie** (macroscopică/microscopică). Lipsă ca situație distinctă. Ecografie
  reno-vezicală = *Indicat, grad B* primă intenție.
- **Litiază renală** — apare doar în treacăt (RRVS, NR 134/145). Propunere situație
  proprie: Ecografie = *Indicat, grad A*; CT low-dose fără contrast = *Doar cu aviz
  specializat* (când ecografia e neconcludentă).

### 3.5 Gât și coloană vertebrală
- **Mase cervicale congenitale** (chist tireoglos, chist branhial) — distinct de
  „Adenopatii cervicale". Ecografie = *Indicat, grad A* primă intenție; IRM/CT cu
  contrast = *Doar cu aviz specializat* (bilanț preoperator).

### 3.6 Rânduri-schiță pentru inserare (draft insertion-ready, de validat de editori)

Coloane fixe pentru toate: `Capitol = Pediatrie`, `Terapeutic = Nu`; `NR.CRT` = ID nou, atribuit
la inserare (la finalul secvenței). `Alte informații` = referința indicată sub fiecare situație.
Gradele/dozele sunt orientative; ordinea examenelor = de la prima intenție în jos. **Referințe
confirmate real (2026-07-10):** ACR AC *Hematuria-Child*, *Osteomyelitis or Septic Arthritis-Child
(Excluding Axial Skeleton)* (2022), *Acutely Limping Child Up To Age 5*; AAP *Bronchiolitis* CPG
(2014); EULAR-PReS imaging in JIA (Colebatch-Bourn, Ann Rheum Dis 2015).

#### (1) `Pediatrie › Aparat digestiv` — **Boală inflamatorie intestinală (Crohn) – bilanț și monitorizare**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Crohn Disease (considerații pediatrice); ESPGHAN/ESPR."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| M | Entero-IRM | Indicat | B | 0/0 | Metoda de referință la copil (neiradiantă): extindere, activitate inflamatorie, complicații (stenoze, fistule, abcese). De preferat pentru monitorizarea repetată. |
| E | Ecografie de anse intestinale | Indicat | B | 0/0 | Primă intenție și monitorizare: îngroșare parietală, hiperemie Doppler, complicații. Accesibilă, fără sedare/iradiere. |
| T | Entero-CT | Doar în cazuri particulare | B | 2/3 | Rezervat contextului acut/ocluziv sau când IRM nu e disponibil (iradiere — de evitat la monitorizarea repetată la copil). |

> **Hernie inghinală / patologie de canal** — diagnostic clinic; **nu se drafteză rând propriu**
> (acoperire imagistică marginală). Dacă editorii doresc totuși o linie pentru cazuri echivoce:
> Ecografie = *Doar în cazuri particulare, grad C*.

#### (2) `Pediatrie › Aparat locomotor` — **Artrită septică / osteomielită acută**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Osteomyelitis or Septic Arthritis-Child (Excluding Axial Skeleton); Acutely Limping Child Up To Age 5."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| E | Ecografie | Indicat | B | 0/0 | Primă intenție articulară: revărsat, ghidarea puncției/artrocentezei (cheia diagnosticului de artrită septică). |
| M | IRM | Indicat | A | 0/0 | Examen de referință: edem osos precoce, abces subperiostal/de părți moi, extensie; cu substanță de contrast când e disponibilă. |
| G | Radiografie | Indicat | C | 1/1 | Inițial adesea normală (modificările osoase apar tardiv); utilă pentru excluderea altor cauze (fractură, tumoră osoasă). |
| N | Scintigrafie osoasă | Doar cu aviz specializat | B | 2/3 | Când sediul nu poate fi localizat clinic sau la suspiciune de focare multiple; IRM preferată dacă e disponibilă. |

#### (3) `Pediatrie › Aparat locomotor` — **Artrită idiopatică juvenilă (AIJ) – bilanț articular**
`Alte informații =` „Cf. EULAR-PReS – imaging in juvenile idiopathic arthritis (Colebatch-Bourn 2015)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| M | IRM cu substanță de contrast | Indicat | B | 0/0 | Sinovită, edem osos, eroziuni precoce; util mai ales la articulații profunde (șold, ATM, sacro-iliace). Gadolinium pentru evaluarea activității sinoviale. |
| E | Ecografie (Doppler) | Indicat | B | 0/0 | Sinovită, revărsat, hiperemie Doppler; monitorizarea articulațiilor superficiale, ghidarea infiltrațiilor. Neiradiantă, fără sedare. |

#### (4) `Pediatrie › Torace, pulmon, cord` — **Bronșiolită acută (sugar)**
`Alte informații =` „Cf. AAP Clinical Practice Guideline – Bronchiolitis (2014)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| G | Radiografie toracică | Neindicat | B | 1/1 | Diagnostic clinic; radiografia de rutină NU e indicată în forma tipică (crește riscul de supradiagnostic de pneumonie și de antibioterapie inutilă). Doar în forme severe/atipice, agravare sau necesar de terapie intensivă. |

#### (5) `Pediatrie › Torace, pulmon, cord` — **Malformații pulmonare congenitale (CPAM / sechestrare pulmonară) – bilanț postnatal**
`Alte informații =` „Literatura de specialitate (bilanț imagistic postnatal CPAM/sechestrare) — *de confirmat sursa citabilă*."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | Angio-CT toracic cu substanță de contrast | Indicat | B | 2/3 | Caracterizare postnatală: definește leziunea (CPAM vs sechestrare) și identifică **pediculul arterial sistemic** (de obicei aortic) al sechestrării — esențial pre-chirurgical. |
| G | Radiografie toracică | Indicat | C | 1/1 | Evaluare inițială postnatală; o radiografie normală NU exclude leziunea (bilanțul se completează prin CT). |

> Notă: editorialul propunea „CT toracic cu contrast"; rafinat la **angio-CT**, fiindcă maparea
> aportului arterial sistemic (diagnosticul de sechestrare) e obiectivul-cheie. Sursa citabilă
> rămâne de fixat de editori.

#### (6) `Pediatrie › Uro-nefrologie` — **Hematurie (macroscopică / microscopică)**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Hematuria-Child."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| E | Ecografie reno-vezicală | Indicat | B | 0/0 | Primă intenție: parenchim renal, dilatația căilor, litiază, mase; neiradiantă. Explorările ulterioare doar în funcție de rezultat/context clinic. |

#### (7) `Pediatrie › Uro-nefrologie` — **Litiază renală (colică / suspiciune)**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Hematuria-Child (varianta durere / urolitiază)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| E | Ecografie reno-vezicală | Indicat | A | 0/0 | Primă intenție la copil pentru litiază: detectează calculii și hidronefroza, fără iradiere. |
| T | CT low-dose fără substanță de contrast | Doar cu aviz specializat | B | 2/2 | Când ecografia e neconcludentă și persistă suspiciunea clinică; protocol low-dose (minimizarea iradierii la copil). |

#### (8) `Pediatrie › Gât și coloană vertebrală` — **Mase cervicale congenitale (chist tireoglos, chist branhial)**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Neck Mass/Adenopathy (considerații pediatrice)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| E | Ecografie | Indicat | A | 0/0 | Primă intenție: localizare, caracter chistic/solid, raport cu osul hioid (tireoglos) / marginea sternocleidomastoidianului (branhial); **confirmă țesut tiroidian normal** înainte de excizia unui chist tireoglos. |
| M | IRM cu substanță de contrast | Doar cu aviz specializat | B | 0/0 | Bilanț preoperator pentru leziuni profunde/complicate (extensie, raporturi); alternativă neiradiantă la CT. |
| T | CT cu substanță de contrast | Doar cu aviz specializat | B | 2/3 | Bilanț preoperator când IRM nu e disponibil sau la suprainfecție (definește colecția). |

---

## 4. Pediatrie — chestiuni editoriale de stil

1. ✅ **Comentarii identice pe rânduri ale aceleiași situații** (ex. NR 12/13, 16/17,
   89/90) — **DECIS: se păstrează.** Fiecare comentariu aparține unei situații; e normal
   ca rânduri diferite să fie identice. Rândurile rămân auto-suficiente. (Vezi CLAUDE.md.)
2. ✅ **Ordinea indicațiilor în cadrul unei situații** — **DECIS: intențională, nu se
   reordonează.** Reflectă prioritatea clinică. (Vezi CLAUDE.md.)
3. **Gradele nu se modifică** (vezi CLAUDE.md). Cazuri care par evident greșite, de
   verificat de editori (listă deschisă):
   - ⏳ _(niciunul confirmat încă)_ — ex. semnalat la analiză: Ecografie „Masă abdominală
     sau pelvină palpabilă" NR 22 = grad B, în timp ce ecografia e grad A în situații
     similare. Probabil intențional (context clinic diferit); de reconfirmat.

---

## 5. Subcapitole-husk rămase de confirmat (audit global)

Găsite la auditul global, subcapitol **doar** cu rândul-placeholder Tip Z,
fără situație reală.

- ✅ **„Aparat digestiv › Abdomen"** — REZOLVAT (review Cancer, 2026-07): eliminat.
  Bucket generic gol; capitolul e organizat pe organ („Ficat, colecist și pancreas",
  „Tub digestiv"). (cap. 6)
- ✅ **„Aparat uro-genital › Uter și anexe"** — REZOLVAT (review Aparat uro-genital,
  2026-07-09): eliminat. Conținutul de uter/anexe trăiește deja în Obstetrică-ginecologie
  (Ginecologie / Sarcină) și Cancer (col/corp uterin). (cap. 7)

---

## 6. Pediatrie — bucket-uri de context (după crearea „Pediatrie › Traumatisme")

S-a creat subcapitolul de context **`Pediatrie › Traumatisme`** (relocare pură, CHANGELOG §1).
Consecințe de decis:

- ✅ **Trauma abdominală majoră pediatrică — REZOLVAT.** Adăugat rândul „Traumatism
  abdominal major la copil" (eco FAST, CT cu contrast, CEUS, radiografie) și retras
  breadcrumb-ul de pe forma minoră; perechea e acum simetrică („minor / major la copil").
  Împreună cu alte 4 situații de traumă pediatrică lipsă (coloană cervicală, torace, membru,
  politraumatism) — vezi CHANGELOG §1.
- ✅ **Oncologia pediatrică — REZOLVAT.** Creat `Pediatrie › Oncologie`; mutată „Masă
  abdominală palpabilă" (îmbogățită cu diagnosticul diferențial pentru căutare); adăugate
  **7 situații** (tumori cerebrale/medulare, retinoblastom, neuroblastom-stadializare, limfom,
  tumori osoase, rabdomiosarcom/sarcom de părți moi, histiocitoză Langerhans) și eliminat
  breadcrumb-ul stub NR 113 — vezi CHANGELOG §1. „Adenopatii cervicale" (NR 66) rămâne în
  „Gât și coloană" (încadrare inflamatorie la copil).

---

## 7. Traumatisme (adult) — granița Abdomen vs Bazin

**Situația:** capitolul Traumatisme are două subcapitole care ating bazinul:

- **`Abdomen`** → o singură situație: **„Traumatism abdominal major și/sau de bazin"**
  (Ecografie, Radiografie abdominală și/sau de bazin, CT abdomino-pelvin).
- **`Bazin și sacru`** → **„Traumatism izolat de bazin"** (CT de bazin, Radiografie de
  bazin, IRM de bazin).

Prin urmare, trauma de bazin apare în **două locuri**: forma combinată (abdomino-pelvină,
politraumatism de mare energie) în „Abdomen", forma izolată (inel pelvin) în „Bazin și sacru".

**Opțiuni:**
1. **Păstrare (recomandarea mea).** Cele două reflectă scenarii clinice distincte: trauma
   abdominală majoră cu interesare pelvină se explorează printr-un **CT abdomino-pelvin
   unic** (o situație), pe când fractura izolată de bazin e un workup separat. Suprapunerea
   e intențională, nu o eroare. Eventual s-ar clarifica doar formularea („și/sau de bazin"
   = «când coexistă cu trauma abdominală»).
2. **Separare strictă.** „Abdomen" devine pur abdominal („Traumatism abdominal major"),
   iar tot ce ține de bazin (izolat + combinat) merge la „Bazin și sacru". Dezavantaj:
   trauma combinată abdomino-pelvină nu are un home natural (se explorează împreună).
3. **Comasare** într-un subcapitol „Abdomen și bazin". Dezavantaj: pierde distincția
   regiune-anatomică curată.

> Status: ✅ **REZOLVAT — opțiunea 1** (păstrare + clarificare). Cele două situații sunt
> clinic distincte (viscere abdominale ± bazin pe același CT, vs inel pelvin osos izolat);
> nu s-au comasat. Situația din „Abdomen" a fost redenumită „Traumatism abdominal major"
> (fără „și/sau de bazin"), iar comentariul CT precizează că achiziția trebuie să includă
> bazinul. Vezi CHANGELOG §2.

---

## 8. Traumatisme (adult) — sub-axa regiune + fațete; „Corp străin › Ingestie"

✅ **Decis (documentat în `CLAUDE.md`):** sub-axa Traumatisme = **regiune anatomică + un set
închis de 4 fațete cross-region** (Sistem vascular, Politraumatism, Corp străin, Aparat
urogenital). Fiecare fațetă traversează regiuni și are un workup coerent; dizolvarea lor în
regiuni ar fragmenta topicuri clinice unitare. Setul e închis — fără alte subcapitole
organ-sistem în Traumatisme.

⏳ **De discutat mai departe — „Corp străin" conține două lucruri diferite:**
- **„Traumatism de părți moi cu suspiciune de corp străin"** (metal, sticlă, lemn) —
  penetrant, **clar traumă**. ✓ rămâne.
- **„Ingestie de corp străin, situat la nivel faringian sau esofagian înalt"** (NR 250–252)
  — corp străin **ingerat**, care e mai degrabă patologie **digestivă / ORL**, nu traumă.
  Paralel cu decizia pediatrică (corpul străin la copil → capitolul Torace/respirator, nu
  Traumatisme). **Decizie (utilizator): rămâne deocamdată în Traumatisme › Corp străin**, dar
  de reevaluat: se mută la Aparat digestiv (sau un capitol ORL / căi aero-digestive), lăsând
  „Corp străin" = doar corpul străin penetrant de părți moi? De discutat în echipă.
  **Actualizare 2026-07-09:** versiunea aproape identică din `Cap › ORL` (NR 1007–1008,
  „Corp străin faringian sau esofagian înalt") a fost **mutată la Gât (părți moi) › Diverse**
  (la cerere) — vezi §10 mai jos. Rezultă un **cvasi-duplicat cross-capitol**
  Traumatisme/Corp străin ↔ Gât (părți moi)/Diverse, nerezolvat — aceeași întrebare de fond
  (ORL/digestiv vs traumă), acum cu trei capitole candidate. Consemnat în
  `DUPLICATE-review.md` §C.

---

## 9. Coloană cervicală — „CT-întâi" (modernizare, separat de consolidare)

Consolidarea celor 9 situații în 5 (CHANGELOG §2) a **păstrat filozofia ghidului:
radiografie-întâi la pacientul cu risc scăzut / benign** („Traumatism cervical benign"
spunea explicit „nu există argumente pentru a înlocui radiografia cu CT", grad A).

⏳ **De decis separat:** practica modernă (ACR Appropriateness Criteria, EAST, NICE NG41)
recomandă **CT-întâi** pentru orice pacient care necesită imagistică (CT a înlocuit
radiografia ca test de screening primar; radiografia rămâne pentru cazuri selectate).
Trecerea la „CT-întâi" ar schimba indicațiile/gradele pe situația de evaluare inițială —
o decizie clinică de sine stătătoare, nu de amestecat în consolidare. De discutat în echipă.

---

## 10. Situații de traumă rămase în capitole diagnostice (de reconciliat la parsarea lor)

Căutare (2026-07) în capitolele diagnostice (exclus Pediatrie, RI, Traumatisme) după
situații de **leziune traumatică acută** care, per ierarhie (regula 4), ar trebui să stea în
**Traumatisme**. Rezultat: un singur cluster real, tot în capitolul **Cap** — și **paralel
(nu identic)** cu situații deja existente în Traumatisme, deci necesită **reconciliere**
(nu mutare oarbă): se compară cele două versiuni, se păstrează conținutul mai bun/complet,
se elimină duplicatul. **De făcut la parsarea capitolului Cap**, nu acum.

✅ **REZOLVAT (2026-07-09).** Cele 7 situații de traumă față/craniu din Cap au fost
**eliminate** (dublau, cu variații, situațiile canonice din Traumatisme, care erau egale sau
mai bune). Comentariul clinic al radiografiei nazale a fost salvat în Traumatisme. Vezi
CHANGELOG §10 (−23 rânduri). Perechile reconciliate:
- `Cap › Neuro: Traumatisme cranio-encefalice` → duplica `Traumatisme › Cap` (Cap avea „?" la Rg craniu).
- `Cap › ORL: orbită – obiecte neascuțite / prin perforare` → duplica `Față și orbite: orbitar
  contondent / penetrant` (Cap avea etichete greșite „regiune cervicală", Rg „?").
- `Cap › ORL: stâncă temporală / 1/3 centrală a feței / mandibulă / nazal` → duplicau omologii
  din `Față și orbite` (la mandibulă, Traumatisme are OPG „Indicat" + Alte informații mai complete).

✅ **REZOLVAT (2026-07-09) — mutat, nu comasat.** `Cap › ORL → Corp străin faringian sau
esofagian înalt` (NR 1007–1008) — corp străin **ingerat** — a fost mutat la cerere în
**`Gât (părți moi) › Diverse`** (NR.CRT neschimbate). Rămâne totuși **aproape identic** cu
`Traumatisme › Corp străin: Ingestie de corp străin, situat la nivel faringian sau esofagian
înalt` (NR 250–252) — chestiunea de fond (ORL/digestiv vs traumă, §8) **nu e rezolvată**,
doar relocată: acum e un duplicat între Gât (părți moi) și Traumatisme, nu între Cap și
Traumatisme. Vezi `DUPLICATE-review.md` §C.

**Fals-pozitive (NU sunt traumă acută — rămân unde sunt, confirmat):**
- `Coloană › Bilanț fractură vertebrală spontană` (fractură spontană/patologică).
- `Coloană › Sindrom medular (în afara traumatismelor coloanei vertebrale)` (explicit ne-traumatic).
- `Coloană cervicală › Posibilitate de subluxație atlanto-axoidiană` (de regulă reumatoidă/congenitală).
- `Aparat locomotor › Gonalgie (meniscală/condropatie)` (patologie cronică internă a genunchiului).

---

## 11. Cancer — subcapitole fără fază „Monitorizare" (goluri de conținut)

După unificarea etichetelor de situație la axa canonică **Diagnostic → Stadializare →
Monitorizare** (2026-07-08), au rămas **9 subcapitole** fără nicio secțiune de
monitorizare/urmărire post-terapeutică. Nu știu dacă e omisiune reală a sursei sau
lipsă intenționată (unele cancere se urmăresc predominant non-imagistic) — 
inventariez pentru decizia editorilor:

- ⏳ **Cancer de corp uterin** — are doar Diagnostic + Stadializare. Urmărirea endometrială
  e predominant clinică/citologică; posibil intenționat, dar multe ghiduri recomandă
  IRM/CT la recidivă suspectată — de verificat.
- ⏳ **Cancer esofagian** — surprinzător absent; supravegherea postoperatorie/postterapeutică
  prin CT e practică standard. Pare omisiune.
- ⏳ **Cancer gastric** — similar cu esofagianul; CT de urmărire e uzual. Pare omisiune.
- ⏳ **Cancer pancreatic** — pare omisiune notabilă: supravegherea imagistică postoperatorie
  (CT) e standard, mai ales cu rată mare de recidivă.
- ⏳ **Cancer prostatic** — urmărirea e predominant prin PSA, non-imagistică; **posibil
  intenționat**. Scintigrafia osoasă/IRM apar doar la restadializare (deja acoperite
  parțial de „Stadializare").
- ⏳ **Cancer vezical** — urmărirea standard e cistoscopică (nu imagistică), dar CT
  urografie/torace apare des în ghiduri pentru tumori infiltrative. Ambiguu.
- ⏳ **Cancerul parotidian** — surprinzător absent, mai ales că restul cancerelor ORL din
  capitol (laringian, tiroidian, căi aero-digestive, nazofaringian) au toate
  „Monitorizare". Pare omisiune / inconsecvență cu restul clusterului ORL.
- ⏳ **Tumori maligne primare hepatice (CHC)** — pare omisiune notabilă: supravegherea
  postterapeutică (post-rezecție/ablație/transplant) prin IRM/CT e practică standard,
  menționată chiar în comentariile de la „Stadializare" ("Este metodă de referință
  pentru aprecierea răspunsului terapeutic în nodulii tumorali tratați").
- ⏳ **Tumori maligne secundare hepatice** — are doar Diagnostic (nici Stadializare). Posibil
  intenționat — subcapitolul e strict despre detecția/caracterizarea metastazelor
  hepatice, stadializarea bolii de fond ținând de capitolul cancerului primar.

> Status: **inventariat, neatins.** Dacă se decide completarea vreunuia, conținutul
> (examen, grad de indicație) trebuie să vină dintr-o sursă citabilă (ACR/ESMO/RCR sau
> echivalent), nu inventat.

---

## 12. Cardiovascular — chestiuni rămase după review (2026-07-08)

Rezolvate la reviewul capitolului 4 (vezi CHANGELOG §4). Corecturile mecanice (ortografie,
normalizare, Tip↔Examen, de-duplicare de etichetă) au fost aplicate; rămân următoarele,
care ating grade / ordine / formulare clinică → **decizia editorilor**, neatinse în date:

1. ✅ **REZOLVAT — ordinea examenelor la „Anevrisme vase periferice".** Decizie editor:
   **Eco Doppler pe prima poziție.** Ordinea CT-întâi rezultase mecanic din fuziunea
   celor două etichete (CT era rândul singular NR 647). Reordonat la **Eco Doppler (648) →
   Angio-CT (647) → Angio-IRM (649)** — consecvent cu nota „metoda de primă intenție" a Eco
   Doppler și cu situația-soră „Arteriopatii periferice simptomatice" (Eco → CT → IRM).
   Reordonare fizică a rândurilor; NR.CRT neschimbate. Vezi CHANGELOG §4.

2. ✅ **REZOLVAT — notă clinică scoasă din eticheta „Arteriopatii periferice simptomatice".**
   Avertismentul parantetic „*(arteriopatiile asimptomatice nu necesită evaluare imagistică!)*"
   a fost scos din etichetă (→ „Arteriopatii periferice simptomatice") și mutat în `Comentarii`
   pe **toate cele 3 investigații** (NR 650–652), fiind o notă valabilă pentru toată situația
   (regula „informația de situație pe toate investigațiile"). Vezi CHANGELOG §4.

3. ✅ **REZOLVAT — indicația scintigrafiei osoase la ATTR aliniată la ghid.** Decizie editor:
   respectă ghidurile. **NR 589** · Indicație „Doar în cazuri particulare" → **„Indicat"**
   (scintigrafia osoasă cu trasori de fosfat e testul-cheie non-invaziv pentru ATTR —
   Perugini 2–3 + excluderea gamapatiei monoclonale = diagnostic fără biopsie; recomandare
   de Clasă I, ESC 2021 / criteriile Gillmore). **Gradul B rămâne** — nivelul de evidență
   ESC pentru acest test e B; s-a corectat puterea indicației, nu nivelul de evidență.
   Vezi CHANGELOG §4.

> Status: **toate cele 3 puncte rezolvate** (2026-07-08).

---

## 13. Cardiovascular — goluri de conținut față de ghidurile de referință (2026-07-09)

Analiză de omisiuni a capitolului 4 față de practica curentă (**ESC**, **ACR Appropriateness
Criteria**, **RCR iRefer**), în paralel cu §3 (Pediatrie) și §11 (Cancer). **Schițe — de
validat clinic de editori** înainte de inserare; gradele și indicațiile sunt propuneri.
Acoperirea existentă a fost verificată prin căutare în tot fișierul (ce e mai jos e absent
sau doar menționat în comentarii). **Notă de metodă:** verificarea live pe ghiduri a fost
limitată (WebSearch a atins limita de sesiune); recomandările vin din cunoașterea ghidurilor
și trebuie confirmate pe documentele-sursă înainte de a fixa grade/doze.

### 13.A Goluri clare în Cardiovascular (propuneri de adăugat în capitol)

- ⏳ **Durere toracică cronică / suspiciune de boală coronariană stabilă — evaluare inițială.**
  Distinctă de „Explorarea non-invazivă a ischemiei miocardice" (testare funcțională) și de
  „Boala coronariană cronică și evaluare post IMA" (boală cunoscută). Lipsește **workup-ul
  inițial la probabilitate pre-test joasă–intermediară**, unde imagistica s-a mutat spre
  **Angio-CT coronarian (Coronaro-CT)** ca primă linie:
  - Angio-CT coronarian = *Indicat, grad A* (ESC 2019/2024 sindroame coronariene cronice —
    Clasă I; NICE CG95 — CTCA primă linie; ACR AC).
  - Scor de calciu coronarian (CT) = *Indicat, grad B* — stratificare de risc la selectați.
  - Teste funcționale de stress (eco / IRM / SPECT) = *Indicat, grad A* la probabilitate
    intermediară–înaltă (parțial acoperite de „Explorarea non-invazivă" — de corelat/uniformizat).
  - Coronarografia invazivă e deja la RI.
- ⏳ **Endocardită infecțioasă.** **Absentă complet** (0 apariții în tot ghidul). Indicație
  imagistică majoră:
  - Ecocardiografie transtoracică (ETT) = *Indicat, grad A* — primă intenție.
  - Ecocardiografie transesofagiană (ETE) = *Indicat, grad A* — sensibilitate superioară,
    valve protetice, complicații (abces, vegetații mici).
  - 18F-FDG PET/CT = *Indicat / Doar în cazuri particulare, grad B* — endocardită pe valvă
    protetică / dispozitive intracardiace (criteriu major ESC 2023), embolii oculte.
  - CT cardiac = *Indicat, grad B* — abcese/pseudoanevrisme, dehiscență protetică, planificare
    chirurgicală; angio-CT pentru embolii sistemice. (SPECT cu leucocite marcate = alternativă.)
- ⏳ **Fibrilație atrială — evaluare pre-procedurală / sursă cardioembolică.** **Absentă** (doar
  o mențiune în comentariul NR 622). 
  - ETE = *Indicat, grad A* — excluderea trombului din auriculul stâng înainte de
    cardioversie/ablație; bilanț de sursă embolică după AVC.
  - CT cardiac (atriu stâng + vene pulmonare) = *Indicat, grad B* — cartografiere pre-ablație /
    pre-închidere de auricul stâng (LAA).
- ⏳ **(prioritate medie) Sarcoidoză cardiacă.** IRM cardiac + FDG-PET (protocol dedicat cu
  pregătire dietetică). Poate sta și ca sub-caz la „Suspiciune de cardiomiopatie sau miocardită".

### 13.B Goluri în alte capitole, privind Cardiovascular / decizie de încadrare

- ✅ **Stenoză de arteră renală / HTA renovasculară** — REZOLVAT (review Aparat uro-genital,
  2026-07-09): acoperire confirmată la situația „Hipertensiune arterială (la adult tânăr sau
  unde pacientul nu răspunde la tratamentul medical)" (Eco-Doppler, Scintigrafie renală,
  AngioRM, AngioCT). Fără gol de conținut.
- ⏳ **Boală carotidiană / stenoză carotidiană (AVC/AIT)** — deja parțial în **Cap** (NR 969, AVC
  tranzitor) și Traumatisme; de verificat completitudinea la parsarea capitolului Cap, nu se
  adaugă la Cardiovascular.
- ⏳ **Ischemie mezenterică (diagnostic)** — home **Aparat digestiv** (forma cronică e deja la
  RI, NR 1293); de verificat.
- ⏳ **Cardio-oncologie / cardiotoxicitate** (monitorizarea FEVS sub terapie oncologică: eco cu
  strain/GLS, IRM cardiac, ventriculografie izotopică) — **absentă complet** (ESC 2022
  cardio-oncologie). **Decizie de home:** Cancer vs Cardiovascular.
- ⏳ **Vasculite de vase mari** (arterită Takayasu, arterită cu celule gigante) — eco („halo sign"),
  angio-IRM/CT de aortă, FDG-PET (recomandările EULAR). Sistemic apare doar pulmonar în **Torace**
  (NR 692–694); afectarea aortică/vase mari nu e acoperită vascular. Decizie de home.
- ⏳ **Urmărire post-EVAR/TEVAR aortic (endoleak)** — CT de supraveghere a protezelor aortice.
  Absentă. Home: Cardiovascular (diagnostic) vs RI (urmărire de procedură).

### 13.C Parțial acoperite — de îmbogățit (nu neapărat situație nouă)

- ⏳ **Evaluare structurală pre-TAVI/TAVR** — există doar în comentarii (NR 593, 633), nu ca
  situație dedicată. De decis dacă merită rând propriu (angio-CT „de la aortă la femurale").

### 13.D Rânduri-schiță pentru inserare (draft insertion-ready, de validat de editori)

Coloane fixe: `Capitol = Aparat cardiovascular`, `Terapeutic = Nu`; `NR.CRT` = ID nou la inserare.
`Alte informații` = referința de sub fiecare situație. **Referințe confirmate real (2026-07-10):**
ESC 2024 *Chronic Coronary Syndromes* (CCTA primă linie la probabilitate 5–50%, Clasă I); ESC 2023
*Management of Endocarditis* (rol FDG-PET/CT pe valvă protetică/dispozitive); ESC 2024 *Atrial
Fibrillation*; HRS 2014 *Expert Consensus – Cardiac Sarcoidosis*; NICE CG95. Gradele/dozele orientative.

#### (1) `Cord` — **Durere toracică cronică / suspiciune de boală coronariană stabilă – evaluare inițială**
`Alte informații =` „Cf. ESC 2024 Chronic Coronary Syndromes; NICE CG95; ACR Appropriateness Criteria."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | Coronaro-CT | Indicat | A | 2/3 | Primă linie la probabilitate pre-test joasă–intermediară (>5–50%): exclude/confirmă boala coronariană obstructivă și estimează riscul de evenimente (ESC 2024, Clasă I; NICE CG95). |
| T | Scor de calciu coronarian (CT) | Indicat | B | 1/1 | Stratificare de risc la pacienți selectați; NU înlocuiește coronaro-CT pentru boala obstructivă. |

> Testele funcționale de stress (ecografie / IRM / SPECT de perfuzie) sunt **deja parțial acoperite**
> de situația „Explorarea non-invazivă a ischemiei miocardice" → **uniformizare**, nu rânduri noi.
> De corelat cele două situații la decizia editorilor.

#### (2) `Cord` — **Endocardită infecțioasă**
`Alte informații =` „Cf. ESC 2023 Guidelines – Management of Endocarditis."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| E | Ecocardiografie transtoracică (ETT) | Indicat | A | 0/0 | Primă intenție la suspiciune de endocardită: vegetații, regurgitări, abcese. |
| E | Ecocardiografie transesofagiană (ETE) | Indicat | A | 0/0 | Sensibilitate superioară; indicată la ETT neconcludentă, valve protetice, dispozitive intracardiace, suspiciune de complicații (abces, vegetații mici). |
| N | PET-CT cu 18F-FDG | Doar în cazuri particulare | B | 4/4 | Criteriu major ESC 2023 pentru endocardita pe **valvă protetică / dispozitive intracardiace**; detecția emboliilor oculte și a focarelor extracardiace. Fals-negativ posibil în primele ~3 luni postoperator. |
| T | CT cardiac (angio-CT) | Indicat | B | 2/3 | Abcese/pseudoanevrisme, dehiscență protetică, planificare chirurgicală; angio-CT pentru emboliile sistemice. |

#### (3) `Cord` — **Fibrilație atrială – evaluare pre-procedurală / sursă cardioembolică**
`Alte informații =` „Cf. ESC 2024 Guidelines – Atrial Fibrillation."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| E | Ecocardiografie transesofagiană (ETE) | Indicat | A | 0/0 | Excluderea trombului din auriculul stâng înainte de cardioversie/ablație; bilanț de sursă embolică după AVC. |
| T | CT cardiac (atriu stâng + vene pulmonare) | Indicat | B | 2/3 | Cartografiere pre-ablație / pre-închidere de auricul stâng (LAA); anatomia venelor pulmonare. |

#### (4) `Cord` — **Sarcoidoză cardiacă** (prioritate medie)
`Alte informații =` „Cf. HRS 2014 Expert Consensus – Cardiac Sarcoidosis."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| M | IRM cardiac cu substanță de contrast | Indicat | B | 0/0 | Edem/inflamație (T2, mapare) și fibroză (captare tardivă de gadolinium, tipic mediomiocardică/subepicardică). |
| N | PET-CT cu 18F-FDG (protocol dedicat) | Indicat | B | 4/4 | Inflamație activă; necesită pregătire dietetică (supresia captării miocardice fiziologice). Util și pentru monitorizarea răspunsului la tratament. |

> Poate fi încadrată și ca sub-caz la „Suspiciune de cardiomiopatie sau miocardită" (decizie de încadrare).

#### (5) `Cord` — **Evaluare structurală pre-TAVI/TAVR** (din §13.C)
`Alte informații =` „Cf. ESC/EACTS – Valvular Heart Disease; ACR Appropriateness Criteria."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | Angio-CT „de la aortă la arterele femurale" | Indicat | B | 2/3 | Măsurarea inelului aortic (annulus sizing), anatomia rădăcinii aortice și a coronarelor, evaluarea căilor de acces ilio-femural. Standard pre-TAVI. |

> **§13.B rămâne NON-insertion-ready** — fiecare punct (boală carotidiană, ischemie mezenterică,
> cardio-oncologie, vasculite de vase mari, urmărire post-EVAR) e blocat pe o **decizie de home**
> cross-capitol; nu se poate drafta un rând complet până nu se fixează capitolul-gazdă. Nedraftat intenționat.

> Status: **niciun rând nou inserat** în `GHID.csv`. Se așteaptă decizia editorilor; apoi
> se adaugă cu grade/doze validate pe sursă citabilă (ESC/ACR/RCR) și se consemnează în CHANGELOG.

---

## 14. Traumatisme (adult) — omisiuni de subcapitol / situație (de adăugat) (2026-07-09)

Comparație cu ghidurile majore (ACR Appropriateness Criteria, RCR iRefer, NICE, ATLS / EAST /
WSES). **Schițe orientative — de validat clinic**; niciun rând inserat în `GHID.csv`.
Gradele/indicațiile sunt propuneri.

### 14.1 „Gât" — regiune întreagă lipsă (MAJOR) 🔴
Nu există subcapitol de traumă cervicală de părți moi (CLAUDE.md o anticipează deja — `[gât]`
în lista de regiuni). Trauma **vasculară** cervicală e parțial acoperită de „Sistem vascular ›
Leziune cerebrovasculară posttraumatică", dar restul gâtului nu. De adăugat un subcapitol
**Gât**:
- **Traumatism cervical penetrant** (plagă înjunghiată / împușcată; zonele I/II/III) →
  Angio-CT cervico-toracic = *Indicat* (screening vascular + aerodigestiv, ACR AC –
  *Penetrating Neck Injury*).
- **Leziune laringo-traheală** (traumatism cervical închis) → CT = *Indicat*.
- **Leziune faringo-esofagiană** → CT + esofagografie cu contrast hidrosolubil.

### 14.2 Traumatism penetrant — subreprezentat 🔴
Capitolul e orientat aproape exclusiv pe traumă închisă (blunt). De adăugat:
- **Traumatism abdominal penetrant** (armă albă / armă de foc) → CT cu contrast = *Indicat*
  (ACR AC – *Penetrating Abdominal/Flank Trauma*) — distinct de „Traumatism abdominal major".

### 14.3 Torace — situații lipsă
- **Leziune diafragmatică traumatică** → CT cu reconstrucții coronale/sagitale = *Indicat*
  (entitate frecvent ratată).
- **Fractură de stern** → radiografie de profil / CT = *Indicat*; asociere cu contuzia cardiacă.

### 14.4 Membre — situație generică
- **„Traumatism de membru — suspiciune de fractură" (adult)**, ca la pediatrie: acoperă
  claviculă / mână-degete / femur diafizar / gambă, neacoperite ca situații individuale.

### 14.5 Minore
- **Traumatism cranian la vârstnic / anticoagulat** — prag mai jos de CT; mai degrabă o notă
  în situația „Traumatism cranio-cerebral" existentă, nu un subcapitol nou.

### 14.6 Rânduri-schiță pentru inserare (draft insertion-ready, de validat de editori)

Coloane fixe: `Capitol = Traumatisme`, `Terapeutic = Nu`; `NR.CRT` = ID nou la inserare.
`Alte informații` = referința de sub fiecare situație. **Referințe confirmate real (2026-07-10):**
ACR AC *Penetrating Neck Injury* (2017), *Penetrating Torso Trauma* (2024, acoperă abdomenul
și leziunea diafragmatică). Gradele orientative (capitolul folosește mult „Indicat" fără grad
explicit — propus grad B unde ghidul dă recomandare fermă). Ordinea examenelor = prima intenție în jos.

> ⚠️ **Încadrare (14.1):** rândurile (1a–1c) presupun crearea unui **subcapitol nou `Gât`** în
> Traumatisme (anticipat de `CLAUDE.md`, `[gât]` în lista de regiuni). Decizia de a crea subcapitolul
> precede inserarea.

#### (1a) `Gât` — **Traumatism cervical penetrant (plagă înjunghiată / împușcată; zonele I/II/III)**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Penetrating Neck Injury."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | Angio-CT cervico-toracic | Indicat | B | 2/3 | Screening vascular + aerodigestiv la pacientul fără indicație chirurgicală imediată (semne „soft" sau „hard" fără instabilitate): evaluează vasele, laringo-traheea și faringo-esofagul într-o singură achiziție. |

#### (1b) `Gât` — **Leziune laringo-traheală (traumatism cervical închis)**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Penetrating Neck Injury (leziuni aerodigestive)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | CT cervical (cu reconstrucții) | Indicat | B | 2/3 | Fracturi de cartilaj laringian, emfizem, leziuni traheale; completează endoscopia. |

#### (1c) `Gât` — **Leziune faringo-esofagiană**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Penetrating Neck Injury (leziuni aerodigestive)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | CT cervico-toracic cu substanță de contrast | Indicat | B | 2/3 | Emfizem cervical/mediastinal, colecții periesofagiene; suspiciune de perforație. |
| X | Esofagografie cu contrast hidrosolubil | Indicat | B | 2/2 | Confirmă extravazarea; **contrast hidrosolubil, nu bariu** (risc de mediastinită chimică la perforație). |

#### (2) `Abdomen` — **Traumatism abdominal penetrant (armă albă / armă de foc)**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Penetrating Torso Trauma (2024)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | CT abdomino-pelvin cu substanță de contrast | Indicat | B | 2/3 | Pacient stabil hemodinamic: violare peritoneală, leziuni de organ, traiectul plăgii. **Distinct de „Traumatism abdominal major"** (mecanism contuziv). La pacientul instabil, FAST triază spre laparotomie. |

#### (3a) `Torace` — **Leziune diafragmatică traumatică**
`Alte informații =` „Cf. ACR Appropriateness Criteria – Penetrating Torso Trauma (2024)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| T | CT torace cu reconstrucții coronale/sagitale | Indicat | B | 2/3 | Entitate frecvent ratată: hernierea viscerelor abdominale, „collar sign", discontinuitatea diafragmatică. Reconstrucțiile multiplanare sunt esențiale. |

#### (3b) `Torace` — **Fractură de stern**
`Alte informații =` „Cf. RCR iRefer; ACR Appropriateness Criteria (trauma toracică)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| G | Radiografie de stern (incidență de profil) | Indicat | B | 1/2 | Primă intenție; incidență laterală/oblică. |
| T | CT torace | Doar în cazuri particulare | B | 2/3 | Fracturi complexe sau suspiciune de contuzie cardiacă / leziuni mediastinale asociate. |

#### (4) `Membru superior` **și** `Membru inferior` — **Traumatism de membru – suspiciune de fractură (adult)**
`Alte informații =` „Cf. RCR iRefer; ACR Appropriateness Criteria (trauma de extremitate)."
| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentarii |
|---|---|---|---|---|---|
| G | Radiografie standard (min. 2 incidențe ortogonale) | Indicat | B | 1/1 | Primă intenție la suspiciune de fractură (claviculă, mână/degete, femur diafizar, gambă etc.). |
| T | CT | Doar în cazuri particulare | B | 2/3 | Fracturi complexe/intraarticulare, planificare chirurgicală, radiografie neconcludentă cu suspiciune persistentă. |
| M | IRM | Doar în cazuri particulare | B | 0/0 | Fracturi oculte (ex. scafoid) și leziuni de părți moi/ligamentare asociate. |

> **Încadrare (14.4):** setul de fațete Traumatisme e **regional**, fără bucket generic „Membre" →
> situația de mai sus se inserează **identic în ambele** subcapitole (`Membru superior`, `Membru
> inferior`), sau se lasă ca situație generică — decizie de încadrare pentru editori.

> **14.5 nu produce rând nou** — traumatismul cranian la vârstnic/anticoagulat = **completare de
> comentariu** pe situația existentă „Traumatism cranio-cerebral" (prag mai jos de CT la
> anticoagulați/vârstnici), nu subcapitol/situație nouă.

> Status: **inventariat, neatins.** De validat/adăugat de editori. Nu confunda cu §10
> (trauma care EXISTĂ deja în alte capitole și se aduce în Traumatisme — vezi CHANGELOG).

---

## 15. Sân — goluri de conținut față de ghidurile de referință (2026-07-09)

Analiză de omisiuni a capitolului 9 față de practica curentă (**ACR Appropriateness
Criteria**, **NCCN Breast Cancer Screening and Diagnosis**), în paralel cu §3 (Pediatrie),
§11 (Cancer) și §13 (Cardiovascular). **Schițe — de validat clinic de editori** înainte de
inserare; gradele sunt orientative. **Notă de metodă:** temele de mai jos au fost verificate
live prin căutare (titluri exacte de ghiduri ACR AC confirmate, cu link); conținutul detaliat
al fiecărei teme (grade complete pe toate variantele clinice) nu a fost extras integral —
de confirmat pe documentul-sursă înainte de a fixa gradele definitive.

### 15.A Goluri clare cu home = Sân (propuneri de adăugat în capitol)

- ⏳ **Evaluarea răspunsului la chimioterapia neoadjuvantă.** **Absentă complet** din
  „Cancer de sân" (care are doar stadializare inițială + urmărire post-tratament, nimic
  intra-tratament). Temă ACR AC proprie: *„Monitoring Response to Neoadjuvant Systemic
  Therapy for Breast Cancer"* (2017, actualizat 2022). Propunere — situație nouă
  „Evaluarea răspunsului la chimioterapia neoadjuvantă":
  - IRM mamar = *Indicat, grad A* — metoda cea mai performantă pentru evaluarea
    răspunsului și planificarea chirurgicală (sensibilitate ~87% pentru răspuns complet).
  - Ecografie = *Doar în cazuri particulare, grad B* — evaluare interimară, mai accesibilă.
  - Mamografie/tomosinteză = *Doar în cazuri particulare, grad B* — utilitate limitată de
    modificările induse de tratament.
- ⏳ **Patologia mamară simptomatică la bărbat.** **Absentă complet.** Temă ACR AC proprie:
  *„Evaluation of the Symptomatic Male Breast"* (2018), cu recomandări stratificate pe
  vârstă și context clinic. Propunere — situație nouă în „Paciente cu simptome…" (sau
  subcapitol propriu „Patologie mamară la bărbat"):
  - Ginecomastie/pseudoginecomastie cu aspect clinic tipic = *Neindicat* — fără imagistică
    de rutină.
  - Masă nedeterminată, bărbat sub 25 ani = Ecografie, *Indicat, grad B* — primă intenție.
  - Masă nedeterminată, bărbat peste 25 ani = Mamografie, *Indicat, grad B*.
  - Suspiciune clinică de cancer, indiferent de vârstă = Mamografie, *Indicat, grad A*.
- ⏳ **Imagistica sânului în sarcină și lactație.** **Absentă complet.** Temă ACR AC proprie:
  *„Breast Imaging of Pregnant and Lactating Females"*. Propunere — situație nouă:
  - Ecografie = *Indicat, grad A* — primă linie, fără iradiere/contrast.
  - Mamografie cu protecție abdominală = *Doar în cazuri particulare, grad B* — dacă
    ecografia e neconcludentă sau leziune suspectă.
  - IRM cu contrast = *Neindicat* în sarcină (gadoliniu traversează placenta);
    *Doar în cazuri particulare* în lactație (alăptarea poate continua, excreție minimă
    în lapte).
- ⏳ **Algoritmul de urmărire BI-RADS 3 („probabil benign").** Piatră de temelie a practicii
  (NCCN), absentă ca traseu explicit — BI-RADS apare o singură dată, în comentariul NR 990.
  Propunere — situație nouă „Leziune probabil benignă (BI-RADS 3) — urmărire":
  - Mamografie și/sau Ecografie (metoda care a detectat leziunea) = *Indicat, grad B* —
    control la 6 luni, apoi la 12 și 24 luni dacă rămâne stabilă.
- ⏳ **Screening suplimentar pe bază de densitate mamară.** Temă ACR AC proprie, actualizată
  2024/2025 (subiect activ legislativ — notificarea densității). La noi apare doar punctual,
  în comentariile altor situații („adjuvant... în cazul unui sân dens"), nu ca prag/situație
  proprie. Propunere — situație nouă „Screening suplimentar la sân dens (categorie
  BI-RADS C/D)":
  - Ecografie = *Doar în cazuri particulare, grad B* — adjuvant la mamografie normală.
  - IRM = *Doar cu aviz specializat, grad B* — la risc suplimentar asociat densității.

### 15.B Goluri cu home probabil în alt capitol (nu se adaugă în Sân)

- ⏳ **Localizarea preoperatorie ghidată imagistic a leziunilor nepalpabile** (harpon,
  sămânță radioactivă/magnetică) — procedură (Tip I), home = **RI › Oncologie**, nu Sân.
  Nu apare nicăieri în tot ghidul (verificat) — de confirmat dacă lipsește real din RI sau
  e considerată implicită în alt rând.
- ⏳ **Drenajul percutan al abcesului mamar** — menționat doar în comentariul „Inflamație
  mamară" (NR 976, „drenajul ghidat percutan"), fără rând propriu de procedură. Tip I,
  home = **RI › Oncologie**. De verificat dacă există deja acolo.

### 15.C Parțial acoperite — de îmbogățit (nu neapărat situație nouă)

- ⏳ **Tomosinteza (mamografia 3D)** — nu apare deloc ca modalitate distinctă (Tip `G` acoperă
  generic „Mamografie"). Ghidurile 2025 (ACR) o recomandă alături de mamografia 2D pentru
  toate categoriile de risc la screening. De decis dacă merită distincție de Tip/Examen sau
  rămâne implicită în „Mamografie".

> Status: **niciun rând nou inserat** în `GHID.csv`. Se așteaptă decizia editorilor; apoi
> se adaugă cu grade/doze validate pe sursă citabilă (ACR AC/NCCN) și se consemnează în
> CHANGELOG.

---

## 16. Cancer — goluri de conținut, subcapitol cu subcapitol (2026-07-09)

Trecere a doua, mai profundă, prin cele **29 de subcapitole** ale capitolului Cancer
(dincolo de golurile de fază „Monitorizare" deja inventariate în §11), în paralel cu §13
(Cardiovascular) și §15 (Sân). Surse: **NCCN Guidelines**, **ESMO Clinical Practice
Guidelines**, **ACR Appropriateness Criteria**, ghiduri de societate (Fleischner, IMWG,
EAU/EANM/SNMMI). **Schițe — de validat clinic de editori**; gradele sunt orientative.
Temele marcate „✓ verificat live" au fost confirmate prin căutare directă; restul vin din
cunoașterea ghidurilor și trebuie reconfirmate pe sursă înainte de a fixa grade/doze.
Subcapitolele cu acoperire bună sunt listate scurt, fără propunere.

### ✅ 16.1 Adenopatii cervicale — acoperire bună
Workup-ul pentru „unknown primary" e complet (IRM, CT, PET-CT). Fără propuneri.

### ✅ 16.2 Cancer anal — acoperire bună
Diagnostic/Stadializare/Monitorizare complete și coerente cu ghidurile.

### ✅ 16.3 Cancer bronho-pulmonar — acoperire bună (2 goluri redirecționate la Torace)
La analiza inițială semnalasem aici screeningul LDCT și urmărirea nodulului pulmonar
incidental. **Corectat**: ambele au home confirmat de editor în **Torace**, nu Cancer —
vezi §17 („Nodul pulmonar solitar" rămâne diagnostic în Torace: „nodul indeterminat ≠
malignitate confirmată") și §18/„14.1" (screening LDCT + masă mediastinală, încadrare
Torace explicit confirmată). Eliminate de aici pentru a nu duplica/contrazice deciziile
deja luate. Restul subcapitolului (Diagnostic la suspiciune clinică, Stadializare,
Monitorizare) are acoperire bună.

### 16.4 Cancer de col uterin — 1 gol ✓ verificat live
- ⏳ **PET-CT absent din Stadializare** (are doar IRM + CT). NCCN recomandă explicit PET-CT
  pentru evaluarea ganglionilor para-aortici din stadiul IB1 în sus, mai ales pentru
  planificarea câmpului de radioterapie în boala local-avansată (IB2–IVA). Propunere:
  - PET-CT (F18-FDG) = *Indicat, grad B* — stadiul IB2 și mai avansat, evaluare
    ganglionară para-aortică / planificare radioterapie. (Notă: sensibilitate limitată
    pentru metastaze ganglionare <5 mm — fals-negativ posibil, nu exclude stadializarea
    chirurgicală la caz selectat.)

### ✅ 16.5 Cancer de colon — acoperire bună

### ✅ 16.6 Cancer de corp uterin — acoperire relativ bună
Fără goluri majore de modalitate imagistică identificate.

### ✅ 16.7 Cancer de rect — acoperire bună

### ✅ 16.8 Cancer esofagian — acoperire relativ bună
Diagnosticul endoscopic e corect reflectat (imagistica doar completare).

### ✅ 16.9 Cancer gastric — acoperire relativ bună

### ✅ 16.10 Cancer laringian și al hipofaringelui — acoperire bună

### ✅ 16.11 Cancer ovarian — acoperire bună

### ✅ 16.12 Cancer pancreatic — acoperire bună (deja completat la consolidare)

### ✅ 16.13 Tumori neuroendocrine gastro-entero-pancreatice (GEP-NET) — acoperire bună
(subcapitol nou, construit la consolidare)

### 16.14 Cancer prostatic — 2 goluri majore ✓ verificat live
- ⏳ **IRM multiparametrică (mpMRI) încadrată greșit ca linia a doua.** În ghid, IRM apare
  doar „Doar în cazuri particulare — suspiciune clinică + biopsie ecoghidată negativă"
  (adică *după* o biopsie negativă). Practica actuală (NCCN, EAU) recomandă **mpMRI
  ÎNAINTE de biopsie**, ca instrument de selecție a candidaților și de ghidare a biopsiei
  țintite (protocol PI-RADS). **Nu modific gradul/încadrarea singur** (regulă CLAUDE.md) —
  semnalez pentru decizia editorilor: posibilă reformulare a situației „Diagnostic" pentru
  a reflecta mpMRI pre-biopsie ca prim pas, nu doar ca recurs post-biopsie negativă.
- ⏳ **PSMA PET-CT absent complet.** A devenit modalitate de stadializare standard pentru risc
  intermediar-înalt (superioară CT+scintigrafie osoasă convențională pentru detecția
  metastazelor ganglionare/osoase oculte) și pentru recidiva biochimică — susținută
  convergent de EAU, ESMO, NCCN (ghid comun EANM/SNMMI 2.0). Propunere — rând nou în
  Stadializare:
  - PSMA PET-CT = *Indicat / Doar cu aviz specializat, grad B* — risc intermediar-înalt la
    diagnostic (stadializare ganglionară/osoasă) sau recidivă biochimică post-tratament.

### ✅ 16.15 Cancer testicular — acoperire bună

### ✅ 16.16 Cancer tiroidian — acoperire relativ bună

### ✅ 16.17 Cancer vezical — acoperire relativ bună

### ✅ 16.18 Cancerul de căi aero-digestive superioare — acoperire bună

### ✅ 16.19 Cancerul nazofaringian — acoperire bună

### ✅ 16.20 Cancerul parotidian — acoperire bună

### 16.21 Cancerul renal — acoperire bună, dar fază „Diagnostic" aproape duplicat cross-capitol
⏳ **Găsit la reviewul Aparat uro-genital (2026-07-09):** faza „Diagnostic" (NR 495–498:
Ecografie/CT/UIV/IRM) e aproape identică cu `Aparat uro-genital › Masă renală` (Ecografie/
CT/IRM/PET-CT/UIV) — aceleași examene, grade apropiate, comentarii parafrazate din aceeași
sursă. Analog precedentului „Nodul pulmonar solitar" (Torace, §17): caracterizarea unei mase
renale **indeterminate** (chist/oncocitom/AML/RCC) ar trebui să stea în capitolul anatomic
(regula 5), iar Cancer să rețină doar Stadializare (502–504) + Monitorizare (499–501), care
presupun deja malignitate stabilită. **Recomandare: eliminarea fazei „Diagnostic" din
`Cancer › Cancerul renal`** — dar **neaplicat la cererea explicită a utilizatorului**
(„nu modificăm capitolul de cancer" acum). De reconciliat separat, la parsarea capitolului
Cancer sau când se decide explicit.

### ✅ 16.22 Ficat, colecist și pancreas — acoperire bună (scop îngust, intenționat)

### 16.23 Limfom — 1 gol major de capitol (nu doar subcapitol) ✓ verificat live
- ⏳ **Mielomul multiplu lipsește complet din tot ghidul** — nicio mențiune, în niciun
  capitol. E o malignitate hematologică distinctă de limfom, cu workup imagistic propriu
  și foarte specific (**IMWG Bone Working Group**): CT whole-body low-dose ca primă linie
  pentru boala osoasă (mai sensibil decât radiografia convențională), IRM pentru cazurile
  fără alte „myeloma-defining events" pe CT, PET-CT FDG ca standard pentru evaluare
  funcțională/răspuns la tratament. Propunere: **subcapitol nou „Mielom multiplu"** în
  Cancer (analog GEP-NET ca precedent de subcapitol nou creat la nevoie), cu situații
  Diagnostic + Monitorizare:
  - CT whole-body low-dose = *Indicat, grad A* — primă linie pentru boala osoasă litică.
  - IRM (coloană/whole-body) = *Indicat, grad B* — la CT neconcludent sau fără leziuni
    definitorii; superior pentru afectarea medulară difuză.
  - PET-CT (F18-FDG) = *Indicat, grad B* — evaluare funcțională, răspuns la tratament,
    boală extramedulară.

### ✅ 16.24 Melanom malign — acoperire bună
(absența situației „Diagnostic" e intenționată — diagnostic prin biopsie excizională,
menționat explicit în comentariul de la Stadializare, consecvent cu restul ghidului).

### ✅ 16.25 Metastaze cu tumoră primară necunoscută — acoperire bună

### 16.26 Tumori ale aparatului locomotor — 1 gol (completare la §11)
Lipsește complet faza de **Monitorizare** (urmărire post-tratament pentru recidivă locală
sau metastaze la distanță după rezecția unui sarcom osos/de părți moi) — subcapitolul are
doar „bilanț diagnostic" și „bilanț de extensie". Nu a fost inclus în lista din §11 (care
viza doar subcapitolele cu axa Diagnostic/Stadializare/Monitorizare standard). Propunere:
- CT toracic = *Indicat, grad B* — supraveghere metastaze pulmonare (sarcoame osoase).
- IRM loco-regională = *Indicat, grad B* — supraveghere recidivă locală.
- Radiografie standard = *Doar în cazuri particulare, grad C* — supraveghere de rutină,
  acces limitat.

### ✅ 16.27 Tumori cerebrale și medulare — acoperire bună

### ✅ 16.28 Tumori maligne primare hepatice — gol Monitorizare (deja în §11)

### ✅ 16.29 Tumori maligne secundare hepatice — gol Stadializare + Monitorizare
Deja notat în §11; posibil intenționat — scop îngust pe detecție/caracterizare.

### 16.30 Goluri la nivel de capitol (cancere absente complet din grupul ginecologic)
- ⏳ **Cancer de vulvă / cancer vaginal** — absente din grupul ginecologic (există doar col
  uterin, corp uterin, ovarian). Prevalență mai mică, dar workup imagistic distinct
  (IRM pelvină pentru stadializare loco-regională, similar cu col uterin). De evaluat
  prioritatea de adăugare.
- ⏳ **Cancer de penis** — absent, prevalență redusă; menționat doar ca prioritate scăzută.

> Status: **niciun rând nou inserat** în `GHID.csv`. Se așteaptă decizia editorilor; apoi
> se adaugă cu grade/doze validate pe sursă citabilă (NCCN/ESMO/ACR AC/IMWG/EAU) și se
> consemnează în CHANGELOG. Golul cu impact clinic cel mai mare rămas **la Cancer** (după
> redirecționarea screeningului LDCT / nodulului pulmonar la Torace, §17–18): **mielomul
> multiplu absent complet din tot ghidul** (§16.23) — temă majoră, frecventă, fără
> subcapitol propriu nicăieri.

---

## 17. Torace — chestiuni de încadrare rămase după review (2026-07-08)

Ridicate la reviewul capitolului 5 (vezi CHANGELOG §5). Corecturile mecanice (ortografie,
diacritice, normalizare, spații) au fost aplicate; cele două chestiuni de **încadrare pe
ierarhia de capitole** (flagate inițial pentru a nu fi decise unilateral, regula de aur 6)
au fost între timp **tranșate de editor** — status mai jos:

1. ✅ **REZOLVAT — „Neoplasm bronhopulmonar" (NR 695–705) mutat la Cancer › Cancer
   bronho-pulmonar și fuzionat (⛔ BREAKING).** Decizie editor: se mută la Cancer și se
   fuzionează. Cele 11 rânduri Torace s-au eliminat; reconciliere fază-cu-fază (Torace
   „diagnostic – suspiciune clinică"=Diagnostic; „bilanț preterapeutic"+„stadializare"=
   Stadializare; „supraveghere"=Monitorizare). Vezi CHANGELOG §3 pentru detaliul complet.
   - **Excepție confirmată:** *Nodul pulmonar solitar* (NR 706–708) rămâne **diagnostic în
     Torace** — nodul indeterminat ≠ malignitate confirmată.
   - **✅ CONFLICTE DE GRAD — tranșate „gradul din Cancer prevalează" (niciun grad Cancer
     modificat), confirmat de editor și susținut de ghiduri (iRefer/NICE NG122/ACR AC 2019):**
     pentru aceeași investigație în aceeași fază, rândul-sursă din Torace avea alt grad decât
     cel din Cancer. S-a păstrat rândul Cancer și s-a renunțat la duplicatul Torace:
     | Fază | Investigație | Grad Cancer (păstrat) | Grad Torace (renunțat) | Susținere ghid |
     |---|---|---|---|---|
     | Diagnostic | Radiografie toracică | **A** (NR 334) | C (fost 699) | primă linie la suspiciune (NICE NG12/NG122) |
     | Stadializare | IRM cerebral | **A** (NR 339) | C (fost 695) | IRM > CT pt. metastaze cerebrale (NICE NG122) |
     | Stadializare | CT cerebral/torace/abdomen | **A** (NR 340) | C (fost 697) | CT de stadializare standard (NICE NG122) |
     | Stadializare | IRM toracal/mediastinal | **C** (NR 341) | B (fost 698) | instrument select/problem-solving (ACR AC 2019) — **editor: C** |

     Referințele scurte au fost consemnate în col. 10 „Alte informații" pe rândurile
     respective. Restul duplicatelor (PET-CT ×3, Scintigrafie) aveau grade identice → fără conflict.

   - ✅ **REZOLVAT — Scintigrafie osoasă (NR 338): indicație coborâtă la „Doar în cazuri
     particulare" (grad B neschimbat).** Decizie editor. Ghidurile actuale (NICE NG122,
     ACR AC 2019, ESMO) arată că **FDG PET-CT a înlocuit în mare scintigrafia osoasă** în
     stadializarea de rutină (PET-CT sensibilitate ~94% vs ~78% pentru metastaze osoase,
     imagând tumora, nu reacția osoasă). PET-CT stadializare **există deja** (NR 337,
     „Indicat" A) și acoperă rolul de metastaze osoase/la distanță. Aplicat: indicația NR 338
     „Indicat" → **„Doar în cazuri particulare"**; comentariul completat cu „…mai ales atunci
     când PET-CT nu este disponibil"; **gradul B rămâne**. Referință în col. 10. Vezi CHANGELOG §3.

2. ✅ **REZOLVAT — „Nodul pulmonar" unificat la „Nodul pulmonar solitar".**
   Decizie editor: unificăm eticheta. Rândul PET-CT („nodul solid > 8 mm", azi **NR 698**)
   purta eticheta scurtată „Nodul pulmonar"; rândul CT torace (azi **NR 697**) folosea „Nodul
   pulmonar solitar" — aceeași situație în subcapitolul Pulmon. Eticheta a fost unificată la
   „Nodul pulmonar solitar"; cele două examene stau acum sub o singură situație. **Reordonat**
   CT torace (697, primă intenție, Indicat B) înaintea PET-CT (698, „Doar în cazuri
   particulare"). „Nodul pulmonar solitar urmărire" (azi **NR 699**) rămâne situație distinctă.
   Vezi CHANGELOG §5. _(NR post-renumerotare 2026-07-09.)_

> Status: **toate punctele rezolvate** (2026-07-08). Conflictele de grad — tranșate; discrepanța
> scintigrafiei osoase NR 338 — aplicată (indicație coborâtă, grad B neschimbat).

---

## 18. Torace — omisiuni de patologie (propuneri de adăugat)

Din analiza capitolului Torace (NR 664–727) față de tabelele de indicații toracice din
**ACR Appropriateness Criteria, NICE și RCR iRefer**. Patologii frecvente aparent neacoperite
sau doar parțial acoperite. **Schițe — de validat clinic de editori** înainte de inserare în
`GHID.csv`; gradele/dozele sunt orientative. Încadrare confirmată de editor: screeningul LDCT
și masa mediastinală merg în **Torace**.

### 14.1 Lacune majore (topicuri de ghid de sine stătătoare, absente)

- ⏳ **Screening cancer pulmonar — CT low-dose la persoane cu risc** (→ subcapitol **Pulmon**).
  Lipsă ca situație dedicată (apare doar în treacăt în comentariul „Nodul pulmonar solitar").
  Recomandare majoră actuală (USPSTF 2021; ACR AC *Lung Cancer Screening* 2022): LDCT anual la
  50–80 ani cu ≥20 pachete-an, fumători activi sau opriți de <15 ani. Propunere:
  - CT torace low-dose fără contrast = *Indicat, grad A* (screening la populația cu risc,
    anual; nodulii se gestionează pe protocolul din „Nodul pulmonar solitar urmărire").
  - Radiografie toracică = *Neindicat, grad A* ca test de screening (insensibilă — mesaj util).
  - Încadrare: rămâne în **Torace › Pulmon** (screeningul unui asimptomatic cu risc ≠
    malignitate cunoscută, deci nu la Cancer). Ref.: ACR AC 2022; USPSTF 2021.

- ⏳ **Masă / lărgire mediastinală** (→ subcapitol nou **Mediastin**, sau în Pulmon). Absentă.
  Topic ACR dedicat (*Imaging of Mediastinal Masses* 2021). Propunere:
  - CT torace cu substanță de contrast = *Indicat, grad B* (primă linie — localizare,
    caracterizare, raporturi vasculare).
  - IRM torace/mediastin = *Doar în cazuri particulare* (caracterizare tisulară: chistic vs
    solid, invazie; intoleranță la contrast iodat).
  - PET-CT (F18-FDG) = *Doar cu aviz specializat* (suspiciune de malignitate / limfom).
  - Radiografie toracică = *Indicat, grad C* (adesea descoperire incidentală inițială).
  - Încadrare: evaluarea unei mase incidentale/suspectate = diagnostic toracic → **Torace**;
    dacă se confirmă malignă (timom, limfom) → migrează la Cancer. Ref.: ACR AC 2021.

### 14.2 Lacune reale, dar parțial acoperite indirect

- ⏳ **Dispnee acută / insuficiență respiratorie acută** (→ Pulmon sau subcapitolul Torace
  general). Prezentare frecventă, acoperită azi doar indirect (embolie, pneumonie, pacienți
  ATI). Topic ACR (*Acute Respiratory Illness* / *Dyspnea*). Propunere:
  - Radiografie toracică = *Indicat, grad B* (primă linie).
  - CT torace ± angio-CT = *Doar în cazuri particulare* (radiografie neconcludentă,
    suspiciune de embolie/patologie parenchimatoasă).
  - Ecografie toracică (pulmonar + cardiac) = *Doar în cazuri particulare* (la patul
    bolnavului). De decis dacă nu se suprapune prea mult cu situațiile existente.

- ⏳ **Tuberculoză pulmonară activă — suspiciune / diagnostic** (→ Pulmon). Avem doar „Contacți
  de tuberculoză" (screening de contact), nu boala activă. Propunere:
  - Radiografie toracică = *Indicat, grad B* (primă linie — infiltrate, cavitații, adenopatii).
  - CT torace = *Doar în cazuri particulare* (radiografie echivocă, forme complicate/miliare,
    evaluarea activității).

### 14.3 Rafinări (mai degrabă situații distincte din situații existente)

- ⏳ **Empiem / pleurezie parapneumonică** (→ Pleură; azi parțial sub „Epanșament pleural").
  Ecografie = *Indicat, grad B* (cloazonări, ghidaj drenaj); CT torace cu contrast = *Indicat,
  grad B* (colecție organizată, „split pleura sign", ghidaj drenaj). De decis dacă merită
  situație proprie sau rămâne notă în „Epanșament pleural".

- ⏳ **Bronșiectazii** (→ Pulmon; azi parțial sub „Bronhoree cronică", care menționează deja
  „dilatații bronșice"). HRCT torace fără contrast = *Indicat, grad A* (examen de referință);
  Radiografie toracică = *Doar în cazuri particulare* (insensibilă). De decis dacă se separă
  de „Bronhoree cronică" sau rămâne acoperită acolo.

> Status: **6 propuneri deschise** (2026-07-09). Încadrare confirmată: screening LDCT + masă
> mediastinală → Torace. Gradele/încadrarea fină rămân de validat de editori înainte de inserarea
> în `GHID.csv`.

---

## 19. Aparat digestiv — chestiuni ridicate la review (2026-07-09)

Ridicate în review-ul capitolului (pașii 6–7). Modificările mecanice (ortografie,
diacritice, whitespace, unificare etichete) au fost aplicate. **§19.1–19.3 au fost
EXECUTATE** la cererea editorului (2026-07-09) — vezi `CHANGELOG.md` (cap. 6 și cap. 3).
Rămân documentate mai jos ca justificare a deciziei.

### 19.1 „Cancerul de stomac – diagnostic și bilanț de extensie" (PET-CT F18-FDG) — încadrare
Rândul (azi în `Aparat digestiv › Tub digestiv`, PET-CT F18-FDG, *Doar în cazuri
particulare, B*; comentariul vizează stadializarea/urmărirea tumorilor stromale
gastrointestinale — GIST) e **determinat de malignitate** → per ierarhia capitolelor
(regula 3) ar trebui în **Cancer › Cancer gastric**. Subcapitolul „Cancer gastric" există
deja (Diagnostic: CT, tranzit dublu contrast; Stadializare: ecoendoscopie, CT) și **nu**
are un rând de medicină nucleară — deci mutarea l-ar completa, nu ar duplica.
**✅ APLICAT (2026-07-09):** MUTAT → `Cancer › Cancer gastric › Stadializare` (⛔ BREAKING,
mutare cross-capitol; NR.CRT păstrat).

### 19.2 „Suspiciune de fistulă biliară" — cvasi-duplicat între două subcapitole
Aceeași situație clinică apare de două ori, în subcapitole diferite, cu conținut
cvasi-identic (Ecografie / CT / IRM colangio, aceleași indicații și note):
- `Ficat, colecist și pancreas` — „Suspiciune de fistulă biliară – antecedente
  chirurgicale recente" (Eco *Indicat C*, CT *Indicat C*, IRM *Doar în cazuri particulare C*).
- `Tub digestiv` — „Suspiciune de fistulă biliară – antecedente recente de chirurgie
  digestivă" (Eco *Indicat C*, CT *Indicat C*, IRM *Doar în cazuri particulare C*).
Fistula biliară e patologie hepato-biliară → aparține subcapitolului **Ficat, colecist și
pancreas**. **✅ APLICAT (2026-07-09):** COMASAT — cele 3 rânduri din `Tub digestiv`
(NR 786–788) eliminate ca duplicate; situația din `Ficat, colecist și pancreas` e păstrată
(conținut cel puțin la fel de bogat — include nota ALTE pe IRM și monitorizarea ascitei).

### 19.3 „Sângerare acută" vs. „sângerare ocultă" — scintigrafia cu hematii marcate (NR 794)
Confuzie de etichete în `Tub digestiv`:
- „Hemoragie gastro-intestinală ocultă – bilanț" (Scintigrafie cu hematii marcate,
  *Doar în cazuri particulare B*; + PET-CT neindicat; + Videocapsulă, Entero-CT, Eco, IRM).
- „Sângerare gastro-intestinală acută" (CT *Indicat B*; Eco/IRM neindicate) — hemoragie activă.
- „Suspiciunea de sângerare gastro-intestinală acută" (NR 794, Scintigrafie cu hematii
  marcate, *Indicat*, grad `?`) — dar **comentariul e identic** cu cel al scintigrafiei din
  „Hemoragie ocultă" (sângerări recurente intermitente de origine necunoscută, endoscopie
  negativă) → descrie de fapt **sângerarea ocultă/obscură**, nu una acută/manifestă.
**✅ APLICAT (2026-07-09):** COMASAT — NR 794 eliminat ca duplicat al scintigrafiei din
„Hemoragie gastro-intestinală ocultă – bilanț" (NR 754, *Doar în cazuri particulare, grad B*,
comentariu identic). Situația-fantomă „Suspiciunea de sângerare gastro-intestinală acută"
(un singur rând, etichetat greșit) dispare astfel; sângerarea acută manifestă rămâne acoperită
de situația „Sângerare gastro-intestinală acută" (CT prima intenție).

### 19.4 Informativ — situații fragmentate (fără schimbare de date)
„Hemoragie gastro-intestinală ocultă – bilanț" are rânduri non-contigue în fișier
(scintigrafie + PET-CT într-un loc; videocapsulă/entero-CT/eco/IRM în altul), dar cu
**etichetă identică** → se consolidează automat în vizualizarea HTML (gruparea e pe
Capitol → Subcapitol → Situație). Nu necesită acțiune; notat pentru claritate.

### 19.5 ✅ Încadrare confirmată — „durere toracică" / reflux-hernie hiatală **rămâne în Aparat digestiv**
Întrebare ridicată la rafinarea titlurilor: rândul (tranzit baritat pentru reflux / hernie
hiatală), fost intitulat „Durerea toracică – suspiciunea de hernie hiatală sau de reflux",
ar trebui mutat la **Torace**? **Decizie: NU.** Motivare (ierarhia capitolelor — home după
**entitate**, nu după simptomul de prezentare):
- **Entitatea** e esofagiană/eso-gastrică (BRGE, hernie hiatală) → esofagul e organ digestiv;
  restul patologiei esofagiene stă deja în Aparat digestiv (disfagie, perforație esofagiană,
  fistulă esofagiană/anastomotică). Mutarea la Torace ar **fragmenta** patologia esofagiană.
- **„Durere toracică" e o prezentare**, nu un home; diagnosticul diferențial al durerii
  toracice traversează capitole (cardiac, aortic, pulmonar, esofagian) = treabă de **index /
  aplicație de consultare**, nu de duplicare în date (regula „un singur home / fără breadcrumb").
- Prezentarea „durere toracică" e deja ancorată unde stă urgența: **Torace** — „Durere toracică
  izolată fără cauze aparente" (NR 726, radiografie); **Cardiovascular** — „Sindrom coronarian
  acut", „Sindrom aortic acut".
- **Acțiune aplicată:** titlul a fost reformulat pe entitate → „Reflux gastroesofagian / hernie
  hiatală", cu prezentarea „durere toracică" mutată în `Comentarii`. Confuzia dispare fără mutare.

---

## 20. Aparat digestiv — omisiuni de patologie față de ghiduri (propuneri de adăugat, 2026-07-09)

Verificare a capitolului (65 rânduri) față de **ACR Appropriateness Criteria (AC)**, **RCR
iRefer** și **ESGAR/ESGE**. Se listează situații clinice diagnostice **non-oncologice**
absente sau doar parțial acoperite. **Nimic nu s-a inserat în `GHID.csv`** — gradele/indicațiile
propuse sunt orientative și **de validat de editori** înainte de adăugare. Excluse (au home în
alt capitol): screening HCC în ciroză și stadializările → **Cancer**; trauma abdominală →
**Traumatisme**; drenaje/embolizări/TIPS → **RI**; variantele pediatrice → **Pediatrie**.

### 20.1 Lacune majore (topicuri AC dedicate, frecvente, fără situație proprie)

- ⏳ **Durere în hipocondrul drept — suspiciune de colecistită acută** (→ `Ficat, colecist și
  pancreas`). **Colecistita acută ≠ litiaza biliară — abordare imagistică distinctă**, deși
  ambele pornesc de la ecografie:
  - *Litiaza biliară* („Patologie biliară litiazică", situația existentă) = întrebare **anatomică**:
    există calculi? sunt căile dilatate? → Eco (referință); pentru litiaza **coledociană** →
    colangio-IRM (MRCP) / ecoendoscopie. **Colescintigrafia nu are rol.**
  - *Colecistita acută* = întrebare **inflamatorie/funcțională** (obstrucție de canal cistic +
    inflamație): Eco (perete îngroșat, lichid pericolecistic, semn Murphy ecografic, calcul
    inclavat în infundibul); când Eco e echivocă → **colescintigrafie (HIDA)**, cea mai
    sensibilă/specifică (non-umplerea colecistului = obstrucție cistică) — **modalitate absentă
    din tot capitolul**; CT/IRM pentru **complicații** (gangrenoasă, emfizematoasă, perforată).
  - Ref.: **Tokyo Guidelines TG18** (criterii dg. + gradare severitate colecistită acută);
    ACR AC *Right Upper Quadrant Pain* (Eco prima intenție; HIDA ca test de rezolvare a cazurilor
    echivoce; CT/IRM+MRCP pentru complicații).
  - Ecografie abdominală = *Indicat, B* (prima intenție).
  - **Scintigrafie biliară (colescintigrafie / HIDA)** = *Doar în cazuri particulare, B* — când
    ecografia e echivocă (sensibilitate/specificitate superioare pentru colecistita acută).
    **NB: HIDA lipsește complet din tot capitolul digestiv.**
  - CT abdominal cu contrast = *Doar în cazuri particulare* (complicații, diagnostic alternativ).
  - IRM + colangio-IRM = *Doar în cazuri particulare* (echivoc, gravide, coledocolitiază asociată).
  - Ref.: ACR AC *Right Upper Quadrant Pain*.

- ⏳ **Durere în fosa iliacă dreaptă — suspiciune de apendicită acută (adult)** (→ `Tub digestiv`).
  Azi doar în comentariul CT/Eco de la „Durerea abdominală acută"; AC îi dedică topic propriu.
  - CT abdomen și pelvis cu contrast = *Indicat, A/B* (adult, prima intenție).
  - Ecografie = *Doar în cazuri particulare* (pacient slab; **Indicat** la gravide/copii — copiii → Pediatrie).
  - IRM fără contrast = *Doar în cazuri particulare* (gravide).
  - Ref.: ACR AC *Right Lower Quadrant Pain — Suspected Appendicitis* (2022).

- ⏳ **Durere în fosa iliacă stângă — suspiciune de diverticulită acută** (→ `Tub digestiv`).
  Azi doar menționată în comentariul CT de la „Durerea abdominală acută".
  - CT abdomen și pelvis cu contrast = *Indicat, A/B* (prima intenție; stadializare Hinchey).
  - Ecografie = *Doar în cazuri particulare*.
  - Ref.: ACR AC *Left Lower Quadrant Pain — Suspected Diverticulitis*.

- ⏳ **Ischemie mezenterică (acută / cronică)** (→ `Tub digestiv`). Complet absentă. Patologie
  vasculară abdominală, dar **non-traumatică** → home în digestiv (Traumatisme = doar vascular traumatic).
  - Angio-CT abdomen și pelvis = *Indicat, A/B* (prima intenție, acut și cronic).
  - Angio-IRM abdomen și pelvis = *Doar în cazuri particulare* (cronic; insuficiență renală).
  - Eco Doppler = *Doar în cazuri particulare* (screening / formă cronică).
  - Ref.: ACR AC *Imaging of Mesenteric Ischemia*.

### 20.2 Lacune reale, parțial acoperite / mai înguste

- ⏳ **Boală hepatică cronică difuză — steatoză / fibroză / cuantificare (NAFLD-MASLD)** (→ `Ficat…`).
  - Ecografie ± elastografie (shear-wave) = *Indicat, B* (screening steatoză, stadializare fibroză).
  - IRM (PDFF / elastografie-RM) = *Doar cu aviz specializat, B* (cuantificare grăsime/fier, fibroză).
  - Non-oncologic (screening HCC în ciroză rămâne la Cancer › Tumori maligne primare hepatice).

- ⏳ **Hipertensiune portală / tromboză de venă portă / evaluare vasculară hepatică** (→ `Ficat…`).
  - Eco Doppler abdominal = *Indicat, B* (prima intenție: flux/permeabilitate portală, colaterale, Budd-Chiari).
  - CT / IRM cu contrast (fază venoasă/portală) = *Indicat / Doar în cazuri particulare* (cartografiere,
    tromboză tumorală vs. blandă, evaluare pre-TIPS — procedura însăși = RI).

- ⏳ **Suspiciune de abces hepatic / colecție intraabdominală (non-postoperator)** (→ `Ficat…` sau `Tub digestiv`).
  - Ecografie = *Indicat* (prima intenție); CT abdomen cu contrast = *Indicat* (caracterizare; drenajul = RI).
  - Azi acoperit doar tangențial (fistulă biliară postop, durere abdominală acută).

- ⏳ **Fistulă perianală / boală perianală (inclusiv Crohn perianal)** (→ `Tub digestiv`).
  Azi doar o mențiune în comentariul IRM de la „Maladie inflamatorie a colonului".
  - IRM pelvin (protocol fistulă) = *Indicat, A/B* (standard de aur).
  - Ecografie endoanală = *Doar cu aviz specializat*.
  - Ref.: ESGAR; ACR AC *Crohn Disease*.

- ⏳ **Chist hidatic hepatic / echinococoză** (→ `Ficat…`). Relevanță endemică (RO).
  - Ecografie = *Indicat, B* (clasificare WHO-IWGE / Gharbi); CT / IRM = *Doar în cazuri particulare*
    (localizări dificile, complicații biliare, planificare terapeutică).

### 20.3 Rafinări (situații distincte din situații/etichete existente)

- ⏳ **Perforație de organ cavitar / pneumoperitoneu (non-esofagian)** — azi doar perforația
  **esofagiană** are situație; perforația gastro-duodenală/colonică apare doar în comentarii
  („Durerea abdominală acută", „Sindrom ocluziv"). Radiografie în ortostatism + CT cu contrast
  oral/i.v. De decis dacă merită situație proprie.
- ⏳ **Colangită sclerozantă primitivă / evaluarea căilor biliare (colangio-IRM)** — azi doar
  mențiune în „Icter" și „Patologie biliară". Posibilă situație proprie (MRCP = examen de referință).
- ⏳ **Achalazie / tulburări de motilitate esofagiană** — tranzit baritat cronometrat (timed barium
  esophagogram); azi parțial sub „Disfagia înaltă sau joasă".
- ⏳ **Defecografie / disfuncție de planșeu pelvin posterior** (constipație de evacuare, prolaps,
  intususcepție rectală) — MR-defecografie / defecografie fluoroscopică. **Încadrare de decis:**
  `Tub digestiv` vs. `Obstetrică și ginecologie` (planșeu pelvin).

> Status: **13 propuneri deschise** (2026-07-09) — 4 lacune majore, 5 parțial acoperite, 4 rafinări.
> Gradele/indicațiile propuse sunt orientative (aliniate ACR AC / RCR iRefer / ESGAR) și rămân
> de validat de editori înainte de inserarea în `GHID.csv`. Nicio modificare de date până la decizie.

---

## 21. Gât (părți moi) — chestiuni ridicate la review (2026-07-09)

Din reviewul capitolului „Gât (părți moi)" (NR 1042–1059). Modificările mecanice
(diacritice, normalizare, de-duplicarea etichetei) au fost aplicate — vezi `CHANGELOG.md`
§11.

1. ✅ **Terminologie: „Hiperparatiroidie" vs „Hiperparatiroidism" — DECIS (2026-07-09).**
   La de-duplicarea etichetei (NR 1050 / NR 1051 — aceeași situație, scindată accidental),
   ambele rânduri s-au unificat la **„Hiperparatiroidism"** (forma standard din
   endocrinologie). Notă de consecvență: „Hipertiroidie" și „Hipotiroidie" rămân în forma
   „-ie" (nu au fost atinse); dacă editorii vor o uniformizare „-ism" pe tot vocabularul
   tiroidian, e o decizie separată, de semnalat aparte.

2. ✅ **Încadrare: „Suflu carotidian asimptomatic" (NR 1044) — DECIS și APLICAT
   (2026-07-09).** Situația este esențialmente **vasculară** — investigația unică e
   „Eco Doppler al vaselor cervico-craniene" (trunchiuri supra-aortice), workup identic cu
   evaluarea stenozelor carotidiene din **Aparat cardiovascular**. **Mutată** din „Gât
   (părți moi) › Diverse" în **„Aparat cardiovascular › Sistem vascular"** (poziționată
   alfabetic, între „Malformații vasculare" și „Tromboză venoasă membre inferioare"). Vezi
   `CHANGELOG.md` §4 și §11.

> Status: **2 decise și aplicate** (terminologia hiperparatiroidism; mutarea suflului
> carotidian) — 2026-07-09. Vezi §22 pentru chestiunile noi ridicate ulterior (omisiuni
> față de ghidurile internaționale, suprapunere cu „Cap › ORL").

---

## 22. Gât (părți moi) — omisiuni față de ghidurile internaționale + suprapunere cu „Cap › ORL" (2026-07-09)

Cercetare punctuală (ACR Appropriateness Criteria, RCR iRefer, ESR Essentials — Thyroid
Imaging 2025) pentru capitolul „Gât (părți moi)" (NR 1042–1059, după mutările din §21).
Verificarea încrucișată cu restul fișierului a scos la iveală și o **suprapunere
structurală cu „Cap › ORL"**, separată de chestiunea omisiunilor pure. Nicio modificare de
date — doar propuneri, de validat de editori.

### A. Suprapunere / încadrare greșită — „Cap › ORL" conține conținut de „Gât (părți moi)"

✅ **DECIS și APLICAT (2026-07-09) — varianta (a), mutare, fără unificare.** La cererea
editorului („mută la Gât tot ce e ORL/gât în capitolul Cap"), cele **12 rânduri** (3
situații) au fost relocate din „Cap › ORL" în „Gât (părți moi)":

- **NR 1015–1017 „Mase ale glandelor salivare"** + **NR 1021–1025 „Obstrucția fluxului
  salivar"** + **NR 1029 „Sindromul izolat de gură uscată"** → subcapitol **nou „Glande
  salivare"** (+ placeholder nou **NR 1439**).
- **NR 1018–1020 „Mase cervicale ale adultului"** → subcapitolul **„Diverse"**, alături de
  **NR 1042–1043 „Masă cervicală cu punct de plecare necunoscut"**.

✅ **Unificare — DECISĂ și APLICATĂ ulterior (2026-07-09, „do your best").** Cele două
situații au fost **comasate** într-una singură — „Masă cervicală la adult, cu punct de
plecare necunoscut" (NR 1042 E, 1043 M, 1020 T; NR 1018/1019 eliminate) — plus subcapitolul
„Diverse" **redenumit „Mase cervicale"**. Detalii complete (inclusiv un fragment de text
contaminat cu conținut de gușă, eliminat la comasare) în `CHANGELOG.md` §11
(„DE-DUPLICAT + RESTRUCTURAT"). Fostă intrare în `DUPLICATE-review.md` §C mutată la
„REZOLVATE".

**Rămas nemutat, la „Cap › ORL"** (structuri ale capului, nu ale gâtului): TMJ,
leziuni nazo-sinusale, patologie de ureche (colesteatom, urechea internă/medie,
surditate), sinuzite, tulburări de miros. „Corp străin faringian sau esofagian înalt"
rămâne subiectul unei decizii deschise separate (§8, §10 — nu face parte din acest lot).

### B. Omisiuni de conținut (propuneri de adăugat)

- ✅ **Sialolitiază / sialadenită acută — DECISĂ și APLICATĂ (2026-07-09).** La reverificare,
  golul era mai îngust decât estimat inițial: „Obstrucția fluxului salivar" acoperea deja
  litiaza (NR 1021 „natura litiazică", NR 1023 „complicație infecțioasă"/calculi). Lipsea
  doar **sialadenita acută infecțioasă fără calcul** (bacteriană, pacienți deshidratați/
  postoperator) — adăugată ca frază la finalul comentariului NR 1021 (Ecografie): aspect
  ecografic specific (glandă difuz mărită, hipoecogenă, hiperemică Doppler), ecografia
  rămâne primă intenție și fără litiază. Surse: StatPearls — *Sialolithiasis*; Applied
  Radiology — *Obstructive Sialadenitis*. Fără rând nou — completare de conținut existent.
- ✅ **Abces / infecție de spații cervicale profunde — DECISĂ și APLICATĂ (2026-07-09).**
  Situație nouă „Abces / infecție profundă de spații cervicale", subcapitol „Mase cervicale"
  — **2 rânduri**: NR 1441 (CT cu substanță de contrast, Indicat, grad B — standardul pentru
  extensie/complicații, câmp extins la mediastin dacă suspiciune de extensie descendentă) și
  NR 1442 (Ecografie cervicală/intraorală, Doar în cazuri particulare, grad B — pentru
  abcesul periamigdalian, sensibilitate/specificitate 89–100% comparativ cu CT, poate ghida
  drenajul). Surse: Springer — *Imaging of Neck and Facial Infections*; *Retropharyngeal
  Abscess* (2024); JETem — *POCUS for Peritonsillar Abscess*. Detalii în `CHANGELOG.md` §11.
- ✅ **Stratificare de risc ecografică a nodulului tiroidian (TI-RADS / EU-TIRADS) —
  DECISĂ și APLICATĂ (2026-07-09, la cerere explicită).** Reformulată față de propunerea
  inițială: nu completare pe NR 1046 (care descria de fapt greșit „Gușă plonjantă", nu
  nodulul tiroidian generic — vezi descoperirea din review-ul de comentarii), ci **rând nou
  de Ecografie (NR 1440)** pe situația care lipsea complet de testul de primă intenție —
  „Nodul tiroidian palpabil și gușă eutiroidiană – fază diagnostică" (avea doar
  Scintigrafie). Conținut verificat față de ATA 2015, ACR TI-RADS (JACR 2017) și ESR
  Essentials 2025. NR 1046/1047 („Gușă plonjantă – diagnostic") corectate separat, cu
  conținut specific gușii plonjante (limitarea ecografiei la extensia retrosternală,
  verificată StatPearls — Substernal Goiter). Detalii complete în `CHANGELOG.md` §11.

### Surse consultate

- [ACR AC — Neck Mass/Adenopathy (patient summary)](https://www.jacr.org/article/S1546-1440(22)00174-0/fulltext)
- [ACR AC — Parathyroid Adenoma](https://acsearch.acr.org/docs/3158171/Narrative/)
- [ACR TI-RADS — White Paper](https://www.jacr.org/article/s1546-1440(17)30186-2/fulltext)
- [ESR Essentials — Thyroid imaging (European Radiology, 2025)](https://link.springer.com/article/10.1007/s00330-025-12101-2)
- [Sialolithiasis — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK549845/)
- [Imaging of Neck and Facial Infections — Springer](https://link.springer.com/rwe/10.1007/978-3-031-78916-8_12)
- [Obstructive Sialadenitis — Applied Radiology](https://appliedradiology.com/articles/obstructive-sialadenitis)

> Status: **A și B decise și aplicate integral** (mutare Cap›ORL → Gât + de-duplicare „Mase
> cervicale ale adultului"/„Masă cervicală..." + redenumire subcapitol „Diverse" → „Mase
> cervicale" + TI-RADS/EU-TIRADS (NR 1440) + abces cervical profund (NR 1441/1442) +
> sialadenită acută fără litiază (NR 1021), 2026-07-09). Rămâne cvasi-duplicat cross-capitol
> **doar** „Corp străin faringian sau esofagian înalt" vs `Traumatisme › Corp străin`
> (nerezolvat, decizie de încadrare cross-capitol lăsată deschisă intenționat — vezi §8/§10
> și `DUPLICATE-review.md` §C). Nicio propunere de conținut deschisă. §22 **închis** —
> rămâne doar duplicatul din §8/§10.

---

## 23. Aparat uro-genital și glande suprarenale — chestiune ridicată la review (2026-07-09)

Ridicată la reviewul mecanic al capitolului 7 (vezi `CHANGELOG.md` §7). Corecturile
mecanice (ortografie, diacritice, normalizare, Tip↔Examen, eliminare breadcrumb-uri, husk)
au fost aplicate; rămâne o singură formulare clinică ambiguă, neatinsă:

- ⏳ **„Impotență" › Ecografie = Neindicat, cu comentariul „În formele secundare
  posttraumatice".** Formulare moștenită identic din sursa originală (necedilată deja
  acolo). Verdictul „Neindicat" pare să contrazică propria notă (care sugerează un context —
  forma secundară posttraumatică — în care ecografia ar avea rol). Posibil rezultat al unei
  trunchieri de conținut în sursă. Nu am modificat gradul/verdictul (regulă CLAUDE.md) —
  de clarificat de editori: fie completarea comentariului, fie schimbarea indicației la
  „Doar în cazuri particulare" dacă asta reflectă intenția reală.

> Status: **inventariat, neatins.** Restul capitolului (69→68 rânduri după eliminarea
> husk-ului „Uter și anexe") e curat: 0 breadcrumb-uri, 0 mismatch Tip↔Examen, 0 cedilă,
> subcapitole ordonate alfabetic pe situație. O analiză de completitudine față de ghiduri
> (ACR AC / RCR iRefer, gen §13/§15/§16/§18/§20) **a fost făcută separat — vezi §24**.

---

## 24. Aparat uro-genital și glande suprarenale — goluri de conținut față de ghidurile de
referință (2026-07-09)

Analiză de omisiuni a capitolului 7 față de practica curentă (**ACR Appropriateness
Criteria**, **AUA/SMSNA**, **Endocrine Society**), în paralel cu §13 (Cardiovascular), §15
(Sân), §16 (Cancer), §18/§20 (Torace/Aparat digestiv). **Schițe — de validat clinic de
editori** înainte de inserare; gradele sunt orientative. Acoperirea existentă a fost
verificată prin căutare în tot fișierul. **Notă de metodă:** temele de mai jos au fost
verificate live prin WebSearch (surse citate); conținutul detaliat (grade complete pe toate
variantele clinice) nu a fost extras integral din documentele-sursă — de confirmat înainte
de a fixa gradele definitive. Exclus din scop, per ierarhia capitolelor: cancer renal/
vezical/prostatic/testicular (→ Cancer), trauma urogenitală (→ Traumatisme), UTI/reflux la
copil (→ Pediatrie), infertilitate feminină (→ Obstetrică-ginecologie, deja acoperit — vezi
breadcrumb NR 801).

### 24.A Goluri clare (propuneri de adăugat în capitol)

- ⏳ **Priapism.** **Absent complet** (0 apariții în tot ghidul). Urgență urologică distinctă
  de „Durere și/sau masă scrotală" (organ diferit — corpi cavernoși, nu testicul/epididim).
  Ghidul AUA/SMSNA 2022 confirmă: gazometria din corpii cavernoși e primul test (non-
  imagistic), dar ecografia Doppler peniană are rol când diagnosticul ischemic vs.
  non-ischemic e neclar clinic (disting flux absent/velocități <50 cm/s + reversul
  diastolic în priapismul ischemic, față de flux crescut cu velocități >50 cm/s în cel
  non-ischemic — distincție critică pentru conduită, ischemic = urgență). Propunere —
  situație nouă „Priapism", subcapitol „Aparat genital masculin":
  - Eco-Doppler penian = *Doar în cazuri particulare, grad B* — când diagnosticul clinic
    ischemic/non-ischemic e neconcludent.
- ⏳ **Incontinență urinară / disfuncție de planșeu pelvin (femeie).** **Absentă complet**
  din tot ghidul (0 apariții „incontinen", inclusiv în Obstetrică-ginecologie). Temă ACR AC
  proprie, actualizată recent (*„Pelvic Floor Dysfunction in Females"*, cu topic conex
  *„Recurrent Lower Urinary Tract Infections in Females"* — update 2026). Propunere —
  situație nouă:
  - Ecografie (transperineală/introitală, reziduu postmicțional) = *Indicat, grad B* —
    evaluare inițială.
  - IRM dinamic de planșeu pelvin = *Doar cu aviz specializat, grad B* — cazuri complexe/
    preoperator, disfuncție combinată.
  - **De decis home:** Aparat urogenital (simetric cu „Sindrom obstructiv jos" la bărbat)
    vs. Obstetrică-ginecologie › Ginecologie (disfuncție de planșeu pelvin e adesea
    tratată acolo). Recomandare: Aparat urogenital, pentru simetrie cu LUTS masculin deja
    prezent aici.

### 24.B Modernizare — glande suprarenale (propuneri de completare/reconsiderare a gradelor,
NU aplicate — decizie editori)

- ⏳ **Feocromocitom/paragangliom — PET-CT cu ⁶⁸Ga-DOTATATE absent.** Situația „Tumori
  medulosuprarenaliene (feocromocitom)" are IRM/CT/Scintigrafie mIBG, toate *Indicat*. Studii
  comparative directe arată sensibilitate net superioară a ⁶⁸Ga-DOTATATE PET-CT față de
  scintigrafia cu I-131/I-123-MIBG (~93% vs. ~47% per-pacient; ~92% vs. ~26% per-leziune),
  cu detecție superioară și a bolii metastatice/extra-adrenale — surse convergente îl descriu
  ca „prima linie ideală" pentru pheo/paragangliom. mIBG rămâne util adjuvant (planificare
  terapie cu I-131-MIBG) dar nu mai e echivalent ca test de primă linie. Propunere: rând nou
  PET-CT (⁶⁸Ga-DOTATATE) = *Indicat, grad B*; **nu modific gradul scintigrafiei mIBG singur**
  (regulă CLAUDE.md) — semnalez pentru decizia editorilor dacă indicația ei coboară la „Doar
  în cazuri particulare" (analog precedentului scintigrafiei osoase la cancer bronho-pulmonar,
  §17).
- ⏳ **Sdr. Conn — scintigrafia I131-Norcolesterol supra-cotată față de rolul actual.**
  Ghidul Endocrine Society (2016, reconfirmat 2025) situează **CT suprarenalian** (excludere
  carcinom) + **cateterism venos suprarenalian / AVS** (deja prezent corect în RI › Aparat
  urogenital, Tip A, „Doar cu aviz specializat") ca modalitățile centrale pentru
  lateralizare; scintigrafia cu iodocolesterol (NP-59/I131-Norcolesterol) e descrisă explicit
  ca rol **ancilar** — folosită doar când cateterismul bilateral eșuează — nu ca test
  co-egal cu CT-ul. În ghidul nostru, scintigrafia apare *Indicat* grad B, la fel ca CT-ul,
  sugerând paritate. **Nu modific gradul singur** — semnalez pentru editori: posibilă
  coborâre la „Doar în cazuri particulare" sau reformulare a comentariului (rol ancilar,
  nu de primă linie). Aceeași scintigrafie apare și la sdr. Cushing (NR 858) — verificați
  dacă observația se aplică și acolo, sau dacă acolo rolul ei diferă (localizări ectopice/
  bilaterale, unde comentariul actual pare deja adecvat).

### 24.C Minore — de îmbogățit, nu neapărat situație nouă

- ⏳ **Varicocel — fără linie diagnostică proprie în Aparat genital masculin.** Apare doar
  implicit, în comentariul „Infertilitate masculină" (Obstetrică-ginecologie › Fertilitate,
  NR 871: „ecografia Doppler scrotală… pentru depistarea… varicocelelor infraclinice") și ca
  tratament la RI (`Radiologie intervențională › Aparat cardiovascular › Varicocel ›
  Embolizare`, NR 1280 — încadrare RI discutabilă, ar aparține mai degrabă „Aparat
  urogenital" ca restul procedurilor urologice, de verificat la parsarea RI). Diagnosticul
  propriu-zis (Eco-Doppler scrotal) nu are rând dedicat în capitolul de diagnostic. Prioritate
  scăzută — acoperire implicită suficientă pentru scopul ghidului.
- ⏳ **„Durere și/sau masă scrotală" combină două topicuri ACR AC distincte** (*Acute Onset
  of Scrotal Pain* vs. *Newly Diagnosed Palpable Scrotal Abnormality*, cu grade de suspiciune
  de malignitate diferite pentru masa nedureroasă). Combinarea într-o singură situație e o
  simplificare rezonabilă (ambele → ecografie, grad B), dar de reconfirmat dacă merită
  separare (masa nedureroasă la adult tânăr are prag mai jos pentru a exclude tumoră
  testiculară → breadcrumb implicit spre Cancer, neexplicit azi).

### Surse consultate

- [ACR AC — Pelvic Floor Dysfunction in Females](https://acsearch.acr.org/docs/3083064/Narrative/)
- [ACR AC — Recurrent Lower Urinary Tract Infections in Females: Update 2026 (JACR)](https://www.jacr.org/article/S1546-1440(26)00158-4/fulltext)
- [ACR AC — Lower Urinary Tract Symptoms-Suspicion of BPH](https://acsearch.acr.org/docs/69368/Narrative/)
- [AUA/SMSNA — Acute Ischemic Priapism Guideline (2022)](https://www.auanet.org/guidelines-and-quality/guidelines/acute-ischemic-priapism)
- [Diagnostic Performance of 68Ga-DOTATATE PET/CT vs. 131I-MIBG in Pheochromocytoma/
  Paraganglioma — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4463879/)
- [Endocrine Society — Primary Aldosteronism Clinical Practice Guideline (AVS/CT vs.
  scintigraphy)](https://academic.oup.com/jcem/article/101/5/1889/2804729)
- [ACR AC — Newly Diagnosed Palpable Scrotal Abnormality](https://acsearch.acr.org/docs/3158184/Narrative/)

> Status: **niciun rând nou inserat, niciun grad modificat** în `GHID.csv`. Se așteaptă
> decizia editorilor pentru 24.A (situații noi) și 24.B (reconsiderare grad scintigrafie
> suprarenaliană / adăugare DOTATATE); apoi se adaugă/ajustează cu grade validate pe sursă
> citabilă și se consemnează în `CHANGELOG.md`. 24.C rămas informativ, prioritate scăzută.

---

## 25. Fostul „Uter și anexe" — capitol scris superficial: doar terapeutic, fără diagnostic
(observație utilizator, 2026-07-09)

**Observația utilizatorului, confirmată de verificare:** subcapitolul „Aparat uro-genital ›
Uter și anexe", eliminat la review (§5/§23, CHANGELOG §7) fiindcă rămăsese doar cu rândul-
placeholder Z, nu era gol întâmplător — **conținea de la bun început, în sursa originală,
exclusiv proceduri Tip I** (embolizare / HSG / angiografie), **fără nicio linie de
diagnostic** (ecografie/IRM) pentru ele. Nu e un artefact al restructurării RI — e o lacună
preexistentă în ghidul-sursă, doar devenită mai vizibilă acum că rândurile terapeutice
(corect mutate la RI › Aparat urogenital, NR 1363–1375) nu mai lasă în urmă niciun rând-
umbrelă în capitolul anatomic.

**Verificare acoperire existentă** (căutare în tot `GHID.csv`): din cele 12 situații clinice
ale fostului subcapitol, **3 au deja diagnostic în altă parte** (Sarcină ectopică →
Obstetrică-ginecologie › Sarcină, NR 891; Avorturi spontane multiple + Infertilitate
feminină → Fertilitate, NR 867–870; Metroragii postmenopauzale → Ginecologie, NR 876–877).
**9 nu au nicio linie de diagnostic nicăieri.**

**Home corect pentru diagnostic** (per ierarhia capitolelor): nu Aparat uro-genital (unde
stătea husk-ul) — patologia uterină/anexială stă la **Obstetrică-ginecologie**, lângă
conținutul deja existent acolo (simetric cu „Suspiciune de masă pelvină", „Metroragii
postmenopauzale" din Ginecologie). Terapeuticul rămâne corect la RI (regula de aur 4) —
aici se propune **doar** completarea diagnosticului lipsă, capăt care precede logic orice
decizie de embolizare.

**Decizie utilizator:** doar draft aici (fără inserare în `GHID.csv` deocamdată).

### 25.A Propuneri — `Obstetrică-ginecologie › Ginecologie`

- ⏳ **Leiomiom uterin (fibrom uterin, unic sau multiplu)** — unifică etichetele „Leiomiomul
  uterin" + „Polifibromatoza uterina" din RI (workup diagnostic identic indiferent de
  numărul fibroamelor; procedurile terapeutice din RI rămân neatinse). **Gol notabil** —
  patologie extrem de frecventă, complet absentă ca diagnostic din tot ghidul. Temă ACR AC
  proprie (*„Fibroids"*, 2022; *„Management of Uterine Fibroids: 2023 Update"*):
  - Ecografie (transvaginală ± transabdominală, ± Doppler) = *Indicat, grad A* — primă
    intenție pentru diagnostic inițial.
  - IRM cu contrast i.v. = *Doar cu aviz specializat, grad B* — mapare (număr, dimensiune,
    perfuzie, poziție) înainte de embolizare/miomectomie; exclude leiomiosarcomul la cazuri
    atipice.
- ⏳ **Adenomioză uterină.** **Absentă complet** ca diagnostic (există doar embolizarea în
  RI). Literatura (review-uri de acuratețe diagnostică, 2023–2024) confirmă ecografia
  transvaginală ca primă linie, IRM ca linie a doua (mai sensibil/specific) la caz echivoc
  sau coexistență cu fibrom:
  - Ecografie (transvaginală) = *Indicat, grad B* — primă intenție.
  - IRM = *Doar cu aviz specializat, grad B* — caz echivoc ecografic sau înainte de
    embolizare/tratament conservator.
- ⏳ **Sângerare genitală acută/severă (refractară la tratament medical).** Corespunde
  „Hemoragii acute/cronice în sfera genitală" din fostul „Uter și anexe" — distinctă de
  „Metroragii postmenopauzale" (care e specific perimenopauzal/de excludere a malignității,
  deja acoperită). Aici accentul e pe **identificarea sursei înainte de o embolizare de
  urgență/electivă** (fibrom, resturi placentare, tumoră, cauză vasculară):
  - Ecografie (± Doppler) = *Indicat, grad B* — evaluare inițială, identifică patologia
    subiacentă.
  - AngioCT = *Doar în cazuri particulare, grad C* — pacientă instabilă hemodinamic, pentru
    localizarea sursei active de sângerare înaintea embolizării emergente.
- ⏳ **Varice periuterine (sindrom de congestie pelvină).** Absent complet ca diagnostic
  (doar embolizare în RI). Consens SFICV/FRI/CERF/SIFEM (2024) și literatura de specialitate:
  - Ecografie transvaginală + Doppler = *Doar în cazuri particulare, grad C* — primă linie,
    dar sensibilitate/specificitate limitate.
  - IRM (± angio-IRM) = *Doar cu aviz specializat, grad B* — extensia varicelor, exclude
    diagnostice diferențiale (ex. endometrioză), planificare pre-embolizare.
- ⏳ **Malformații/fistule arterio-venoase pelvine.** Absente ca diagnostic; patologie rară,
  de obicei surprinsă incidental sau prin extensia investigării altei situații (hemoragie,
  masă pelvină). Prioritate scăzută — **de cercetat mai atent** înainte de a propune
  grade (sursele găsite sunt de nivel caz-serie, insuficiente pentru un grad citabil).

### 25.B Propuneri — `Obstetrică-ginecologie › Obstetrică`

- ⏳ **Anomalii de placentație (spectrul placenta accreta).** Absente complet ca diagnostic
  (doar embolizare „doar în cazuri particulare" în RI). Temă ACR AC proprie („Placenta
  Accreta Spectrum Disorder"): ecografia (2D + Doppler, cu markeri standardizați EW-AIP:
  lacune placentare, subțiere miometrială) e testul de primă linie antenatal; IRM e adjuvant
  pentru cazuri echivoce/planificare chirurgicală (sensibilitate/specificitate similare, dar
  câmp vizual mai mare, utilă mai ales pentru placenta posterioară):
  - Ecografie (cu Doppler) = *Indicat, grad A* — screening/diagnostic la paciente cu risc
    (placenta praevia + cezariană/chirurgie uterină în antecedente).
  - IRM = *Doar cu aviz specializat, grad B* — ecografie echivocă sau nevoie de planificare
    chirurgicală detaliată (extensie laterală, organe adiacente).

### Surse consultate

- [ACR AC — Fibroids (2022)](https://www.jacr.org/article/S1546-1440(22)00653-6/fulltext)
- [ACR AC — Management of Uterine Fibroids: 2023 Update](https://www.jacr.org/article/S1546-1440(24)00263-1/abstract)
- [ACR AC — Abnormal Uterine Bleeding](https://www.jacr.org/article/S1546-1440(20)30948-0/fulltext)
- [ACR AC — Placenta Accreta Spectrum Disorder](https://www.jacr.org/article/S1546-1440(20)30119-8/fulltext)
- [MRI and Adenomyosis: What Can Radiologists Evaluate? — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9140978/)
- [Pelvic Congestion Syndrome — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK560790/)
- [Endovascular management of pelvic congestion syndrome — SFICV/FRI/CERF/SIFEM expert
  consensus (2024/2025)](https://www.sciencedirect.com/science/article/pii/S2211568425000750)

> Status: **niciun rând inserat** în `GHID.csv` (la cererea utilizatorului — doar draft).
> 9 din 12 situații ale fostului „Uter și anexe" nu au diagnostic nicăieri în ghid; 3 au deja
> (§ intro). Propuneri gata de validat/inserat la `Obstetrică-ginecologie` (nu la Aparat
> uro-genital) când se decide — ar completa și capitolul 8, nu doar 7. „Malformații/fistule
> arterio-venoase pelvine" rămâne fără propunere de grad (sursă insuficientă).

---

## 26. Aparat uro-genital — ordine/grad pe muchie, semnalate la recitire (2026-07-09)

Observații de la a treia trecere prin capitol (după renumerotare). **Ating grade sau ordinea
examenelor → NU le modific singur** (reguli de aur); le consemnez pentru editori.

- ⏳ **Incidentalom suprarenalian — CT non-contrast pare subevaluat ca poziție și grad.**
  Ordinea curentă a examenelor: IRM (grad C) → Scintigrafie Norcolesterol (B) → CT (C). Dar
  **comentariul propriu** al situației spune „Sunt indicate un examen CT fără injectare și
  măsurarea densității… O leziune omogenă cu densitate sub 10 UH (CT)… sunt sugestive pentru
  adenom" — adică CT-ul non-contrast cu măsurarea densității e, în text, testul-cheie de
  primă linie (ACR AC / ghiduri de incidentalom suprarenalian: CT washout = pilonul
  caracterizării). Totuși e listat ultimul și cu grad C „Doar cu aviz specializat", sub IRM.
  Posibilă inversiune de prioritate moștenită din sursă. **De decis editori:** promovarea
  CT-ului pe prima poziție și/sau ridicarea gradului. (Nu am reordonat — ordinea examenelor e
  intangibilă fără decizie explicită.)
- ⏳ **sdr. Cushing — două rânduri CT (grad A + grad B) sub aceeași situație.** NR 859 (CT,
  grad A, „de primă intenție când ACTH plasmatic e scăzut" = Cushing ACTH-independent,
  suprarenalian) și NR 860 (CT, grad B, comentariu identic cu IRM-ul NR 858, scenariul
  „ACTH nu e diminuat" → IRM hipofizar/CT toracic = Cushing ACTH-dependent). **Nu e duplicat
  greșit** — sunt două sub-scenarii etiologice reale colapsate sub o etichetă unică. De decis
  dacă merită **etichete de situație separate** („Cushing ACTH-independent" vs „ACTH-dependent")
  pentru claritate, sau rămân comasate (compact, dar cu grade duble aparent contradictorii pe
  aceeași modalitate). Analog perechilor duplicate păstrate intenționat (CLAUDE.md).

> Status: **niciun grad/ordine modificat**. Pur observațional, pentru decizia editorilor.

---

## 27. Obstetrică și ginecologie — chestiuni ridicate la review (2026-07-10)

Observații de la trecerea completă prin capitol. Corecturile mecanice (diacritice, spații,
breadcrumb, repartizare col. 9/10) au fost aplicate. Punctele 1, 3 și 4 de mai jos au fost
**rezolvate ulterior la cererea editorului (2026-07-10)**; rămâne deschis doar punctul 2.

- ✅ **REZOLVAT — „Dureri pelvine": etichetă unificată.** Rândul CT (fostă etichetă „*Dureri
  pelvine, în special suspiciune de inflamație pelvină*") a primit sufixul „**și de
  endometrioză**", identic cu rândurile Ecografie și IRM → cele 3 modalități formează acum o
  singură situație (CT → Eco → IRM). **Ordinea examenelor NU a fost atinsă** (rămâne CT întâi,
  cum era fizic); dacă editorii vor promovarea Ecografiei — prima intenție, grad A — pe prima
  poziție, e o decizie separată de ordine-examene (intangibilă fără cerere explicită).
- ⏳ **DESCHIS — „Metroragii postmenopauzale…": etichetă concatenată fără separator.** Eticheta
  e „*Metroragii postmenopauzale: excluderea unei patologii semnificative Menometroragii*" —
  două entități lipite („…semnificative" + „Menometroragii"). Editorul a confirmat că **sunt
  două situații**, dar a cerut **să rămână nerezolvată** deocamdată (de discutat cu ceilalți
  editori: separare în două situații vs. reformulare cu separator). **Nemodificată.**
- ✅ **REZOLVAT — „Infertilitate masculină" mutată la Uro-genital › Aparat genital masculin.**
  Rândul (Ecografie Doppler scrotală) a fost relocat din Obstetrică-ginecologie › Fertilitate
  în capitolul Aparat uro-genital, subcap. „Aparat genital masculin", situația „Infertilitate
  masculină" (înaintea „ALTĂ SITUAȚIE CLINICĂ"). A **înlocuit placeholder-ul-breadcrumb** Tip
  `Z` care exista deja acolo („Infertilitate – vezi capitolul Obstetrică-Ginecologie") →
  breadcrumb eliminat, conținut real adus. NR.CRT 870 păstrat (necontiguu în uro-genital).
- ✅ **REZOLVAT — reordonare situații subcap. „Sarcină" (flux urgență → cronic → ALTĂ).**
  Ordine nouă: „Suspiciune de sarcină extrauterină" (urgență) → „Posibilitate de sarcină
  non-viabilă" (acut) → „Suspiciune de sarcină la o femeie asimptomatică" (detecție/particular)
  → „Ecografie de control în timpul sarcinii" (monitorizare de rutină) → „…Evaluare a
  restricției de creștere fetală" (monitorizare specializată) → „ALTĂ SITUAȚIE CLINICĂ".
  Reordonare **fizică** (NR.CRT rămân atașate rândurilor, deci necontigue până la o eventuală
  renumerotare la cerere). Ordinea examenelor din interiorul fiecărei situații — neatinsă.

> Status: **niciun grad, doză sau ordine de examene modificat.** Rămâne deschis punctul 2
> (etichetă „Metroragii/Menometroragii"), la cererea editorului.

---

## 28. Obstetrică și ginecologie — goluri de conținut față de ghidurile de referință (2026-07-10)

Comparație a capitolului (26 rânduri, ~13 situații) cu topicele **ACR Appropriateness
Criteria® — Women's Imaging** (2023–2024), **RCR iRefer** și ghidul CAR OB/GYN (2023).
Capitolul actual e **subțire**: acoperă infertilitate (parțial), durere pelvină cronică/
inflamație/endometrioză (comasate), metroragii postmenopauzale, DIU, masă pelvină,
disproporție cefalo-pelvină și 5 scenarii de sarcină. Lipsesc mai multe topice majore.

**NU am adăugat rânduri în `GHID.csv`** — adăugarea de situații/grade e decizie clinică-
editorială (regula 6). Mai jos sunt **propuneri**, cu modalitatea de primă intenție conform
ghidurilor; gradul final îl fixează editorii. Încadrarea urmează ierarhia din `CLAUDE.md`.

### 28.A Goluri clare cu home = Obstetrică-ginecologie (propuneri de adăugat)

**Ginecologie:**

1. 🔴 **Durere pelvină acută (femeie de vârstă reproductivă, non-gravidă)** — topic ACR
   distinct de „dureri pelvine cronice/endometrioză" pe care le avem. Acoperă **torsiune
   anexială/ovariană, chist hemoragic sau rupt, abces tubo-ovarian**. Eco transvaginală +
   transabdominală **cu Doppler** = primă intenție (grad A); **CT abdomen-pelvis** când se
   suspectează etiologie non-ginecologică (ex. apendicită) sau Eco echivocă. Torsiunea
   ovariană e o urgență — merită vizibilitate proprie (azi complet absentă).
2. 🔴 **Sângerare uterină anormală — premenopauzală / vârstă reproductivă (AUB).** Avem doar
   metroragiile *postmenopauzale*. Eco TV+TA cu Doppler = primă intenție (A);
   **sonohisterografie (SIS/histerosonografie)** pentru polipi/miom submucos/patologie
   endometrială; IRM a doua intenție. ACR „Abnormal Uterine Bleeding".
3. 🟠 **Leiomioame uterine (fibroame) — caracterizare / cartografiere.** Absente ca situație.
   Eco = primă intenție; **IRM** pentru cartografiere pre-miomectomie/pre-embolizare și când
   Eco e neconcludentă. (Embolizarea de arteră uterină = capitolul RI — vezi 28.B.)
4. 🟠 **Endometrioză — situație dedicată** (azi comasată în „Dureri pelvine…"). ACR are topic
   separat: Eco TV (primă intenție, inclusiv endometrioză profundă) + **IRM cu protocol
   dedicat** (opacifiere vaginală/rectală — deja descris în comentariul nostru IRM). De decis
   dacă se separă „Endometrioză (suspiciune / bilanț de extensie)" de durerea pelvină generică.
5. 🟡 **Anomalii congenitale uterine (malformații mülleriene).** Azi doar menționate în
   comentariile de la infertilitate/avorturi. Eco 3D + **IRM** pentru clasificare (uter
   septat vs bicorn etc.) — relevant pentru infertilitate și avort recurent.

**Obstetrică / Sarcină:**

6. 🔴 **Sângerare de trimestru II/III (placenta previa, dezlipire de placentă).** Absentă.
   Eco = primă intenție (localizarea placentei, previa, vasa previa); IRM adjuvant în cazuri
   selectate. ACR „Second and Third Trimester Bleeding".
7. 🔴 **Spectru placenta accreta (placentă aderentă morbid).** Absentă, dar clinic majoră
   (risc hemoragic peripartum). **Eco cu Doppler** (lacune placentare, hipervascularizație la
   nivelul cicatricei de cezariană) = primă intenție; **IRM** pentru profunzimea invaziei,
   placentă posterioară și planificare chirurgicală multidisciplinară.
8. 🟠 **Hemoragie postpartum / retenție de produse de concepție.** Absentă. Eco (retenție,
   cheaguri) primă intenție; CT/angiografie la sângerare activă. (Embolizarea de arteră
   uterină = RI — vezi 28.B.) ACR „Postpartum Hemorrhage".
9. 🟡 **Evaluarea colului gravid / insuficiență cervicală (col scurt).** Absentă. **Eco TV**
   a lungimii cervicale. ACR „Assessment of the Gravid Cervix".
10. 🟠 **Suspiciune de anomalie fetală — completarea ecografiei (IRM fetal).** Avem doar
    „ecografie de control". **IRM fetal** e adjuvant recunoscut pentru anomalii SNC (și altele)
    când ecografia e neconcludentă/insuficientă. De adăugat ca situație/rând (IRM, fără iradiere).

### 28.B Goluri cu home probabil în alt capitol (nu se adaugă aici)

- **Embolizări** (fibrom/UAE, hemoragie postpartum, sindrom de congestie pelvină / varice
  pelvine): Tip `I`/`A` → **RI › Aparat urogenital**. (Congestia pelvină e deja semnalată la
  §23/§24 uro-genital.) Partea *diagnostică* a fiecăreia rămâne aici.
- **Disfuncție de planșeu pelvin / prolaps de organe pelvine** — IRM dinamic / **defecografie
  IRM** (ACR „Pelvic Floor Dysfunction in Females"). **De decis home:** Obstetrică-ginecologie
  vs Aparat uro-genital (ACR îl încadrează la Women's Imaging; la noi funcția vezicală/
  urinară e la uro-genital). Flag de încadrare.
- **Durere abdomino-pelvină non-obstetricală la gravidă** (apendicită, colică renală): Eco
  primă intenție, **IRM fără contrast** a doua intenție (evită iradierea) — scenariu de graniță
  cu Aparat digestiv / uro-genital; de decis dacă merită un rând „la gravidă".
- **Tromboembolism venos în sarcină (TVP / embolie pulmonară)** → Cardiovascular / Torace.
- **Screening / stadializare cancer ovarian, endometrial, de col** → **Cancer** (de verificat
  completitudinea acolo — cf. §16 pentru col/corp uterin/ovar).

### 28.C Parțial acoperite — de îmbogățit (nu neapărat situație nouă)

- **Infertilitate feminină — lipsesc examenele-cheie de permeabilitate tubară.**
  **Histerosalpingografia (HSG, Tip `X`)** și **HyCoSy / histerosonografia** sunt menționate
  doar în comentarii, dar nu există ca rânduri de examen. ACR „Female Infertility" le listează
  explicit. Propunere: adăugarea lor ca investigații la situația „Infertilitate feminină".
- **Masă anexială — caracterizare (fără simptome acute).** Situația „Suspiciune de masă
  pelvină" acoperă scenariul, dar se poate îmbogăți cu **clasificarea O-RADS** (US/MRI) și
  rolul IRM pentru leziuni indeterminate. ACR „Clinically Suspected Adnexal Mass".
- **Sarcină de prim trimestru — „sarcină cu localizare necunoscută (PUL)".** Avem
  extrauterina și non-viabila; scenariul PUL (Eco TV + β-hCG seriat) ar completa logic grupul.

> Status: **analiză, fără modificare de date.** Propunerile de mai sus așteaptă decizia
> editorilor (ce se adaugă, cu ce grad, unde se încadrează cazurile de graniță din 28.B).
> Surse: ACR Appropriateness Criteria® (Women's Imaging, 2023–2024), RCR iRefer (ed. 8),
> CAR OB/GYN Referral Guideline (2023).

---

## 29. Pediatrie — chestiuni ridicate la reviewul de conținut (2026-07-10)

Al doilea review complet al capitolului (primul fusese la începutul proiectului, înainte de
consolidarea regulilor). Corecturile mecanice (diacritice, spații, breadcrumb-uri, denumiri
examene, repartizarea col. 9/10) au fost aplicate. Cele de mai jos ating **coduri Tip** →
nu le schimb singur (pot fi intenționale în sursă), le las editorilor.

- ⏳ **„Cistosonografie" (RVU, NR 192) — Tip `X` (contrast/fluoroscopie) vs `E` (ecografie).**
  Cistosonografia micțională cu contrast (ceVUS) este **ecografică** (comentariul o descrie ca
  „neimplicând iradiere", preferabilă cistografiei). Codul `X` pare incorect (ar trebui `E`).
  Nu l-am schimbat — de confirmat editorii (unele ghiduri o grupează cu cistografia micțională).
- ⏳ **„RRVS, UIV" (NR 175 „Dilatație de căi urinare", NR 186 „Infecție urinară") — Tip `G`
  pe un examen combinat.** RRVS (radiografie renală simplă) = `G`, dar UIV (urografie i.v.) e
  contrast/fluoroscopie = `X`. Rândul reunește două examene sub un singur cod. De decis:
  separare în două rânduri (fiecare cu Tip-ul propriu) sau păstrare combinată; nu am atins-o.

> Status: **niciun grad, doză sau cod Tip modificat** la aceste puncte. Restul reviewului
> (corecturi mecanice + repartizare col. 9/10 + reordonare pe flux) a fost aplicat.

---

## 30. Coloană vertebrală — chestiuni ridicate la review (2026-07-10)

> ✅ **REZOLVAT (2026-07-10, la cerere — „consolidare completă").** Toate punctele 30.A–D de mai
> jos au fost aplicate; vezi `CHANGELOG.md §12 › RESTRUCTURAT — consolidare completă Coloană lombară`.
> Rezumat al raționamentului pe grade/indicații (păstrat pentru trasabilitate): în ambele perechi o
> situație era **superset de modalități** al celeilalte, deci fuziunea a păstrat situația-superset și
> gradele ei (identice pe modalitățile comune cu cealaltă). Singura diferență de formulare — G la
> lombalgia cronică, „Neindicat" vs „Neindicat în primă intenție" — s-a rezolvat în favoarea variantei
> nuanțate, **susținută de comentariul propriu** (radiografia e utilă la tineri <20 / >55 ani pentru
> spondilolisteză / spondilită anchilozantă), nu printr-o schimbare arbitrară de grad. Textul de mai
> jos se păstrează ca justificare a deciziei.

Review complet al capitolului. Corecturile mecanice (diacritice, spații, denumiri examene,
`toracală→toracică`) și comasările **evidente** (duplicate cu examene identice) au fost
aplicate — vezi `CHANGELOG.md §12`. Punctele de mai jos (comasări cu seturi de examene diferite
+ ștergerea rândului-punte + reordonarea) au fost **aplicate în runda a doua**.

### 30.A ⏳ „Lombalgie cronică" — două situații cvasi-duplicate, seturi de examene diferite

Coloană lombară conține două situații cu același sens clinic (lombalgie cronică fără semne de
infecție/tumoră), scrise diferit și cu **liste de examene care nu coincid**:

- **„Durere lombară cronică fără semne de infecție sau tumoră: lombalgie comună"** — M, N
  (scintigrafie), T, G.
- **„Lombalgie cronică fără semne de infecție sau tumoră"** — N (PET-CT), N (scintigrafie),
  M, T, G. (adaugă PET-CT față de prima)

Ambele au grade preponderent „Doar în cazuri particulare"/C. **Nu le-am comasat** — o fuziune
ar trebui să decidă: (a) eticheta unică păstrată; (b) dacă PET-CT (F18-FDG) rămâne la lombalgia
cronică *necomplicată* sau doar la cea cu semne de gravitate; (c) ce comentarii se păstrează pe
fiecare modalitate. De asemenea, denumirile „**IRM coloana lombara**"/„**CT coloana lombara**"
(la a doua situație) ar trebui normalizate la „IRM"/„CT" (convenția dominantă) la comasare.

### 30.B ⏳ „Lombalgie în context particular / semne de gravitate" — pereche cvasi-duplicată

Tot în Coloană lombară, două situații cu același sens (red flags: debut <20/>55 ani, sdr. de
coadă de cal, deficit neurologic, cancer, HIV etc.), seturi de examene parțial suprapuse:

- **„Lombalgie în context particular sau însoțită de semne de gravitate: …"** — M (IRM coloana
  lombara), N (PET-CT F18-FDG sau F18-NaF), N (scintigrafie). Toate „Indicat".
- **„Lombalgie într-un context particular sau eventual însoțită de semne de gravitate ca și: …"**
  — N (scintigrafie), M (IRM). Toate „Indicat".

**Nu le-am comasat** (M și N-scintigrafie apar în ambele → fuziunea ar crea duplicate intra-
situație de rezolvat). De decis eticheta unică, dacă se păstrează PET-CT, și normalizarea
„IRM coloana lombara → IRM".

### 30.C ⏳ Rând-breadcrumb „Afecțiuni congenitale – vezi capitolul Pediatrie" (Tip `Z`)

Subcapitolul „Coloană" conține un rând-punte Tip `Z` fără examen concret („Vezi Detalii Ghid!",
comentariu „Vezi capitolul Pediatrie") a cărui unică funcție e navigarea către Pediatrie.
Conform regulii „un singur home / fără breadcrumb-uri", este **candidat la eliminare** (afecțiunile
congenitale ale coloanei au home-ul în Pediatrie). **Nu l-am șters** — confirmă editorii dacă se
elimină rândul sau se păstrează ca semnalizare.

### 30.D ⏳ Ordonarea pe flux clinic a situațiilor din Coloană lombară

După comasări, ordinea situațiilor din Coloană lombară nu urmează strict fluxul
urgență/acut → cronic → screening (checklist §7). Reordonare fizică **neaplicată** în acest
review (pentru a păstra diff-ul concentrat pe corecturi + de-duplicare); de făcut la o trecere
ulterioară dedicată, împreună cu deciziile 30.A/30.B.

> Status: **niciun grad, doză sau cod Tip modificat** în acest capitol. Comasările aplicate au
> vizat exclusiv duplicate cu examene + grade **identice** pe modalitățile comune; comentariile
> păstrate au fost alese dintre cele existente (cel mai bogat/canonic per modalitate), fără
> compunere de text clinic nou. Singura completare de etichetă (30.B) a adăugat red-flag-uri deja
> prezente în perechea eliminată.

---

## 31. Coloană vertebrală — goluri de conținut față de ghidurile de referință (2026-07-10)

Comparație a capitolului (38 rânduri, 10 situații) cu topicele de coloană din **ACR
Appropriateness Criteria®** — *Low Back Pain* (2021 Update), *Suspected Spine Infection* (2021),
*Myelopathy*, *Management of Vertebral Compression Fractures* — cu **RCR iRefer** (secțiunea
musculo-scheletală / coloană) și cu criteriile **ASAS** pentru spondilartrita axială.

**Acoperit azi:** durere axială (cervicalgie / dorsalgie / lombalgie cronică), durere radiculară
(nevralgie cervico-brahială, lombo-radiculalgie acută), lombalgie cu semne de gravitate,
instabilitate atlanto-axoidiană non-traumatică, sindrom medular (mielopatie) netraumatic, bilanț
de fractură vertebrală spontană, sacroileită. **Lipsesc câteva topice majore din ghiduri.**

**NU am adăugat rânduri în `GHID.csv`** — adăugarea de situații/grade e decizie clinică-editorială
(regula 6). Mai jos sunt **propuneri**, cu modalitatea de primă intenție conform ghidurilor; gradul
final îl fixează editorii. Încadrarea urmează ierarhia din `CLAUDE.md`.

### 31.A Goluri clare cu home = Coloană vertebrală (propuneri de adăugat)

1. 🔴 **Suspiciune de infecție spinală / spondilodiscită (± abces epidural / paravertebral).**
   Absent complet — deși e o urgență diagnostică majoră. **IRM cu contrast (gadolinium)** =
   examenul de elecție (edem disco-vertebral, colecții epidurale); radiografia/CT pot fi normale
   în faza precoce (CT util pentru distrucția osoasă / ghidarea biopsiei); **scintigrafie cu
   leucocite marcate / PET-CT (FDG)** în cazuri selectate sau contraindicație IRM. Context de risc:
   diabet, consum de droguri i.v., cancer, HIV, dializă, imunosupresie, febră + VSH/CRP crescute.
   Home = subcapitolul general **„Coloană"** (poate afecta orice segment). Sursă: ACR *Suspected
   Spine Infection* (2021).
2. 🔴 **Sindrom de coadă de cal (cauda equina).** Azi „topit" ca red-flag în eticheta „Lombalgie
   cu semne de gravitate…" și în comentarii. ACR îl tratează ca **variantă distinctă, urgentă**.
   **IRM lombară de urgență** = gold standard; CT/mielo-CT dacă IRM e contraindicat. Fiind o urgență
   neurochirurgicală, merită **situație proprie** (vizibilitate). Home = **Coloană lombară**.
   De decis: situație separată vs. păstrare ca red-flag.
3. 🟠 **Coloană (lombară) operată — recidivă de hernie / „failed back surgery".** Azi doar
   menționat în comentarii („recidivele dureroase postoperatorii necesită IRM"). ACR are variantă
   dedicată (*LBP with prior lumbar surgery*). **IRM cu ȘI fără contrast** = tehnica de elecție —
   gadoliniul distinge **fibroza/cicatricea epidurală** (captează) de **hernia recidivată** (nu
   captează central); CT pentru evaluarea instrumentației/fuziunii. Home = **Coloană lombară**.
4. 🟠 **Suspiciune de spondilartrită axială / durere lombară de tip inflamator.** Avem „Sacro-
   ileită" centrată pe **radiografie**, dar abordarea modernă (ASAS) pornește de la **IRM articulații
   sacro-iliace** (edem osos subcondral pe STIR = sacroiliită activă precoce, radiografie încă
   normală), ± IRM coloană. De decis: situație dedicată **„Spondilartrită axială (durere de tip
   inflamator)"** cu IRM SI + coloană ca primă intenție, sau **îmbogățirea „Sacro-ileită"** cu IRM
   ca primă intenție la suspiciune clinică (radiografia rămânând pentru leziunile structurale
   tardive). Home = **Sacru** (sau nou subcapitol). Sursă: criteriile ASAS.

### 31.B Goluri cu home în alt capitol (nu se adaugă aici)

- **Suspiciune de tumoră spinală / metastaze vertebrale / compresie medulară malignă** →
  **Cancer** (ierarhie: malignitate cunoscută/suspectată). IRM cu contrast = primă intenție;
  „Sindrom medular netraumatic" din capitolul nostru acoperă compresia *non-tumorală*. De
  verificat completitudinea la **Cancer** (stadializare osoasă / metastaze vertebrale).
- **Anomalii congenitale ale coloanei / disrafism spinal / măduvă ancorată / scolioză la copil**
  → **Pediatrie** (aici exista un rând-breadcrumb „Afecțiuni congenitale", eliminat în runda 2).
- **Malformații vasculare spinale (MAV, fistulă durală arterio-venoasă) / ischemie medulară** →
  **Sistem nervos** (diagnostic: IRM + angio-IRM) și **RI** (angiografie/embolizare).
- **Vertebroplastie / cifoplastie, biopsie vertebrală percutană, infiltrații / blocaje** → deja la
  **RI › Aparat locomotor** (Tip `I`).

### 31.C Parțial acoperite — de îmbogățit (nu neapărat situație nouă)

- **Fractură vertebrală: diferențierea benign (osteoporotic) vs. malign (patologic).** „Bilanț
  fractură vertebrală spontană" o acoperă parțial; rolul **IRM** (secvențe de difuzie / chemical-
  shift pentru infiltrarea măduvei) în această diferențiere merită explicitat în comentariu (azi
  menționat sumar). Sursă: ACR *Management of Vertebral Compression Fractures*.
- **Mielopatie cervicală spondilotică.** „Sindrom medular netraumatic" o include, dar ar putea fi
  menționată explicit (cea mai frecventă cauză de mielopatie non-traumatică la adult; IRM cervical).
- **Osteoporoză — VFA (vertebral fracture assessment) prin DXA lateral** ca și complement al
  osteodensitometriei, pentru fracturi vertebrale morfometrice asimptomatice.

### 31.D Rânduri propuse — schiță pentru editori (NU sunt în `GHID.csv`)

Draft concret al situațiilor din 31.A, gata de studiat. **Gradele și dozele sunt orientative** —
deduse din rândurile analoge din capitol (IRM 0/0; CT 2/3; radiografie 1–2; scintigrafie 2/3;
PET-CT 4/4) + logica de primă intenție din ghiduri. **Se validează de editori înainte de orice
inserare.** Coloane fixe pentru toate: `Capitol = Coloană vertebrală`, `Terapeutic = Nu`,
`Alte informații =` (gol). Ordinea examenelor în fiecare situație = de la prima intenție în jos.

#### (1) Subcapitol „Coloană" — **Suspiciune de infecție spinală (spondilodiscită, abces epidural)** 🔴

| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentariu |
|---|---|---|---|---|---|
| M | IRM | Indicat | A | 0 / 0 | Examen de elecție, **cu substanță de contrast** (gadolinium): edem disco-vertebral, abces epidural/paravertebral, empiem. De realizat **în urgență** la deficit neurologic sau suspiciune de abces epidural. |
| G | Radiografie standard | Doar în cazuri particulare | B | 2 / 2 | Bilanț inițial; poate fi **normală în faza precoce** — pensarea discului și eroziunile platourilor apar după 2–3 săptămâni. |
| T | CT | Doar în cazuri particulare | B | 2 / 3 | Pentru distrucția osoasă și **ghidarea puncției-biopsii**; sensibilitate mai mică decât IRM precoce. |
| N | Scintigrafie cu leucocite radiomarcate | Doar cu aviz specializat | B | 2 / 3 | Când IRM e contraindicat/neconcludent. |
| N | PET-CT (F18-FDG) | Doar cu aviz specializat | B | 4 / 4 | Util în infecția cronică sau de material protetic; diferențiere de modificările degenerative. |

#### (2) Subcapitol „Coloană lombară" — **Sindrom de coadă de cal (cauda equina)** 🔴

| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentariu |
|---|---|---|---|---|---|
| M | IRM | Indicat | A | 0 / 0 | **Urgență neurochirurgicală.** IRM lombo-sacrată de urgență = gold standard (compresia sacului dural, hernie mediană masivă, proces expansiv). De realizat imediat. |
| T | CT / mielo-CT | Doar în cazuri particulare | B | 2 / 3 | Când IRM e contraindicat sau indisponibil; mielo-CT evidențiază compresia sacului dural. |

#### (3) Subcapitol „Coloană lombară" — **Rahialgie/radiculalgie după chirurgie lombară (recidivă de hernie vs. fibroză)** 🟠

| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentariu |
|---|---|---|---|---|---|
| M | IRM | Indicat | B | 0 / 0 | IRM **cu și fără gadolinium** = tehnica de elecție: fibroza/cicatricea epidurală **captează** contrastul, hernia recidivată **nu captează** central. |
| T | CT | Doar în cazuri particulare | B | 2 / 3 | Pentru evaluarea instrumentației/fuziunii și a complicațiilor osoase. |

#### (4) Subcapitol „Sacru" (sau subcapitol nou) — **Suspiciune de spondilartrită axială (durere lombară de tip inflamator)** 🟠

| Tip | Examen | Indicație | Grad | Doză Min/Max | Comentariu |
|---|---|---|---|---|---|
| M | IRM articulații sacro-iliace (± coloană) | Indicat | A | 0 / 0 | **Primă intenție** la suspiciune clinică (durere inflamatorie, HLA-B27): edem osos subcondral pe STIR = **sacroiliită activă precoce**, când radiografia e încă normală (criterii ASAS). |
| G | Radiografie de bazin / sacro-iliace | Doar în cazuri particulare | B | 1 / 2 | Pentru **sacroiliita structurală tardivă** (eroziuni, scleroză, anchiloză); normală în faza precoce. |
| T | CT sacro-iliace | Doar cu aviz specializat | B | 2 / 3 | Pentru leziuni structurale echivoce pe radiografie; iradiere mai mare. |

> ⚠️ **Suprapunere de rezolvat (situația 4):** se suprapune cu „Sacro-ileită" existentă (Sacru,
> radiografie-centric). De decis: (a) situație nouă „Spondilartrită axială" distinctă de
> „Sacro-ileită", sau (b) **îmbogățirea „Sacro-ileită"** mutând IRM ca primă intenție și
> reîncadrând radiografia pentru leziunile structurale tardive. Recomandare: (b), pentru a evita
> două situații cvasi-suprapuse.

> Status: **analiză, fără modificare de date.** Propunerile (inclusiv rândurile-schiță din 31.D)
> așteaptă decizia editorilor (ce se adaugă, cu ce grad/doză, unde se încadrează). Priorități:
> 🔴 = gol major (infecție spinală, cauda equina). Surse: ACR Appropriateness Criteria®
> (*Low Back Pain* 2021, *Suspected Spine Infection* 2021, *Myelopathy*, *Vertebral Compression
> Fractures*), RCR iRefer (ed. 8), criteriile ASAS pentru spondilartrita axială.

---

## 32. Aparat locomotor — chestiuni ridicate la review (2026-07-10)

Review complet al capitolului (74 de rânduri). Corecturile mecanice (diacritice, spații,
denumiri de examene) au fost **aplicate** — vezi `CHANGELOG.md §13 › REVIZUIT`. Punctele de
mai jos sunt **de încadrare / conținut** și rămân deschise (fără modificare de date).

### 32.A ✅ „Nevralgie cervico-brahială" încadrată la subcapitolul „Umăr"

> ✅ **REZOLVAT (2026-07-10, la cerere) — mutat la Coloană cervicală, cu reconciliere.** La mutare
> s-a descoperit că **Coloană vertebrală › Coloană cervicală conținea deja o situație omonimă**
> „Nevralgie cervico-brahială" (CT, IRM, Radiografie standard), cu **grade identice** pe cele 3
> modalități suprapuse. Deci nu s-a făcut mutare oarbă, ci **comasare**: rândurile CT/IRM/G din
> Aparat locomotor au fost eliminate (duplicau existentul canonic), iar singurul conținut nou —
> **Mielo-CT** — a fost relocat în grupul cervical. Niciun grad schimbat. Vezi `CHANGELOG.md
> §13 › MUTAT/COMASAT` și `§12 › ADĂUGAT`. Găuri NR.CRT: 1154, 1156, 1157.

Situația **„Nevralgie cervico-brahială"** (NR 1154–1157) stă în subcapitolul **Umăr**, dar
toate examenele ei vizează **coloana cervicală** (CT coloană cervicală, Mielo-CT, IRM coloană
cervicală, Radiografie coloană cervicală) — patologie de **radiculopatie cervicală**, nu de
umăr. Per ierarhia de capitole, home-ul „anatomic" ar fi **Coloană vertebrală › Coloană
cervicală**. Motivul plasării actuale e clinic (nevralgia cervico-brahială e un **diagnostic
diferențial al umărului dureros**), dar datele nu poartă breadcrumb-uri (regula „un singur
home"). **De decis:** (a) rămâne la Umăr ca fațetă de diagnostic diferențial, sau (b) se mută
la Coloană vertebrală › Coloană cervicală (unde există deja „Cervicalgii comune", „Nevralgie
cervico-brahială" ar fi vecina firească). Recomandare slabă: (b) — situația e integral
cervico-vertebrală. **Lăsată neatinsă.**

### 32.B ✅ „Fasceita plantară" în „Diverse" vs. subcapitolul „Picior"

> ✅ **REZOLVAT (2026-07-10, la cerere) — mutat la „Picior".** Cele 4 rânduri „Fasceita plantară"
> relocate din „Diverse" în subcapitolul „Picior" (lângă „Halux valgus"), ordinea examenelor
> păstrată, NR.CRT neschimbate. „Diverse" păstrează doar condițiile sistemice/cross-regiune.
> Vezi `CHANGELOG.md §13 › MUTAT/COMASAT`.

Subcapitolul **Picior** conține o singură situație reală (**„Halux valgus"**, NR 1140) + rândul
placeholder Tip `Z`. În același timp, **„Fasceita plantară"** (NR 1106–1109) — patologie strict
a piciorului — stă în subcapitolul-coș **„Diverse"**. **De decis:** consolidarea patologiei de
picior sub „Picior" (mutarea „Fasceita plantară" din „Diverse" la „Picior"). Nu s-a mutat
unilateral — „Diverse" grupează și alte enteziopatii, iar granița „coș sistemic vs. subcapitol
de regiune" e o alegere editorială. (Restul din „Diverse" — artropatie inflamatorie, osteomalacie,
osteomielită, sindrom dureros post-protezare — sunt condiții **sistemice / cross-regiune**, deci
„Diverse" pare un coș legitim pentru ele.)

### 32.C ⏳ Acoperire subțire a capitolului (posibil audit de conținut viitor)

Capitolul are subcapitole doar pentru **Genunchi, Șold, Umăr, Picior** (+ „Diverse"). Lipsesc
regiuni MSK frecvent indicate în ghiduri (ACR AC / RCR iRefer): **pumn / mână** (sindrom de tunel
carpian, suspiciune de scafoid), **cot**, **gleznă / picior** (entorsă, reguli Ottawa),
**tumori de părți moi** (masă palpabilă — parțial mutate la Cancer). Nu e o eroare de date, ci un
**gol de conținut** — de evaluat într-un audit dedicat față de ghidurile de referință (analog
secțiunilor de „goluri de conținut" ale altor capitole), dacă editorii doresc extinderea
capitolului. **Nesemnalat ca sarcină acum** — doar consemnat.

> Status: **analiză, fără modificare de date.** Sursele pentru un eventual audit: ACR
> Appropriateness Criteria® (musculoskeletal), RCR iRefer (ed. 8).

---

## 33. Aparat locomotor — consolidare situații (2026-07-10, la cerere)

Analiză de deduplicare/consolidare pe tot capitolul (inclusiv cross-subcapitol). Concluzie:
capitolul e în mare curat — cele 3 gonalgii (gonartroză / meniscală / femuro-patelară), cele 2
afecțiuni de șold (coxalgie / necroză aseptică) și condițiile din „Diverse" (artropatie
inflamatorie, osteomalacie, osteomielită, sindrom post-protezare) sunt **clinic distincte**, nu
dubluri. Un singur duplicat real:

### 33.A ✅ „Patologia umărului" ≡ „Umăr dureros" — COMASAT (decizie de grad luată la cerere)

Aceeași situație (umăr dureros / coafa rotatorilor), aceleași 5 modalități. Gradele coincideau pe
Ecografie/Radiografie/IRM; difereau doar la **Artro-IRM/Artro-CT**: „Doar cu aviz specializat"/B
(Patologia umărului) vs „Neindicat în primă intenție"/C (Umăr dureros). **Decizie (la cerere):**
comasare sub „Umăr dureros" cu artrografia la **„Doar cu aviz specializat"/B** — consecvent cu
restul subcapitolului Umăr (și „Umăr dureros instabil" o are la B; artrografia de umăr e o
procedură invazivă, specialist-directed). Comentariile mai bogate păstrate; nota „umăr hiperalgic"
portată pe rândul radiografiei. „Umăr dureros instabil" rămâne distinctă. Vezi `CHANGELOG.md §13 ›
ELIMINAT/COMASAT — consolidare situații umăr`. (−5 rânduri.)

> Nota de trasabilitate pe grade: nu s-a „inventat" un grad — s-a **ales între cele două grade
> deja existente** pe aceeași modalitate, aliniat la convenția dominantă a subcapitolului. Restul
> gradelor rămân neatinse.

---

## 34. Aparat locomotor — goluri de conținut față de ghidurile de referință (2026-07-10)

Audit al capitolului față de **ACR Appropriateness Criteria®** (panel Musculoskeletal) și **RCR
iRefer (ed. 8)**, căutând situații **non-traumatice** care ar trebui neapărat prezente și lipsesc.
Filtre de încadrare (ierarhia GIRI): leziunile **acut-traumatice** (entorsă acută de gleznă,
fractură de scafoid, genunchi acut — reguli Ottawa/NEXUS) merg la **Traumatisme**, nu aici;
**tumorile osoase / masele de părți moi / metastazele** merg la **Cancer** (mutate deja); deci
NU sunt goluri ale acestui capitol. Propunerile de mai jos sunt **non-traumatice, non-tumorale**.

> Status: **analiză, fără modificare de date.** Rândurile-schiță (modalități, indicație, grad,
> doză, comentariu) sunt **propuneri** — gradele/dozele se confirmă de editori. Priorități:
> 🔴 = gol major (topic ACR/RCR dedicat, regiune întreagă absentă); 🟠 = recomandat; 🟢 = opțional.

### 34.A 🔴 Regiuni MSK absente complet (topicuri ACR AC dedicate)

Capitolul are subcapitole doar pentru Genunchi, Șold, Umăr, Picior (+ „Diverse"). Lipsesc trei
regiuni cu topic ACR AC propriu (*Chronic Wrist Pain*, *Chronic Elbow Pain*, *Chronic Ankle Pain*):

#### (1) Subcapitol nou **„Pumn și mână"** — *Durere cronică de pumn / mână*
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| G | Radiografie | Indicat | B | 1/1 | Primă intenție: artroză, condrocalcinoză, aliniament, sechele. |
| M | IRM | Doar cu aviz specializat | B | 0/0 | Leziuni TFCC, ligament scafo-lunar, necroză (Kienböck/scafoid), sinovită. |
| M | Artro-IRM | Doar cu aviz specializat | C | 0/0 | Leziuni ligamentare intrinseci / TFCC când IRM nativ e neconcludent. |
| E | Ecografie | Doar în cazuri particulare | C | 0/0 | Tenosinovite, ganglioni, **sindrom de tunel carpian** (nerv median). |
| T | CT | Doar în cazuri particulare | C | 1/1 | Pseudartroză de scafoid, aliniament osos, corpi liberi. |

#### (2) Subcapitol nou **„Cot"** — *Durere cronică de cot / epicondilită*
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| G | Radiografie | Indicat | B | 1/1 | Primă intenție: artroză, corpi liberi, osteocondrită disecantă. |
| E | Ecografie | Indicat | C | 0/0 | Epicondilită, patologie tendinoasă, colecții, nerv ulnar. |
| M | IRM | Doar cu aviz specializat | B | 0/0 | Tendinopatii, leziuni ligamentare/osteocondrale, neuropatie ulnară. |

#### (3) Subcapitol nou **„Gleznă"** — *Durere cronică de gleznă / instabilitate*
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| G | Radiografie (cu încărcare) | Indicat | B | 1/1 | Primă intenție: artroză, aliniament, sechele post-traumatice. |
| M | IRM | Doar cu aviz specializat | B | 0/0 | Leziuni osteocondrale, tendinoase (ahilian/peronieri), ligamentare, impingement. |
| E | Ecografie | Doar în cazuri particulare | C | 0/0 | Patologie tendinoasă, sinovită, ghidaj infiltrații. |
| T | CT | Doar în cazuri particulare | C | 1/2 | Coaliție tarsală, leziuni osoase/osteocondrale, aliniament. |

### 34.B 🔴 Osteoporoză — evaluarea densității minerale osoase (DXA)

Cea mai frecventă indicație imagistică MSK metabolică **lipsește ca situație** (osteodensitometria
apare doar incidental sub „Osteomalacie"). DXA centrală (coloană + șold) e metoda standard de
diagnostic și de estimare a riscului de fractură (clinician's guide NOF/BHOF; ISCD). Home propus:
**„Diverse"** (sistemic).
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| D | Osteodensitometrie (DXA coloană + șold) | Indicat | A | 1/1 | Diagnostic (T-scor ≤ −2,5) și estimarea riscului de fractură; monitorizare la 1–2 ani. |
| G | Radiografie coloană toraco-lombară (morfometrie / VFA) | Doar în cazuri particulare | B | 1/1 | Detectarea fracturilor vertebrale de fragilitate. |
| T | CT (QCT) | Doar cu aviz specializat | B | 2/3 | În cazuri selectate; iradiere mai mare decât DXA. |

### 34.C 🟠 Situații recomandate (topic dedicat, dar de prioritate a doua)

- **Artrită septică** (home „Diverse") — distinctă de osteomielită (ACR: *Suspected Osteomyelitis,
  Septic Arthritis…*). Rg + **Ecografie** (epanșament, ghidaj puncție articulară — cheia
  diagnosticului) + IRM (extensie osoasă/părți moi).
- **Fractură de stres / insuficiență** (home „Diverse" sau pe regiune) — suprasolicitare, **non-acut
  traumatică** (topic ACR *Stress (fatigue/insufficiency) fracture*). Rg (adesea normală precoce) +
  **IRM** (cea mai sensibilă) + scintigrafie osoasă (alternativă).
- **Durere cronică de picior extinsă** (în „Picior", pe lângă Halux/Fasceită) — nevrom Morton,
  metatarsalgie, disfuncție de tendon tibial posterior: **Ecografie / IRM**.

### 34.D 🟢 Opțional (de completat dacă se dorește acoperire exhaustivă)

- **Sindrom dureros de trohanter mare** / bursită trohanteriană (în „Șold") — Eco / IRM.
- **Boala Paget osoasă** (în „Diverse") — Radiografie + scintigrafie osoasă.
- **Artropatie microcristalină / gută** (extindere a „Artropatie inflamatorie") — **DECT** (CT
  dual-energy) pentru depozitele de urat.

> Surse: ACR Appropriateness Criteria® — *Chronic Wrist Pain*, *Chronic Elbow Pain*, *Chronic
> Ankle Pain*, *Chronic Foot Pain*, *Osteonecrosis*, *Stress (fatigue/insufficiency) fracture*,
> *Suspected Osteomyelitis, Septic Arthritis, or Soft Tissue Infection*; RCR iRefer (ed. 8), secțiunea
> musculo-scheletală; clinician's guide to prevention and treatment of osteoporosis (BHOF/NOF) și
> ISCD pentru DXA. **Nimic adăugat în `GHID.csv`** — se decid în echipă situațiile păstrate,
> gradele, dozele și încadrarea (subcapitole noi: Pumn și mână, Cot, Gleznă).

---

## 35. Aparat locomotor — topicuri prezente, de îmbogățit față de ghiduri (2026-07-10)

Complementar §34 (topicuri absente): audit al situațiilor **deja prezente**, comparând setul de
modalități cu ACR AC / RCR iRefer, pentru a găsi ce le lipsește. Concluzie generală: majoritatea
situațiilor sunt **bine acoperite**; un singur gol clar + două minore.

> Status: **analiză, fără modificare de date.** Rândurile-schiță = propuneri; gradele/dozele se
> confirmă de editori.

### 35.A 🟠 „Sindrom dureros post protezare" — lipsește IRM (cu reducerea artefactelor metalice)

Situația are Rg, Ecografie, PET-CT, scintigrafie osoasă, CT — dar **nu IRM**. ACR *Imaging After
Total Hip/Knee Arthroplasty* clasează **IRM nativ** ca „usually appropriate" pentru: mobilizare/
osteoliză periprotetică, **reacție adversă la debriuri metalice** (proteze metal-on-metal) și
infecție periprotetică. Necesită secvențe de **reducere a artefactelor metalice (MARS/MAVRIC)**.
Propunere (consecvent cu celelalte modalități avansate din situație, toate B/„Doar cu aviz"):
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| M | IRM (cu reducerea artefactelor metalice) | Doar cu aviz specializat | B | 0/0 | Osteoliză/mobilizare periprotetică, reacție adversă la debriuri metalice (metal-on-metal), infecție. Secvențe MARS/MAVRIC. |

> (Puncția articulară ghidată imagistic pentru infecție = **procedură intervențională** → home la
> RI › Aparat locomotor, nu aici.)

### 35.B 🟢 „Necroza aseptică de cap femural" — CT ca alternativă la IRM contraindicat

Are IRM (etalon), Radiografie, PET-CT, scintigrafie. ACR *Osteonecrosis*: când **IRM e
contraindicat**, **CT** sau scintigrafia osoasă cu SPECT sunt alternative (CT util și pentru
evaluarea fracturii subcondrale / colapsului articular pre-operator). Lipsește CT:
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| T | CT | Doar în cazuri particulare | C | 2/3 | Alternativă la IRM contraindicat; evaluarea fracturii subcondrale / colapsului capului femural. |

### 35.C 🟢 „Osteomielită – suspiciune" — notă de graniță: piciorul diabetic

Situația e bine acoperită (Rg, IRM, PET-CT, scintigrafie ± leucocite marcate, CT, Eco). ACR tratează
**osteomielita piciorului diabetic** ca scenariu distinct (IRM = etalon; complicații particulare).
De decis dacă se adaugă o situație separată „Osteomielita piciorului diabetic" sau rămâne acoperită
generic. **Nedecis** — flag.

### 35.D ✅ Situații verificate — acoperire bună (fără modificare propusă)

- **Coxalgie** — Rg primă intenție + IRM/Eco second-line + Artro-IRM (labrum/FAI). Conform ACR
  *Chronic Hip Pain* (IRM/US „usually appropriate" ca pas următor după Rg negativă).
- **Gonalgii (gonartroză / meniscală / femuro-patelară)** — Rg (de preferat cu încărcare) + IRM
  pentru OCD/corpi liberi/menisc + CT (măsurători femuro-patelare). Conform ACR *Chronic Knee Pain*.
- **Umăr dureros / instabil** — Rg + Ecografie + IRM + Artro-IRM/Artro-CT. Conform ACR *Shoulder Pain*
  (Eco și IRM ambele adecvate pentru coafa rotatorilor).
- **Artropatie inflamatorie (bilanț / monitorizare)** — Rg + Eco (Doppler) + IRM (sinovită/edem osos)
  + CT + scintigrafie. Conform ACR *Chronic Extremity Joint Pain – Suspected Inflammatory Arthritis*.
- **Osteomalacie** — Rg + scintigrafie + DXA + PET-CT + scintigrafie cu analogi de somatostatină
  (osteomalacie oncogenă). Acoperire completă.
- **Fasceita plantară** — Ecografie (primă intenție) + IRM + Rg + scintigrafie. Conform ACR *Chronic
  Foot Pain*.

> Surse: ACR Appropriateness Criteria® — *Imaging After Total Hip Arthroplasty* (2023), *Imaging
> After Total Knee Arthroplasty* (2023), *Osteonecrosis of the Hip*, *Chronic Hip Pain* (2022),
> *Chronic Knee Pain*, *Chronic Extremity Joint Pain – Suspected Inflammatory Arthritis*, *Suspected
> Osteomyelitis, Septic Arthritis…*; RCR iRefer (ed. 8). **Nimic adăugat în `GHID.csv`.**

---

## 36. GLOBAL — textele multi-linie (de decis/uniformizat la final, pe tot fișierul)

Sarcină **cross-capitol**, de rulat **la sfârșit** (nu pe un capitol anume). În `GHID.csv` există
câmpuri cu newline interne (`\n`), de două feluri, cu tratament diferit:

**(a) Denumiri de examene (col. Examen) — newline PARAZIT, de aplatizat.** 17 rânduri, toate
aceeași denumire de scintigrafie osoasă spartă pe 3 linii:
`Scintigrafie osoasă\n(99mTc- HDP, 99mTc-HMDP, 99mTc-MDP) WB și\nSPECT-CT`. Newline-urile nu poartă
informație — sunt un artefact de formatare din sursă. **Propunere:** aplatizare la o singură linie
(`Scintigrafie osoasă (99mTc- HDP, 99mTc-HMDP, 99mTc-MDP) WB și SPECT-CT`) pe tot fișierul. Tot
atunci: normalizarea celor **2 rânduri rămase cu `WB si`** (fără diacritică, în alte capitole) →
`WB și`, și varianta cu sufix „, Scintigrafie cu leucocite marcate" (Aparat locomotor › Picior).
Impact: uniformizează denumirea + reduce diff-ul viitor. (Nu s-a făcut acum ca să nu ating rânduri
din alte capitole în cadrul reviewului Aparat locomotor.)

**(b) Comentarii structurate (col. Comentarii) — newline SEMNIFICATIV, de păstrat.** 11 rânduri cu
note clinice pe mai multe paragrafe/liste (ex. PECARN traumatism cranian pediatric; urmărirea
nodulilor pulmonari; criterii de trombectomie mecanică; criterii endovascular/clipare anevrism;
tratamentul vasospasmului). Aici newline-ul structurează liste și criterii — **NU se aplatizează**
(aplatizarea ar face textul ilizibil). **De decis la final:** o convenție unică de formatare (ex.
marcaje de listă consecvente, fără spații parazite înainte de `\n`), nu ștergerea structurii.

> Status: **doar consemnat** — nicio modificare acum. De executat ca pas global, după terminarea
> reviewului pe capitole (înainte de/împreună cu o eventuală renumerotare finală).

---

## 37. Cap › Neuro — comentariu mis-asignat la „Probleme psihiatrice" (2026-07-10)

Ridicat la reviewul capitolului Cap.

**Rând:** NR 989 · Cap › Neuro · „Probleme psihiatrice" · Tip M · „IRM cerebral" · Indicat ·
grad C.

**Problema.** Comentariul de la NR 989 este, cuvânt cu cuvânt, textul de la NR 993 („Scleroza
în plăci și alte leziuni ale substanței albe"):

> _„De prima intenție pentru diagnosticul pozitiv, pentru monitorizarea afecțiunii de substanță
> albă și pentru diagnosticul diferențial. Poate fi completat cu IRM medular dacă nu sunt
> completate criteriile de diagnostic sau pentru diagnosticul diferențial."_

Textul descrie monitorizarea substanței albe și completarea cu IRM medular (criterii de tip
McDonald) — specific sclerozei multiple, **fără legătură cu explorarea IRM în tulburările
psihiatrice**. Aproape sigur un copy-paste din rândul-soră NR 993. (Rândul-pereche CT, NR 990,
are un comentariu corect, psihiatric: contraindicații IRM / excluderea unei tumori frontale.)

**De decis:** conținutul clinic corect al comentariului IRM pentru „Probleme psihiatrice" (ce
rol are IRM-ul cerebral în bilanțul unei tulburări psihiatrice — ex. excluderea unei cauze
organice, primă intenție vs. la nevoie). **Nu s-a modificat** — e conținut clinic, nu typo.

---

## 38. Cap — structura pe subcapitole (Neuro / ORL) și granularitatea (2026-07-10)

Ridicat de editor: e corectă împărțirea Neuro/ORL? S-ar putea sparge Neuro în subcapitole
independente (pe boală)?

**Situație actuală:** `Cap` are 2 subcapitole — **Neuro** (23 situații, 56 rânduri) și
**ORL** (10 situații, 23 rânduri).

**Analiză (stilul casei).** Cele 95 de subcapitole ale ghidului se împart **anatomic
(organ/regiune)**, niciodată pe boală. Subcapitolele mono-sistem mari sunt ținute **întregi**:
`Torace › Pulmon` (27 situații), `Aparat cardiovascular › Cord` (21). `Cap › Neuro` (23) e în
aceeași ligă — un sistem (SNC: encefal + măduvă + vase cerebrale + nervi cranieni) ținut întreg.
Unde ghidul sparge fin (Coloană, Aparat locomotor, Aparat digestiv), axa e **regională**, nu pe
boală.

**Ghiduri de referință.** ACR Appropriateness Criteria are două panel-uri separate —
**„Neurologic Imaging"** (stroke, headache, head trauma, neuroendocrin/hipofiză, demență…) și
**„Head and Neck Imaging"** (ORL) — și pune **direct condiția clinică** sub panel, fără nivel
intermediar de „grup de boli". Maparea `panel → topic` e identică cu `Neuro/ORL → situație`.
RCR iRefer e organizat regional (Head cuprinde neuro; ORL ca „Head and neck").

**Recomandare (de confirmat de editori):**

1. **Se păstrează împărțirea Neuro / ORL** — se suprapune peste panel-urile ACR și e o graniță
   anatomică/de specialitate reală.
2. **NU se sparge Neuro în subcapitole pe boală** — ar fi singurul caz de subcapitolizare pe
   boală într-un capitol anatomic, inconsecvent cu Cord/Pulmon (ținute întregi) și cu structura
   ACR (condiții direct sub panel).
3. **Alternativa pentru navigabilitate:** reordonarea **situațiilor** pe flux clinic în interiorul
   Neuro (checklist pasul 7) — grupare fizică a blocurilor (AVC / cefalee / epilepsie /
   neurodegenerativ-cognitiv / neuroinflamator-infecțios / tumoral-selar / hidrocefalie / medular /
   neuro-oftalmologic / bază craniu-nervi cranieni), `ALTĂ` ultima. Dă gruparea fără axă nouă.
   **De decis dacă se aplică** (reordonare fizică, NR.CRT neschimbate).
4. **Minor / cosmetic:** „Neuro" și „ORL" sunt singurele etichete de tip jargon de specialitate
   din ghid (restul subcapitolelor sunt anatomice). Opțional, redenumire consecventă
   („Sistem nervos" / „Sferă ORL" sau „Ureche, nas, sinusuri").

**Note de încadrare conexe:** ATM (articulație, azi în ORL) — vezi §1 (posibil Aparat locomotor);
„Sindroame medulare" (măduvă, azi în Neuro) — de confirmat dacă rămâne în Cap sau se raportează
la Coloană vertebrală.

---

## 39. Cap — chestiuni ridicate la reviewul de conținut, pasul 2 (2026-07-10)

✅ **Rezolvat (2026-07-10, la cerere) — toate cele 3 loturi aplicate** (vezi `CHANGELOG.md` §10,
„Review Cap, pasul 3"): (a) notele de nivel-situație propagate pe investigațiile-soră (ATM,
sinuzită acută, olfactiv, ureche medie); (b) etichetele „IRM regiune cervicală" corectate
anatomic (NR 1022 → conduct auditiv intern/unghi ponto-cerebelos; NR 1010 → sinusuri și fose
nazale); (c) justificări adăugate pe „Neindicat" (NR 1009, 1020). _Rămân de verificat de
editori:_ formulările nou-scrise la (b) și (c) (corecții/justificări standard, dar autorate în
review, nu preluate din sursă). Detaliile inițiale mai jos.

Ridicate la a doua trecere pe Neuro + ORL (după mutarea notelor clinice din col. 10 în col. 9).

### (a) Propagarea notelor de nivel-situație pe toate investigațiile

Per regula „informația clinică de nivel-situație se copiază pe toate investigațiile situației"
(`CLAUDE.md` › Decizii), câteva note mutate din `Alte informații` descriu **situația în general**
(nu o modalitate anume) și, în prezent, stau doar pe un rând. Candidate de propagat pe toate
rândurile situației:

- **Disfuncții ATM** (NR 1006–1009): „Analiza simptomatologiei și examenul clinic și dentar
  trebuie să preceadă imagistica. Examenul imagistic trebuie să aibă indicație…" (acum doar pe
  NR 1006, Ortopantomografie).
- **Sinuzită acută** (NR 1015–1017): „Diagnosticul este clinic, uneori confirmat prin endoscopie.
  Imagistica este indicată doar în cazuri atipice, cu complicații sau în caz de eșec terapeutic."
  (acum doar pe NR 1016, CT).
- **Tulburări ale simțului olfactiv** (NR 1024–1025): „Indicația imagisticii este doar după
  realizarea unui examen clinic ORL detaliat." (acum doar pe NR 1025, CT).
- **Simptomatologia urechii medii** (NR 1013–1014): „Tumorile urechii medii… necesită examinare
  IRM și CT în egală măsură." (acum doar pe NR 1014, IRM) — de decis dacă e nivel-situație.

**De decis:** care sunt strict nivel-situație (se propagă) vs. specifice modalității (rămân). Nu
s-a propagat automat (dublează text; decizie de conținut).

### (b) Etichete de examen cu nepotrivire anatomică

- **NR 1022** — „Surditatea neurosenzorială la adult" → Examen „**IRM regiune cervicală**".
  Surditatea neurosenzorială se explorează prin IRM de conduct auditiv intern / unghi
  ponto-cerebelos, nu „regiune cervicală". Probabil artefact din sursă.
- **NR 1010** — „Leziuni tumorale… ale foselor nazale și sinusurilor" → „**IRM regiune
  cervicală**" (ar fi de așteptat „IRM masiv facial / sinusuri").
- Minor: rândurile de ureche (NR 1004, 1005, 1012, 1013, 1014) au Examen generic „IRM"/„CT"
  fără regiune, spre deosebire de restul capitolului („CT sinusuri", „IRM sinusuri").

**De decis:** corectarea denumirii examenului (schimbă ținta descrisă → conținut, nu se face
unilateral).

### (c) Rânduri „Neindicat" fără justificare

- **NR 1009** — Radiografie articulații temporo-mandibulare, „Neindicat", grad „?", `Comentarii`
  gol.
- **NR 1020** — Ortopantomografie la „Sinuzită cronică", „Neindicat", grad „?", `Comentarii` gol.

Comparativ, celelalte „Neindicat" din capitol au o notă (ex. NR 1017, 1021). **De decis:** dacă
se adaugă o justificare scurtă (conținut → editorii).

---

## 40. Stenoza carotidiană asimptomatică — încadrare + duplicate cross-capitol (2026-07-10)

✅ **Decizie luată (2026-07-10):** partea **diagnostică rămâne în Cap › Neuro** (opțiunea A).
Stub-ul din Cardiovascular (NR 663, „Suflu carotidian asimptomatic", doar Eco-Doppler) a fost
**comasat** în versiunea Neuro (NR 998–1000): partea descriptivă utilă a comentariului lui 663
a fost portată pe NR 998; rândul 663 eliminat. Gradul Eco-Doppler rămâne **A** (versiunea Neuro
păstrată; stub-ul avea B). ⏳ **Amânat (la cerere):** consolidarea **intervenționalului RI**
(problema 2 de mai jos) — carotida apare și la RI › Aparat cardiovascular, și la RI › Sistem
nervos.

**Context (analiza inițială) — topicul era fragmentat pe 4 locuri:**

**Diagnostic:**
- **Cap › Neuro** — „Stenoza carotidiană asimptomatică (suflu) – diagnostic" (NR 998–1000):
  Eco-Doppler (grad A), Angio-IRM (B), Angio-CT (B). *Cea mai completă versiune.*
- **Aparat cardiovascular › Sistem vascular** — „Suflu carotidian asimptomatic" (NR 663):
  Eco-Doppler (grad B). *Un singur rând — duplicat parțial al celui de mai sus.*

**Intervențional (RI):**
- **RI › Aparat cardiovascular** — „Stenoză carotidiană asimptomatică" (NR 1226 arterografie,
  1227 angioplastie) + „…simptomatică" (NR 1228 angioplastie).
- **RI › Sistem nervos** — „…(suflu) – tratament" (NR 1383 angioplastie cu stent) + „…(suflu)
  – diagnostic" (NR 1384 arterografie).

**Probleme:**
1. **Duplicat diagnostic** Neuro (NR 998–1000) ≡ Cardiovascular (NR 663) — același topic, două
   home-uri. Încalcă „un singur home per rând".
2. **Fragmentare intervențională** — carotida apare și la RI › Aparat cardiovascular, și la
   RI › Sistem nervos (NR 1227 ≈ 1383 angioplastie; NR 1226 ≈ 1384 arterografie) — duplicate
   interne RI.

**Recomandare (de confirmat):** un **singur home** pentru carotidă. Două opțiuni:
- **(A) Neuro/cerebrovascular** *(recomandarea mea)* — restul workup-ului de trunchiuri
  supraaortice / vascularizație cerebrală e deja în Cap › Neuro (AVC extracranian NR 950–952,
  AVCT trunchiuri NR 959–961). Stenoza carotidiană asimptomatică e capătul de screening al
  aceluiași continuum de prevenție a AVC; ACR o clasează la „Cerebrovascular Disease". → se
  **elimină/comasează** stub-ul NR 663 din Cardiovascular în versiunea Neuro (mai bogată).
- **(B) Cardiovascular › Sistem vascular** — carotida = arteră sistemică; subcapitolul găzduiește
  deja topicul. → se mută NR 998–1000 din Neuro aici, comasat cu NR 663.

În ambele cazuri: aliniat și **RI** (carotida intervențională într-un singur subcapitol — cardio
sau neuro — nu ambele). Nedecis unilateral (încadrare cross-capitol + comasare de duplicate).

---

## 41. Cap — goluri de conținut față de ghidurile de referință (ACR AC, iRefer) — propuneri (2026-07-10)

Audit al capitolului Cap (Neuro + ORL) față de **ACR Appropriateness Criteria®** (panelurile
*Neurologic Imaging* și *Head and Neck Imaging*) și **RCR iRefer (ed. 8)**, căutând situații
care ar trebui prezente și lipsesc sau sunt subțiri.

**Filtre de încadrare (ierarhia GIRI) — NU sunt goluri ale acestui capitol:** traumatismul
cranio-cerebral / facial → **Traumatisme**; tumorile cerebrale/medulare, metastazele, meningiomul,
schwannomul vestibular *ca stadializare/urmărire oncologică* → **Cancer** (menționate aici doar ca
diagnostic diferențial); masa cervicală / tiroida / glandele salivare / laringele → **Gât (părți
moi)**; stenoza carotidiană → deja acoperită (Neuro, §40).

> Status: **analiză, fără modificare de date.** Rândurile-schiță (modalități, indicație, grad,
> doză, comentariu) sunt **propuneri** — gradele/dozele se confirmă de editori și de sursa primară.
> Priorități: 🔴 = gol major (topic ACR/RCR dedicat, entitate întreagă absentă); 🟠 = recomandat;
> 🟢 = opțional.

### 41.A Neuro

#### (N1) 🔴 Anevrism intracranian nerupt / malformație vasculară (MAV, fistulă durală) — depistare & urmărire
_ACR AC „Cerebrovascular Diseases — Aneurysm, Vascular Malformation, and Subarachnoid Hemorrhage"._
Azi capitolul acoperă doar **ruptura** (prin „Cefalee acute brutale" → HSA). Lipsesc depistarea/
screeningul anevrismului **nerupt** și urmărirea, plus MAV / fistula durală. Home: **Cap › Neuro**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| M | Angio-IRM (TOF) cap | Indicat | B | 0/0 | Depistare/urmărire anevrism nerupt; screening la risc înalt (≥ 2 rude gr. I cu anevrism/HSA, boală polichistică renală autosomal dominantă). Neiradiant, fără contrast. |
| T | Angio-CT poligon Willis | Indicat | B | 2/3 | Caracterizare pre-terapeutică (dimensiune, col, calcificări); sensibil pentru anevrisme ≥ 3 mm și pentru MAV/fistulă. |
| M | Angio-IRM cu contrast + secvențe vasculare | Doar cu aviz specializat | B | 0/0 | MAV / fistulă arterio-venoasă durală: angioarhitectură, drenaj venos. |

_(Arteriografia DSA = standard de referință, dar Tip `A` → **RI**.)_

#### (N2) 🟠 Tromboză venoasă cerebrală (TVC)
_ACR AC (stroke-related)._ Azi doar **menționată** în comentarii (cefalee progresive), fără situație
proprie. Home: **Cap › Neuro**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| M | IRM cerebral + veno-IRM (2D-TOF / cu contrast) | Indicat | B | 0/0 | Suspiciune TVC: cefalee progresivă, hipertensiune intracraniană, crize, deficite fluctuante, context protrombotic/post-partum. Evidențiază trombul + infarctul venos/hemoragia. |
| T | Veno-CT (angio-CT în timp venos) | Indicat | B | 2/3 | Alternativă în urgență / IRM indisponibil; sensibilă pentru sinusurile durale. |

#### (N3) 🔴 Alterarea acută a stării de conștiență / comă / delir (encefalopatie acută)
_ACR AC „Altered Mental Status, Coma, Delirium, and Psychosis" (2024)._ Distinct de „Probleme
psihiatrice" (cronic) și „Probleme cognitive" (demență). Home: **Cap › Neuro** (bloc acut).
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| T | CT cerebral fără contrast | Indicat | B | 2/2 | Primă intenție în urgență: exclude hemoragie, efect de masă, hidrocefalie, infarct extins. |
| M | IRM cerebral | Indicat | B | 0/0 | CT neconcludent / suspiciune encefalită sau encefalopatie (difuzie: ischemie, status epileptic, cauze metabolice/toxice, PRES, encefalită autoimună). |

#### (N4) 🟠 Ataxie / sindrom cerebelos
_ACR AC „Ataxia"._ Home: **Cap › Neuro**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| M | IRM cerebral (accent fosă posterioară), cu și fără contrast | Indicat | B | 0/0 | Examen de elecție: atrofie cerebeloasă, leziune structurală/demielinizantă, sdr. paraneoplazic, malformație (Chiari). |
| T | CT cerebral | Doar în cazuri particulare | C | 2/2 | Doar dacă IRM contraindicat/indisponibil; sensibilitate limitată în fosa posterioară. |

#### (N5) 🟠 Paralizie facială periferică / neuropatie craniană izolată
_ACR AC „Cranial Neuropathy"._ Completează „Afectarea bazei craniului și nervilor cranieni"
(generic). Home: **Cap › Neuro**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| M | IRM cerebral + conduct auditiv intern + stâncă temporală, cu contrast | Doar în cazuri particulare | B | 0/0 | Paralizie facială **atipică, recurentă, progresivă sau fără recuperare la 2–4 luni**. Paralizia Bell tipică NU se imagistică de rutină. Traiect CN VII (trunchi cerebral → parotidă). |
| T | CT stâncă temporală și bază de craniu | Doar în cazuri particulare | C | 2/3 | Context traumatic/otologic (canal facial, dehiscențe, eroziuni). |

#### (N6) 🟠 Fistulă de LCR (rinoree / otoree de LCR)
_ACR AC „Cerebrospinal Fluid Leak"._ Interfață cu ORL, dar defectul e al **bazei craniului**.
Home propus: **Cap › Neuro**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| T | CT în strat subțire al bazei craniului / sinusurilor (înaltă rezoluție) | Indicat | B | 2/3 | Localizarea defectului osos. |
| M | Cisterno-IRM (T2 înaltă rezoluție) | Indicat | B | 0/0 | Confirmarea traiectului fistulos, meningo-/encefalocel; neiradiant. |
| X | Cisternografie CT cu contrast intratecal | Doar cu aviz specializat | C | 3/4 | Cazuri neconcludente / fistulă intermitentă (procedură invazivă). |

### 41.B ORL

#### (O1) 🔴 Tinitus pulsatil
_ACR AC „Tinnitus" (forma pulsatilă)._ Distinct de „Simptomatologia urechii interne (vertij,
acufene)" (nepulsatil). Workup **vascular** dedicat. Home: **Cap › ORL**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| T | Angio-CT cap și gât + CT stâncă temporală | Indicat | B | 2/3 | Cauză vasculară: tumoră glomică (timpanică/jugulară), dehiscență de golf jugular / sinus sigmoid, fistulă durală, stenoză, sinus lateral aberrant. |
| M | IRM + Angio-IRM cap, cu și fără contrast | Indicat | B | 0/0 | Alternativă neinvazivă: paragangliom, schwannom, cauze vasculare, tromboză de sinus. |

#### (O2) 🟠 Surditate brusc instalată (neurosenzorială)
Urgentă; distinctă de „Surditatea neurosenzorială la adult" (cronic). Home: **Cap › ORL**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| M | IRM conduct auditiv intern și unghi ponto-cerebelos, cu contrast | Indicat | B | 0/0 | Excludere schwannom vestibular / leziune retrocohleară; urgență ORL (fereastră terapeutică precoce). |

#### (O3) 🔴 Patologie orbitară (exoftalmie, masă orbitară, oftalmopatie tiroidiană, celulită orbitară)
_ACR AC „Orbits, Vision, and Visual Loss"._ Azi „Tulburări de vedere" acoperă neuro-oftalmologia
funcțională (acuitate/câmp), NU patologia orbitară structurală. Home: **Cap › Neuro** (lângă
„Tulburări de vedere") sau ORL.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| M | IRM orbite, cu și fără contrast | Indicat | B | 0/0 | Masă orbitară, nevrită optică, oftalmopatie tiroidiană (părți moi, apex orbitar, nerv optic). |
| T | CT orbite | Indicat | B | 2/2 | Exoftalmie / celulită orbitară (os, colecții, corp străin), traumă — complementar; **urgență** în celulita orbitară cu complicații. |

#### (O4) 🟠 Otită externă malignă (necrozantă) / osteomielita bazei craniului
Home: **Cap › ORL**.
| Tip | Examen | Indicație | Grad | Doză | Comentariu |
|---|---|---|---|---|---|
| T | CT stâncă temporală și bază de craniu, cu contrast | Indicat | B | 2/3 | Eroziune osoasă, extensie (diabetic / imunodeprimat). |
| M | IRM bază de craniu, cu contrast | Indicat | B | 0/0 | Extensie părți moi profunde / intracraniană, spații parafaringiene. |
| N | Scintigrafie osoasă / cu leucocite marcate / PET-CT | Doar cu aviz specializat | C | 2/4 | Confirmarea activității, urmărirea răspunsului terapeutic. |

### 41.C 🟢 Opțional (acoperire exhaustivă)

- **Boala Menière / hidrops endolimfatic** (extindere a „urechii interne") — IRM cu gadolinium
  tardiv, secvențe dedicate — la aviz specializat.
- **Malformații / displazii ale urechii interne** (surditate progresivă/asimetrică, bilanț
  pre-implant cohlear) — CT stâncă temporală + IRM.
- **Nevralgie de trigemen** (posibil sub N5 „neuropatie craniană") — IRM cu secvențe de conflict
  neuro-vascular (ansă vasculară pe CN V).

### Note de acoperire (deja prezente — fără gol)

Encefalitele/meningitele → „Patologie neuroinfecțioasă" ✓; demența → „Probleme cognitive" ✓;
sindroamele parkinsoniene → „Mișcări anormale" ✓; mielopatia → „Sindroame medulare" ✓; scleroza
multiplă → „Scleroza în plăci…" ✓; patologia hipofizară → „Procese expansive hipofizare…" ✓.

---

## 42. Radiologie intervențională — conflicte de grad/indicație descoperite la deduplicare (2026-07-10)

Reviewul capitolului RI (247 → 176 rânduri — cifra de pornire e după scoaterea artrografiei
ATM, §1 — vezi `CHANGELOG.md` §14 și `DUPLICATE-review.md` §E) a găsit capitolul construit
din **două „valuri" de import suprapuse** pe fiecare subcapitol (rândul-placeholder „ALTĂ
SITUAȚIE CLINICĂ" ajunsese sistematic la mijlocul fiecărui subcapitol, nu la final — semnul
granulei celor două valuri) plus duplicate izolate între subcapitole. Marea majoritate a
perechilor identificate aveau **Indicație + Grad + Terapeutic identice** (doar diacritice/
formulare diferite) și au fost comasate mecanic. **Următoarele perechi au conflicte reale de
conținut clinic și au fost lăsate NEATINSE (ambele rânduri păstrate)** — de tranșat de editori:

- **NR 1166 vs 1176** · Traumatisme · „…traumatisme renale hemodinamic instabile" · Arteriografie
  cu embolizare, grad B ambele · **Indicație diferă**: „Doar în cazuri particulare" (1166) vs
  „Neindicat" (1176), pentru practic aceeași descriere clinică (fără extravazare CT la pacient
  stabil/responsiv).
- **NR 1236 vs 1264** · Aparat cardiovascular · „Arteriopatii periferice simptomatice" ·
  Angiografie directă/invazivă, grad A ambele · **Indicație diferă**: „Doar cu aviz specializat"
  (1236) vs „Indicat" (1264).
- **NR 1338 vs 1356** · Aparat urogenital · „Avorturi spontane multiple" · HSG, „Doar cu aviz
  specializat" ambele · **Grad diferă**: C (1338) vs B (1356).
- **NR 1359 vs 1379** · Sistem nervos · „Accident vascular cerebral constituit (AVC)" ·
  Angiografie, „Doar cu aviz specializat" ambele · **Grad diferă**: B (1359) vs A (1379).
- **NR 1388 vs 1393** · Aparat endocrin · „Nodul tiroidian palpabil…" · PCAFGE · **Indicație
  diferă**: „Indicat"/A (1388) vs „Doar cu aviz specializat"/B (1393).
- **NR 1192 vs 1289** · Oncologie vs Aparat digestiv · Carcinom hepatocelular · Chemoembolizare
  (variantă convențională + drug-eluting beads, grad B, NR 1192) vs Chemoembolizare
  intraarterială generică (grad A, NR 1289) — descriu practic aceeași procedură la **grade
  diferite** și în **subcapitole diferite** (vezi și §43 mai jos pentru chestiunea de graniță
  Oncologie/organ).

**Regula de aur „gradele nu se modifică de mine" a fost respectată** — niciuna dintre aceste
perechi nu a fost alterată; doar semnalate.

## 43. Radiologie intervențională — granițe de subcapitol de confirmat (2026-07-10)

Descoperite la deduplicare — conținut identic sau aproape identic există în **două subcapitole
diferite** ale RI, fără un criteriu clar care să decidă „home"-ul unic. Pentru cazurile cu
conținut *strict identic* am consolidat pe un subcapitol (motivat mai jos, dar **reversibil** —
nu e o decizie clinică, doar de organizare) și am șters duplicatul; principiul general de graniță
rămâne **de confirmat**. (Suprapunerea **carotidă** cardiovascular/sistem nervos e deja tratată
pe larg în §40 — nu se repetă aici; NR 1384 a primit doar corecția obiectivă `Tip I→A`, vezi
`CHANGELOG.md` §14.)

- **Biopsie/patologie pulmonară oncologică — Oncologie vs Aparat respirator.** „Neoplasm
  bronhopulmonar – diagnostic – suspiciune clinică" exista identic în ambele (NR 1187 Oncologie ==
  NR 1281 Aparat respirator) — **comasat, păstrat NR 1281** (Aparat respirator, unde există deja
  grupul de biopsii pulmonare NR 1270–1274, 1280, 1282). Rămân însă în **Oncologie** alte rânduri
  înrudite (NR 1188 nodul în contact cu peretele, NR 1189 tumoră pulmonară, NR 1193 HCC-adiacent
  radioembolizare+RT) care s-ar putea la fel de bine muta la Aparat respirator — **de decis** dacă
  Oncologie ar trebui să rămână doar pentru proceduri fără organ unic (adenopatii, mase de părți
  moi) sau să găzduiască tot ce ține de stadializare/tratament oncologic indiferent de organ.
- **Hepatocarcinom / colangiocarcinom — Oncologie vs Aparat digestiv.** Tot conținutul terapeutic
  hepatobiliar (chemoembolizare, radioembolizare, drenaj biliar, biopsie) exista **duplicat
  integral** între Oncologie (NR 1194–1197) și Aparat digestiv (NR 1289, 1291–1293). **Comasat,
  păstrate variantele din Aparat digestiv** (motivație: precedent „Cancer de sân rămâne în Sân" —
  patologia hepatobiliară oncologică e indisolubil legată de restul conținutului hepatobiliar).
  NR 1192 (Oncologie, variantă cu grad diferit) **lăsat neatins** — vezi conflictul din §42.
  Rămâne în Oncologie NR 1193 (radioembolizare + radioterapie externă HCC, fără pereche în
  Aparat digestiv). **De confirmat**: principiul „malignitate cu organ unic → subcapitolul de
  organ, nu Oncologie" ca regulă generală pentru RI (analog excepției Sân de la nivelul
  capitolelor) — același principiu care ar putea răspunde și la întrebarea de mai sus.
- **Embolie pulmonară / malformație arterio-venoasă pulmonară — Aparat cardiovascular vs Aparat
  respirator.** Ambele existau duplicate (NR 1219 cardio == NR 1278 respirator pentru embolie
  pulmonară; NR 1243 cardio == NR 1276 respirator pentru MAV pulmonară). **Comasate inconsecvent**
  (embolia pulmonară păstrată la Cardiovascular lângă filtrul de VCI NR 1220; MAV pulmonară
  păstrată la Respirator lângă restul patologiei vasculare pulmonare NR 1274) — **de confirmat**
  dacă merită aliniate pe același criteriu.
- **Sindrom Conn (hiperaldosteronism primar) — Aparat urogenital vs Aparat endocrin.** Exista
  **triplicat** (NR 1354, 1355 în Aparat urogenital + NR 1387 în Aparat endocrin, conținut
  identic). **Comasat la Aparat endocrin** (NR 1387 — glanda suprarenală e conținut endocrin,
  plasarea în urogenital era clar eronată). Nu e o chestiune de graniță reală, doar o eroare de
  încadrare corectată.
