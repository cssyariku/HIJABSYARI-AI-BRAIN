"""Render Day 32 carousel, Stories, and QA previews.

Run: python CONTENT/DAY-32/render.py
Requires: Pillow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "storage-triptych.png"

CW, CH = 1080, 1350
SW, SH = 1080, 1920
PAPER = (249, 245, 239)
CREAM = (235, 225, 213)
DARK = (53, 43, 38)
MUTED = (108, 91, 82)
LINE = (214, 197, 183)
TAUPE = (148, 119, 106)
ROSE = (185, 145, 137)
SAGE = (126, 137, 116)
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
    leading = leading or int(face.size * 1.18)
    for row in wrap(draw, value, face, max_width):
        draw.text((x, y), row, font=face, fill=fill)
        y += leading
    return y


def footer(draw, h=CH, light=False):
    draw.text((64, h - 44), "@hijabsyaricoid", font=font(SANS, 22),
              fill=PAPER if light else MUTED, anchor="ls")


def panel(index):
    src = Image.open(SOURCE).convert("RGB")
    pw = src.width / 3
    pad = 3
    left = round(index * pw) + (pad if index else 0)
    right = round((index + 1) * pw) - (pad if index < 2 else 0)
    return src.crop((left, 0, right, src.height))


def photo(index, size, centering=(.5, .5)):
    return ImageOps.fit(panel(index), size, Image.Resampling.LANCZOS, centering=centering)


def bullets(draw, items, y, accent=TAUPE, x=78, max_width=860, size=28, gap=98):
    for item in items:
        d = y
        draw.ellipse((x, d + 12, x + 22, d + 34), fill=accent)
        text_block(draw, item, (x + 48, d), font(SANS_BOLD, size), DARK, max_width, size + 14)
        y += gap
    return y


def cover():
    im = Image.new("RGB", (CW, CH), PAPER)
    im.paste(photo(0, (CW, 690), (.5, .45)), (0, 660))
    d = ImageDraw.Draw(im)
    text_block(d, "Bekas lipatan mengganggu styling?", (64, 76),
               font(SERIF_BOLD, 64), DARK, 940, 76)
    rounded(d, (64, 370, 720, 468), radius=42, fill=CREAM, outline=LINE)
    d.text((392, 419), "Cek cara simpannya.", font=font(SANS_BOLD, 31), fill=TAUPE, anchor="mm")
    footer(d, light=True)
    return im


def before_storage():
    im = Image.new("RGB", (CW, CH), CREAM)
    im.paste(photo(0, (430, 1130), (.5, .48)), (650, 110))
    d = ImageDraw.Draw(im)
    text_block(d, "Sebelum masuk lemari", (64, 76), font(SERIF_BOLD, 58), DARK, 570, 69)
    d.text((64, 245), "Empat pemeriksaan sederhana:", font=font(SANS, 26), fill=MUTED)
    bullets(d, ["Pastikan bersih", "Pastikan benar-benar kering", "Lepas pin, jarum, dan magnet", "Ratakan tanpa menarik kain"], 365, max_width=500, size=24, gap=156)
    rounded(d, (64, 1075, 600, 1182), radius=34, fill=PAPER, outline=LINE)
    d.text((332, 1128), "Mulai dari kondisi kain.", font=font(SANS_BOLD, 24), fill=TAUPE, anchor="mm")
    footer(d)
    return im


def soft_folds():
    im = Image.new("RGB", (CW, CH), PAPER)
    im.paste(photo(1, (CW, 700), (.5, .55)), (0, 650))
    d = ImageDraw.Draw(im)
    text_block(d, "Kurangi lipatan tajam", (64, 80), font(SERIF_BOLD, 64), DARK, 930, 76)
    text_block(d, "Buat lipatan lebih lebar dan longgar.", (64, 278), font(SANS_BOLD, 31), TAUPE, 900, 43)
    rounded(d, (64, 410, 930, 552), radius=38, fill=CREAM, outline=LINE)
    text_block(d, "Hindari menekan kain sampai membentuk garis keras.", (102, 450), font(SANS, 27), DARK, 780, 39)
    footer(d, light=True)
    return im


def rotate_fold():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Jangan tekan titik yang sama terus-menerus", (64, 76), font(SERIF_BOLD, 57), DARK, 930, 69)
    text_block(d, "Jika disimpan terlipat, ubah posisi garis lipatan secara berkala.", (64, 300), font(SANS, 29), MUTED, 910, 43)
    for x, label, color, direction in [(90, "HARI INI", TAUPE, "↔"), (570, "BERIKUTNYA", SAGE, "↕")]:
        rounded(d, (x, 520, x + 420, 950), radius=42, fill=PAPER, outline=LINE)
        d.text((x + 210, 590), label, font=font(SANS_BOLD, 24), fill=color, anchor="mm")
        d.text((x + 210, 745), direction, font=font(SANS_BOLD, 110), fill=color, anchor="mm")
        d.text((x + 210, 875), "garis lipatan", font=font(SANS, 24), fill=MUTED, anchor="mm")
    rounded(d, (64, 1080, 1016, 1215), radius=38, fill=DARK)
    d.text((540, 1147), "Tujuan: kurangi tekanan berulang pada satu area.", font=font(SANS_BOLD, 24), fill=PAPER, anchor="mm")
    footer(d)
    return im


def flat_or_roll():
    im = Image.new("RGB", (CW, CH), PAPER)
    d = ImageDraw.Draw(im)
    text_block(d, "Flat atau gulung longgar?", (64, 70), font(SERIF_BOLD, 61), DARK, 930, 73)
    left = photo(1, (470, 660), (.5, .55)); right = photo(2, (470, 660), (.5, .5))
    im.paste(left, (40, 300)); im.paste(right, (570, 300))
    d = ImageDraw.Draw(im)
    rounded(d, (68, 860, 482, 944), radius=36, fill=TAUPE)
    d.text((275, 902), "FLAT", font=font(SANS_BOLD, 28), fill=PAPER, anchor="mm")
    rounded(d, (598, 860, 1012, 944), radius=36, fill=ROSE)
    d.text((805, 902), "GULUNG LONGGAR", font=font(SANS_BOLD, 25), fill=PAPER, anchor="mm")
    text_block(d, "Pilih dari struktur, detail, kondisi, dan care label kain—bukan kebiasaan semata.", (64, 1010), font(SANS, 28), DARK, 940, 42)
    footer(d)
    return im


def environment():
    im = Image.new("RGB", (CW, CH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Ruang simpan ikut berpengaruh", (64, 76), font(SERIF_BOLD, 60), DARK, 930, 72)
    cards = [("KERING", "Pastikan kain tidak lembap", TAUPE), ("TEDUH", "Jauh dari cahaya langsung", ROSE), ("BERVENTILASI", "Hindari ruang pengap", SAGE), ("STABIL", "Jauh dari panas berlebih", (117, 126, 143))]
    y = 340
    for title, body, color in cards:
        rounded(d, (64, y, 1016, y + 180), radius=38, fill=PAPER, outline=LINE)
        d.ellipse((96, y + 49, 176, y + 129), fill=color)
        d.text((215, y + 42), title, font=font(SANS_BOLD, 27), fill=DARK)
        d.text((215, y + 101), body, font=font(SANS, 25), fill=MUTED)
        y += 200
    d.text((64, 1195), "Prinsip umum—sesuaikan dengan ruang dan care label.", font=font(SANS_BOLD, 23), fill=TAUPE)
    footer(d)
    return im


def pressure():
    im = Image.new("RGB", (CW, CH), PAPER)
    im.paste(photo(1, (470, 1080), (.5, .55)), (610, 180))
    d = ImageDraw.Draw(im)
    text_block(d, "Batasi tekanan & gesekan", (64, 76), font(SERIF_BOLD, 58), DARK, 530, 69)
    y = bullets(d, ["Jangan menumpuk terlalu berat", "Beri pemisah bila kain mudah tersangkut", "Susun agar mudah diambil tanpa menarik tumpukan"], 360, max_width=470, size=24, gap=225)
    rounded(d, (64, y + 5, 540, y + 130), radius=34, fill=CREAM, outline=LINE)
    text_block(d, "Akses mudah = lebih sedikit tarikan dan bongkar tumpukan.", (92, y + 35), font(SANS_BOLD, 22), TAUPE, 420, 32)
    footer(d)
    return im


def reset():
    im = Image.new("RGB", (CW, CH), (226, 212, 197))
    d = ImageDraw.Draw(im)
    text_block(d, "Reset lemari 60 detik", (64, 76), font(SERIF_BOLD, 64), DARK, 930, 76)
    steps = [("01", "CEK", "bersih dan kering"), ("02", "LEPAS", "pin, jarum, magnet"), ("03", "PILIH", "flat atau gulung longgar"), ("04", "SIMPAN", "tanpa tekanan berat")]
    y = 300
    for num, title, body in steps:
        rounded(d, (64, y, 1016, y + 170), radius=38, fill=PAPER, outline=LINE)
        d.ellipse((94, y + 44, 176, y + 126), fill=TAUPE)
        d.text((135, y + 85), num, font=font(SANS_BOLD, 23), fill=PAPER, anchor="mm")
        d.text((215, y + 35), title, font=font(SANS_BOLD, 26), fill=DARK)
        d.text((215, y + 94), body, font=font(SANS, 24), fill=MUTED)
        y += 188
    rounded(d, (64, 1085, 1016, 1215), radius=38, fill=DARK)
    d.text((540, 1130), "Simpan checklist ini.", font=font(SANS_BOLD, 29), fill=PAPER, anchor="mm")
    d.text((540, 1175), "Tim lipat, gulung, atau gantung?", font=font(SANS, 24), fill=PAPER, anchor="mm")
    footer(d)
    return im


def story_one():
    im = Image.new("RGB", (SW, SH), PAPER)
    im.paste(photo(0, (SW, 1050), (.5, .45)), (0, 870))
    d = ImageDraw.Draw(im)
    text_block(d, "Bekas lipatan muncul lagi?", (72, 145), font(SERIF_BOLD, 68), DARK, 930, 82)
    text_block(d, "Cek bukan hanya setrika—cara simpannya juga.", (72, 410), font(SANS_BOLD, 31), TAUPE, 900, 46)
    rounded(d, (72, 595, 940, 760), radius=42, fill=CREAM, outline=LINE)
    d.text((506, 650), "Bersih · kering · tanpa pin", font=font(SANS_BOLD, 27), fill=DARK, anchor="mm")
    d.text((506, 705), "lipatan longgar · tekanan ringan", font=font(SANS, 24), fill=MUTED, anchor="mm")
    footer(d, SH, light=True)
    return im


def story_two():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Metode yang paling sering kamu pakai?", (72, 145), font(SERIF_BOLD, 65), DARK, 930, 80)
    im.paste(photo(1, (430, 850), (.5, .55)), (72, 470))
    im.paste(photo(2, (430, 850), (.5, .5)), (578, 470))
    d = ImageDraw.Draw(im)
    rounded(d, (92, 1240, 482, 1330), radius=40, fill=TAUPE)
    d.text((287, 1285), "LIPAT", font=font(SANS_BOLD, 28), fill=PAPER, anchor="mm")
    rounded(d, (598, 1240, 988, 1330), radius=40, fill=ROSE)
    d.text((793, 1285), "GULUNG", font=font(SANS_BOLD, 28), fill=PAPER, anchor="mm")
    rounded(d, (72, 1480, 1008, 1750), radius=42, fill=PAPER, outline=LINE)
    d.text((540, 1580), "Tambahkan Poll native ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 1670), "LIPAT / GULUNG", font=font(SANS_BOLD, 31), fill=DARK, anchor="mm")
    footer(d, SH)
    return im


def story_three():
    im = Image.new("RGB", (SW, SH), CREAM)
    d = ImageDraw.Draw(im)
    text_block(d, "Bagian paling merepotkan saat menyimpan hijab?", (72, 145), font(SERIF_BOLD, 63), DARK, 930, 78)
    d.text((72, 500), "Tumpukan, ruang, lipatan, atau lainnya?", font=font(SANS_BOLD, 28), fill=TAUPE)
    rounded(d, (72, 690, 1008, 1230), radius=48, fill=PAPER, outline=LINE)
    d.text((540, 820), "Tambahkan Questions native ↓", font=font(SANS_BOLD, 25), fill=MUTED, anchor="mm")
    d.text((540, 1010), "Tulis masalahmu di sini", font=font(SANS_BOLD, 31), fill=DARK, anchor="mm")
    d.text((72, 1500), "Jawabanmu membantu Hijab Fix berikutnya.", font=font(SANS_BOLD, 28), fill=MUTED)
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


def sheet(images, path, cols, thumb, title):
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows + 54), WHITE)
    d = ImageDraw.Draw(canvas)
    d.text((20, 12), title, font=font(SANS_BOLD, 24), fill=DARK)
    for i, im in enumerate(images):
        small = im.convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        canvas.paste(small, ((i % cols) * thumb[0], 54 + (i // cols) * thumb[1]))
    save_png(canvas, path)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    slides = [cover(), before_storage(), soft_folds(), rotate_fold(), flat_or_roll(), environment(), pressure(), reset()]
    for i, im in enumerate(slides, 1):
        save_png(im, ASSETS / f"carousel-{i:02d}.png")
    stories = [story_one(), story_two(), story_three()]
    for i, im in enumerate(stories, 1):
        save_png(im, ASSETS / f"story-{i:02d}.png")
    sheet(slides, ASSETS / "contact-sheet.png", 4, (270, 338), "DAY 32 — CAROUSEL QA")
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480), "DAY 32 — STORIES QA")


if __name__ == "__main__":
    main()
