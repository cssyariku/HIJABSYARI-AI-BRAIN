"""Render Day 18 carousel, Stories, and QA previews.

Run: python CONTENT/DAY-18/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "wrinkle-triptych.jpg"

CW, CH = 1080, 1350
SW, SH = 1080, 1920
PAPER = (250, 247, 241)
CREAM = (240, 235, 225)
BLUE = (112, 130, 151)
BLUE_DARK = (70, 87, 108)
DARK = (47, 42, 39)
MUTED = (104, 94, 88)
LINE = (208, 198, 188)
WHITE = (255, 255, 255)
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


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
    leading = leading or int(face.size * 1.2)
    for row in wrap(draw, value, face, max_width):
        draw.text((x, y), row, font=face, fill=fill)
        y += leading
    return y


def rounded(draw, box, radius=28, fill=PAPER, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def footer(draw, h=CH, light=False):
    draw.text((64, h - 42), "@hijabsyaricoid", font=font(SANS, 21),
              fill=PAPER if light else MUTED, anchor="ls")


def source_panel(index):
    src = Image.open(SOURCE).convert("RGB")
    left = round(src.width * index / 3) + (4 if index else 0)
    right = round(src.width * (index + 1) / 3) - (4 if index < 2 else 0)
    return src.crop((left, 0, right, src.height))


def triptych(size, indices=(0, 1, 2)):
    out = Image.new("RGB", size, PAPER)
    gap = 7
    cell = (size[0] - gap * (len(indices) - 1)) // len(indices)
    for pos, index in enumerate(indices):
        pic = ImageOps.fit(source_panel(index), (cell, size[1]), Image.Resampling.LANCZOS,
                           centering=(.5, .43))
        out.paste(pic, (pos * (cell + gap), 0))
    return out


def cover():
    im = Image.new("RGB", (CW, CH), PAPER)
    im.paste(triptych((CW, 710)), (0, 640))
    overlay = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, CW, 760), fill=(*PAPER, 240))
    im = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(im)
    text_block(d, "Hijab gampang kusut? Cek 4 titik ini dulu.",
               (64, 92), font(SERIF_BOLD, 68), DARK, 920, 81)
    rounded(d, (64, 420, 866, 525), 48, CREAM, LINE)
    d.text((104, 452), "Kain · lembap · kering · simpan",
           font=font(SANS_BOLD, 28), fill=BLUE_DARK)
    footer(d, light=True)
    return im


def four_points():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Kusut bukan cuma soal ‘bahan jelek’", (64, 74),
               font(SERIF_BOLD, 58), DARK, 930, 70)
    cards = [
        ("01", "Karakter kain", "serat · konstruksi · finish"),
        ("02", "Saat masih lembap", "menumpuk · terpelintir · tertekan"),
        ("03", "Cara mengeringkan", "waktu · bentuk · panas"),
        ("04", "Cara menyimpan", "lipatan · tumpukan · ruang"),
    ]
    y = 300
    for num, title, sub in cards:
        rounded(d, (64, y, 1016, y + 184), 34, PAPER, LINE)
        d.ellipse((96, y + 50, 180, y + 134), fill=BLUE_DARK)
        d.text((138, y + 92), num, font=font(SANS_BOLD, 23), fill=PAPER, anchor="mm")
        d.text((216, y + 42), title, font=font(SANS_BOLD, 31), fill=DARK)
        d.text((216, y + 102), sub, font=font(SANS, 25), fill=MUTED)
        y += 208
    d.text((64, 1170), "Nama bahan saja belum menjelaskan semuanya.",
           font=font(SANS, 24), fill=MUTED)
    footer(d)
    return im


def detail_slide(number, title, body, action, index, tags):
    im = Image.new("RGB", (CW, CH), PAPER)
    portrait = ImageOps.fit(source_panel(index), (500, 1120), Image.Resampling.LANCZOS,
                            centering=(.5, .43))
    im.paste(portrait, (580, 100))
    overlay = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 620, CH), fill=(*PAPER, 248))
    im = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(im)
    rounded(d, (64, 82, 176, 150), 32, BLUE_DARK)
    d.text((120, 116), f"{number}", font=font(SANS_BOLD, 24), fill=PAPER, anchor="mm")
    y = text_block(d, title, (64, 205), font(SERIF_BOLD, 54), DARK, 480, 66)
    y = text_block(d, body, (64, y + 55), font(SANS, 28), DARK, 466, 44)
    d.line((64, y + 32, 520, y + 32), fill=LINE, width=2)
    d.text((64, y + 76), "COBA INI", font=font(SANS_BOLD, 21), fill=BLUE_DARK)
    y = text_block(d, action, (64, y + 120), font(SANS_BOLD, 26), BLUE_DARK, 460, 40)
    for i, tag in enumerate(tags):
        yy = 1010 + i * 58
        d.ellipse((64, yy + 9, 82, yy + 27), fill=BLUE)
        d.text((104, yy), tag, font=font(SANS, 23), fill=MUTED)
    footer(d)
    return im


def reset_slide():
    im = Image.new("RGB", (CW, CH), (225, 232, 238))
    d = ImageDraw.Draw(im)
    text_block(d, "Reset kusut dengan aman", (64, 80), font(SERIF_BOLD, 62), DARK, 930, 75)
    steps = [
        "Lepaskan hijab dari tubuh",
        "Baca care label",
        "Mulai dari suhu rendah",
        "Uji area kecil",
        "Press cloth / steam bila aman",
    ]
    y = 290
    for i, step in enumerate(steps, 1):
        rounded(d, (64, y, 1016, y + 130), 30, PAPER, LINE)
        d.ellipse((92, y + 27, 168, y + 103), fill=BLUE_DARK)
        d.text((130, y + 65), f"{i:02}", font=font(SANS_BOLD, 21), fill=PAPER, anchor="mm")
        d.text((208, y + 65), step, font=font(SANS_BOLD, 29), fill=DARK, anchor="lm")
        y += 150
    rounded(d, (64, 1080, 1016, 1192), 30, BLUE_DARK)
    d.text((540, 1136), "Stop jika warna, tekstur, atau kilap berubah.",
           font=font(SANS_BOLD, 25), fill=PAPER, anchor="mm")
    footer(d)
    return im


def checklist_slide():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Checklist 60 detik", (64, 82), font(SERIF_BOLD, 66), DARK, 900, 79)
    items = [
        "Care label sudah dicek?",
        "Dirapikan saat lembap?",
        "Tidak dibiarkan menumpuk?",
        "Disimpan tanpa tekanan berlebih?",
    ]
    y = 300
    for item in items:
        rounded(d, (64, y, 1016, y + 150), 34, PAPER, LINE)
        d.rounded_rectangle((98, y + 47, 154, y + 103), radius=14, outline=BLUE_DARK, width=4)
        d.text((190, y + 75), item, font=font(SANS_BOLD, 28), fill=DARK, anchor="lm")
        y += 174
    rounded(d, (64, 1050, 1016, 1198), 34, BLUE_DARK)
    d.text((540, 1100), "Simpan untuk hari cuci berikutnya.",
           font=font(SANS_BOLD, 29), fill=PAPER, anchor="mm")
    d.text((540, 1151), "Paling sering kusut setelah cuci atau simpan?",
           font=font(SANS, 22), fill=PAPER, anchor="mm")
    footer(d)
    return im


def story_one():
    im = Image.new("RGB", (SW, SH), PAPER)
    im.paste(triptych((SW, 1010), (0, 2)), (0, 910))
    d = ImageDraw.Draw(im)
    text_block(d, "Hijabmu paling sering kusut setelah…", (72, 145),
               font(SERIF_BOLD, 70), DARK, 920, 84)
    rounded(d, (72, 535, 1008, 810), 42, CREAM, LINE)
    d.text((540, 614), "RUANG POLL INSTAGRAM", font=font(SANS_BOLD, 24), fill=BLUE_DARK, anchor="mm")
    d.text((540, 718), "DICUCI   /   DISIMPAN", font=font(SANS_BOLD, 35), fill=DARK, anchor="mm")
    footer(d, SH, light=True)
    return im


def story_two():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Empat titik yang perlu dicek", (72, 145),
               font(SERIF_BOLD, 70), DARK, 920, 84)
    items = ["Karakter kain", "Saat masih lembap", "Cara mengeringkan", "Cara menyimpan"]
    y = 440
    for i, item in enumerate(items, 1):
        rounded(d, (72, y, 1008, y + 152), 34, PAPER, LINE)
        d.ellipse((102, y + 39, 176, y + 113), fill=BLUE_DARK)
        d.text((139, y + 76), f"{i:02}", font=font(SANS_BOLD, 21), fill=PAPER, anchor="mm")
        d.text((216, y + 76), item, font=font(SANS_BOLD, 30), fill=DARK, anchor="lm")
        y += 176
    rounded(d, (72, 1310, 1008, 1645), 42, PAPER, LINE)
    d.text((540, 1400), "RUANG EMOJI SLIDER", font=font(SANS_BOLD, 24), fill=BLUE_DARK, anchor="mm")
    d.text((540, 1528), "Sudah cek berapa?", font=font(SANS_BOLD, 36), fill=DARK, anchor="mm")
    footer(d, SH)
    return im


def story_three():
    im = Image.new("RGB", (SW, SH), (225, 232, 238))
    d = ImageDraw.Draw(im)
    text_block(d, "Hijab apa yang paling sulit kamu rapikan?", (72, 145),
               font(SERIF_BOLD, 70), DARK, 920, 84)
    pic = ImageOps.fit(source_panel(1), (936, 700), Image.Resampling.LANCZOS, centering=(.5, .44))
    im.paste(pic, (72, 480))
    d = ImageDraw.Draw(im)
    rounded(d, (72, 1300, 1008, 1640), 42, PAPER, LINE)
    d.text((540, 1390), "RUANG QUESTIONS STICKER", font=font(SANS_BOLD, 24), fill=BLUE_DARK, anchor="mm")
    d.text((540, 1518), "Bahan / model / masalahnya…", font=font(SANS_BOLD, 31), fill=DARK, anchor="mm")
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
    d.text((20, 12), "DAY 18 — QA PREVIEW", font=font(SANS_BOLD, 24), fill=DARK)
    for i, im in enumerate(images):
        canvas.paste(im.convert("RGB").resize(thumb, Image.Resampling.LANCZOS),
                     ((i % cols) * thumb[0], 54 + (i // cols) * thumb[1]))
    save_png(canvas, path)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    slides = [
        cover(),
        four_points(),
        detail_slide("01", "Kenali karakter kainnya",
                     "Serat, konstruksi, campuran, dan finishing memengaruhi respons kain terhadap kerutan.",
                     "Mulai dari care label—bukan tebakan suhu.", 2,
                     ["respons kain berbeda", "hindari aturan universal"]),
        detail_slide("02", "Cek saat masih lembap",
                     "Kain yang menumpuk, terpelintir, atau tertekan saat lembap dapat mengering mengikuti bentuk itu.",
                     "Angkat, kibas lembut, lalu rapikan bentuknya.", 1,
                     ["jangan dipelintir", "jangan lama menumpuk"]),
        detail_slide("03", "Periksa cara mengeringkan",
                     "Panas berlebih dan tumpukan basah dapat membuat perawatan lebih sulit dan berisiko pada kain tertentu.",
                     "Rapikan tepi; gantung atau baringkan sesuai label.", 1,
                     ["ikuti care label", "hindari panas berlebih"]),
        detail_slide("04", "Lihat cara menyimpan",
                     "Lipatan sempit, tumpukan berat, atau tas penuh bisa meninggalkan garis tekan berulang.",
                     "Lipat lebih lebar, gulung longgar, atau gantung bila sesuai.", 0,
                     ["kurangi tekanan", "beri ruang"]),
        reset_slide(),
        checklist_slide(),
    ]
    for i, im in enumerate(slides, 1):
        save_png(im, ASSETS / f"carousel-{i:02d}.png")
    stories = [story_one(), story_two(), story_three()]
    for i, im in enumerate(stories, 1):
        save_png(im, ASSETS / f"story-{i:02d}.png")
    sheet(slides, ASSETS / "contact-sheet.png", 4, (270, 338))
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480))


if __name__ == "__main__":
    main()

