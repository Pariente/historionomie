#!/usr/bin/env python3
"""
Génère des fichiers HTML à partir des fichiers méthodologiques (.md)
du projet historionomie, enrichis d'exemples tirés des parcours nationaux.

Usage: python3 scripts/generate_html.py
Output: site/*.html
"""

import os
import re
import html as html_module
from pathlib import Path

# --- Configuration ---

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
NATIONS = REFS / "nations"
SITE = ROOT / "docs"

METHODOLOGY_FILES = [
    ("parcours.md", "Le Parcours de construction nationale", "#8B7355"),
    ("phase_pre_feodale.md", "Phase pré-féodale", "#A0A0A0"),
    ("phase_feodale.md", "Phase féodale", "#8B7355"),
    ("phase_oligarchique.md", "Phase oligarchique", "#2E8B57"),
    ("phase_absolutiste.md", "Phase absolutiste", "#6A0DAD"),
    ("phase_rn.md", "Révolution Nationale", "#D4A017"),
    ("phase_parlementaire.md", "Phase parlementaire", "#1E90FF"),
    ("elites.md", "Les élites", "#8B7355"),
    ("perturbations.md", "Perturbations", "#8B7355"),
]

# Mapping: methodology file → which saillant titles to extract from parcours
EXAMPLES_MAP = {
    "phase_feodale.md": [
        "Éveil féodal", "Pic féodal", "Crise féodale", "Pacte oligarchique"
    ],
    "phase_oligarchique.md": [
        "1er monarque oligarchique", "Acmé oligarchique",
        "Fin de l'expansion", "Guerre sociale"
    ],
    "phase_absolutiste.md": [
        "1er monarque absolu", "Dernière grande révolte oligarchique",
        "Acmé absolutiste", "Fin de l'expansion", "Remontrance"
    ],
    "phase_rn.md": [
        "Éclatement de l'AR", "Expérience parlementaire",
        "Phase aiguë", "Moment thermidorien",
        "Émergence de l'IR", "Restauration", "Glorieuse Révolution"
    ],
    "elites.md": [
        "Guerre sociale", "1er monarque absolu"
    ],
    "perturbations.md": ["__perturbations__"],  # special handling
}

NATION_LABELS = {
    "france": "France",
    "angleterre": "Angleterre",
    "israel": "Israël",
    "espagne": "Espagne",
    "venise": "Venise",
    "baviere": "Bavière",
    "piemont": "Piémont",
    "milan": "Milan",
    "suisse": "Suisse",
    "autriche": "Autriche",
    "allemagne": "Allemagne",
    "boheme": "Bohême",
    "chili": "Chili",
    "hongrie": "Hongrie",
}

NATION_FLAGS = {
    "France": "../docs/images/france/flag.png",
    "Angleterre": "../docs/images/angleterre/flag.png",
    "Israël": "../docs/images/israel/flag.png",
    "Israël antique": "../docs/images/israel/flag.png",
    "Israël (prolongement)": "../docs/images/israel/flag.png",
    "Espagne": "../docs/images/espagne/flag.png",
    "Venise": "../docs/images/venise/flag.png",
    "Bavière": "../docs/images/baviere/flag.png",
    "Piémont": "../docs/images/piemont/flag.png",
    "Milan": "../docs/images/milan/flag.png",
    "Suisse": "../docs/images/suisse/flag.png",
    "Autriche": "../docs/images/autriche/flag.png",
    "Allemagne": "../docs/images/baviere/flag.png",
    "Bohême": "../docs/images/boheme/flag.png",
    "Chili": "../docs/images/chili/flag.png",
    "Hongrie": "../docs/images/hongrie/flag.png",
}

# Icon + color per saillant title (matches docs/index.html)
SAILLANT_ICONS = {
    'Éveil féodal': ('wb_sunny', '#8B7355'),
    'Pic féodal': ('terrain', '#8B7355'),
    'Crise féodale': ('close', '#8B7355'),
    'Pacte oligarchique': ('gavel', '#8B7355'),
    '1er monarque oligarchique': ('stars', '#2E8B57'),
    'Acmé oligarchique': ('terrain', '#2E8B57'),
    "Fin de l'expansion": ('block', '#2E8B57'),
    'Guerre sociale': ('local_fire_department', '#2E8B57'),
    '1er monarque absolu': ('crown', '#6A0DAD'),
    'Dernière grande révolte oligarchique': ('whatshot', '#6A0DAD'),
    'Acmé absolutiste': ('terrain', '#6A0DAD'),
    'Remontrance': ('record_voice_over', '#6A0DAD'),
    "Éclatement de l'AR": ('flash_on', '#D4A017'),
    'Expérience parlementaire': ('account_balance', '#D4A017'),
    'Phase aiguë': ('skull', '#D4A017'),
    'Moment thermidorien': ('balance', '#D4A017'),
    "Émergence de l'IR": ('military_tech', '#D4A017'),
    'Restauration': ('star', '#D4A017'),
    'Glorieuse Révolution': ('star', '#D4A017'),
    'choc_heterogeneite': ('open_in_full', '#ba1a1a'),
    'choc_exogene': ('bolt', '#ba1a1a'),
    'insuffisance_interne': ('close', '#ba1a1a'),
    'correction_echelle': ('compress', '#ba1a1a'),
}

# --- Markdown to HTML converter ---


def escape(text):
    return html_module.escape(text)


MATERIAL_ICON_NAMES = {
    'open_in_full', 'bolt', 'close', 'compress', 'wb_sunny', 'terrain',
    'gavel', 'stars', 'local_fire_department', 'block', 'crown', 'whatshot',
    'record_voice_over', 'flash_on', 'account_balance', 'skull', 'balance',
    'military_tech', 'star', 'swords', 'circle', 'restart_alt',
}


def convert_inline(text):
    """Convert inline markdown (bold, italic, code, links) to HTML."""
    # Strip emoji circles (used in perturbations.md tables)
    text = re.sub(r'[🟠🔵🔴🟤]\s*', '', text)
    # Strip diamond markers
    text = re.sub(r'◆\s*', '', text)

    segments = re.split(r'(`[^`]+`)', text)
    converted = []
    for seg in segments:
        if seg.startswith('`') and seg.endswith('`') and len(seg) > 1:
            icon_name = seg[1:-1].strip()
            if icon_name in MATERIAL_ICON_NAMES:
                converted.append(
                    f'<span class="material-symbols-outlined" '
                    f'style="font-size:1.1rem;vertical-align:-3px;">'
                    f'{icon_name}</span>'
                )
            else:
                converted.append(f'<code>{escape(icon_name)}</code>')
        else:
            s = seg
            # Links: [text](url)
            s = re.sub(
                r'\[([^\]]+)\]\(([^)]+)\)',
                r'<a href="\2">\1</a>',
                s
            )
            # Bold: **text**
            s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
            # Italic: *text*
            s = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', s)
            # Em-dash
            s = s.replace(' — ', ' &mdash; ')
            converted.append(s)

    return ''.join(converted)


def markdown_to_html(text):
    """Convert a markdown document to HTML body content + extract TOC."""
    lines = text.split('\n')
    html_lines = []
    toc = []
    in_table = False
    in_code_block = False
    in_list = False
    in_blockquote = False
    in_recap_section = False  # skip "Tableau récapitulatif" (replaced by dynamic examples)
    list_items = []
    table_rows = []
    blockquote_lines = []
    first_h1_skipped = False

    def flush_list():
        nonlocal in_list, list_items
        if in_list and list_items:
            html_lines.append('<ul>')
            for item in list_items:
                html_lines.append(f'  <li>{convert_inline(item)}</li>')
            html_lines.append('</ul>')
            list_items = []
            in_list = False

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            headers = [c.strip() for c in table_rows[0].split('|')[1:-1]]
            header_lower = [h.lower() for h in headers]

            # Detect example tables (contain a "Nation" column)
            has_nation = 'nation' in header_lower
            if has_nation and len(table_rows) > 2:
                nation_idx = header_lower.index('nation')
                # Find date and example/text columns
                date_idx = None
                text_idx = None
                for i, h in enumerate(header_lower):
                    if h in ('date', 'période', 'dates'):
                        date_idx = i
                    if h in ('exemple', 'exemples', 'noyau', 'marges'):
                        text_idx = i
                # Use last column as text if not found
                if text_idx is None:
                    text_idx = len(headers) - 1

                # Render as example cards
                html_lines.append('<div class="saillant-examples">')
                for ri in range(2, len(table_rows)):  # skip header + separator
                    cells = [c.strip() for c in table_rows[ri].split('|')[1:-1]]
                    if len(cells) <= nation_idx:
                        continue
                    nation_raw = re.sub(r'\*\*([^*]+)\*\*', r'\1', cells[nation_idx]).strip()
                    flag_src = NATION_FLAGS.get(nation_raw, '')
                    date_val = cells[date_idx].strip() if date_idx is not None and date_idx < len(cells) else ''
                    # Collect all non-nation, non-date cells as description
                    desc_parts = []
                    for i, cell in enumerate(cells):
                        if i != nation_idx and i != date_idx:
                            desc_parts.append(cell.strip())
                    desc_text = ' — '.join(p for p in desc_parts if p)
                    desc_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', desc_text)  # strip bold

                    flag_html = f'<img class="card-flag" src="{flag_src}" alt="{escape(nation_raw)}">' if flag_src else ''
                    date_html = f'<span class="card-date">{escape(date_val)}</span>' if date_val else ''

                    html_lines.append(
                        f'<div class="example-card">'
                        f'<div class="card-content">'
                        f'<div class="card-header">'
                        f'{flag_html}'
                        f'<span class="card-title">{escape(nation_raw)}</span>'
                        f'{date_html}'
                        f'</div>'
                        f'<span class="card-desc">{convert_inline(desc_text)}</span>'
                        f'</div>'
                        f'</div>'
                    )
                html_lines.append('</div>')
            else:
                # Regular table
                html_lines.append('<div class="table-wrapper"><table>')
                for ri, row in enumerate(table_rows):
                    if ri == 1:  # separator row
                        continue
                    tag = 'th' if ri == 0 else 'td'
                    if ri == 0:
                        html_lines.append('<thead>')
                    elif ri == 2:
                        html_lines.append('<tbody>')
                    html_lines.append('  <tr>')
                    cells = [c.strip() for c in row.split('|')[1:-1]]
                    for cell in cells:
                        html_lines.append(f'    <{tag}>{convert_inline(cell)}</{tag}>')
                    html_lines.append('  </tr>')
                    if ri == 0:
                        html_lines.append('</thead>')
                if len(table_rows) > 2:
                    html_lines.append('</tbody>')
                html_lines.append('</table></div>')
            table_rows = []
            in_table = False

    def flush_blockquote():
        nonlocal in_blockquote, blockquote_lines
        if in_blockquote and blockquote_lines:
            html_lines.append('<blockquote>')
            html_lines.append(f'<p>{convert_inline(" ".join(blockquote_lines))}</p>')
            html_lines.append('</blockquote>')
            blockquote_lines = []
            in_blockquote = False

    for line in lines:
        stripped = line.strip()

        # Skip content inside "Tableau récapitulatif" section (non-header lines)
        if in_recap_section:
            header_match_check = re.match(r'^(#{1,2})\s+(.+)$', stripped)
            if header_match_check and 'tableau récapitulatif' not in header_match_check.group(2).lower():
                in_recap_section = False
                # fall through to process this header
            else:
                continue

        # Code blocks
        if stripped.startswith('```'):
            if in_code_block:
                html_lines.append('</code></pre>')
                in_code_block = False
            else:
                flush_list()
                flush_table()
                flush_blockquote()
                lang = stripped[3:].strip()
                html_lines.append(f'<pre><code class="language-{lang}">' if lang else '<pre><code>')
                in_code_block = True
            continue

        if in_code_block:
            html_lines.append(escape(line))
            continue

        # Empty line
        if not stripped:
            flush_list()
            flush_table()
            flush_blockquote()
            continue

        # Blockquote
        if stripped.startswith('> '):
            flush_list()
            flush_table()
            in_blockquote = True
            blockquote_lines.append(stripped[2:])
            continue
        elif in_blockquote:
            flush_blockquote()

        # Table
        if '|' in stripped and stripped.startswith('|'):
            flush_list()
            flush_blockquote()
            in_table = True
            table_rows.append(stripped)
            continue
        elif in_table:
            flush_table()

        # Headers
        header_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if header_match:
            flush_list()
            flush_table()
            flush_blockquote()
            level = len(header_match.group(1))
            title = header_match.group(2)
            # Skip the first h1 (already in hero)
            if level == 1 and not first_h1_skipped:
                first_h1_skipped = True
                continue
            # Skip "Tableau récapitulatif" sections (replaced by dynamic examples)
            if 'tableau récapitulatif' in title.lower():
                in_recap_section = True
                continue
            # End recap section when a new h2 starts
            if in_recap_section and level <= 2:
                in_recap_section = False
            if in_recap_section:
                continue
            # Clean "Saillant : " prefix from h3 titles
            display_title = title
            saillant_name = None
            if level == 3 and title.startswith('Saillant : '):
                saillant_name = title[len('Saillant : '):]
                # Strip "(récurrent)" suffix for icon lookup
                saillant_lookup = re.sub(r'\s*\(récurrent\)', '', saillant_name)
                display_title = saillant_name

            anchor = re.sub(r'[^a-z0-9àâäéèêëïîôùûüç]+', '-', title.lower()).strip('-')
            toc.append((level, display_title, anchor))

            # Add Material icon for saillant h3
            icon_html = ''
            if saillant_name:
                saillant_lookup = re.sub(r'\s*\(récurrent\)', '', saillant_name)
                icon_info = SAILLANT_ICONS.get(saillant_lookup)
                if icon_info:
                    iname, icolor = icon_info
                    ifill = "font-variation-settings:'FILL' 1;" if iname in ('crown', 'skull') else ''
                    icon_html = f'<span class="material-symbols-outlined h3-icon" style="color:{icolor};{ifill}">{iname}</span>'

            html_lines.append(
                f'<h{level} id="{anchor}">'
                f'{icon_html}'
                f'{convert_inline(display_title)}'
                f'<a class="anchor" href="#{anchor}">#</a>'
                f'</h{level}>'
            )
            continue

        # Horizontal rule
        if stripped == '---':
            flush_list()
            flush_table()
            flush_blockquote()
            html_lines.append('<hr>')
            continue

        # List items
        if re.match(r'^[-*]\s', stripped):
            in_list = True
            list_items.append(stripped[2:])
            continue
        elif in_list:
            flush_list()

        # Paragraph
        html_lines.append(f'<p>{convert_inline(stripped)}</p>')

    # Flush remaining
    flush_list()
    flush_table()
    flush_blockquote()

    return '\n'.join(html_lines), toc


def build_toc_html(toc):
    """Build a table of contents from extracted headers."""
    if not toc:
        return ''
    # Only include h2 and h3
    filtered = [(l, t, a) for l, t, a in toc if l in (2, 3)]
    if not filtered:
        return ''

    parts = ['<nav class="toc"><h2>Sommaire</h2><ul>']
    current_level = 2
    for level, title, anchor in filtered:
        if level > current_level:
            parts.append('<ul>')
        elif level < current_level:
            parts.append('</ul>')
        current_level = level
        parts.append(f'<li><a href="#{anchor}">{escape(title)}</a></li>')
    while current_level > 2:
        parts.append('</ul>')
        current_level -= 1
    parts.append('</ul></nav>')
    return '\n'.join(parts)


# --- Parcours parser (extract examples) ---


def parse_parcours(filepath):
    """Parse a parcours.md file and extract saillants and perturbations."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    saillants = []
    current = None

    for line in content.split('\n'):
        stripped = line.strip()

        # Detect saillant or perturbation blocks
        if stripped.startswith('#### Saillant :') or stripped.startswith('### Perturbation :'):
            if current:
                saillants.append(current)
            current = {}
            continue

        if stripped.startswith('## Phase :') or stripped.startswith('### Subphase :'):
            if current:
                saillants.append(current)
                current = None
            continue

        if current is not None:
            if stripped.startswith('- type:'):
                current['type'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- title:'):
                current['title'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- start:'):
                current['start'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- figure:'):
                current['figure'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- subtitle:'):
                current['subtitle'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- summary:'):
                current['summary'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- perturbation: true'):
                current['perturbation'] = True
            elif stripped.startswith('- mechanism:'):
                current['mechanism'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- effect:'):
                current['effect'] = stripped.split(':', 1)[1].strip()
            elif stripped.startswith('- confidence:'):
                current['confidence'] = stripped.split(':', 1)[1].strip()

    if current:
        saillants.append(current)

    return saillants


def extract_all_examples():
    """Extract saillants from all nation parcours files."""
    all_examples = {}

    for nation_dir in sorted(NATIONS.iterdir()):
        if not nation_dir.is_dir():
            continue
        nation_key = nation_dir.name
        label = NATION_LABELS.get(nation_key, nation_key.capitalize())

        # Try parcours.md, then parcours_h1.md
        parcours_file = nation_dir / "parcours.md"
        if not parcours_file.exists():
            parcours_file = nation_dir / "parcours_h1.md"
        if not parcours_file.exists():
            continue

        saillants = parse_parcours(parcours_file)
        for s in saillants:
            s['nation'] = label

        all_examples[nation_key] = saillants

    return all_examples


def build_examples_section(methodology_file, all_examples):
    """Build an HTML section with collapsible example cards (matching docs/index.html)."""
    target_titles = EXAMPLES_MAP.get(methodology_file, [])
    if not target_titles:
        return ''

    is_perturbations = "__perturbations__" in target_titles

    # Collect matching saillants
    by_title = {}
    for nation_key, saillants in all_examples.items():
        for s in saillants:
            title = s.get('title', '')
            if is_perturbations:
                if s.get('perturbation') or s.get('type') == 'perturbation':
                    group_key = s.get('mechanism', 'inconnu')
                    by_title.setdefault(group_key, []).append(s)
            else:
                if title in target_titles:
                    by_title.setdefault(title, []).append(s)

    if not by_title:
        return ''

    parts = ['<section class="examples">',
             '<h2 id="exemples-du-corpus">Exemples du corpus'
             '<a class="anchor" href="#exemples-du-corpus">#</a></h2>',
             '<p class="examples-intro">Saillants identifiés dans les parcours nationaux déjà mappés.</p>',
             '<div class="saillant-list">']

    # Sort titles
    if is_perturbations:
        mechanism_order = ['choc_heterogeneite', 'choc_exogene', 'insuffisance_interne', 'correction_echelle']
        ordered_titles = sorted(by_title.keys(),
                                key=lambda k: mechanism_order.index(k) if k in mechanism_order else 99)
    else:
        ordered_titles = [t for t in target_titles if t in by_title]

    mechanism_labels = {
        'choc_heterogeneite': 'Choc d\'hétérogénéité',
        'choc_exogene': 'Choc exogène',
        'insuffisance_interne': 'Insuffisance interne',
        'correction_echelle': 'Correction d\'échelle',
    }

    for title in ordered_titles:
        examples_list = by_title[title]
        display_title = mechanism_labels.get(title, title) if is_perturbations else title
        icon_name, icon_color = SAILLANT_ICONS.get(title, ('circle', '#888'))
        fill_style = "font-variation-settings:'FILL' 1;" if icon_name in ('crown', 'skull') else ''

        # Sort by date
        def sort_key(s):
            d = s.get('start', '0')
            try:
                return int(d.replace('~', '').replace(' ', ''))
            except ValueError:
                return 0

        sorted_examples = sorted(examples_list, key=sort_key)

        # Build collapsible
        parts.append('<details class="saillant-details">')
        parts.append(
            f'<summary>'
            f'<span class="saillant-left">'
            f'<span class="material-symbols-outlined" style="color:{icon_color};{fill_style}">{icon_name}</span>'
            f'<span>{escape(display_title)}</span>'
            f'</span>'
            f'<span class="material-symbols-outlined expand-icon">chevron_right</span>'
            f'</summary>'
        )
        parts.append('<div class="saillant-body">')

        # Example cards grid
        parts.append('<div class="saillant-examples">')
        for s in sorted_examples:
            nation = s.get('nation', '')
            flag_src = NATION_FLAGS.get(nation, '')
            start = escape(s.get('start', ''))
            figure = escape(s.get('figure', s.get('subtitle', '')))
            summary_text = s.get('summary', '')
            if len(summary_text) > 180:
                summary_text = summary_text[:177] + '...'
            summary_text = escape(summary_text)

            # For perturbations, show effect badge + title instead of figure
            if is_perturbations:
                effect_raw = s.get('effect', '')
                effect_badge_class = {
                    'prolongement': 'badge-prolongement',
                    'acceleration': 'badge-acceleration',
                    'avortement': 'badge-avortement',
                    'reboot': 'badge-reboot',
                }.get(effect_raw, '')
                effect_label = {
                    'prolongement': 'Prolongement',
                    'acceleration': 'Accélération',
                    'avortement': 'Avortement',
                    'reboot': 'Reboot',
                }.get(effect_raw, effect_raw)
                card_title = escape(s.get('title', s.get('subtitle', '')))
                badge_html = f' <span class="badge {effect_badge_class}">{effect_label}</span>'
            else:
                card_title = figure if figure else escape(nation)
                badge_html = ''

            flag_html = f'<img class="card-flag" src="{flag_src}" alt="{escape(nation)}">' if flag_src else ''

            parts.append(
                f'<div class="example-card">'
                f'<div class="card-content">'
                f'<div class="card-header">'
                f'{flag_html}'
                f'<span class="card-title">{card_title}{badge_html}</span>'
                f'<span class="card-date">{start}</span>'
                f'</div>'
                f'<span class="card-desc">{summary_text}</span>'
                f'</div>'
                f'</div>'
            )
        parts.append('</div>')  # saillant-examples
        parts.append('</div>')  # saillant-body
        parts.append('</details>')

    parts.append('</div>')  # saillant-list
    parts.append('</section>')
    return '\n'.join(parts)


# --- HTML template ---

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior:smooth; }
body { font-family:'Public Sans', system-ui, sans-serif; background:#f9f9f9; color:#1a1c1c; line-height:1.6; }
.material-symbols-outlined { font-variation-settings:'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }

/* --- Navbar (= docs/index.html) --- */
.navbar { background:#f9f9f9; position:sticky; top:0; z-index:50; display:flex; justify-content:space-between; align-items:center; padding:1rem 2rem; border-bottom:1px solid rgba(209,196,185,0.3); }
.navbar-brand { font-family:'Newsreader', serif; font-size:1.5rem; font-weight:600; font-style:italic; color:#8B7355; text-decoration:none; }
.navbar-links { display:flex; gap:1.5rem; }
.navbar-links a { text-decoration:none; font-size:0.9rem; font-weight:500; color:#888; transition:color 0.2s; }
.navbar-links a:hover { color:#8B7355; }
.navbar-links a.active { color:#8B7355; font-weight:700; border-bottom:2px solid #8B7355; padding-bottom:2px; }

/* --- Layout --- */
.page-grid { margin-left:14rem; min-height:calc(100vh - 3.5rem); }

/* --- Sidebar --- */
.sidebar { position:fixed; top:3.5rem; left:0; width:14rem; height:calc(100vh - 3.5rem); overflow-y:auto; padding:1.5rem 0.8rem 2rem 1rem; background:#f3f3f3; border-right:1px solid rgba(209,196,185,0.2); scrollbar-width:none; z-index:40; }
.sidebar::-webkit-scrollbar { display:none; }
.sidebar-label { font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#999; padding:0 0.4rem; margin-bottom:0.6rem; }
.sidebar-nav { list-style:none; }
.sidebar-nav li { margin:2px 0; }
.sidebar-nav a { display:block; padding:0.4rem 0.6rem; font-size:0.82rem; font-weight:500; color:#666; text-decoration:none; border-radius:6px; transition:background 0.15s, color 0.15s; line-height:1.4; }
.sidebar-nav a:hover { background:rgba(139,115,85,0.04); color:#4d453c; }
.sidebar-nav a.active { background:rgba(139,115,85,0.08); color:#8B7355; font-weight:700; }

/* --- Content --- */
.content { padding:0 2.5rem 4rem; min-width:0; }
.toc-grid { display:grid; grid-template-columns:13rem 1fr; gap:2rem; align-items:start; }
article { max-width:50rem; min-width:0; }

/* --- Hero --- */
.hero { padding:1rem 0 0; max-width:700px; }
.hero-label { display:none; }
.hero h1 { font-family:'Newsreader', serif; font-size:2.4rem; font-weight:600; color:#1a1c1c; line-height:1.15; margin-bottom:0.8rem; border:none; padding:0; }
.hero-divider { height:0; border-bottom:1px solid rgba(209,196,185,0.2); margin-bottom:0.5rem; }

/* --- TOC --- */
nav.toc { position:sticky; top:4.5rem; max-height:calc(100vh - 5.5rem); overflow-y:auto; padding:1rem 0 2rem; scrollbar-width:none; }
nav.toc::-webkit-scrollbar { display:none; }
nav.toc h2 { font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#999; margin:0 0 0.6rem; border:none; padding:0 0.5rem; }
nav.toc ul { list-style:none; padding-left:0; }
nav.toc ul ul { padding-left:0.9rem; }
nav.toc li { margin:2px 0; }
nav.toc a { color:#888; text-decoration:none; display:block; padding:0.2rem 0.5rem; border-radius:4px; line-height:1.4; font-size:0.78rem; transition:background 0.1s, color 0.1s; }
nav.toc a:hover { background:rgba(139,115,85,0.04); color:#4d453c; }
nav.toc > ul > li > a { font-weight:600; color:#666; font-size:0.8rem; }

/* --- Headers --- */
h1, h2, h3, h4, h5, h6 { scroll-margin-top:4.5rem; }
h1 { font-family:'Newsreader', serif; font-size:1.6rem; font-weight:600; color:#1a1c1c; margin:2.5rem 0 0.5rem; border:none; padding:0; }
h2 { font-family:'Newsreader', serif; font-size:1.4rem; font-weight:600; color:var(--phase-color, #8B7355); margin:2.5rem 0 0.6rem; padding-bottom:0.6rem; border-bottom:1px solid rgba(209,196,185,0.2); }
h3 { font-size:0.95rem; font-weight:700; color:#1a1c1c; margin:1.8rem 0 0.4rem; display:flex; align-items:center; gap:0.4rem; padding:0.7rem 0 0.4rem; border-bottom:1px solid rgba(209,196,185,0.15); opacity:0.8; text-transform:uppercase; letter-spacing:1px; }
.h3-icon { font-size:1.1rem; flex-shrink:0; }
h4, h5, h6 { font-size:0.85rem; font-weight:600; color:#666; margin:1.2rem 0 0.3rem; }
.anchor { font-size:0.75em; color:#ccc; text-decoration:none; margin-left:0.4rem; opacity:0; transition:opacity 0.15s; }
h2:hover .anchor, h3:hover .anchor { opacity:1; }

/* --- Body text --- */
p { margin:0.4rem 0 0.7rem; color:#4d453c; font-size:0.9rem; line-height:1.7; }
a { color:#715b3e; text-decoration:none; }
a:hover { text-decoration:underline; }
strong { font-weight:600; color:#1a1c1c; }

/* --- Lists --- */
ul, ol { margin:0.3rem 0; padding-left:1.6rem; }
li { margin:0.25rem 0; line-height:1.65; font-size:0.9rem; color:#4d453c; }

/* --- Code --- */
code { font-family:'SF Mono','Fira Code',monospace; font-size:0.84em; background:#f3f3f3; padding:0.12em 0.35em; border-radius:3px; color:#715b3e; }
pre { background:#f3f3f3; border-radius:8px; padding:1rem; overflow-x:auto; margin:0.8rem 0; }
pre code { background:none; padding:0; font-size:0.82rem; color:#1a1c1c; }

/* --- Tables --- */
.table-wrapper { overflow-x:auto; margin:1rem 0; background:#fff; border-radius:8px; box-shadow:0 12px 32px rgba(26,28,28,0.06); border:1px solid rgba(209,196,185,0.15); }
table { border-collapse:collapse; width:100%; font-size:0.84rem; }
th { font-weight:700; font-size:0.72rem; text-transform:uppercase; letter-spacing:0.5px; color:#8B7355; padding:0.65rem 1rem; text-align:left; border-bottom:1px solid rgba(209,196,185,0.3); background:rgba(139,115,85,0.025); }
td { padding:0.55rem 1rem; text-align:left; vertical-align:top; border-bottom:1px solid rgba(209,196,185,0.1); color:#4d453c; }
tbody tr:hover { background:rgba(139,115,85,0.02); }
td:first-child { font-weight:600; color:#1a1c1c; white-space:nowrap; }
td.summary { font-size:0.78rem; line-height:1.5; max-width:26rem; color:#666; }

/* --- Blockquote --- */
blockquote { border-left:3px solid rgba(209,196,185,0.4); margin:1rem 0; padding:0.3rem 0 0.3rem 1rem; color:#666; font-size:0.9rem; }

/* --- HR --- */
hr { border:none; border-top:1px solid rgba(209,196,185,0.2); margin:2rem 0; }

/* --- Examples --- */
.examples { margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(209,196,185,0.3); }
.examples > h2 { font-family:'Newsreader', serif; font-size:1.3rem; font-weight:500; color:#8B7355; border:none; margin-bottom:0.3rem; padding:0; }
.examples-intro { color:#999; margin-bottom:1.2rem; font-size:0.85rem; font-style:italic; }

/* Saillant accordion (= docs/index.html) */
.saillant-list { display:flex; flex-direction:column; gap:0.4rem; }
details summary::-webkit-details-marker { display:none; }
details[open] summary .expand-icon { transform:rotate(90deg); }
.saillant-details { background:none; border:none; border-radius:0; padding:0; }
.saillant-details summary { display:flex; align-items:center; justify-content:space-between; cursor:pointer; list-style:none; padding:0.55rem 0.4rem; border-radius:6px; transition:background 0.15s; }
.saillant-details summary:hover { background:rgba(139,115,85,0.04); }
.saillant-details summary .saillant-left { display:flex; align-items:center; gap:0.5rem; }
.saillant-details summary .saillant-left .material-symbols-outlined { font-size:1rem; }
.saillant-details summary .saillant-left span:last-child { font-size:0.82rem; font-weight:700; color:#1a1c1c; }
.saillant-details summary .expand-icon { font-size:1rem; color:#b0a28e; transition:transform 0.25s ease, color 0.2s; }
.saillant-details[open] summary .expand-icon { color:#8B7355; }
.saillant-details .saillant-body { padding:0.1rem 0.4rem 0.6rem; }
.saillant-details .saillant-body p { font-size:0.84rem; color:#4d453c; line-height:1.65; margin-bottom:0.7rem; }

/* Example cards (= docs/index.html) */
.saillant-examples { display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:0.55rem; overflow:hidden; }
.example-card { display:flex; align-items:flex-start; gap:0.5rem; font-size:0.78rem; color:#4d453c; padding:0.55rem 0.6rem; background:rgba(139,115,85,0.025); border-radius:6px; border:1px solid rgba(209,196,185,0.15); min-width:0; overflow:hidden; }
.example-card .card-content { flex:1; min-width:0; }
.example-card .card-header { display:flex; align-items:center; gap:0.35rem; margin-bottom:0.15rem; }
.example-card .card-flag { height:11px; width:auto; border-radius:2px; box-shadow:0 0 0 1px rgba(0,0,0,0.06); flex-shrink:0; }
.example-card .card-title { font-weight:700; color:#1a1c1c; font-size:0.78rem; flex:1; min-width:0; }
.example-card .card-date { font-family:'IBM Plex Mono','Courier New',monospace; color:#8B7355; font-size:0.68rem; font-weight:600; white-space:nowrap; flex-shrink:0; font-variant-numeric:tabular-nums; margin-left:auto; }
.example-card .card-title { font-weight:700; color:#1a1c1c; font-size:0.78rem; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.example-card .card-desc { display:block; color:#666; font-size:0.72rem; line-height:1.4; }

/* Badges */
.badge { display:inline-block; padding:2px 8px; font-size:0.6rem; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; border-radius:20px; white-space:nowrap; margin-left:0.3rem; }
.badge-prolongement { background:rgba(255,165,0,0.12); color:#b86e00; }
.badge-acceleration { background:rgba(59,130,246,0.1); color:#2563eb; }
.badge-avortement { background:rgba(220,38,38,0.08); color:#c94a4a; }
.badge-reboot { background:rgba(139,115,85,0.1); color:#715b3e; }

@media (max-width:900px) { .saillant-examples { grid-template-columns:1fr 1fr; } }
@media (max-width:600px) { .saillant-examples { grid-template-columns:1fr; } }

/* --- Footer --- */
footer { border-top:1px solid rgba(209,196,185,0.15); padding:2rem; text-align:center; }
.footer-brand { font-family:'Newsreader', serif; font-weight:600; font-style:italic; color:#8B7355; font-size:1rem; margin-bottom:0.3rem; }
.footer-meta { font-size:0.78rem; color:#999; font-style:italic; }

/* --- Responsive --- */
@media (max-width:1024px) {
    .page-grid { margin-left:0; }
    .sidebar { display:none; }
    .toc-grid { grid-template-columns:1fr; gap:0; }
    nav.toc { position:static; max-height:none; overflow-y:visible; background:#f3f3f3; padding:1rem; margin:1rem 0 1.5rem; border-radius:8px; }
}
@media (max-width:640px) {
    .content { padding:0 1rem 3rem; }
    .hero h1 { font-size:1.8rem; }
    .navbar { padding:0.6rem 1rem; }
}
"""


def build_topnav():
    """Build top navbar matching docs/index.html."""
    return """<nav class="navbar">
<a class="navbar-brand" href="index.html">Historionomie</a>
<div class="navbar-links">
    <a href="index.html">Accueil</a>
    <a class="active" href="parcours.html">Méthodologie</a>
</div>
</nav>"""


def build_sidebar(current_file):
    """Build left sidebar with methodology file links."""
    parts = ['<aside class="sidebar">',
             '<span class="sidebar-label">Méthodologie</span>',
             '<ul class="sidebar-nav">']
    for filename, label, _color in METHODOLOGY_FILES:
        html_name = filename.replace('.md', '.html')
        cls = ' class="active"' if filename == current_file else ''
        parts.append(f'<li><a href="{html_name}"{cls}>{escape(label)}</a></li>')
    parts.append('</ul></aside>')
    return '\n'.join(parts)


def build_page(title, topnav, sidebar, toc, body, examples='', phase_color='#8B7355'):
    """Build a complete HTML page."""
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)} — Historionomie</title>
    <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Public+Sans:wght@100..900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <style>:root {{ --phase-color: {phase_color}; }}{CSS}</style>
</head>
<body>
{topnav}
<div class="page-grid">
{sidebar}
<div class="content">
<div class="hero">
    <span class="hero-label">Section Méthodologique</span>
    <h1>{escape(title)}</h1>
    <div class="hero-divider"></div>
</div>
<div class="toc-grid">
{toc}
<article>
{body}
{examples}
</article>
</div>
</div>
</div>
<footer>
    <div class="footer-brand">Historionomie</div>
    <div class="footer-meta">Cadre théorique de Philippe Fabry — Parcours de construction nationale</div>
</footer>
</body>
</html>"""


# --- Main ---

def main():
    SITE.mkdir(exist_ok=True)

    # Extract all examples from parcours files
    print("Extraction des exemples du corpus...")
    all_examples = extract_all_examples()
    total = sum(len(v) for v in all_examples.values())
    print(f"  {total} saillants extraits de {len(all_examples)} nations")

    # Process each methodology file
    for filename, label, phase_color in METHODOLOGY_FILES:
        filepath = REFS / filename
        if not filepath.exists():
            print(f"  SKIP {filename} (fichier non trouvé)")
            continue

        print(f"  {filename} → {filename.replace('.md', '.html')}")

        with open(filepath, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert markdown to HTML
        body_html, toc = markdown_to_html(md_content)

        # Build TOC
        toc_html = build_toc_html(toc)

        # Build navigation components
        topnav_html = build_topnav()
        sidebar_html = build_sidebar(filename)

        # Build examples section
        examples_html = build_examples_section(filename, all_examples)

        # Add examples to TOC if present
        if examples_html:
            toc_html = toc_html.replace(
                '</ul></nav>',
                '<li><a href="#exemples-du-corpus">Exemples du corpus</a></li></ul></nav>'
            )

        # Build page
        page_html = build_page(label, topnav_html, sidebar_html, toc_html, body_html, examples_html, phase_color)

        # Write output
        out_path = SITE / filename.replace('.md', '.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page_html)

    print(f"\nTerminé. {len(METHODOLOGY_FILES)} fichiers générés dans {SITE}/")


if __name__ == '__main__':
    main()
