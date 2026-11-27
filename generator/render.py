# -*- coding: utf-8 -*-
"""Render every post in content.py to 1080x1350 JPEG slides, plus schedule.csv,
captions.md and a self-contained review page.

Usage:
    pip install playwright pillow
    playwright install chromium
    python render.py                 # writes ../posts, ../schedule.csv, ../captions.md
    python render.py --review out.html   # also writes the review page

Fonts: Crimson Text, Anton and Inter (all free on Google Fonts). Set FONT_DIR to
a folder containing their .ttf/.otf files to render offline; otherwise the
Google Fonts stylesheet is used.
"""
import argparse, base64, csv, html, io, json, math, os, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from content import POSTS, BRAND_HANDLE, TZ_OFFSET  # noqa: E402

ROOT = HERE.parent
W, H = 1080, 1350
C = dict(green="#163F31", paper="#E8EAE1", ink="#0F1713", brass="#C8963E",
         sage="#A4B8AC", graphite="#56635C", light="#EEEFE7", line="#2B4A3E")

# ───────────────────── the unscaled.co mark ─────────────────────
# Semicircle k has radius r/2^k and flips sides each time; the stroke halves every
# half-turn, so the mark is exactly self-similar. It lands on the dot at 2/3 of the width.
def _spiral_outline(r0=100.0, w0=26.0, narcs=14, base_steps=160):
    outer, inner = [], []
    e = -r0
    for k in range(narcs):
        r = r0 / 2 ** k
        even = k % 2 == 0
        cx = e + r if even else e - r
        a0, a1 = (math.pi, 2 * math.pi) if even else (0.0, math.pi)
        n = max(14, int(base_steps / 2 ** (k * 0.5)))
        for i in range(n + 1):
            if k and i == 0:
                continue
            phi = a0 + (a1 - a0) * i / n
            w = w0 * 2 ** (-(k * math.pi + phi - a0) / math.pi)
            c, sn = math.cos(phi), math.sin(phi)
            outer.append((cx + (r + w / 2) * c, (r + w / 2) * sn))
            inner.append((cx + (r - w / 2) * c, (r - w / 2) * sn))
        e = e + 2 * r if even else e - 2 * r
    return outer + inner[::-1]

_LP = _spiral_outline()
_LX0, _LX1 = min(p[0] for p in _LP) - 2, max(p[0] for p in _LP) + 2
_LY0, _LY1 = min(p[1] for p in _LP) - 2, max(p[1] for p in _LP) + 2
LOGO_D = "M" + " L".join(f"{x - _LX0:.1f} {_LY1 - y:.1f}" for x, y in _LP) + "Z"
LOGO_VB = f"0 0 {_LX1 - _LX0:.1f} {_LY1 - _LY0:.1f}"

def logo_svg(cls="lg"):
    return (f'<svg class="{cls}" viewBox="{LOGO_VB}" aria-hidden="true"><path d="{LOGO_D}" fill="currentColor"/>'
            f'<circle class="lgdot" cx="{100.0 / 3 - _LX0:.2f}" cy="{_LY1:.2f}" r="4.6"/></svg>')

# ───────────────────────────── fonts ─────────────────────────────
def font_css():
    fd = os.environ.get("FONT_DIR")
    candidates = {
        "crimson": ["/usr/share/fonts/truetype/google-fonts/ofl/crimsontext"],
        "anton": ["/usr/share/fonts/truetype/google-fonts/ofl/anton"],
        "inter": ["/usr/share/fonts/opentype/inter"],
    }
    if fd:
        for k in candidates:
            candidates[k].insert(0, fd)

    def find(name):
        for key, dirs in candidates.items():
            for d in dirs:
                p = Path(d) / name
                if p.exists():
                    return p.as_uri()
        return None

    faces = [("Crimson Text", "CrimsonText-Regular.ttf", 400, "normal"),
             ("Crimson Text", "CrimsonText-Italic.ttf", 400, "italic"),
             ("Crimson Text", "CrimsonText-SemiBold.ttf", 600, "normal"),
             ("Crimson Text", "CrimsonText-SemiBoldItalic.ttf", 600, "italic"),
             ("Anton", "Anton-Regular.ttf", 400, "normal"),
             ("Inter", "Inter-Regular.otf", 400, "normal"),
             ("Inter", "Inter-Medium.otf", 500, "normal"),
             ("Inter", "Inter-SemiBold.otf", 600, "normal")]
    rules, missing = [], False
    for fam, fn, wt, st in faces:
        uri = find(fn)
        if not uri:
            missing = True
            break
        rules.append(f'@font-face{{font-family:"{fam}";src:url("{uri}");font-weight:{wt};font-style:{st}}}')
    if missing:
        return ('@import url("https://fonts.googleapis.com/css2?family=Anton&family=Crimson+Text:'
                'ital,wght@0,400;0,600;1,400;1,600&family=Inter:wght@400;500;600&display=swap");')
    return "\n".join(rules)

# ───────────────────────────── slide CSS ─────────────────────────────
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#000}
body{font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;font-kerning:normal}
.s{position:relative;width:1080px;height:1350px;padding:118px 104px 156px;display:flex;flex-direction:column;overflow:hidden}
.dark{background:%(green)s;color:%(light)s}
.inkbg{background:%(ink)s;color:%(light)s}
.lightbg{background:%(paper)s;color:%(ink)s}
.brassbg{background:%(brass)s;color:%(ink)s}
.serif{font-family:"Crimson Text",Georgia,serif}
.anton{font-family:Anton,Impact,sans-serif;font-weight:400}
.foot{position:absolute;left:104px;right:104px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font:500 26px/1 Inter,sans-serif}
.mark{display:flex;align-items:center;gap:14px}
.mark .lg{height:38px;width:auto;flex:none;display:block}.lgdot{fill:%(brass)s}.dark .lg,.inkbg .lg{color:%(light)s}.lightbg .lg{color:%(green)s}.brassbg .lg{color:%(ink)s}.brassbg .lgdot{fill:%(ink)s}
.dark .foot,.inkbg .foot{color:%(sage)s}
.lightbg .foot{color:%(graphite)s}
.brassbg .foot{color:rgba(15,23,19,.72)}
.count{font-variant-numeric:tabular-nums}

/* founder stories */
.yr{position:absolute;right:-18px;top:150px;font:400 430px/0.8 Anton,sans-serif;color:rgba(238,239,231,.06);letter-spacing:-.01em;pointer-events:none}
.kicker{font:500 28px/1.2 Inter,sans-serif;color:%(sage)s}
.hook{font:600 108px/1.03 "Crimson Text",serif;letter-spacing:-.012em;margin-top:auto;margin-bottom:36px;max-width:860px;position:relative}
.center{justify-content:center}
.fig{font:400 230px/0.86 Anton,sans-serif;color:%(brass)s;margin-bottom:54px;white-space:nowrap}
.body{font:400 64px/1.22 "Crimson Text",serif;max-width:872px}
.end{font:italic 600 76px/1.12 "Crimson Text",serif;max-width:860px}
.cta{font:500 30px/1.3 Inter,sans-serif;color:%(sage)s;margin-top:60px}

/* data */
.dtitle{font:600 104px/1.0 "Crimson Text",serif;letter-spacing:-.012em;max-width:860px}
.stats{margin-top:auto;display:flex;flex-direction:column;gap:30px}
.stat{display:flex;align-items:baseline;gap:34px}
.stat .num{font:400 250px/0.84 Anton,sans-serif;color:%(green)s;min-width:200px}
.stat .lbl{font:500 34px/1.25 Inter,sans-serif;color:%(graphite)s;max-width:580px}
.dh{font:600 76px/1.02 "Crimson Text",serif;letter-spacing:-.01em}
.dsub{font:400 30px/1.3 Inter,sans-serif;color:%(graphite)s;margin-top:14px}
.rows{margin-top:54px;display:flex;flex-direction:column;gap:22px}
.row{display:grid;grid-template-columns:230px 170px 1fr 74px;align-items:center;column-gap:20px}
.row .n{font:600 34px/1 Inter,sans-serif}
.row .sp{font:400 27px/1 Inter,sans-serif;color:%(graphite)s;font-variant-numeric:tabular-nums}
.row .track{height:26px;position:relative}
.row .bar{position:absolute;left:0;top:0;bottom:0;background:%(green)s}
.row .v{font:400 52px/1 Anton,sans-serif;color:%(green)s;text-align:right}
.src{position:absolute;left:104px;right:104px;bottom:128px;font:400 23px/1.35 Inter,sans-serif;color:%(graphite)s}
.plist{margin-top:50px;display:flex;flex-direction:column;gap:26px}
.prow{display:grid;grid-template-columns:250px 1fr;column-gap:26px;align-items:baseline}
.prow .n{font:600 50px/1.05 "Crimson Text",serif}
.prow .w{font:400 31px/1.3 Inter,sans-serif;color:%(graphite)s}
.alist{margin-top:44px;display:flex;flex-direction:column;gap:17px}
.arow{display:grid;grid-template-columns:96px 66px 1fr;column-gap:22px;align-items:center}
.arow .a{font:400 64px/1 Anton,sans-serif;color:%(green)s;text-align:right}
.mono{width:62px;height:62px;border-radius:50%%;border:2px solid %(green)s;display:flex;align-items:center;justify-content:center;font:600 25px/1 "Crimson Text",serif;color:%(green)s;letter-spacing:.02em}
.arow .who{display:flex;flex-direction:column;gap:6px}
.arow .who b{font:600 32px/1.05 Inter,sans-serif}
.arow .who span{font:400 25px/1.1 Inter,sans-serif;color:%(graphite)s}
.cards{margin-top:46px;display:flex;flex-direction:column;gap:40px}
.card{display:grid;grid-template-columns:300px 1fr;column-gap:36px;align-items:center}
.card .big{font:400 300px/0.82 Anton,sans-serif;color:%(green)s;text-align:right}
.card .unit{font:600 34px/1.2 Inter,sans-serif}
.card .deal{font:400 28px/1.3 Inter,sans-serif;color:%(graphite)s;margin-top:8px}
.card .price{font:600 52px/1.05 "Crimson Text",serif;margin-top:18px}
.card .per{font:600 32px/1.2 Inter,sans-serif;color:%(green)s;margin-top:10px}
.ntext{font:600 84px/1.08 "Crimson Text",serif;letter-spacing:-.01em;max-width:872px}
.nsmall{font:500 32px/1.35 Inter,sans-serif;color:%(graphite)s;margin-top:56px;max-width:820px}

/* hiring */
.hh{font:600 100px/1.02 "Crimson Text",serif;letter-spacing:-.012em;max-width:872px}
.role{font:600 38px/1.25 Inter,sans-serif;margin-top:56px;max-width:872px}
.loc{font:400 32px/1.3 Inter,sans-serif;margin-top:12px}
.sal{font:400 196px/0.9 Anton,sans-serif;margin-top:auto;white-space:nowrap}
.ssub{font:500 34px/1.3 Inter,sans-serif;margin-top:22px}
.asof{font:400 24px/1.35 Inter,sans-serif;color:rgba(15,23,19,.75);margin-top:34px;max-width:800px}

/* explainers */
.art{width:872px;height:520px;margin-bottom:auto}
.xh{font:400 148px/0.95 Anton,sans-serif;text-transform:uppercase;letter-spacing:.004em;max-width:872px}
.xsub{font:italic 400 48px/1.2 "Crimson Text",serif;color:%(sage)s;margin-top:28px}
.xtext{font:400 66px/1.22 "Crimson Text",serif;max-width:872px}
.diagram{width:872px;height:820px}
.dcap{font:italic 400 46px/1.25 "Crimson Text",serif;color:%(sage)s;margin-top:24px;max-width:872px}

/* history */
.hlabel{font:500 30px/1.2 Inter,sans-serif;color:%(graphite)s}
.hbig{font:400 320px/0.84 Anton,sans-serif;color:%(green)s;margin-top:40px;white-space:nowrap}
.ht{font:600 88px/1.04 "Crimson Text",serif;letter-spacing:-.01em;margin-top:30px;max-width:872px}
.hart{width:872px;height:340px;margin-top:auto}
.facts{display:flex;flex-direction:column;gap:40px}
.facts p{font:400 54px/1.24 "Crimson Text",serif;max-width:872px}
""" % C

FIT_JS = """
(() => {
  // shrink single-line elements to fit their width, multi-line ones to a max height
  document.querySelectorAll('[data-fitw]').forEach(el => {
    let s = parseFloat(getComputedStyle(el).fontSize);
    const max = el.parentElement.clientWidth - (parseFloat(getComputedStyle(el.parentElement).paddingLeft)||0) - (parseFloat(getComputedStyle(el.parentElement).paddingRight)||0);
    while (el.scrollWidth > Math.min(max, 872) && s > 40) { s -= 2; el.style.fontSize = s + 'px'; }
  });
  document.querySelectorAll('[data-fith]').forEach(el => {
    const mh = parseFloat(el.dataset.fith);
    let s = parseFloat(getComputedStyle(el).fontSize);
    while (el.scrollHeight > mh && s > 30) { s -= 2; el.style.fontSize = s + 'px'; }
  });
})();
"""

def esc(t):
    return html.escape(t, quote=False)

def foot(i, n, show_count=True):
    count = f'<span class="count">{i} / {n}</span>' if (show_count and n > 1) else ""
    return f'<div class="foot"><span class="mark">{logo_svg()}<span>{esc(BRAND_HANDLE)}</span></span>{count}</div>'

# ───────────────────────────── SVG art ─────────────────────────────
def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'

def txt(x, y, s, size=26, fill=None, weight=500, anchor="start", family="Inter", style="normal"):
    fill = fill or C["sage"]
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'font-style="{style}" fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>')

def art_jevons():
    b = []
    b.append(f'<line x1="0" y1="470" x2="872" y2="470" stroke="{C["line"]}" stroke-width="3"/>')
    # falling cost line
    b.append(f'<path d="M20 70 C 260 120, 520 330, 852 430" fill="none" stroke="{C["sage"]}" stroke-width="6" stroke-dasharray="2 16" stroke-linecap="round"/>')
    # rising total use
    b.append(f'<path d="M20 440 C 330 430, 560 330, 852 60" fill="none" stroke="{C["brass"]}" stroke-width="10" stroke-linecap="round"/>')
    b.append(txt(24, 46, "Cost per use", 30, C["sage"], 500))
    b.append(txt(806, 40, "Total use", 30, C["brass"], 600, "end"))
    b.append(txt(852, 510, "Illustrative", 22, C["sage"], 400, "end"))
    return svg(872, 520, "".join(b))

def art_chess():
    # a search tree fanning out, the signature of brute-force search
    b = []
    rootx, rooty = 436, 490
    levels = [(1, 490), (3, 360), (9, 235), (27, 110)]
    prev = [(rootx, rooty)]
    for li in range(1, len(levels)):
        n, y = levels[li]
        xs = [24 + (824 * (k + 0.5) / n) for k in range(n)]
        cur = []
        for k, x in enumerate(xs):
            px, py = prev[k // 3]
            op = 0.95 if li < 3 else 0.7
            b.append(f'<line x1="{px:.1f}" y1="{py}" x2="{x:.1f}" y2="{y}" stroke="{C["brass"]}" stroke-opacity="{op}" stroke-width="{5 - li}"/>')
            cur.append((x, y))
        prev = cur
    for li, (n, y) in enumerate(levels):
        xs = [rootx] if n == 1 else [24 + (824 * (k + 0.5) / n) for k in range(n)]
        r = [16, 12, 9, 6][li]
        for x in xs:
            b.append(f'<circle cx="{x:.1f}" cy="{y}" r="{r}" fill="{C["light"] if li == 0 else C["brass"]}"/>')
    return svg(872, 520, "".join(b))

def art_org():
    b = []
    box = lambda x, y, w, h: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" stroke="{C["brass"]}" stroke-width="5"/>'
    b.append(box(356, 40, 160, 96))
    xs = [60, 356, 652]
    for x in xs:
        b.append(f'<path d="M436 136 V 220 H {x+80} V 290" fill="none" stroke="{C["brass"]}" stroke-width="4"/>')
        b.append(box(x, 290, 160, 96))
        b.append(f'<line x1="{x+80}" y1="386" x2="{x+80}" y2="440" stroke="{C["sage"]}" stroke-width="3" stroke-dasharray="3 9" stroke-linecap="round"/>')
        b.append(f'<rect x="{x+30}" y="440" width="100" height="56" rx="4" fill="{C["brass"]}" fill-opacity=".85"/>')
    return svg(872, 520, "".join(b))

def complete_graph(cx, cy, r, n, stroke, node_fill, sw=2.2, op=0.6, nr=9):
    pts = [(cx + r * math.cos(2 * math.pi * k / n - math.pi / 2), cy + r * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            out.append(f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{stroke}" stroke-opacity="{op}" stroke-width="{sw}"/>')
    for x, y in pts:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{nr}" fill="{node_fill}"/>')
    return "".join(out)

def art_network():
    return svg(872, 520, complete_graph(436, 262, 238, 12, C["brass"], C["light"], 2.2, .55, 10))

def diag_jevons_chain():
    steps = ["Engines get more efficient", "Power gets cheaper", "People find new uses", "Total coal use rises"]
    b = []
    for i, s in enumerate(steps):
        y = 20 + i * 200
        last = i == 3
        b.append(f'<rect x="0" y="{y}" width="872" height="140" rx="10" fill="{C["brass"] if last else "none"}" stroke="{C["brass"]}" stroke-width="4"/>')
        b.append(txt(48, y + 88, str(i + 1), 54, C["ink"] if last else C["brass"], 400, "start", "Anton"))
        b.append(txt(118, y + 86, s, 42, C["ink"] if last else C["light"], 600))
        if not last:
            b.append(f'<path d="M436 {y+148} V {y+190}" stroke="{C["sage"]}" stroke-width="4"/>')
            b.append(f'<path d="M422 {y+176} L436 {y+194} L450 {y+176}" fill="none" stroke="{C["sage"]}" stroke-width="4"/>')
    return svg(872, 820, "".join(b))

def diag_bitter():
    b = []
    b.append(f'<line x1="70" y1="40" x2="70" y2="690" stroke="{C["line"]}" stroke-width="3"/>')
    b.append(f'<line x1="70" y1="690" x2="860" y2="690" stroke="{C["line"]}" stroke-width="3"/>')
    b.append(f'<text x="40" y="365" font-family="Inter" font-size="28" font-weight="500" fill="{C["sage"]}" text-anchor="middle" transform="rotate(-90 40 365)">Performance</text>')
    b.append(txt(860, 736, "Computing power available", 28, C["sage"], 500, "end"))
    b.append(f'<path d="M80 600 C 220 380, 330 320, 860 300" fill="none" stroke="{C["sage"]}" stroke-width="7" stroke-dasharray="2 16" stroke-linecap="round"/>')
    b.append(f'<path d="M80 670 C 420 650, 560 420, 860 70" fill="none" stroke="{C["brass"]}" stroke-width="10" stroke-linecap="round"/>')
    # legend, top-left, clear of both curves
    b.append(f'<line x1="110" y1="70" x2="170" y2="70" stroke="{C["brass"]}" stroke-width="10" stroke-linecap="round"/>')
    b.append(txt(190, 80, "Search and learning at scale", 30, C["brass"], 600))
    b.append(f'<line x1="110" y1="124" x2="170" y2="124" stroke="{C["sage"]}" stroke-width="7" stroke-dasharray="2 16" stroke-linecap="round"/>')
    b.append(txt(190, 134, "Built-in human knowledge", 30, C["sage"], 600))
    b.append(txt(860, 800, "Illustrative sketch, not data", 22, C["sage"], 400, "end"))
    return svg(872, 820, "".join(b))

def diag_conway():
    b = []
    colx = [90, 482]
    heads = ["Teams", "System"]
    labels = [["Team A", "Team B", "Team C"], ["Part A", "Part B", "Part C"]]
    ys = [120, 360, 600]
    for ci, x in enumerate(colx):
        b.append(txt(x + 150, 58, heads[ci], 34, C["sage"], 600, "middle"))
        for k, y in enumerate(ys):
            filled = ci == 1
            b.append(f'<rect x="{x}" y="{y}" width="300" height="110" rx="8" fill="{C["brass"] if filled else "none"}" stroke="{C["brass"]}" stroke-width="4"/>')
            b.append(txt(x + 150, y + 68, labels[ci][k], 36, C["ink"] if filled else C["light"], 600, "middle"))
        for a, bb in [(0, 1), (1, 2)]:
            b.append(f'<line x1="{x+150}" y1="{ys[a]+110}" x2="{x+150}" y2="{ys[bb]}" stroke="{C["light"]}" stroke-width="5"/>')
        # A and C don't talk, so A and C don't connect: dashed arc on the outer side of each column
        edge = x if ci == 0 else x + 300
        out = -62 if ci == 0 else 62
        b.append(f'<path d="M{edge} {ys[0]+55} C {edge+out} {ys[0]+55}, {edge+out} {ys[2]+55}, {edge} {ys[2]+55}" fill="none" stroke="{C["sage"]}" stroke-width="3" stroke-dasharray="4 12" stroke-linecap="round"/>')
        b.append(txt(edge + out * 0.78, ys[1] + 70, "×", 44, C["sage"], 500, "middle"))
    b.append(f'<path d="M396 415 H 470" stroke="{C["sage"]}" stroke-width="4"/>')
    b.append(f'<path d="M458 403 L472 415 L458 427" fill="none" stroke="{C["sage"]}" stroke-width="4"/>')
    return svg(872, 820, "".join(b))

def diag_metcalfe():
    b = []
    specs = [(2, 130, 300, 70, "2 users", "1 link"), (5, 436, 300, 120, "5 users", "10 links"), (12, 742, 300, 125, "12 users", "66 links")]
    for n, cx, cy, r, u, l in specs:
        b.append(complete_graph(cx, cy, r, n, C["brass"], C["light"], 2.6 if n < 12 else 1.8, .75 if n < 12 else .55, 10 if n < 12 else 8))
        b.append(txt(cx, 520, l.split()[0], 120, C["brass"], 400, "middle", "Anton"))
        b.append(txt(cx, 572, l.split()[1], 32, C["light"], 600, "middle"))
        b.append(txt(cx, 616, u, 30, C["sage"], 500, "middle"))
    b.append(txt(436, 740, "connections = n × (n − 1) ÷ 2", 34, C["sage"], 500, "middle"))
    return svg(872, 820, "".join(b))

def art_sms():
    b = []
    b.append(f'<path d="M40 40 H 832 Q 860 40 860 68 V 232 Q 860 260 832 260 H 170 L 96 322 L 112 260 H 68 Q 40 260 40 232 V 68 Q 40 40 68 40 Z" fill="{C["green"]}"/>')
    b.append(txt(450, 178, "Merry Christmas", 84, C["light"], 600, "middle", "Crimson Text"))
    return svg(872, 340, "".join(b))

def art_ipo():
    b = []
    maxw = 860
    for i, (lbl, val, col) in enumerate([("IPO price", 22, C["graphite"]), ("First-day close, about", 29, C["green"])]):
        y = 40 + i * 150
        w = maxw * val / 29
        b.append(f'<rect x="0" y="{y}" width="{w:.0f}" height="64" fill="{col}"/>')
        b.append(txt(0, y + 108, f"{lbl} ${val}", 32, C["ink"], 600))
    return svg(872, 340, "".join(b))

def art_flight():
    b = []
    maxw = 860
    for i, (lbl, ft) in enumerate([("Flight 1, Orville: 120 ft in 12 s", 120), ("Flight 4, Wilbur: 852 ft in 59 s", 852)]):
        y = 40 + i * 150
        w = maxw * ft / 852
        b.append(f'<rect x="0" y="{y}" width="{w:.0f}" height="64" fill="{C["green"] if i else C["brass"]}"/>')
        b.append(txt(0, y + 108, lbl, 32, C["ink"], 600))
    b.append(txt(872, 330, "Bars drawn to scale", 22, C["graphite"], 400, "end"))
    return svg(872, 340, "".join(b))

def art_transistor():
    b = []
    b.append(f'<rect x="250" y="230" width="372" height="80" fill="{C["graphite"]}"/>')
    b.append(f'<path d="M300 40 H 572 L 436 226 Z" fill="none" stroke="{C["green"]}" stroke-width="6" stroke-linejoin="round"/>')
    b.append(f'<path d="M300 40 L 433 222" stroke="{C["brass"]}" stroke-width="12" stroke-linecap="round"/>')
    b.append(f'<path d="M572 40 L 439 222" stroke="{C["brass"]}" stroke-width="12" stroke-linecap="round"/>')
    b.append(f'<line x1="640" y1="80" x2="520" y2="110" stroke="{C["graphite"]}" stroke-width="2"/>')
    b.append(txt(650, 88, "Plastic wedge", 28, C["ink"], 600))
    b.append(f'<line x1="230" y1="150" x2="355" y2="128" stroke="{C["graphite"]}" stroke-width="2"/>')
    b.append(txt(220, 158, "Gold contacts", 28, C["ink"], 600, "end"))
    b.append(f'<line x1="640" y1="270" x2="622" y2="270" stroke="{C["graphite"]}" stroke-width="2"/>')
    b.append(txt(650, 280, "Germanium", 28, C["ink"], 600))
    return svg(872, 340, "".join(b))

ART = {"jevons": art_jevons, "chess": art_chess, "org": art_org, "network": art_network,
       "sms": art_sms, "ipo": art_ipo, "flight": art_flight, "transistor": art_transistor}
DIAGRAM = {"jevons_chain": diag_jevons_chain, "bitter_curves": diag_bitter,
           "conway": diag_conway, "metcalfe": diag_metcalfe}

# ───────────────────────────── templates ─────────────────────────────
def initials(name):
    parts = [p for p in name.replace("’", "").split() if p[0].isalpha()]
    return (parts[0][0] + parts[-1][0]).upper()

def slide_html(post, slide, i, n):
    t = slide["tpl"]
    if t == "story_cover":
        inner = (f'<div class="yr">{esc(post.get("year", ""))}</div>'
                 f'<div class="kicker">Founder story</div>'
                 f'<h1 class="hook" data-fith="760">{esc(slide["headline"])}</h1>')
        cls = "dark"
    elif t == "story":
        fig = f'<div class="fig" data-fitw>{esc(slide["fig"])}</div>' if slide.get("fig") else ""
        inner = f'{fig}<p class="body" data-fith="{620 if fig else 900}">{esc(slide["text"])}</p>'
        cls = "dark center"
    elif t == "story_end":
        inner = f'<p class="end" data-fith="640">{esc(slide["text"])}</p><p class="cta">Follow {esc(BRAND_HANDLE)} for one true startup story a day.</p>'
        cls = "dark center"
    elif t == "data_cover":
        stats = "".join(f'<div class="stat"><span class="num">{esc(a)}</span><span class="lbl">{esc(b)}</span></div>' for a, b in slide["stats"])
        inner = f'<h1 class="dtitle" data-fith="440">{esc(slide["title"])}</h1><div class="stats">{stats}</div>'
        cls = "lightbg"
    elif t == "bars":
        mx = max(r[2] for r in slide["rows"])
        rows = "".join(
            f'<div class="row"><span class="n">{esc(a)}</span><span class="sp">{esc(b)}</span>'
            f'<span class="track"><span class="bar" style="width:{100*v/mx:.1f}%"></span></span><span class="v">{v}</span></div>'
            for a, b, v in slide["rows"])
        inner = (f'<h2 class="dh">{esc(slide["title"])}</h2><p class="dsub">{esc(slide["sub"])}</p>'
                 f'<div class="rows">{rows}</div><p class="src">{esc(slide["foot"])}</p>')
        cls = "lightbg"
    elif t == "pivots":
        rows = "".join(f'<div class="prow"><span class="n">{esc(a)}</span><span class="w">{esc(b)}</span></div>' for a, b in slide["rows"])
        inner = f'<h2 class="dh">{esc(slide["title"])}</h2><div class="plist">{rows}</div><p class="src">{esc(slide["foot"])}</p>'
        cls = "lightbg"
    elif t == "ages":
        rows = "".join(
            f'<div class="arow"><span class="a">{esc(a)}</span><span class="mono">{initials(b)}</span>'
            f'<span class="who"><b>{esc(b)}</b><span>{esc(c)}</span></span></div>' for a, b, c in slide["rows"])
        inner = f'<h2 class="dh">{esc(slide["title"])}</h2><div class="alist">{rows}</div><p class="src">{esc(slide["foot"])}</p>'
        cls = "lightbg"
    elif t == "compare":
        cards = "".join(
            f'<div class="card"><div class="big">{esc(c["big"])}</div><div><div class="unit">{esc(c["unit"])}</div>'
            f'<div class="deal">{esc(c["deal"])}</div><div class="price">{esc(c["price"])}</div><div class="per">{esc(c["per"])}</div></div></div>'
            for c in slide["cards"])
        inner = f'<h2 class="dh">{esc(slide["title"])}</h2><div class="cards">{cards}</div><p class="src">{esc(slide["foot"])}</p>'
        cls = "lightbg"
    elif t == "note":
        inner = f'<p class="ntext" data-fith="720">{esc(slide["text"])}</p><p class="nsmall">{esc(slide["small"])}</p>'
        cls = "lightbg center"
    elif t == "hire":
        loc = f'<div class="loc">{esc(slide["loc"])}</div>' if slide.get("loc") else ""
        inner = (f'<h1 class="hh" data-fith="420">{esc(slide["headline"])}</h1><div class="role">{esc(slide["role"])}</div>{loc}'
                 f'<div class="sal" data-fitw>{esc(slide["salary"])}</div><div class="ssub">{esc(slide["sub"])}</div>'
                 f'<div class="asof">{esc(slide["asof"])}</div>')
        cls = "brassbg"
    elif t == "ex_cover":
        inner = (f'<div class="art">{ART[slide["art"]]()}</div>'
                 f'<h1 class="xh" data-fith="440">{esc(slide["headline"])}</h1><p class="xsub">{esc(slide["sub"])}</p>')
        cls = "inkbg"
    elif t == "ex_text":
        inner = f'<p class="xtext" data-fith="900">{esc(slide["text"])}</p>'
        cls = "inkbg center"
    elif t == "ex_diagram":
        inner = f'<div class="diagram">{DIAGRAM[slide["diagram"]]()}</div><p class="dcap">{esc(slide["caption"])}</p>'
        cls = "inkbg center"
    elif t == "ex_end":
        inner = f'<p class="end" data-fith="640">{esc(slide["text"])}</p><p class="cta">Follow {esc(BRAND_HANDLE)} for one true startup story a day.</p>'
        cls = "inkbg center"
    elif t == "hist_cover":
        inner = (f'<div class="hlabel">{esc(slide["label"])}</div><div class="hbig" data-fitw>{esc(slide["big"])}</div>'
                 f'<h1 class="ht" data-fith="200">{esc(slide["title"])}</h1><div class="hart">{ART[slide["art"]]()}</div>')
        cls = "lightbg"
    elif t == "hist_facts":
        inner = '<div class="facts">' + "".join(f"<p>{esc(f)}</p>" for f in slide["facts"]) + "</div>"
        cls = "lightbg center"
    else:
        raise ValueError(t)
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{font_css()}{CSS}</style></head>'
            f'<body><div class="s {cls}">{inner}{foot(i, n)}</div><script>{FIT_JS}</script></body></html>')

# ───────────────────────────── outputs ─────────────────────────────
def post_dir(p):
    return f"posts/{p['id']}"

def render_all(out_root):
    from playwright.sync_api import sync_playwright
    out_root = Path(out_root)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for p in POSTS:
            d = out_root / post_dir(p)
            d.mkdir(parents=True, exist_ok=True)
            n = len(p["slides"])
            files = []
            for i, s in enumerate(p["slides"], 1):
                page.set_content(slide_html(p, s, i, n), wait_until="load")
                page.evaluate("document.fonts.ready.then(() => true)")
                page.evaluate(FIT_JS)
                f = d / f"{i:02d}.jpg"
                page.screenshot(path=str(f), type="jpeg", quality=92, clip={"x": 0, "y": 0, "width": W, "height": H})
                files.append(f"{post_dir(p)}/{f.name}")
            p["_files"] = files
            print(f"  {p['id']}: {n} slide(s)")
        browser.close()

def iso(p):
    return f"{p['date']}T{p['time']}:00{TZ_OFFSET}"

def write_schedule(out_root):
    cols = ["post_id", "publish_at", "day", "time_et", "pillar", "title", "format", "images", "caption", "alt_text", "sources", "notes"]
    import datetime as dt
    with open(Path(out_root) / "schedule.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for p in POSTS:
            d = dt.date.fromisoformat(p["date"])
            w.writerow({
                "post_id": p["id"], "publish_at": iso(p), "day": d.strftime("%a %b %-d"), "time_et": p["time"],
                "pillar": p["pillar"], "title": p["title"],
                "format": "carousel" if len(p["slides"]) > 1 else "single image",
                "images": ";".join(p["_files"]), "caption": p["caption"], "alt_text": p["alt"],
                "sources": " ; ".join(f"{a} | {b}" for a, b in p["sources"]), "notes": p["notes"],
            })

def write_captions(out_root):
    import datetime as dt
    lines = ["# Captions, in posting order", "",
             "Times are US Eastern. Images for each post are in posts/<post id>/, in slide order.", ""]
    for p in POSTS:
        d = dt.date.fromisoformat(p["date"])
        lines += [f"## {d.strftime('%a %b %-d')}, {p['time']} ET · {p['pillar']}", f"**{p['title']}**  ", f"Folder: `{post_dir(p)}/` ({len(p['slides'])} image{'s' if len(p['slides']) > 1 else ''})", "",
                  "```", p["caption"], "```", "", f"Alt text: {p['alt']}", "",
                  "Sources:"] + [f"- {a}: {b}" for a, b in p["sources"]] + ([f"", f"Note: {p['notes']}"] if p["notes"] else []) + ["", "---", ""]
    (Path(out_root) / "captions.md").write_text("\n".join(lines), encoding="utf-8")

def thumb_uri(path, width=600, quality=80):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    im = im.resize((width, int(width * H / W)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def write_review(out_root, review_path):
    import datetime as dt
    data = []
    for p in POSTS:
        d = dt.date.fromisoformat(p["date"])
        data.append({
            "id": p["id"], "date": p["date"], "dow": d.strftime("%a"), "label": d.strftime("%b %-d"),
            "time": p["time"], "pillar": p["pillar"], "title": p["title"],
            "slides": [thumb_uri(Path(out_root) / f) for f in p["_files"]],
            "caption": p["caption"], "alt": p["alt"], "sources": p["sources"], "notes": p["notes"],
        })
    tpl = (HERE / "review_template.html").read_text(encoding="utf-8")
    out = tpl.replace("/*__DATA__*/[]", json.dumps(data, ensure_ascii=False)).replace("__HANDLE__", esc(BRAND_HANDLE))
    Path(review_path).write_text(out, encoding="utf-8")
    print(f"  review page: {review_path} ({len(out)/1e6:.1f} MB)")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT))
    ap.add_argument("--review", default=None)
    a = ap.parse_args()
    render_all(a.out)
    write_schedule(a.out)
    write_captions(a.out)
    if a.review:
        write_review(a.out, a.review)
