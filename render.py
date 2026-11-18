#!/usr/bin/env python3
"""Draw the one-image summary of Tuesday 17 November 2026."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (10, 17, 30)
CARD = (17, 27, 44)
EDGE = (36, 52, 78)
WHITE = (245, 248, 252)
MUTED = (166, 182, 206)
ACCENT = (45, 212, 191)
RED = (239, 68, 68)
ORANGE = (249, 115, 22)
YELLOW = (253, 224, 71)
STEEL = (203, 213, 225)
SEA = (30, 64, 108)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(d, xy, s, f, fill, maxw):
    """Draw s, shrinking until it fits maxw."""
    while f.size > 10 and d.textlength(s, font=f) > maxw:
        f = font(f.path, f.size - 1)
    d.text(xy, s, font=f, fill=fill)
    return f


def icon_bridge(d, x, y):
    """A bridge whose middle span has fallen into the water."""
    d.rectangle([x + 4, y + 96, x + 114, y + 104], fill=SEA)
    d.rectangle([x + 2, y + 62, x + 44, y + 70], fill=STEEL)
    d.rectangle([x + 76, y + 62, x + 116, y + 70], fill=STEEL)
    d.polygon([(x + 44, y + 62), (x + 60, y + 88), (x + 40, y + 92)], fill=STEEL)
    d.polygon([(x + 76, y + 62), (x + 64, y + 86), (x + 82, y + 90)], fill=STEEL)
    d.rectangle([x + 14, y + 30, x + 22, y + 62], fill=(148, 163, 184))
    d.rectangle([x + 96, y + 30, x + 104, y + 62], fill=(148, 163, 184))
    d.line([(x + 18, y + 32), (x + 60, y + 62)], fill=(148, 163, 184), width=3)
    d.line([(x + 100, y + 32), (x + 60, y + 62)], fill=(148, 163, 184), width=3)
    for i in range(3):
        d.arc([x + 34 + i * 6, y + 74 + i * 4, x + 82 + i * 6, y + 104 + i * 4],
              200, 340, fill=ORANGE, width=3)


def icon_plane(d, x, y):
    """A wide-body jet on its way, with a red carpet under the nose."""
    d.polygon([(x + 8, y + 66), (x + 74, y + 48), (x + 104, y + 52), (x + 110, y + 60),
               (x + 74, y + 64), (x + 30, y + 80), (x + 12, y + 78)], fill=STEEL)
    d.polygon([(x + 58, y + 54), (x + 74, y + 20), (x + 84, y + 20), (x + 78, y + 58)],
              fill=(148, 163, 184))
    d.polygon([(x + 40, y + 66), (x + 30, y + 96), (x + 42, y + 94), (x + 56, y + 68)],
              fill=(148, 163, 184))
    for i in range(4):
        d.ellipse([x + 34 + i * 12, y + 58, x + 40 + i * 12, y + 64], fill=(71, 85, 105))
    d.polygon([(x + 8, y + 92), (x + 52, y + 88), (x + 44, y + 100), (x + 12, y + 100)],
              fill=(190, 24, 40))


def icon_hormuz(d, x, y):
    """A tanker burning in the strait, a drone overhead."""
    d.rectangle([x + 4, y + 84, x + 116, y + 96], fill=SEA)
    d.polygon([(x + 18, y + 62), (x + 96, y + 62), (x + 104, y + 84), (x + 12, y + 84)],
              fill=(148, 163, 184))
    d.rectangle([x + 44, y + 44, x + 74, y + 62], fill=(203, 213, 225))
    for i, fx in enumerate((x + 30, x + 56, x + 82)):
        d.polygon([(fx, y + 60), (fx + 12, y + 60), (fx + 6, y + 34 - i % 2 * 8)], fill=ORANGE)
        d.polygon([(fx + 3, y + 56), (fx + 10, y + 56), (fx + 7, y + 44)], fill=YELLOW)
    d.line([(x + 20, y + 26), (x + 44, y + 26)], fill=STEEL, width=3)
    d.line([(x + 26, y + 20), (x + 38, y + 20)], fill=STEEL, width=3)
    d.ellipse([x + 22, y + 14, x + 32, y + 22], fill=RED)


def icon_knesset(d, x, y):
    """A parliament front: pediment, columns, a flag."""
    d.polygon([(x + 10, y + 44), (x + 60, y + 20), (x + 110, y + 44)], fill=(148, 163, 184))
    d.rectangle([x + 10, y + 44, x + 110, y + 54], fill=STEEL)
    for i in range(4):
        cx = x + 22 + i * 24
        d.rectangle([cx, y + 54, cx + 10, y + 92], fill=(148, 163, 184))
    d.rectangle([x + 6, y + 92, x + 114, y + 100], fill=STEEL)
    d.rectangle([x + 96, y + 4, x + 99, y + 30], fill=(120, 134, 158))
    d.rectangle([x + 99, y + 6, x + 116, y + 18], fill=(0, 56, 184))


def icon_crash(d, x, y):
    """A transport plane going down, trailing smoke."""
    d.polygon([(x + 30, y + 40), (x + 96, y + 72), (x + 88, y + 84), (x + 22, y + 54)],
              fill=STEEL)
    d.polygon([(x + 54, y + 50), (x + 62, y + 20), (x + 74, y + 22), (x + 70, y + 56)],
              fill=(148, 163, 184))
    d.polygon([(x + 40, y + 46), (x + 24, y + 22), (x + 34, y + 20), (x + 52, y + 48)],
              fill=(148, 163, 184))
    for i in range(4):
        d.ellipse([x + 6 + i * 6, y + 24 - i * 4, x + 26 + i * 6, y + 44 - i * 4],
                  outline=(120, 134, 158), width=3)
    d.rectangle([x + 20, y + 96, x + 108, y + 104], fill=(51, 65, 85))


def icon_reactor(d, x, y):
    """Cooling towers and an atom: a first nuclear plant on the grid."""
    for i, tx in enumerate((x + 14, x + 58)):
        d.polygon([(tx, y + 96), (tx + 10, y + 46), (tx + 30, y + 46), (tx + 40, y + 96)],
                  fill=(148, 163, 184))
        d.rectangle([tx + 8, y + 42, tx + 32, y + 50], fill=(203, 213, 225))
    for i in range(3):
        d.arc([x + 66, y + 30, x + 118, y + 82], i * 60, i * 60 + 180, fill=ACCENT, width=4)
    d.ellipse([x + 88, y + 52, x + 96, y + 60], fill=ACCENT)


CARDS = [
    ("KERCH BRIDGE DOWN", ["Ukraine's 'unprecedented'", "strike drops a span; Russia", "hits Kyiv in return"], icon_bridge),
    ("TRUMP IN MANILA", ["Lands for ASEAN and Quad", "talks; protests met with", "hundreds of arrests"], icon_plane),
    ("TANKERS ABLAZE", ["Iran hits a US radar in", "Bahrain; three ships burn", "in the Strait of Hormuz"], icon_hormuz),
    ("ISRAEL: NEW SPEAKER", ["Matan Kahana elected, and", "Netanyahu's opponents take", "the parliament"], icon_knesset),
    ("19 DIE IN SIBERIA", ["A Russian An-12 transport", "crashes near Kemerovo,", "all aboard killed"], icon_crash),
    ("BANGLADESH: FIRST REACTOR", ["Rooppur nuclear plant", "starts feeding the", "national grid"], icon_reactor),
]


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 8], fill=ACCENT)
    d.text((36, 40), "TUESDAY", font=font(BOLD, 26), fill=ACCENT)
    d.text((34, 74), "17 NOVEMBER 2026", font=font(BOLD, 76), fill=WHITE)
    d.text((36, 162), "THE WORLD IN ONE DAY", font=font(BOLD, 22), fill=MUTED)
    d.line([(36, 200), (W - 36, 200)], fill=EDGE, width=2)

    cw, ch, gap = 470, 216, 18
    left, top = 32, 214
    for i, (title, lines, icon) in enumerate(CARDS):
        x = left + (i % 2) * (cw + gap)
        y = top + (i // 2) * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=18, fill=CARD, outline=EDGE, width=2)
        icon(d, x + 26, y + 52)
        tf = fit(d, (x + 152, y + 34), title, font(BOLD, 30), WHITE, cw - 176)
        ty = y + 34 + tf.size + 12
        for line in lines:
            fit(d, (x + 152, ty), line, font(REG, 21), MUTED, cw - 172)
            ty += 28

    fy = top + 3 * (ch + gap) + 12
    d.rounded_rectangle([left, fy, W - left, fy + 66], radius=14, fill=(15, 25, 40), outline=EDGE, width=2)
    d.text((left + 20, fy + 20), "Also today: UK sanctions eight settler firms, an NSA network",
           font=font(REG, 20), fill=MUTED)
    d.text((left + 20, fy + 42), "outage in the US, and Dhoni retires from the IPL",
           font=font(REG, 20), fill=MUTED)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
