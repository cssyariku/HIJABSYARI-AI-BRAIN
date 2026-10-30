"""Render Day 23 carousel, Stories, and QA previews.

Run: python CONTENT/DAY-23/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "brown-outfit-five-hijab-colors.png"

CW, CH = 1080, 1350
SW, SH = 1080, 1920
PAPER = (249, 244, 237)
CREAM = (239, 226, 208)
DARK = (54, 39, 32)
MUTED = (111, 91, 80)
LINE = (214, 194, 178)
BROWN = (93, 61, 47)
WARM_CREAM = (221, 207, 185)
ROSE = (174, 126, 124)
OLIVE = (111, 112, 78)
BLUE = (105, 121, 145)
BURGUNDY = (116, 42, 49)
WHITE = (255, 255, 255)
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LOOKS = [
    ("WARM CREAM", WARM_CREAM, "light & clean",
     "Kontras terang yang tetap terasa hangat di samping outfit cokelat.",
     ["light contrast", "warm", "clean"]),
    ("DUSTY ROSE", ROSE, "soft color",
     "Aksen warna lembut tanpa membuat palet terasa terlalu terang.",
     ["soft", "muted color", "gentle contrast"]),
    ("MUTED OLIVE", OLIVE, "earthy tonal",
     "Warna muted yang menjaga nuansa bumi tetap dominan.",
     ["earthy", "tonal", "grounded"]),
    ("DUSTY BLUE", BLUE, "cool contrast",
     "Kontras lebih sejuk, tetap tenang karena arah warnanya redup.",
     ["cool contrast", "muted", "balanced"]),
    ("BURGUNDY", BURGUNDY, "deep accent",
     "Arah warna dalam dengan kontras yang terlihat lebih tegas.",
     ["deep", "rich accent", "higher contrast"]),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def rounded(draw, box, radius=30, fill=PAPER, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrap(draw, value, face, max_width):
    rows, row = [], ""
    for word in value.split():
        trial = f"{row} {word}".strip()
        if draw.textbbox((0, 0), trial, font=face)[2] <= max_width:
            row = trial
        else:
            if row:
                rows.append(row)
            row = word
    if row:
        rows.append(row)
    return rows


def text_block(draw, value, xy, face, fill, max_width, leading=None):
    x, y = xy
    leading = leading or int(face.size * 1.18)
    for row in wrap(draw, value, face, max_width):
        draw.text((x, y), row, font=face, fill=fill)
        y += leading
    return y


def footer(draw, h=CH, light=False):
    draw.text((64, h - 44), "@hijabsyaricoid", font=font(SANS, 22),
              fill=PAPER if light else MUTED, anchor="ls")


def panel(index):
    src = Image.open(SOURCE).convert("RGB")
    pw = src.width / 5
    pad = 5
    left = round(index * pw) + (pad if index else 0)
    right = round((index + 1) * pw) - (pad if index < 4 else 0)
    return src.crop((left, 0, right, src.height))


def strip(size):
    out = Image.new("RGB", size, PAPER)
    gap = 6
    cell = (size[0] - gap * 4) // 5
    for i in range(5):
        pic = ImageOps.fit(panel(i), (cell, size[1]), Image.Resampling.LANCZOS, centering=(.5, .42))
        out.paste(pic, (i * (cell + gap), 0))
    return out


def cover():
    im = Image.new("RGB", (CW, CH), PAPER)
    im.paste(strip((CW, 710)), (0, 640))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rectangle((0, 0, CW, 760), fill=(*PAPER, 242))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    text_block(d, "Outfit cokelat + hijab apa?", (64, 84),
               font(SERIF_BOLD, 72), DARK, 940, 84)
    d.text((64, 290), "Coba 5 arah warna ini.", font=font(SANS_BOLD, 34), fill=BROWN)
    rounded(d, (64, 402, 820, 508), radius=48, fill=CREAM, outline=LINE)
    d.text((442, 455), "Light · soft · earthy · cool · deep",
           font=font(SANS_BOLD, 26), fill=DARK, anchor="mm")
    footer(d, light=True)
    return im


def overview():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Pilih nuansanya dulu", (64, 76), font(SERIF_BOLD, 62), DARK, 930, 74)
    labels = ["light & clean", "soft color", "earthy tonal", "cool contrast", "deep accent"]
    y = 248
    for i, ((name, color, _, _, _), label) in enumerate(zip(LOOKS, labels), 1):
        rounded(d, (64, y, 1016, y + 156), radius=30, fill=PAPER, outline=LINE)
        d.rounded_rectangle((92, y + 28, 222, y + 128), radius=24, fill=color)
        d.text((157, y + 78), f"{i:02d}", font=font(SANS_BOLD, 26),
               fill=DARK if i == 1 else PAPER, anchor="mm")
        d.text((254, y + 34), name, font=font(SANS_BOLD, 27), fill=DARK)
        d.text((254, y + 86), label, font=font(SANS, 25), fill=MUTED)
        y += 176
    d.text((64, 1168), "Referensi visual—bukan aturan warna universal.",
           font=font(SANS, 23), fill=MUTED)
    footer(d)
    return im


def look_slide(index):
    name, color, lead, body, tags = LOOKS[index]
    im = Image.new("RGB", (CW, CH), PAPER)
    portrait = ImageOps.fit(panel(index), (540, 1120), Image.Resampling.LANCZOS, centering=(.5, .42))
    im.paste(portrait, (540, 110))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rectangle((0, 0, 610, CH), fill=(*PAPER, 248))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    rounded(d, (64, 84, 330, 150), radius=30, fill=color)
    d.text((197, 117), f"{index+1:02d}  {name}", font=font(SANS_BOLD, 19),
           fill=DARK if index == 0 else PAPER, anchor="mm")
    text_block(d, name.replace(" ", "\n", 1), (64, 210),
               font(SERIF_BOLD, 55), DARK, 450, 66)
    d.text((64, 372), lead, font=font(SANS_BOLD, 29), fill=color)
    y = text_block(d, body, (64, 446), font(SANS, 28), DARK, 450, 43)
    d.line((64, y + 26, 500, y + 26), fill=LINE, width=2)
    for i, tag in enumerate(tags):
        yy = y + 80 + i * 74
        d.ellipse((64, yy + 8, 84, yy + 28), fill=color)
        d.text((108, yy), tag, font=font(SANS_BOLD, 23), fill=MUTED)
    d.text((64, 1176), "Cek lagi di cahaya alami.", font=font(SANS, 22), fill=MUTED)
    footer(d)
    return im


def chooser():
    im = Image.new("RGB", (CW, CH), (226, 212, 196))
    d = ImageDraw.Draw(im)
    text_block(d, "Pilih lewat 3 pertanyaan", (64, 82), font(SERIF_BOLD, 62), DARK, 930, 74)
    cards = [
        ("01", "Kontras light, medium,", "atau deep?"),
        ("02", "Tetap hangat atau", "tambah kontras sejuk?"),
        ("03", "Warna mana yang", "sudah ada di lemari?"),
    ]
    y = 340
    for num, a, b in cards:
        rounded(d, (64, y, 1016, y + 210), radius=36, fill=PAPER, outline=LINE)
        d.ellipse((96, y + 64, 178, y + 146), fill=BROWN)
        d.text((137, y + 105), num, font=font(SANS_BOLD, 24), fill=PAPER, anchor="mm")
        d.text((218, y + 52), a, font=font(SANS_BOLD, 31), fill=DARK)
        d.text((218, y + 108), b, font=font(SANS, 29), fill=MUTED)
        y += 236
    rounded(d, (64, 1075, 1016, 1208), radius=32, fill=BROWN)
    d.text((540, 1121), "Simpan paletnya.", font=font(SANS_BOLD, 29), fill=PAPER, anchor="mm")
    d.text((540, 1165), "Kamu pilih nomor berapa?", font=font(SANS, 25), fill=PAPER, anchor="mm")
    footer(d)
    return im


def story_one():
    im = Image.new("RGB", (SW, SH), PAPER)
    im.paste(strip((SW, 1020)), (0, 900))
    d = ImageDraw.Draw(im)
    text_block(d, "Satu outfit cokelat, lima arah warna.", (72, 145),
               font(SERIF_BOLD, 70), DARK, 930, 84)
    d.text((72, 400), "Light · soft · earthy · cool · deep",
           font=font(SANS_BOLD, 33), fill=BROWN)
    rounded(d, (72, 545, 1008, 790), radius=40, fill=CREAM, outline=LINE)
    d.text((540, 665), "Geser untuk lihat semuanya →", font=font(SANS_BOLD, 33), fill=DARK, anchor="mm")
    footer(d, SH, light=True)
    return im


def story_two():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Kamu lebih sering pilih yang mana?", (72, 145),
               font(SERIF_BOLD, 68), DARK, 930, 82)
    a = ImageOps.fit(panel(0), (430, 900), Image.Resampling.LANCZOS, centering=(.5, .42))
    b = ImageOps.fit(panel(4), (430, 900), Image.Resampling.LANCZOS, centering=(.5, .42))
    im.paste(a, (72, 430)); im.paste(b, (578, 430))
    d = ImageDraw.Draw(im)
    rounded(d, (92, 1250, 482, 1335), radius=40, fill=WARM_CREAM)
    d.text((287, 1292), "LIGHT & SOFT", font=font(SANS_BOLD, 26), fill=DARK, anchor="mm")
    rounded(d, (598, 1250, 988, 1335), radius=40, fill=BURGUNDY)
    d.text((793, 1292), "EARTHY & DEEP", font=font(SANS_BOLD, 26), fill=PAPER, anchor="mm")
    rounded(d, (72, 1465, 1008, 1740), radius=40, fill=PAPER, outline=LINE)
    d.text((540, 1545), "Pilih di Poll ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 1650), "LIGHT & SOFT / EARTHY & DEEP", font=font(SANS_BOLD, 28), fill=DARK, anchor="mm")
    footer(d, SH)
    return im


def story_three():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Nomor 1–5 yang paling kamu pilih?", (72, 145),
               font(SERIF_BOLD, 69), DARK, 930, 84)
    x = 72
    for i, (_, color, _, _, _) in enumerate(LOOKS, 1):
        d.rounded_rectangle((x, 520, x + 164, 670), radius=30, fill=color, outline=LINE)
        d.text((x + 82, 595), str(i), font=font(SANS_BOLD, 38),
               fill=DARK if i == 1 else PAPER, anchor="mm")
        x += 184
    rounded(d, (72, 850, 1008, 1230), radius=42, fill=PAPER, outline=LINE)
    d.text((540, 946), "Jawab di sticker ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 1080), "Nomor + outfit berikutnya", font=font(SANS_BOLD, 34), fill=DARK, anchor="mm")
    d.text((72, 1480), "Jawabanmu membantu Color Lab berikutnya.",
           font=font(SANS_BOLD, 29), fill=MUTED)
    footer(d, SH)
    return im


def save_png(im, path):
    tmp = path.with_name(path.stem + ".rendering.png")
    if tmp.exists():
        tmp.unlink()
    im.convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(tmp, optimize=False)
    with Image.open(tmp) as check:
        check.load()
        if check.size != im.size:
            raise ValueError(f"Dimension mismatch: {path}")
    tmp.replace(path)


def sheet(images, path, cols, thumb, title):
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows + 54), WHITE)
    d = ImageDraw.Draw(canvas)
    d.text((20, 12), title, font=font(SANS_BOLD, 24), fill=DARK)
    for i, im in enumerate(images):
        small = im.convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        canvas.paste(small, ((i % cols) * thumb[0], 54 + (i // cols) * thumb[1]))
    save_png(canvas, path)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    slides = [cover(), overview()] + [look_slide(i) for i in range(5)] + [chooser()]
    for i, im in enumerate(slides, 1):
        save_png(im, ASSETS / f"carousel-{i:02d}.png")
    stories = [story_one(), story_two(), story_three()]
    for i, im in enumerate(stories, 1):
        save_png(im, ASSETS / f"story-{i:02d}.png")
    sheet(slides, ASSETS / "contact-sheet.png", 4, (270, 338), "DAY 23 — CAROUSEL QA")
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480), "DAY 23 — STORIES QA")


if __name__ == "__main__":
    main()
