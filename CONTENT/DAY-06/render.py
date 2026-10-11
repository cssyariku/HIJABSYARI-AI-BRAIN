"""Render Day 6 Reel, cover, Stories, and QA preview.

Run: python CONTENT/DAY-06/render.py
Requires: Pillow and FFmpeg.
"""

from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "face-framing-triptych.png"
LOGO_SOURCE = ROOT.parent.parent / "Logo Hijab Syari Transparan.png"

W, H, FPS = 1080, 1920, 30
PAPER = (250, 247, 241)
CREAM = (241, 233, 222)
DARK = (47, 41, 38)
MUTED = (103, 91, 84)
TAUPE = (166, 137, 119)
LINE = (205, 190, 177)
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def logo(width=315, light=False):
    src = Image.open(LOGO_SOURCE).convert("RGBA")
    src = src.crop(src.getchannel("A").getbbox())
    color = (250, 247, 241) if light else DARK
    out = Image.new("RGBA", src.size, color + (0,))
    out.putalpha(src.getchannel("A"))
    return out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)


def paste_logo(im, light=False):
    mark = logo(light=light)
    im.paste(mark, (72, 62), mark)


def wrap_text(draw, text, face, max_width):
    words, rows, row = text.split(), [], ""
    for word in words:
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


def panel(index):
    src = Image.open(SOURCE).convert("RGB")
    pw = src.width / 3
    left = round(index * pw + (5 if index else 0))
    right = round((index + 1) * pw - (5 if index < 2 else 0))
    return src.crop((left, 0, right, src.height))


def photo_background(index=1, darken=0):
    base = ImageOps.fit(panel(index), (W, H), Image.Resampling.LANCZOS, centering=(0.5, 0.48)).convert("RGBA")
    if darken:
        overlay = Image.new("RGBA", base.size, (34, 26, 22, darken))
        base = Image.alpha_composite(base, overlay)
    return base


def gradient_overlay(im, top_alpha=225, bottom_alpha=185):
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    px = overlay.load()
    for y in range(H):
        if y < 650:
            a = round(top_alpha * (1 - y / 650))
            c = PAPER
        elif y > 1320:
            a = round(bottom_alpha * ((y - 1320) / 600))
            c = DARK
        else:
            a, c = 0, DARK
        if a:
            for x in range(W):
                px[x, y] = (*c, min(255, a))
    return Image.alpha_composite(im, overlay)


def hook_scene():
    im = gradient_overlay(photo_background(1), 245, 165)
    paste_logo(im)
    d = ImageDraw.Draw(im)
    d.text((72, 275), "Wajah bulat", font=font(FONT_SERIF_BOLD, 82), fill=DARK)
    d.text((72, 375), "bukan masalah.", font=font(FONT_SERIF_BOLD, 82), fill=DARK)
    d.rounded_rectangle((72, 500, 870, 596), radius=48, fill=(*PAPER, 235))
    d.text((112, 528), "Coba 3 framing ini.", font=font(FONT_SANS_BOLD, 38), fill=DARK)
    d.text((72, 1722), "Ubah framing, bukan wajahmu.", font=font(FONT_SANS_BOLD, 31), fill=PAPER)
    return im.convert("RGB")


def option_scene(index, number, title, subtitle):
    im = gradient_overlay(photo_background(index), 195, 205)
    paste_logo(im)
    d = ImageDraw.Draw(im)
    d.ellipse((72, 272, 166, 366), fill=TAUPE)
    d.text((119, 319), str(number), font=font(FONT_SANS_BOLD, 39), fill=PAPER, anchor="mm")
    d.text((192, 270), title, font=font(FONT_SERIF_BOLD, 66), fill=DARK)
    text_block(d, subtitle, (192, 355), font(FONT_SANS, 30), MUTED, 760, 43)
    d.rounded_rectangle((72, 1608, 1008, 1788), radius=30, fill=(*PAPER, 225))
    d.text((112, 1650), "Efek visual berbeda—", font=font(FONT_SANS_BOLD, 31), fill=DARK)
    d.text((112, 1701), "pilih yang terasa nyaman.", font=font(FONT_SANS, 31), fill=DARK)
    return im.convert("RGB")


def cta_scene():
    im = Image.new("RGB", (W, H), CREAM).convert("RGBA")
    paste_logo(im)
    d = ImageDraw.Draw(im)
    d.text((72, 330), "Mana yang paling", font=font(FONT_SERIF_BOLD, 75), fill=DARK)
    d.text((72, 425), "kamu suka?", font=font(FONT_SERIF_BOLD, 75), fill=DARK)
    d.text((72, 565), "A — soft open", font=font(FONT_SANS_BOLD, 38), fill=DARK)
    d.text((72, 635), "B — gentle structure", font=font(FONT_SANS_BOLD, 38), fill=DARK)
    d.text((72, 705), "C — vertical drape", font=font(FONT_SANS_BOLD, 38), fill=DARK)
    thumbs = []
    for i in range(3):
        p = ImageOps.fit(panel(i), (280, 560), Image.Resampling.LANCZOS, centering=(0.5, 0.42))
        thumbs.append(p)
        im.paste(p, (72 + i * 312, 890))
    d.text((72, 1585), "Tulis A, B, atau C—atau simpan", font=font(FONT_SANS_BOLD, 31), fill=DARK)
    d.text((72, 1635), "untuk dicoba saat styling.", font=font(FONT_SANS, 31), fill=DARK)
    d.text((72, 1778), "Semua opsi valid. Kenyamanan tetap utama.", font=font(FONT_SANS, 25), fill=MUTED)
    return im.convert("RGB")


def story(title, body, index, filename, sticker_hint=None):
    im = gradient_overlay(photo_background(index), 235, 200)
    paste_logo(im)
    d = ImageDraw.Draw(im)
    y = text_block(d, title, (72, 300), font(FONT_SERIF_BOLD, 72), DARK, 930, 87)
    text_block(d, body, (72, y + 48), font(FONT_SANS, 31), DARK, 900, 47)
    if sticker_hint:
        d.rounded_rectangle((72, 1425, 1008, 1690), radius=32, fill=(*PAPER, 225), outline=LINE, width=3)
        d.text((112, 1488), sticker_hint, font=font(FONT_SANS_BOLD, 28), fill=MUTED)
    im.convert("RGB").save(ASSETS / filename, optimize=True)


def write_frames_and_stories():
    scenes = [
        hook_scene(),
        option_scene(0, 1, "Soft open", "Garis depan rileks, volume samping ringan."),
        option_scene(1, 2, "Gentle structure", "Sedikit tinggi di atas, jatuh seimbang di sisi."),
        option_scene(2, 3, "Vertical drape", "Jatuh memanjang dengan volume samping rendah."),
        cta_scene(),
    ]
    names = ["scene-01-hook.png", "scene-02-soft-open.png", "scene-03-gentle-structure.png", "scene-04-vertical-drape.png", "scene-05-cta.png"]
    for im, name in zip(scenes, names):
        im.save(ASSETS / name, optimize=True)
    scenes[0].save(ASSETS / "reel-cover.png", optimize=True)
    story("Wajah bulat bukan masalah.", "Tiga framing ini memberi arah visual berbeda—bukan aturan untuk mengoreksi wajah.", 1, "story-01-teaser.png", "Lanjut ke Reel untuk melihat A / B / C")
    story("A atau B?", "A: soft open.  B: gentle structure. Pilih berdasarkan efek visual dan rasa nyaman.", 0, "story-02-poll.png", "Tambahkan Poll: A — SOFT / B — STRUCTURED")
    story("Framing mana yang ingin kamu coba?", "Tulis A, B, atau C. Kamu juga boleh sebut bahan hijab yang biasa dipakai.", 2, "story-03-question.png", "Tambahkan Questions: A, B, atau C?")
    return scenes


def zoom_frame(src, progress):
    scale = 1.0 + 0.025 * progress
    nw, nh = round(W * scale), round(H * scale)
    tmp = src.resize((nw, nh), Image.Resampling.BICUBIC)
    left, top = (nw - W) // 2, round((nh - H) * 0.42)
    return tmp.crop((left, top, left + W, top + H))


def render_video(scenes):
    durations = [2.0, 3.5, 3.5, 3.5, 2.5]
    command = [
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(ASSETS / "reel-final.mp4")
    ]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for scene, duration in zip(scenes, durations):
        total = round(duration * FPS)
        for i in range(total):
            frame = zoom_frame(scene, i / max(1, total - 1))
            proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("FFmpeg render failed")


def contact_sheet():
    names = ["scene-01-hook.png", "scene-02-soft-open.png", "scene-03-gentle-structure.png", "scene-04-vertical-drape.png", "scene-05-cta.png"]
    sheet = Image.new("RGB", (1290, 590), PAPER)
    d = ImageDraw.Draw(sheet)
    d.text((35, 22), "DAY 06 — Reel keyframes", font=font(FONT_SANS_BOLD, 27), fill=DARK)
    for i, name in enumerate(names):
        im = Image.open(ASSETS / name).convert("RGB")
        im.thumbnail((220, 390), Image.Resampling.LANCZOS)
        x = 35 + i * 250
        sheet.paste(im, (x, 82))
        d.text((x, 500), str(i + 1), font=font(FONT_SANS_BOLD, 22), fill=MUTED)
    sheet.save(ASSETS / "contact-sheet.png", optimize=True)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    result = write_frames_and_stories()
    render_video(result)
    contact_sheet()
