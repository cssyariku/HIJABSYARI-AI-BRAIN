"""Render Day 29 carousel, Stories, and QA previews.

Run: python CONTENT/DAY-29/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "editorial-workflow-source.png"
CW, CH = 1080, 1350
SW, SH = 1080, 1920
PAPER = (249, 244, 237)
CREAM = (238, 226, 211)
DARK = (52, 40, 34)
MUTED = (116, 95, 84)
LINE = (216, 198, 184)
COCOA = (108, 72, 58)
SAGE = (133, 144, 126)
ROSE = (180, 133, 135)
TAUPE = (158, 137, 125)
CHARCOAL = (65, 62, 61)
WHITE = (255, 255, 255)
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def rounded(draw, box, radius=30, fill=PAPER, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


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


def footer(draw, h=CH, light=False):
    draw.text((64, h - 42), "@hijabsyaricoid", font=font(SANS, 22),
              fill=PAPER if light else MUTED, anchor="ls")


def source():
    return Image.open(SOURCE).convert("RGB")


def photo(size, centering=(0.62, 0.52)):
    return ImageOps.fit(source(), size, Image.Resampling.LANCZOS, centering=centering)


def badge(draw, num, color=COCOA, xy=(64, 70)):
    x, y = xy
    rounded(draw, (x, y, x + 132, y + 64), radius=30, fill=color)
    draw.text((x + 66, y + 32), num, font=font(SANS_BOLD, 23), fill=PAPER, anchor="mm")


def cover():
    im = photo((CW, CH), (0.56, 0.48))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle((44, 55, 1018, 710), radius=42, fill=(*PAPER, 246))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    text_block(d, "28 paket kemudian", (78, 105), font(SERIF_BOLD, 68), DARK, 880, 82)
    text_block(d, "7 hal yang kita pelajari", (78, 300), font(SERIF_BOLD, 54), COCOA, 870, 68)
    rounded(d, (78, 500, 926, 620), radius=34, fill=CREAM, outline=LINE)
    d.text((502, 540), "Pelajaran produksi, bukan hasil performa.",
           font=font(SANS_BOLD, 25), fill=DARK, anchor="mm")
    d.text((502, 585), "Day 1–28 READY · belum ada Insights tercatat",
           font=font(SANS, 22), fill=MUTED, anchor="mm")
    footer(d, light=True)
    return im


def lesson_photo(num, title, body, accent, crop_center=(0.66, 0.5), bullets=None):
    im = Image.new("RGB", (CW, CH), PAPER)
    im.paste(photo((480, CH), crop_center), (600, 0))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rectangle((0, 0, 660, CH), fill=(*PAPER, 250))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    badge(d, num, accent)
    y = text_block(d, title, (64, 190), font(SERIF_BOLD, 56), DARK, 520, 68)
    y = text_block(d, body, (64, y + 45), font(SANS, 29), MUTED, 510, 44)
    if bullets:
        d.line((64, y + 38, 530, y + 38), fill=LINE, width=2)
        yy = y + 88
        for item in bullets:
            d.ellipse((64, yy + 9, 84, yy + 29), fill=accent)
            d.text((108, yy), item, font=font(SANS_BOLD, 23), fill=DARK)
            yy += 72
    footer(d)
    return im


def comparison_slide():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    badge(d, "02", SAGE)
    text_block(d, "Kontrol variabel saat membandingkan", (64, 180),
               font(SERIF_BOLD, 54), DARK, 930, 66)
    rounded(d, (64, 390, 1016, 925), radius=38, fill=PAPER, outline=LINE)
    fixed = ["model", "outfit", "pose", "cahaya"]
    x = 100
    for i, label in enumerate(fixed):
        rounded(d, (x, 470, x + 184, 610), radius=28, fill=(227, 218, 207))
        d.text((x + 92, 525), label.upper(), font=font(SANS_BOLD, 20), fill=DARK, anchor="mm")
        d.text((x + 92, 573), "tetap", font=font(SANS, 22), fill=MUTED, anchor="mm")
        if i < 3:
            d.text((x + 204, 540), "+", font=font(SANS_BOLD, 32), fill=COCOA, anchor="mm")
        x += 224
    d.line((150, 700, 930, 700), fill=LINE, width=4)
    d.polygon([(900, 684), (930, 700), (900, 716)], fill=COCOA)
    rounded(d, (275, 755, 805, 865), radius=30, fill=SAGE)
    d.text((540, 810), "SATU HAL BERUBAH", font=font(SANS_BOLD, 27), fill=WHITE, anchor="mm")
    d.text((64, 1010), "Hasilnya: perbedaan lebih mudah dijelaskan—",
           font=font(SANS_BOLD, 27), fill=DARK)
    d.text((64, 1060), "bukan klaim bahwa satu pilihan cocok untuk semua.",
           font=font(SANS, 26), fill=MUTED)
    footer(d)
    return im


def decision_slide():
    im = Image.new("RGB", (CW, CH), PAPER)
    d = ImageDraw.Draw(im)
    badge(d, "03", ROSE)
    text_block(d, "Jangan berhenti di daftar", (64, 180), font(SERIF_BOLD, 58), DARK, 930, 70)
    rounded(d, (64, 390, 420, 960), radius=36, fill=CREAM, outline=LINE)
    d.text((242, 455), "DAFTAR", font=font(SANS_BOLD, 26), fill=MUTED, anchor="mm")
    for i in range(4):
        d.line((112, 560 + i * 92, 372, 560 + i * 92), fill=TAUPE, width=8)
    d.text((500, 690), "→", font=font(SERIF_BOLD, 64), fill=COCOA, anchor="mm")
    rounded(d, (580, 390, 1016, 960), radius=36, fill=(234, 220, 214), outline=ROSE)
    d.text((798, 455), "KEPUTUSAN", font=font(SANS_BOLD, 26), fill=COCOA, anchor="mm")
    cards = ["CHOOSER", "CHECKLIST", "LANGKAH"]
    y = 550
    for item in cards:
        rounded(d, (642, y, 954, y + 90), radius=28, fill=PAPER)
        d.text((798, y + 45), item, font=font(SANS_BOLD, 22), fill=DARK, anchor="mm")
        y += 125
    d.text((64, 1050), "Utility muncul saat audience tahu langkah berikutnya.",
           font=font(SANS_BOLD, 27), fill=DARK)
    footer(d)
    return im


def format_slide():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    badge(d, "05", SAGE)
    text_block(d, "Format punya tugas berbeda", (64, 180), font(SERIF_BOLD, 56), DARK, 930, 68)
    cards = [
        ("REEL", "discovery", COCOA, "jangkauan + retention"),
        ("CAROUSEL", "depth", ROSE, "save + share"),
        ("STORIES", "research", SAGE, "poll + reply"),
    ]
    y = 430
    for label, role, color, note in cards:
        rounded(d, (64, y, 1016, y + 210), radius=36, fill=PAPER, outline=LINE)
        rounded(d, (98, y + 52, 330, y + 158), radius=28, fill=color)
        d.text((214, y + 105), label, font=font(SANS_BOLD, 23), fill=WHITE, anchor="mm")
        d.text((380, y + 48), role, font=font(SERIF_BOLD, 34), fill=DARK)
        d.text((380, y + 105), note, font=font(SANS, 25), fill=MUTED)
        y += 236
    d.text((64, 1160), "Jangan bandingkan KPI seolah tugasnya sama.",
           font=font(SANS_BOLD, 25), fill=MUTED)
    footer(d)
    return im


def claim_slide():
    im = Image.new("RGB", (CW, CH), PAPER)
    d = ImageDraw.Draw(im)
    badge(d, "06", COCOA)
    text_block(d, "Batas klaim menjaga trust", (64, 180), font(SERIF_BOLD, 58), DARK, 930, 70)
    pairs = [
        ("OBSERVASI", "bukan fakta universal"),
        ("HIPOTESIS", "bukan hasil"),
        ("VISUAL AI", "bukan testimonial"),
    ]
    y = 440
    for left, right in pairs:
        rounded(d, (64, y, 1016, y + 190), radius=34, fill=CREAM, outline=LINE)
        d.text((105, y + 48), left, font=font(SANS_BOLD, 24), fill=COCOA)
        d.text((540, y + 95), "≠", font=font(SERIF_BOLD, 44), fill=ROSE, anchor="mm")
        d.text((975, y + 48), right, font=font(SANS_BOLD, 24), fill=DARK, anchor="ra")
        y += 220
    d.text((64, 1130), "Kejelasan lebih penting daripada terdengar pasti.",
           font=font(SANS_BOLD, 27), fill=MUTED)
    footer(d)
    return im


def final_slide():
    im = photo((CW, CH), (0.6, 0.48))
    ov = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle((48, 70, 1032, 1160), radius=44, fill=(52, 40, 34, 238))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    badge(d, "07", ROSE, (82, 118))
    text_block(d, "READY bukan PUBLISHED", (82, 235), font(SERIF_BOLD, 59), PAPER, 890, 72)
    steps = [("PUBLISH", "unggah dengan bukti"), ("MEASURE", "catat Insights"), ("LEARN", "bandingkan sejenis")]
    y = 480
    for i, (label, note) in enumerate(steps):
        rounded(d, (82, y, 998, y + 150), radius=32, fill=(247, 241, 232))
        d.text((125, y + 36), f"0{i+1}", font=font(SANS_BOLD, 23), fill=COCOA)
        d.text((215, y + 30), label, font=font(SANS_BOLD, 27), fill=DARK)
        d.text((215, y + 82), note, font=font(SANS, 24), fill=MUTED)
        y += 180
    d.text((82, 1050), "Baru setelah itu tentukan winner.", font=font(SANS_BOLD, 27), fill=PAPER)
    rounded(d, (82, 1190, 998, 1282), radius=28, fill=ROSE)
    d.text((540, 1236), "Simpan recap ini · pilih poin 1–7", font=font(SANS_BOLD, 24), fill=WHITE, anchor="mm")
    footer(d, light=True)
    return im


def story_one():
    im = photo((SW, SH), (0.58, 0.5))
    ov = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle((54, 90, 1026, 760), radius=44, fill=(*PAPER, 246))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    text_block(d, "28 paket, 7 pelajaran produksi", (86, 150), font(SERIF_BOLD, 65), DARK, 880, 80)
    d.text((86, 455), "Bukan hasil performa.", font=font(SANS_BOLD, 31), fill=COCOA)
    d.text((86, 525), "Belum ada Insights yang dicatat.", font=font(SANS, 27), fill=MUTED)
    footer(d, SH, light=True)
    return im


def story_two():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Kamu lebih ingin lihat?", (72, 150), font(SERIF_BOLD, 68), DARK, 930, 82)
    cards = [("UTILITY", "chooser · checklist · solusi", COCOA), ("VISUAL", "warna · styling · inspo", SAGE)]
    y = 560
    for label, note, color in cards:
        rounded(d, (72, y, 1008, y + 310), radius=42, fill=PAPER, outline=LINE)
        rounded(d, (120, y + 64, 480, y + 164), radius=32, fill=color)
        d.text((300, y + 114), label, font=font(SANS_BOLD, 29), fill=WHITE, anchor="mm")
        d.text((120, y + 220), note, font=font(SANS_BOLD, 27), fill=MUTED)
        y += 360
    rounded(d, (72, 1450, 1008, 1730), radius=42, fill=PAPER, outline=COCOA)
    d.text((540, 1535), "Tambahkan Poll native ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 1645), "UTILITY / VISUAL", font=font(SANS_BOLD, 31), fill=DARK, anchor="mm")
    footer(d, SH)
    return im


def story_three():
    im = photo((SW, SH), (0.62, 0.52))
    ov = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rectangle((0, 0, SW, SH), fill=(52, 40, 34, 150))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    text_block(d, "Topik berikutnya?", (72, 150), font(SERIF_BOLD, 70), PAPER, 930, 86)
    d.text((72, 350), "Tulis masalah hijab yang ingin dibahas.", font=font(SANS_BOLD, 29), fill=(236, 222, 213))
    rounded(d, (72, 760, 1008, 1190), radius=44, fill=PAPER)
    d.text((540, 870), "Jawab di Questions sticker ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 1025), "Contoh: hijab licin saat kerja", font=font(SANS_BOLD, 31), fill=DARK, anchor="mm")
    footer(d, SH, light=True)
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


def sheet(images, path, cols, thumb, title):
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows + 54), WHITE)
    d = ImageDraw.Draw(canvas)
    d.text((20, 12), title, font=font(SANS_BOLD, 24), fill=DARK)
    for i, im in enumerate(images):
        canvas.paste(im.convert("RGB").resize(thumb, Image.Resampling.LANCZOS),
                     ((i % cols) * thumb[0], 54 + (i // cols) * thumb[1]))
    save_png(canvas, path)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    slides = [
        cover(),
        lesson_photo("01", "Mulai dari masalah spesifik", "Problem konkret membuat hook dan naskah lebih fokus.", COCOA, bullets=["problem", "hook", "one promise"]),
        comparison_slide(),
        decision_slide(),
        lesson_photo("04", "Realistis butuh QA", "Prompt baru permulaan. Final visual tetap harus diperiksa.", ROSE, bullets=["identity & hands", "fabric & anatomy", "dimensions & readability"]),
        format_slide(),
        claim_slide(),
        final_slide(),
    ]
    for i, im in enumerate(slides, 1):
        save_png(im, ASSETS / f"carousel-{i:02d}.png")
    stories = [story_one(), story_two(), story_three()]
    for i, im in enumerate(stories, 1):
        save_png(im, ASSETS / f"story-{i:02d}.png")
    sheet(slides, ASSETS / "contact-sheet.png", 4, (270, 338), "DAY 29 — CAROUSEL QA")
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480), "DAY 29 — STORIES QA")


if __name__ == "__main__":
    main()
