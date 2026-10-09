"""Render Day 4 assets with Pillow: python CONTENT/DAY-04/render.py"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"
PHOTO_SOURCE = ASSETS / "editorial-adjusting-hijab.png"

PAPER = (250, 247, 241)
CREAM = (242, 235, 225)
TAUPE = (112, 89, 77)
DARK = (50, 44, 41)
MUTED = (112, 100, 92)
LINE = (205, 190, 177)
ACCENT = (157, 113, 89)
PALE = (230, 218, 205)

FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def text_lines(draw, lines, xy, font, fill, leading):
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def logo(dark=False, width=275):
    src = Image.open(LOGO_SOURCE).convert("RGBA")
    src = src.crop(src.getchannel("A").getbbox())
    color = (238, 216, 194) if dark else DARK
    out = Image.new("RGBA", src.size, color + (0,))
    out.putalpha(src.getchannel("A"))
    return out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)


def masthead(im, dark=False, y=38):
    mark = logo(dark)
    im.paste(mark, (76, y), mark)
    d = ImageDraw.Draw(im)
    d.line((76, 148, 1004, 148), fill=(207, 184, 165) if dark else LINE, width=2)


def save(im, name):
    im.convert("RGB").save(ASSETS / name, optimize=True, quality=95)


def cover():
    src = Image.open(PHOTO_SOURCE).convert("RGB")
    im = ImageOps.fit(src, (1080, 1350), method=Image.Resampling.LANCZOS, centering=(0.56, 0.5))
    wash = Image.new("RGBA", im.size, (0, 0, 0, 0))
    px = wash.load()
    for x in range(im.width):
        alpha = int(245 * max(0, min(1, (670 - x) / 380)))
        for y in range(im.height):
            px[x, y] = (*PAPER, alpha)
    im = Image.alpha_composite(im.convert("RGBA"), wash)
    masthead(im)
    d = ImageDraw.Draw(im)
    text_lines(d, ["Hijab selalu", "maju?"], (76, 310), f(FONT_SERIF_BOLD, 92), DARK, 105)
    d.line((80, 560, 205, 560), fill=ACCENT, width=5)
    text_lines(d, ["Cek 4 hal ini dulu."], (76, 615), f(FONT_SANS_BOLD, 37), DARK, 54)
    text_lines(d, ["Mulai dari pola, bukan tebakan."], (76, 678), f(FONT_SANS, 27), MUTED, 42)
    save(im, "01-cover.png")


def title_block(im, number, title, subtitle=None, dark=False):
    fg = PAPER if dark else DARK
    muted = PALE if dark else MUTED
    d = ImageDraw.Draw(im)
    masthead(im, dark)
    if number:
        d.ellipse((76, 240, 154, 318), fill=PALE if dark else TAUPE)
        d.text((103, 252), str(number), font=f(FONT_SANS_BOLD, 34), fill=TAUPE if dark else PAPER, anchor="ma")
        x = 182
    else:
        x = 76
    y = text_lines(d, title, (x, 238), f(FONT_SERIF_BOLD, 60), fg, 72)
    if subtitle:
        text_lines(d, subtitle, (76, y + 24), f(FONT_SANS, 28), muted, 43)
    return d, fg, muted


def two_paths():
    im = Image.new("RGB", (1080, 1350), CREAM)
    d, fg, muted = title_block(im, None, ["Mulainya kapan?"])
    cards = [
        ((76, 505, 502, 1085), "LANGSUNG", ["Cek fit inner,", "lipatan depan,", "dan titik kunci."], "fit • lipatan • anchor"),
        ((578, 505, 1004, 1085), "SETELAH GERAK", ["Cek gesekan", "aksesori, pakaian,", "dan aktivitas."], "gesekan • gerak"),
    ]
    for box, label, body, foot in cards:
        d.rounded_rectangle(box, radius=28, fill=PAPER, outline=LINE, width=3)
        x0, y0, x1, y1 = box
        d.text((x0 + 34, y0 + 38), label, font=f(FONT_SANS_BOLD, 24), fill=ACCENT)
        text_lines(d, body, (x0 + 34, y0 + 128), f(FONT_SERIF_BOLD, 39), fg, 58)
        d.line((x0 + 34, y1 - 135, x1 - 34, y1 - 135), fill=LINE, width=2)
        d.text((x0 + 34, y1 - 92), foot, font=f(FONT_SANS, 22), fill=muted)
    d.text((76, 1160), "Amati polanya sebelum mengubah styling.", font=f(FONT_SANS_BOLD, 27), fill=fg)
    save(im, "02-pattern.png")


def icon_inner(draw, cx, cy, color):
    draw.arc((cx-100, cy-115, cx+100, cy+105), 195, 345, fill=color, width=12)
    draw.arc((cx-82, cy-75, cx+82, cy+110), 205, 335, fill=color, width=9)
    draw.line((cx-80, cy+30, cx+80, cy+30), fill=color, width=8)
    draw.line((cx, cy+30, cx, cy+125), fill=color, width=8)
    draw.polygon([(cx-16, cy+103), (cx, cy+133), (cx+16, cy+103)], fill=color)


def icon_anchor(draw, cx, cy, color):
    draw.arc((cx-120, cy-115, cx+120, cy+85), 205, 335, fill=color, width=11)
    draw.line((cx-82, cy+28, cx, cy+108), fill=color, width=9)
    draw.line((cx+82, cy+28, cx, cy+108), fill=color, width=9)
    draw.ellipse((cx-17, cy+91, cx+17, cy+125), fill=color)


def icon_balance(draw, cx, cy, color):
    draw.line((cx, cy-125, cx, cy+105), fill=color, width=10)
    draw.line((cx-135, cy-80, cx+135, cy-80), fill=color, width=10)
    draw.ellipse((cx-13, cy-94, cx+13, cy-68), fill=color)
    for side in (-1, 1):
        sx = cx + side * 105
        draw.line((sx, cy-80, sx-45, cy+25), fill=color, width=6)
        draw.line((sx, cy-80, sx+45, cy+25), fill=color, width=6)
        draw.arc((sx-52, cy-8, sx+52, cy+70), 0, 180, fill=color, width=8)
    draw.line((cx-65, cy+108, cx+65, cy+108), fill=color, width=10)


def icon_friction(draw, cx, cy, color):
    draw.rounded_rectangle((cx-145, cy-70, cx-25, cy+15), radius=24, outline=color, width=9)
    draw.rounded_rectangle((cx+25, cy-70, cx+145, cy+15), radius=24, outline=color, width=9)
    draw.line((cx-25, cy-28, cx+25, cy-28), fill=color, width=8)
    draw.arc((cx-88, cy+15, cx+88, cy+135), 200, 340, fill=color, width=9)
    for dx in (-180, 180):
        draw.line((cx+dx, cy-20, cx+dx//2, cy-20), fill=ACCENT, width=6)


def diagnostic(filename, number, title, summary, body, tip, icon_fn, dark=False):
    bg = TAUPE if dark else CREAM
    im = Image.new("RGB", (1080, 1350), bg)
    d, fg, muted = title_block(im, number, title, summary, dark)
    panel_fill = (126, 101, 87) if dark else PAPER
    d.rounded_rectangle((76, 500, 1004, 1110), radius=30, fill=panel_fill,
                        outline=(190, 164, 143) if dark else LINE, width=3)
    icon_fn(d, 790, 730, PALE if dark else TAUPE)
    text_lines(d, body, (112, 575), f(FONT_SANS, 31), fg, 49)
    d.line((112, 935, 968, 935), fill=(190, 164, 143) if dark else LINE, width=2)
    text_lines(d, tip, (112, 975), f(FONT_SANS_BOLD, 27), muted, 42)
    save(im, filename)


def movement_test():
    im = Image.new("RGB", (1080, 1350), CREAM)
    d, fg, muted = title_block(im, None, ["Tes gerak sebelum", "berangkat"], ["Cukup sekitar 60 detik."])
    labels = [("01", "Tengok", "kanan–kiri"), ("02", "Lihat", "ke bawah"),
              ("03", "Angkat", "dua tangan"), ("04", "Jalan", "beberapa langkah")]
    for i, (num, a, b) in enumerate(labels):
        col, row = i % 2, i // 2
        x, y = 76 + col * 502, 565 + row * 272
        d.rounded_rectangle((x, y, x+426, y+220), radius=25, fill=PAPER, outline=LINE, width=3)
        d.text((x+28, y+28), num, font=f(FONT_SANS_BOLD, 24), fill=ACCENT)
        d.text((x+28, y+82), a, font=f(FONT_SERIF_BOLD, 36), fill=fg)
        d.text((x+28, y+136), b, font=f(FONT_SANS, 26), fill=muted)
    d.text((76, 1145), "Catat bagian yang bergerak lebih dulu.", font=f(FONT_SANS_BOLD, 29), fill=fg)
    save(im, "07-test.png")


def closing():
    im = Image.new("RGB", (1080, 1350), TAUPE)
    d, fg, muted = title_block(im, None, ["Jangan ubah", "semuanya sekaligus."], None, True)
    d.line((76, 520, 205, 520), fill=PALE, width=5)
    text_lines(d, ["Uji satu hal setiap kali agar", "kamu tahu apa yang membantu."],
               (76, 575), f(FONT_SANS, 34), fg, 54)
    items = ["INNER", "TITIK KUNCI", "TARIKAN KAIN", "GESEKAN"]
    for i, item in enumerate(items):
        y = 770 + i * 90
        d.ellipse((76, y, 106, y+30), fill=PALE)
        d.text((132, y-5), item, font=f(FONT_SANS_BOLD, 25), fill=fg)
    d.rounded_rectangle((76, 1150, 1004, 1240), radius=18, outline=PALE, width=3)
    d.text((112, 1177), "Simpan checklist ini untuk styling berikutnya.",
           font=f(FONT_SANS_BOLD, 27), fill=fg)
    save(im, "08-save.png")


def story(number, title, body, foot, dark=False, blank=False):
    bg = TAUPE if dark else CREAM
    fg = PAPER if dark else DARK
    muted = PALE if dark else MUTED
    im = Image.new("RGB", (1080, 1920), bg)
    mark = logo(dark, 330)
    im.paste(mark, (76, 62), mark)
    d = ImageDraw.Draw(im)
    d.line((76, 190, 1004, 190), fill=muted, width=2)
    y = text_lines(d, title, (76, 380), f(FONT_SERIF_BOLD, 88), fg, 105)
    d.line((76, y+30, 205, y+30), fill=PALE if dark else ACCENT, width=5)
    text_lines(d, body, (76, y+105), f(FONT_SANS, 38), fg, 60)
    if blank:
        d.rounded_rectangle((76, 1280, 1004, 1600), radius=25, fill=(126, 101, 87) if dark else PAPER,
                            outline=PALE if dark else LINE, width=3)
    d.text((76, 1740), foot, font=f(FONT_SANS_BOLD, 27), fill=muted)
    save(im, f"story-{number:02d}.png")


def contact_sheet():
    files = [f"0{i}-{name}.png" for i, name in enumerate(
        ["cover", "pattern", "inner", "anchor", "balance", "friction", "test", "save"], start=1)]
    thumbs = []
    for path in files:
        im = Image.open(ASSETS / path).convert("RGB")
        im.thumbnail((270, 338), Image.Resampling.LANCZOS)
        thumbs.append(im.copy())
    sheet = Image.new("RGB", (1160, 760), PAPER)
    d = ImageDraw.Draw(sheet)
    d.text((40, 25), "DAY 04 — Carousel preview", font=f(FONT_SANS_BOLD, 28), fill=DARK)
    for i, im in enumerate(thumbs):
        x = 40 + (i % 4) * 280
        y = 80 + (i // 4) * 340
        sheet.paste(im, (x, y))
    sheet.save(ASSETS / "contact-sheet.png", optimize=True)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    cover()
    two_paths()
    diagnostic("03-inner.png", 1, ["Inner dan", "posisi rambut"],
               ["Cek dasar yang menjaga", "kain tetap di tempat."],
               ["Inner yang terlalu longgar", "atau licin bisa memberi", "lebih sedikit grip."],
               ["Pilih fit yang stabil,", "tetapi tetap nyaman."], icon_inner)
    diagnostic("04-anchor.png", 2, ["Titik kunci", "di bawah dagu"],
               ["Rapikan dua sisi", "sebelum dikunci."],
               ["Titik yang terlalu longgar", "membuat bagian depan", "lebih mudah berubah."],
               ["Kunci secukupnya—", "jangan sampai menekan."], icon_anchor, True)
    diagnostic("05-balance.png", 3, ["Panjang dan", "lipatan kain"],
               ["Periksa gaya tarik", "dari kedua sisi."],
               ["Satu sisi yang jauh lebih", "berat atau lipatan menumpuk", "bisa menarik bentuk depan."],
               ["Seimbangkan panjang dan", "kurangi lapisan berlebih."], icon_balance)
    diagnostic("06-friction.png", 4, ["Gesekan di", "sekitar wajah"],
               ["Cek apa yang menyentuh", "hijab saat bergerak."],
               ["Kacamata, masker, kerah,", "angin, atau tali tas dapat", "menggeser kain."],
               ["Pasang aksesori setelah", "dasar hijab stabil."], icon_friction, True)
    movement_test()
    closing()
    story(1, ["Hijab selalu", "maju?"],
          ["Jangan buru-buru", "salahkan bahannya.", "Ada empat bagian", "yang bisa dicek dulu."],
          "Checklist lengkap ada di carousel terbaru.")
    story(2, ["Mulai maju", "kapan?"],
          ["Baru dipakai atau", "setelah banyak bergerak?", "Polanya menentukan", "apa yang dicek dulu."],
          "Tambahkan Poll: BARU DIPAKAI / SETELAH GERAK", True, True)
    story(3, ["Bagian mana yang", "paling cepat", "bergeser?"],
          ["Tepi dekat dahi,", "sisi pipi, atau", "bagian bawah dagu?"],
          "Tambahkan Questions: Ceritakan di sini", False, True)
    contact_sheet()
