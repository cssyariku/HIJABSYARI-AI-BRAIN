"""Render Day 26 deterministic Reel, cover, Stories, and QA previews.

Run: python CONTENT/DAY-26/render.py
Requires: Pillow and FFmpeg.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import subprocess

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "monochrome-three-look-triptych.png"
W, H, FPS = 1080, 1920, 30
SCENE_FRAMES = [72, 81, 81, 81, 72, 63]

CREAM = "#F7F1E8"
INK = "#302824"
MUTED = "#70625B"
TAUPE = "#9C8174"
ROSE = "#A66A73"
CHARCOAL = "#3B3A3D"
WHITE = "#FFFDFC"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(size, bold=False, serif=False):
    return ImageFont.truetype(SERIF if serif else (BOLD if bold else REG), size)


def fit(img, size, centering=(0.5, 0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=centering)


def split_panels(src):
    w = src.width / 3
    panels = []
    for i in range(3):
        left = round(i * w) + (5 if i else 0)
        right = round((i + 1) * w) - (5 if i < 2 else 0)
        panels.append(src.crop((left, 0, right, src.height)))
    return panels


def wrapped(draw, value, box, fnt, fill=INK, spacing=10):
    x0, y0, x1, _ = box
    lines, cur = [], ""
    for word in value.split():
        trial = (cur + " " + word).strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= x1 - x0:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    y = y0
    for line in lines:
        draw.text((x0, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + spacing
    return y


def brand(draw, light=False):
    fill = CREAM if light else MUTED
    draw.text((72, 1828), "@hijabsyaricoid", font=font(23), fill=fill)


def zoom_image(image, amount=1.0, center=(0.5, 0.48)):
    base = fit(image, (W, H), center)
    if amount <= 1:
        return base
    nw, nh = int(W * amount), int(H * amount)
    z = base.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - W) // 2
    top = int((nh - H) * center[1])
    return z.crop((left, top, left + W, top + H))


def vertical_triptych(src):
    panels = split_panels(src)
    canvas = Image.new("RGB", (W, H), CREAM)
    gap = 6
    cell = (W - 2 * gap) // 3
    for i, panel in enumerate(panels):
        crop = fit(panel, (cell, H), (0.5, 0.50))
        canvas.paste(crop, (i * (cell + gap), 0))
    return canvas


def text_card(image, title, subtitle, detail=None, badge=None, dark=False):
    base = image.copy()
    d = ImageDraw.Draw(base, "RGBA")
    fill = (48, 40, 36, 236) if dark else (247, 241, 232, 244)
    title_fill = CREAM if dark else INK
    sub_fill = "#D8C9BD" if dark else MUTED
    d.rounded_rectangle((54, 100, 1026, 625), radius=46, fill=fill)
    y = 165
    if badge:
        accent = ROSE if not dark else TAUPE
        d.rounded_rectangle((94, 150, 330, 218), radius=30, fill=accent)
        d.text((212, 184), badge, font=font(25, True), fill=WHITE, anchor="mm")
        y = 270
    y = wrapped(d, title, (94, y, 976, 440), font(61, serif=True), title_fill, 10)
    d.text((94, min(y + 24, 495)), subtitle, font=font(31, True), fill=sub_fill)
    if detail:
        d.text((94, min(y + 78, 555)), detail, font=font(25), fill=sub_fill)
    brand(d, light=dark)
    return base


def triptych(src, title, subtitle, zoom=1.0, dark=False):
    image = vertical_triptych(src)
    if zoom > 1:
        nw, nh = int(W * zoom), int(H * zoom)
        image = image.resize((nw, nh), Image.Resampling.LANCZOS)
        image = image.crop(((nw-W)//2, (nh-H)//2, (nw-W)//2+W, (nh-H)//2+H))
    return text_card(image, title, subtitle, dark=dark)


def formula_scene(src, zoom=1.0):
    image = vertical_triptych(src)
    if zoom > 1:
        nw, nh = int(W * zoom), int(H * zoom)
        image = image.resize((nw, nh), Image.Resampling.LANCZOS)
        image = image.crop(((nw-W)//2, (nh-H)//2, (nw-W)//2+W, (nh-H)//2+H))
    d = ImageDraw.Draw(image, "RGBA")
    d.rounded_rectangle((54, 96, 1026, 715), radius=46, fill=(247, 241, 232, 246))
    wrapped(d, "Biar tidak terasa datar", (94, 155, 976, 330), font(59, serif=True), INK, 10)
    d.text((94, 390), "BEDAKAN 2 HAL", font=font(27, True), fill=ROSE)
    rows = [
        ("01", "Kedalaman warna", "light · mid · deep"),
        ("02", "Tekstur", "matte · woven · smooth"),
    ]
    y = 455
    for num, label, note in rows:
        d.ellipse((94, y, 166, y + 72), fill=TAUPE)
        d.text((130, y + 36), num, font=font(22, True), fill=WHITE, anchor="mm")
        d.text((198, y - 2), label, font=font(27, True), fill=INK)
        d.text((198, y + 37), note, font=font(23), fill=MUTED)
        y += 112
    brand(d)
    return image


def scene_at(src, panels, index, progress):
    zoom = 1.0 + 0.024 * max(0.0, min(1.0, progress))
    if index == 0:
        return triptych(src, "Monochrome tidak harus terasa datar", "Coba 3 arah tonal ini.", zoom)
    if index == 1:
        return text_card(zoom_image(panels[0], zoom), "Light tonal", "ivory · oat · warm beige", "ringan & lembut", "01")
    if index == 2:
        return text_card(zoom_image(panels[1], zoom), "Soft tonal", "mushroom · taupe · cocoa", "tenang & berlapis", "02")
    if index == 3:
        return text_card(zoom_image(panels[2], zoom), "Deep tonal", "charcoal · graphite · black", "tegas & minimal", "03", dark=True)
    if index == 4:
        return formula_scene(src, 1.0 + 0.012 * progress)
    return triptych(src, "Light, soft, atau deep?", "Simpan referensinya.", 1.0 + 0.008 * progress)


def save_static(src, panels):
    names = [
        "scene-01-hook.png", "scene-02-light.png", "scene-03-soft.png",
        "scene-04-deep.png", "scene-05-formula.png", "scene-06-cta.png",
    ]
    paths = []
    for i, name in enumerate(names):
        path = ASSETS / name
        scene_at(src, panels, i, 0.5).save(path, compress_level=6)
        paths.append(path)
    scene_at(src, panels, 0, 0.35).save(ASSETS / "reel-cover.png", compress_level=6)
    return paths


def stories(src, panels):
    s1 = triptych(src, "Satu warna, tiga arah tonal", "Light · soft · deep", 1.0)
    s2 = triptych(src, "Kamu lebih sering pilih?", "Tambahkan Poll native ↓", 1.0)
    d2 = ImageDraw.Draw(s2, "RGBA")
    d2.rounded_rectangle((94, 1360, 986, 1645), radius=36, fill=(255,253,252,240), outline=ROSE, width=3)
    d2.text((540, 1450), "LIGHT", font=font(32, True), fill=INK, anchor="mm")
    d2.text((540, 1555), "SOFT", font=font(32, True), fill=INK, anchor="mm")
    s3 = zoom_image(panels[2], 1.01)
    s3 = text_card(s3, "Pilih look + occasion", "Jawab di Questions sticker ↓", dark=True)
    d3 = ImageDraw.Draw(s3, "RGBA")
    d3.rounded_rectangle((94, 1350, 986, 1655), radius=36, fill=(48,40,36,238), outline=TAUPE, width=3)
    d3.text((540, 1445), "LIGHT / SOFT / DEEP", font=font(31, True), fill=CREAM, anchor="mm")
    d3.text((540, 1548), "+ daily, kantor, atau acara", font=font(25), fill="#D8C9BD", anchor="mm")
    paths = []
    for i, im in enumerate([s1, s2, s3], 1):
        path = ASSETS / f"story-{i:02d}.png"
        im.save(path, compress_level=6)
        paths.append(path)
    return paths


def contact_sheet(paths, out_name, thumb=(270, 480)):
    sheet = Image.new("RGB", (thumb[0] * len(paths), thumb[1]), "#DCD2CA")
    for i, path in enumerate(paths):
        im = Image.open(path).convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        sheet.paste(im, (i * thumb[0], 0))
    sheet.save(ASSETS / out_name, compress_level=6)


def render_video(src, panels):
    cmd = [
        "ffmpeg", "-y", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        str(ASSETS / "reel-final.mp4")
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for scene_i, count in enumerate(SCENE_FRAMES):
            for local in range(count):
                progress = local / max(1, count - 1)
                proc.stdin.write(scene_at(src, panels, scene_i, progress).tobytes())
    finally:
        if proc.stdin:
            proc.stdin.close()
    code = proc.wait()
    if code:
        raise RuntimeError(f"FFmpeg failed: {code}")


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    panels = split_panels(src)
    scenes = save_static(src, panels)
    story_paths = stories(src, panels)
    contact_sheet(scenes, "contact-sheet.png")
    contact_sheet(story_paths, "stories-contact-sheet.png")
    render_video(src, panels)


if __name__ == "__main__":
    main()
