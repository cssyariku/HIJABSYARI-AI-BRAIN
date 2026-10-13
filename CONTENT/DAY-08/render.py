"""Render Day 8 carousel and Stories: python CONTENT/DAY-08/render.py"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"
PHOTO_SOURCE = ASSETS / "sage-five-looks.png"

W, H = 1080, 1350
PAPER = (250, 247, 241)
CREAM = (243, 237, 226)
DARK = (48, 43, 40)
MUTED = (107, 97, 89)
LINE = (207, 193, 180)
SAGE = (142, 151, 126)
SOFT_CREAM = (231, 222, 205)
TAUPE = (166, 145, 128)
ROSE = (186, 137, 140)
BURGUNDY = (109, 46, 53)
CHARCOAL = (66, 65, 66)
PALE = (233, 223, 211)

FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LOOKS = [
    ("SOFT CREAM", SOFT_CREAM, "low contrast", ["ringan", "clean", "lembut"],
     "Memberi arah yang ringan dan dekat dengan warna netral terang."),
    ("WARM TAUPE", TAUPE, "earthy neutral", ["tenang", "earthy", "mudah dipakai"],
     "Menjaga palet tetap earthy tanpa menyatu sepenuhnya dengan sage."),
    ("DUSTY ROSE", ROSE, "soft accent", ["feminin", "muted", "warna lembut"],
     "Menambah aksen warna yang tetap kalem karena sama-sama muted."),
    ("BURGUNDY", BURGUNDY, "deep contrast", ["dalam", "tegas", "rich"],
     "Membuat kontras lebih dalam dan memberi titik fokus yang kuat."),
    ("CHARCOAL", CHARCOAL, "grounded neutral", ["netral gelap", "modern", "grounded"],
     "Memberi netral gelap yang terasa modern tanpa kembali ke hitam pekat."),
]


def f(path, size):
    return ImageFont.truetype(path, size)


def logo(width=275, light=False):
    src = Image.open(LOGO_SOURCE).convert("RGBA")
    src = src.crop(src.getchannel("A").getbbox())
    color = PAPER if light else DARK
    out = Image.new("RGBA", src.size, color + (0,))
    out.putalpha(src.getchannel("A"))
    return out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)


def masthead(im, light=False):
    mark = logo(light=light)
    im.paste(mark, (76, 38), mark)
    d = ImageDraw.Draw(im)
    d.line((76, 148, 1004, 148), fill=PALE if light else LINE, width=2)


def save(im, name):
    out = im.convert("RGB")
    out.load()
    out.save(ASSETS / name, compress_level=6)


def lines(draw, rows, xy, face, fill, leading):
    x, y = xy
    for row in rows:
        draw.text((x, y), row, font=face, fill=fill)
        y += leading
    return y


def wrap(draw, text, face, width):
    words, rows, row = text.split(), [], ""
    for word in words:
        trial = f"{row} {word}".strip()
        if draw.textbbox((0, 0), trial, font=face)[2] <= width:
            row = trial
        else:
            rows.append(row)
            row = word
    if row:
        rows.append(row)
    return rows


def paragraph(draw, text, xy, face, fill, width, leading):
    return lines(draw, wrap(draw, text, face, width), xy, face, fill, leading)


def panel(index):
    with Image.open(PHOTO_SOURCE) as opened:
        src = opened.convert("RGB")
        src.load()
        pw = src.width / 5
        left = round(index * pw + (4 if index else 0))
        right = round((index + 1) * pw - (4 if index < 4 else 0))
        return src.crop((left, 0, right, src.height)).copy()


def panel_strip(size=(928, 505)):
    out = Image.new("RGB", size, PAPER)
    gap = 6
    cell_w = (size[0] - gap * 4) // 5
    for i in range(5):
        pic = ImageOps.fit(panel(i), (cell_w, size[1]), Image.Resampling.LANCZOS, centering=(0.5, 0.48))
        out.paste(pic, (i * (cell_w + gap), 0))
    return out


def base(bg=CREAM, light=False):
    im = Image.new("RGB", (W, H), bg).convert("RGBA")
    masthead(im, light=light)
    return im


def cover():
    im = base(PAPER)
    d = ImageDraw.Draw(im)
    lines(d, ["Outfit sage +", "hijab apa?"], (76, 220), f(FONT_SERIF_BOLD, 74), DARK, 88)
    d.rounded_rectangle((76, 420, 830, 510), radius=44, fill=SAGE)
    d.text((112, 446), "5 arah warna untuk dicoba.", font=f(FONT_SANS_BOLD, 31), fill=PAPER)
    strip = panel_strip((928, 650))
    im.paste(strip, (76, 590))
    d = ImageDraw.Draw(im)
    d.text((76, 1265), "Satu outfit, lima efek visual →", font=f(FONT_SANS_BOLD, 25), fill=MUTED)
    save(im, "01-cover.png")


def overview():
    im = base()
    d = ImageDraw.Draw(im)
    lines(d, ["Mulai dari arah", "yang kamu mau."], (76, 225), f(FONT_SERIF_BOLD, 62), DARK, 74)
    for i, (name, color, lead, _, _) in enumerate(LOOKS):
        y = 485 + i * 145
        d.rounded_rectangle((76, y, 1004, y+112), radius=24, fill=PAPER, outline=LINE, width=2)
        d.rounded_rectangle((104, y+24, 184, y+88), radius=20, fill=color, outline=LINE, width=1)
        d.text((220, y+22), name, font=f(FONT_SANS_BOLD, 26), fill=DARK)
        d.text((220, y+64), lead, font=f(FONT_SANS, 23), fill=MUTED)
    d.text((76, 1230), "Efek ini observasi visual, bukan aturan undertone.", font=f(FONT_SANS, 22), fill=MUTED)
    save(im, "02-palette.png")


def look_slide(index, filename):
    name, color, lead, tags, body = LOOKS[index]
    im = Image.new("RGB", (W, H), PAPER).convert("RGBA")
    portrait = ImageOps.fit(panel(index), (480, 1030), Image.Resampling.LANCZOS, centering=(0.5, 0.45))
    im.paste(portrait, (600, 160))
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 650, H), fill=(*PAPER, 248))
    im = Image.alpha_composite(im, overlay)
    masthead(im)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((76, 225, 292, 278), radius=26, fill=color)
    label_color = DARK if index == 0 else PAPER
    d.text((105, 238), f"0{index+1}  {name}", font=f(FONT_SANS_BOLD, 20), fill=label_color)
    lines(d, lead.split(" / ") if " / " in lead else [lead], (76, 350), f(FONT_SERIF_BOLD, 55), DARK, 66)
    y = paragraph(d, body, (76, 475), f(FONT_SANS, 29), DARK, 470, 46)
    d.line((76, y+36, 530, y+36), fill=LINE, width=2)
    for i, tag in enumerate(tags):
        yy = y + 92 + i * 82
        d.ellipse((76, yy+8, 94, yy+26), fill=color)
        d.text((116, yy), tag, font=f(FONT_SANS_BOLD, 25), fill=MUTED)
    d.text((76, 1225), "Bandingkan lagi di cahaya alami.", font=f(FONT_SANS, 22), fill=MUTED)
    save(im, filename)


def chooser():
    im = base(SAGE)
    d = ImageDraw.Draw(im)
    lines(d, ["Pilih lewat", "3 pertanyaan."], (76, 225), f(FONT_SERIF_BOLD, 66), DARK, 79)
    cards = [
        ("01", "Mau kontras rendah", "atau lebih dalam?"),
        ("02", "Mau tetap netral", "atau tambah warna?"),
        ("03", "Dipakai daily", "atau acara tertentu?"),
    ]
    for i, (num, a, b) in enumerate(cards):
        y = 510 + i * 205
        d.rounded_rectangle((76, y, 1004, y+160), radius=28, fill=(*PAPER, 235), outline=LINE, width=2)
        d.text((112, y+36), num, font=f(FONT_SANS_BOLD, 24), fill=BURGUNDY)
        d.text((190, y+28), a, font=f(FONT_SANS_BOLD, 29), fill=DARK)
        d.text((190, y+78), b, font=f(FONT_SANS, 27), fill=MUTED)
    d.text((76, 1165), "Simpan paletnya, lalu cek kain asli dan pencahayaan.", font=f(FONT_SANS_BOLD, 25), fill=DARK)
    d.text((76, 1215), "Kamu paling suka nomor berapa?", font=f(FONT_SANS, 24), fill=DARK)
    save(im, "08-choose.png")


def story_poll():
    strip = panel_strip((1080, 960))
    im = Image.new("RGB", (1080, 1920), PAPER).convert("RGBA")
    im.paste(strip, (0, 720))
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Outfit sage +", "hijab apa?"], (76, 300), f(FONT_SERIF_BOLD, 78), DARK, 92)
    d.text((76, 525), "Lima arah warna, lima efek visual.", font=f(FONT_SANS, 31), fill=MUTED)
    d.rounded_rectangle((76, 1560, 1004, 1805), radius=30, fill=(*PAPER, 235), outline=LINE, width=3)
    d.text((112, 1620), "Tambahkan Poll:", font=f(FONT_SANS_BOLD, 27), fill=MUTED)
    d.text((112, 1683), "LIGHT / DEEP", font=f(FONT_SANS_BOLD, 32), fill=DARK)
    save(im, "story-01-poll.png")


def story_compare():
    im = Image.new("RGB", (1080, 1920), CREAM).convert("RGBA")
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Kontras rendah", "atau lebih dalam?"], (76, 300), f(FONT_SERIF_BOLD, 72), DARK, 86)
    a = ImageOps.fit(panel(0), (430, 800), Image.Resampling.LANCZOS, centering=(0.5, 0.45))
    b = ImageOps.fit(panel(3), (430, 800), Image.Resampling.LANCZOS, centering=(0.5, 0.45))
    im.paste(a, (76, 685))
    im.paste(b, (574, 685))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((95, 1390, 475, 1460), radius=35, fill=SOFT_CREAM, outline=LINE, width=2)
    d.text((285, 1425), "SOFT CREAM", font=f(FONT_SANS_BOLD, 23), fill=DARK, anchor="mm")
    d.rounded_rectangle((593, 1390, 973, 1460), radius=35, fill=BURGUNDY)
    d.text((783, 1425), "BURGUNDY", font=f(FONT_SANS_BOLD, 23), fill=PAPER, anchor="mm")
    d.rounded_rectangle((76, 1570, 1004, 1810), radius=30, fill=PAPER, outline=LINE, width=3)
    d.text((112, 1632), "Tambahkan Poll:", font=f(FONT_SANS_BOLD, 27), fill=MUTED)
    d.text((112, 1695), "CREAM / BURGUNDY", font=f(FONT_SANS_BOLD, 30), fill=DARK)
    save(im, "story-02-contrast.png")


def story_question():
    im = Image.new("RGB", (1080, 1920), CREAM).convert("RGBA")
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Nomor berapa", "yang paling ingin", "kamu coba?"], (76, 340), f(FONT_SERIF_BOLD, 76), DARK, 90)
    x = 76
    for i, (_, color, _, _, _) in enumerate(LOOKS):
        d.rounded_rectangle((x, 760, x+154, 890), radius=28, fill=color, outline=LINE, width=2)
        d.text((x+77, 825), str(i+1), font=f(FONT_SANS_BOLD, 34), fill=DARK if i==0 else PAPER, anchor="mm")
        x += 182
    d.rounded_rectangle((76, 1160, 1004, 1550), radius=32, fill=PAPER, outline=LINE, width=3)
    d.text((116, 1230), "Tambahkan Questions:", font=f(FONT_SANS_BOLD, 27), fill=MUTED)
    d.text((116, 1300), "1, 2, 3, 4, atau 5?", font=f(FONT_SANS, 32), fill=DARK)
    d.text((76, 1740), "Jawabanmu membantu Color Lab berikutnya.", font=f(FONT_SANS_BOLD, 25), fill=MUTED)
    save(im, "story-03-question.png")


def contact_sheet():
    names = ["01-cover.png", "02-palette.png", "03-soft-cream.png", "04-warm-taupe.png", "05-dusty-rose.png", "06-burgundy.png", "07-charcoal.png", "08-choose.png"]
    sheet = Image.new("RGB", (1160, 760), PAPER)
    d = ImageDraw.Draw(sheet)
    d.text((40, 24), "DAY 08 — Carousel preview", font=f(FONT_SANS_BOLD, 28), fill=DARK)
    for i, name in enumerate(names):
        with Image.open(ASSETS / name) as opened:
            pic = opened.convert("RGB")
            pic.load()
        pic.thumbnail((250, 313), Image.Resampling.LANCZOS)
        x, y = 40 + (i % 4) * 280, 78 + (i // 4) * 332
        sheet.paste(pic, (x, y))
    sheet.save(ASSETS / "contact-sheet.png", optimize=True)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    cover()
    overview()
    for i, name in enumerate(["03-soft-cream.png", "04-warm-taupe.png", "05-dusty-rose.png", "06-burgundy.png", "07-charcoal.png"]):
        look_slide(i, name)
    chooser()
    story_poll()
    story_compare()
    story_question()
    contact_sheet()
