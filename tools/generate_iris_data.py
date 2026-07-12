#!/usr/bin/env python3
"""Generează pachetul de date IRIS (`iris-data.js`) din `GHID.csv`.

Port fidel al convertorului din IRIS (`tools/csv-to-json.html`): aceeași
logică de canonizare, slug, detecție placeholder și numărare. În plus,
împachetează rezultatul în forma `window.IRIS={...}` a fișierului consumat de
PWA, adăugând `legend` + `synonyms` (statice, nederivabile din CSV — păstrate
în `iris_static.json`, lângă GHID.csv) și `meta` regenerat.

Rulează:
    python3 tools/generate_iris_data.py                 # -> iris/iris-data.js
    python3 tools/generate_iris_data.py --out /path/iris-data.js

`legend`/`synonyms` se actualizează prin re-extragere din iris-data.js-ul
curent al IRIS (vezi `iris_static.json`); nu se editează manual aici.
"""
import argparse
import csv
import datetime
import json
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(HERE, "..")
DEFAULT_CSV = os.path.join(REPO_ROOT, "GHID.csv")
STATIC_JSON = os.path.join(REPO_ROOT, "iris_static.json")
DEFAULT_OUT = os.path.join(REPO_ROOT, "iris", "iris-data.js")

_CEDILLA = str.maketrans({"ş": "ș", "Ş": "Ș", "ţ": "ț", "Ţ": "Ț"})


def fix_dia(s):
    return (s or "").translate(_CEDILLA)


def clean(s):
    """clean() din convertor: normalizează spațiile + repară cedila."""
    return fix_dia(re.sub(r"\s+", " ", s or "").strip())


def canon(s):
    """canon() din convertor: lowercase, fără diacritice, punctuație → spațiu."""
    s = fix_dia(s or "").lower()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[.,;:()/\-]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def slug(s):
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", canon(s)))[:60]


def is_placeholder(sit, exam):
    key = canon(sit) + " " + canon(exam)
    return bool(re.search(
        r"alta situatie clinica|refaceti selectia|"
        r"situatie clinica neincadrabila|vezi detalii ghid", key))


def score(name):
    """pickName(): preferă varianta cu mai multe diacritice / majusculă inițială."""
    return len(re.findall(r"[șțăâîȘȚĂÂÎ]", name)) + (2 if re.match(r"[A-ZȘȚĂÂÎ]", name) else 0)


def pick_name(existing, candidate):
    if not candidate:
        return existing
    return candidate if score(candidate) > score(existing) else existing


def convert(csv_path):
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    idx = {h.strip(): i for i, h in enumerate(header)}
    data = [r for r in rows[1:] if len(r) > 1 and any(x.strip() for x in r)]

    chapters, subchapters, situations = {}, {}, {}
    recommendations = []
    ch_order = 0
    ph = 0

    def col(r, name):
        return r[idx[name]] if idx.get(name) is not None and idx[name] < len(r) else ""

    for r in data:
        cap, sub = clean(col(r, "Capitol")), clean(col(r, "Subcapitol"))
        sit, exam = clean(col(r, "Situația Clinică")), clean(col(r, "Examen"))
        ck, sk, stk = canon(cap), canon(sub), canon(sit)

        if ck not in chapters:
            chapters[ck] = {"id": "c-" + slug(cap), "name": cap, "order": ch_order, "count": 0}
            ch_order += 1
        ch = chapters[ck]
        ch["name"] = pick_name(ch["name"], cap)

        sub_key = ck + "|" + sk
        if sub_key not in subchapters:
            subchapters[sub_key] = {"id": ch["id"] + "__s-" + slug(sub), "name": sub,
                                    "chapterId": ch["id"], "order": len(subchapters), "count": 0}
        sb = subchapters[sub_key]
        sb["name"] = pick_name(sb["name"], sub)

        isph = is_placeholder(sit, exam)
        if isph:
            ph += 1

        sit_key = sub_key + "|" + stk
        if sit_key not in situations:
            situations[sit_key] = {"id": sb["id"] + "__q-" + slug(sit), "name": sit,
                                   "subchapterId": sb["id"], "chapterId": ch["id"],
                                   "placeholder": isph, "order": len(situations), "count": 0}
        st = situations[sit_key]
        st["name"] = pick_name(st["name"], sit)

        dn, dx = col(r, "Doza Min").strip(), col(r, "Doza Max").strip()
        recommendations.append({
            "id": "r-" + str(len(recommendations) + 1),
            "situationId": st["id"],
            "nr": int(col(r, "NR.CRT")) if col(r, "NR.CRT").strip().lstrip("-").isdigit() else None,
            "tip": col(r, "Tip").strip(),
            "exam": exam,
            "indication": clean(col(r, "Indicație")),
            "grade": re.sub(r"^\?$", "", clean(col(r, "Grad Indicație"))),
            "comments": clean(col(r, "Comentarii")),
            "otherInfo": clean(col(r, "Alte informații")),
            "doseMin": None if dn == "" else num(dn),
            "doseMax": None if dx == "" else num(dx),
            "placeholder": isph,
        })

    sit_by_id = {s["id"]: s for s in situations.values()}
    sub_by_id = {s["id"]: s for s in subchapters.values()}
    ch_by_id = {c["id"]: c for c in chapters.values()}
    for rec in recommendations:
        if not rec["placeholder"]:
            sit_by_id[rec["situationId"]]["count"] += 1
    for s in situations.values():
        if not s["placeholder"]:
            sub_by_id[s["subchapterId"]]["count"] += 1
            ch_by_id[s["chapterId"]]["count"] += 1

    ch_a = sorted(chapters.values(), key=lambda x: x["order"])
    sb_a = sorted(subchapters.values(), key=lambda x: x["order"])
    st_a = sorted(situations.values(), key=lambda x: x["order"])
    strip = lambda x: {k: v for k, v in x.items() if k != "order"}

    return {
        "chapters": [strip(c) for c in ch_a],
        "subchapters": [strip(s) for s in sb_a],
        "situations": [strip(s) for s in st_a],
        "recommendations": recommendations,
        "_ph": ph,
    }


def num(s):
    """Number(): întreg dacă e posibil, altfel float."""
    try:
        f = float(s)
        return int(f) if f.is_integer() else f
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--csv", default=DEFAULT_CSV, help="sursă (implicit GHID.csv)")
    parser.add_argument("--out", default=DEFAULT_OUT, help="destinație iris-data.js")
    args = parser.parse_args()

    with open(STATIC_JSON, encoding="utf-8") as f:
        static = json.load(f)

    conv = convert(args.csv)
    ph = conv.pop("_ph")

    bundle = {
        "chapters": conv["chapters"],
        "subchapters": conv["subchapters"],
        "situations": conv["situations"],
        "recommendations": conv["recommendations"],
        "legend": static["legend"],
        "synonyms": static["synonyms"],
        "meta": {
            "source": "Ghid indicații radioimagistice",
            "generated": datetime.date.today().isoformat(),
            "counts": {
                "chapters": len(conv["chapters"]),
                "subchapters": len(conv["subchapters"]),
                "situations": sum(1 for s in conv["situations"] if not s["placeholder"]),
                "recommendations": sum(1 for r in conv["recommendations"] if not r["placeholder"]),
            },
        },
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    payload = json.dumps(bundle, ensure_ascii=False, separators=(",", ":"))
    header = ("/* Iris — datasource. Auto-generat din GHID.csv "
              "(tools/generate_iris_data.py). Nu edita manual. */\n")
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(header + "window.IRIS=" + payload + ";\n")

    print(f"✓ {args.out}")
    print(f"  Capitole: {len(conv['chapters'])}  ·  Subcapitole: {len(conv['subchapters'])}  "
          f"·  Situații: {len(conv['situations'])} (placeholder: {ph})  "
          f"·  Recomandări: {len(conv['recommendations'])}")


if __name__ == "__main__":
    main()
