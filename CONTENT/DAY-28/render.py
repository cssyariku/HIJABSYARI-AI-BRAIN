"""Render Day 28 deterministic Reel, cover, Stories, and QA previews.

Run: python CONTENT/DAY-28/render.py
Requires: Pillow and FFmpeg.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import subprocess

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "daily-formal-diptych.png"
W, H, FPS = 1080, 1920, 30
SCENE_FRAMES = [72, 84, 84, 90, 120]

CREAM = "#F7F1E8"
INK = "#302824"
MUTED = "#70625B"
SAGE = "#899187"
COCOA = "#6D4F45"
TAUPE = "#A58A7B"
WHITE = "#FFFDFC"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(size, bold=False, serif=False):
    return ImageFont.truetype(SERIF if serif else (BOLD if bold else REG), size)


def fit(img, size, centering=(0.5, 0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=centering)


def split_panels(src):
    half = src.width / 2
    return [src.crop((0, 0, round(half) - 4, src.height)),
            src.crop((round(half) + 4, 0, src.width, src.height))]


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
    draw.text((72, 1830), "@hijabsyaricoid", font=font(23), fill=CREAM if light else MUTED)


def zoom_image(image, amount=1.0, center=(0.5, 0.5)):
    base = fit(image, (W, H), center)
    if amount <= 1:
        return base
    nw, nh = int(W * amount), int(H * amount)
    enlarged = base.resize((nw, nh), Image.Resampling.LANCZOS)
    left, top = (nw - W) // 2, (nh - H) // 2
    return enlarged.crop((left, top, left + W, top + H))


def vertical_diptych(src, zoom=1.0):
    panels = split_panels(src)
    canvas = Image.new("RGB", (W, H), CREAM)
    gap = 8
    cell = (W - gap) // 2
    for i, panel in enumerate(panels):
        canvas.paste(fit(panel, (cell, H), (0.5, 0.5)), (i * (cell + gap), 0))
    if zoom > 1:
        nw, nh = int(W * zoom), int(H * zoom)
        canvas = canvas.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas = canvas.crop(((nw-W)//2, (nh-H)//2, (nw-W)//2+W, (nh-H)//2+H))
    return canvas


def text_card(image, title, subtitle, detail=None, badge=None, accent=TAUPE, dark=False):
    base = image.copy()
    d = ImageDraw.Draw(base, "RGBA")
    bg = (48, 40, 36, 238) if dark else (247, 241, 232, 246)
    tf = CREAM if dark else INK
    sf = "#D8C9BD" if dark else MUTED
    d.rounded_rectangle((54, 100, 1026, 650), radius=46, fill=bg)
    y = 165
    if badge:
        d.rounded_rectangle((94, 150, 344, 220), radius=31, fill=accent)
        d.text((219, 185), badge, font=font(25, True), fill=WHITE, anchor="mm")
        y = 278
    y = wrapped(d, title, (94, y, 976, 455), font(61, serif=True), tf, 10)
    d.text((94, min(y + 24, 515)), subtitle, font=font(30, True), fill=sf)
    if detail:
        d.text((94, min(y + 80, 575)), detail, font=font(24), fill=sf)
    brand(d, light=dark)
    return base


def hook_scene(src, zoom=1.0):
    im = vertical_diptych(src, zoom)
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle((54, 98, 1026, 618), radius=46, fill=(247, 241, 232, 246))
    wrapped(d, "Hijab formal vs daily", (94, 168, 976, 365), font(64, serif=True), INK, 10)
    d.text((94, 420), "Bedakan 3 detail ini.", font=font(31, True), fill=COCOA)
    d.rounded_rectangle((94, 505, 474, 572), radius=28, fill=SAGE)
    d.text((284, 538), "DAILY", font=font(24, True), fill=WHITE, anchor="mm")
    d.rounded_rectangle((606, 505, 986, 572), radius=28, fill=COCOA)
    d.text((796, 538), "FORMAL", font=font(24, True), fill=WHITE, anchor="mm")
    brand(d)
    return im


def framework_scene(src, zoom=1.0):
    im = vertical_diptych(src, zoom)
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle((54, 90, 1026, 820), radius=46, fill=(247, 241, 232, 247))
    wrapped(d, "Yang dibedakan", (94, 145, 976, 285), font(59, serif=True), INK, 10)
    rows = [
        ("01", "Struktur", "relaxed  ↔  defined"),
        ("02", "Finish visual", "textured  ↔  smooth"),
        ("03", "Koordinasi outfit", "practical  ↔  polished"),
    ]
    y = 338
    for num, label, note in rows:
        d.ellipse((94, y, 166, y + 72), fill=COCOA)
        d.text((130, y + 36), num, font=font(21, True), fill=WHITE, anchor="mm")
        d.text((198, y - 2), label, font=font(27, True), fill=INK)
        d.text((198, y + 38), note, font=font(23), fill=MUTED)
        y += 134
    brand(d)
    return im


def cta_scene(src, zoom=1.0):
    im = vertical_diptych(src, zoom)
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle((54, 1030, 1026, 1710), radius=46, fill=(48, 40, 36, 238))
    wrapped(d, "Sesuaikan konteksnya", (94, 1110, 976, 1310), font(61, serif=True), CREAM, 10)
    d.text((94, 1365), "Bukan mana yang lebih baik.", font=font(30, True), fill="#D8C9BD")
    d.rounded_rectangle((94, 1465, 986, 1625), radius=38, fill=COCOA)
    d.text((540, 1515), "DAILY ATAU FORMAL?", font=font(29, True), fill=CREAM, anchor="mm")
    d.text((540, 1578), "Simpan checklist-nya.", font=font(24), fill="#E7DCD4", anchor="mm")
    brand(d, light=True)
    return im


def scene_at(src, panels, index, progress):
    zoom = 1.0 + 0.018 * max(0.0, min(1.0, progress))
    if index == 0:
        return hook_scene(src, zoom)
    if index == 1:
        return text_card(zoom_image(panels[0], zoom), "Daily", "relaxed structure", "matte/textured · practical", "01  DAILY", SAGE)
    if index == 2:
        return text_card(zoom_image(panels[1], zoom), "Formal", "defined structure", "smooth/refined · polished", "02  FORMAL", COCOA, dark=True)
    if index == 3:
        return framework_scene(src, 1.0 + 0.009 * progress)
    return cta_scene(src, 1.0 + 0.006 * progress)


def save_static(src, panels):
    names = ["scene-01-hook.png", "scene-02-daily.png", "scene-03-formal.png", "scene-04-framework.png", "scene-05-cta.png"]
    paths = []
    for i, name in enumerate(names):
        path = ASSETS / name
        scene_at(src, panels, i, 0.5).save(path, compress_level=6)
        paths.append(path)
    scene_at(src, panels, 0, 0.35).save(ASSETS / "reel-cover.png", compress_level=6)
    return paths


def stories(src, panels):
    s1 = hook_scene(src, 1.0)
    s2 = vertical_diptych(src)
    s2 = text_card(s2, "Kamu lebih sering butuh?", "Tambahkan Poll native ↓")
    d2 = ImageDraw.Draw(s2, "RGBA")
    d2.rounded_rectangle((94, 1350, 986, 1650), radius=36, fill=(255,253,252,242), outline=COCOA, width=3)
    d2.text((540, 1442), "DAILY", font=font(32, True), fill=INK, anchor="mm")
    d2.text((540, 1555), "FORMAL", font=font(32, True), fill=INK, anchor="mm")
    s3 = zoom_image(panels[1], 1.01)
    s3 = text_card(s3, "Konteks + warna outfitmu", "Jawab di Questions sticker ↓", dark=True)
    d3 = ImageDraw.Draw(s3, "RGBA")
    d3.rounded_rectangle((94, 1350, 986, 1655), radius=36, fill=(48,40,36,240), outline=TAUPE, width=3)
    d3.text((540, 1450), "Contoh: kantor + navy", font=font(30, True), fill=CREAM, anchor="mm")
    d3.text((540, 1552), "daily / formal + warna outfit", font=font(24), fill="#D8C9BD", anchor="mm")
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
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(ASSETS / "reel-final.mp4")
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
