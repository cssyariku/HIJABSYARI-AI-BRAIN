"""Render Day 1 Instagram assets. Requires Pillow. Run: python CONTENT/DAY-01/render.py"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"
CREAM = (246, 240, 231)
PAPER = (252, 249, 244)
INK = (51, 43, 38)
TAUPE = (124, 98, 84)
MUTED = (107, 95, 87)
LINE = (202, 185, 170)
FONT_DIR = Path("C:/Windows/Fonts")


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


SERIF = "GeorgiaPro-CondRegular.ttf"
SERIF_ITALIC = "GeorgiaPro-CondItalic.ttf"
SANS = "ArialNova.ttf"
def lines(draw, items, x, y, family, size, fill, leading):
    f = font(family, size)
    for item in items:
        draw.text((x, y), item, font=f, fill=fill)
        y += leading
    return y


def brand_logo(dark=False, width=310):
    source = Image.open(LOGO_SOURCE).convert("RGBA")
    source = source.crop(source.getchannel("A").getbbox())
    color = (239, 194, 137) if dark else INK
    logo = Image.new("RGBA", source.size, color + (0,))
    logo.putalpha(source.getchannel("A"))
    height = round(logo.height * width / logo.width)
    return logo.resize((width, height), Image.Resampling.LANCZOS)


def chrome(im, draw, dark=False, line_end=1004):
    faint = (214, 195, 179) if dark else LINE
    logo = brand_logo(dark)
    im.paste(logo, (76, 39), logo)
    draw.line((76, 150, line_end, 150), fill=faint, width=2)


def save(im, name):
    im.save(ASSETS / name, optimize=True)


def cover():
    photo = Image.open(ASSETS / "editorial-photo.png").convert("RGB")
    photo = photo.resize((1080, 1350), Image.Resampling.LANCZOS)
    overlay = Image.new("RGBA", photo.size, (0, 0, 0, 0))
    op = overlay.load()
    for x in range(1080):
        alpha = int(248 * max(0, min(1, (720 - x) / 470)))
        for y in range(1350):
            op[x, y] = (*PAPER, alpha)
    im = Image.alpha_composite(photo.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(im)
    chrome(im, d, line_end=610)
    lines(d, ["Halo, kita", "mulai lagi."], 76, 355, SERIF, 99, INK, 103)
    d.line((80, 620, 178, 620), fill=TAUPE, width=5)
    lines(d, ["Urusan hijab terasa lebih", "mudah, mulai hari ini."], 76, 665, SANS, 33, INK, 48)
    save(im, "01-cover.png")


def standard(number, heading, body, foot, dark=False):
    im = Image.new("RGB", (1080, 1350), TAUPE if dark else CREAM)
    d = ImageDraw.Draw(im)
    chrome(im, d, dark)
    main = PAPER if dark else INK
    secondary = (232, 217, 202) if dark else MUTED
    heading_bottom = lines(d, heading, 76, 265, SERIF, 92, main, 98)
    rule_y = heading_bottom + 32
    d.line((80, rule_y, 205, rule_y), fill=secondary, width=5)
    lines(d, body, 76, rule_y + 68, SANS, 38, main, 57)
    d.rounded_rectangle((76, 1072, 1004, 1185), radius=16, outline=secondary, width=2)
    lines(d, foot, 110, 1090, SANS, 28, main, 37)
    save(im, f"{number:02d}-slide.png")


def story(number, heading, body, footer, dark=False):
    im = Image.new("RGB", (1080, 1920), TAUPE if dark else CREAM)
    d = ImageDraw.Draw(im)
    main = PAPER if dark else INK
    secondary = (232, 217, 202) if dark else TAUPE
    logo = brand_logo(dark, 350)
    im.paste(logo, (76, 64), logo)
    d.line((76, 190, 1004, 190), fill=secondary, width=2)
    heading_bottom = lines(d, heading, 76, 400, SERIF, 103, main, 114)
    rule_y = heading_bottom + 35
    d.line((76, rule_y, 205, rule_y), fill=secondary, width=5)
    lines(d, body, 76, rule_y + 88, SANS, 43, main, 66)
    d.rounded_rectangle((76, 1450, 1004, 1650), radius=18, outline=secondary, width=3)
    lines(d, footer, 120, 1498, SANS, 34, main, 52)
    save(im, f"story-{number:02d}.png")


if __name__ == "__main__":
    cover()
    standard(2, ["Karena hijab", "punya banyak", "cerita kecil."],
             ["Ada pilihan warna, bahan, dan styling", "yang sering bikin kita berhenti", "sejenak sebelum berangkat."],
             ["Di sini, kita bahas dengan cara", "yang praktis dan mudah dicoba."])
    standard(3, ["Masalah sehari-", "hari? Kita cari", "solusinya."],
             ["Hijab bergeser, kusut, atau terasa", "kurang nyaman? Kita uraikan sebab", "dan opsi yang bisa dicoba."],
             ["Tips akan fokus pada kebutuhan,", "bukan aturan gaya yang kaku."], dark=True)
    standard(4, ["Pilih warna", "dan bahan", "lebih yakin."],
             ["Lihat perbandingan warna dengan", "outfit, kenali karakter bahan, lalu", "pilih yang cocok untuk aktivitasmu."],
             ["Simpan ide yang ingin kamu", "coba nanti."], dark=False)
    standard(5, ["Inspirasi yang", "bisa jadi milikmu."],
             ["Bukan sekadar foto cantik. Kita", "akan berbagi ide look yang bisa", "diadaptasi dengan isi lemarimu."],
             ["Pilihan dan pertanyaanmu ikut", "membentuk topik berikutnya."], dark=False)
    standard(6, ["Masalah hijab", "apa yang ingin", "kita bahas dulu?"],
             ["Tulis satu hal yang sering bikin", "kamu bingung saat memilih atau", "memakai hijab."],
             ["Ceritakan di komentar.", "Kami baca untuk ide konten berikutnya."], dark=True)
    story(1, ["Halo lagi,", "Hijab Syari", "Indonesia."],
          ["Mulai sekarang, kita berbagi", "tips hijab yang praktis,", "inspirasi, dan pilihan", "yang lebih mudah dipahami."],
          ["Lihat carousel terbaru", "di feed kami."], dark=False)
    story(2, ["Kamu ingin", "bahas apa", "lebih dulu?"],
          ["Warna hijab untuk outfit?", "Atau solusi hijab yang", "sering bergeser?"],
          ["Pilihanmu membantu kami", "menentukan bahasan pertama."], dark=True)
    story(3, ["Pertanyaanmu", "bisa jadi topik", "berikutnya."],
          ["Hal kecil soal hijab", "apa yang paling sering", "bikin kamu bingung?"],
          ["Tulis di kotak pertanyaan", "di bawah, ya."], dark=False)
