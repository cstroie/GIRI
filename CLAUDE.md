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
   Poate fi renumerotat; nu construi referințe externe pe el. Referă rândurile prin
   **Capitol + Situație clinică**.
4. **Tot ce e intervențional (Tip `I` și `A`) stă în capitolul „Radiologie
   intervențională".** Nu trebuie să reapară intervențional împrăștiat în capitolele
   diagnostice — procedurile terapeutice nu sunt opțiuni de diagnostic.
5. **Documentează fiecare modificare în `CHANGELOG.md`**, la capitolul corespunzător.
   Marchează ⛔ BREAKING ce e incompatibil cu versiunea aprobată.
6. **Nu decide singur chestiunile clinice ambigue.** Încadrări de capitol discutabile,
   duplicate cu conținut diferit, cazuri pe muchie → `EDITORIAL-decisions.md` și
   întreabă. (Vezi „Decizii deja luate" mai jos.)

## Invarianți — trebuie să rămână adevărați după orice modificare

Rulează `python3 tools/validate.py` și verifică:

- `NR.CRT` contigue 1..N, fără găuri sau duplicate.
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

## Decizii încă deschise (în `EDITORIAL-decisions.md`)

- Artrografia articulației temporo-mandibulare (ATM): încadrare subcapitol (Sistem
  nervos vs Aparat locomotor) și dacă se păstrează (e „Neindicat", înlocuită de IRM).

## Maparea capitol origine → subcapitol RI (pentru mutări viitoare de intervențional)

Traumatisme→Traumatisme · Cancer→Oncologie · Aparat cardiovascular→Aparat cardiovascular ·
Torace→Aparat respirator · Aparat digestiv→Aparat digestiv · Aparat uro-genital→Aparat urogenital ·
Obstetrică-ginecologie→Aparat urogenital · Sân→Oncologie · Cap→Sistem nervos ·
Gât→Aparat endocrin (dar „Masă cervicală"→Oncologie) · Coloană→Aparat locomotor (dar
embolizări spinale→Sistem nervos) · Aparat locomotor→Aparat locomotor.
