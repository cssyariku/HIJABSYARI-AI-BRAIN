"""Render Day 2 assets with Pillow: python CONTENT/DAY-02/render.py"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"
FONTS = Path("C:/Windows/Fonts")

PAPER = (251, 248, 243)
CREAM_BG = (246, 240, 231)
INK = (49, 43, 39)
TAUPE_BG = (119, 94, 81)
LINE = (204, 187, 171)
MUTED = (107, 92, 82)

COLORS = {
    "cream": (230, 217, 196),
    "taupe": (153, 133, 117),
    "mocha": (111, 76, 61),
    "charcoal": (73, 74, 78),
    "navy": (38, 48, 69),
}


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def draw_lines(draw, text_lines, pos, name, size, fill, step):
    x, y = pos
    f = font(name, size)
    for line in text_lines:
        draw.text((x, y), line, font=f, fill=fill)
        y += step
    return y


def logo(dark=False, width=310):
    src = Image.open(LOGO_SOURCE).convert("RGBA")
    src = src.crop(src.getchannel("A").getbbox())
    color = (239, 194, 137) if dark else INK
    out = Image.new("RGBA", src.size, color + (0,))
    out.putalpha(src.getchannel("A"))
    return out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)


def masthead(im, dark=False, line_end=1004, y=39):
    mark = logo(dark)
    im.paste(mark, (76, y), mark)
    d = ImageDraw.Draw(im)
    d.line((76, 150, line_end, 150), fill=(214, 195, 179) if dark else LINE, width=2)


def save(im, name):
    im.save(ASSETS / name, optimize=True)


def cover():
    photo = Image.open(ASSETS / "five-fabrics-photo.png").convert("RGB")
    im = photo.resize((1080, 1350), Image.Resampling.LANCZOS)
    wash = Image.new("RGBA", im.size, (0, 0, 0, 0))
    overlay = wash.load()
    for x in range(im.width):
        alpha = int(246 * max(0, min(1, (750 - x) / 435)))
        for y in range(im.height):
            overlay[x, y] = (*PAPER, alpha)
    im = Image.alpha_composite(im.convert("RGBA"), wash).convert("RGB")
    masthead(im, line_end=600)
    d = ImageDraw.Draw(im)
    draw_lines(d, ["5 warna hijab", "yang gampang", "dipadukan."], (76, 330),
               "GeorgiaPro-CondRegular.ttf", 84, INK, 93)
    d.line((80, 685, 190, 685), fill=TAUPE_BG, width=5)
    draw_lines(d, ["Ide padu padan dari", "isi lemari yang ada."],
               (76, 735), "ArialNova.ttf", 32, INK, 47)
    save(im, "01-cover.png")


def swatch_bar(draw, x, y, width, height, color):
    draw.rounded_rectangle((x, y, x + width, y + height), radius=12, fill=color)


def intro():
    im = Image.new("RGB", (1080, 1350), CREAM_BG)
    masthead(im)
    d = ImageDraw.Draw(im)
    draw_lines(d, ["Bukan soal", "punya semua", "warna."], (76, 270),
               "GeorgiaPro-CondRegular.ttf", 93, INK, 99)
    d.line((80, 625, 205, 625), fill=TAUPE_BG, width=5)
    draw_lines(d, ["Lihat dulu warna atasan yang", "paling sering kamu pakai.",
                   "Mulai dari hijab yang bisa", "masuk ke beberapa outfit."],
               (76, 690), "ArialNova.ttf", 37, INK, 57)
    for i, key in enumerate(COLORS):
        swatch_bar(d, 76 + i * 190, 1125, 170, 95, COLORS[key])
    save(im, "02-intro.png")


def color_slide(filename, name, key, description, pairings, tip, dark=False):
    bg = TAUPE_BG if dark else CREAM_BG
    fg = PAPER if dark else INK
    pale = (226, 211, 196) if dark else MUTED
    im = Image.new("RGB", (1080, 1350), bg)
    masthead(im, dark)
    d = ImageDraw.Draw(im)
    draw_lines(d, name, (76, 270), "GeorgiaPro-CondRegular.ttf", 102, fg, 108)
    d.line((80, 505, 204, 505), fill=pale, width=5)
    draw_lines(d, description, (76, 570), "ArialNova.ttf", 36, fg, 54)

    # Deterministic, color-accurate swatch with gentle fabric-like folds.
    x0, y0, x1, y1 = 654, 265, 1004, 980
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((x0 + 14, y0 + 19, x1 + 14, y1 + 19), radius=28, fill=(0, 0, 0, 54))
    shadow = shadow.filter(ImageFilter.GaussianBlur(21))
    im = Image.alpha_composite(im.convert("RGBA"), shadow)
    panel = Image.new("RGBA", im.size, (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel)
    base = COLORS[key]
    pd.rounded_rectangle((x0, y0, x1, y1), radius=28, fill=base + (255,))
    light = tuple(min(255, int(c + (255 - c) * 0.18)) for c in base)
    shade = tuple(max(0, int(c * 0.75)) for c in base)
    pd.polygon([(x0 + 56, y0), (x0 + 100, y0), (x0 + 230, y1), (x0 + 170, y1)], fill=light + (95,))
    pd.polygon([(x0 + 258, y0), (x1, y0), (x1, y1), (x0 + 315, y1)], fill=shade + (88,))
    pd.line([(x0 + 130, y0 + 5), (x0 + 290, y1 - 5)], fill=light + (90,), width=3)
    im = Image.alpha_composite(im, panel).convert("RGB")
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((76, 1025, 1004, 1196), radius=16, outline=pale, width=2)
    draw_lines(d, pairings, (107, 1045), "ArialNova.ttf", 30, fg, 43)
    draw_lines(d, tip, (76, 820), "ArialNova.ttf", 27, fg, 42)
    save(im, filename)


def closing():
    im = Image.new("RGB", (1080, 1350), TAUPE_BG)
    masthead(im, True)
    d = ImageDraw.Draw(im)
    draw_lines(d, ["Pilih yang paling", "nyambung dengan", "lemarimu."],
               (76, 270), "GeorgiaPro-CondRegular.ttf", 91, PAPER, 98)
    d.line((80, 625, 205, 625), fill=(226, 211, 196), width=5)
    draw_lines(d, ["Cukup mulai dari 2–3 warna yang", "bisa kamu pakai berulang.",
                   "Tidak perlu punya semuanya."],
               (76, 690), "ArialNova.ttf", 37, PAPER, 58)
    for i, key in enumerate(COLORS):
        swatch_bar(d, 76 + i * 190, 975, 170, 95, COLORS[key])
    draw_lines(d, ["Simpan untuk referensi outfit berikutnya."],
               (76, 1135), "ArialNova.ttf", 31, PAPER, 45)
    save(im, "08-save.png")


def story(number, heading, body, foot, dark=False, palette=False):
    bg = TAUPE_BG if dark else CREAM_BG
    fg = PAPER if dark else INK
    pale = (226, 211, 196) if dark else MUTED
    im = Image.new("RGB", (1080, 1920), bg)
    mark = logo(dark, 350)
    im.paste(mark, (76, 64), mark)
    d = ImageDraw.Draw(im)
    d.line((76, 190, 1004, 190), fill=pale, width=2)
    heading_bottom = draw_lines(d, heading, (76, 400),
                                "GeorgiaPro-CondRegular.ttf", 105, fg, 114)
    d.line((76, heading_bottom + 34, 205, heading_bottom + 34), fill=pale, width=5)
    draw_lines(d, body, (76, heading_bottom + 122),
               "ArialNova.ttf", 42, fg, 64)
    if palette:
        for i, key in enumerate(COLORS):
            swatch_bar(d, 76 + i * 190, 1220, 170, 145, COLORS[key])
    d.rounded_rectangle((76, 1490, 1004, 1660), radius=17, outline=pale, width=3)
    draw_lines(d, foot, (112, 1534), "ArialNova.ttf", 33, fg, 49)
    save(im, f"story-{number:02d}.png")


if __name__ == "__main__":
    cover()
    intro()
    color_slide("03-cream.png", ["Cream"], "cream",
                ["Terang dan lembut saat", "dipasangkan dengan", "outfit yang lebih gelap."],
                ["Coba dengan hitam, denim biru,", "atau cokelat."],
                ["Pilih nuansa cream yang", "terasa pas dekat wajahmu."])
    color_slide("04-taupe.png", ["Taupe"], "taupe",
                ["Di antara abu dan cokelat;", "tenang untuk banyak", "warna netral."],
                ["Coba dengan putih tulang,", "hitam, atau olive."],
                ["Jika atasannya taupe juga,", "bedakan tingkat terangnya."], dark=True)
    color_slide("05-mocha.png", ["Mocha"], "mocha",
                ["Cokelat medium untuk", "tampilan hangat tanpa", "terlalu terang."],
                ["Coba dengan cream, sage,", "atau denim."],
                ["Beri sedikit kontras antara", "hijab dan atasan."])
    color_slide("06-charcoal.png", ["Abu arang"], "charcoal",
                ["Pilihan gelap saat kamu", "ingin alternatif selain", "hijab hitam."],
                ["Coba dengan putih, denim muda,", "atau dusty pink."],
                ["Cek di cahaya alami agar", "nuansa abunya terlihat."], dark=True)
    color_slide("07-navy.png", ["Navy"], "navy",
                ["Gelap dan tenang, cocok", "untuk variasi dari", "kombinasi serba hitam."],
                ["Coba dengan putih, abu muda,", "atau camel."],
                ["Atasan yang lebih terang", "membantu warna navy terbaca."])
    closing()
    story(1, ["5 warna hijab", "untuk banyak", "outfit."],
          ["Cream, taupe, mocha,", "abu arang, dan navy.",
           "Lihat contoh padanannya", "di carousel terbaru."],
          ["Lihat pilihan lengkap", "di feed kami."], palette=True)
    story(2, ["Taupe atau", "mocha?"],
          ["Dua warna netral dengan", "kesan yang berbeda.",
           "Kamu lebih sering", "pakai yang mana?"],
          ["Pilihanmu membantu kami", "memilih bahasan berikutnya."], dark=True)
    story(3, ["Warna outfitmu", "yang paling susah", "dipadukan?"],
          ["Tulis warna atasannya.", "Kita bisa bahas pilihan", "hijabnya di konten berikut."],
          ["Tulis di kotak pertanyaan", "di bawah, ya."])
