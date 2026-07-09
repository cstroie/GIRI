#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renumerotare globală NR.CRT la 1..N (contigu, fără găuri).
Folosit când se cere renumerotare după ștergeri sau reordonări.
Păstrează ordinea fizică a rândurilor; doar schimbă ID-urile din coloana 0."""
import csv, sys
APPLY = "--apply" in sys.argv
PATH = "GHID.csv"

with open(PATH, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
header, data = rows[0], rows[1:]

# raport înainte de modificare
old_ids = [r[0] for r in data]
old_max = max(int(r[0]) for r in data)
old_gaps = len(data) - (old_max - 1)

print(f"{'APPLY' if APPLY else 'DRY-RUN'} — renumerotare NR.CRT")
print(f"  Rânduri totale: {len(data)}")
print(f"  ID max curent: {old_max}")
print(f"  Găuri în ID: {old_gaps}")

# renumerotare
new_ids = [str(i + 1) for i in range(len(data))]
for i, r in enumerate(data):
    r[0] = new_ids[i]

# raport după modificare
print(f"  ID min nou: 1, ID max nou: {len(data)}")
print(f"  Rânduri schimbate: {sum(1 for o, n in zip(old_ids, new_ids) if o != n)}")

if not APPLY:
    print(f"\n  (Adaugă --apply pentru a rescrie {PATH})")
else:
    with open(PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        w.writerows(data)
    print(f"\n✅ scris — {len(data)} rânduri, 1..{len(data)}")
