# GIRI — Ghid de Indicații Radioimagistice

Sursă de date structurată (CSV) pentru ghidul de indicații radioimagistice, cu istoric
de modificări versionat. Acest repo conține **doar datele** — aplicația de consultare
(„IRIS") este un proiect separat și **nu** se regenerează din acest ghid deocamdată
(posibil ani de zile).

## Fișierul principal

**`GHID.csv`** — 1340 rânduri (fără antet) × 13 coloane, UTF-8, cu diacritice românești
corecte (ș/ț cu virgulă, **nu** cedilă). Delimitator virgulă, câmpuri cu text între
ghilimele duble (`"`), ghilimele interne dublate (`""`).

### Coloane

| # | Coloană | Descriere |
|---|---|---|
| 1 | `NR.CRT` | ID de rând, secvențial **1..1340** (renumerotat 2026-07-10, după readucerea intervenționalului mamar în Sân și adăugarea PET-CT DOTATATE). **Doar identificator**, fără semnificație clinică. Între renumerotări poate deveni necontiguu (găuri după ștergeri; ID-uri noi la finalul secvenței); renumerotare doar la cerere explicită. |
| 2 | `Capitol` | Unul din cele 14 capitole (vezi mai jos). |
| 3 | `Subcapitol` | Grupare în cadrul capitolului. |
| 4 | `Situația Clinică` | Scenariul clinic pentru care se recomandă (sau nu) investigația. |
| 5 | `Tip` | Codul modalității imagistice (vezi legenda). |
| 6 | `Examen` | Denumirea investigației / procedurii. |
| 7 | `Indicație` | Gradul de recomandare (vezi legenda). |
| 8 | `Grad Indicație` | Nivel de evidență: A = dovezi solide, B = dovezi moderate, C = consens / dovezi limitate (vezi legenda). |
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

### Legenda `Grad Indicație` (nivel de evidență)

| Grad | Semnificație |
|---|---|
| `A` | Dovezi solide |
| `B` | Dovezi moderate |
| `C` | Consens / dovezi limitate |
| `?` | Neprecizat |

## Structura pe capitole (1340 rânduri)

| # | Capitol | NR.CRT | Rânduri |
|---|---|---|---|
| 1 | Pediatrie | 1–196 | 196 |
| 2 | Traumatisme | 197–317 | 121 |
| 3 | Cancer | 318–577 | 260 |
| 4 | Aparat cardiovascular | 578–664 | 87 |
| 5 | Torace | 665–728 | 64 |
| 6 | Aparat digestiv | 729–796 | 68 |
| 7 | Aparat uro-genital și glande suprarenale | 797–865 | 69 |
| 8 | Obstetrică și ginecologie | 866–891 | 26 |
| 9 | Sân | 892–949 | 58 |
| 10 | Cap | 950–1029 | 80 |
| 11 | Gât (părți moi) | 1030–1062 | 33 |
| 12 | Coloană vertebrală | 1063–1101 | 39 |
| 13 | Aparat locomotor | 1102–1166 | 65 |
| 14 | Radiologie intervențională | 1167–1340 | 174 |

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

## Vizualizare HTML

`tools/generate_html.py` transformă `GHID.csv` într-un `GHID.html` lizibil (un singur
fișier, CSS inclus, fără JavaScript și fără dependențe externe) — cuprins, legendă și
ierarhia Capitol → Subcapitol → Situație clinică → examene, cu badge-uri colorate pentru
Indicație/Grad/Terapeutic.

```
python3 tools/generate_html.py        # citește GHID.csv, scrie GHID.html
```

`GHID.html` e un artefact generat, **nu se editează manual**. Workflow-ul GitHub Actions
`.github/workflows/build-html.yml` rulează `validate.py` și regenerează `GHID.html` la
fiecare push care atinge `GHID.csv`, comițând rezultatul înapoi pe aceeași ramură dacă
s-a schimbat.
