from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "audience-problem-grid.png"
W, H = 1080, 1920

CREAM = "#F7F0E8"
INK = "#2C2724"
MUTED = "#6D625B"
ROSE = "#A95F69"
TAUPE = "#8B7568"
SAGE = "#879078"
BURGUNDY = "#7B3444"
WHITE = "#FFFDFC"

REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def fit(img, size, centering=(0.5, 0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=centering)


def panels(src):
    mx, my = src.width // 2, src.height // 2
    return [
        src.crop((0, 0, mx, my)),
        src.crop((mx, 0, src.width, my)),
        src.crop((0, my, mx, src.height)),
        src.crop((mx, my, src.width, src.height)),
    ]


def rounded(draw, box, fill=WHITE, radius=38, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def wrapped(draw, text, box, fnt, fill=INK, spacing=10):
    x0, y0, x1, _ = box
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = (current + " " + word).strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= x1 - x0:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    y = y0
    for line in lines:
        draw.text((x0, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + spacing
    return y


def brand(draw):
    draw.ellipse((72, 1817, 90, 1835), fill=ROSE)
    draw.text((104, 1809), "HIJAB SYARI INDONESIA", font=font(22, True), fill=MUTED)


def photo(base, img, box, radius=36):
    crop = fit(img, (box[2] - box[0], box[3] - box[1]))
    mask = Image.new("L", crop.size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, crop.width, crop.height), radius=radius, fill=255)
    base.paste(crop, (box[0], box[1]), mask)


def story_1(src):
    base = fit(src, (W, H))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, W, H), fill=(24, 20, 18, 34))
    base = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(base)
    rounded(d, (54, 128, 1026, 780), fill="#F7F0E8F2", radius=46)
    wrapped(d, "Masalah hijab apa yang paling ingin kamu bereskan?",
            (94, 200, 976, 570), font(65, True), INK, 13)
    d.text((94, 625), "Bantu pilih pembahasan berikutnya.", font=font(31), fill=MUTED)
    brand(d)
    return base


def comparison_story(left, right, title, body, labels, accents):
    base = Image.new("RGB", (W, H), CREAM)
    photo(base, left, (54, 110, 527, 910), 36)
    photo(base, right, (553, 110, 1026, 910), 36)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((76, 785, 505, 850), radius=28, fill=accents[0])
    d.rounded_rectangle((575, 785, 1004, 850), radius=28, fill=accents[1])
    d.text((290, 817), labels[0], font=font(23, True), fill=WHITE, anchor="mm")
    d.text((790, 817), labels[1], font=font(23, True), fill=WHITE, anchor="mm")
    rounded(d, (54, 955, 1026, 1772), fill=WHITE, radius=46)
    wrapped(d, title, (94, 1025, 976, 1275), font(61, True), INK, 12)
    wrapped(d, body, (94, 1288, 976, 1450), font(33), MUTED, 12)
    rounded(d, (94, 1510, 986, 1682), fill="#F5ECE6", radius=30, outline="#D6C4BA", width=3)
    d.text((540, 1597), "Tambahkan Poll native di area ini", font=font(29, True), fill=TAUPE, anchor="mm")
    brand(d)
    return base


def story_4(src):
    base = fit(src, (W, H))
    d = ImageDraw.Draw(base)
    rounded(d, (54, 110, 1026, 1780), fill="#F7F0E8F5", radius=48)
    wrapped(d, "Ceritakan masalah paling spesifikmu.",
            (94, 185, 976, 470), font(64, True), INK, 12)
    wrapped(d, "Kapan terjadi? Bahan apa? Apa yang sudah dicoba?",
            (94, 540, 976, 720), font(35), MUTED, 12)
    rounded(d, (94, 860, 986, 1420), fill=WHITE, radius=38, outline="#D7C3B9", width=3)
    d.text((134, 920), "Hijabku sering ___ saat ___", font=font(33), fill="#9B8D84")
    d.text((94, 1515), "Jawabanmu membantu menentukan", font=font(30), fill=MUTED)
    d.text((94, 1562), "Hijab Fix berikutnya.", font=font(38, True), fill=ROSE)
    brand(d)
    return base


def contact_sheet(paths):
    thumb_w, thumb_h = 270, 480
    sheet = Image.new("RGB", (thumb_w * 4, thumb_h), "#DED4CD")
    for i, path in enumerate(paths):
        im = Image.open(path).convert("RGB")
        im = im.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(im, (i * thumb_w, 0))
    sheet.save(ASSETS / "contact-sheet.png", compress_level=6)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    p = panels(src)
    outputs = [
        ("story-01.png", story_1(src)),
        ("story-02.png", comparison_story(
            p[0], p[1], "Mana yang lebih sering?",
            "Bentuk depan sulit stay—atau hijab mudah bergeser saat bergerak?",
            ("BENTUK DEPAN", "MUDAH BERGESER"), (TAUPE, ROSE))),
        ("story-03.png", comparison_story(
            p[2], p[3], "Topik mana yang lebih kamu butuhkan?",
            "Bahan & perawatan—atau warna & outfit?",
            ("BAHAN & CARE", "WARNA & OUTFIT"), (SAGE, BURGUNDY))),
        ("story-04.png", story_4(src)),
    ]
    paths = []
    for name, image in outputs:
        path = ASSETS / name
        image.save(path, compress_level=6)
        paths.append(path)
    contact_sheet(paths)


if __name__ == "__main__":
    main()
