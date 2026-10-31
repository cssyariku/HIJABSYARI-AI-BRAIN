"""Render Day 25 carousel, Stories, and QA previews.

Run: python CONTENT/DAY-25/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "material-five-panel.png"

CW, CH = 1080, 1350
SW, SH = 1080, 1920
PAPER = (249, 245, 239)
CREAM = (237, 226, 211)
DARK = (53, 43, 38)
MUTED = (108, 91, 82)
LINE = (214, 197, 183)
TAUPE = (151, 126, 111)
SAND = (221, 204, 185)
ROSE = (185, 145, 137)
OLIVE = (128, 126, 96)
BLUE = (111, 128, 145)
WHITE = (255, 255, 255)
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

MATERIALS = [
    ("VOAL-LIKE", "matte & structured", TAUPE,
     "Mudah memberi garis yang lebih tegas. Cek komposisi, ketebalan, dan opasitas produk aslinya.",
     ["struktur", "finishing matte", "cek opasitas"]),
    ("CHIFFON-LIKE", "light & flowy", ROSE,
     "Drape ringan dan bergerak lembut. Cek kebutuhan inner, coverage, dan titik anchor.",
     ["ringan", "drape lembut", "cek coverage"]),
    ("JERSEY", "soft & stretch", OLIVE,
     "Knit yang lentur mengikuti styling. Cek recovery, bobot, dan rasa saat dipakai.",
     ["stretch", "soft drape", "cek recovery"]),
    ("SATIN-SURFACE", "smooth & luminous", BLUE,
     "Permukaan berkilau memberi aksen dressy. Cek tingkat licin dan petunjuk perawatan.",
     ["sheen", "smooth", "cek grip"]),
    ("TEXTURED CREPE", "textured & drapey", SAND,
     "Tekstur membantu tampilan lebih berdimensi. Cek komposisi, bobot, dan rasa di kulit.",
     ["tekstur", "soft weight", "cek label"]),
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
    pad = 3
    left = round(index * pw) + (pad if index else 0)
    right = round((index + 1) * pw) - (pad if index < 4 else 0)
    return src.crop((left, 0, right, src.height))


def strip(size):
    out = Image.new("RGB", size, PAPER)
    gap = 6
    cell = (size[0] - gap * 4) // 5
    for i in range(5):
        pic = ImageOps.fit(panel(i), (cell, size[1]), Image.Resampling.LANCZOS,
                           centering=(.5, .47))
        out.paste(pic, (i * (cell + gap), 0))
    return out


def cover():
    im = Image.new("RGB", (CW, CH), PAPER)
    im.paste(strip((CW, 655)), (0, 695))
    d = ImageDraw.Draw(im)
    text_block(d, "Pilih bahan hijab sesuai kebutuhan", (64, 84),
               font(SERIF_BOLD, 68), DARK, 930, 79)
    d.text((64, 330), "Mulai dari 5 karakter ini.", font=font(SANS_BOLD, 33), fill=TAUPE)
    rounded(d, (64, 430, 910, 548), radius=46, fill=CREAM, outline=LINE)
    d.text((487, 488), "struktur · drape · stretch · sheen · tekstur",
           font=font(SANS_BOLD, 24), fill=DARK, anchor="mm")
    footer(d, light=True)
    return im


def framework():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Nama bahan belum cukup", (64, 80), font(SERIF_BOLD, 62), DARK, 930, 75)
    d.text((64, 250), "Bandingkan karakter yang benar-benar kamu butuhkan:",
           font=font(SANS, 27), fill=MUTED)
    cards = [
        ("01", "STRUKTUR", "Tegas atau mudah dibentuk?"),
        ("02", "DRAPE", "Jatuh ringan atau lebih berbobot?"),
        ("03", "STRETCH", "Lentur atau stabil?"),
        ("04", "SHEEN", "Matte atau ada kilau?"),
        ("05", "COVERAGE", "Opaque, perlu inner, atau berlapis?"),
    ]
    y = 355
    for num, title, body in cards:
        rounded(d, (64, y, 1016, y + 150), radius=30, fill=PAPER, outline=LINE)
        d.ellipse((92, y + 34, 174, y + 116), fill=TAUPE)
        d.text((133, y + 75), num, font=font(SANS_BOLD, 23), fill=PAPER, anchor="mm")
        d.text((210, y + 27), title, font=font(SANS_BOLD, 25), fill=DARK)
        d.text((210, y + 79), body, font=font(SANS, 24), fill=MUTED)
        y += 166
    d.text((64, 1212), "Lalu cek komposisi dan care label produk.",
           font=font(SANS_BOLD, 24), fill=TAUPE)
    footer(d)
    return im


def material_slide(index):
    name, lead, color, body, tags = MATERIALS[index]
    im = Image.new("RGB", (CW, CH), PAPER)
    portrait = ImageOps.fit(panel(index), (540, 1120), Image.Resampling.LANCZOS,
                            centering=(.5, .47))
    im.paste(portrait, (540, 110))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rectangle((0, 0, 620, CH), fill=(*PAPER, 249))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    text_block(d, name.replace("-", " "), (64, 92), font(SERIF_BOLD, 49), DARK, 450, 58)
    rounded(d, (64, 245, 450, 316), radius=32, fill=color)
    d.text((257, 280), lead, font=font(SANS_BOLD, 24), fill=PAPER, anchor="mm")
    y = text_block(d, body, (64, 385), font(SANS, 27), DARK, 450, 42)
    d.line((64, y + 24, 500, y + 24), fill=LINE, width=2)
    for i, tag in enumerate(tags):
        yy = y + 78 + i * 72
        d.ellipse((64, yy + 8, 84, yy + 28), fill=color)
        d.text((108, yy), tag, font=font(SANS_BOLD, 22), fill=MUTED)
    d.text((64, 1168), "Karakter dapat berbeda antarproduk.", font=font(SANS, 21), fill=MUTED)
    footer(d)
    return im


def chooser():
    im = Image.new("RGB", (CW, CH), (229, 217, 202))
    d = ImageDraw.Draw(im)
    text_block(d, "Sebelum checkout, jawab 4 hal", (64, 80), font(SERIF_BOLD, 60), DARK, 930, 73)
    cards = [
        ("01", "Dipakai untuk aktivitas apa?"),
        ("02", "Mau struktur atau drape lembut?"),
        ("03", "Perlu coverage tanpa banyak layer?"),
        ("04", "Siap dengan cara perawatannya?"),
    ]
    y = 340
    for num, body in cards:
        rounded(d, (64, y, 1016, y + 164), radius=34, fill=PAPER, outline=LINE)
        d.ellipse((94, y + 41, 176, y + 123), fill=TAUPE)
        d.text((135, y + 82), num, font=font(SANS_BOLD, 23), fill=PAPER, anchor="mm")
        text_block(d, body, (215, y + 46), font(SANS_BOLD, 28), DARK, 735, 39)
        y += 184
    rounded(d, (64, 1094, 1016, 1214), radius=34, fill=DARK)
    d.text((540, 1137), "Simpan checklist ini.", font=font(SANS_BOLD, 29), fill=PAPER, anchor="mm")
    d.text((540, 1178), "Kamu paling nyaman pakai bahan apa?", font=font(SANS, 24), fill=PAPER, anchor="mm")
    footer(d)
    return im


def story_one():
    im = Image.new("RGB", (SW, SH), PAPER)
    im.paste(strip((SW, 1000)), (0, 920))
    d = ImageDraw.Draw(im)
    text_block(d, "Pilih bahan hijab dari kebutuhannya", (72, 145),
               font(SERIF_BOLD, 69), DARK, 930, 82)
    d.text((72, 420), "Bukan dari nama bahan saja.", font=font(SANS_BOLD, 32), fill=TAUPE)
    rounded(d, (72, 560, 1008, 790), radius=42, fill=CREAM, outline=LINE)
    d.text((540, 625), "Lihat 5 karakter:", font=font(SANS, 27), fill=MUTED, anchor="mm")
    d.text((540, 704), "struktur · drape · stretch · sheen · tekstur",
           font=font(SANS_BOLD, 25), fill=DARK, anchor="mm")
    footer(d, SH, light=True)
    return im


def story_two():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Kamu lebih sering cari yang mana?", (72, 145),
               font(SERIF_BOLD, 67), DARK, 930, 82)
    a = ImageOps.fit(panel(0), (430, 900), Image.Resampling.LANCZOS, centering=(.5, .47))
    b = ImageOps.fit(panel(1), (430, 900), Image.Resampling.LANCZOS, centering=(.5, .47))
    im.paste(a, (72, 430)); im.paste(b, (578, 430))
    d = ImageDraw.Draw(im)
    rounded(d, (92, 1250, 482, 1338), radius=40, fill=TAUPE)
    d.text((287, 1294), "STRUCTURED", font=font(SANS_BOLD, 27), fill=PAPER, anchor="mm")
    rounded(d, (598, 1250, 988, 1338), radius=40, fill=ROSE)
    d.text((793, 1294), "FLOWY", font=font(SANS_BOLD, 27), fill=PAPER, anchor="mm")
    rounded(d, (72, 1480, 1008, 1750), radius=42, fill=PAPER, outline=LINE)
    d.text((540, 1570), "Tambahkan Poll native ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 1665), "STRUCTURED / FLOWY", font=font(SANS_BOLD, 31), fill=DARK, anchor="mm")
    footer(d, SH)
    return im


def story_three():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Ceritakan kebutuhanmu", (72, 145), font(SERIF_BOLD, 70), DARK, 930, 84)
    d.text((72, 390), "Aktivitas + karakter bahan yang dicari", font=font(SANS_BOLD, 29), fill=TAUPE)
    rounded(d, (72, 600, 1008, 1110), radius=48, fill=PAPER, outline=LINE)
    d.text((540, 715), "Tambahkan Questions native ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 875), "Contoh:", font=font(SANS, 28), fill=MUTED, anchor="mm")
    d.text((540, 955), "\"Kantor + matte, mudah dibentuk\"", font=font(SANS_BOLD, 30), fill=DARK, anchor="mm")
    d.text((72, 1400), "Jawabanmu membantu panduan bahan berikutnya.",
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
    slides = [cover(), framework()] + [material_slide(i) for i in range(5)] + [chooser()]
    for i, im in enumerate(slides, 1):
        save_png(im, ASSETS / f"carousel-{i:02d}.png")
    stories = [story_one(), story_two(), story_three()]
    for i, im in enumerate(stories, 1):
        save_png(im, ASSETS / f"story-{i:02d}.png")
    sheet(slides, ASSETS / "contact-sheet.png", 4, (270, 338), "DAY 25 — CAROUSEL QA")
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480), "DAY 25 — STORIES QA")


if __name__ == "__main__":
    main()
