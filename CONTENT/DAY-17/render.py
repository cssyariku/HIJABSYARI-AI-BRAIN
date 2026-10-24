"""Render Day 17 carousel, Stories, and QA previews.

Run: python CONTENT/DAY-17/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "earth-tone-five-looks.jpg"

CW, CH = 1080, 1350
SW, SH = 1080, 1920
PAPER = (250, 247, 241)
CREAM = (244, 237, 228)
DARK = (48, 41, 37)
MUTED = (103, 91, 84)
LINE = (210, 195, 181)
CAMEL = (170, 126, 82)
TAUPE = (145, 127, 113)
TERRACOTTA = (167, 87, 62)
SAND = (216, 190, 155)
MOCHA = (115, 88, 72)
SAGE = (119, 123, 91)
CHOCOLATE = (78, 52, 42)
OLIVE = (111, 114, 75)
WHITE = (255, 255, 255)
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LOOKS = [
    ("OATMEAL + CAMEL", CAMEL, "light & warm",
     "Outfit terang menjaga look terasa ringan. Camel menambah kehangatan tanpa kontras yang terlalu tajam.",
     ["ringan", "hangat", "low contrast"]),
    ("OLIVE + WARM TAUPE", TAUPE, "grounded neutral",
     "Olive memberi warna utama yang muted. Warm taupe menjaga palet tetap tenang dan earthy.",
     ["muted", "tenang", "grounded"]),
    ("TERRACOTTA + SAND", TERRACOTTA, "warm accent",
     "Terracotta menjadi aksen hangat. Sand yang lebih terang memberi ruang dan keseimbangan visual.",
     ["hangat", "berwarna", "seimbang"]),
    ("MOCHA + SOFT CREAM", MOCHA, "tonal contrast",
     "Mocha memberi dasar medium–deep. Soft cream membuat kontras terang yang tetap hangat.",
     ["tonal", "clean", "medium contrast"]),
    ("CHOCOLATE + MUTED SAGE", SAGE, "deep earthy",
     "Chocolate menjadi dasar yang dalam. Muted sage menambah warna lembut tanpa memutus nuansa earthy.",
     ["deep", "earthy", "soft color"]),
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
    draw.text((64, h - 45), "@hijabsyaricoid", font=font(SANS, 22),
              fill=PAPER if light else MUTED, anchor="ls")


def panel(index):
    src = Image.open(SOURCE).convert("RGB")
    pw = src.width / 5
    pad = 4
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
    im.paste(strip((CW, 700)), (0, 650))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.rectangle((0, 0, CW, 760), fill=(*PAPER, 238))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    text_block(d, "5 kombinasi earth tone yang nggak terasa monoton.",
               (64, 88), font(SERIF_BOLD, 68), DARK, 930, 80)
    rounded(d, (64, 430, 872, 534), radius=48, fill=CREAM, outline=LINE)
    d.text((104, 461), "Light · grounded · warm · tonal · deep",
           font=font(SANS_BOLD, 27), fill=DARK)
    footer(d, light=True)
    return im


def overview():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Pilih arah paletnya dulu", (64, 76), font(SERIF_BOLD, 60), DARK, 900, 72)
    y = 250
    for i, (name, color, lead, _, _) in enumerate(LOOKS, 1):
        rounded(d, (64, y, 1016, y + 154), radius=30, fill=PAPER, outline=LINE)
        d.rounded_rectangle((92, y + 28, 222, y + 126), radius=24, fill=color)
        d.text((157, y + 77), f"{i:02d}", font=font(SANS_BOLD, 26),
               fill=PAPER if i != 4 else DARK, anchor="mm")
        d.text((254, y + 34), name, font=font(SANS_BOLD, 26), fill=DARK)
        d.text((254, y + 83), lead, font=font(SANS, 25), fill=MUTED)
        y += 174
    d.text((64, 1168), "Referensi visual—bukan aturan warna universal.",
           font=font(SANS, 23), fill=MUTED)
    footer(d)
    return im


def look_slide(index):
    name, color, lead, body, tags = LOOKS[index]
    im = Image.new("RGB", (CW, CH), PAPER)
    portrait = ImageOps.fit(panel(index), (520, 1120), Image.Resampling.LANCZOS, centering=(.5, .42))
    im.paste(portrait, (560, 105))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.rectangle((0, 0, 620, CH), fill=(*PAPER, 247))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    rounded(d, (64, 84, 326, 150), radius=30, fill=color)
    d.text((195, 117), f"{index+1:02d}  {name.split(' + ')[0]}",
           font=font(SANS_BOLD, 20), fill=PAPER if index != 3 else DARK, anchor="mm")
    text_block(d, name.replace(" + ", " +\n"), (64, 210),
               font(SERIF_BOLD, 53), DARK, 470, 64)
    d.text((64, 372), lead, font=font(SANS_BOLD, 28), fill=color)
    y = text_block(d, body, (64, 444), font(SANS, 28), DARK, 450, 43)
    d.line((64, y + 26, 510, y + 26), fill=LINE, width=2)
    for i, tag in enumerate(tags):
        yy = y + 80 + i * 75
        d.ellipse((64, yy + 8, 84, yy + 28), fill=color)
        d.text((108, yy), tag, font=font(SANS_BOLD, 24), fill=MUTED)
    d.text((64, 1176), "Cek lagi di cahaya alami.", font=font(SANS, 22), fill=MUTED)
    footer(d)
    return im


def chooser():
    im = Image.new("RGB", (CW, CH), (224, 211, 191))
    d = ImageDraw.Draw(im)
    text_block(d, "Pilih lewat 3 pertanyaan", (64, 82), font(SERIF_BOLD, 62), DARK, 920, 74)
    cards = [
        ("01", "Mau kontras light,", "medium, atau deep?"),
        ("02", "Mau netral dominan", "atau satu aksen warna?"),
        ("03", "Warna mana yang", "sudah ada di lemari?"),
    ]
    y = 340
    for num, a, b in cards:
        rounded(d, (64, y, 1016, y + 210), radius=36, fill=PAPER, outline=LINE)
        d.ellipse((96, y + 64, 178, y + 146), fill=CHOCOLATE)
        d.text((137, y + 105), num, font=font(SANS_BOLD, 24), fill=PAPER, anchor="mm")
        d.text((218, y + 52), a, font=font(SANS_BOLD, 31), fill=DARK)
        d.text((218, y + 108), b, font=font(SANS, 29), fill=MUTED)
        y += 236
    rounded(d, (64, 1075, 1016, 1208), radius=32, fill=CHOCOLATE)
    d.text((540, 1121), "Simpan paletnya, lalu cek di cahaya alami.",
           font=font(SANS_BOLD, 27), fill=PAPER, anchor="mm")
    d.text((540, 1165), "Nomor berapa yang ingin kamu coba?",
           font=font(SANS, 24), fill=PAPER, anchor="mm")
    footer(d)
    return im


def story_one():
    im = Image.new("RGB", (SW, SH), PAPER)
    im.paste(strip((SW, 1020)), (0, 900))
    d = ImageDraw.Draw(im)
    text_block(d, "Earth tone kamu lebih sering…", (72, 150),
               font(SERIF_BOLD, 70), DARK, 920, 84)
    d.text((72, 382), "Light atau deep?", font=font(SANS_BOLD, 36), fill=MUTED)
    rounded(d, (72, 540, 1008, 810), radius=40, fill=CREAM, outline=LINE)
    d.text((540, 615), "RUANG POLL INSTAGRAM", font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
    d.text((540, 716), "LIGHT   /   DEEP", font=font(SANS_BOLD, 38), fill=DARK, anchor="mm")
    footer(d, SH, light=True)
    return im


def story_two():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Pilih satu kombinasi", (72, 150), font(SERIF_BOLD, 72), DARK, 920, 86)
    a = ImageOps.fit(panel(0), (430, 920), Image.Resampling.LANCZOS, centering=(.5, .42))
    b = ImageOps.fit(panel(4), (430, 920), Image.Resampling.LANCZOS, centering=(.5, .42))
    im.paste(a, (72, 410))
    im.paste(b, (578, 410))
    d = ImageDraw.Draw(im)
    rounded(d, (92, 1250, 482, 1335), radius=40, fill=CAMEL)
    d.text((287, 1292), "A — LIGHT", font=font(SANS_BOLD, 27), fill=PAPER, anchor="mm")
    rounded(d, (598, 1250, 988, 1335), radius=40, fill=CHOCOLATE)
    d.text((793, 1292), "B — DEEP", font=font(SANS_BOLD, 27), fill=PAPER, anchor="mm")
    rounded(d, (72, 1465, 1008, 1740), radius=40, fill=PAPER, outline=LINE)
    d.text((540, 1542), "RUANG POLL INSTAGRAM", font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
    d.text((540, 1650), "A — LIGHT   /   B — DEEP", font=font(SANS_BOLD, 34), fill=DARK, anchor="mm")
    footer(d, SH)
    return im


def story_three():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Nomor berapa yang ingin kamu coba?", (72, 150),
               font(SERIF_BOLD, 70), DARK, 920, 84)
    x = 72
    for i, (_, color, _, _, _) in enumerate(LOOKS, 1):
        d.rounded_rectangle((x, 520, x + 164, 670), radius=30, fill=color, outline=LINE)
        d.text((x + 82, 595), str(i), font=font(SANS_BOLD, 38),
               fill=PAPER if i != 4 else DARK, anchor="mm")
        x += 184
    rounded(d, (72, 850, 1008, 1230), radius=42, fill=PAPER, outline=LINE)
    d.text((540, 946), "RUANG QUESTIONS STICKER", font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
    d.text((540, 1080), "1, 2, 3, 4, atau 5?", font=font(SANS_BOLD, 38), fill=DARK, anchor="mm")
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


def sheet(images, path, cols, thumb):
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows + 54), WHITE)
    d = ImageDraw.Draw(canvas)
    d.text((20, 12), "DAY 17 — QA PREVIEW", font=font(SANS_BOLD, 24), fill=DARK)
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
    sheet(slides, ASSETS / "contact-sheet.png", 4, (270, 338))
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480))


if __name__ == "__main__":
    main()
