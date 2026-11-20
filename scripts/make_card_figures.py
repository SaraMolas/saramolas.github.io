"""Generate the simplified SVG figures used on the homepage research cards.

Usage:  python3 scripts/make_card_figures.py _includes/card-figures

The figures deliberately use their own bold palette (yellow / red / blue)
so the research cards stand out from the site's terracotta-and-cream design.
"""
import math
import random
import sys

OUT = sys.argv[1]

# Neutrals (shared with the site so figures sit nicely on the cards)
INK = "#2A231F"; MUTED = "#6B5F55"; BORDER = "#E3D8C6"; SURF = "#FBF7F0"; GREY = "#B9B2A8"; NEURON_OFF = "#E4DED5"

# Bold figure palette
YELLOW = "#F5B700"; YELLOW_D = "#B88600"; YELLOW_T = "#FFF1C2"
TEAL = "#00A88F"; TEAL_D = "#00775F"; TEAL_T = "#CDEFE8"
RED = "#E63946"; RED_D = "#B5172B"; RED_T = "#FCDDE0"
BLUE = "#2F6BFF"; BLUE_D = "#1C46B8"; BLUE_L = "#9DB6F7"; BLUE_T = "#DCE6FF"

SERIF = 'font-family="Instrument Serif, Georgia, serif"'
SANS = 'font-family="Inter, -apple-system, Helvetica, Arial, sans-serif"'
BOLD = 'font-weight="600"'
CAPS = 'font-weight="600" letter-spacing="1.2"'


def svg(name, label, body):
    with open(f"{OUT}/{name}.svg", "w") as f:
        f.write(f'<svg class="card-figure" viewBox="0 0 360 225" xmlns="http://www.w3.org/2000/svg" '
                f'role="img" aria-label="{label}">\n{body}</svg>\n')


def text(x, y, s, size=11, fill=MUTED, anchor="middle", font=SANS, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {font} {extra}>{s}</text>\n'


def arrowhead(x, y, angle_deg, color, size=5.5, width=1.4):
    a = math.radians(angle_deg)
    hx, hy = x - size * math.cos(a), y - size * math.sin(a)
    l = (hx - 3.5 * math.sin(a), hy + 3.5 * math.cos(a))
    r = (hx + 3.5 * math.sin(a), hy - 3.5 * math.cos(a))
    return f'<path d="M{l[0]:.1f} {l[1]:.1f} L{x} {y} L{r[0]:.1f} {r[1]:.1f}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"/>'


def arrow(x1, y1, x2, y2, color=MUTED, width=1.4):
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>'
            + arrowhead(x2, y2, ang, color, width=width) + "\n")


def noise(x, y, size, n=14, seed=3):
    random.seed(seed)
    c = size / n
    s = ""
    for i in range(n):
        for j in range(n):
            g = random.randint(55, 235)
            s += f'<rect x="{x+i*c:.2f}" y="{y+j*c:.2f}" width="{c+0.2:.2f}" height="{c+0.2:.2f}" fill="rgb({g},{g},{g})"/>'
    return s + "\n"


def tile(x, y, size, shape, color):
    """Dark image tile with a coloured shape."""
    s = f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="2" fill="{INK}"/>'
    cx, cy, r = x + size / 2, y + size / 2, size * 0.27
    if shape == "triangle":
        s += f'<path d="M{cx} {cy-r*1.1:.1f} L{cx-r*1.15:.1f} {cy+r*0.85:.1f} L{cx+r*1.15:.1f} {cy+r*0.85:.1f} Z" fill="{color}"/>'
    elif shape == "circle":
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
    else:
        s += f'<rect x="{cx-r:.1f}" y="{cy-r:.1f}" width="{2*r:.1f}" height="{2*r:.1f}" fill="{color}"/>'
    return s + "\n"


# ---------------- Diffusion: noise -> U-Net -> new image ----------------
def diffusion():
    b = ""
    # Trained on / never seen strip
    b += text(16, 19, "TRAINED ON", 9.5, MUTED, "start", extra=CAPS)
    for k, (shape, col) in enumerate([("triangle", RED), ("circle", BLUE), ("square", RED), ("square", BLUE)]):
        b += tile(16 + k * 29, 26, 23, shape, col)
    b += text(344, 19, "NEVER SEEN", 9.5, RED_D, "end", extra=CAPS)
    b += tile(320, 26, 23, "triangle", BLUE)
    b += f'<rect x="317" y="23" width="29" height="29" rx="3" fill="none" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 2"/>\n'

    cy = 124
    # Contiguous U-Net blocks on one level (encoder -> bottleneck -> decoder)
    x0, w, gap = 94, 22, 10
    heights = [58, 46, 34, 34, 46, 58]
    xs = [x0 + i * (w + gap) for i in range(6)]
    # Nested skip connections over the top: 1->6 outermost, 2->5, 3->4 innermost
    for i, level in [(0, 68), (1, 80), (2, 92)]:
        j = 5 - i
        xa, xb = xs[i] + w / 2, xs[j] + w / 2
        ya, yb = cy - heights[i] / 2, cy - heights[j] / 2
        b += (f'<path d="M{xa} {ya} V{level+5} Q{xa} {level} {xa+5} {level} H{xb-5} Q{xb} {level} {xb} {level+5} V{yb-1}" '
              f'fill="none" stroke="{YELLOW_D}" stroke-width="1.4"/>' + arrowhead(xb, yb - 1, 90, YELLOW_D) + "\n")
    for k, (x, h) in enumerate(zip(xs, heights)):
        b += f'<rect x="{x}" y="{cy-h/2}" width="{w}" height="{h}" rx="2" fill="{YELLOW}" stroke="{YELLOW_D}" stroke-width="1.4"/>'
        if k < 5:
            b += arrow(x + w + 1, cy, x + w + gap - 1, cy, YELLOW_D, 1.3)
    b += "\n" + text(186, 172, "U-Net", 12, INK, extra=BOLD)

    b += noise(34, cy - 24, 48)
    b += text(58, 166, "noise")
    b += arrow(83, cy, 92, cy)
    b += arrow(282, cy, 290, cy)
    b += tile(292, cy - 24, 48, "triangle", BLUE)
    b += text(316, 166, "new image", 11, INK, extra=BOLD)

    b += f'<line x1="16" y1="186" x2="344" y2="186" stroke="{BORDER}" stroke-width="1"/>\n'
    b += text(180, 208, "From pure noise to an image it has never seen", 12.5, INK)
    svg("diffusion", "Diagram: trained on some shape and colour combinations, a U-Net turns pure noise into a combination it has never seen.", b)


# ---------------- SAE on biological neurons ----------------
def star_neuron(x, y, fill, stroke, r=5, seed=0, branches=5, length=(11, 17)):
    """Biological-looking neuron: round soma, curved tapering dendrites that fork, and a thin axon."""
    random.seed(seed)
    s = ""
    base = random.uniform(0, 2 * math.pi)
    for k in range(branches):
        a = base + k * 2 * math.pi / branches + random.uniform(-0.35, 0.35)
        L = r + random.uniform(*length)
        bend = random.uniform(-0.35, 0.35)
        b1 = (x + r * math.cos(a - 0.32), y + r * math.sin(a - 0.32))
        b2 = (x + r * math.cos(a + 0.32), y + r * math.sin(a + 0.32))
        mid = (x + (r + L) / 2 * math.cos(a + bend * 0.5), y + (r + L) / 2 * math.sin(a + bend * 0.5))
        tip = (x + L * math.cos(a + bend), y + L * math.sin(a + bend))
        # tapered dendrite trunk
        s += (f'<path d="M{b1[0]:.1f} {b1[1]:.1f} Q{mid[0]:.1f} {mid[1]:.1f} {tip[0]:.1f} {tip[1]:.1f} '
              f'Q{mid[0]:.1f} {mid[1]:.1f} {b2[0]:.1f} {b2[1]:.1f} Z" fill="{fill}" stroke="{stroke}" stroke-width="0.9" stroke-linejoin="round"/>')
        # fork near the tip
        for side in (-1, 1):
            fa = a + bend + side * random.uniform(0.45, 0.8)
            fl = random.uniform(4, 7)
            s += (f'<line x1="{tip[0]:.1f}" y1="{tip[1]:.1f}" x2="{tip[0]+fl*math.cos(fa):.1f}" y2="{tip[1]+fl*math.sin(fa):.1f}" '
                  f'stroke="{stroke}" stroke-width="1" stroke-linecap="round"/>')
    # axon: one long thin process
    aa = base + math.pi / branches
    ax = (x + (r + 24) * math.cos(aa), y + (r + 24) * math.sin(aa))
    s += (f'<path d="M{x + r*math.cos(aa):.1f} {y + r*math.sin(aa):.1f} Q{x + (r+12)*math.cos(aa+0.25):.1f} {y + (r+12)*math.sin(aa+0.25):.1f} {ax[0]:.1f} {ax[1]:.1f}" '
          f'fill="none" stroke="{stroke}" stroke-width="1" stroke-linecap="round"/>')
    s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>'
    return s + "\n"


def neuron(x, y, active, seed=0):
    if active:
        return (f'<circle cx="{x}" cy="{y}" r="17" fill="{RED}" opacity="0.16"/>'
                + star_neuron(x, y, RED, RED_D, seed=seed))
    return star_neuron(x, y, NEURON_OFF, GREY, seed=seed)


def pill(x, y, label):
    w = len(label) * 6.6 + 16
    return (f'<rect x="{x}" y="{y-10}" width="{w:.1f}" height="20" rx="10" fill="{RED_T}"/>'
            + text(x + w / 2, y + 4, label, 11, RED_D, extra=BOLD))


def saes():
    pts = [(38, 48), (96, 36), (64, 96), (118, 94), (34, 150), (100, 152)]
    active = {1, 2, 5}
    edges = [(0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5), (2, 5), (0, 1)]
    b = ""
    for i, j in edges:
        on = i in active and j in active
        b += f'<line x1="{pts[i][0]}" y1="{pts[i][1]}" x2="{pts[j][0]}" y2="{pts[j][1]}" stroke="{RED if on else BORDER}" stroke-width="{1.8 if on else 1}"/>'
    b += "\n"
    for k, (x, y) in enumerate(pts):
        b += neuron(x, y, k in active, seed=k)
    b += text(76, 186, "biological neurons")
    b += arrow(140, 100, 174, 100)
    b += text(157, 92, "SAE", 10, MUTED, extra=BOLD)
    lit = {1: "position", 4: "running speed", 6: "reward"}
    for i in range(8):
        y = 30 + i * 20
        if i in lit:
            b += f'<circle cx="190" cy="{y}" r="7" fill="{RED}" stroke="{RED_D}" stroke-width="1.2"/>'
            b += f'<line x1="198" y1="{y}" x2="212" y2="{y}" stroke="{RED}" stroke-width="1.2"/>'
            b += pill(214, y, lit[i])
        else:
            b += f'<circle cx="190" cy="{y}" r="7" fill="{SURF}" stroke="{GREY}" stroke-width="1.2"/>'
    b += "\n" + text(190, 186, "sparse latents")
    b += text(180, 212, "Each active latent stands for one concept", 12.5, INK)
    svg("saes", "Diagram: active biological neurons are mapped by a sparse autoencoder to a few latents, each standing for a concept such as position, running speed or reward.", b)


# ---------------- Compressed computation ----------------
def compressed_computation():
    b = f'<line x1="180" y1="14" x2="180" y2="206" stroke="{BORDER}" stroke-width="1"/>\n'
    # Left: looked like more computations than neurons
    b += text(90, 22, "LOOKED LIKE", 9.5, BLUE_D, extra=CAPS)
    b += text(90, 44, "more computations", 19, INK, font=SERIF)
    b += text(90, 63, "than neurons", 19, INK, font=SERIF)
    top = 92
    ins = [top + i * 25 for i in range(5)]
    hid = [top + 32, top + 68]
    xl, xh, xr = 38, 90, 142
    for y1 in ins:
        for y2 in hid:
            b += f'<line x1="{xl}" y1="{y1}" x2="{xh}" y2="{y2}" stroke="{BLUE_L}" stroke-width="1"/>'
            b += f'<line x1="{xh}" y1="{y2}" x2="{xr}" y2="{y1}" stroke="{BLUE_L}" stroke-width="1"/>'
    for y in ins:
        b += f'<circle cx="{xl}" cy="{y}" r="5.5" fill="{SURF}" stroke="{BLUE_D}" stroke-width="1.3"/><circle cx="{xr}" cy="{y}" r="5.5" fill="{SURF}" stroke="{BLUE_D}" stroke-width="1.3"/>'
    for y in hid:
        b += f'<circle cx="{xh}" cy="{y}" r="9" fill="{BLUE}" stroke="{BLUE_D}" stroke-width="1.3"/>'
    b += "\n"
    # Right: was really noise-driven help from a mixing term
    b += text(270, 22, "WAS REALLY", 9.5, RED_D, extra=CAPS)
    b += text(270, 44, "noise-driven help", 19, INK, font=SERIF)
    b += text(270, 63, "from a mixing term", 19, INK, font=SERIF)
    b += (f'<text x="270" y="128" font-size="26" fill="{INK}" text-anchor="middle" {SERIF}>'
          f'<tspan font-style="italic">y</tspan> = ReLU(<tspan font-style="italic">x</tspan>)</text>\n')
    b += (f'<text x="270" y="166" font-size="34" fill="{RED}" text-anchor="middle" {SERIF}>'
          f'+ <tspan font-style="italic">Mx</tspan></text>\n')
    b += f'<path d="M250 176 v4 H298 v-4 M274 180 v4" fill="none" stroke="{RED}" stroke-width="1.3"/>\n'
    b += text(270, 200, "mixing term", 11.5, RED_D, extra=BOLD)
    svg("compressed-computation", "Diagram: a network that looked like it did more computations than it has neurons was really helped by a noise-driven mixing term: y = ReLU(x) + Mx.", b)


# ---------------- Neuroscience helpers ----------------
def mouse(x, y, s=1.0, color="#8A8580", flip=False, sleepy=False):
    """Small side-view mouse facing right, centred on its body at (x, y)."""
    t = f' transform="translate({x} {y}) scale({-s if flip else s} {s})"'
    return (f'<g{t}>'
            f'<path d="M-11 1 C-18 2 -22 -4 -27 -2" fill="none" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>'
            f'<ellipse cx="0" cy="0" rx="12" ry="7.5" fill="{color}"/>'
            f'<ellipse cx="11" cy="-2" rx="6.5" ry="5" fill="{color}"/>'
            f'<path d="M16 -3.5 L20.5 -1 L16 0.8 Z" fill="{color}"/>'
            f'<circle cx="8.5" cy="-7.5" r="3.6" fill="{color}" stroke="{SURF}" stroke-width="1"/>'
            + (f'<path d="M11.4 -3 q1.6 1.4 3.2 0" fill="none" stroke="{SURF}" stroke-width="1" stroke-linecap="round"/>' if sleepy
               else f'<circle cx="13" cy="-3" r="1.1" fill="{SURF}"/>') +
            f'</g>\n')


ROOMS = [("A", RED_T, RED_D), ("B", BLUE_T, BLUE_D), ("B", BLUE_T, BLUE_D), ("C", YELLOW_T, YELLOW_D)]


def rooms(y, h, letter_size=24, stripes=True, x0=32, w=74, gap=4, letter_at=0.5):
    """A-B-B-C track of rooms. The two B rooms share an identical wall pattern."""
    s = ""
    for k, (name, fill, deep) in enumerate(ROOMS):
        x = x0 + k * (w + gap)
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{deep}" stroke-width="1.3"/>'
        if stripes and name == "B":
            for sx in (w * 0.11, w * 0.22, w * 0.78, w * 0.89):
                s += f'<line x1="{x+sx:.1f}" y1="{y+4}" x2="{x+sx:.1f}" y2="{y+h-4}" stroke="{BLUE_L}" stroke-width="2.4"/>'
        s += text(round(x + w * letter_at, 1), y + h / 2 + letter_size * 0.33, name, letter_size, deep, font=SERIF)
    return s


def spikes(xs, y, h, color, width=1.6):
    return "".join(f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{y+h}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>' for x in xs) + "\n"


# ---------------- Shared pieces for the neuroscience figures ----------------
TX0, RW, RG = 48, 70, 4            # track start, room width, gap between rooms
TX1 = TX0 + 4 * RW + 3 * RG          # track end (340)


def room_x(k):
    return TX0 + k * (RW + RG)


def room_strip(y=14, h=30, with_mouse=True):
    s = rooms(y, h, 17, stripes=False, x0=TX0, w=RW, gap=RG, letter_at=0.5)
    if with_mouse:
        s += mouse(TX0 + 15, y + h - 9, 0.45, INK)
    # faint guides continuing the room boundaries downwards
    for k in range(1, 4):
        x = room_x(k) - RG / 2
        s += f'<line x1="{x}" y1="{y+h}" x2="{x}" y2="152" stroke="{BORDER}" stroke-width="1" stroke-dasharray="2 3"/>'
    return s + "\n"


def lane(y, h=24):
    return f'<rect x="{TX0}" y="{y}" width="{TX1-TX0}" height="{h}" rx="3" fill="{SURF}" stroke="{BORDER}" stroke-width="1"/>\n'


def burst(xc, n, spread, y, h, color, tint, seed=0, glow=True):
    """A cluster of spikes (ticks) with a soft glow behind them."""
    random.seed(seed)
    s = ""
    if glow:
        s += f'<rect x="{xc-spread*2.2:.1f}" y="{y+2}" width="{spread*4.4:.1f}" height="{h-4}" rx="5" fill="{tint}"/>'
    xs = sorted(random.gauss(xc, spread) for _ in range(n))
    return s + spikes(xs, y + 5, h - 10, color, 1.7)


def row_label(y, label, color, icon_fill, icon_stroke, seed):
    """Neuron icon to the left of a lane, with a label above the lane."""
    return (star_neuron(24, y + 12, icon_fill, icon_stroke, r=4, seed=seed, length=(5, 8))
            + text(TX0, y - 5, label, 10.5, color, "start", extra=BOLD))


def spike_legend(y, color=INK):
    s = spikes([TX0 + 2, TX0 + 7, TX0 + 12], y - 9, 11, color, 1.7)
    return s + text(TX0 + 22, y, "each line = one spike (the neuron firing)", 10.5, MUTED, "start")


# ---------------- Place cells distinguish identical rooms ----------------
def identical_rooms():
    b = room_strip()
    bx1, bx2 = room_x(1) + RW * 0.4, room_x(2) + RW * 0.4
    # Neuron 1: same response in both B rooms
    b += row_label(70, "Neuron 1: fires in both B rooms", TEAL_D, TEAL, TEAL_D, 3)
    b += lane(70)
    b += burst(bx1, 7, 4.5, 70, 24, TEAL_D, TEAL_T, 1) + burst(bx2, 7, 4.5, 70, 24, TEAL_D, TEAL_T, 2)
    # Neuron 2: fires only in the first B room
    b += row_label(120, "Neuron 2: fires only in the first B room", RED_D, RED, RED_D, 8)
    b += lane(120)
    b += burst(bx1, 8, 4.5, 120, 24, RED_D, RED_T, 3)
    b += spike_legend(172)
    b += text(180, 208, "Some neurons tell identical rooms apart", 12.5, INK)
    svg("identical-rooms", "Diagram: on a track of rooms A, B, B and C, one neuron fires in both identical-looking B rooms, while another fires only in the first B room. Each line is one spike.", b)


# ---------------- Neurons that "count" rooms ----------------
def counting_rooms():
    b = room_strip()
    counts = [3, 6, 4, 8]                    # different strength in each room
    centres = [room_x(k) + RW * 0.32 for k in range(4)]
    y = 92
    b += star_neuron(24, y + 14, YELLOW, YELLOW_D, r=4, seed=7, length=(5, 8))
    b += lane(y, 28)
    for k, (n, c) in enumerate(zip(counts, centres)):
        b += f'<line x1="{c:.1f}" y1="44" x2="{c:.1f}" y2="{y}" stroke="{YELLOW_D}" stroke-width="1" stroke-dasharray="2 2"/>'
        b += burst(c, n, 3.2, y, 28, YELLOW_D, YELLOW_T, 10 + k)
        b += f'<circle cx="{c:.1f}" cy="66" r="8.5" fill="{RED}"/>' + text(round(c, 1), 70, str(k + 1), 10.5, "#FFFFFF", extra=BOLD)
    b += text(TX0, 140, "One neuron: same spot in each room, different strength", 10.5, YELLOW_D, "start", extra=BOLD)
    b += spike_legend(176)
    b += text(180, 208, "Fires at the same spot in every room", 12.5, INK)
    svg("counting-rooms", "Diagram: one neuron fires at the same position within each of four rooms, with more or fewer spikes in each room, as if counting the rooms. Each line is one spike.", b)


# ---------------- Attention shapes spatial maps ----------------
def attention():
    random.seed(5)
    b = ""
    # linear track with reward zone
    b += f'<rect x="{TX0}" y="16" width="{TX1-TX0}" height="24" rx="3" fill="{SURF}" stroke="{GREY}" stroke-width="1"/>'
    rz0 = TX0 + (TX1 - TX0) * 0.76
    b += f'<rect x="{rz0:.1f}" y="16" width="40" height="24" fill="{YELLOW}"/>'
    b += text(round(rz0 + 20, 1), 31.5, "reward", 9, INK, extra=BOLD)
    b += text(TX0 + 8, 32, "virtual track", 9.5, MUTED, "start")
    place = rz0 + 14
    b += f'<line x1="{place:.1f}" y1="40" x2="{place:.1f}" y2="152" stroke="{BORDER}" stroke-width="1" stroke-dasharray="2 3"/>\n'
    # Engaged: spikes cluster at the place field
    y1 = 72
    b += mouse(30, y1 + 13, 0.5, INK)
    for k, (x1, x2) in enumerate([(4, 13), (1, 11), (4, 13)]):   # speed lines: running fast
        b += f'<line x1="{x1}" y1="{y1+8+k*4}" x2="{x2}" y2="{y1+8+k*4}" stroke="{TEAL}" stroke-width="1.6" stroke-linecap="round"/>'
    b += "\n"
    b += text(TX0, y1 - 5, "Engaged, running mouse: neuron fires at one place", 10.5, TEAL_D, "start", extra=BOLD)
    b += lane(y1)
    b += burst(place, 9, 4, y1, 24, TEAL_D, TEAL_T, 21)
    # Disengaged: the same neuron's spikes are scattered
    y2 = 122
    b += mouse(30, y2 + 15, 0.5, "#8A8580", sleepy=True)
    b += text(37, y2 + 4, "z", 8, MUTED, extra=BOLD) + text(42, y2 - 1, "z", 10, MUTED, extra=BOLD)
    b += text(TX0, y2 - 5, "Tired, disengaged mouse: spikes scattered", 10.5, MUTED, "start", extra=BOLD)
    b += lane(y2)
    xs = [random.uniform(TX0 + 8, TX1 - 8) for _ in range(9)]
    b += spikes(xs, y2 + 5, 14, MUTED, 1.7)
    b += spike_legend(174)
    b += text(180, 208, "Attention keeps the neural map of space sharp", 12.5, INK)
    svg("attention", "Diagram: when the mouse is engaged, a place cell fires at one spot on the track; when it is disengaged, the same cell's spikes are scattered along the track. Each line is one spike.", b)


diffusion()
saes()
compressed_computation()
identical_rooms()
counting_rooms()
attention()
print("ok")
