"""Draw the 23 November 2026 front page as entry.png (1024x1024).

Run once, locally, before submitting. The grader never runs this file:
main.py only copies the finished entry.png to the output directory.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 241, 221)
INK = (22, 22, 22)
RED = (178, 28, 28)
NAVY = (23, 48, 84)
TEAL = (14, 94, 88)
GOLD = (176, 124, 20)
ORANGE = (214, 96, 20)
GREY = (90, 88, 80)
CARD = (255, 253, 246)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# --- small pictograms, one per story -------------------------------------

def icon_globe(d, x, y, s):
    d.ellipse([x, y, x + s, y + s], outline=NAVY, width=5)
    d.ellipse([x + s * 0.28, y + 4, x + s * 0.72, y + s - 4], outline=NAVY, width=3)
    d.line([x + 4, y + s * 0.5, x + s - 4, y + s * 0.5], fill=NAVY, width=3)
    d.line([x + s * 0.62, y + s * 0.08, x + s * 0.38, y + s * 0.92], fill=RED, width=5)
    d.line([x + s * 0.78, y + s * 0.78, x + s * 0.95, y + s * 0.95], fill=RED, width=5)


def icon_tanker(d, x, y, s):
    d.polygon([(x, y + s * 0.55), (x + s, y + s * 0.55), (x + s * 0.88, y + s * 0.85),
               (x + s * 0.12, y + s * 0.85)], fill=NAVY)
    d.rectangle([x + s * 0.12, y + s * 0.28, x + s * 0.42, y + s * 0.55], fill=RED)
    d.rectangle([x + s * 0.48, y + s * 0.28, x + s * 0.78, y + s * 0.55], fill=GOLD)
    d.rectangle([x + s * 0.78, y + s * 0.12, x + s * 0.92, y + s * 0.55], fill=INK)
    for i, wx in enumerate([0.05, 0.38, 0.71]):
        d.arc([x + s * wx, y + s * 0.86, x + s * (wx + 0.28), y + s * 1.02],
              180, 360, fill=TEAL, width=4)


def icon_warship(d, x, y, s):
    d.polygon([(x, y + s * 0.6), (x + s, y + s * 0.6), (x + s * 0.85, y + s * 0.88),
               (x + s * 0.15, y + s * 0.88)], fill=NAVY)
    d.rectangle([x + s * 0.3, y + s * 0.32, x + s * 0.62, y + s * 0.6], fill=INK)
    d.line([x + s * 0.46, y + s * 0.32, x + s * 0.46, y + s * 0.08], fill=INK, width=4)
    d.polygon([(x + s * 0.46, y + s * 0.08), (x + s * 0.72, y + s * 0.18),
               (x + s * 0.46, y + s * 0.26)], fill=RED)
    for cx, cy, r in [(0.18, 0.22, 7), (0.3, 0.12, 5), (0.12, 0.1, 4)]:
        d.ellipse([x + s * cx - r, y + s * cy - r, x + s * cx + r, y + s * cy + r],
                  fill=GREY)


def icon_building(d, x, y, s):
    d.rectangle([x + s * 0.2, y + s * 0.12, x + s * 0.8, y + s * 0.88],
                outline=INK, width=4)
    d.line([x + s * 0.2, y + s * 0.5, x + s * 0.8, y + s * 0.5], fill=INK, width=3)
    for wx in (0.32, 0.52, 0.68):
        for wy in (0.24, 0.62):
            d.rectangle([x + s * wx, y + s * wy, x + s * (wx + 0.1), y + s * (wy + 0.12)],
                        fill=NAVY)
    d.line([x + s * 0.5, y + s * 0.12, x + s * 0.38, y + s * 0.5,
            x + s * 0.58, y + s * 0.88], fill=RED, width=4)
    d.polygon([(x + s * 0.05, y + s * 0.95), (x + s * 0.3, y + s * 0.8),
               (x + s * 0.5, y + s * 0.95)], fill=GREY)


def icon_mercury(d, x, y, s):
    d.ellipse([x + s * 0.22, y + s * 0.22, x + s * 0.78, y + s * 0.78],
              fill=GOLD, outline=INK, width=3)
    for cx, cy, r in [(0.4, 0.4, 6), (0.58, 0.55, 8), (0.45, 0.62, 4)]:
        d.ellipse([x + s * cx - r, y + s * cy - r, x + s * cx + r, y + s * cy + r],
                  outline=INK, width=2)
    d.arc([x, y + s * 0.05, x + s, y + s * 0.95], 200, 340, fill=NAVY, width=3)
    d.ellipse([x + s * 0.82, y + s * 0.08, x + s * 0.94, y + s * 0.2], fill=TEAL)


def icon_flame(d, x, y, s):
    d.rectangle([x + s * 0.12, y + s * 0.55, x + s * 0.3, y + s * 0.9], fill=INK)
    d.rectangle([x + s * 0.7, y + s * 0.55, x + s * 0.88, y + s * 0.9], fill=INK)
    d.polygon([(x + s * 0.5, y + s * 0.05), (x + s * 0.72, y + s * 0.45),
               (x + s * 0.62, y + s * 0.38), (x + s * 0.78, y + s * 0.75),
               (x + s * 0.5, y + s * 0.92), (x + s * 0.22, y + s * 0.75),
               (x + s * 0.38, y + s * 0.38), (x + s * 0.28, y + s * 0.45)],
              fill=ORANGE, outline=RED, width=3)
    d.polygon([(x + s * 0.5, y + s * 0.45), (x + s * 0.62, y + s * 0.68),
               (x + s * 0.5, y + s * 0.82), (x + s * 0.38, y + s * 0.68)],
              fill=GOLD)


ICONS = [icon_globe, icon_tanker, icon_warship, icon_building, icon_mercury, icon_flame]
ACCENTS = [TEAL, NAVY, RED, NAVY, GOLD, ORANGE]

STORIES = [
    ("CLIMATE  •  COP31", "COP31 COLLAPSES — NO CLIMATE DEAL",
     "UN climate talks end without agreement. The EU and others reject "
     "any deal with no language on phasing out fossil fuels."),
    ("STRAIT OF HORMUZ", "TANKERS HIT OFF HORMUZ",
     "At least three oil tankers are struck in and near the strait; two "
     "more catch fire after hitting naval mines. Shipping attacks are at "
     "their highest since the war began."),
    ("LIBYA  •  BENGHAZI", "DRONE STRIKE SINKS RUSSIAN SHIP",
     "Suspected Ukrainian sea drones hit the Russian corvette Merkury at "
     "Benghazi naval base. The ship capsizes; 10 people are injured."),
    ("UKRAINE  •  DYMER", "FLAT HIT NEAR KYIV: 2 DEAD, 11 MISSING",
     "A Russian drone hits a five-storey block north of Kyiv. Rescuers "
     "search the rubble for 11 missing people, including two children."),
    ("SPACE  •  MERCURY", "BEPICOLOMBO REACHES MERCURY",
     "After an eight-year journey, the European-Japanese BepiColombo "
     "spacecraft enters orbit around Mercury — only the second mission "
     "ever to do so."),
    ("INDONESIA  •  CIKANDE", "FACTORY FIRE IN INDONESIA",
     "A fire tears through a candy factory in Cikande, Banten. Rescuers "
     "recover 24 body bags; dozens of workers are still missing."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=INK, width=1)

    # Masthead
    f_kicker = font(SANS_B, 20)
    f_title = font(SERIF_B, 56)
    f_date = font(SANS_B, 26)
    f_sub = font(SERIF, 21)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 34), title, font=f_title, fill=INK)
    d.line([60, 108, W - 60, 108], fill=RED, width=4)
    date = "MONDAY  •  23 NOVEMBER 2026"
    dw = d.textlength(date, font=f_date)
    d.rectangle([(W - dw) / 2 - 22, 122, (W + dw) / 2 + 22, 160], fill=INK)
    d.text(((W - dw) / 2, 126), date, font=f_date, fill=(255, 255, 255))
    sub = "Six stories that defined the day — from climate talks to Mercury orbit."
    sw = d.textlength(sub, font=f_sub)
    d.text(((W - sw) / 2, 168), sub, font=f_sub, fill=GREY)

    # Story cards: 2 columns x 3 rows
    f_tag = font(SANS_B, 17)
    f_head = font(SANS_B, 25)
    f_body = font(SANS, 18)
    cw, ch, gap = 464, 242, 16
    ox, oy = 36, 200
    for i, (tag, head, body) in enumerate(STORIES):
        x = ox + (i % 2) * (cw + gap)
        y = oy + (i // 2) * (ch + gap)
        d.rectangle([x, y, x + cw, y + ch], fill=CARD, outline=INK, width=2)
        d.rectangle([x, y, x + cw, y + 6], fill=ACCENTS[i])
        d.text((x + 16, y + 16), f"{i + 1}.  {tag}", font=f_tag, fill=RED)
        hy = draw_lines(d, wrap(d, head, f_head, cw - 32), x + 16, y + 44,
                        f_head, INK, 30)
        ix, iy, isize = x + 16, hy + 6, 78
        ICONS[i](d, ix, iy, isize)
        bx = ix + isize + 14
        draw_lines(d, wrap(d, body, f_body, cw - 32 - isize - 14), bx, hy + 4,
                   f_body, INK, 23)

    # Footer
    f_foot = font(SANS, 15)
    foot = "Sources: AP • Reuters • BBC • Al Jazeera • The Hindu  —  23 November 2026"
    fw = d.textlength(foot, font=f_foot)
    d.text(((W - fw) / 2, 962), foot, font=f_foot, fill=GREY)
    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
