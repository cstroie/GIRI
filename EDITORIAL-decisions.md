# Decizii editoriale — de discutat cu ceilalți editori

NR = NR.CRT curent. (Numerotarea veche nu se mai păstrează.)

---

## 1. Artrografia articulației temporo-mandibulare (ATM) — încadrare capitol

**Rânduri:**

- **NR 1460** · RI › Sistem nervos · „Disfuncții ale articulației temporo-mandibulare" ·
  Tip I · „Artrografie articulații temporo-mandibulare" · **Neindicat** · grad „?" ·
  _„Artrografia temporo-mandibulară este în prezent înlocuită de examenul IRM."_
- **NR 1461** · RI › Sistem nervos · idem · Tip I · **Neindicat** · grad „B" ·
  aceeași notă · „RI - PC8".
- **NR 1358** · RI › Aparat digestiv · artrografie (existentă în RI, subcapitol aparent greșit).

**De decis:**

1. **Încadrare pe subcapitol.** ATM este anatomic o articulație → logic ar sta la
   **Aparat locomotor**, nu la Sistem nervos (unde a ajuns automat, venind din capitolul
   „Cap"). NR 1360 pare greșit la „Aparat digestiv". Confirmați subcapitolul corect.
2. **Păstrare vs. eliminare.** Ambele rânduri sunt **Neindicat**, cu nota că artrografia
   ATM „este în prezent înlocuită de examenul IRM". De decis dacă se mai păstrează în ghid
   (ca indicație istorică / negativă) sau se elimină.

> Status: **lăsat neatins** în date până la decizia editorială. Nicio mutare automată.

---

## 2. ERCP (Tip D) rămas în capitolele de origine

**Decizie luată** (de consemnat): ERCP **rămâne** în capitolul de origine (nu se mută la
Radiologie intervențională), deși este o procedură intervențională. În coloana nouă
„Terapeutic" este marcat **Da**. De reconfirmat la review dacă poziționarea e cea dorită.

---

## 3. Pediatrie — omisiuni de patologie (propuneri de adăugat)

Din analiza capitolului Pediatrie (NR 1–155). Patologii frecvente aparent neacoperite,
propuse pe baza practicii curente și a ghidurilor de referință (ACR Appropriateness
Criteria, RCR iRefer). **Schițe — de validat clinic de editori** înainte de inserare
în `GHID.csv`. Gradele/dozele sunt orientative.

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

### 3.6 Sistem nervos — acoperire bună
- Eventual **ataxie acută** de adăugat (IRM = referință). Prioritate mică.

> Status: **niciun rând nou inserat** în `GHID.csv`. Se așteaptă decizia editorilor;
> apoi se adaugă cu grade/doze validate și se consemnează în CHANGELOG.

---

## 4. Pediatrie — întrebări editoriale de stil (nu s-au atins datele)

Identificate la analiza capitolului; sunt decizii de stil, nu corecturi obiective →
lăsate pentru editori.

1. **Comentarii identice pe rânduri ale aceleiași situații** — perechile NR 12/13
   (Constipație), NR 16/17 (Invaginație), NR 89/90 (Cefalee). Se păstrează (fiecare rând
   rămâne autonom la consultare) sau se rezumă pe rândul principal? *Recomandare: păstrare
   — ghidul e conceput cu rânduri auto-suficiente.*
2. **Ordinea modalităților în cadrul unei situații** nu e uniformă (uneori E,G,M,T,N;
   alteori G,E,...). Standardizarea ar cere renumerotarea `NR.CRT` (invaziv, beneficiu
   doar cosmetic). *Recomandare: nu se schimbă acum.*
3. **Grad indicație neuniform** pentru aceeași modalitate în situații similare (ex.
   Ecografie „Masă abdominală" NR 22 = grad B vs. grad A în alte situații). Poate fi
   intențional (context clinic diferit) → decizie clinică, nu se aliniază automat.
