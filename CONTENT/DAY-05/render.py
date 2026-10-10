"""Render Day 5 Stories with Pillow: python CONTENT/DAY-05/render.py"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"
PHOTO_SOURCE = ASSETS / "neutral-ab-fabrics.png"

PAPER = (250, 247, 241)
CREAM = (242, 235, 225)
DARK = (49, 43, 40)
MUTED = (109, 97, 89)
LINE = (205, 190, 177)
WARM = (173, 145, 125)
COOL = (164, 160, 157)
TAUPE_DARK = (104, 80, 68)

FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def lines(draw, rows, xy, face, fill, leading):
    x, y = xy
    for row in rows:
        draw.text((x, y), row, font=face, fill=fill)
        y += leading
    return y


def logo(dark=False, width=330):
    src = Image.open(LOGO_SOURCE).convert("RGBA")
    src = src.crop(src.getchannel("A").getbbox())
    color = (239, 220, 201) if dark else DARK
    out = Image.new("RGBA", src.size, color + (0,))
    out.putalpha(src.getchannel("A"))
    return out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)


def masthead(im, dark=False):
    mark = logo(dark)
    im.paste(mark, (76, 62), mark)
    d = ImageDraw.Draw(im)
    d.line((76, 190, 1004, 190), fill=(216, 195, 177) if dark else LINE, width=2)


def save(im, name):
    im.convert("RGB").save(ASSETS / name, optimize=True, quality=95)


def label(draw, x, y, letter, name, fill):
    draw.rounded_rectangle((x, y, x + 390, y + 116), radius=58, fill=(250, 247, 241, 232))
    draw.ellipse((x + 18, y + 18, x + 98, y + 98), fill=fill)
    draw.text((x + 58, y + 58), letter, font=font(FONT_SANS_BOLD, 34), fill=PAPER, anchor="mm")
    draw.text((x + 122, y + 35), name, font=font(FONT_SANS_BOLD, 27), fill=DARK)


def story_ab():
    src = Image.open(PHOTO_SOURCE).convert("RGB")
    im = ImageOps.fit(src, (1080, 1920), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")
    wash = Image.new("RGBA", im.size, (0, 0, 0, 0))
    wd = ImageDraw.Draw(wash)
    wd.rectangle((0, 0, 1080, 620), fill=(*PAPER, 238))
    wd.rectangle((0, 1540, 1080, 1920), fill=(*PAPER, 225))
    im = Image.alpha_composite(im, wash)
    masthead(im)
    d = ImageDraw.Draw(im)
    lines(d, ["Kalau harus", "pilih satu:"], (76, 310), font(FONT_SERIF_BOLD, 78), DARK, 91)
    d.text((76, 505), "neutral A atau B?", font=font(FONT_SANS_BOLD, 38), fill=DARK)
    label(d, 68, 1220, "A", "WARM TAUPE", WARM)
    label(d, 622, 1220, "B", "COOL GREIGE", COOL)
    d.text((76, 1695), "Pilih yang paling mungkin kamu pakai berulang.",
           font=font(FONT_SANS_BOLD, 28), fill=DARK)
    save(im, "story-01-ab-poll.png")


def crop_side(side):
    src = Image.open(PHOTO_SOURCE).convert("RGB")
    w, h = src.size
    if side == "left":
        box = (0, int(h * 0.20), int(w * 0.53), int(h * 0.82))
    else:
        box = (int(w * 0.47), int(h * 0.20), w, int(h * 0.82))
    return src.crop(box)


def option_story(side, letter, name, descriptor, pairs, note, bg, swatch, filename):
    im = Image.new("RGB", (1080, 1920), bg)
    masthead(im)
    d = ImageDraw.Draw(im)
    d.ellipse((76, 308, 174, 406), fill=swatch)
    d.text((125, 357), letter, font=font(FONT_SANS_BOLD, 39), fill=PAPER, anchor="mm")
    d.text((205, 314), name, font=font(FONT_SERIF_BOLD, 64), fill=DARK)
    d.text((205, 394), descriptor, font=font(FONT_SANS, 29), fill=MUTED)

    photo = ImageOps.fit(crop_side(side), (928, 680), method=Image.Resampling.LANCZOS)
    mask = Image.new("L", photo.size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, photo.width, photo.height), radius=34, fill=255)
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((88, 520, 1016, 1200), radius=34, fill=(0, 0, 0, 44))
    shadow = shadow.filter(ImageFilter.GaussianBlur(20))
    im = Image.alpha_composite(im.convert("RGBA"), shadow)
    im.paste(photo, (76, 500), mask)
    d = ImageDraw.Draw(im)
    d.text((76, 1270), "COBA DENGAN", font=font(FONT_SANS_BOLD, 24), fill=TAUPE_DARK)
    x = 76
    for label_text in pairs:
        width = d.textbbox((0, 0), label_text, font=font(FONT_SANS_BOLD, 27))[2] + 58
        d.rounded_rectangle((x, 1320, x + width, 1396), radius=38, fill=PAPER, outline=LINE, width=2)
        d.text((x + 29, 1343), label_text, font=font(FONT_SANS_BOLD, 27), fill=DARK)
        x += width + 16
    lines(d, note, (76, 1505), font(FONT_SANS, 34), DARK, 55)
    save(im, filename)


def question_story():
    im = Image.new("RGB", (1080, 1920), CREAM)
    masthead(im)
    d = ImageDraw.Draw(im)
    y = lines(d, ["Outfit warna apa", "yang paling susah", "kamu padukan?"],
              (76, 360), font(FONT_SERIF_BOLD, 72), DARK, 88)
    d.line((76, y + 34, 205, y + 34), fill=TAUPE_DARK, width=5)
    lines(d, ["Tulis warna atasannya.", "Jawabanmu bisa menjadi", "Color Lab berikutnya."],
          (76, y + 110), font(FONT_SANS, 37), DARK, 59)
    d.rounded_rectangle((76, 1210, 1004, 1590), radius=30, fill=PAPER, outline=LINE, width=3)
    d.rounded_rectangle((114, 1260, 478, 1370), radius=55, fill=WARM)
    d.rounded_rectangle((602, 1260, 966, 1370), radius=55, fill=COOL)
    d.text((296, 1315), "WARM TAUPE", font=font(FONT_SANS_BOLD, 25), fill=PAPER, anchor="mm")
    d.text((784, 1315), "COOL GREIGE", font=font(FONT_SANS_BOLD, 25), fill=PAPER, anchor="mm")
    d.text((114, 1480), "Tambahkan jawabanmu di kotak Questions.",
           font=font(FONT_SANS_BOLD, 25), fill=MUTED)
    d.text((76, 1745), "Tidak harus neutral—warna apa pun boleh.",
           font=font(FONT_SANS_BOLD, 27), fill=MUTED)
    save(im, "story-04-question.png")


def contact_sheet():
    names = ["story-01-ab-poll.png", "story-02-warm-taupe.png",
             "story-03-cool-greige.png", "story-04-question.png"]
    sheet = Image.new("RGB", (1040, 590), PAPER)
    d = ImageDraw.Draw(sheet)
    d.text((35, 24), "DAY 05 — Stories preview", font=font(FONT_SANS_BOLD, 27), fill=DARK)
    for i, name in enumerate(names):
        im = Image.open(ASSETS / name).convert("RGB")
        im.thumbnail((225, 400), Image.Resampling.LANCZOS)
        x = 35 + i * 250
        sheet.paste(im, (x, 88))
        d.text((x, 510), str(i + 1), font=font(FONT_SANS_BOLD, 22), fill=MUTED)
    sheet.save(ASSETS / "contact-sheet.png", optimize=True)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    story_ab()
    option_story("left", "A", "Warm taupe", "nuansa cokelat lebih terasa",
                 ["CREAM", "CAMEL", "OLIVE"],
                 ["Pilih berdasarkan kombinasi", "yang memang sering kamu pakai."],
                 CREAM, WARM, "story-02-warm-taupe.png")
    option_story("right", "B", "Cool greige", "abu-beige yang lebih muted",
                 ["PUTIH", "CHARCOAL", "NAVY"],
                 ["Bandingkan lagi di cahaya alami;", "warna layar dan kain bisa berbeda."],
                 (238, 236, 232), COOL, "story-03-cool-greige.png")
    question_story()
    contact_sheet()
