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
        "elements": [],  # flat list of phases, subphases, saillants, perturbations
        "area_data": [],  # superficie de référence data points
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

        # Superficie de référence
        if "Superficie" in heading_text:
            area_data = []
            for line in sec_lines:
                m = re.match(r"^- (~?\-?\d+)\s*:\s*(\d+)(?:\+(\d+))?\s*(?:\|\s*(.*))?", line)
                if m:
                    year, _ = parse_date(m.group(1))
                    noyau = int(m.group(2))
                    marges = int(m.group(3)) if m.group(3) else 0
                    label = m.group(4).strip() if m.group(4) else ""
                    if year is not None:
                        area_data.append({
                            "year": year, "noyau": noyau, "marges": marges,
                            "area": noyau + marges, "label": label,
                        })
            result["area_data"] = sorted(area_data, key=lambda d: d["year"])
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
        "subtitle": fields.get("subtitle", ""),
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
        # New perturbation fields
        "perturbation": fields.get("perturbation", ""),
        "mechanism": fields.get("mechanism", ""),
        "effect": fields.get("effect", ""),
        "territorial": fields.get("territorial", ""),
    }


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

PHASE_COLORS = {
    "prefeodale": "#A0A0A0",
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
    "Remontrance": "record_voice_over",
    "Crise féodale": "swords",
    "Choc d'hétérogénéité": "group_add",
    "Accélérateur": "fast_forward",
}
SAILLANT_ICON_DEFAULT = "diamond"
SAILLANT_ICON_AVORTEMENT = "cancel"  # legacy, used as fallback

# New perturbation system: mechanism → icon, effect → color
PERTURBATION_EFFECT_COLORS = {
    "prolongement": "#E67E22",   # orange
    "acceleration": "#2980B9",   # blue
    "avortement": "#c0392b",     # red
    "reboot": "#8B0000",         # dark red / crimson
}

PERTURBATION_MECHANISM_ICONS = {
    "choc_heterogeneite": "open_in_full",
    "choc_exogene": "bolt",
    "insuffisance_interne": "close",
    "correction_echelle": "compress",
}

PHASE_LABELS = {
    "prefeodale": "Pré-féodale",
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
    year_padding = max(5, int((max_year - min_year) * 0.01))
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
    flag_url = meta.get("flag", "")
    illustration_url = meta.get("illustration", "")

    # Extract highlights and open questions from metadata
    highlights = []
    questions = []
    for key, val in sorted(meta.items()):
        if key.startswith("highlight") and val:
            highlights.append(val)
        if key.startswith("question") and val:
            questions.append(val)

    # Build JSON data for JS
    elements_json_parts = []
    for i, e in enumerate(elements):
        parts = []
        for key in ["kind", "type", "phase", "title", "subtitle", "summary", "description",
                     "figure", "confidence", "alternatives", "step", "deviation",
                     "typical_duration", "perturbation_type", "affected_motor", "note",
                     "resolution", "resolution_conditions", "avortement"]:
            parts.append(f"'{key}':'{escape_js_string(str(e.get(key, '')))}'")
        parts.append(f"'start':{e['start'] if e['start'] is not None else 'null'}")
        parts.append(f"'end':{e['end'] if e['end'] is not None else 'null'}")
        parts.append(f"'start_approx':{'true' if e['start_approx'] else 'false'}")
        parts.append(f"'end_approx':{'true' if e['end_approx'] else 'false'}")
        elements_json_parts.append("{" + ",".join(parts) + "}")

    elements_js = "[" + ",".join(elements_json_parts) + "]"

    # Briefing section (highlights + questions)
    insight_icons = ["compress", "restart_alt", "coronavirus", "shield",
                     "fast_forward", "cancel", "auto_awesome", "lightbulb"]
    insights_html = ""
    if highlights:
        items = ""
        for i, h in enumerate(highlights):
            icon = insight_icons[i % len(insight_icons)]
            # Support "Title | Description | image_url | phase" format
            parts = [p.strip() for p in h.split(" | ")]
            img_url = None
            phase_color = None
            # Extract phase (last segment if it matches a known phase)
            if len(parts) >= 2 and parts[-1] in PHASE_COLORS:
                phase_color = PHASE_COLORS[parts[-1]]
                parts = parts[:-1]
            # Extract image (last segment if URL or path)
            if len(parts) >= 3 and (parts[-1].startswith("http") or parts[-1].startswith("images/")):
                img_url = parts[-1]
                parts = parts[:-1]
            dot_html = f'<span style="width:10px;height:10px;border-radius:50%;background:{phase_color};flex-shrink:0;margin-top:3px;"></span>' if phase_color else ""
            if len(parts) >= 2:
                h_html = f'<span class="insight-title">{dot_html}{escape_html(parts[0])}</span><span class="insight-desc">{escape_html(parts[1])}</span>'
            else:
                h_html = f'<span class="insight-desc">{escape_html(h)}</span>'
            if img_url:
                icon_html = f'<img class="insight-img" src="{img_url}" alt="">'
            else:
                icon_html = f'<span class="material-icons">{icon}</span>'
            items += f"""<div class="insight-item">{icon_html}<div>{h_html}</div></div>"""
        insights_html = f"""<div class="briefing-insights">
            <div class="briefing-label">Faits marquants</div>
            <div class="insights-grid">{items}</div>
        </div>"""

    questions_html = ""
    if questions:
        qs = ""
        for i, q in enumerate(questions):
            # Support "Title | Description" format for titled questions
            if " | " in q:
                q_title, q_desc = q.split(" | ", 1)
                qs += f"""<div class="question-item"><span class="question-tag">{escape_html(q_title)}</span><span class="question-text">{escape_html(q_desc)}</span></div>"""
            else:
                qs += f"""<div class="question-item"><span class="question-tag">Q{i+1}</span><span class="question-text">{escape_html(q)}</span></div>"""
        questions_html = f"""<div class="briefing-questions">
            <div class="briefing-label">Questions ouvertes</div>
            {qs}
        </div>"""

    briefing_html = ""
    if insights_html or questions_html:
        grid_class = "briefing" if questions_html else "briefing briefing-full"
        briefing_html = f"""<div class="{grid_class}">{insights_html}{questions_html}</div>"""

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

        border_style = "solid"

        start_label = format_year(p["start"], p["start_approx"])
        end_label = format_year(p["end"], p["end_approx"]) if p["end"] else "en cours"

        # Clean phase label: use title if it starts with "Pré-", otherwise canonical name
        if p["title"].lower().startswith("pré-"):
            phase_display = p["title"]
        elif p["phase"] == "rn":
            phase_display = "Révolution Nationale"
        else:
            phase_display = PHASE_LABELS.get(p["phase"], p["title"])

        # Add narrow-indicator for phases too small to see/click
        NARROW_PHASE_ICONS = {
            "prefeodale": "shield",
            "feodale": "shield",
            "oligarchique": "gavel",
            "absolutiste": "crown",
            "rn": "bolt",
            "parlementaire": "account_balance",
            "technocratique": "precision_manufacturing",
        }
        is_narrow = width_pct < 2
        narrow_indicator = ""
        if is_narrow:
            mid_pct = left_pct + width_pct / 2
            pin_icon = NARROW_PHASE_ICONS.get(p["phase"], "circle")
            narrow_indicator = f"""
        <div class="narrow-indicator" style="left:{mid_pct:.4f}%; top:-8px;"
            data-tooltip="&lt;strong&gt;{escape_html(p['title'])}&lt;/strong&gt; ({start_label} — {end_label})&#10;{escape_html(p['summary'])}"
            onclick="showDetail({elements.index(p)})">
            <div class="narrow-indicator-pin" style="background:{color};">
                <span class="material-icons">{pin_icon}</span>
            </div>
        </div>"""

        narrow_class = " phase-narrow" if is_narrow else ""
        phase_bands_html += f"""{narrow_indicator}
        <div class="phase-band{narrow_class}" style="left:{left_pct:.4f}%;width:{width_pct:.4f}%;
            background:{bg};border-top:3px {border_style} {color};border-right:1px solid #fff;"
            data-tooltip="&lt;strong&gt;{escape_html(p['title'])}&lt;/strong&gt; ({start_label} — {end_label})&#10;{escape_html(p['summary'])}"
            onclick="showDetail({elements.index(p)})">
            {"" if is_narrow else f'<div class="phase-band-label" style="color:{color};">{escape_html(phase_display)}</div>'}
            {"" if is_narrow else f'<div class="phase-band-dates">{start_label} — {end_label}</div>'}
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
        if width_pct < 3:
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

    # Build area chart (superficie de référence)
    area_chart_html = ""
    has_area_data = bool(data.get("area_data"))
    # Pre-compute whether territorial perturbations exist (for CSS layout)
    _area_mechs = {"choc_heterogeneite", "correction_echelle", "choc_exogene"}
    _area_effects = {"prolongement", "acceleration"}
    has_area_saillants = has_area_data and any(
        e.get("perturbation") == "true" and e.get("mechanism") in _area_mechs and e.get("effect") in _area_effects and e.get("territorial") != "false"
        for e in elements if e["kind"] == "saillant")
    area_chart_top = 230 if has_area_saillants else 185
    if has_area_data:
        area_data = data["area_data"]
        max_area = max(d["area"] for d in area_data)
        AREA_MAX_PX = 62  # max pixel height for the tallest step

        steps_html = ""
        edges_html = ""

        for i, d in enumerate(area_data):
            x_start = d["year"]
            x_end = area_data[i + 1]["year"] if i + 1 < len(area_data) else timeline_end

            left_pct = ((x_start - timeline_start) / timeline_span) * 100
            width_pct = ((x_end - x_start) / timeline_span) * 100
            total_px = (d["area"] / max_area) * AREA_MAX_PX
            noyau_px = (d["noyau"] / max_area) * AREA_MAX_PX
            marges_px = (d["marges"] / max_area) * AREA_MAX_PX
            has_marges = d["marges"] > 0

            # Individual tooltips
            noyau_fmt = f"~{d['noyau'] * 1000:,}".replace(",", " ") + " km²"
            label_text = d.get("label", "")
            if has_marges:
                noyau_tooltip = f"&lt;strong&gt;Noyau territorial&lt;/strong&gt;&#10;{escape_html(noyau_fmt)}"
                marges_fmt = f"~{d['marges'] * 1000:,}".replace(",", " ") + " km²"
                marges_line = escape_html(f"{marges_fmt} — {label_text}") if label_text else escape_html(marges_fmt)
                marges_tooltip = f"&lt;strong&gt;Marges&lt;/strong&gt;&#10;{marges_line}"
            else:
                noyau_line = escape_html(f"{noyau_fmt} — {label_text}") if label_text else escape_html(noyau_fmt)
                noyau_tooltip = f"&lt;strong&gt;Noyau territorial&lt;/strong&gt;&#10;{noyau_line}"

            # Stacked chart — noyau + marges
            group_class = " has-marges" if has_marges else ""
            noyau_div = f'<div class="area-noyau" style="height:{noyau_px:.1f}px;" data-tooltip="{noyau_tooltip}"></div>'
            marges_div = f'<div class="area-marges" style="bottom:{noyau_px:.1f}px;height:{marges_px:.1f}px;" data-tooltip="{marges_tooltip}"></div>' if has_marges else ""

            steps_html += f"""
        <div class="area-step-group{group_class}" style="left:{left_pct:.4f}%;width:{width_pct:.4f}%;height:{total_px:.1f}px;">{noyau_div}{marges_div}</div>"""

            # Vertical edges at transitions
            if i > 0:
                prev_total = (area_data[i - 1]["area"] / max_area) * AREA_MAX_PX
                edge_h = max(total_px, prev_total)
                edges_html += f"""
        <div class="area-edge" style="left:{left_pct:.4f}%;height:{edge_h:.1f}px;"></div>"""

        # Align label with first phase band
        first_phase_left = 0
        if phases:
            fp_start = phases[0]["start"] if phases[0]["start"] is not None else timeline_start
            first_phase_left = ((fp_start - timeline_start) / timeline_span) * 100

        # area_chart_html will be finalized after we know if there are area saillants
        area_chart_inner = f"""
        <div class="area-chart-label" style="left:{first_phase_left:.4f}%;">Superficie de référence (×1000 km²)</div>
        {steps_html}
        {edges_html}"""

    # Build saillant markers — row assignment is done in JS after measuring real label widths
    dated_saillants = [(s, ((s["start"] - timeline_start) / timeline_span) * 100)
                       for s in saillants if s["start"] is not None]
    dated_saillants.sort(key=lambda x: x[1])

    # Split territorial perturbations (shown above area chart) from regular saillants
    # All external/territorial mechanisms go above the chart; only insuffisance_interne stays in the main row
    area_saillant_mechanisms = {"choc_heterogeneite", "correction_echelle", "choc_exogene"}
    if has_area_data:
        area_saillant_effects = {"prolongement", "acceleration"}
        def _is_area_saillant(s):
            return (s.get("perturbation") == "true" and s.get("mechanism") in area_saillant_mechanisms
                    and s.get("effect") in area_saillant_effects and s.get("territorial") != "false")
        area_saillants_list = [(s, pct) for s, pct in dated_saillants if _is_area_saillant(s)]
        regular_saillants = [(s, pct) for s, pct in dated_saillants if not _is_area_saillant(s)]
    else:
        area_saillants_list = []
        regular_saillants = dated_saillants

    # Finalize area chart HTML with computed top position
    if has_area_data:
        area_chart_html = f"""
    <div class="area-chart" style="top:{area_chart_top}px;">
        {area_chart_inner}
    </div>"""

    # Build area saillant markers (compact, above area chart)
    area_saillants_html = ""
    for (s, left_pct) in area_saillants_list:
        mechanism = s.get("mechanism", "")
        effect = s.get("effect", "")
        bg_color = PERTURBATION_EFFECT_COLORS.get(effect, "#c0392b")
        if effect == "reboot":
            icon_name = "restart_alt"
        else:
            icon_name = PERTURBATION_MECHANISM_ICONS.get(mechanism, SAILLANT_ICON_AVORTEMENT)
        icon_class = 'material-symbols-outlined' if icon_name in ('crown', 'skull', 'swords') else 'material-icons'
        frise_subtitle = s["subtitle"] if s["subtitle"] else (s["figure"] if s["figure"] else "")
        tooltip_label = s["subtitle"] if s["subtitle"] else (s["figure"] if s["figure"] else s["title"])
        start_label = format_year(s["start"], s["start_approx"])

        area_saillants_html += f"""
        <div class="area-saillant-group" style="left:{left_pct:.4f}%;">
            <div class="saillant-marker perturbation-marker" style="background:{bg_color};"
                data-tooltip="&lt;strong&gt;{escape_html(s['title'])}&lt;/strong&gt;&#10;{escape_html(tooltip_label)} ({start_label})&#10;{escape_html(s['summary'])}"
                onclick="showDetail({elements.index(s)})">
                <span class="{icon_class}">{icon_name}</span>
            </div>
            <div class="area-saillant-label"><span class="saillant-figure">{escape_html(s['title'])}</span><span class="saillant-date">{start_label}</span></div>
        </div>"""

    saillant_markers_html = ""
    for (s, left_pct) in regular_saillants:
        color = PHASE_COLORS.get(s["phase"], "#333")

        # subtitle (shown on frise) falls back to figure, then nothing
        frise_subtitle = s["subtitle"] if s["subtitle"] else (s["figure"] if s["figure"] else "")
        # tooltip secondary line: subtitle or figure or title
        tooltip_label = s["subtitle"] if s["subtitle"] else (s["figure"] if s["figure"] else s["title"])
        start_label = format_year(s["start"], s["start_approx"])

        is_perturbation = s.get("perturbation") == "true" or s.get("avortement") == "true"
        mechanism = s.get("mechanism", "")
        effect = s.get("effect", "")

        if is_perturbation:
            # New system: color from effect, icon from mechanism (with reboot override)
            bg_color = PERTURBATION_EFFECT_COLORS.get(effect, "#c0392b")
            if effect == "reboot":
                icon_name = "restart_alt"
            else:
                icon_name = PERTURBATION_MECHANISM_ICONS.get(mechanism, SAILLANT_ICON_AVORTEMENT)
            marker_class = " perturbation-marker"
        else:
            bg_color = color
            icon_name = SAILLANT_ICONS.get(s["title"], SAILLANT_ICON_DEFAULT)
            marker_class = ""

        icon_class = 'material-symbols-outlined' if icon_name in ('crown', 'skull', 'swords') else 'material-icons'
        saillant_markers_html += f"""
        <div class="saillant-group" style="left:{left_pct:.4f}%;">
            <div class="saillant-marker{marker_class}" style="background:{bg_color};"
                data-tooltip="&lt;strong&gt;{escape_html(s['title'])}&lt;/strong&gt;&#10;{escape_html(tooltip_label)} ({start_label})&#10;{escape_html(s['summary'])}"
                onclick="showDetail({elements.index(s)})">
                <span class="{icon_class}">{icon_name}</span>
            </div>
            <div class="saillant-label"><span class="saillant-title">{escape_html(s['title'])}</span><span class="saillant-figure">{escape_html(frise_subtitle)}</span><span class="saillant-date">{start_label}</span></div>
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

    gen_date = date.today().strftime("%d/%m/%Y")

    # Compute stats
    phase_count = len([e for e in elements if e["kind"] == "phase"])
    total_duration = timeline_end - timeline_start

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Parcours — {escape_html(nation)}</title>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Public+Sans:wght@100..900&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: 'Public Sans', 'Segoe UI', system-ui, sans-serif; background:#f9f9f9; color:#1a1c1c; line-height:1.5; }}
.font-headline {{ font-family: 'Newsreader', Georgia, serif; }}

/* Navbar */
.navbar {{ background:#fff; border-bottom:1px solid #e0dcd4; padding:0.6rem 2rem; display:flex; align-items:center; gap:2rem; }}
.navbar-brand {{ font-family:'Newsreader', Georgia, serif; font-size:1.3rem; font-style:italic; color:#8B7355; text-decoration:none; font-weight:600; }}
.navbar-links {{ display:flex; gap:1.2rem; }}
.navbar-links a {{ text-decoration:none; font-size:0.85rem; color:#888; font-weight:500; }}
.navbar-links a:hover {{ color:#333; }}

/* Header — briefing style */
.header {{ background:#f9f9f9; padding:1.5rem 2rem 0; }}
.header-title-row {{ display:flex; align-items:center; gap:0.75rem; margin-bottom:0.5rem; }}
.header-title-row h1 {{ font-family:'Newsreader', Georgia, serif; font-size:2.4rem; color:#1a1c1c; font-weight:600; line-height:1; }}
.header-flag {{ height:25px; width:auto; border-radius:2px; box-shadow:0 0 0 1px rgba(0,0,0,0.08); position:relative; top:-1px; }}
.header-badge {{ display:inline-flex; font-size:0.55rem; font-weight:700; padding:2px 8px;
    border-radius:2px; text-transform:uppercase; letter-spacing:0.8px; position:relative; top:-4px; }}
.badge-territory {{ background:#8B7355; color:#fff; }}
.badge-status {{ background:#d4edda; color:#2d6a4f; }}
.badge-status.wip {{ background:#fff3cd; color:#856404; border:1px solid #f0e0a0; }}
.header-subtitle {{ font-family:'Newsreader', Georgia, serif; font-style:italic;
    font-size:1.05rem; color:#8B7355; line-height:1.5; margin-bottom:1rem; }}
.header-illustration {{ width:110px; height:75px; object-fit:cover; border-radius:4px;
    box-shadow:0 1px 4px rgba(0,0,0,0.1); flex-shrink:0; }}

/* Briefing grid */
.briefing {{ display:grid; grid-template-columns:2fr 1fr; gap:2rem; padding:1rem 2rem 1rem;
    border-top:1px solid #e0dcd4; }}
.briefing.briefing-full {{ grid-template-columns:1fr; }}
.briefing-full .insights-grid {{ grid-template-columns:1fr 1fr 1fr; }}
.briefing-insights {{ }}
.briefing-label {{ font-family:'Newsreader', Georgia, serif; font-size:1.6rem; font-weight:500;
    color:#1a1c1c; margin-bottom:0.75rem; }}
.insights-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:0.75rem 1.2rem; }}
.insight-item {{ display:flex; align-items:flex-start; gap:0.6rem; font-size:0.78rem; color:#4d453c;
    line-height:1.5; padding:0.7rem 0.8rem; background:#fff; border-radius:6px;
    border:1px solid rgba(209,196,185,0.3); box-shadow:0 1px 3px rgba(0,0,0,0.03); }}
.insight-item .insight-title {{ display:flex; align-items:center; gap:0.35rem; font-weight:700; color:#1a1c1c; font-size:0.78rem; margin-bottom:0.15rem; }}
.insight-item .insight-desc {{ display:block; color:#666; font-size:0.73rem; }}
.insight-item .material-icons {{ font-size:14px; color:#8B7355; flex-shrink:0; margin-top:2px; }}
.insight-item .insight-img {{ width:60px; height:70px; object-fit:cover; object-position:top; border-radius:4px; flex-shrink:0; filter:sepia(0.3); }}
.briefing-questions {{ padding-left:1.5rem; border-left:1px solid #e0dcd4; }}
.question-item {{ font-size:0.82rem; color:#555; line-height:1.55; margin-bottom:0.8rem;
    padding:0.6rem 0.8rem; background:#f9f9f9; border-radius:6px; border-left:3px solid #d4c9b8; }}
.question-tag {{ display:block; font-family:'Public Sans', sans-serif;
    font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px;
    color:#8B7355; margin-bottom:0.2rem; }}
.question-item .question-text {{ font-family:'Newsreader', Georgia, serif; font-style:italic; }}

/* Timeline container */
.timeline-wrapper {{ padding:1.5rem 2rem 0.5rem; overflow-x:auto; }}
.timeline-container {{ position:relative; min-width:2800px; min-height:{area_chart_top + 500 if has_area_data else 600}px; margin-bottom:10px; }}

/* Ticks */
.tick {{ position:absolute; top:0; height:100%; pointer-events:none; }}
.tick-line {{ position:absolute; top:0; left:0; width:1px; height:100%; background:#ddd; }}
.tick-label {{ position:absolute; top:-20px; left:-20px; width:40px; text-align:center; font-size:0.7rem; color:#888; }}

/* Phase bands */
.phase-band {{ position:absolute; top:20px; height:70px; border-radius:0; border-right:1px solid #fff; cursor:pointer;
    display:flex; flex-direction:column; justify-content:center; align-items:center; min-width:30px;
    transition: filter 0.15s; overflow:hidden; border:none; border-right:1px solid #fff; }}
.phase-band.phase-narrow {{ min-width:4px; }}
.phase-band:hover {{ filter:brightness(0.95); }}
.phase-band-label {{ font-size:0.75rem; font-weight:700; text-align:center; max-width:95%;
    overflow:hidden; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; line-height:1.2;
    text-transform:uppercase; letter-spacing:0.5px; }}
.phase-band-dates {{ font-size:0.6rem; color:#555; }}

/* Subphase bands */
.subphase-band {{ position:absolute; top:100px; height:80px; border-radius:0; cursor:pointer;
    min-width:4px; transition: filter 0.15s; border-right:1px solid #fff;
    display:flex; align-items:center; justify-content:center; padding:2px; overflow:visible; }}
.subphase-band:hover {{ filter:brightness(0.92); }}
.subphase-label {{ font-size:0.65rem; font-weight:600; color:#333; text-align:center;
    line-height:1.2; word-wrap:break-word; overflow-wrap:break-word; max-width:95%;
    text-transform:uppercase; letter-spacing:0.3px; }}
.subphase-band.narrow .subphase-label {{ font-size:0.5rem; word-wrap:break-word;
    overflow-wrap:break-word; max-width:95%; }}
.subphase-band.very-narrow .subphase-label {{ font-size:0.5rem; max-width:none; width:max-content;
    line-height:10px; overflow:visible; transform:rotate(-90deg); }}

/* Perturbation overlay */
.perturbation-overlay {{ position:absolute; top:100px; height:80px; cursor:pointer; border-radius:0;
    background: repeating-linear-gradient(45deg, transparent, transparent 4px, rgba(200,50,50,0.08) 4px, rgba(200,50,50,0.08) 8px);
    border:1px dashed rgba(200,50,50,0.4); z-index:5; }}
.perturbation-overlay:hover {{ background: repeating-linear-gradient(45deg, transparent, transparent 4px, rgba(200,50,50,0.15) 4px, rgba(200,50,50,0.15) 8px); }}
.perturbation-label {{ font-size:0.5rem; color:#a33; font-weight:600;
    position:absolute; top:50%; left:50%; transform:translate(-50%,-50%) rotate(-90deg);
    pointer-events:none; letter-spacing:0.3px; width:100%; text-align:center; }}
.perturbation-overlay.narrow .perturbation-label {{ font-size:0.45rem; }}

/* Area chart — superficie de référence (stacked: noyau + marges + ref line) */
.area-chart {{ position:absolute; left:0; width:100%; height:70px; pointer-events:none; }}
.area-step-group {{ position:absolute; bottom:0; }}
.area-noyau {{ position:absolute; bottom:0; left:0; width:100%;
    background:rgba(130,110,85,0.25); cursor:pointer; pointer-events:auto;
    transition:background 0.15s; }}
.area-noyau:hover {{ background:rgba(130,110,85,0.38); }}
.area-step-group.has-marges .area-noyau {{ border-top:1px dashed rgba(130,110,85,0.30); }}
.area-marges {{ position:absolute; left:0; width:100%;
    background:rgba(175,165,150,0.13); border-top:1.5px solid rgba(140,128,115,0.35);
    cursor:pointer; pointer-events:auto; transition:background 0.15s; }}
.area-marges:hover {{ background:rgba(175,165,150,0.24); }}
.area-edge {{ position:absolute; bottom:0; width:1.5px; background:rgba(140,128,115,0.25); pointer-events:none; }}
.area-chart-label {{ position:absolute; top:0; left:0; font-size:0.6rem; color:#a09080;
    font-weight:600; text-transform:uppercase; letter-spacing:0.5px; pointer-events:none; white-space:nowrap; }}
.area-saillant-group {{ position:absolute; top:188px; z-index:15; }}
.area-saillant-label {{ position:absolute; top:25px; left:-35px; width:70px; text-align:center;
    line-height:1.1; pointer-events:none; }}
.area-saillant-label .saillant-figure {{ font-size:0.55rem; color:#666; display:block; }}
.area-saillant-label .saillant-date {{ font-size:0.5rem; color:#999; display:block; font-weight:600; }}

/* Narrow-phase indicator — visible marker for phases too short to see */
.narrow-indicator {{ position:absolute; z-index:15; cursor:pointer; pointer-events:auto; margin-left:-10px; }}
.narrow-indicator-pin {{ width:20px; height:20px; border-radius:50% 50% 50% 0; transform:rotate(-45deg);
    box-shadow:0 1px 4px rgba(0,0,0,0.25); display:flex; align-items:center; justify-content:center; }}
.narrow-indicator-pin .material-icons {{ font-size:10px; color:#fff; transform:rotate(45deg); }}
.narrow-indicator:hover .narrow-indicator-pin {{ transform:rotate(-45deg) scale(1.15);
    box-shadow:0 2px 8px rgba(0,0,0,0.3); }}

/* Saillant markers */
.saillant-group {{ position:absolute; top:200px; z-index:10; }}
.saillant-marker {{ width:24px; height:24px; cursor:pointer; border-radius:50%;
    margin-left:-12px; transition:transform 0.15s; display:flex; align-items:center;
    justify-content:center; box-shadow:0 2px 6px rgba(0,0,0,0.2); }}
.saillant-marker:hover {{ transform:scale(1.15); box-shadow:0 3px 10px rgba(0,0,0,0.25); }}
.saillant-marker .material-icons, .saillant-marker .material-symbols-outlined {{ font-size:12px; color:#fff; }}
.saillant-label {{ position:absolute; top:30px; left:-45px; width:90px; text-align:center;
    line-height:1.15; pointer-events:none; }}
.saillant-label .saillant-title {{ font-size:0.55rem; font-weight:800; text-transform:uppercase;
    letter-spacing:0.02em; color:#333; display:block; }}
.saillant-label .saillant-figure {{ font-size:0.6rem; color:#666; display:block; }}
.saillant-label .saillant-date {{ font-size:0.55rem; color:#999; display:block; font-weight:600; }}
.saillant-marker.avortement {{ background:#c0392b !important; }}
.saillant-marker.perturbation-marker {{ width:19px; height:19px; border-radius:2px; transform:rotate(45deg); margin-left:-9px; }}
.saillant-marker.perturbation-marker .material-icons,
.saillant-marker.perturbation-marker .material-symbols-outlined {{ transform:rotate(-45deg); font-size:10px; }}
.saillant-marker.selected {{ box-shadow:0 0 0 4px #fff, 0 4px 12px rgba(0,0,0,0.3); }}

/* Tooltip */
.tooltip {{ position:fixed; background:#333; color:#fff; padding:8px 12px; border-radius:6px;
    font-size:0.8rem; max-width:350px; pointer-events:none; z-index:1000;
    line-height:1.4; box-shadow:0 2px 8px rgba(0,0,0,0.3); display:none; }}
.tooltip strong {{ color:#fff; font-weight:700; }}

/* Detail panel — Stitch style */
.detail-overlay {{ position:fixed; top:0; right:0; bottom:0; left:0; background:rgba(0,0,0,0.2);
    z-index:500; display:none; }}
.detail-panel {{ position:fixed; top:0; right:0; bottom:0; width:min(400px,92vw);
    background:rgba(243,243,243,0.95); backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
    box-shadow:-4px 0 24px rgba(0,0,0,0.08); z-index:501; overflow-y:auto;
    display:none; border-left:1px solid rgba(209,196,185,0.3); }}
.detail-panel.open {{ display:block; }}
.detail-overlay.open {{ display:block; }}

/* Panel header */
.detail-panel-header {{ padding:1.2rem 1.5rem; border-bottom:1px solid rgba(209,196,185,0.2); }}
.detail-panel-header-top {{ display:flex; align-items:center; justify-content:space-between; margin-bottom:0.8rem; }}
.detail-panel-title {{ font-family:'Newsreader', Georgia, serif; font-size:1.15rem; font-weight:600; color:#1a1c1c; }}
.detail-close {{ background:none; border:none; cursor:pointer; color:#7f756b; font-size:1.2rem; padding:4px; }}
.detail-close:hover {{ color:#1a1c1c; }}

.detail-badges {{ display:flex; gap:0.5rem; align-items:center; flex-wrap:wrap; }}
.detail-kind {{ display:inline-flex; align-items:center; gap:4px; font-size:0.6rem; font-weight:700; padding:4px 10px;
    border-radius:20px; color:#fff; text-transform:uppercase; letter-spacing:0.8px; }}
.confidence-badge {{ display:inline-flex; align-items:center; gap:4px; padding:4px 10px; border-radius:20px;
    font-size:0.6rem; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; }}
.confidence-high {{ background:rgba(0,99,151,0.1); color:#006397; }}
.confidence-medium {{ background:rgba(113,91,62,0.1); color:#715b3e; }}
.confidence-low {{ background:rgba(186,26,26,0.1); color:#ba1a1a; }}

/* Panel content */
.detail-panel-content {{ padding:1.5rem; }}
.detail-panel-content > section {{ margin-bottom:1.5rem; }}

.detail-section-label {{ font-size:0.6rem; font-weight:700; text-transform:uppercase; letter-spacing:1px;
    color:#7f756b; margin-bottom:0.3rem; display:block; }}
.detail-title {{ font-family:'Newsreader', Georgia, serif; font-size:1.7rem; font-weight:500;
    color:#1a1c1c; line-height:1.25; padding-right:1rem; }}
.detail-subtitle {{ font-family:'Newsreader', Georgia, serif; font-style:italic; color:#8B7355;
    font-size:1rem; margin-top:0.3rem; line-height:1.4; }}

/* Data cards grid */
.detail-cards {{ display:grid; grid-template-columns:1fr 1fr; gap:0.6rem; }}
.detail-card {{ background:#fff; border-radius:10px; padding:0.8rem 1rem; }}
.detail-card .detail-section-label {{ margin-bottom:0.2rem; }}
.detail-card-value {{ font-family:'Newsreader', Georgia, serif; font-size:1.05rem; color:#1a1c1c; }}

/* Figure card */
.detail-figure {{ display:flex; align-items:center; gap:0.8rem; background:rgba(226,226,226,0.5);
    border-radius:10px; padding:0.8rem 1rem; }}
.detail-figure-portrait {{ width:52px; height:52px; border-radius:6px; object-fit:cover; flex-shrink:0;
    }}
.detail-figure-icon {{ width:52px; height:52px; border-radius:6px; background:#d1c4b9;
    display:flex; align-items:center; justify-content:center; flex-shrink:0; }}
.detail-figure-icon .material-icons {{ font-size:22px; color:#574329; }}
.detail-figure-info {{ flex:1; }}
.detail-figure-info .detail-section-label {{ margin-bottom:0; }}
.detail-figure-name {{ font-weight:600; color:#1a1c1c; font-size:0.95rem; }}
.detail-figure-role {{ font-size:0.78rem; color:#7f756b; }}

/* Synthèse */
.detail-section {{ margin-bottom:1.2rem; }}
.detail-section p {{ font-size:0.88rem; color:#4d453c; line-height:1.7; }}
.detail-description {{ font-size:0.88rem; line-height:1.7; color:#4d453c; }}

.detail-meta {{ font-size:0.82rem; color:#4d453c; margin-bottom:1rem; }}
.detail-meta div {{ margin-bottom:0.3rem; }}

.detail-divider {{ border:none; border-top:1px solid rgba(209,196,185,0.3); margin:1.2rem 0; }}

/* Legend */
.legend {{ padding:0.8rem 2rem; display:flex; flex-wrap:wrap; gap:1.2rem; align-items:center; border-top:1px solid #e0dcd4; background:#f9f9f9; }}
.legend-title {{ font-size:0.8rem; font-weight:700; color:#555; }}
.legend-item {{ display:inline-flex; align-items:center; gap:0.4rem; font-size:0.75rem; color:#444; }}
.legend-swatch {{ width:16px; height:16px; border-radius:3px; flex-shrink:0; }}
.legend-diamond {{ width:16px; height:16px; flex-shrink:0; background:#666; border-radius:50%;
    display:inline-flex; align-items:center; justify-content:center; }}
.legend-diamond .material-icons, .legend-diamond .material-symbols-outlined {{ font-size:10px; color:#fff; }}
.legend-conf {{ display:inline-block; width:24px; height:14px; border-radius:3px; flex-shrink:0; }}

/* Footer */
.footer {{ text-align:center; padding:1rem; font-size:0.75rem; color:#999; border-top:1px solid #e0dcd4; margin-top:1rem; background:#fff; }}

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

<nav class="navbar">
    <a class="navbar-brand" href="index.html">Historionomie</a>
    <div class="navbar-links">
        <a href="index.html">Accueil</a>
        <a href="index.html#wiki">Wiki</a>
    </div>
</nav>

<div class="header">
    <div class="header-title-row">
        {"<img class='header-flag' src='" + escape_html(flag_url) + "' alt='drapeau'>" if flag_url else ""}
        <h1>{escape_html(nation)}</h1>
        {"<span class='header-badge badge-status" + (" wip" if status.lower() in ("wip", "en cours", "à valider") else "") + "'>" + escape_html(status) + "</span>" if status else ""}
    </div>
    <div class="header-subtitle">{escape_html(data['metadata'].get('subtitle', '') or data['title'])}</div>
</div>

{briefing_html}

<div class="timeline-wrapper">
    <div class="timeline-container" id="timeline">
        {ticks_html}
        {phase_bands_html}
        {subphase_bands_html}
        {perturbation_html}
        {area_chart_html}
        {area_saillants_html}
        {saillant_markers_html}
    </div>
</div>

<div class="legend">
    <span class="legend-title">Phases :</span>
    {"".join(f'<span class="legend-item"><span class="legend-swatch" style="background:{very_light_hex(c)};border:2px solid {c};"></span>{PHASE_LABELS.get(k, k)}</span>' for k, c in PHASE_COLORS.items())}
    <span class="legend-item"><span class="legend-diamond" style="border-radius:50%;"><span class="material-icons" style="font-size:10px;color:#fff;">diamond</span></span>Saillant</span>
    <span class="legend-item"><span class="legend-diamond" style="background:#E67E22;border-radius:2px;"><span class="material-icons" style="font-size:10px;color:#fff;">open_in_full</span></span>Prolongement</span>
    <span class="legend-item"><span class="legend-diamond" style="background:#2980B9;border-radius:2px;"><span class="material-icons" style="font-size:10px;color:#fff;">bolt</span></span>Accélération</span>
    <span class="legend-item"><span class="legend-diamond" style="background:#c0392b;border-radius:2px;"><span class="material-icons" style="font-size:10px;color:#fff;">close</span></span>Avortement</span>
    <span class="legend-item"><span class="legend-diamond" style="background:#8B0000;border-radius:2px;"><span class="material-icons" style="font-size:10px;color:#fff;">restart_alt</span></span>Reboot</span>
    {"<span class='legend-item'><span class='legend-swatch' style=" + '"' + "background:rgba(130,110,85,0.25);border:1.5px solid rgba(130,110,85,0.40);" + '"' + "></span>Noyau territorial</span><span class='legend-item'><span class='legend-swatch' style=" + '"' + "background:rgba(175,165,150,0.13);border:1.5px solid rgba(140,128,115,0.35);" + '"' + "></span>Marges</span>" if has_area_data else ""}
</div>

<div class="tooltip" id="tooltip"></div>
<div class="detail-overlay" id="detailOverlay" onclick="closeDetail()"></div>
<div class="detail-panel" id="detailPanel">
    <div class="detail-panel-header" id="detailHeader"></div>
    <div class="detail-panel-content" id="detailContent"></div>
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

// Layout saillants: measure real label widths and assign rows to avoid overlap
(function layoutSaillants() {{
    const ROW_HEIGHT = 90;
    const MAX_ROWS = 6;
    const BASE_TOP = {area_chart_top + 85 if has_area_data else 200};
    const MARGIN = 6; // px of horizontal breathing room between labels

    const groups = Array.from(document.querySelectorAll('.saillant-group'));
    if (!groups.length) return;

    // Sort by left position (already sorted in HTML, but be safe)
    groups.sort((a, b) => parseFloat(a.style.left) - parseFloat(b.style.left));

    // For each saillant, compute the horizontal extent of its label
    // relative to the timeline container
    const container = groups[0].parentElement;
    const containerRect = container.getBoundingClientRect();

    const extents = groups.map(g => {{
        const label = g.querySelector('.saillant-label');
        const marker = g.querySelector('.saillant-marker');
        // Use the wider of label vs marker for the horizontal footprint
        const labelRect = label.getBoundingClientRect();
        const markerRect = marker.getBoundingClientRect();
        const left = Math.min(labelRect.left, markerRect.left) - containerRect.left;
        const right = Math.max(labelRect.right, markerRect.right) - containerRect.left;
        return {{ left: left - MARGIN, right: right + MARGIN }};
    }});

    // Greedy row assignment: for each saillant, find the lowest row
    // where it doesn't overlap with any already-placed saillant
    const rows = [];
    const rowExtents = [];

    for (let i = 0; i < groups.length; i++) {{
        const ext = extents[i];
        let row = 0;
        while (row < MAX_ROWS - 1) {{
            const occupied = rowExtents[row] || [];
            const conflict = occupied.some(o => !(ext.right < o.left || ext.left > o.right));
            if (!conflict) break;
            row++;
        }}
        rows.push(row);
        if (!rowExtents[row]) rowExtents[row] = [];
        rowExtents[row].push(ext);
    }}

    // Apply positions
    for (let i = 0; i < groups.length; i++) {{
        groups[i].style.top = (BASE_TOP + rows[i] * ROW_HEIGHT) + 'px';
    }}

    // Adjust timeline container min-height to fit all rows
    const maxRow = Math.max(...rows);
    const neededHeight = BASE_TOP + (maxRow + 1) * ROW_HEIGHT + 120;
    const current = parseInt(getComputedStyle(container).minHeight) || 0;
    if (neededHeight > current) {{
        container.style.minHeight = neededHeight + 'px';
    }}
}})();

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

    // Figure portrait images (Wikimedia Commons, public domain)
    const figureImages = {{
        // France
        'Louis VI le Gros': 'images/france/louis-vi-le-gros.jpg',
        'Louis IX': 'images/france/louis-ix.jpg',
        'Philippe le Bel': 'images/france/philippe-le-bel.jpg',
        'Philippe Auguste': 'images/france/philippe-auguste.jpg',
        'Philippe VI': 'images/france/philippe-vi.jpg',
        'François Ier': 'images/france/francois-ier.jpg',
        'Henri IV': 'images/france/henri-iv.jpg',
        'Louis XIV': 'images/france/louis-xiv.jpg',
        'Bonaparte': 'images/france/bonaparte.jpg',
        'La Fronde': 'images/france/la-fronde.jpg',
        'Loi salique': 'images/france/loi-salique.png',
        'Traité de Troyes': 'images/france/traite-de-troyes.jpg',
        'Chinon': 'images/france/chinon.jpg',
        'Charles VII': 'images/france/charles-vii.jpg',
        'Guerres de Religion': 'images/france/guerres-de-religion.jpg',
        'Polysynodie': 'images/france/polysynodie.jpg',
        'Robespierre': 'images/france/robespierre.jpg',
        // Angleterre
        'Henri VII': 'images/angleterre/henri-vii.jpg',
        'Henri VIII': 'images/angleterre/henri-viii.jpg',
        'Élisabeth Ière': 'images/angleterre/elisabeth-iere.jpg',
        'Oliver Cromwell': 'images/angleterre/oliver-cromwell.jpg',
        'Cromwell': 'images/angleterre/oliver-cromwell.jpg',
        'Guillaume le Conquérant': 'images/angleterre/guillaume-le-conquerant.jpg',
        'Édouard Ier': 'images/angleterre/edouard-ier.jpg',
        'Édouard III': 'images/angleterre/edouard-iii.jpg',
        // Israël
        'Saül': 'images/israel/saul.jpg',
        'Salomon': 'images/israel/salomon.jpg',
        'Hérode': 'images/israel/herode.jpg',
        // Bavière
        'Maximilien Ier': 'images/baviere/maximilien-ier.jpg',
        'Max-Emmanuel': 'images/baviere/max-emmanuel.png',
        'Maximilien III Joseph': 'images/baviere/maximilien-iii-joseph.jpg',
        'Louis Ier': 'images/baviere/louis-ier.jpg',
        'Kurt Eisner': 'images/baviere/kurt-eisner.jpg',
        // Venise
        'Francesco Foscari': 'images/venise/francesco-foscari.jpg',
        'Francesco Morosini': 'images/venise/francesco-morosini.jpg',
        'Daniele Manin': 'images/venise/daniele-manin.jpg',
    }};

    // Concept descriptions for subtitles
    const concepts = {{
        'Éveil féodal': 'Premier chef dont l\\'autorité supra-régionale est effective',
        'Pic féodal': 'Roi fort au sommet de sa puissance personnelle',
        'Crise féodale': 'Effondrement du système personnel du suzerain',
        'Pacte oligarchique': 'Les oligarques codifient collectivement la structure de l\\'exécutif',
        '1er monarque oligarchique': 'Premier souverain disposant d\\'un État central permanent',
        'Pic oligarchique': 'Pic de puissance et de prestige de la phase oligarchique',
        'Fin de l\\'expansion': 'L\\'expansion extérieure cesse, les tensions internes prennent le relais',
        'Guerre sociale': 'Conflit factieux résolu par le triomphe de l\\'État central',
        '1er monarque absolu': 'Figure qui résout la guerre sociale et concentre le pouvoir',
        'Dernière grande révolte oligarchique': 'Dernier sursaut armé des oligarques contre l\\'exécutif',
        'Pic absolutiste': 'Sommet de la puissance absolutiste — prestige et expansion maximaux',
        'Remontrance': 'Tentative institutionnelle de reprendre des prérogatives au pouvoir absolu',
        'Explosion de l\\'AR': 'L\\'Ancien Régime perd sa légitimité et sa capacité financière',
        'Expérience parlementaire': 'On expérimente le parlementarisme après le renversement de l\\'ancien ordre',
        'Phase aiguë': 'L\\'extrême-gauche prend le contrôle et élimine les modérés',
        'Moment thermidorien': 'Le centre reprend le pouvoir et purge l\\'extrême-gauche',
        'Impérialiste Revanchard': 'Figure autoritaire qui renoue avec la verticalité du pouvoir',
        'Restauration': 'Retour de la monarchie dans un cadre constitutionnel préservant les acquis révolutionnaires',
        'Glorieuse Révolution': 'Réplique qui ancre définitivement le parlementarisme',
        'Écrasement': 'La Révolution Nationale est interrompue avant d\\'aboutir',
        'Choc d\\'hétérogénéité': 'Expansion territoriale qui hétérogénéise brutalement la société',
        'Avortement': 'Phase interrompue avant sa résolution naturelle',
        'Absorption dans le Parcours allemand': 'Le Parcours bavarois est absorbé dans le Parcours allemand',
    }};
    const conceptSubtitle = concepts[e.title] || '';

    // === HEADER ===
    let headerHtml = `<div class="detail-panel-header-top">`;
    headerHtml += `<span class="detail-panel-title">Détails du ${{kindLabel.toLowerCase()}}</span>`;
    headerHtml += `<button class="detail-close" onclick="closeDetail()"><span class="material-symbols-outlined">close</span></button>`;
    headerHtml += `</div>`;
    headerHtml += `<div class="detail-badges">`;
    headerHtml += `<span class="detail-kind" style="background:${{color}}">${{phaseLabel}}</span>`;
    if (e.confidence) headerHtml += `<span class="confidence-badge ${{confClass}}">Confiance : ${{confLabel}}</span>`;
    headerHtml += `</div>`;
    document.getElementById('detailHeader').innerHTML = headerHtml;

    // === CONTENT ===
    let html = '';

    // Title section
    html += `<section>`;
    html += `<span class="detail-section-label">Nom de l'événement</span>`;
    html += `<div class="detail-title">${{e.title}}</div>`;
    if (e.subtitle) html += `<div class="detail-subtitle">${{e.subtitle}}</div>`;
    else if (conceptSubtitle) html += `<div class="detail-subtitle">${{conceptSubtitle}}</div>`;
    html += `</section>`;

    // Data cards — adapted for phases/subphases vs saillants
    const isPhaseOrSub = (e.kind === 'phase' || e.kind === 'subphase');
    html += `<section><div class="detail-cards">`;
    if (isPhaseOrSub) {{
        // Separate start/end for phases
        const startLabel = formatYear(e.start, e.start_approx);
        const endLabel = e.end !== null ? formatYear(e.end, e.end_approx) : 'en cours';
        html += `<div class="detail-card"><div class="detail-section-label">Début</div><div class="detail-card-value">${{startLabel}}</div></div>`;
        html += `<div class="detail-card"><div class="detail-section-label">Fin</div><div class="detail-card-value">${{endLabel}}</div></div>`;
    }} else {{
        html += `<div class="detail-card"><div class="detail-section-label">Date</div><div class="detail-card-value">${{dates}}</div></div>`;
        if (e.perturbation_type) {{
            html += `<div class="detail-card"><div class="detail-section-label">Type</div><div class="detail-card-value">${{e.perturbation_type}}</div></div>`;
        }} else {{
            html += `<div class="detail-card"><div class="detail-section-label">${{kindLabel}}</div><div class="detail-card-value">${{phaseLabel}}</div></div>`;
        }}
    }}
    html += `</div></section>`;

    // Duration section for phases/subphases
    if (isPhaseOrSub && e.start !== null && e.end !== null) {{
        const duration = e.end - e.start;

        // Parse typical duration to compute deviation
        let typicalYears = null;
        let deviationPct = 0;
        let deviationStatus = '';  // 'normal', 'short', 'long'
        let deviationColor = '#2e7d32';  // green by default
        let deviationLabel = 'Dans la norme';
        let deviationIcon = 'check_circle';

        if (e.typical_duration) {{
            const m = e.typical_duration.match(/(\\d+)/);
            if (m) {{
                typicalYears = parseInt(m[1]);
                deviationPct = Math.round(((duration - typicalYears) / typicalYears) * 100);
                if (deviationPct > 20) {{
                    deviationStatus = 'long';
                    deviationColor = '#e65100';
                    deviationLabel = `+${{deviationPct}}% — plus longue que la norme`;
                    deviationIcon = 'trending_up';
                }} else if (deviationPct < -20) {{
                    deviationStatus = 'short';
                    deviationColor = '#1565c0';
                    deviationLabel = `${{deviationPct}}% — plus courte que la norme`;
                    deviationIcon = 'trending_down';
                }} else {{
                    deviationLabel = `${{deviationPct > 0 ? '+' : ''}}${{deviationPct}}% — dans la norme`;
                }}
            }}
        }}

        html += `<section><div class="detail-cards">`;
        html += `<div class="detail-card"><div class="detail-section-label">Durée observée</div><div class="detail-card-value">~${{duration}} ans</div></div>`;
        if (typicalYears) {{
            html += `<div class="detail-card"><div class="detail-section-label">Durée typique</div><div class="detail-card-value" style="color:#7f756b;">~${{typicalYears}} ans</div></div>`;
        }}
        html += `</div></section>`;

        if (typicalYears) {{
            html += `<section><div style="display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:8px;background:${{deviationColor}}10;color:${{deviationColor}};font-size:0.78rem;font-weight:600;">`;
            html += `<span class="material-symbols-outlined" style="font-size:16px;">${{deviationIcon}}</span>`;
            html += `${{deviationLabel}}`;
            html += `</div></section>`;
        }}
    }}

    // Figure card with portrait
    if (e.figure) {{
        const imgUrl = figureImages[e.figure] || null;
        html += `<section><div class="detail-figure">`;
        if (imgUrl) {{
            html += `<img src="${{imgUrl}}" alt="${{e.figure}}" class="detail-figure-portrait" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">`;
            html += `<div class="detail-figure-icon" style="display:none;"><span class="material-icons">person</span></div>`;
        }} else {{
            html += `<div class="detail-figure-icon"><span class="material-icons">person</span></div>`;
        }}
        html += `<div class="detail-figure-info">`;
        html += `<span class="detail-section-label">Figure clé</span>`;
        html += `<div class="detail-figure-name">${{e.figure}}</div>`;
        html += `</div></div></section>`;
    }}

    // Synthèse historique
    if (e.summary) {{
        html += `<section>`;
        html += `<span class="detail-section-label">Synthèse historique</span>`;
        html += `<p>${{e.summary}}</p>`;
        html += `</section>`;
    }}

    // Description détaillée
    if (e.description) {{
        html += `<section>`;
        html += `<span class="detail-section-label">Analyse détaillée</span>`;
        html += `<div class="detail-description">${{e.description}}</div>`;
        html += `</section>`;
    }}

    // Metadata supplémentaires
    if (e.deviation) {{
        html += `<section><span class="detail-section-label">Déviation</span><p style="color:#715b3e;">${{e.deviation}}</p></section>`;
    }}
    if (e.affected_motor) {{
        html += `<section><span class="detail-section-label">Moteur affecté</span><p>${{e.affected_motor}}</p></section>`;
    }}
    if (e.alternatives) {{
        html += `<section><span class="detail-section-label">Alternatives envisagées</span><p style="font-style:italic;">${{e.alternatives}}</p></section>`;
    }}

    // Résolution
    if (e.resolution) {{
        const isAborted = e.resolution.startsWith('AVORTÉE');
        const resColor = isAborted ? '#ba1a1a' : '#2e7d32';
        const resIcon = isAborted ? '✗' : '✓';
        html += `<hr class="detail-divider">`;
        html += `<section><span class="detail-section-label">Résolution ${{resIcon}}</span><p style="color:${{resColor}};font-weight:600;">${{e.resolution}}</p></section>`;
    }}
    if (e.resolution_conditions) {{
        html += `<section><span class="detail-section-label">Conditions de résolution</span><p>${{e.resolution_conditions}}</p></section>`;
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
