from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "white-hijab-source.png"
CW, CH = 1080, 1350
SW, SH = 1080, 1920

CREAM = "#F5EFE7"
PAPER = "#FFFDF9"
INK = "#282522"
MUTED = "#6F665F"
TAUPE = "#A58673"
SAND = "#D9C3B1"
LINE = "#DCCFC3"
WHITE = "#FFFFFF"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def f(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def txt(draw, xy, value, size, fill=INK, bold=False, anchor="la", spacing=10):
    draw.multiline_text(xy, value, font=f(size, bold), fill=fill,
                        anchor=anchor, spacing=spacing)


def rounded(draw, xy, radius=32, fill=PAPER, outline=None, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill,
                           outline=outline, width=width)


def crop(img, size, anchor_x=0.5, anchor_y=0.4):
    target = size[0] / size[1]
    ratio = img.width / img.height
    if ratio > target:
        nw = int(img.height * target)
        left = int((img.width - nw) * anchor_x)
        img = img.crop((left, 0, left + nw, img.height))
    else:
        nh = int(img.width / target)
        top = int((img.height - nh) * anchor_y)
        img = img.crop((0, top, img.width, top + nh))
    return img.resize(size, Image.Resampling.LANCZOS)


def footer(draw, h=CH):
    txt(draw, (64, h - 48), "@hijabsyaricoid", 24, fill=MUTED, anchor="ls")


def header(draw, title, subtitle=None):
    txt(draw, (64, 66), title, 62, bold=True, spacing=7)
    if subtitle:
        txt(draw, (64, 226), subtitle, 30, fill=MUTED, spacing=7)


def cover(src):
    base = crop(src, (CW, CH), 0.78, 0.28)
    overlay = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for y in range(CH):
        a = int(228 * max(0, 1 - y / 920))
        od.rectangle((0, y, CW, y + 1), fill=(245, 239, 231, a))
    od.rectangle((0, 0, 570, CH), fill=(245, 239, 231, 172))
    base = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(base)
    txt(d, (64, 112), "Hijab putih terlihat\nmenerawang?", 76, bold=True, spacing=4)
    txt(d, (64, 342), "Cek 4 hal ini sebelum dipakai.", 34, fill=MUTED)
    rounded(d, (64, 448, 536, 552), radius=30, fill="#FFFDF9E8")
    txt(d, (300, 500), "kain · cahaya · tarikan · inner", 25,
        fill=INK, bold=True, anchor="mm")
    footer(d)
    return base


def overview():
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "Putih bukan satu-satunya\nfaktor", "Kesan menerawang bisa berubah karena empat hal ini.")
    items = [
        ("01", "KONSTRUKSI KAIN", "Ketebalan dan kerapatan antarbenang"),
        ("02", "ARAH CAHAYA", "Terutama saat cahaya datang dari belakang"),
        ("03", "TARIKAN KAIN", "Ruang antarbenang dapat terlihat lebih terbuka"),
        ("04", "INNER & KONTRAS", "Latar yang kontras lebih mudah terbaca"),
    ]
    y = 342
    for num, title, sub in items:
        rounded(d, (64, y, 1016, y + 182), radius=34, fill=PAPER, outline=LINE)
        d.ellipse((96, y + 48, 176, y + 128), fill=TAUPE)
        txt(d, (136, y + 88), num, 26, fill=WHITE, bold=True, anchor="mm")
        txt(d, (214, y + 48), title, 32, bold=True)
        txt(d, (214, y + 100), sub, 27, fill=MUTED)
        y += 205
    footer(d)
    return base


def photo_card(src, title, body, badge, position=0.76):
    base = Image.new("RGB", (CW, CH), CREAM)
    pic = crop(src, (CW, 720), position, 0.2)
    base.paste(pic, (0, 0))
    d = ImageDraw.Draw(base)
    rounded(d, (48, 630, 1032, 1286), radius=48, fill=PAPER)
    d.rounded_rectangle((80, 680, 274, 730), radius=25, fill=TAUPE)
    txt(d, (177, 705), badge, 24, fill=WHITE, bold=True, anchor="mm")
    txt(d, (80, 786), title, 58, bold=True, spacing=7)
    txt(d, (80, 970), body, 31, fill=MUTED, spacing=11)
    footer(d)
    return base


def light_slide(src):
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "2. Cek arah cahaya", "Kain yang sama bisa tampak berbeda.")
    left = crop(src, (456, 520), 0.84, 0.15)
    right = ImageEnhance.Brightness(left).enhance(0.78)
    right = ImageEnhance.Contrast(right).enhance(0.9)
    base.paste(left, (64, 352))
    base.paste(right, (560, 352))
    d = ImageDraw.Draw(base)
    rounded(d, (94, 802, 490, 862), radius=28, fill="#FFFDF9E8")
    txt(d, (292, 832), "CAHAYA DARI BELAKANG", 22, bold=True, anchor="mm")
    rounded(d, (590, 802, 986, 862), radius=28, fill="#FFFDF9E8")
    txt(d, (788, 832), "CAHAYA DARI DEPAN", 22, bold=True, anchor="mm")
    txt(d, (64, 942), "Backlight menonjolkan cahaya yang lolos\nmelalui kain. Jadi, cek juga dekat jendela—\nbukan hanya di kamar yang redup.", 34, spacing=12)
    footer(d)
    return base


def tension_slide():
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "3. Cek saat kain tertarik", "Ketegangan bisa mengubah tampilan permukaan kain.")
    for i, (label, gap, x0) in enumerate([("RELAKS", 14, 64), ("TERTARIK", 27, 560)]):
        rounded(d, (x0, 354, x0 + 456, 842), radius=36, fill=PAPER, outline=LINE)
        for y in range(410, 728, gap):
            d.line((x0 + 42, y, x0 + 414, y), fill=SAND, width=5 if i == 0 else 3)
        for x in range(x0 + 42, x0 + 415, gap):
            d.line((x, 410, x, 728), fill="#E8D9CC", width=5 if i == 0 else 3)
        txt(d, (x0 + 228, 790), label, 27, bold=True, anchor="mm")
    txt(d, (64, 932), "Perhatikan area yang sering tertarik saat styling:\npelipis, bawah dagu, dan lipatan depan.", 39, bold=True, spacing=11)
    txt(d, (64, 1094), "Coba bentuk hijab seperti biasa, lalu lihat lagi\ndi bawah cahaya terang.", 31, fill=MUTED, spacing=10)
    footer(d)
    return base


def inner_slide():
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "4. Cek inner & kontras", "Latar di balik kain ikut memengaruhi yang terlihat mata.")
    swatches = [("PUTIH", "#F7F4EF"), ("SKIN-TONE", "#C9A58C"), ("GELAP", "#463D38")]
    x = 64
    for label, color in swatches:
        rounded(d, (x, 382, x + 292, 770), radius=36, fill=color, outline=LINE)
        overlay = Image.new("RGBA", (244, 250), (255, 255, 255, 150))
        base.paste(overlay, (x + 24, 432), overlay)
        d = ImageDraw.Draw(base)
        txt(d, (x + 146, 822), label, 25, bold=True, anchor="mm")
        x += 330
    rounded(d, (64, 916, 1016, 1172), radius=38, fill=PAPER, outline=LINE)
    txt(d, (96, 950), "Tidak ada satu warna inner yang\nselalu paling benar.", 31, bold=True, spacing=7)
    txt(d, (96, 1054), "Pilih yang memberi cakupan dan hasil visual yang\nkamu inginkan, lalu uji bersama hijabnya.", 28, fill=MUTED, spacing=8)
    footer(d)
    return base


def test_slide():
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "Tes 30 detik\nsebelum berangkat", "Lakukan dengan styling yang benar-benar akan dipakai.")
    checks = [
        "Hadapkan kain ke cahaya jendela.",
        "Bandingkan satu dan dua lapis.",
        "Bentuk hijab, lalu cek area yang tertarik.",
        "Ambil foto: backlight dan front light.",
    ]
    y = 366
    for i, item in enumerate(checks, 1):
        rounded(d, (64, y, 1016, y + 162), radius=34, fill=PAPER, outline=LINE)
        d.ellipse((94, y + 42, 172, y + 120), fill=TAUPE)
        txt(d, (133, y + 81), str(i), 29, fill=WHITE, bold=True, anchor="mm")
        txt(d, (206, y + 81), item, 32, bold=True, anchor="lm")
        y += 184
    footer(d)
    return base


def recap(src):
    base = crop(src, (CW, CH), 0.78, 0.3)
    shade = Image.new("RGBA", (CW, CH), (35, 31, 28, 85))
    base = Image.alpha_composite(base.convert("RGBA"), shade).convert("RGB")
    d = ImageDraw.Draw(base)
    rounded(d, (54, 96, 1026, 1168), radius=50, fill="#FFFDF9EB")
    txt(d, (96, 146), "Sebelum memilih hijab putih,", 35, fill=MUTED)
    txt(d, (96, 212), "cek 4 hal:", 66, bold=True)
    items = ["kerapatan kain", "arah cahaya", "tarikan saat styling", "inner & kontras"]
    y = 374
    for item in items:
        d.ellipse((104, y + 5, 138, y + 39), fill=TAUPE)
        d.line((113, y + 22, 123, y + 32), fill=WHITE, width=4)
        d.line((123, y + 32, 137, y + 12), fill=WHITE, width=4)
        txt(d, (166, y), item, 38, bold=True)
        y += 118
    txt(d, (96, 906), "Kalau masih kurang tertutup, tambah inner/lapis\natau pilih kain yang lebih rapat.", 31, fill=MUTED, spacing=9)
    txt(d, (96, 1054), "Simpan checklist ini untuk fitting berikutnya.", 30, bold=True)
    footer(d)
    return base


def story_cover(src):
    base = crop(src, (SW, SH), 0.78, 0.25)
    ov = Image.new("RGBA", (SW, SH), (245, 239, 231, 0))
    od = ImageDraw.Draw(ov)
    od.rectangle((0, 0, SW, 900), fill=(245, 239, 231, 224))
    base = Image.alpha_composite(base.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(base)
    txt(d, (72, 150), "Hijab putihmu pernah\ntampak beda saat di luar?", 66, bold=True, spacing=8)
    txt(d, (72, 352), "Cahaya bisa mengubah yang terlihat.", 32, fill=MUTED)
    rounded(d, (72, 510, 1008, 820), radius=42, fill="#FFFDF9E8", outline=LINE)
    txt(d, (540, 585), "TAMBAHKAN POLL", 28, fill=TAUPE, bold=True, anchor="mm")
    txt(d, (540, 680), "Pernah  /  Sering", 44, bold=True, anchor="mm")
    footer(d, SH)
    return base


def story_check():
    base = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(base)
    txt(d, (72, 150), "Checklist cepat\nhijab putih", 74, bold=True, spacing=8)
    items = ["Kerapatan kain", "Cahaya belakang", "Tarikan styling", "Inner & kontras"]
    y = 510
    for item in items:
        rounded(d, (72, y, 1008, y + 206), radius=40, fill=PAPER, outline=LINE)
        d.rounded_rectangle((112, y + 62, 194, y + 144), radius=18, outline=TAUPE, width=5)
        txt(d, (244, y + 103), item, 40, bold=True, anchor="lm")
        y += 238
    txt(d, (72, 1580), "Tes dekat jendela sebelum berangkat.", 34, fill=MUTED)
    footer(d, SH)
    return base


def story_question(src):
    base = crop(src, (SW, SH), 0.77, 0.28)
    ov = Image.new("RGBA", (SW, SH), (40, 35, 31, 70))
    base = Image.alpha_composite(base.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(base)
    rounded(d, (54, 128, 1026, 1040), radius=48, fill="#FFFDF9ED")
    txt(d, (96, 208), "Yang paling bikin repot\nsaat pakai hijab putih?", 64, bold=True, spacing=8)
    txt(d, (96, 430), "menerawang · warna inner\natau jatuh kain?", 37, fill=MUTED, spacing=10)
    rounded(d, (96, 620, 984, 930), radius=38, fill="#F4ECE4", outline=LINE)
    txt(d, (540, 698), "TAMBAHKAN QUESTIONS", 26, fill=TAUPE, bold=True, anchor="mm")
    txt(d, (540, 806), "Aku paling sulit di…", 38, bold=True, anchor="mm")
    footer(d, SH)
    return base


def sheet(files, out, cols=4, thumb=(270, 338)):
    rows = (len(files) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows), WHITE)
    for i, path in enumerate(files):
        im = Image.open(path).convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        canvas.paste(im, ((i % cols) * thumb[0], (i // cols) * thumb[1]))
    canvas.save(out, optimize=True)


def save_png(image, path):
    image.convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(path, optimize=True)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    slides = [cover(src), overview(),
              photo_card(src, "1. Cek konstruksi kain", "Pegang ke arah cahaya lembut. Bandingkan satu\ndan dua lapis. Kain yang tampak rapat dari depan\nbelum tentu memberi hasil sama saat backlight.", "KAIN"),
              light_slide(src), tension_slide(), inner_slide(), test_slide(), recap(src)]
    slide_paths = []
    for i, im in enumerate(slides, 1):
        path = ASSETS / f"slide-{i:02d}.png"
        save_png(im, path)
        slide_paths.append(path)
    stories = [story_cover(src), story_check(), story_question(src)]
    story_paths = []
    for i, im in enumerate(stories, 1):
        path = ASSETS / f"story-{i:02d}.png"
        save_png(im, path)
        story_paths.append(path)
    sheet(slide_paths, ASSETS / "contact-sheet.png")
    sheet(story_paths, ASSETS / "stories-contact-sheet.png", cols=3, thumb=(270, 480))


if __name__ == "__main__":
    main()
