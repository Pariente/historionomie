#!/usr/bin/env python3
"""
Generate an interactive HTML timeline from a structured Markdown file
describing a nation's Parcours de construction nationale.

Usage:
    python generate_timeline.py references/nations/france/parcours_h3.md -o france_h3.html
"""

import argparse
import re
import sys
import os
from datetime import date


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_date(val: str):
    """Return (numeric_year, is_approximate). Handles ~, negatives, BCE."""
    if val is None:
        return None, False
    val = val.strip()
    approx = val.startswith("~")
    if approx:
        val = val[1:]
    try:
        return int(val), approx
    except ValueError:
        return None, approx


def parse_parcours(filepath: str) -> dict:
    """Parse a parcours Markdown file and return structured data."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")

    result = {
        "title": "",
        "metadata": {},
        "prephase": None,
        "elements": [],  # flat list of phases, subphases, saillants, perturbations
    }

    # Extract title (first H1)
    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            result["title"] = line[2:].strip()
            break

    # Split into sections by ## headings
    sections = []
    current_section_lines = []
    current_heading = ""

    for line in lines:
        if line.startswith("## "):
            if current_heading or current_section_lines:
                sections.append((current_heading, current_section_lines))
            current_heading = line
            current_section_lines = []
        else:
            current_section_lines.append(line)

    if current_heading or current_section_lines:
        sections.append((current_heading, current_section_lines))

    for heading, sec_lines in sections:
        heading_text = heading.strip()

        # Metadata section
        if heading_text.startswith("## Metadata"):
            result["metadata"] = parse_fields(sec_lines)
            continue

        # Pré-phase
        if "Pré-phase" in heading_text or "Pre-phase" in heading_text:
            fields = parse_fields(sec_lines)
            # Extract the heading label
            m = re.match(r"##\s+Pré-phase\s*:\s*(.*)", heading_text)
            label = m.group(1).strip() if m else heading_text.replace("## ", "")
            result["prephase"] = {
                "label": label,
                "description": fields.get("description", ""),
            }
            continue

        # Phase, perturbation, subphase, saillant — parse subsections
        all_sub_lines = [heading] + sec_lines
        sub_sections = split_by_headings(all_sub_lines)

        current_phase = ""
        for sub_heading, sub_lines in sub_sections:
            element = parse_element(sub_heading, sub_lines)
            if element and element.get("type") != "note":
                # Track current phase for children that lack a phase field
                if element["kind"] == "phase" and element["phase"]:
                    current_phase = element["phase"]
                elif not element["phase"] and current_phase:
                    element["phase"] = current_phase
                result["elements"].append(element)

    # Second pass: propagate phase from phases to subsequent elements that lack one
    current_phase = ""
    for e in result["elements"]:
        if e["kind"] == "phase" and e["phase"]:
            current_phase = e["phase"]
        elif not e["phase"] and current_phase:
            e["phase"] = current_phase

    return result


def split_by_headings(lines: list) -> list:
    """Split lines into (heading, body_lines) groups by any heading level (##, ###, ####)."""
    sections = []
    current_heading = ""
    current_lines = []

    for line in lines:
        if re.match(r"^#{2,4}\s", line):
            if current_heading:
                sections.append((current_heading, current_lines))
            current_heading = line
            current_lines = []
        else:
            current_lines.append(line)

    if current_heading:
        sections.append((current_heading, current_lines))

    return sections


def parse_fields(lines: list) -> dict:
    """Parse key-value fields from lines like '- key: value'. Handles multi-line values."""
    fields = {}
    current_key = None
    current_val = []

    for line in lines:
        m = re.match(r"^- (\w[\w_]*)\s*:\s*(.*)", line)
        if m:
            if current_key is not None:
                fields[current_key] = "\n".join(current_val).strip()
            current_key = m.group(1)
            current_val = [m.group(2)]
        elif current_key is not None and line.startswith("  "):
            current_val.append(line.strip())
        # other lines (blank, ---) just ignored

    if current_key is not None:
        fields[current_key] = "\n".join(current_val).strip()

    return fields


def parse_element(heading: str, body_lines: list) -> dict:
    """Parse a single element (phase, subphase, saillant, perturbation) from heading + body."""
    fields = parse_fields(body_lines)
    if not fields:
        return None

    etype = fields.get("type", "")

    # Determine element kind from heading pattern
    heading_clean = heading.strip()
    kind = None
    heading_label = ""
    if heading_clean.startswith("## Phase"):
        kind = "phase"
        m = re.match(r"##\s+Phase\s*:\s*(.*)", heading_clean)
        heading_label = m.group(1).strip() if m else ""
    elif heading_clean.startswith("### Subphase") or heading_clean.startswith("### Sous-phase"):
        kind = "subphase"
        m = re.match(r"###\s+(?:Subphase|Sous-phase)\s*:\s*(.*)", heading_clean)
        heading_label = m.group(1).strip() if m else ""
    elif heading_clean.startswith("#### Saillant"):
        kind = "saillant"
        m = re.match(r"####\s+Saillant\s*:\s*(.*)", heading_clean)
        heading_label = m.group(1).strip() if m else ""
    elif heading_clean.startswith("### Perturbation"):
        kind = "perturbation"
        m = re.match(r"###\s+Perturbation\s*:\s*(.*)", heading_clean)
        heading_label = m.group(1).strip() if m else ""
    elif heading_clean.startswith("## Pré-phase") or heading_clean.startswith("## Pre-phase"):
        return None  # handled separately

    if kind is None and etype:
        kind = etype

    if kind is None:
        return None

    start_year, start_approx = parse_date(fields.get("start"))
    end_year, end_approx = parse_date(fields.get("end"))

    return {
        "kind": kind,
        "type": etype or kind,
        "phase": fields.get("phase", ""),
        "start": start_year,
        "start_approx": start_approx,
        "end": end_year,
        "end_approx": end_approx,
        "title": fields.get("title", heading_label),
        "summary": fields.get("summary", ""),
        "description": fields.get("description", ""),
        "figure": fields.get("figure", ""),
        "confidence": fields.get("confidence", ""),
        "alternatives": fields.get("alternatives", ""),
        "step": fields.get("step", ""),
        "deviation": fields.get("deviation", ""),
        "typical_duration": fields.get("typical_duration", ""),
        "perturbation_type": fields.get("perturbation_type", ""),
        "affected_motor": fields.get("affected_motor", ""),
        "note": fields.get("note", ""),
        "resolution": fields.get("resolution", ""),
        "resolution_conditions": fields.get("resolution_conditions", ""),
        "avortement": fields.get("avortement", ""),
        "narrative": fields.get("narrative", ""),
    }


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

PHASE_COLORS = {
    "feodale": "#8B7355",
    "oligarchique": "#2E8B57",
    "absolutiste": "#6A0DAD",
    "rn": "#D4A017",
    "parlementaire": "#1E90FF",
    "technocratique": "#708090",
}

SAILLANT_ICONS = {
    "Éveil féodal": "wb_sunny",
    "Pic féodal": "terrain",
    "Crise féodale": "bolt",
    "Pacte oligarchique": "gavel",
    "1er monarque oligarchique": "stars",
    "Pic oligarchique": "terrain",
    "Fin de l'expansion": "block",
    "Guerre sociale": "local_fire_department",
    "1er monarque absolu": "crown",
    "1er monarque absolu (du reboot)": "crown",
    "Dernière grande révolte oligarchique": "whatshot",
    "Pic absolutiste": "terrain",
    "Explosion de l'AR": "flash_on",
    "Expérience parlementaire": "account_balance",
    "Phase aiguë": "skull",
    "Moment thermidorien": "balance",
    "Émergence de l'IR": "military_tech",
    "Impérialiste Revanchard": "military_tech",
    "Glorieuse Révolution": "star",
    "Reconstruction": "construction",
    "Codification de la Torah": "menu_book",
    "Destruction du 1er Temple": "cancel",
    "Invasion macédonienne": "cancel",
    "Écrasement": "cancel",
    "Liquidation définitive": "cancel",
    "Réduction d'échelle": "compress",
    "Magna Carta": "description",
}
SAILLANT_ICON_DEFAULT = "diamond"
SAILLANT_ICON_AVORTEMENT = "cancel"

PHASE_LABELS = {
    "feodale": "Féodale",
    "oligarchique": "Oligarchique",
    "absolutiste": "Absolutiste",
    "rn": "Révolution Nationale",
    "parlementaire": "Parlementaire",
    "technocratique": "Technocratique",
}


def lighten_hex(hex_color: str, factor: float = 0.35) -> str:
    """Make a hex color lighter by blending towards white."""
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)
    return f"#{r:02x}{g:02x}{b:02x}"


def very_light_hex(hex_color: str) -> str:
    return lighten_hex(hex_color, 0.75)


def escape_html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")


def escape_js_string(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n").replace("\r", "")


def format_year(year, approx=False):
    if year is None:
        return "?"
    prefix = "~" if approx else ""
    if year < 0:
        return f"{prefix}-{abs(year)}"
    return f"{prefix}{year}"


def generate_html(data: dict) -> str:
    elements = data["elements"]

    # Compute timeline bounds
    all_years = []
    for e in elements:
        if e["start"] is not None:
            all_years.append(e["start"])
        if e["end"] is not None:
            all_years.append(e["end"])

    if data.get("prephase"):
        # Try to get a start year from the metadata
        meta_start, _ = parse_date(data["metadata"].get("start"))
        if meta_start is not None:
            all_years.append(meta_start)

    if not all_years:
        return "<html><body>No timeline data found.</body></html>"

    min_year = min(all_years)
    max_year = max(all_years)

    # If there are ongoing phases (no end), extend to current year + some margin
    current_year = date.today().year
    for e in elements:
        if e["kind"] == "phase" and e["end"] is None:
            max_year = max(max_year, current_year)

    # Add padding
    year_padding = max(20, int((max_year - min_year) * 0.03))
    timeline_start = min_year - year_padding
    timeline_end = max_year + year_padding
    timeline_span = timeline_end - timeline_start

    # Separate element types
    phases = [e for e in elements if e["kind"] == "phase"]
    subphases = [e for e in elements if e["kind"] == "subphase"]
    saillants = [e for e in elements if e["kind"] == "saillant"]
    perturbations = [e for e in elements if e["kind"] == "perturbation"]

    meta = data["metadata"]
    nation = meta.get("nation", "Nation inconnue")
    hypothesis = meta.get("hypothesis", "")
    status = meta.get("status", "")
    territory = meta.get("territory", "")
    meta_confidence = meta.get("confidence", "")

    # Build JSON data for JS
    elements_json_parts = []
    for i, e in enumerate(elements):
        parts = []
        for key in ["kind", "type", "phase", "title", "summary", "description",
                     "figure", "confidence", "alternatives", "step", "deviation",
                     "typical_duration", "perturbation_type", "affected_motor", "note",
                     "resolution", "resolution_conditions", "avortement", "narrative"]:
            parts.append(f"'{key}':'{escape_js_string(str(e.get(key, '')))}'")
        parts.append(f"'start':{e['start'] if e['start'] is not None else 'null'}")
        parts.append(f"'end':{e['end'] if e['end'] is not None else 'null'}")
        parts.append(f"'start_approx':{'true' if e['start_approx'] else 'false'}")
        parts.append(f"'end_approx':{'true' if e['end_approx'] else 'false'}")
        elements_json_parts.append("{" + ",".join(parts) + "}")

    elements_js = "[" + ",".join(elements_json_parts) + "]"

    # Pre-phase info
    prephase_html = ""
    if data.get("prephase"):
        pp = data["prephase"]
        prephase_html = f"""
        <div class="prephase-note">
            <strong>Pré-phase : {escape_html(pp['label'])}</strong><br>
            <span>{escape_html(pp['description'])}</span>
        </div>"""

    # Build phase bands HTML
    phase_bands_html = ""
    for p in phases:
        start = p["start"] if p["start"] is not None else timeline_start
        end = p["end"] if p["end"] is not None else current_year
        color = PHASE_COLORS.get(p["phase"], "#999")
        bg = very_light_hex(color)
        border_color = color
        left_pct = ((start - timeline_start) / timeline_span) * 100
        width_pct = ((end - start) / timeline_span) * 100

        conf = p.get("confidence", "high")
        border_style = "solid"
        if conf == "medium":
            border_style = "dashed"
        elif conf == "low":
            border_style = "dotted"

        start_label = format_year(p["start"], p["start_approx"])
        end_label = format_year(p["end"], p["end_approx"]) if p["end"] else "en cours"

        phase_bands_html += f"""
        <div class="phase-band" style="left:{left_pct:.4f}%;width:{width_pct:.4f}%;
            background:{bg};border-top:3px {border_style} {color};border-right:1px solid #fff;"
            data-tooltip="&lt;strong&gt;{escape_html(p['title'])}&lt;/strong&gt; ({start_label} — {end_label})&#10;{escape_html(p['summary'])}"
            onclick="showDetail({elements.index(p)})">
            <div class="phase-band-label" style="color:{color};">{escape_html(p['title'])}</div>
            <div class="phase-band-dates">{start_label} — {end_label}</div>
        </div>"""

    # Build subphase bands
    subphase_bands_html = ""
    for sp in subphases:
        start = sp["start"] if sp["start"] is not None else timeline_start
        end = sp["end"] if sp["end"] is not None else current_year
        color = PHASE_COLORS.get(sp["phase"], "#999")
        bg = lighten_hex(color, 0.55)
        left_pct = ((start - timeline_start) / timeline_span) * 100
        width_pct = ((end - start) / timeline_span) * 100

        step_label = f" (ét. {sp['step']})" if sp.get("step") else ""
        start_label = format_year(sp["start"], sp["start_approx"])
        end_label = format_year(sp["end"], sp["end_approx"]) if sp["end"] else "en cours"

        narrow_class = ""
        if width_pct < 2:
            narrow_class = " very-narrow"
        elif width_pct < 5:
            narrow_class = " narrow"
        subphase_bands_html += f"""
        <div class="subphase-band{narrow_class}" style="left:{left_pct:.4f}%;width:{width_pct:.4f}%;
            background:{bg};border-bottom:2px solid {color};"
            data-tooltip="&lt;strong&gt;{escape_html(sp['title'])}{step_label}&lt;/strong&gt; ({start_label} — {end_label})&#10;{escape_html(sp['summary'])}"
            onclick="showDetail({elements.index(sp)})">
            <span class="subphase-label">{escape_html(sp['title'])}{step_label}</span>
        </div>"""

    # Build perturbation overlays
    perturbation_html = ""
    for pt in perturbations:
        start = pt["start"] if pt["start"] is not None else timeline_start
        end = pt["end"] if pt["end"] is not None else current_year
        left_pct = ((start - timeline_start) / timeline_span) * 100
        width_pct = ((end - start) / timeline_span) * 100

        ptype = pt.get("perturbation_type", "")
        start_label = format_year(pt["start"], pt["start_approx"])
        end_label = format_year(pt["end"], pt["end_approx"]) if pt["end"] else "?"

        pt_narrow = " narrow" if width_pct < 4 else ""
        perturbation_html += f"""
        <div class="perturbation-overlay{pt_narrow}" style="left:{left_pct:.4f}%;width:{width_pct:.4f}%;"
            data-tooltip="&lt;strong&gt;{escape_html(pt['title'])}&lt;/strong&gt; ({start_label} — {end_label})&#10;Type : {escape_html(ptype)}&#10;{escape_html(pt['summary'])}"
            onclick="showDetail({elements.index(pt)})">
            <span class="perturbation-label">{escape_html(pt['title'])}</span>
        </div>"""

    # Build saillant markers — with staggered labels to avoid overlap
    # Sort saillants by start date and assign vertical levels
    dated_saillants = [(s, ((s["start"] - timeline_start) / timeline_span) * 100)
                       for s in saillants if s["start"] is not None]
    dated_saillants.sort(key=lambda x: x[1])

    # Assign stagger levels (0-4): default to row 0, bump down only if conflict
    # A saillant "occupies" a horizontal band of ~7% around its position
    MAX_ROWS = 6
    ROW_HEIGHT = 65  # px per row
    CONFLICT_RADIUS = 4  # % of timeline width — two saillants within this range conflict

    levels = []
    for i, (s, pct) in enumerate(dated_saillants):
        # Check which rows are occupied by NEARBY saillants only
        occupied_rows = set()
        for j in range(i):
            _, prev_pct = dated_saillants[j]
            if abs(pct - prev_pct) < CONFLICT_RADIUS:
                occupied_rows.add(levels[j])
        # Pick the lowest free row
        level = 0
        while level in occupied_rows and level < MAX_ROWS - 1:
            level += 1
        levels.append(level)

    level_offsets = {i: i * ROW_HEIGHT for i in range(MAX_ROWS)}

    saillant_markers_html = ""
    for (s, left_pct), level in zip(dated_saillants, levels):
        color = PHASE_COLORS.get(s["phase"], "#333")
        offset = level_offsets[level]

        figure_label = s["figure"] if s["figure"] else s["title"]
        start_label = format_year(s["start"], s["start_approx"])

        is_avortement = s.get("avortement") == "true"
        avortement_class = " avortement" if is_avortement else ""
        if is_avortement:
            icon_name = SAILLANT_ICON_AVORTEMENT
        else:
            icon_name = SAILLANT_ICONS.get(s["title"], SAILLANT_ICON_DEFAULT)
        bg_color = "#c0392b" if is_avortement else color
        saillant_markers_html += f"""
        <div class="saillant-group" style="left:{left_pct:.4f}%;top:{200 + offset}px;">
            <div class="saillant-marker{avortement_class}" style="background:{bg_color};"
                data-tooltip="&lt;strong&gt;{escape_html(s['title'])}&lt;/strong&gt;&#10;{escape_html(figure_label)} ({start_label})&#10;{escape_html(s['summary'])}"
                onclick="showDetail({elements.index(s)})">
                <span class="{'material-symbols-outlined' if icon_name in ('crown', 'skull') else 'material-icons'}">{icon_name}</span>
            </div>
            <div class="saillant-label"><span class="saillant-title">{escape_html(s['title'])}</span><span class="saillant-figure">{escape_html(s['figure']) if s['figure'] else ''}</span><span class="saillant-date">{start_label}</span></div>
        </div>"""

    # Tick marks
    tick_interval = compute_tick_interval(timeline_span)
    first_tick = (timeline_start // tick_interval + 1) * tick_interval
    ticks_html = ""
    yr = first_tick
    while yr <= timeline_end:
        left_pct = ((yr - timeline_start) / timeline_span) * 100
        label = format_year(yr)
        ticks_html += f"""
        <div class="tick" style="left:{left_pct:.4f}%;">
            <div class="tick-line"></div>
            <div class="tick-label">{label}</div>
        </div>"""
        yr += tick_interval

    # Pre-phase area on timeline
    prephase_timeline = ""
    if data.get("prephase"):
        meta_start, meta_approx = parse_date(data["metadata"].get("start"))
        if meta_start is not None:
            # pre-phase goes from some earlier point to meta_start
            # we estimate the start from the label if possible
            pp_label = data["prephase"]["label"]
            m = re.search(r"\((\~?\-?\d+)", pp_label)
            if m:
                pp_start, _ = parse_date(m.group(1))
            else:
                pp_start = meta_start - 120  # fallback
            if pp_start is not None:
                left_pct = ((pp_start - timeline_start) / timeline_span) * 100
                width_pct = ((meta_start - pp_start) / timeline_span) * 100
                prephase_timeline = f"""
        <div class="prephase-band" style="left:{left_pct:.4f}%;width:{width_pct:.4f}%;"
            data-tooltip="Pré-phase : {escape_html(data['prephase']['label'])}">
            <span class="prephase-band-label">Pré-phase</span>
        </div>"""

    # Build narrative sections
    narrative_html = ""
    narrative_phases = [p for p in phases if p.get("narrative")]
    if narrative_phases:
        narrative_html = '\n<div class="narrative-section">\n<h2>Récit historionomique</h2>\n'
        for p in narrative_phases:
            color = PHASE_COLORS.get(p["phase"], "#999")
            title = escape_html(p["title"])
            start_label = format_year(p["start"], p["start_approx"])
            end_label = format_year(p["end"], p["end_approx"]) if p["end"] else "en cours"
            raw_narrative = p["narrative"].strip()
            if raw_narrative.startswith("|"):
                raw_narrative = raw_narrative[1:].strip()
            paragraphs = raw_narrative.split("\n\n") if "\n\n" in raw_narrative else raw_narrative.split("\n")
            paras_html = "".join(f"<p>{escape_html(para.strip())}</p>" for para in paragraphs if para.strip())
            narrative_html += f"""
<div class="narrative-phase">
    <h3 style="color:{color}; border-left:4px solid {color}; padding-left:12px;">{title} ({start_label} — {end_label})</h3>
    {paras_html}
</div>"""
        narrative_html += '\n</div>'

    gen_date = date.today().strftime("%d/%m/%Y")

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Parcours — {escape_html(nation)}</title>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background:#fafafa; color:#222; line-height:1.5; }}

/* Header */
.header {{ background:#fff; border-bottom:1px solid #ddd; padding:1.2rem 2rem; }}
.header h1 {{ font-size:1.6rem; color:#333; margin-bottom:0.3rem; }}
.header .subtitle {{ font-size:0.95rem; color:#666; }}
.header .meta-row {{ display:flex; flex-wrap:wrap; gap:1.5rem; margin-top:0.5rem; font-size:0.85rem; color:#555; }}
.header .meta-row span {{ display:inline-flex; align-items:center; gap:0.3rem; }}
.meta-label {{ font-weight:600; color:#444; }}

/* Pre-phase note */
.prephase-note {{ background:#f5f0e6; border-left:4px solid #bba87a; padding:0.8rem 1.2rem; margin:1rem 2rem; border-radius:0 4px 4px 0; font-size:0.9rem; color:#555; }}
.prephase-note strong {{ color:#7a6840; }}

/* Timeline container */
.timeline-wrapper {{ padding:1rem 2rem 0.5rem; overflow-x:auto; }}
.timeline-container {{ position:relative; min-width:2800px; min-height:600px; margin-bottom:10px; }}

/* Ticks */
.tick {{ position:absolute; top:0; height:100%; pointer-events:none; }}
.tick-line {{ position:absolute; top:0; left:0; width:1px; height:100%; background:#ddd; }}
.tick-label {{ position:absolute; top:-20px; left:-20px; width:40px; text-align:center; font-size:0.7rem; color:#888; }}

/* Phase bands */
.phase-band {{ position:absolute; top:20px; height:70px; border-radius:0; border-right:1px solid #fff; cursor:pointer;
    display:flex; flex-direction:column; justify-content:center; align-items:center; min-width:30px;
    transition: filter 0.15s; overflow:hidden; border:none; border-right:1px solid #fff; }}
.phase-band:hover {{ filter:brightness(0.95); }}
.phase-band-label {{ font-size:0.8rem; font-weight:700; text-align:center; max-width:95%;
    overflow:hidden; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; line-height:1.2; }}
.phase-band-dates {{ font-size:0.65rem; color:#555; }}

/* Subphase bands */
.subphase-band {{ position:absolute; top:100px; height:80px; border-radius:0; cursor:pointer;
    min-width:4px; transition: filter 0.15s; border-right:1px solid #fff;
    display:flex; align-items:center; justify-content:center; padding:2px; overflow:visible; }}
.subphase-band:hover {{ filter:brightness(0.92); }}
.subphase-label {{ font-size:0.7rem; font-weight:600; color:#333; text-align:center;
    line-height:1.2; word-wrap:break-word; overflow-wrap:break-word; max-width:95%; }}
.subphase-band.narrow .subphase-label {{ font-size:0.5rem; word-wrap:break-word;
    overflow-wrap:break-word; max-width:95%; }}
.subphase-band.very-narrow .subphase-label {{ font-size:0.5rem; max-width:none; width:max-content;
    line-height:10px; overflow:visible; transform:rotate(-90deg); }}

/* Perturbation overlay */
.perturbation-overlay {{ position:absolute; top:18px; height:170px; cursor:pointer; border-radius:0;
    background: repeating-linear-gradient(45deg, transparent, transparent 4px, rgba(200,50,50,0.08) 4px, rgba(200,50,50,0.08) 8px);
    border:1px dashed rgba(200,50,50,0.4); z-index:5; }}
.perturbation-overlay:hover {{ background: repeating-linear-gradient(45deg, transparent, transparent 4px, rgba(200,50,50,0.15) 4px, rgba(200,50,50,0.15) 8px); }}
.perturbation-label {{ font-size:0.6rem; color:#a33; font-weight:600; white-space:nowrap;
    position:absolute; bottom:4px; left:0; right:0; text-align:center; }}
.perturbation-overlay.narrow .perturbation-label {{ font-size:0.5rem; max-width:none; width:max-content;
    line-height:10px; overflow:visible; transform:rotate(-90deg); transform-origin:left;
    left:50%; white-space:normal; }}

/* Pre-phase band */
.prephase-band {{ position:absolute; top:20px; height:70px; background:rgba(180,170,150,0.15); border:1px dashed #bba87a;
    border-radius:6px; display:flex; align-items:center; justify-content:center; }}
.prephase-band-label {{ font-size:0.75rem; color:#998866; font-weight:600; }}

/* Saillant markers */
.saillant-group {{ position:absolute; top:150px; z-index:10; }}
.saillant-marker {{ width:24px; height:24px; cursor:pointer; border-radius:50%;
    margin-left:-12px; transition:transform 0.15s; display:flex; align-items:center;
    justify-content:center; box-shadow:0 1px 3px rgba(0,0,0,0.3); }}
.saillant-marker:hover {{ transform:scale(1.2); }}
.saillant-marker .material-icons, .saillant-marker .material-symbols-outlined {{ font-size:14px; color:#fff; }}
.saillant-label {{ position:absolute; top:28px; left:-40px; width:80px; text-align:center;
    line-height:1.15; pointer-events:none; }}
.saillant-label .saillant-title {{ font-size:0.5rem; font-weight:800; text-transform:uppercase;
    letter-spacing:-0.02em; color:#333; display:block; }}
.saillant-label .saillant-figure {{ font-size:0.6rem; color:#555; display:block; }}
.saillant-label .saillant-date {{ font-size:0.5rem; color:#888; display:block; }}
.saillant-marker.avortement {{ background:#c0392b !important; }}

/* Tooltip */
.tooltip {{ position:fixed; background:#333; color:#fff; padding:8px 12px; border-radius:6px;
    font-size:0.8rem; max-width:350px; pointer-events:none; z-index:1000;
    line-height:1.4; box-shadow:0 2px 8px rgba(0,0,0,0.3); display:none; }}
.tooltip strong {{ color:#fff; font-weight:700; }}

/* Detail panel */
.detail-overlay {{ position:fixed; top:0; right:0; bottom:0; left:0; background:rgba(0,0,0,0.3);
    z-index:500; display:none; }}
.detail-panel {{ position:fixed; top:0; right:0; bottom:0; width:min(480px,90vw); background:#fff;
    box-shadow:-4px 0 20px rgba(0,0,0,0.15); z-index:501; overflow-y:auto; padding:2rem;
    display:none; }}
.detail-panel.open {{ display:block; }}
.detail-overlay.open {{ display:block; }}
.detail-close {{ position:absolute; top:1rem; right:1rem; background:none; border:none;
    font-size:1.5rem; cursor:pointer; color:#666; line-height:1; }}
.detail-close:hover {{ color:#333; }}
.detail-title {{ font-size:1.3rem; font-weight:700; margin-bottom:0.3rem; padding-right:2rem; }}
.detail-kind {{ display:inline-block; font-size:0.7rem; font-weight:600; padding:2px 8px;
    border-radius:10px; color:#fff; margin-bottom:0.8rem; }}
.detail-meta {{ font-size:0.85rem; color:#555; margin-bottom:1rem; }}
.detail-meta div {{ margin-bottom:0.3rem; }}
.detail-description {{ font-size:0.9rem; line-height:1.6; color:#333; margin-bottom:1rem;
    border-left:3px solid #ddd; padding-left:1rem; }}
.detail-section {{ margin-bottom:0.8rem; }}
.detail-section-title {{ font-size:0.75rem; font-weight:700; color:#888; text-transform:uppercase;
    letter-spacing:0.5px; margin-bottom:0.3rem; }}
.detail-section p {{ font-size:0.85rem; color:#444; line-height:1.5; }}

.confidence-badge {{ display:inline-block; padding:2px 8px; border-radius:10px; font-size:0.7rem; font-weight:600; }}
.confidence-high {{ background:#d4edda; color:#155724; border:1px solid #28a745; }}
.confidence-medium {{ background:#fff3cd; color:#856404; border:1px dashed #ffc107; }}
.confidence-low {{ background:#f8d7da; color:#721c24; border:1px dotted #dc3545; }}

/* Legend */
.legend {{ padding:0.8rem 2rem; display:flex; flex-wrap:wrap; gap:1.2rem; align-items:center; border-top:1px solid #eee; background:#fff; }}
.legend-title {{ font-size:0.8rem; font-weight:700; color:#555; }}
.legend-item {{ display:inline-flex; align-items:center; gap:0.4rem; font-size:0.75rem; color:#444; }}
.legend-swatch {{ width:16px; height:16px; border-radius:3px; flex-shrink:0; }}
.legend-diamond {{ width:16px; height:16px; flex-shrink:0; background:#666; border-radius:50%;
    display:inline-flex; align-items:center; justify-content:center; }}
.legend-diamond .material-icons, .legend-diamond .material-symbols-outlined {{ font-size:10px; color:#fff; }}
.legend-conf {{ display:inline-block; width:24px; height:14px; border-radius:3px; flex-shrink:0; }}

/* Narrative */
.narrative-section {{ padding:2rem; max-width:900px; margin:0 auto; }}
.narrative-section h2 {{ font-size:1.4rem; color:#333; margin-bottom:1.5rem; border-bottom:2px solid #ddd; padding-bottom:0.5rem; }}
.narrative-phase {{ margin-bottom:2rem; }}
.narrative-phase h3 {{ font-size:1.1rem; margin-bottom:0.8rem; }}
.narrative-phase p {{ font-size:0.9rem; color:#444; line-height:1.7; margin-bottom:0.8rem; text-align:justify; }}

/* Footer */
.footer {{ text-align:center; padding:1rem; font-size:0.75rem; color:#999; border-top:1px solid #eee; margin-top:1rem; }}

/* Mobile */
@media (max-width: 768px) {{
    .header {{ padding:0.8rem 1rem; }}
    .header h1 {{ font-size:1.2rem; }}
    .timeline-wrapper {{ padding:0.5rem 1rem; }}
    .legend {{ padding:0.5rem 1rem; gap:0.8rem; }}
    .detail-panel {{ width:100vw; }}
    .saillant-label {{ width:60px; left:-30px; font-size:0.55rem; }}
}}
</style>
</head>
<body>

<div class="header">
    <h1>Parcours de construction nationale — {escape_html(nation)}</h1>
    <div class="subtitle">{escape_html(data['title'])}</div>
    <div class="meta-row">
        {"<span><span class='meta-label'>Hypothèse :</span> " + escape_html(hypothesis) + "</span>" if hypothesis else ""}
        {"<span><span class='meta-label'>Territoire :</span> " + escape_html(territory) + "</span>" if territory else ""}
        {"<span><span class='meta-label'>Statut :</span> " + escape_html(status) + "</span>" if status else ""}
        {"<span><span class='meta-label'>Confiance :</span> " + escape_html(meta_confidence) + "</span>" if meta_confidence else ""}
    </div>
</div>

{prephase_html}

<div class="timeline-wrapper">
    <div class="timeline-container" id="timeline">
        {ticks_html}
        {prephase_timeline}
        {phase_bands_html}
        {subphase_bands_html}
        {perturbation_html}
        {saillant_markers_html}
    </div>
</div>

{narrative_html}

<div class="legend">
    <span class="legend-title">Phases :</span>
    {"".join(f'<span class="legend-item"><span class="legend-swatch" style="background:{very_light_hex(c)};border:2px solid {c};"></span>{PHASE_LABELS.get(k, k)}</span>' for k, c in PHASE_COLORS.items())}
    <span class="legend-item"><span class="legend-diamond"><span class="material-icons" style="font-size:10px;color:#fff;">terrain</span></span>Saillant</span>
    <span class="legend-item"><span class="legend-diamond" style="background:#c0392b;"><span class="material-icons" style="font-size:10px;color:#fff;">cancel</span></span>Avortement</span>
</div>

<div class="tooltip" id="tooltip"></div>
<div class="detail-overlay" id="detailOverlay" onclick="closeDetail()"></div>
<div class="detail-panel" id="detailPanel">
    <button class="detail-close" onclick="closeDetail()">&times;</button>
    <div id="detailContent"></div>
</div>

<div class="footer">
    Généré par le skill Historionomie — {gen_date}
</div>

<script>
const elements = {elements_js};

const phaseColors = {{
    'feodale':'#8B7355','oligarchique':'#2E8B57','absolutiste':'#6A0DAD',
    'rn':'#D4A017','parlementaire':'#1E90FF','technocratique':'#708090'
}};
const phaseLabels = {{
    'feodale':'Féodale','oligarchique':'Oligarchique','absolutiste':'Absolutiste',
    'rn':'Révolution Nationale','parlementaire':'Parlementaire','technocratique':'Technocratique'
}};
const kindLabels = {{
    'phase':'Phase','subphase':'Sous-phase','saillant':'Saillant','perturbation':'Perturbation'
}};

// Tooltip
const tooltip = document.getElementById('tooltip');
document.querySelectorAll('[data-tooltip]').forEach(el => {{
    el.addEventListener('mouseenter', e => {{
        tooltip.innerHTML = el.getAttribute('data-tooltip').replace(/\\n/g, '<br>');
        tooltip.style.display = 'block';
    }});
    el.addEventListener('mousemove', e => {{
        let x = e.clientX + 15, y = e.clientY + 15;
        if (x + 360 > window.innerWidth) x = e.clientX - 360;
        if (y + 100 > window.innerHeight) y = e.clientY - 110;
        tooltip.style.left = x + 'px';
        tooltip.style.top = y + 'px';
    }});
    el.addEventListener('mouseleave', () => {{ tooltip.style.display = 'none'; }});
}});

// Detail panel
function formatYear(yr, approx) {{
    if (yr === null) return '?';
    let p = approx ? '~' : '';
    if (yr < 0) return p + '-' + Math.abs(yr);
    return p + yr;
}}

function showDetail(idx) {{
    const e = elements[idx];
    const panel = document.getElementById('detailPanel');
    const overlay = document.getElementById('detailOverlay');
    const content = document.getElementById('detailContent');

    const color = phaseColors[e.phase] || '#666';
    const kindLabel = kindLabels[e.kind] || e.kind;
    const phaseLabel = phaseLabels[e.phase] || e.phase;

    let confClass = 'confidence-high';
    if (e.confidence === 'medium') confClass = 'confidence-medium';
    if (e.confidence === 'low') confClass = 'confidence-low';
    const confLabel = e.confidence === 'high' ? 'Haute' : e.confidence === 'medium' ? 'Moyenne' : e.confidence === 'low' ? 'Basse' : '';

    let dates = formatYear(e.start, e.start_approx);
    if (e.end !== null) dates += ' — ' + formatYear(e.end, e.end_approx);
    else if (e.kind === 'phase') dates += ' — en cours';

    let html = `<div class="detail-title">${{e.title}}</div>`;
    html += `<span class="detail-kind" style="background:${{color}}">${{kindLabel}}</span>`;
    if (e.phase) html += ` <span style="font-size:0.75rem;color:#666;">${{phaseLabel}}</span>`;
    if (e.step) html += ` <span style="font-size:0.75rem;color:#888;">(étape ${{e.step}})</span>`;

    html += `<div class="detail-meta">`;
    html += `<div><strong>Dates :</strong> ${{dates}}</div>`;
    if (e.figure) html += `<div><strong>Figure :</strong> ${{e.figure}}</div>`;
    if (e.confidence) html += `<div><strong>Confiance :</strong> <span class="confidence-badge ${{confClass}}">${{confLabel}}</span></div>`;
    if (e.deviation) html += `<div><strong>Déviation :</strong> ${{e.deviation}}</div>`;
    if (e.typical_duration) html += `<div><strong>Durée typique :</strong> ${{e.typical_duration}}</div>`;
    if (e.perturbation_type) html += `<div><strong>Type :</strong> ${{e.perturbation_type}}</div>`;
    if (e.affected_motor) html += `<div><strong>Moteur affecté :</strong> ${{e.affected_motor}}</div>`;
    html += `</div>`;

    if (e.summary) {{
        html += `<div class="detail-section"><div class="detail-section-title">Résumé</div><p>${{e.summary}}</p></div>`;
    }}
    if (e.description) {{
        html += `<div class="detail-section"><div class="detail-section-title">Description</div><div class="detail-description">${{e.description}}</div></div>`;
    }}
    if (e.alternatives) {{
        html += `<div class="detail-section"><div class="detail-section-title">Alternatives</div><p style="font-style:italic;color:#666;">${{e.alternatives}}</p></div>`;
    }}
    if (e.note) {{
        html += `<div class="detail-section"><div class="detail-section-title">Note</div><p style="color:#666;">${{e.note}}</p></div>`;
    }}
    if (e.resolution) {{
        const isAborted = e.resolution.startsWith('AVORTÉE');
        const resColor = isAborted ? '#c0392b' : '#27ae60';
        const resIcon = isAborted ? '✗' : '✓';
        html += `<div class="detail-section"><div class="detail-section-title">Résolution ${{resIcon}}</div><p style="color:${{resColor}};font-weight:600;">${{e.resolution}}</p></div>`;
    }}
    if (e.resolution_conditions) {{
        html += `<div class="detail-section"><div class="detail-section-title">Conditions de résolution</div><p style="color:#555;">${{e.resolution_conditions}}</p></div>`;
    }}

    content.innerHTML = html;
    panel.classList.add('open');
    overlay.classList.add('open');
    tooltip.style.display = 'none';
}}

function closeDetail() {{
    document.getElementById('detailPanel').classList.remove('open');
    document.getElementById('detailOverlay').classList.remove('open');
}}

document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeDetail(); }});
</script>
</body>
</html>"""
    return html


def compute_tick_interval(span):
    """Choose a reasonable tick interval for the axis."""
    if span > 2000:
        return 500
    if span > 1000:
        return 200
    if span > 500:
        return 100
    if span > 200:
        return 50
    if span > 80:
        return 25
    return 10


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate interactive HTML timeline from a Parcours Markdown file.")
    parser.add_argument("input", help="Path to the parcours .md file")
    parser.add_argument("-o", "--output", help="Output HTML file path", default=None)
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    data = parse_parcours(args.input)

    html = generate_html(data)

    output_path = args.output
    if output_path is None:
        base = os.path.splitext(os.path.basename(args.input))[0]
        output_path = base + ".html"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Timeline generated: {output_path}")
    print(f"  Nation: {data['metadata'].get('nation', '?')}")
    print(f"  Elements: {len(data['elements'])} (phases, subphases, saillants, perturbations)")


if __name__ == "__main__":
    main()
