#!/usr/bin/env python3
"""Generează GHID.html — versiune HTML lizibilă a GHID.csv.

Rulează:  python3 tools/generate_html.py
Scrie:    GHID.html (fișier unic, CSS inclus, fără JS, fără dependențe externe)

GHID.html e un artefact generat — nu se editează manual. Sursa canonică
rămâne GHID.csv (vezi CLAUDE.md, regula de aur #1).
"""
import csv
import html
import os
import re
import subprocess
import sys
import unicodedata

from validate import EXPECTED_HEADER

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(HERE, "..")
DEFAULT_INPUT = os.path.join(REPO_ROOT, "GHID.csv")
DEFAULT_OUTPUT = os.path.join(REPO_ROOT, "GHID.html")

TIP_LABELS = {
    "G": "Radiografie",
    "E": "Ecografie / Doppler",
    "M": "IRM",
    "T": "CT",
    "N": "Medicină nucleară",
    "X": "Contrast / fluoroscopie",
    "D": "Diagnostic invaziv / endoscopic",
    "I": "Intervențional",
    "A": "Angiografie invazivă",
    "Z": "Placeholder",
}

GRAD_LABELS = {
    "A": "Dovezi solide",
    "B": "Dovezi moderate",
    "C": "Consens / dovezi limitate",
    "?": "Neprecizat",
}

# valoare din coloana Indicație -> (clasă CSS, etichetă scurtă afișată)
INDICATIE_STYLE = {
    "Indicat": ("indicat", "Indicat"),
    "Doar în cazuri particulare": ("particular", "Cazuri particulare"),
    "Doar cu aviz specializat": ("aviz", "Aviz specializat"),
    "Este necesară justificare detaliată": ("justificare", "Justificare detaliată"),
    "Neindicat": ("neindicat", "Neindicat"),
    "Neindicat în primă intenție": ("neindicat-prima", "Neindicat în primă intenție"),
    "Vezi Detalii Ghid!": ("detalii", "Vezi Detalii Ghid!"),
    "": ("unknown", "—"),
}


def slugify(text, seen):
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    slug = slug or "sect"
    base = slug
    n = 2
    while slug in seen:
        slug = f"{base}-{n}"
        n += 1
    seen.add(slug)
    return slug


def read_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != EXPECTED_HEADER:
            sys.exit(f"Antet neașteptat în {path}:\n  {reader.fieldnames}")
        rows = list(reader)
    for i, row in enumerate(rows, start=2):
        if len(row) != len(EXPECTED_HEADER):
            sys.exit(f"Linia {i}: număr de coloane neașteptat (rulează tools/validate.py)")
    return rows


def build_tree(rows):
    tree = {}
    for row in rows:
        cap = tree.setdefault(row["Capitol"], {})
        sub = cap.setdefault(row["Subcapitol"], {})
        sub.setdefault(row["Situația Clinică"], []).append(row)
    return tree


def source_last_update():
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", "GHID.csv"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        return out.split("T")[0] if out else "necunoscută"
    except Exception:
        return "necunoscută"


def esc(text):
    return html.escape(text or "", quote=True)


def render_exam(row):
    tip = row["Tip"].strip()
    tip_label = TIP_LABELS.get(tip, tip or "?")
    indicatie = row["Indicație"].strip()
    indic_class, indic_label = INDICATIE_STYLE.get(indicatie, ("unknown", indicatie or "—"))
    grad = row["Grad Indicație"].strip()
    grad_label = GRAD_LABELS.get(grad, grad)

    badges = [f'<span class="badge tip" title="{esc(tip_label)}">{esc(tip)}</span>']
    badges.append(f'<span class="badge indic indic-{indic_class}">{esc(indic_label)}</span>')
    if grad:
        badges.append(f'<span class="badge grad" title="{esc(grad_label)}">Grad {esc(grad)}</span>')
    if row["Terapeutic"].strip() == "Da":
        badges.append('<span class="badge terapeutic">Terapeutic</span>')

    doza_min, doza_max = row["Doza Min"].strip(), row["Doza Max"].strip()
    if doza_min or doza_max:
        doza = doza_min if doza_min == doza_max else f"{doza_min}–{doza_max}"
        badges.append(f'<span class="badge doza">Doză {esc(doza)}</span>')

    parts = [f'<li class="exam-item"><div class="exam-head">',
              f'<span class="exam-name">{esc(row["Examen"])}</span>',
              '<span class="badge-row">' + "".join(badges) + '</span>',
              '</div>']
    if row["Comentarii"].strip():
        parts.append(f'<p class="exam-note">{esc(row["Comentarii"])}</p>')
    if row["Alte informații"].strip():
        parts.append(f'<p class="exam-extra">{esc(row["Alte informații"])}</p>')
    parts.append("</li>")
    return "".join(parts)


def render_body(tree):
    seen_ids = set()
    toc_parts = ['<nav id="toc" aria-label="Cuprins"><h2>Cuprins</h2><ol class="toc-cap">']
    body_parts = []

    for capitol, subs in tree.items():
        cap_count = sum(len(rows) for sub in subs.values() for rows in sub.values())
        cap_id = slugify(capitol, seen_ids)
        toc_parts.append(f'<li><a href="#{cap_id}">{esc(capitol)}</a> '
                          f'<span class="toc-count">({cap_count})</span><ol class="toc-sub">')
        body_parts.append(f'<section class="capitol" id="{cap_id}">')
        body_parts.append(f'<h1>{esc(capitol)} <a class="top-link" href="#toc">↑ cuprins</a></h1>')

        for subcapitol, situatii in subs.items():
            sub_id = slugify(f"{capitol}-{subcapitol}", seen_ids)
            toc_parts.append(f'<li><a href="#{sub_id}">{esc(subcapitol)}</a></li>')
            body_parts.append(f'<section class="subcapitol" id="{sub_id}">')
            body_parts.append(f'<h2>{esc(subcapitol)}</h2>')

            for situatie, rows in situatii.items():
                body_parts.append('<article class="situatie">')
                body_parts.append(f'<h3>{esc(situatie)}</h3>')
                body_parts.append('<ul class="exam-list">')
                body_parts.extend(render_exam(r) for r in rows)
                body_parts.append('</ul>')
                body_parts.append('</article>')

            body_parts.append('</section>')

        toc_parts.append('</ol></li>')
        body_parts.append('</section>')

    toc_parts.append('</ol></nav>')
    return "".join(toc_parts), "".join(body_parts)


CSS = """
:root {
  --fg: #1c2530; --muted: #5b6774; --bg: #ffffff; --bg-alt: #f4f6f8;
  --border: #dde3e8; --accent: #1c5d8c; --accent-bg: #eaf2f8;
  --indicat: #1e7d3c; --indicat-bg: #e7f5eb;
  --neindicat: #b02a2a; --neindicat-bg: #fbe9e9;
  --particular: #9a6a00; --particular-bg: #fbf1dc;
  --detalii: #5b3fa0; --detalii-bg: #efe9f9;
  --terapeutic: #0b6e6e; --terapeutic-bg: #e2f4f4;
  --grad: #4a5a7a; --grad-bg: #eef1f7;
  --doza: #7a5a86; --doza-bg: #f2ecf6;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg-alt); color: var(--fg);
  font: 16px/1.5 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.page-header {
  background: var(--accent); color: #fff; padding: 2rem 1.25rem;
}
.page-header h1 { margin: 0 0 .25rem; font-size: 1.6rem; }
.page-header p { margin: 0; opacity: .85; font-size: .9rem; }
main { max-width: 900px; margin: 0 auto; padding: 1.25rem; }
#toc {
  background: var(--bg); border: 1px solid var(--border); border-radius: 8px;
  padding: 1rem 1.25rem; margin-bottom: 1.5rem;
}
#toc h2 { margin-top: 0; font-size: 1.1rem; }
#toc ol { margin: 0; padding-left: 1.25rem; }
.toc-cap > li { margin: .4rem 0; font-weight: 600; }
.toc-sub { font-weight: 400; padding-left: 1.1rem; margin-top: .25rem; }
.toc-sub li { margin: .15rem 0; font-size: .92rem; }
.toc-count { color: var(--muted); font-weight: 400; font-size: .85em; }
#toc a { color: var(--accent); text-decoration: none; }
#toc a:hover { text-decoration: underline; }
.legend {
  background: var(--bg); border: 1px solid var(--border); border-radius: 8px;
  padding: 1rem 1.25rem; margin-bottom: 1.5rem; font-size: .9rem;
}
.legend h2 { margin-top: 0; font-size: 1.1rem; }
.legend dl { display: grid; grid-template-columns: max-content 1fr; gap: .25rem .75rem; margin: 0; }
.legend dt { font-weight: 600; }
.legend dd { margin: 0; color: var(--muted); }
section.capitol {
  background: var(--bg); border: 1px solid var(--border); border-radius: 8px;
  padding: 0 1.25rem 1rem; margin-bottom: 1.5rem;
}
section.capitol h1 {
  font-size: 1.4rem; border-bottom: 2px solid var(--accent);
  padding: 1rem 0 .6rem; margin: 0 0 .75rem;
  display: flex; align-items: baseline; justify-content: space-between; gap: 1rem;
}
.top-link { font-size: .75rem; font-weight: 400; color: var(--muted); text-decoration: none; white-space: nowrap; }
.top-link:hover { text-decoration: underline; }
section.subcapitol { margin: 1.25rem 0; }
section.subcapitol h2 {
  font-size: 1.15rem; color: var(--accent); margin: 0 0 .6rem;
  padding-bottom: .3rem; border-bottom: 1px solid var(--border);
}
article.situatie { margin: 0 0 1rem; }
article.situatie h3 { font-size: 1rem; margin: 0 0 .4rem; }
.exam-list { list-style: none; margin: 0; padding: 0; }
.exam-item {
  border: 1px solid var(--border); border-radius: 6px; background: var(--bg-alt);
  padding: .55rem .75rem; margin-bottom: .5rem; page-break-inside: avoid;
}
.exam-head { display: flex; flex-wrap: wrap; align-items: center; gap: .4rem .6rem; }
.exam-name { font-weight: 600; }
.badge-row { display: inline-flex; flex-wrap: wrap; gap: .35rem; }
.badge {
  display: inline-block; font-size: .74rem; line-height: 1.5; padding: .05rem .5rem;
  border-radius: 999px; border: 1px solid transparent; white-space: nowrap;
}
.badge.tip { background: var(--accent-bg); color: var(--accent); border-color: var(--accent); font-weight: 700; }
.badge.grad { background: var(--grad-bg); color: var(--grad); }
.badge.doza { background: var(--doza-bg); color: var(--doza); }
.badge.terapeutic { background: var(--terapeutic-bg); color: var(--terapeutic); }
.indic-indicat { background: var(--indicat-bg); color: var(--indicat); }
.indic-particular { background: var(--particular-bg); color: var(--particular); }
.indic-aviz { background: var(--particular-bg); color: var(--particular); }
.indic-justificare { background: var(--particular-bg); color: var(--particular); }
.indic-neindicat { background: var(--neindicat-bg); color: var(--neindicat); }
.indic-neindicat-prima { background: var(--neindicat-bg); color: var(--neindicat); }
.indic-detalii { background: var(--detalii-bg); color: var(--detalii); }
.indic-unknown { background: var(--bg); color: var(--muted); border-color: var(--border); }
.exam-note { margin: .4rem 0 0; color: var(--fg); font-size: .92rem; }
.exam-extra { margin: .3rem 0 0; color: var(--muted); font-size: .82rem; font-style: italic; }
footer { text-align: center; color: var(--muted); font-size: .82rem; padding: 1.5rem 1rem 2.5rem; }
@media (max-width: 600px) {
  main { padding: .75rem; }
  section.capitol { padding: 0 .75rem .75rem; }
  .page-header { padding: 1.25rem .9rem; }
}
@media print {
  body { background: #fff; }
  #toc { break-after: page; }
  section.capitol { border: none; box-shadow: none; }
  .top-link { display: none; }
}
"""

LEGEND_HTML = """
<div class="legend">
<h2>Legendă</h2>
<dl>
<dt>Tip G</dt><dd>Radiografie (grafie convențională, mamografie)</dd>
<dt>Tip E</dt><dd>Ecografie / Doppler</dd>
<dt>Tip M</dt><dd>IRM / RM</dd>
<dt>Tip T</dt><dd>CT</dd>
<dt>Tip N</dt><dd>Medicină nucleară (PET-CT, scintigrafie)</dd>
<dt>Tip X</dt><dd>Radiologie cu contrast / fluoroscopie</dd>
<dt>Tip D</dt><dd>Diagnostic invaziv / endoscopic</dd>
<dt>Tip I</dt><dd>Intervențional</dd>
<dt>Tip A</dt><dd>Angiografie invazivă</dd>
<dt>Tip Z</dt><dd>Placeholder / situație clinică neîncadrabilă</dd>
<dt>Grad A</dt><dd>Dovezi solide</dd>
<dt>Grad B</dt><dd>Dovezi moderate</dd>
<dt>Grad C</dt><dd>Consens / dovezi limitate</dd>
<dt>Grad ?</dt><dd>Neprecizat</dd>
</dl>
</div>
"""


def render(tree, row_count):
    toc_html, body_html = render_body(tree)
    updated = source_last_update()
    return f"""<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ghid de Indicații Radioimagistice</title>
<style>{CSS}</style>
</head>
<body>
<header class="page-header">
<h1>Ghid de Indicații Radioimagistice</h1>
<p>{row_count} situații de examen &middot; sursă actualizată la {esc(updated)} &middot;
generat automat din GHID.csv — nu edita acest fișier direct</p>
</header>
<main>
{toc_html}
{LEGEND_HTML}
{body_html}
</main>
<footer>Generat automat din <code>GHID.csv</code> de <code>tools/generate_html.py</code>.</footer>
</body>
</html>
"""


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    output_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUTPUT

    rows = read_rows(input_path)
    tree = build_tree(rows)
    html_out = render(tree, len(rows))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Scris {output_path} ({len(rows)} rânduri, {len(html_out)} caractere).")


if __name__ == "__main__":
    main()
