# GIRI — Ghid de Indicații Radioimagistice

Sursă de date structurată (CSV) pentru ghidul de indicații radioimagistice, cu istoric
de modificări versionat. Acest repo conține **doar datele** — aplicația de consultare
(„IRIS") este un proiect separat și **nu** se regenerează din acest ghid deocamdată
(posibil ani de zile).

## Fișierul principal

**`GHID.csv`** — 1488 rânduri (fără antet) × 13 coloane, UTF-8, cu diacritice românești
corecte (ș/ț cu virgulă, **nu** cedilă). Delimitator virgulă, câmpuri cu text între
ghilimele duble (`"`), ghilimele interne dublate (`""`).

### Coloane

| # | Coloană | Descriere |
|---|---|---|
| 1 | `NR.CRT` | ID secvențial 1..1488. **Doar identificator de rând**, fără semnificație clinică. Se renumerotează la nevoie. |
| 2 | `Capitol` | Unul din cele 14 capitole (vezi mai jos). |
| 3 | `Subcapitol` | Grupare în cadrul capitolului. |
| 4 | `Situația Clinică` | Scenariul clinic pentru care se recomandă (sau nu) investigația. |
| 5 | `Tip` | Codul modalității imagistice (vezi legenda). |
| 6 | `Examen` | Denumirea investigației / procedurii. |
| 7 | `Indicație` | Gradul de recomandare (vezi legenda). |
| 8 | `Grad Indicație` | Nivel de evidență (A / B / C / ? etc.). |
| 9 | `Comentarii` | Note clinice. |
| 10 | `Alte informații` | Coduri interne (ex. „RI - PCx"), referințe. |
| 11 | `Doza Min` | Doză minimă (mSv sau scală relativă). |
| 12 | `Doza Max` | Doză maximă. |
| 13 | `Terapeutic` | **Da / Nu** (gol pentru placeholder-e). Da = investigația/procedura are și rol terapeutic, chiar dacă e și diagnostică. |

### Legenda `Tip`

| Cod | Semnificație |
|---|---|
| `G` | Radiografie (grafie convențională, mamografie) |
| `E` | Ecografie / Doppler |
| `M` | IRM / RM |
| `T` | CT |
| `N` | Medicină nucleară (PET-CT, scintigrafie) |
| `X` | Radiologie cu contrast / fluoroscopie (UIV, cistografie, irigografie, tranzit baritat) |
| `D` | Diagnostic invaziv / endoscopic (ecoendoscopie, ERCP, osteodensitometrie, videocapsulă) |
| `I` | **Intervențional** (proceduri; consolidat integral în capitolul Radiologie intervențională) |
| `A` | **Angiografie invazivă** (tratat ca intervențional; mutat în Radiologie intervențională) |
| `Z` | Placeholder / „situație clinică neîncadrabilă" — rând-punte, fără examen concret |

### Legenda `Indicație`

`Indicat` · `Doar în cazuri particulare` · `Doar cu aviz specializat` ·
`Este necesară justificare detaliată` · `Neindicat` · `Neindicat în primă intenție` ·
`Vezi Detalii Ghid!`

## Structura pe capitole (1488 rânduri)

| # | Capitol | NR.CRT | Rânduri |
|---|---|---|---|
| 1 | Pediatrie | 1–155 | 155 |
| 2 | Traumatisme | 156–280 | 125 |
| 3 | Cancer | 281–516 | 236 |
| 4 | Aparat cardiovascular | 517–603 | 87 |
| 5 | Torace | 604–678 | 75 |
| 6 | Aparat digestiv | 679–806 | 128 |
| 7 | Aparat uro-genital și glande suprarenale | 807–875 | 69 |
| 8 | Obstetrică și ginecologie | 876–902 | 27 |
| 9 | Sân | 903–958 | 56 |
| 10 | Cap | 959–1078 | 120 |
| 11 | Gât (părți moi) | 1079–1096 | 18 |
| 12 | Coloană vertebrală | 1097–1151 | 55 |
| 13 | Aparat locomotor | 1152–1238 | 87 |
| 14 | Radiologie intervențională | 1239–1488 | 250 |

## Documentație și review

- **`CHANGELOG.md`** — jurnalul tuturor modificărilor, **organizat pe capitole**, ca
  fiecare capitol să poată fi trimis independent la review. Marchează modificările
  ⛔ BREAKING (incompatibile cu versiunea aprobată).
- **`DUPLICATE-review.md`** — evidența cvasi-duplicatelor (rezolvate + rămase de studiat).
- **`THERAPEUTIC-review.md`** — cazurile duale/pe muchie pentru coloana „Terapeutic".
- **`EDITORIAL-decisions.md`** — chestiuni deschise pentru decizia comună a editorilor.

## Baseline

Această ramură pornește de la sursa canonică aprobată și **s-a îndepărtat mult** de ea
(mutarea intervenționalului, coloana „Terapeutic", normalizări). Vezi `CHANGELOG.md`.
Sursa aprobată nu e inclusă (e statică); se poate adăuga ulterior ca referință dacă e
nevoie de un diff „aprobat → GIRI".

## Flux de lucru

1. Editează `GHID.csv` (sau prin scripturi, pentru operații în masă).
2. Rulează validarea: `python3 tools/validate.py` (vezi `CLAUDE.md`).
3. Documentează în `CHANGELOG.md`, la capitolul corespunzător.
4. Commit + push. Fiecare capitol trimis la review poate fi un pull request.
