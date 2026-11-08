"""Render Day 30 Stories and QA preview.

Run: python CONTENT/DAY-30/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "topic-vote-source.png"
W, H = 1080, 1920

CREAM = "#F7F1E8"
PAPER = "#FFFDFC"
INK = "#302824"
MUTED = "#71635C"
COCOA = "#704C40"
ROSE = "#B98787"
SAGE = "#879181"
TAUPE = "#C9B8A7"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(size, bold=False, serif=False):
    return ImageFont.truetype(SERIF if serif else (BOLD if bold else REG), size)


def fit(img, size, centering=(0.5, 0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=centering)


def panels(src):
    gap = 8
    mx, my = src.width // 2, src.height // 2
    return [
        src.crop((0, 0, mx - gap, my - gap)),
        src.crop((mx + gap, 0, src.width, my - gap)),
        src.crop((0, my + gap, mx - gap, src.height)),
        src.crop((mx + gap, my + gap, src.width, src.height)),
    ]


def wrap(draw, text, xy, width, fnt, fill=INK, spacing=12):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + spacing
    return y


def brand(draw, light=False):
    draw.text((72, 1840), "@hijabsyaricoid", font=font(22), fill=CREAM if light else MUTED)


def save_png(im, name):
    path = ASSETS / name
    im = im.convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    im.save(path, optimize=True)
    with Image.open(path) as check:
        if check.size != (W, H):
            raise RuntimeError(f"Bad dimensions: {path} {check.size}")
    return path


def story_one(src):
    bg = fit(src, (W, H), centering=(0.5, 0.5)).convert("RGB")
    d = ImageDraw.Draw(bg, "RGBA")
    d.rectangle((0, 0, W, H), fill=(38, 28, 25, 58))
    d.rounded_rectangle((58, 90, 1022, 610), radius=42, fill=(255, 253, 250, 242))
    y = wrap(d, "Bulan berikutnya,", (96, 145), 860, font(64, serif=True), INK, 5)
    d.text((96, y + 5), "kamu yang pilih.", font=font(64, serif=True), fill=COCOA)
    d.text((96, 390), "Empat topik untuk konten Hijab Syari berikutnya.", font=font(28), fill=MUTED)
    d.rounded_rectangle((96, 470, 984, 555), radius=25, fill=TAUPE)
    d.text((540, 512), "Pilih di dua Poll · tulis detail di Questions", font=font(23, True), fill=INK, anchor="mm")
    brand(d, light=True)
    return bg


def pair_story(p1, p2, heading, labels, accent):
    im = Image.new("RGB", (W, H), CREAM)
    im.paste(fit(p1, (540, H), centering=(0.5, 0.42)), (0, 0))
    im.paste(fit(p2, (540, H), centering=(0.5, 0.42)), (540, 0))
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle((0, 0, W, H), fill=(36, 27, 24, 34))
    d.rounded_rectangle((54, 74, 1026, 485), radius=42, fill=(255, 253, 250, 245))
    wrap(d, heading, (94, 125), 850, font(50, serif=True), INK, 6)
    d.rounded_rectangle((48, 870, 518, 1015), radius=34, fill=(255, 253, 250, 232))
    d.rounded_rectangle((562, 870, 1032, 1015), radius=34, fill=(255, 253, 250, 232))
    d.text((283, 942), labels[0], font=font(28, True), fill=INK, anchor="mm")
    d.text((797, 942), labels[1], font=font(28, True), fill=INK, anchor="mm")
    d.rounded_rectangle((130, 1300, 950, 1685), radius=42, fill=(255, 253, 250, 246), outline=accent, width=4)
    d.text((540, 1382), "Tambahkan Poll native ↓", font=font(25), fill=MUTED, anchor="mm")
    d.rounded_rectangle((190, 1460, 890, 1545), radius=24, fill=accent)
    d.rounded_rectangle((190, 1575, 890, 1660), radius=24, fill=COCOA)
    d.text((540, 1503), labels[0], font=font(25, True), fill=CREAM, anchor="mm")
    d.text((540, 1618), labels[1], font=font(25, True), fill=CREAM, anchor="mm")
    brand(d, light=True)
    return im


def story_four(src):
    bg = fit(src, (W, H), centering=(0.72, 0.55)).convert("RGB")
    d = ImageDraw.Draw(bg, "RGBA")
    d.rectangle((0, 0, W, H), fill=(39, 29, 25, 140))
    y = wrap(d, "Topik spesifik versimu?", (72, 120), 900, font(60, serif=True), CREAM, 8)
    d.text((72, y + 20), "Tulis masalah, konteks, atau warna outfitmu.", font=font(27), fill="#EADFD5")
    d.rounded_rectangle((88, 870, 992, 1370), radius=48, fill=(255, 253, 250, 246))
    d.text((540, 985), "Tambahkan Questions sticker ↓", font=font(25), fill=MUTED, anchor="mm")
    d.rounded_rectangle((150, 1080, 930, 1270), radius=34, fill=CREAM, outline=ROSE, width=4)
    d.text((540, 1140), "Contoh:", font=font(23, True), fill=COCOA, anchor="mm")
    d.text((540, 1205), "hijab licin saat kerja", font=font(30, True), fill=INK, anchor="mm")
    d.text((540, 1475), "Jawabanmu jadi bahan riset kalender berikutnya.", font=font(24, True), fill=CREAM, anchor="mm")
    d.text((540, 1525), "Belum ada hasil yang diklaim.", font=font(22), fill="#EADFD5", anchor="mm")
    brand(d, light=True)
    return bg


def contact_sheet(paths):
    thumb_w, thumb_h = 270, 480
    sheet = Image.new("RGB", (1080, 560), "#E2D8CE")
    d = ImageDraw.Draw(sheet)
    d.rectangle((0, 0, 1080, 80), fill=PAPER)
    d.text((28, 24), "DAY 30 — STORIES QA", font=font(30, True), fill=INK)
    for i, path in enumerate(paths):
        pic = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(pic, (i * thumb_w, 80))
    sheet.save(ASSETS / "contact-sheet.png", optimize=True)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    p = panels(src)
    frames = [
        story_one(src),
        pair_story(p[0], p[1], "Mana yang paling ingin kamu bereskan?", ("STAY RAPI", "PADU WARNA"), SAGE),
        pair_story(p[2], p[3], "Mana yang paling ingin kamu pahami?", ("PILIH BAHAN", "FRAMING GAYA"), ROSE),
        story_four(src),
    ]
    paths = [save_png(frame, f"story-{i:02d}.png") for i, frame in enumerate(frames, 1)]
    contact_sheet(paths)


if __name__ == "__main__":
    main()
