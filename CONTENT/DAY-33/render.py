"""Render Day 33 deterministic Reel, cover, Stories, and QA previews.

Run: python CONTENT/DAY-33/render.py
Requires: Pillow and FFmpeg.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import subprocess

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "cheek-stay-triptych.png"
W, H, FPS = 1080, 1920, 30
SCENE_FRAMES = [72, 84, 84, 90, 120]

CREAM = "#F7F1E8"
PAPER = "#FFFDFC"
INK = "#302824"
MUTED = "#71635C"
COCOA = "#6D4B40"
TAUPE = "#A58A7B"
SAGE = "#899187"
ROSE = "#B88484"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(size, bold=False, serif=False):
    return ImageFont.truetype(SERIF if serif else (BOLD if bold else REG), size)


def fit(img, size, centering=(0.5, 0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=centering)


def split_panels(src):
    third = src.width / 3
    gap = 4
    return [
        src.crop((0, 0, round(third) - gap, src.height)),
        src.crop((round(third) + gap, 0, round(2 * third) - gap, src.height)),
        src.crop((round(2 * third) + gap, 0, src.width, src.height)),
    ]


def wrap(draw, text, xy, width, fnt, fill=INK, spacing=10):
    words, lines, current = text.split(), [], ""
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


def zoom_image(img, zoom, centering=(0.5, 0.5)):
    base = fit(img, (W, H), centering=centering)
    if zoom <= 1:
        return base
    zw, zh = round(W * zoom), round(H * zoom)
    enlarged = base.resize((zw, zh), Image.Resampling.LANCZOS)
    x, y = (zw - W) // 2, (zh - H) // 2
    return enlarged.crop((x, y, x + W, y + H))


def brand(draw, light=False):
    draw.text((72, 1835), "@hijabsyaricoid", font=font(22), fill=CREAM if light else MUTED)


def top_card(im, number, title, body, accent=COCOA):
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle((0, 0, W, H), fill=(35, 26, 23, 34))
    d.rounded_rectangle((58, 86, 1022, 575), radius=42, fill=(255, 253, 250, 244))
    if number:
        d.rounded_rectangle((88, 126, 200, 186), radius=21, fill=accent)
        d.text((144, 156), number, font=font(25, True), fill=CREAM, anchor="mm")
    y = wrap(d, title, (88, 220 if number else 150), 850, font(56, serif=True), INK, 6)
    wrap(d, body, (88, y + 22), 850, font(27), MUTED, 8)
    brand(d, light=True)
    return im


def hook_scene(src, zoom):
    im = zoom_image(src, zoom, (0.5, 0.52))
    return top_card(im, "", "Hijab nggak stay di area pipi?", "Cek 3 titik ini.", ROSE)


def detail_scene(panel, zoom, number, title, body, accent, center=(0.5, 0.5)):
    im = zoom_image(panel, zoom, center)
    return top_card(im, number, title, body, accent)


def movement_scene(panel, zoom):
    im = zoom_image(panel, zoom, (0.5, 0.5))
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle((0, 0, W, H), fill=(35, 26, 23, 62))
    d.rounded_rectangle((58, 82, 1022, 570), radius=42, fill=(255, 253, 250, 244))
    d.rounded_rectangle((88, 124, 200, 184), radius=21, fill=SAGE)
    d.text((144, 154), "03", font=font(25, True), fill=CREAM, anchor="mm")
    d.text((88, 230), "Arah tarik & pengunci", font=font(48, serif=True), fill=INK)
    d.text((88, 328), "Atur tanpa menekan pipi.", font=font(27), fill=MUTED)
    d.rounded_rectangle((94, 1280, 986, 1655), radius=40, fill=(48, 39, 34, 238))
    items = [("01", "menoleh"), ("02", "bicara"), ("03", "senyum")]
    for i, (num, label) in enumerate(items):
        y = 1370 + i * 92
        d.rounded_rectangle((140, y - 29, 208, y + 29), radius=16, fill=ROSE if i == 0 else TAUPE)
        d.text((174, y), num, font=font(20, True), fill=CREAM, anchor="mm")
        d.text((250, y), label, font=font(29, True), fill=CREAM, anchor="lm")
    brand(d, light=True)
    return im


def cta_scene(src, zoom):
    im = zoom_image(src, zoom, (0.5, 0.52))
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle((0, 0, W, H), fill=(39, 29, 25, 140))
    d.rounded_rectangle((62, 100, 1018, 700), radius=44, fill=(48, 39, 34, 238))
    d.text((92, 165), "Tes 30 detik", font=font(64, serif=True), fill=CREAM)
    d.text((92, 275), "menoleh · bicara · senyum", font=font(30, True), fill="#E5D8CE")
    wrap(d, "Bagian mana yang berubah?", (92, 390), 820, font(44, serif=True), CREAM, 5)
    d.rounded_rectangle((94, 1315, 986, 1645), radius=40, fill=(255, 253, 250, 242))
    d.text((540, 1405), "Simpan tiga ceknya.", font=font(30, True), fill=INK, anchor="mm")
    d.text((540, 1518), "garis awal · lapisan · arah tarik", font=font(26, True), fill=COCOA, anchor="mm")
    d.text((540, 1585), "Tidak ada satu teknik untuk semua.", font=font(22), fill=MUTED, anchor="mm")
    brand(d, light=True)
    return im


def scene_at(src, panels, index, progress):
    zoom = 1.0 + 0.018 * max(0.0, min(1.0, progress))
    if index == 0:
        return hook_scene(src, zoom)
    if index == 1:
        return detail_scene(panels[0], zoom, "01", "Garis awal", "Mulai dari tepi yang rata.", COCOA, (0.5, 0.48))
    if index == 2:
        return detail_scene(panels[1], zoom, "02", "Jumlah lapisan", "Kurangi tumpukan yang saling bergeser.", ROSE, (0.5, 0.48))
    if index == 3:
        return movement_scene(panels[2], 1.0 + 0.012 * progress)
    return cta_scene(src, 1.0 + 0.008 * progress)


def save_statics(src, panels):
    names = ["scene-01-hook.png", "scene-02-garis-awal.png", "scene-03-lapisan.png", "scene-04-arah-tarik.png", "scene-05-cta.png"]
    paths = []
    for i, name in enumerate(names):
        path = ASSETS / name
        scene_at(src, panels, i, 0.5).save(path, compress_level=7)
        paths.append(path)
    scene_at(src, panels, 0, 0.35).save(ASSETS / "reel-cover.png", compress_level=7)
    return paths


def stories(src, panels):
    s1 = hook_scene(src, 1.006)
    s2 = detail_scene(panels[1], 1.01, "", "Yang paling sering berubah?", "Tambahkan Poll native ↓", SAGE, (0.5, 0.48))
    d2 = ImageDraw.Draw(s2, "RGBA")
    d2.rounded_rectangle((100, 1320, 980, 1640), radius=38, fill=(255, 253, 250, 244), outline=SAGE, width=4)
    d2.text((540, 1412), "GARIS AWAL", font=font(28, True), fill=INK, anchor="mm")
    d2.text((540, 1538), "LAPISAN", font=font(28, True), fill=INK, anchor="mm")
    s3 = zoom_image(panels[2], 1.01, (0.5, 0.5))
    d3 = ImageDraw.Draw(s3, "RGBA")
    d3.rectangle((0, 0, W, H), fill=(39, 29, 25, 115))
    d3.text((72, 120), "Bahan + bagian yang bergeser", font=font(47, serif=True), fill=CREAM)
    d3.text((72, 215), "Jawab di Questions sticker ↓", font=font(27), fill="#E8DCD2")
    d3.rounded_rectangle((92, 1000, 988, 1450), radius=44, fill=(255, 253, 250, 246))
    d3.text((540, 1115), "Contoh:", font=font(24, True), fill=MUTED, anchor="mm")
    d3.text((540, 1210), "voal + sisi dekat pipi", font=font(31, True), fill=INK, anchor="mm")
    d3.text((540, 1325), "Tambahkan Questions native", font=font(24), fill=COCOA, anchor="mm")
    brand(d3, light=True)
    paths = []
    for i, image in enumerate([s1, s2, s3], 1):
        path = ASSETS / f"story-{i:02d}.png"
        image.save(path, compress_level=7)
        paths.append(path)
    return paths


def contact_sheet(paths, name, thumb=(216, 384)):
    header = 80
    sheet = Image.new("RGB", (thumb[0] * len(paths), thumb[1] + header), "#DED4CC")
    d = ImageDraw.Draw(sheet)
    d.rectangle((0, 0, sheet.width, header), fill=PAPER)
    d.text((24, 22), f"DAY 33 — {name.replace('-', ' ').upper()}", font=font(28, True), fill=INK)
    for i, path in enumerate(paths):
        pic = Image.open(path).convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        sheet.paste(pic, (i * thumb[0], header))
    sheet.save(ASSETS / f"{name}.png", compress_level=7)


def render_video(src, panels):
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "slow", "-crf", "30",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(ASSETS / "reel-final.mp4")
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for scene_i, count in enumerate(SCENE_FRAMES):
            for local in range(count):
                progress = local / max(1, count - 1)
                proc.stdin.write(scene_at(src, panels, scene_i, progress).convert("RGB").tobytes())
    finally:
        if proc.stdin:
            proc.stdin.close()
    if proc.wait():
        raise RuntimeError("FFmpeg render failed")


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    panels = split_panels(src)
    scenes = save_statics(src, panels)
    story_paths = stories(src, panels)
    contact_sheet(scenes, "contact-sheet")
    contact_sheet(story_paths, "stories-contact-sheet", (270, 480))
    render_video(src, panels)


if __name__ == "__main__":
    main()
