"""Render Day 9 Reel, cover, Stories, and QA preview.

Run: python CONTENT/DAY-09/render.py
Requires: Pillow and FFmpeg.

The composition is deterministic: every frame is derived from the explicit
timeline below, with no wall-clock time, network state, or random values.
"""

from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "five-neutral-looks.png"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"

W, H, FPS = 1080, 1920, 30
PAPER = (249, 246, 239)
CREAM = (239, 231, 219)
DARK = (45, 39, 35)
MUTED = (105, 94, 86)
TAUPE = (164, 140, 123)
LINE = (206, 192, 177)
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LOOKS = [
    ("Ivory + sand", "ringan & rapi"),
    ("Taupe + mushroom", "monokrom lembut"),
    ("Oatmeal + cocoa", "kontras hangat"),
    ("Stone + greige", "bersih & tenang"),
    ("Soft black + oat", "tegas & seimbang"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, face, max_width):
    rows, row = [], ""
    for word in text.split():
        test = f"{row} {word}".strip()
        if draw.textbbox((0, 0), test, font=face)[2] <= max_width:
            row = test
        else:
            rows.append(row)
            row = word
    if row:
        rows.append(row)
    return rows


def text_block(draw, text, xy, face, fill, max_width, leading=None):
    x, y = xy
    leading = leading or int(face.size * 1.2)
    for row in wrap_text(draw, text, face, max_width):
        draw.text((x, y), row, font=face, fill=fill)
        y += leading
    return y


def logo(width=315, light=False):
    with Image.open(LOGO_SOURCE) as src_file:
        src = src_file.convert("RGBA")
        src = src.crop(src.getchannel("A").getbbox())
    color = PAPER if light else DARK
    out = Image.new("RGBA", src.size, color + (0,))
    out.putalpha(src.getchannel("A"))
    return out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)


def paste_logo(im, light=False):
    mark = logo(light=light)
    im.paste(mark, (72, 62), mark)


def panel(index):
    with Image.open(SOURCE) as src_file:
        src = src_file.convert("RGB")
        pw = src.width / 5
        inset = 3
        left = round(index * pw + (inset if index else 0))
        right = round((index + 1) * pw - (inset if index < 4 else 0))
        return src.crop((left, 0, right, src.height)).copy()


def photo_background(index, darken=0):
    # Bias the vertical crop upward so the model's full face remains visible.
    base = ImageOps.fit(panel(index), (W, H), Image.Resampling.LANCZOS, centering=(0.5, 0.10)).convert("RGBA")
    base = ImageEnhance.Contrast(base.convert("RGB")).enhance(1.02).convert("RGBA")
    if darken:
        base = Image.alpha_composite(base, Image.new("RGBA", base.size, (30, 25, 22, darken)))
    return base


def gradient_overlay(im, top_alpha=225, bottom_alpha=205):
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for y in range(0, 690):
        a = round(top_alpha * (1 - y / 690))
        d.line((0, y, W, y), fill=(*PAPER, a))
    for y in range(1260, H):
        a = round(bottom_alpha * ((y - 1260) / (H - 1260)))
        d.line((0, y, W, y), fill=(*DARK, a))
    return Image.alpha_composite(im, overlay)


def hook_scene():
    im = gradient_overlay(photo_background(2), 245, 205)
    paste_logo(im)
    d = ImageDraw.Draw(im)
    d.text((72, 270), "Netral nggak harus", font=font(FONT_SERIF_BOLD, 75), fill=DARK)
    d.text((72, 365), "terlihat sama.", font=font(FONT_SERIF_BOLD, 75), fill=DARK)
    d.rounded_rectangle((72, 500, 807, 600), radius=48, fill=(*PAPER, 235))
    d.text((112, 529), "5 elegant hijab looks", font=font(FONT_SANS_BOLD, 36), fill=DARK)
    d.text((72, 1730), "Lima palet. Lima karakter.", font=font(FONT_SANS_BOLD, 30), fill=PAPER)
    return im.convert("RGB")


def look_scene(index, title, descriptor):
    im = gradient_overlay(photo_background(index), 210, 220)
    paste_logo(im)
    d = ImageDraw.Draw(im)
    d.ellipse((72, 268, 168, 364), fill=TAUPE)
    d.text((120, 316), str(index + 1), font=font(FONT_SANS_BOLD, 38), fill=PAPER, anchor="mm")
    d.text((194, 270), title, font=font(FONT_SERIF_BOLD, 57), fill=DARK)
    d.rounded_rectangle((72, 1600, 1008, 1778), radius=30, fill=(*PAPER, 228))
    d.text((112, 1640), descriptor, font=font(FONT_SERIF_BOLD, 42), fill=DARK)
    d.text((112, 1702), "Bukan rumus—ini satu arah visual.", font=font(FONT_SANS, 26), fill=MUTED)
    return im.convert("RGB")


def cta_scene():
    im = Image.new("RGB", (W, H), CREAM).convert("RGBA")
    paste_logo(im)
    d = ImageDraw.Draw(im)
    d.text((72, 300), "Look mana yang", font=font(FONT_SERIF_BOLD, 72), fill=DARK)
    d.text((72, 390), "paling kamu simpan?", font=font(FONT_SERIF_BOLD, 72), fill=DARK)
    d.text((72, 510), "Pilih 1–5.", font=font(FONT_SANS_BOLD, 36), fill=MUTED)
    thumb_w, thumb_h, gap = 174, 580, 18
    for i in range(5):
        p = ImageOps.fit(panel(i), (thumb_w, thumb_h), Image.Resampling.LANCZOS, centering=(0.5, 0.30))
        x = 69 + i * (thumb_w + gap)
        im.paste(p, (x, 710))
        d.ellipse((x + 55, 1325, x + 119, 1389), fill=TAUPE)
        d.text((x + 87, 1357), str(i + 1), font=font(FONT_SANS_BOLD, 26), fill=PAPER, anchor="mm")
    d.text((72, 1535), "Simpan sebagai referensi—", font=font(FONT_SANS_BOLD, 31), fill=DARK)
    d.text((72, 1585), "lalu sesuaikan bahan dan konteksmu.", font=font(FONT_SANS, 30), fill=DARK)
    return im.convert("RGB")


def story(title, body, index, filename, sticker_hint=None):
    im = gradient_overlay(photo_background(index), 240, 215)
    paste_logo(im)
    d = ImageDraw.Draw(im)
    y = text_block(d, title, (72, 285), font(FONT_SERIF_BOLD, 69), DARK, 930, 83)
    text_block(d, body, (72, y + 42), font(FONT_SANS, 30), DARK, 900, 45)
    if sticker_hint:
        d.rounded_rectangle((72, 1415, 1008, 1695), radius=32, fill=(*PAPER, 228), outline=LINE, width=3)
        text_block(d, sticker_hint, (112, 1480), font(FONT_SANS_BOLD, 27), MUTED, 850, 42)
    im.convert("RGB").save(ASSETS / filename, optimize=True, compress_level=6)


def write_assets():
    scenes = [hook_scene()]
    scenes.extend(look_scene(i, *look) for i, look in enumerate(LOOKS))
    scenes.append(cta_scene())
    names = ["scene-01-hook.png"] + [f"scene-{i + 2:02d}-look-{i + 1}.png" for i in range(5)] + ["scene-07-cta.png"]
    for im, name in zip(scenes, names):
        im.save(ASSETS / name, optimize=True, compress_level=6)
    scenes[0].save(ASSETS / "reel-cover.png", optimize=True, compress_level=6)
    story("Netral nggak harus terlihat sama.", "Lima look ini memakai palet netral dengan tingkat kontras dan karakter berbeda.", 2, "story-01-teaser.png", "Lanjut ke Reel untuk lihat look 1–5")
    story("Light atau deep?", "Look 1 terasa ringan. Look 5 memberi kontras yang lebih dalam.", 0, "story-02-poll.png", "Tambahkan Poll: LOOK 1 / LOOK 5")
    story("Nomor berapa yang ingin kamu coba?", "Pilih 1–5, atau sebut konteksnya: daily, kantor, atau acara.", 4, "story-03-question.png", "Tambahkan Questions: 1, 2, 3, 4, atau 5?")
    return scenes, names


def zoom_frame(src, progress, direction=1):
    scale = 1.0 + 0.028 * progress
    nw, nh = round(W * scale), round(H * scale)
    tmp = src.resize((nw, nh), Image.Resampling.BICUBIC)
    max_x, max_y = nw - W, nh - H
    x = round(max_x * (0.35 + 0.15 * direction * progress))
    y = round(max_y * 0.35)
    x = max(0, min(max_x, x))
    return tmp.crop((x, y, x + W, y + H))


def render_video(scenes):
    durations = [2.0, 2.2, 2.2, 2.2, 2.2, 2.2, 3.0]
    command = [
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(ASSETS / "reel-final.mp4")
    ]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for scene_index, (scene, duration) in enumerate(zip(scenes, durations)):
        total = round(duration * FPS)
        for i in range(total):
            frame = zoom_frame(scene, i / max(1, total - 1), 1 if scene_index % 2 == 0 else -1)
            proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("FFmpeg render failed")


def contact_sheet(names):
    sheet = Image.new("RGB", (1495, 610), PAPER)
    d = ImageDraw.Draw(sheet)
    d.text((35, 22), "DAY 09 — Reel keyframes", font=font(FONT_SANS_BOLD, 27), fill=DARK)
    for i, name in enumerate(names):
        with Image.open(ASSETS / name) as src:
            im = src.convert("RGB")
            im.thumbnail((180, 410), Image.Resampling.LANCZOS)
        x = 35 + i * 205
        sheet.paste(im, (x, 78))
        d.text((x, 515), str(i + 1), font=font(FONT_SANS_BOLD, 21), fill=MUTED)
    sheet.save(ASSETS / "contact-sheet.png", optimize=True, compress_level=6)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    scene_images, scene_names = write_assets()
    render_video(scene_images)
    contact_sheet(scene_names)
