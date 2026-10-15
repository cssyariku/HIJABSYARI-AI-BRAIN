"""Render Day 10 carousel, Stories, and QA preview.

Run: python CONTENT/DAY-10/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"
PHOTO_SOURCE = ASSETS / "inner-comfort-triptych.png"

W, H = 1080, 1350
PAPER = (250, 247, 241)
CREAM = (243, 236, 225)
DARK = (48, 42, 39)
MUTED = (105, 94, 87)
LINE = (205, 190, 177)
TAUPE = (154, 127, 111)
COCOA = (105, 73, 61)
PALE = (232, 222, 211)
ROSE = (182, 136, 128)
SAGE = (139, 150, 130)

FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def logo(width=275, light=False):
    with Image.open(LOGO_SOURCE) as opened:
        src = opened.convert("RGBA")
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


def wrap(draw, text, face, width):
    rows, row = [], ""
    for word in text.split():
        trial = f"{row} {word}".strip()
        if draw.textbbox((0, 0), trial, font=face)[2] <= width:
            row = trial
        else:
            rows.append(row)
            row = word
    if row:
        rows.append(row)
    return rows


def lines(draw, rows, xy, face, fill, leading):
    x, y = xy
    for row in rows:
        draw.text((x, y), row, font=face, fill=fill)
        y += leading
    return y


def paragraph(draw, text, xy, face, fill, width, leading):
    return lines(draw, wrap(draw, text, face, width), xy, face, fill, leading)


def panel(index):
    with Image.open(PHOTO_SOURCE) as opened:
        src = opened.convert("RGB")
        src.load()
        pw = src.width / 3
        inset = 4
        left = round(index * pw + (inset if index else 0))
        right = round((index + 1) * pw - (inset if index < 2 else 0))
        return src.crop((left, 0, right, src.height)).copy()


def panel_strip(size=(928, 610)):
    out = Image.new("RGB", size, PAPER)
    gap = 7
    cell_w = (size[0] - gap * 2) // 3
    for i in range(3):
        pic = ImageOps.fit(panel(i), (cell_w, size[1]), Image.Resampling.LANCZOS, centering=(0.5, 0.35))
        out.paste(pic, (i * (cell_w + gap), 0))
    return out


def base(bg=CREAM, light=False):
    im = Image.new("RGB", (W, H), bg).convert("RGBA")
    masthead(im, light=light)
    return im


def pill(draw, xy, text, color=TAUPE, text_color=PAPER):
    draw.rounded_rectangle(xy, radius=(xy[3] - xy[1]) // 2, fill=color)
    draw.text(((xy[0] + xy[2]) // 2, (xy[1] + xy[3]) // 2), text,
              font=f(FONT_SANS_BOLD, 21), fill=text_color, anchor="mm")


def bullet(draw, y, text, width=790, color=TAUPE, size=27):
    draw.ellipse((82, y + 12, 100, y + 30), fill=color)
    return paragraph(draw, text, (128, y), f(FONT_SANS, size), DARK, width, 42)


def cover():
    im = base(PAPER)
    d = ImageDraw.Draw(im)
    lines(d, ["Inner terasa", "tidak nyaman?"], (76, 218), f(FONT_SERIF_BOLD, 72), DARK, 86)
    d.rounded_rectangle((76, 410, 780, 502), radius=44, fill=TAUPE)
    d.text((112, 438), "Cek 3 hal ini dulu.", font=f(FONT_SANS_BOLD, 32), fill=PAPER)
    im.paste(panel_strip((928, 655)), (76, 565))
    d = ImageDraw.Draw(im)
    d.text((76, 1255), "Tekanan • gesekan • panas & lembap →", font=f(FONT_SANS_BOLD, 24), fill=MUTED)
    save(im, "01-cover.png")


def map_slide():
    im = base()
    d = ImageDraw.Draw(im)
    lines(d, ["Rasa tidak nyaman", "bisa beda sumber."], (76, 225), f(FONT_SERIF_BOLD, 60), DARK, 73)
    cards = [
        ("01", "TERTEKAN", "Ukuran atau ikatan terasa terlalu rapat.", TAUPE),
        ("02", "BERGESEKAN", "Jahitan atau tepi inner menekan satu titik.", ROSE),
        ("03", "PANAS & LEMBAP", "Material dan lapisan terasa terlalu pengap.", SAGE),
    ]
    for i, (num, title, body, color) in enumerate(cards):
        y = 480 + i * 225
        d.rounded_rectangle((76, y, 1004, y + 182), radius=28, fill=PAPER, outline=LINE, width=2)
        d.ellipse((108, y + 48, 190, y + 130), fill=color)
        d.text((149, y + 89), num, font=f(FONT_SANS_BOLD, 22), fill=PAPER, anchor="mm")
        d.text((225, y + 34), title, font=f(FONT_SANS_BOLD, 27), fill=DARK)
        paragraph(d, body, (225, y + 82), f(FONT_SANS, 25), MUTED, 700, 37)
    d.text((76, 1208), "Cari sumbernya dulu—jangan langsung menyalahkan bahannya.", font=f(FONT_SANS_BOLD, 23), fill=MUTED)
    save(im, "02-map.png")


def photo_check_slide(index, number, title_rows, bullets, footer, filename, accent):
    im = Image.new("RGB", (W, H), PAPER).convert("RGBA")
    portrait = ImageOps.fit(panel(index), (475, 1060), Image.Resampling.LANCZOS, centering=(0.5, 0.30))
    im.paste(portrait, (605, 160))
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(overlay).rectangle((0, 0, 650, H), fill=(*PAPER, 249))
    im = Image.alpha_composite(im, overlay)
    masthead(im)
    d = ImageDraw.Draw(im)
    pill(d, (76, 224, 238, 278), f"{number}  CEK", accent)
    lines(d, title_rows, (76, 335), f(FONT_SERIF_BOLD, 55), DARK, 67)
    y = 535
    for text in bullets:
        y = bullet(d, y, text, width=430, color=accent, size=25) + 28
    d.line((76, 1090, 545, 1090), fill=LINE, width=2)
    paragraph(d, footer, (76, 1130), f(FONT_SANS_BOLD, 22), MUTED, 465, 34)
    save(im, filename)


def reset_slide():
    im = base(PALE)
    d = ImageDraw.Draw(im)
    lines(d, ["Tes cepat:", "longgarkan dulu."], (76, 225), f(FONT_SERIF_BOLD, 64), DARK, 77)
    steps = [
        ("1", "Lepas atau longgarkan inner beberapa menit."),
        ("2", "Ubah posisi tepi inner di hairline dan sisi kepala."),
        ("3", "Jangan menambah ikatan hanya agar hijab terasa lebih stay."),
    ]
    for i, (num, text) in enumerate(steps):
        y = 500 + i * 210
        d.rounded_rectangle((76, y, 1004, y + 160), radius=30, fill=PAPER, outline=LINE, width=2)
        d.ellipse((110, y + 40, 190, y + 120), fill=TAUPE)
        d.text((150, y + 80), num, font=f(FONT_SANS_BOLD, 27), fill=PAPER, anchor="mm")
        paragraph(d, text, (225, y + 40), f(FONT_SANS_BOLD, 26), DARK, 720, 40)
    d.text((76, 1185), "Kalau keluhan tetap ada, jangan paksa lanjut memakai.", font=f(FONT_SANS_BOLD, 24), fill=COCOA)
    save(im, "04-reset.png")


def caution_slide():
    bg = ImageOps.fit(panel(0), (W, H), Image.Resampling.LANCZOS, centering=(0.5, 0.18)).convert("RGBA")
    shade = Image.new("RGBA", (W, H), (35, 29, 26, 145))
    im = Image.alpha_composite(bg, shade)
    masthead(im, light=True)
    d = ImageDraw.Draw(im)
    lines(d, ["Jangan paksa kalau", "tubuh memberi sinyal."], (76, 245), f(FONT_SERIF_BOLD, 61), PAPER, 74)
    d.rounded_rectangle((76, 485, 1004, 1088), radius=32, fill=(*PAPER, 238))
    y = 555
    for text in [
        "Lepas inner jika muncul nyeri atau pusing.",
        "Ganti jika gatal atau kemerahan berulang.",
        "Jika keluhan menetap, berat, atau disertai gejala lain, pertimbangkan bantuan tenaga kesehatan.",
    ]:
        y = bullet(d, y, text, width=790, color=COCOA, size=25) + 35
    d.text((76, 1175), "Konten ini membantu pengecekan awal, bukan diagnosis.", font=f(FONT_SANS_BOLD, 23), fill=PAPER)
    save(im, "07-caution.png")


def checklist_slide():
    im = base(TAUPE)
    d = ImageDraw.Draw(im)
    lines(d, ["Checklist 30 detik", "sebelum keluar."], (76, 225), f(FONT_SERIF_BOLD, 64), PAPER, 78)
    items = [
        "Tidak terasa terlalu kencang.",
        "Jahitan atau tepi tidak menekan.",
        "Inner kering dan lapisannya secukupnya.",
    ]
    for i, text in enumerate(items):
        y = 520 + i * 180
        d.rounded_rectangle((76, y, 1004, y + 135), radius=28, fill=(*PAPER, 238), outline=LINE, width=2)
        d.ellipse((112, y + 38, 172, y + 98), fill=SAGE)
        d.text((142, y + 68), "✓", font=f(FONT_SANS_BOLD, 28), fill=PAPER, anchor="mm")
        d.text((210, y + 48), text, font=f(FONT_SANS_BOLD, 26), fill=DARK)
    d.text((76, 1110), "Simpan checklist ini untuk sesi styling berikutnya.", font=f(FONT_SANS_BOLD, 25), fill=PAPER)
    d.text((76, 1170), "Masalah innermu paling sering yang mana?", font=f(FONT_SANS, 24), fill=PAPER)
    save(im, "08-checklist.png")


def story_teaser():
    im = Image.new("RGB", (1080, 1920), PAPER).convert("RGBA")
    im.paste(panel_strip((1080, 1030)), (0, 675))
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Inner terasa", "tidak nyaman?"], (76, 285), f(FONT_SERIF_BOLD, 76), DARK, 91)
    d.text((76, 510), "Mulai dari sumber rasa tidak nyamannya.", font=f(FONT_SANS, 30), fill=MUTED)
    d.rounded_rectangle((76, 1570, 1004, 1810), radius=32, fill=(*PAPER, 238), outline=LINE, width=3)
    d.text((112, 1628), "Tambahkan Poll:", font=f(FONT_SANS_BOLD, 27), fill=MUTED)
    d.text((112, 1692), "TERTEKAN / PANAS", font=f(FONT_SANS_BOLD, 31), fill=DARK)
    save(im, "story-01-poll.png")


def story_checklist():
    im = Image.new("RGB", (1080, 1920), PALE).convert("RGBA")
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Cek inner dalam", "30 detik."], (76, 300), f(FONT_SERIF_BOLD, 74), DARK, 90)
    items = ["Ukuran tidak terlalu rapat", "Jahitan tidak menekan", "Inner kering, lapisan cukup"]
    for i, text in enumerate(items):
        y = 680 + i * 235
        d.rounded_rectangle((76, y, 1004, y + 175), radius=32, fill=PAPER, outline=LINE, width=3)
        d.ellipse((112, y + 55, 177, y + 120), fill=SAGE)
        d.text((144, y + 87), "✓", font=f(FONT_SANS_BOLD, 28), fill=PAPER, anchor="mm")
        d.text((215, y + 65), text, font=f(FONT_SANS_BOLD, 29), fill=DARK)
    d.text((76, 1615), "Kenyamanan lebih penting daripada memaksa styling.", font=f(FONT_SANS_BOLD, 25), fill=MUTED)
    save(im, "story-02-checklist.png")


def story_question():
    bg = ImageOps.fit(panel(2), (1080, 1920), Image.Resampling.LANCZOS, centering=(0.5, 0.20)).convert("RGBA")
    veil = Image.new("RGBA", (1080, 1920), (*PAPER, 135))
    im = Image.alpha_composite(bg, veil)
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Masalah inner", "paling sering?"], (76, 300), f(FONT_SERIF_BOLD, 74), DARK, 89)
    d.text((76, 510), "Tertekan, bergesekan, panas, atau lainnya?", font=f(FONT_SANS, 29), fill=DARK)
    d.rounded_rectangle((76, 1210, 1004, 1630), radius=32, fill=(*PAPER, 238), outline=LINE, width=3)
    d.text((116, 1280), "Tambahkan Questions:", font=f(FONT_SANS_BOLD, 27), fill=MUTED)
    paragraph(d, "Ceritakan rasa tidak nyaman yang paling sering kamu alami.", (116, 1360), f(FONT_SANS, 31), DARK, 820, 47)
    save(im, "story-03-question.png")


def contact_sheet():
    names = ["01-cover.png", "02-map.png", "03-pressure.png", "04-reset.png", "05-friction.png", "06-heat.png", "07-caution.png", "08-checklist.png"]
    sheet = Image.new("RGB", (1160, 760), PAPER)
    d = ImageDraw.Draw(sheet)
    d.text((40, 24), "DAY 10 — Carousel preview", font=f(FONT_SANS_BOLD, 28), fill=DARK)
    for i, name in enumerate(names):
        with Image.open(ASSETS / name) as opened:
            pic = opened.convert("RGB")
            pic.load()
        pic.thumbnail((250, 313), Image.Resampling.LANCZOS)
        x, y = 40 + (i % 4) * 280, 78 + (i // 4) * 332
        sheet.paste(pic, (x, y))
    sheet.save(ASSETS / "contact-sheet.png", compress_level=6)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    cover()
    map_slide()
    photo_check_slide(0, "01", ["Tekanan", "& ukuran"], ["Ada bekas tekanan?", "Nyeri terasa di titik inner menekan?", "Ukuran berubah setelah dipakai lama?"], "Mulai dengan melepas atau melonggarkan. Jangan dipaksa.", "03-pressure.png", TAUPE)
    reset_slide()
    photo_check_slide(1, "02", ["Jahitan", "& titik gesek"], ["Tepi inner menekan dekat telinga?", "Jahitan terasa kasar?", "Satu titik terus bergesekan?"], "Geser titik tekan atau pilih permukaan yang terasa lebih rata.", "05-friction.png", ROSE)
    photo_check_slide(2, "03", ["Panas, lembap", "& lapisan"], ["Material terasa pengap?", "Keringat terperangkap?", "Lapisan terlalu banyak?"], "Ganti inner yang basah dan sederhanakan lapisan bila memungkinkan.", "06-heat.png", SAGE)
    caution_slide()
    checklist_slide()
    story_teaser()
    story_checklist()
    story_question()
    contact_sheet()
