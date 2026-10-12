"""Render Day 7 carousel and Stories: python CONTENT/DAY-07/render.py"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"
PHOTO_SOURCE = ASSETS / "voal-chiffon-diptych.png"

W, H = 1080, 1350
PAPER = (250, 247, 241)
CREAM = (242, 235, 225)
DARK = (49, 43, 40)
MUTED = (108, 96, 89)
LINE = (207, 191, 178)
VOAL = (146, 119, 103)
CHIFFON = (169, 137, 127)
DEEP = (99, 76, 67)
PALE = (232, 219, 207)

FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def logo(width=275, light=False):
    src = Image.open(LOGO_SOURCE).convert("RGBA")
    src = src.crop(src.getchannel("A").getbbox())
    color = PAPER if light else DARK
    out = Image.new("RGBA", src.size, color + (0,))
    out.putalpha(src.getchannel("A"))
    return out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)


def masthead(im, light=False, line=True):
    mark = logo(light=light)
    im.paste(mark, (76, 38), mark)
    if line:
        d = ImageDraw.Draw(im)
        d.line((76, 148, 1004, 148), fill=PALE if light else LINE, width=2)


def save(im, name):
    im.convert("RGB").save(ASSETS / name, optimize=True)


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


def photo_panel(side, size):
    src = Image.open(PHOTO_SOURCE).convert("RGB")
    mid = src.width // 2
    box = (0, 0, mid - 4, src.height) if side == "left" else (mid + 4, 0, src.width, src.height)
    return ImageOps.fit(src.crop(box), size, Image.Resampling.LANCZOS, centering=(0.5, 0.48))


def base(bg=CREAM, light=False):
    im = Image.new("RGB", (W, H), bg).convert("RGBA")
    masthead(im, light=light)
    return im


def cover():
    src = Image.open(PHOTO_SOURCE).convert("RGB")
    im = ImageOps.fit(src, (W, H), Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")
    wash = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wash)
    wd.rectangle((0, 0, W, 630), fill=(*PAPER, 235))
    wd.rectangle((0, 1080, W, H), fill=(*DARK, 118))
    im = Image.alpha_composite(im, wash)
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Voal atau", "chiffon?"], (76, 245), f(FONT_SERIF_BOLD, 82), DARK, 94)
    d.rounded_rectangle((76, 470, 916, 565), radius=46, fill=(*PAPER, 235))
    d.text((112, 497), "Tergantung kebutuhanmu.", font=f(FONT_SANS_BOLD, 35), fill=DARK)
    d.text((76, 1215), "Geser untuk pilih dengan lebih sadar →", font=f(FONT_SANS_BOLD, 28), fill=PAPER)
    save(im, "01-cover.png")


def split_summary():
    im = base()
    d = ImageDraw.Draw(im)
    lines(d, ["Bedanya bukan", "cuma ‘vibe’."], (76, 225), f(FONT_SERIF_BOLD, 61), DARK, 73)
    cards = [(76, 465, 510, 1120, "VOAL", VOAL, "lebih tegas", ["matte", "framing rapi", "lebih mudah dikontrol"]),
             (570, 465, 1004, 1120, "CHIFFON", CHIFFON, "lebih fluid", ["ringan", "jatuh lembut", "sering perlu grip"])]
    for x0, y0, x1, y1, name, color, lead, bullets in cards:
        d.rounded_rectangle((x0, y0, x1, y1), radius=30, fill=PAPER, outline=LINE, width=3)
        d.rounded_rectangle((x0+28, y0+28, x0+175, y0+76), radius=23, fill=color)
        d.text((x0+50, y0+40), name, font=f(FONT_SANS_BOLD, 20), fill=PAPER)
        d.text((x0+28, y0+130), lead, font=f(FONT_SERIF_BOLD, 38), fill=DARK)
        for i, item in enumerate(bullets):
            y = y0 + 250 + i * 106
            d.ellipse((x0+30, y+8, x0+48, y+26), fill=color)
            d.text((x0+68, y), item, font=f(FONT_SANS, 28), fill=DARK)
        d.text((x0+28, y1-88), "umumnya*", font=f(FONT_SANS_BOLD, 20), fill=MUTED)
    d.text((76, 1190), "*Komposisi, ketebalan, dan finishing bisa mengubah hasil.", font=f(FONT_SANS, 23), fill=MUTED)
    save(im, "02-summary.png")


def material_slide(side, name, title, body, notes, filename, color):
    im = Image.new("RGB", (W, H), PAPER).convert("RGBA")
    photo = photo_panel(side, (455, 1030))
    im.paste(photo, (625, 160))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 690, H), fill=(*PAPER, 248))
    im = Image.alpha_composite(im, overlay)
    masthead(im)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((76, 225, 250, 276), radius=25, fill=color)
    d.text((104, 237), name, font=f(FONT_SANS_BOLD, 22), fill=PAPER)
    y = lines(d, title, (76, 325), f(FONT_SERIF_BOLD, 55), DARK, 66)
    y = paragraph(d, body, (76, y+28), f(FONT_SANS, 27), DARK, 520, 43)
    d.line((76, y+35, 540, y+35), fill=LINE, width=2)
    for i, note in enumerate(notes):
        yy = y + 80 + i * 84
        d.ellipse((76, yy+8, 94, yy+26), fill=color)
        paragraph(d, note, (116, yy), f(FONT_SANS_BOLD, 23), MUTED, 430, 34)
    d.text((76, 1225), "Bukan aturan mutlak—cek kain aslinya.", font=f(FONT_SANS, 22), fill=MUTED)
    save(im, filename)


def choose_slide():
    im = base()
    d = ImageDraw.Draw(im)
    lines(d, ["Pilih dari situasi,", "bukan nama bahan."], (76, 225), f(FONT_SERIF_BOLD, 60), DARK, 72)
    rows = [
        ("Styling cepat & framing rapi", "mulai dari voal", VOAL),
        ("Look fluid atau acara", "mulai dari chiffon", CHIFFON),
        ("Prioritas tidak menerawang", "tes di cahaya kuat", DEEP),
        ("Mudah bergeser di wajah", "cek grip + inner", VOAL),
    ]
    for i, (need, answer, color) in enumerate(rows):
        y = 510 + i * 165
        d.rounded_rectangle((76, y, 1004, y+130), radius=25, fill=PAPER, outline=LINE, width=2)
        d.ellipse((108, y+42, 150, y+84), fill=color)
        d.text((184, y+27), need, font=f(FONT_SANS_BOLD, 27), fill=DARK)
        d.text((184, y+76), answer, font=f(FONT_SANS, 25), fill=MUTED)
    save(im, "05-choose.png")


def not_from_name():
    im = base(DEEP, light=True)
    d = ImageDraw.Draw(im)
    lines(d, ["‘Adem’ tidak bisa", "diputuskan dari", "nama saja."], (76, 235), f(FONT_SERIF_BOLD, 59), PAPER, 72)
    paragraph(d, "Kenyamanan dipengaruhi serat, rapat-tenun, ketebalan, finishing, lapisan, dan kondisi pemakaian.",
              (76, 515), f(FONT_SANS, 31), PAPER, 860, 50)
    d.rounded_rectangle((76, 780, 1004, 1085), radius=30, fill=(116, 91, 79), outline=PALE, width=2)
    d.text((112, 830), "Cara cek paling aman:", font=f(FONT_SANS_BOLD, 27), fill=PALE)
    lines(d, ["sentuh • coba lipat • tes cahaya", "baca komposisi & petunjuk perawatan"],
          (112, 900), f(FONT_SANS, 28), PAPER, 51)
    d.text((76, 1208), "Nama kategori ≠ performa yang selalu sama.", font=f(FONT_SANS_BOLD, 25), fill=PALE)
    save(im, "06-not-name.png")


def checklist():
    im = base()
    d = ImageDraw.Draw(im)
    lines(d, ["Sebelum beli,", "cek 5 hal ini."], (76, 225), f(FONT_SERIF_BOLD, 63), DARK, 75)
    items = [
        ("01", "Komposisi serat", "cotton, polyester, rayon, atau blend"),
        ("02", "Opasitas", "tes di depan cahaya"),
        ("03", "Grip & tekstur", "mudah bergeser atau tidak"),
        ("04", "Ukuran & coverage", "cukup untuk gaya yang dipakai"),
        ("05", "Care label", "cara cuci, suhu, dan setrika"),
    ]
    for i, (num, title, desc) in enumerate(items):
        y = 480 + i * 150
        d.text((76, y), num, font=f(FONT_SANS_BOLD, 23), fill=CHIFFON)
        d.text((148, y-6), title, font=f(FONT_SANS_BOLD, 29), fill=DARK)
        d.text((148, y+42), desc, font=f(FONT_SANS, 23), fill=MUTED)
        d.line((148, y+94, 1004, y+94), fill=LINE, width=2)
    save(im, "07-checklist.png")


def closing():
    im = base(CREAM)
    d = ImageDraw.Draw(im)
    lines(d, ["Jadi, kamu butuh", "yang mana?"], (76, 235), f(FONT_SERIF_BOLD, 66), DARK, 79)
    d.rounded_rectangle((76, 500, 510, 955), radius=30, fill=VOAL)
    d.text((112, 555), "VOAL", font=f(FONT_SANS_BOLD, 25), fill=PAPER)
    lines(d, ["rapi", "terkontrol", "daily"], (112, 655), f(FONT_SERIF_BOLD, 43), PAPER, 62)
    d.rounded_rectangle((570, 500, 1004, 955), radius=30, fill=CHIFFON)
    d.text((606, 555), "CHIFFON", font=f(FONT_SANS_BOLD, 25), fill=PAPER)
    lines(d, ["fluid", "lembut", "dressy"], (606, 655), f(FONT_SERIF_BOLD, 43), PAPER, 62)
    d.text((76, 1045), "Simpan panduan ini sebelum memilih kain.", font=f(FONT_SANS_BOLD, 29), fill=DARK)
    d.text((76, 1105), "Kamu tim voal, chiffon, atau tergantung acara?", font=f(FONT_SANS, 25), fill=MUTED)
    save(im, "08-save.png")


def story_photo(filename, title, subtitle, sticker):
    src = Image.open(PHOTO_SOURCE).convert("RGB")
    im = ImageOps.fit(src, (1080, 1920), Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")
    wash = Image.new("RGBA", im.size, (0, 0, 0, 0))
    wd = ImageDraw.Draw(wash)
    wd.rectangle((0, 0, 1080, 730), fill=(*PAPER, 238))
    wd.rectangle((0, 1400, 1080, 1920), fill=(*DARK, 135))
    im = Image.alpha_composite(im, wash)
    mark = logo(330)
    im.paste(mark, (76, 62), mark)
    d = ImageDraw.Draw(im)
    y = lines(d, title, (76, 315), f(FONT_SERIF_BOLD, 76), DARK, 90)
    paragraph(d, subtitle, (76, y+34), f(FONT_SANS, 31), DARK, 900, 47)
    d.rounded_rectangle((76, 1465, 1004, 1725), radius=30, fill=(*PAPER, 230), outline=LINE, width=3)
    d.text((112, 1527), sticker, font=f(FONT_SANS_BOLD, 27), fill=MUTED)
    save(im, filename)


def story_question():
    im = Image.new("RGB", (1080, 1920), CREAM).convert("RGBA")
    mark = logo(330)
    im.paste(mark, (76, 62), mark)
    d = ImageDraw.Draw(im)
    d.line((76, 190, 1004, 190), fill=LINE, width=2)
    lines(d, ["Apa yang paling", "bikin ragu saat", "pilih bahan?"], (76, 360), f(FONT_SERIF_BOLD, 74), DARK, 89)
    lines(d, ["Opasitas? Grip? Gerah?", "Atau cara merawatnya?"], (76, 705), f(FONT_SANS, 34), DARK, 54)
    d.rounded_rectangle((76, 1160, 1004, 1550), radius=32, fill=PAPER, outline=LINE, width=3)
    d.text((116, 1230), "Tambahkan Questions:", font=f(FONT_SANS_BOLD, 27), fill=MUTED)
    d.text((116, 1300), "Tulis pertanyaan bahanmu", font=f(FONT_SANS, 31), fill=DARK)
    d.text((76, 1740), "Jawabanmu bisa jadi Hijab 101 berikutnya.", font=f(FONT_SANS_BOLD, 25), fill=MUTED)
    save(im, "story-03-question.png")


def contact_sheet():
    names = ["01-cover.png", "02-summary.png", "03-voal.png", "04-chiffon.png", "05-choose.png", "06-not-name.png", "07-checklist.png", "08-save.png"]
    sheet = Image.new("RGB", (1160, 760), PAPER)
    d = ImageDraw.Draw(sheet)
    d.text((40, 24), "DAY 07 — Carousel preview", font=f(FONT_SANS_BOLD, 28), fill=DARK)
    for i, name in enumerate(names):
        im = Image.open(ASSETS / name).convert("RGB")
        im.thumbnail((250, 313), Image.Resampling.LANCZOS)
        x, y = 40 + (i % 4) * 280, 78 + (i // 4) * 332
        sheet.paste(im, (x, y))
    sheet.save(ASSETS / "contact-sheet.png", optimize=True)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    cover()
    split_summary()
    material_slide("left", "VOAL", ["Lebih mudah", "dibentuk rapi"],
                   "Voal umumnya terasa lebih tegas dan matte, sehingga framing wajah lebih mudah dipertahankan.",
                   ["Cocok untuk daily", "Praktis untuk clean look", "Tetap cek opasitas"], "03-voal.png", VOAL)
    material_slide("right", "CHIFFON", ["Jatuh lebih", "fluid"],
                   "Chiffon umumnya ringan, sheer, dan memiliki drape lembut—bagus saat kamu ingin gerak kain yang lebih mengalir.",
                   ["Sering perlu inner", "Bisa butuh magnet/pin", "Layer bila menerawang"], "04-chiffon.png", CHIFFON)
    choose_slide()
    not_from_name()
    checklist()
    closing()
    story_photo("story-01-poll.png", ["Voal atau", "chiffon?"], "Tidak ada jawaban universal. Mulai dari kebutuhan stylingmu.", "Tambahkan Poll: VOAL / CHIFFON")
    story_photo("story-02-chooser.png", ["Butuh yang", "seperti apa?"], "Framing rapi → mulai dari voal. Jatuh fluid → mulai dari chiffon.", "Bagikan carousel lengkap ke temanmu")
    story_question()
    contact_sheet()
