from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "undertone-portrait-source.jpg"
CW, CH = 1080, 1350
SW, SH = 1080, 1920

CREAM = "#F5EFE7"
PAPER = "#FFFDF9"
INK = "#282522"
MUTED = "#6F665F"
ROSE = "#B97B82"
OLIVE = "#7A8061"
BLUE = "#778898"
TAUPE = "#9A806E"
LINE = "#DDD0C4"
WHITE = "#FFFFFF"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def text(draw, xy, value, size, fill=INK, bold=False, anchor="la", spacing=9):
    draw.multiline_text(xy, value, font=font(size, bold), fill=fill,
                        anchor=anchor, spacing=spacing)


def rounded(draw, xy, radius=32, fill=PAPER, outline=None, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def crop(img, size, anchor_x=.5, anchor_y=.35):
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


def footer(draw, height=CH):
    text(draw, (64, height - 46), "@hijabsyaricoid", 22, fill=MUTED, anchor="ls")


def header(draw, title, subtitle=None):
    text(draw, (64, 72), title, 59, bold=True, spacing=6)
    if subtitle:
        text(draw, (64, 226), subtitle, 29, fill=MUTED, spacing=7)


def cover(src):
    base = crop(src, (CW, CH), .5, .38)
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.rectangle((0, 0, 625, CH), fill=(245, 239, 231, 228))
    for x in range(625, 850):
        alpha = max(0, int(228 * (1 - (x - 625) / 225)))
        od.rectangle((x, 0, x + 1, CH), fill=(245, 239, 231, alpha))
    base = Image.alpha_composite(base.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(base)
    text(d, (64, 112), "Undertone 101:\nMulai pilih\nwarna hijab\ndari mana?", 62, bold=True, spacing=2)
    text(d, (64, 452), "Kenali arah warna, lalu tes\ndi cahaya yang tepat.", 31, fill=MUTED, spacing=8)
    rounded(d, (64, 570, 548, 733), radius=32, fill="#FFFDF9E8", outline=LINE)
    text(d, (92, 607), "Warm · cool · neutral", 28, bold=True)
    text(d, (92, 662), "Titik mulai, bukan aturan wajib.", 24, fill=MUTED)
    footer(d)
    return base


def overview():
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "Undertone bukan ukuran\nterang atau gelap", "Tiga arah warna untuk memulai eksplorasi.")
    data = [
        ("WARM", "Keemasan / peach", "#D8A36E"),
        ("COOL", "Pink / kebiruan", "#B78092"),
        ("NEUTRAL", "Seimbang / campuran", "#9A8B7C"),
    ]
    y = 378
    for label, sub, color in data:
        rounded(d, (64, y, 1016, y + 178), radius=36, fill=PAPER, outline=LINE)
        d.ellipse((96, y + 44, 186, y + 134), fill=color)
        text(d, (220, y + 52), label, 31, bold=True)
        text(d, (220, y + 104), sub, 28, fill=MUTED)
        y += 205
    rounded(d, (64, 1033, 1016, 1224), radius=34, fill="#EDE4DB", outline=LINE)
    text(d, (94, 1071), "Tes rumahan bisa memberi petunjuk,", 31, bold=True)
    text(d, (94, 1126), "tetapi satu tes atau satu warna tidak menentukan semuanya.", 25, fill=MUTED)
    footer(d)
    return base


def palette_slide(title, intro, colors, accent):
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, title, intro)
    y = 368
    for label, color in colors:
        rounded(d, (64, y, 1016, y + 154), radius=32, fill=PAPER, outline=LINE)
        d.rounded_rectangle((92, y + 27, 218, y + 127), radius=26, fill=color)
        text(d, (254, y + 77), label, 31, bold=True, anchor="lm")
        y += 178
    rounded(d, (64, 1082, 1016, 1228), radius=31, fill=accent)
    text(d, (92, 1118), "Referensi visual, bukan aturan wajib.", 29, fill=WHITE, bold=True)
    text(d, (92, 1168), "Warna yang kamu suka tetap valid.", 25, fill=WHITE)
    footer(d)
    return base


def test_slide():
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "Tes sederhana di rumah", "Bukan diagnosis—hanya perbandingan yang lebih konsisten.")
    items = [
        ("1", "Pilih dua hijab", "Satu hangat, satu lebih dingin."),
        ("2", "Cari cahaya jendela", "Hindari lampu kuning dan bayangan keras."),
        ("3", "Samakan kondisi", "Outfit, posisi, kamera sama; matikan filter."),
        ("4", "Lihat berdampingan", "Pilih yang kamu suka, bukan yang dianggap wajib."),
    ]
    y = 344
    for num, title, body in items:
        rounded(d, (64, y, 1016, y + 190), radius=34, fill=PAPER, outline=LINE)
        d.ellipse((94, y + 55, 174, y + 135), fill=TAUPE)
        text(d, (134, y + 95), num, 28, fill=WHITE, bold=True, anchor="mm")
        text(d, (208, y + 47), title, 31, bold=True)
        text(d, (208, y + 103), body, 25, fill=MUTED)
        y += 208
    footer(d)
    return base


def mixed_slide():
    base = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(base)
    header(d, "Kalau hasilnya campur?", "Itu wajar. Kesan warna dapat berubah.")
    items = [
        ("CAHAYA", "Pagi, sore, dan lampu indoor berbeda.", "#D8B080"),
        ("KAIN", "Tekstur, ketebalan, dan kilau ikut terbaca.", "#9B806C"),
        ("KAMERA", "White balance dan filter menggeser warna.", BLUE),
        ("PREFERENSI", "Kontras dan mood yang kamu suka juga penting.", ROSE),
    ]
    y = 360
    for label, body, color in items:
        rounded(d, (64, y, 1016, y + 168), radius=34, fill=PAPER, outline=LINE)
        d.rounded_rectangle((92, y + 34, 120, y + 134), radius=14, fill=color)
        text(d, (154, y + 38), label, 27, bold=True)
        text(d, (154, y + 89), body, 25, fill=MUTED)
        y += 190
    rounded(d, (64, 1130, 1016, 1225), radius=30, fill="#E9DED4")
    text(d, (540, 1178), "Boleh suka warna warm dan cool sekaligus.", 28, bold=True, anchor="mm")
    footer(d)
    return base


def recap(src):
    base = crop(src, (CW, CH), .48, .38)
    shade = Image.new("RGBA", (CW, CH), (35, 31, 28, 78))
    base = Image.alpha_composite(base.convert("RGBA"), shade).convert("RGB")
    d = ImageDraw.Draw(base)
    rounded(d, (52, 76, 1028, 1190), radius=48, fill="#FFFDF9ED")
    text(d, (94, 128), "Mini guide sebelum pilih warna hijab", 43, bold=True)
    groups = [
        ("WARM", "camel · terracotta · olive", "#D19A68"),
        ("COOL", "mauve · berry · blue-grey", ROSE),
        ("NEUTRAL", "taupe · soft rose · sage", "#928578"),
    ]
    y = 266
    for label, body, color in groups:
        rounded(d, (94, y, 986, y + 166), radius=33, fill=PAPER, outline=LINE)
        d.rounded_rectangle((120, y + 34, 248, y + 132), radius=24, fill=color)
        text(d, (276, y + 43), label, 26, bold=True)
        text(d, (276, y + 94), body, 25, fill=MUTED)
        y += 190
    text(d, (94, 873), "Bandingkan dua warna di cahaya alami,", 28, bold=True)
    text(d, (94, 924), "lalu tentukan sendiri. Simpan sebagai panduan awal.", 25, fill=MUTED)
    rounded(d, (94, 1028, 986, 1140), radius=30, fill=TAUPE)
    text(d, (540, 1084), "Warna apa yang paling bikin kamu ragu?", 27, fill=WHITE, bold=True, anchor="mm")
    footer(d)
    return base


def story_poll(src):
    base = crop(src, (SW, SH), .48, .36)
    ov = Image.new("RGBA", (SW, SH), (245, 239, 231, 0))
    od = ImageDraw.Draw(ov)
    od.rectangle((0, 0, SW, 940), fill=(245, 239, 231, 232))
    base = Image.alpha_composite(base.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(base)
    text(d, (72, 150), "Saat pilih warna hijab,\nkamu biasanya…", 65, bold=True, spacing=7)
    text(d, (72, 376), "Pilih yang paling sering kamu lakukan.", 31, fill=MUTED)
    rounded(d, (72, 520, 1008, 826), radius=42, fill="#FFFDF9E8", outline=LINE)
    text(d, (540, 600), "RUANG POLL INSTAGRAM", 25, fill=TAUPE, bold=True, anchor="mm")
    text(d, (540, 692), "Ikuti warna outfit", 35, bold=True, anchor="mm")
    text(d, (540, 754), "atau pilih warna yang kusuka", 29, fill=MUTED, anchor="mm")
    footer(d, SH)
    return base


def story_test():
    base = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(base)
    text(d, (72, 150), "Tes warna\ntanpa ribet", 76, bold=True, spacing=7)
    text(d, (72, 350), "Bandingkan dua hijab pada kondisi yang sama.", 31, fill=MUTED)
    items = [
        ("1", "CAHAYA ALAMI", "Dekat jendela, tanpa sinar keras."),
        ("2", "TANPA FILTER", "Jangan ubah white balance foto."),
        ("3", "OUTFIT SAMA", "Foto berdampingan agar mudah dibandingkan."),
    ]
    y = 540
    for num, title, body in items:
        rounded(d, (72, y, 1008, y + 260), radius=42, fill=PAPER, outline=LINE)
        d.ellipse((112, y + 72, 200, y + 160), fill=TAUPE)
        text(d, (156, y + 116), num, 30, fill=WHITE, bold=True, anchor="mm")
        text(d, (244, y + 67), title, 30, bold=True)
        text(d, (244, y + 126), body, 26, fill=MUTED)
        y += 294
    rounded(d, (72, 1458, 1008, 1628), radius=36, fill="#E8DED4")
    text(d, (106, 1496), "Panduan melihat perbedaan,", 29, bold=True)
    text(d, (106, 1548), "bukan menentukan warna yang wajib dipakai.", 25, fill=MUTED)
    footer(d, SH)
    return base


def story_question(src):
    base = crop(src, (SW, SH), .48, .36)
    shade = Image.new("RGBA", (SW, SH), (38, 33, 29, 62))
    base = Image.alpha_composite(base.convert("RGBA"), shade).convert("RGB")
    d = ImageDraw.Draw(base)
    rounded(d, (54, 120, 1026, 1050), radius=48, fill="#FFFDF9EF")
    text(d, (96, 208), "Warna hijab apa\nyang paling bikin\nkamu ragu?", 66, bold=True, spacing=6)
    text(d, (96, 482), "Putih, nude, abu-abu—atau warna\nyang susah dipadukan?", 31, fill=MUTED, spacing=9)
    rounded(d, (96, 674, 984, 954), radius=40, fill="#EEE4DB", outline=LINE)
    text(d, (540, 748), "RUANG QUESTIONS STICKER", 25, fill=TAUPE, bold=True, anchor="mm")
    text(d, (540, 848), "Aku paling bingung dengan…", 34, bold=True, anchor="mm")
    footer(d, SH)
    return base


def save_png(image, path):
    tmp = path.with_name(path.stem + ".rendering.png")
    if tmp.exists():
        tmp.unlink()
    image.convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(tmp, optimize=False)
    with Image.open(tmp) as check:
        check.load()
        if check.size != image.size:
            raise ValueError(f"dimension mismatch: {tmp}")
    tmp.replace(path)


def sheet(images, out, cols, thumb):
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows), WHITE)
    for i, im in enumerate(images):
        canvas.paste(im.convert("RGB").resize(thumb, Image.Resampling.LANCZOS),
                     ((i % cols) * thumb[0], (i // cols) * thumb[1]))
    save_png(canvas, out)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    slides = [
        cover(src), overview(),
        palette_slide("Kalau suka arah warm", "Mulai dari warna yang terasa hangat di mata.",
                      [("Camel / beige hangat", "#C89B74"), ("Terracotta / bata", "#A95F45"),
                       ("Olive / hijau zaitun", "#7B7950"), ("Cream hangat", "#E7D3B5")], TAUPE),
        palette_slide("Kalau suka arah cool", "Coba warna rosy, berry, atau kebiruan.",
                      [("Mauve / dusty rose", "#B48792"), ("Berry / burgundy", "#7D3547"),
                       ("Blue-grey", "#7C8D9C"), ("Putih dingin", "#F0F2F1")], ROSE),
        palette_slide("Kalau terasa neutral", "Warna seimbang bisa menjadi awal yang fleksibel.",
                      [("Taupe", "#9B8575"), ("Soft rose", "#C99D9E"),
                       ("Sage lembut", "#A5AA8A"), ("Beige seimbang", "#C6AD91")], OLIVE),
        test_slide(), mixed_slide(), recap(src),
    ]
    for i, im in enumerate(slides, 1):
        save_png(im, ASSETS / f"carousel-{i:02d}.png")
    stories = [story_poll(src), story_test(), story_question(src)]
    for i, im in enumerate(stories, 1):
        save_png(im, ASSETS / f"story-{i:02d}.png")
    sheet(slides, ASSETS / "carousel-contact-sheet.png", 4, (270, 338))
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480))


if __name__ == "__main__":
    main()
