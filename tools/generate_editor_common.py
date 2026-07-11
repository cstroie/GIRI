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
    ("Radiologie intervențională — un singur capitol pentru proceduri",
     "Tot ce e intervențional (biopsii, embolizări, drenaje, angiografii "
     "terapeutice) a fost adunat într-un singur capitol nou, „Radiologie "
     "intervențională”, organizat pe aparate/sisteme. Nu mai apare împrăștiat "
     "prin capitolele diagnostice."),
    ("Excepție — senologie",
     "Intervenționalul mamar (biopsie percutanată, biopsie ganglionară "
     "axilară, localizare preoperatorie, drenaj de abces) rămâne în capitolul "
     "„Sân”, lângă restul workup-ului senologic — nu s-a mutat la Radiologie "
     "intervențională. Senologia e tratată ca specialitate proprie."),
    ("Excepție — ERCP",
     "ERCP rămâne în capitolul de origine (nu la Radiologie intervențională), "
     "deși are și rol terapeutic (sfincterotomie, extragere de calculi, "
     "stentare) — marcat „Terapeutic = Da”."),
    ("Cancerul de sân rămâne în „Sân”",
     "Deși e determinat de malignitate, cancerul de sân (diagnostic, "
     "stadializare, urmărire) nu a fost mutat la capitolul „Cancer” — rămâne "
     "în „Sân”, subcapitolul „Cancer de sân”, analog excepției ERCP."),
    ("Coloană nouă „Terapeutic” (Da/Nu)",
     "Marchează dacă o investigație/procedură are și rol terapeutic, chiar "
     "dacă e și diagnostică (ex. embolizare, ablație, drenaj = Da; biopsie, "
     "angiografie diagnostică = Nu). Gol doar la rândurile-placeholder."),
    ("Numerotarea rândurilor (NR.CRT) nu are semnificație clinică",
     "E doar un identificator secvențial de rând; a fost renumerotat de mai "
     "multe ori în timpul revizuirii și poate diferi de numerele din ediția "
     "pe care o cunoașteți. Vă rugăm să vă referiți la rânduri prin „Capitol "
     "+ Situație clinică”, nu prin numărul curent."),
    ("Un rând = un singur „acasă” (fără trimiteri încrucișate)",
     "Fiecare situație clinică apare într-un singur capitol/subcapitol, ales "
     "după o ierarhie fixă (context special — pediatric, traumă, oncologic, "
     "intervențional — înaintea anatomiei). Nu mai există trimiteri de tipul "
     "„vezi și capitolul X” în date."),
    ("Ordinea examenelor și a situațiilor clinice",
     "Ordinea investigațiilor în cadrul unei situații clinice este "
     "intenționată (reflectă prioritatea clinică) și nu a fost reordonată. "
     "Situațiile clinice din cadrul unui subcapitol au fost, unde a fost "
     "cazul, reordonate după fluxul clinic (urgență/acut → cronic → "
     "screening), nu alfabetic."),
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
        "Acest memo însoțește pachetele de review pe capitol. Conține doar "
        "deciziile structurale/organizatorice care traversează capitolele — "
        "nu conținut clinic specific. Doar de citit, nu necesită completare."
    ).italic = True

    for titlu, text in DECIZII:
        add_heading(doc, titlu, level=2)
        doc.add_paragraph(text)

    os.makedirs(OUT_DIR, exist_ok=True)
    doc.save(OUT_PATH)
    print(f"✓ {OUT_PATH}")


if __name__ == "__main__":
    main()
