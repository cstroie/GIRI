#!/usr/bin/env python3
"""Generează pentru-editori/00-comun/Decizii-structurale-comune.docx.

Memo scurt, doar de citit (nu se completează), cu deciziile structurale care
traversează capitolele — distilat din CLAUDE.md („Decizii deja luate” și
„Ierarhia capitolelor”). Conținutul e hardcodat aici (text scurt și stabil);
dacă deciziile structurale se schimbă, se editează direct această listă.

Rulează:  python3 tools/generate_editor_common.py
"""
import os

from docx import Document
from docx.shared import RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(HERE, "..")
OUT_DIR = os.path.join(REPO_ROOT, "pentru-editori", "00-comun")
OUT_PATH = os.path.join(OUT_DIR, "Decizii-structurale-comune.docx")

ACCENT = RGBColor(0x1C, 0x5D, 0x8C)

DECIZII = [
    ("Ierarhia capitolelor — de ce a plecat conținut din capitolul dvs.",
     "Un rând stă într-un singur capitol, ales după context, în această ordine: "
     "(1) pacient pediatric → Pediatrie; (2) procedură intervențională → Radiologie "
     "intervențională; (3) malignitate cunoscută/suspectată → Cancer; (4) traumă "
     "acută → Traumatisme; (5) altfel → capitolul anatomic. De asta conținutul "
     "pediatric, oncologic, traumatic sau intervențional din capitolul dvs. anatomic "
     "s-a mutat — nu a fost șters."),
    ("Radiologie intervențională — capitol unic pentru proceduri",
     "Tot ce e intervențional (biopsii, embolizări, drenaje, angiografii terapeutice) "
     "e consolidat în capitolul „Radiologie intervențională”, pe aparate/sisteme."),
    ("Excepție — senologie",
     "Intervenționalul mamar (biopsie percutanată, biopsie ganglionară axilară, "
     "localizare preoperatorie, drenaj de abces) rămâne în capitolul „Sân”."),
    ("Excepție — ERCP",
     "ERCP rămâne în capitolul de origine, marcat „Terapeutic = Da”."),
    ("Cancerul de sân rămâne în „Sân”",
     "Nu e mutat la capitolul „Cancer” — rămâne în „Sân”, subcapitolul „Cancer de sân”."),
    ("Coloană nouă „Terapeutic” (Da/Nu)",
     "Da = rol terapeutic, chiar dacă e și diagnostic (ex. embolizare, ablație, "
     "drenaj = Da; biopsie, angiografie diagnostică = Nu)."),
    ("NR.CRT nu are semnificație clinică",
     "Identificator secvențial de rând, renumerotat pe parcursul revizuirii. "
     "Referiți-vă la rânduri prin „Capitol + Situație clinică”, nu prin număr."),
    ("Un rând = un singur „acasă”",
     "Fiecare situație clinică apare într-un singur capitol/subcapitol; fără "
     "trimiteri încrucișate de tipul „vezi și capitolul X”."),
    ("Ce nu s-a schimbat",
     "Gradele de indicație, dozele și ordinea examenelor în cadrul unei situații "
     "nu au fost modificate unilateral. Unde ceva pare greșit, e semnalat ca "
     "discuție deschisă în pachetul de capitol — nu corectat de noi."),
    ("Ordinea situațiilor clinice",
     "Situațiile clinice dintr-un subcapitol sunt ordonate după flux clinic "
     "(acut → cronic → screening), nu alfabetic."),
]


def add_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = ACCENT
    return h


def main():
    doc = Document()
    add_heading(doc, "Decizii structurale comune — toate capitolele", level=1)
    intro = doc.add_paragraph()
    intro.add_run(
        "Prima revizuire a ghidului de la aprobarea din 2021. Runda aceasta: "
        "curățare structurală, deduplicare și completarea golurilor de conținut — "
        "nu o rescriere clinică. Decizii organizatorice comune tuturor capitolelor, "
        "de citit înainte de pachetul dvs. de capitol."
    ).italic = True

    for titlu, text in DECIZII:
        add_heading(doc, titlu, level=2)
        doc.add_paragraph(text)

    os.makedirs(OUT_DIR, exist_ok=True)
    doc.save(OUT_PATH)
    print(f"✓ {OUT_PATH}")


if __name__ == "__main__":
    main()
