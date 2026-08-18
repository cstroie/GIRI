#!/usr/bin/env python3
"""Generează pentru-editori/Decizii-structurale-comune.docx.

Memo scurt, doar de citit (nu se completează), cu deciziile structurale care
traversează capitolele — distilat din CLAUDE.md („Decizii deja luate” și
„Ierarhia capitolelor”). Conținutul e hardcodat aici (text scurt și stabil);
dacă deciziile structurale se schimbă, se editează direct această listă.

Artefact generat — .docx-ul nu se editează manual (se editează acest script).

Rulează:  python3 tools/generate_editor_common.py
"""
import os

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(HERE, "..")
OUT_DIR = os.path.join(REPO_ROOT, "pentru-editori")
OUT_PATH = os.path.join(OUT_DIR, "Decizii-structurale-comune.docx")

TITLU = "Decizii structurale comune — toate capitolele"
SUBTITLU = ("Revizia ghidului de indicații radioimagistice aprobat în 2021 · "
            "memo pentru editori")

ACCENT = RGBColor(0x1C, 0x5D, 0x8C)
GRI = RGBColor(0x55, 0x55, 0x55)
FONT = "Calibri"

INTRO = (
    "Documentul de față rezumă deciziile de structură aplicate uniform în toate "
    "capitolele reviziei: consolidarea procedurilor intervenționale, regula de "
    "încadrare a unei situații clinice într-un singur capitol, coloana nouă "
    "„Terapeutic” și convențiile de ordonare. Sunt decizii de organizare a "
    "conținutului, nu de conținut clinic."
)
INTRO2 = (
    "Vă rugăm să îl parcurgeți înainte de pachetul dumneavoastră de capitol: "
    "explică de ce anumite situații clinice nu mai apar acolo unde erau în "
    "versiunea din 2021. Nu necesită completare — deciziile care vă privesc "
    "direct sunt formulate ca întrebări în pachetul de capitol."
)

# (titlu, [paragrafe], [bullets])
SECTIUNI = [
    (
        "Ierarhia capitolelor — o situație clinică, un singur capitol",
        ["Ghidul urmează felul în care se pune problema în fața unui caz — "
         "întâi contextul, apoi anatomia. Când o situație clinică poate fi "
         "încadrată în mai multe capitole, se aplică prima regulă care se "
         "potrivește:"],
        [],
    ),
    (
        None,  # continuare a secțiunii de mai sus, lista numerotată
        [],
        [],
    ),
    (
        "Radiologie intervențională — capitol unic pentru proceduri",
        ["Procedurile intervenționale (biopsii, embolizări, drenaje, angiografii "
         "terapeutice) sunt consolidate într-un capitol propriu, organizat pe "
         "aparate și sisteme. Motivul: sunt proceduri terapeutice, nu opțiuni de "
         "diagnostic — locul lor nu e în lista de investigații a unei situații "
         "clinice. Două excepții:"],
        ["ERCP rămâne în capitolul de origine, marcat „Terapeutic = Da”.",
         "Intervenționalul mamar (biopsie percutanată, biopsie ganglionară axilară, "
         "localizare preoperatorie, drenaj de abces) rămâne în capitolul „Sân”, "
         "lângă restul evaluării senologice."],
    ),
    (
        "Coloana nouă „Terapeutic” (Da / Nu)",
        ["Marchează dacă investigația are rol terapeutic, chiar dacă este și "
         "diagnostică. Nu există o a treia valoare „mixt”: embolizarea, ablația "
         "și drenajul sunt „Da”; biopsia și angiografia diagnostică sunt „Nu”."],
        [],
    ),
    (
        "Identificatorul NR.CRT nu are semnificație clinică",
        ["NR.CRT este un simplu identificator de rând, folosit intern. Poate fi "
         "renumerotat integral la finalul reviziei, deci nu este stabil între "
         "versiuni. În corespondență și în comentarii, vă rugăm să vă referiți la "
         "o situație clinică prin „Capitol + Situație clinică”, nu prin număr."],
        [],
    ),
    (
        "O situație clinică = un singur „acasă”",
        ["Fiecare situație clinică apare o singură dată, într-un singur "
         "capitol și subcapitol. Trimiterile încrucișate din date („vezi și "
         "capitolul X”) au fost eliminate: navigarea după organ, peste capitole, "
         "este sarcina aplicației de consultare, nu a textului."],
        [],
    ),
    (
        "Ordinea situațiilor clinice",
        ["În fiecare subcapitol, situațiile clinice sunt ordonate după fluxul "
         "clinic — urgent/acut, apoi cronic, apoi screening și populații speciale "
         "— nu alfabetic. „ALTĂ SITUAȚIE CLINICĂ” rămâne întotdeauna ultima."],
        [],
    ),
    (
        "Ce nu s-a modificat",
        ["Gradele de indicație, dozele și ordinea examenelor în interiorul unei "
         "situații clinice au rămas neatinse. Acolo unde ceva pare discutabil, nu "
         "a fost corectat unilateral, ci este propus ca problemă de decis în "
         "pachetul de capitol."],
        [],
    ),
]

IERARHIE = [
    "Pacient pediatric → capitolul Pediatrie.",
    "Procedură intervențională → capitolul Radiologie intervențională.",
    "Malignitate cunoscută sau suspectată → capitolul Cancer.",
    "Traumatism acut → capitolul Traumatisme.",
    "În rest → capitolul anatomic (organ / aparat).",
]

IERARHIE_NOTA = (
    "Prin urmare, conținutul pediatric, oncologic, traumatic sau intervențional "
    "care era în capitolul dumneavoastră anatomic a fost mutat — nu eliminat. "
    "Senologia face excepție, ca specialitate de sine stătătoare: tot ce ține de "
    "sân, inclusiv cancerul de sân și procedurile intervenționale mamare, rămâne "
    "în capitolul „Sân”."
)

BOARD_INTRO = (
    "Structura actuală — contextul înaintea anatomiei — rămâne neschimbată pentru "
    "această revizie. Semnalăm însă, pentru o discuție separată de board după "
    "încheierea reviewului, câteva fragmentări transversale moștenite:"
)

FRAGMENTARI = [
    "Axul neurologic este împărțit între „Cap › Neuro” și „Coloană vertebrală” — "
    "encefalul, separat de măduvă și coloană.",
    "Sfera ORL este împărțită între „Cap › ORL” și „Gât (părți moi)”.",
    "Patologia vasculară este dispersată: cordul la Cardiovascular, carotidele la "
    "Neuro, teritoriul periferic la Radiologie intervențională.",
    "Patologia endocrină este dispersată: tiroida la Gât, suprarenalele la "
    "Uro-genital, hipofiza la Cap.",
]

BOARD_OUTRO = (
    "Direcția pe care o propunem spre analiză: un capitol „Sistem nervos” "
    "(encefal, măduvă, coloană vertebrală) și un capitol „Cap și gât” (ORL, "
    "tiroidă, mase cervicale). Nimic din acestea nu se decide acum și nu "
    "afectează pachetul de față."
)

INCHEIERE = ("Orice observație sau propunere suplimentară este binevenită și va fi "
             "supusă discuției comune.")


# --- helpers docx --------------------------------------------------------

def set_base_style(doc):
    """Font și spațiere de bază, uniforme pentru tot documentul."""
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    pf = normal.paragraph_format
    pf.space_after = Pt(8)
    pf.line_spacing = 1.15

    for name, size, before, after in (
        ("Heading 1", 20, 0, 6),
        ("Heading 2", 13, 14, 4),
        ("List Bullet", 11, 0, 4),
        ("List Number", 11, 0, 4),
    ):
        st = doc.styles[name]
        st.font.name = FONT
        st.font.size = Pt(size)
        st.font.color.rgb = ACCENT if name.startswith("Heading") else None
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        if name.startswith("Heading"):
            st.font.bold = True


def set_page(doc):
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21.0), Cm(29.7)  # A4
    section.top_margin = section.bottom_margin = Cm(2.0)
    section.left_margin = section.right_margin = Cm(2.2)


def add_field(paragraph, instr):
    """Inserează un câmp Word (ex. PAGE / NUMPAGES) într-un paragraf."""
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr_el = OxmlElement("w:instrText")
    instr_el.set(qn("xml:space"), "preserve")
    instr_el.text = instr
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for el in (begin, instr_el, end):
        run._r.append(el)
    return run


def add_footer(doc):
    """Subsol: titlul scurt la stânga, „Pagina X din Y” la dreapta."""
    section = doc.sections[0]
    p = section.footer.paragraphs[0]
    # Stilul „Footer” aduce tabulatori moșteniți (centru 4680, dreapta 9360
    # twips, pentru pagină Letter); îi anulăm ca tabul să ajungă la marginea A4.
    for pos in (Pt(234), Pt(468)):  # 4680 / 9360 twips
        p.paragraph_format.tab_stops.add_tab_stop(pos, WD_TAB_ALIGNMENT.CLEAR)
    p.paragraph_format.tab_stops.add_tab_stop(
        section.page_width - section.left_margin - section.right_margin,
        WD_TAB_ALIGNMENT.RIGHT,
    )
    run = p.add_run("Decizii structurale comune\t")
    run.font.size = Pt(9)
    run.font.color.rgb = GRI
    pag = p.add_run("Pagina ")
    pag.font.size = Pt(9)
    pag.font.color.rgb = GRI
    for instr, sep in (("PAGE", " din "), ("NUMPAGES", "")):
        f = add_field(p, instr)
        f.font.size = Pt(9)
        f.font.color.rgb = GRI
        if sep:
            r = p.add_run(sep)
            r.font.size = Pt(9)
            r.font.color.rgb = GRI


def add_rule(doc):
    """Linie orizontală subțire, în culoarea de accent."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(10)
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "1C5D8C")
    pbdr.append(bottom)
    p._p.get_or_add_pPr().append(pbdr)
    return p


def add_heading(doc, text, level=2, number=None):
    label = f"{number}. {text}" if number else text
    return doc.add_heading(label, level=level)


def add_note(doc, text):
    """Paragraf de notă — gri, italic, ușor indentat."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.6)
    run = p.add_run(text)
    run.italic = True
    run.font.color.rgb = GRI
    return p


def set_docprops(doc):
    core = doc.core_properties
    core.title = TITLU
    core.subject = "Revizia ghidului de indicații radioimagistice"
    core.category = "Memo pentru editori"
    core.comments = "Artefact generat de tools/generate_editor_common.py"


# --- document ------------------------------------------------------------

def build(doc):
    set_base_style(doc)
    set_page(doc)
    set_docprops(doc)
    add_footer(doc)

    doc.add_heading(TITLU, level=1)
    sub = doc.add_paragraph()
    sub.paragraph_format.space_after = Pt(2)
    run = sub.add_run(SUBTITLU)
    run.font.size = Pt(10.5)
    run.font.color.rgb = GRI
    run.bold = True
    add_rule(doc)

    doc.add_paragraph(INTRO)
    doc.add_paragraph(INTRO2)

    numar = 0
    for titlu, paragrafe, bullets in SECTIUNI:
        if titlu is None:
            for item in IERARHIE:
                doc.add_paragraph(item, style="List Number")
            add_note(doc, IERARHIE_NOTA)
            continue
        numar += 1
        add_heading(doc, titlu, level=2, number=numar)
        for text in paragrafe:
            doc.add_paragraph(text)
        for item in bullets:
            doc.add_paragraph(item, style="List Bullet")

    numar += 1
    add_heading(doc, "Întrebare de board, după încheierea reviewului: structura de capitole",
                level=2, number=numar)
    doc.add_paragraph(BOARD_INTRO)
    for frag in FRAGMENTARI:
        doc.add_paragraph(frag, style="List Bullet")
    doc.add_paragraph(BOARD_OUTRO)

    add_rule(doc)
    closing = doc.add_paragraph()
    closing.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = closing.add_run(INCHEIERE)
    run.italic = True
    run.font.color.rgb = GRI


def main():
    doc = Document()
    build(doc)
    os.makedirs(OUT_DIR, exist_ok=True)
    doc.save(OUT_PATH)
    print(f"✓ {OUT_PATH}")


if __name__ == "__main__":
    main()
