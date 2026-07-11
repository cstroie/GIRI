#!/usr/bin/env python3
"""Generează pachetele .docx de trimis editorilor, câte unul per capitol.

Fiecare pachet conține: conținutul actual al capitolului (din GHID.csv),
modificări deja aplicate (informativ), chestiuni de decis, rânduri noi
propuse și duplicate de rezolvat — acestea patru din urmă preluate dintr-un
fișier YAML de conținut distilat, unul per capitol, în tools/editor_content/.

Rulează:
    python3 tools/generate_editor_docx.py pediatrie cardiovascular
    python3 tools/generate_editor_docx.py --all

Scrie în pentru-editori/<NN-capitol>/<Capitol>.docx — artefacte generate,
nu se editează manual (se editează YAML-ul sursă + acest script).
"""
import argparse
import csv
import os
import sys

import yaml
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate import EXPECTED_HEADER  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(HERE, "..")
CSV_PATH = os.path.join(REPO_ROOT, "GHID.csv")
CONTENT_DIR = os.path.join(HERE, "editor_content")
OUTPUT_ROOT = os.path.join(REPO_ROOT, "pentru-editori")

# (slug, Capitol exact ca în GHID.csv, nume fișier)
CHAPTERS = [
    ("01-pediatrie", "Pediatrie", "Pediatrie"),
    ("02-traumatisme", "Traumatisme", "Traumatisme"),
    ("03-cancer", "Cancer", "Cancer"),
    ("04-aparat-cardiovascular", "Aparat cardiovascular", "Aparat cardiovascular"),
    ("05-torace", "Torace", "Torace"),
    ("06-aparat-digestiv", "Aparat digestiv", "Aparat digestiv"),
    ("07-aparat-uro-genital-si-glande-suprarenale",
     "Aparat uro-genital și glande suprarenale",
     "Aparat uro-genital și glande suprarenale"),
    ("08-obstetrica-si-ginecologie", "Obstetrică și ginecologie", "Obstetrică și ginecologie"),
    ("09-san", "Sân", "Sân"),
    ("10-cap", "Cap", "Cap"),
    ("11-gat-parti-moi", "Gât (părți moi)", "Gât (părți moi)"),
    ("12-coloana-vertebrala", "Coloană vertebrală", "Coloană vertebrală"),
    ("13-aparat-locomotor", "Aparat locomotor", "Aparat locomotor"),
    ("14-radiologie-interventionala", "Radiologie intervențională", "Radiologie intervențională"),
]
SLUG_TO_CHAPTER = {slug: (cap, fname) for slug, cap, fname in CHAPTERS}
CONTENT_KEY_TO_SLUG = {
    "pediatrie": "01-pediatrie",
    "traumatisme": "02-traumatisme",
    "cancer": "03-cancer",
    "cardiovascular": "04-aparat-cardiovascular",
    "torace": "05-torace",
    "digestiv": "06-aparat-digestiv",
    "urogenital": "07-aparat-uro-genital-si-glande-suprarenale",
    "obstetrica": "08-obstetrica-si-ginecologie",
    "san": "09-san",
    "cap": "10-cap",
    "gat": "11-gat-parti-moi",
    "coloana": "12-coloana-vertebrala",
    "locomotor": "13-aparat-locomotor",
    "ri": "14-radiologie-interventionala",
}

ACCENT = RGBColor(0x1C, 0x5D, 0x8C)


def read_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != EXPECTED_HEADER:
            sys.exit(f"Antet neașteptat în {path}:\n  {reader.fieldnames}")
        return list(reader)


def build_tree(rows, capitol):
    tree = {}
    for row in rows:
        if row["Capitol"] != capitol:
            continue
        sub = tree.setdefault(row["Subcapitol"], {})
        sub.setdefault(row["Situația Clinică"], []).append(row)
    return tree


def load_content(content_key):
    path = os.path.join(CONTENT_DIR, f"{content_key}.yaml")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# --- helpers docx --------------------------------------------------------

def set_cell_text(cell, text, bold=False, italic=False, size=None):
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text or "")
    run.bold = bold
    run.italic = italic
    if size:
        run.font.size = Pt(size)


def add_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = ACCENT
    return h


def style_header_row(table):
    for cell in table.rows[0].cells:
        for p in cell.paragraphs:
            for run in p.runs:
                run.bold = True


# --- secțiuni --------------------------------------------------------

def add_intro(doc, chapter_name):
    add_heading(doc, chapter_name, level=1)
    p = doc.add_paragraph()
    run = p.add_run(
        "Acest document conține conținutul actual al capitolului, așa cum a rezultat "
        "din prima revizuire a ghidului (2026), plus chestiunile pe care vă rugăm să le "
        "tranșați. Completați direct în tabele, în coloana „Decizie” (ex. „Aprobat”, "
        "„Respins”, „Amânat”) și, dacă e cazul, în coloana „Comentariu”. Vă rugăm să nu "
        "modificați structura tabelelor (rânduri/coloane), ca să putem prelua răspunsurile "
        "automat."
    )
    run.italic = True


def add_current_content(doc, tree):
    add_heading(doc, "1. Conținutul actual al capitolului", level=2)
    if not tree:
        doc.add_paragraph("(niciun rând în acest capitol)")
        return
    for subcapitol, situatii in tree.items():
        add_heading(doc, subcapitol, level=3)
        table = doc.add_table(rows=1, cols=6)
        table.style = "Light Grid Accent 1"
        headers = ["Situație clinică", "Tip", "Examen", "Indicație", "Grad", "Comentarii"]
        for cell, text in zip(table.rows[0].cells, headers):
            set_cell_text(cell, text, bold=True)
        for situatie, rows in situatii.items():
            for i, row in enumerate(rows):
                cells = table.add_row().cells
                set_cell_text(cells[0], situatie if i == 0 else "")
                set_cell_text(cells[1], row["Tip"])
                set_cell_text(cells[2], row["Examen"])
                terapeutic = " (Terapeutic)" if row["Terapeutic"].strip() == "Da" else ""
                set_cell_text(cells[3], row["Indicație"] + terapeutic)
                set_cell_text(cells[4], row["Grad Indicație"])
                set_cell_text(cells[5], row["Comentarii"])
        doc.add_paragraph()


def add_fyi(doc, items):
    add_heading(doc, "2. Modificări deja aplicate în acest capitol (informativ)", level=2)
    if not items:
        doc.add_paragraph("(niciuna specifică acestui capitol)")
        return
    doc.add_paragraph(
        "Aceste modificări au fost deja aplicate în GHID.csv; le semnalăm doar ca "
        "informare, nu necesită o nouă aprobare — dar comentați dacă nu sunteți de acord.",
        style=None,
    )
    for item in items:
        doc.add_paragraph(item, style="List Bullet")


def add_open_questions(doc, items):
    add_heading(doc, "3. Chestiuni de decis", level=2)
    if not items:
        doc.add_paragraph("(nicio chestiune deschisă în acest capitol)")
        return
    table = doc.add_table(rows=1, cols=3)
    table.style = "Light Grid Accent 1"
    headers = ["Chestiune", "Decizie", "Comentariu"]
    for cell, text in zip(table.rows[0].cells, headers):
        set_cell_text(cell, text, bold=True)
    table.columns[0].width = Pt(320)
    for item in items:
        cells = table.add_row().cells
        cell = cells[0]
        cell.text = ""
        p = cell.paragraphs[0]
        p.add_run(item["titlu"]).bold = True
        cell.add_paragraph(item.get("descriere", ""))
        for opt in item.get("optiuni", []):
            cell.add_paragraph(f"• {opt}")
        set_cell_text(cells[1], "")
        set_cell_text(cells[2], "")


def add_draft_rows(doc, groups):
    add_heading(doc, "4. Rânduri noi propuse", level=2)
    if not groups:
        doc.add_paragraph("(nicio propunere de rând nou în acest capitol)")
        return
    doc.add_paragraph(
        "Propuneri de completare a capitolului (goluri de conținut față de ghidurile "
        "de referință). Gradele/dozele sunt orientative — de validat clinic."
    )
    for group in groups:
        add_heading(doc, f"{group['subcapitol']} — {group['situatie']}", level=3)
        if group.get("referinta"):
            ref_p = doc.add_paragraph()
            ref_p.add_run(group["referinta"]).italic = True
        table = doc.add_table(rows=1, cols=8)
        table.style = "Light Grid Accent 1"
        headers = ["Tip", "Examen", "Indicație", "Grad", "Doză", "Comentarii", "Decizie", "Comentariu editor"]
        for cell, text in zip(table.rows[0].cells, headers):
            set_cell_text(cell, text, bold=True)
        for row in group["randuri"]:
            cells = table.add_row().cells
            set_cell_text(cells[0], row.get("tip", ""))
            set_cell_text(cells[1], row.get("examen", ""))
            set_cell_text(cells[2], row.get("indicatie", ""))
            set_cell_text(cells[3], row.get("grad", ""))
            set_cell_text(cells[4], row.get("doza", ""))
            set_cell_text(cells[5], row.get("comentarii", ""))
            set_cell_text(cells[6], "")
            set_cell_text(cells[7], "")
        doc.add_paragraph()


def add_duplicates(doc, items):
    add_heading(doc, "5. Duplicate de rezolvat", level=2)
    if not items:
        doc.add_paragraph("(niciun duplicat deschis pentru acest capitol)")
        return
    table = doc.add_table(rows=1, cols=3)
    table.style = "Light Grid Accent 1"
    headers = ["Descriere", "Decizie", "Comentariu"]
    for cell, text in zip(table.rows[0].cells, headers):
        set_cell_text(cell, text, bold=True)
    table.columns[0].width = Pt(320)
    for item in items:
        cells = table.add_row().cells
        set_cell_text(cells[0], item)
        set_cell_text(cells[1], "")
        set_cell_text(cells[2], "")


def generate_chapter(slug, all_rows):
    capitol, fname = SLUG_TO_CHAPTER[slug]
    content_key = next(k for k, s in CONTENT_KEY_TO_SLUG.items() if s == slug)
    content = load_content(content_key)

    tree = build_tree(all_rows, capitol)

    doc = Document()
    add_intro(doc, fname)
    add_current_content(doc, tree)
    add_fyi(doc, content.get("fyi", []))
    add_open_questions(doc, content.get("chestiuni", []))
    add_draft_rows(doc, content.get("randuri_noi", []))
    add_duplicates(doc, content.get("duplicate", []))

    out_dir = os.path.join(OUTPUT_ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{fname}.docx")
    doc.save(out_path)
    return out_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapters", nargs="*", help="chei de conținut (ex. pediatrie cardiovascular)")
    parser.add_argument("--all", action="store_true", help="generează toate cele 14 capitole")
    args = parser.parse_args()

    if args.all:
        keys = list(CONTENT_KEY_TO_SLUG.keys())
    elif args.chapters:
        keys = args.chapters
    else:
        parser.error("specifică cel puțin un capitol sau --all")

    all_rows = read_rows(CSV_PATH)

    for key in keys:
        if key not in CONTENT_KEY_TO_SLUG:
            sys.exit(f"Capitol necunoscut: {key} (opțiuni: {sorted(CONTENT_KEY_TO_SLUG)})")
        slug = CONTENT_KEY_TO_SLUG[key]
        out_path = generate_chapter(slug, all_rows)
        print(f"✓ {out_path}")


if __name__ == "__main__":
    main()
