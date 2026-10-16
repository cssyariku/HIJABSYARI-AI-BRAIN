from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "pashmina-vs-segiempat-diptych.png"
W, H = 1080, 1920

CREAM = "#F6F0E8"
INK = "#292622"
MUTED = "#675F58"
TAUPE = "#A78977"
GREIGE = "#AAA198"
WHITE = "#FFFDFC"

REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def fit_crop(img, size, box=None):
    if box:
        img = img.crop(box)
    target = size[0] / size[1]
    ratio = img.width / img.height
    if ratio > target:
        new_w = int(img.height * target)
        left = (img.width - new_w) // 2
        img = img.crop((left, 0, left + new_w, img.height))
    else:
        new_h = int(img.width / target)
        top = max(0, (img.height - new_h) // 3)
        img = img.crop((0, top, img.width, top + new_h))
    return img.resize(size, Image.Resampling.LANCZOS)


def rounded(draw, xy, radius=34, fill=WHITE, outline=None, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, size, fill=INK, bold=False, anchor="la", spacing=12):
    draw.multiline_text(xy, value, font=font(size, bold), fill=fill,
                        anchor=anchor, spacing=spacing)


def footer(draw):
    text(draw, (72, 1842), "@hijabsyaricoid", 28, fill=MUTED)


def soft_gradient(img, y0=0, y1=760):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = overlay.load()
    rgb = (246, 240, 232)
    for y in range(y0, min(y1, H)):
        alpha = int(235 * (1 - (y-y0) / max(1, y1-y0)))
        for x in range(W):
            px[x, y] = (*rgb, max(0, alpha))
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def frame_1(src):
    base = fit_crop(src, (W, H))
    base = soft_gradient(base, 0, 850)
    d = ImageDraw.Draw(base)
    text(d, (72, 116), "Kalau harus pilih satu…", 46, fill=MUTED, bold=False)
    text(d, (72, 190), "PASHMINA\natau SEGI EMPAT?", 82, bold=True, spacing=8)
    rounded(d, (72, 1390, 1008, 1695), radius=42, fill="#FDF9F4E8")
    text(d, (540, 1455), "Pilih yang paling sering kamu pakai", 38,
         bold=True, anchor="ma")
    footer(d)
    return base


def single_frame(src, side, title_value, intro, bullets, accent):
    half = src.crop((0, 0, src.width // 2, src.height)) if side == "left" else src.crop((src.width // 2, 0, src.width, src.height))
    base = Image.new("RGB", (W, H), CREAM)
    portrait = fit_crop(half, (W, 1110))
    base.paste(portrait, (0, 0))
    d = ImageDraw.Draw(base)
    rounded(d, (54, 965, 1026, 1785), radius=54, fill=WHITE)
    d.rounded_rectangle((84, 1022, 278, 1072), radius=25, fill=accent)
    text(d, (181, 1047), title_value.upper(), 24, fill=WHITE, bold=True, anchor="mm")
    text(d, (84, 1138), intro, 44, bold=True, spacing=9)
    y = 1320
    for bullet in bullets:
        d.ellipse((88, y+10, 108, y+30), fill=accent)
        text(d, (132, y), bullet, 34, fill=INK)
        y += 102
    text(d, (84, 1666), "Pilihan terbaik tetap yang terasa nyaman\ndan sesuai kebutuhanmu.", 28, fill=MUTED, spacing=8)
    footer(d)
    return base


def frame_4(src):
    base = Image.new("RGB", (W, H), CREAM)
    top = fit_crop(src, (W, 690))
    base.paste(top, (0, 0))
    d = ImageDraw.Draw(base)
    rounded(d, (54, 610, 1026, 1785), radius=54, fill=WHITE)
    text(d, (84, 690), "Kamu memilih hijab\nberdasarkan apa?", 68, bold=True, spacing=8)
    text(d, (84, 905), "Praktis, bentuk, bahan, aktivitas—\natau ada alasan lain?", 34, fill=MUTED, spacing=10)
    rounded(d, (84, 1115, 996, 1510), radius=38, fill="#F3ECE4", outline="#D8CCC1", width=3)
    text(d, (84, 1590), "Jawabanmu akan membantu menentukan\ntopik berikutnya.", 32, fill=INK, spacing=9)
    footer(d)
    return base


def contact_sheet(files):
    thumb_w, thumb_h = 270, 480
    sheet = Image.new("RGB", (thumb_w * 4, thumb_h), "white")
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(im, (i * thumb_w, 0))
    sheet.save(ASSETS / "contact-sheet.png", compress_level=6)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    outputs = [
        ("story-01-poll.png", frame_1(src)),
        ("story-02-pashmina.png", single_frame(
            src, "left", "Pashmina", "Bisa terasa pas kalau kamu ingin:",
            ["drape lebih panjang", "framing mudah diatur", "variasi styling lebih fleksibel"], TAUPE)),
        ("story-03-segiempat.png", single_frame(
            src, "right", "Segi empat", "Bisa terasa pas kalau kamu ingin:",
            ["bentuk depan lebih terstruktur", "lipatan yang familiar", "rutinitas styling lebih ringkas"], GREIGE)),
        ("story-04-question.png", frame_4(src)),
    ]
    paths = []
    for name, image in outputs:
        path = ASSETS / name
        image.save(path, compress_level=6)
        paths.append(path)
    contact_sheet(paths)


if __name__ == "__main__":
    main()
