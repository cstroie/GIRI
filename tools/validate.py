#!/usr/bin/env python3
"""Validare invarianți GIRI/GHID.csv.

Rulează:  python3 tools/validate.py
Iese cu cod 0 dacă totul e OK, 1 dacă există erori.
"""
import csv
import sys
import os
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "..", "GHID.csv")

EXPECTED_HEADER = [
    "NR.CRT", "Capitol", "Subcapitol", "Situația Clinică", "Tip", "Examen",
    "Indicație", "Grad Indicație", "Comentarii", "Alte informații",
    "Doza Min", "Doza Max", "Terapeutic",
]
RI = "Radiologie intervențională"

# Perechi de duplicate păstrate intenționat (chei = cols 2..12, normalizate).
# Nu sunt semnalate ca erori. Vezi DUPLICATE-review.md.
ALLOWED_DUP_SITUATII = {
    "Suspiciune de masă pelvină",   # NR 880/881 (grad C vs A)
    "Rahialgie / Radiculalgie",     # NR 1446/1447 (PC5 vs PC7)
}


def main():
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    errors = []
    warnings = []
    header, data = rows[0], rows[1:]

    # 1) antet
    if header != EXPECTED_HEADER:
        errors.append(f"Antet neașteptat:\n  {header}")

    # 2) 13 coloane / rând
    for i, r in enumerate(data, start=2):  # linia 2 = primul rând de date
        if len(r) != 13:
            errors.append(f"Linia {i}: {len(r)} coloane (așteptat 13)")

    # 3) NR.CRT: întreg pozitiv + UNIC (erori). Contiguitatea 1..N NU e obligatorie —
    #    renumerotarea nu se face automat (vezi CLAUDE.md), deci găurile sunt tolerate
    #    și raportate ca un singur avertisment (nu o eroare per rând).
    seen_nr = {}
    nums = []
    for pos, r in enumerate(data, start=1):
        if not len(r):
            continue
        nr = r[0]
        if not nr.isdigit():
            errors.append(f"NR.CRT invalid la poziția {pos}: „{nr}” (trebuie întreg pozitiv)")
            continue
        if nr in seen_nr:
            errors.append(f"NR.CRT duplicat „{nr}” (pozițiile {seen_nr[nr]} și {pos})")
        else:
            seen_nr[nr] = pos
        nums.append(int(nr))
    if nums and sorted(nums) != list(range(1, len(nums) + 1)):
        gaps = sorted(set(range(1, len(nums) + 1)) - set(nums))
        warnings.append(
            f"NR.CRT necontiguu ({len(gaps)} găuri, ex. {gaps[:5]}) — "
            f"renumerotare amânată; rulează renumerotarea doar la cerere explicită."
        )

    # 4) intervențional (Tip I/A) doar în RI — excepție: senologia (Sân) își
    #    păstrează intervenționalul mamar (vezi CLAUDE.md, „Decizii deja luate")
    INTERVENTIONAL_HOMES = (RI, "Sân")
    for r in data:
        if len(r) < 5:
            continue
        if r[4].strip() in ("I", "A") and r[1] not in INTERVENTIONAL_HOMES:
            errors.append(f"NR {r[0]}: Tip {r[4].strip()} în afara RI/Sân ({r[1]})")

    # 5) diacritice cu cedilă
    cedilla = "şŞţŢ"
    for r in data:
        for c, val in enumerate(r):
            if any(ch in cedilla for ch in val):
                errors.append(f"NR {r[0]}: cedilă în coloana {c+1}: „{val[:40]}”")
                break

    # 6) Terapeutic ∈ {Da, Nu, gol}
    for r in data:
        if len(r) >= 13 and r[12] not in ("Da", "Nu", ""):
            errors.append(f"NR {r[0]}: Terapeutic invalid „{r[12]}”")

    # 7) duplicate exacte pe cols 2..12
    seen = {}
    for r in data:
        if len(r) < 12:
            continue
        key = tuple(r[1:12])
        if key in seen:
            situatie = r[3]
            if situatie in ALLOWED_DUP_SITUATII:
                warnings.append(f"Duplicat păstrat intenționat: NR {seen[key]} / {r[0]} — „{situatie}”")
            else:
                errors.append(f"Duplicat exact: NR {seen[key]} == NR {r[0]} — „{situatie[:40]}”")
        else:
            seen[key] = r[0]

    # raport
    print(f"Rânduri de date: {len(data)}")
    for w in warnings:
        print("  ⚠️  " + w)
    if errors:
        print(f"\n❌ {len(errors)} erori:")
        for e in errors:
            print("  • " + e)
        sys.exit(1)
    print("\n✅ Toți invarianții sunt respectați.")


if __name__ == "__main__":
    main()
