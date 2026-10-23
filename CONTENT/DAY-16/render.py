"""Render Day 16 Reel, cover, Stories, and QA previews.

Run: python CONTENT/DAY-16/render.py
Requires: Pillow and FFmpeg.
"""

from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "face-framing-oval-triptych.jpg"

W, H, FPS = 1080, 1920, 30
PAPER = (250, 247, 241)
CREAM = (242, 234, 224)
DARK = (48, 41, 37)
MUTED = (103, 91, 84)
TAUPE = (153, 126, 110)
ROSE = (177, 132, 132)
LINE = (208, 192, 179)
WHITE = (255, 255, 255)
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def rounded(draw, box, radius=34, fill=PAPER, outline=None, width=2):
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


def handle(draw, light=False, y=1832):
    draw.text((72, y), "@hijabsyaricoid", font=font(SANS, 23),
              fill=PAPER if light else MUTED)


def panel(index):
    src = Image.open(SOURCE).convert("RGB")
    third = src.width / 3
    pad = 4
    left = round(index * third) + (pad if index else 0)
    right = round((index + 1) * third) - (pad if index < 2 else 0)
    return src.crop((left, 0, right, src.height))


def photo(index, darken=0, center_y=.42):
    base = ImageOps.fit(panel(index), (W, H), Image.Resampling.LANCZOS,
                        centering=(.5, center_y)).convert("RGBA")
    if darken:
        base = Image.alpha_composite(base, Image.new("RGBA", (W, H), (36, 28, 24, darken)))
    return base


def gradient(base, top=235, bottom=190):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = ov.load()
    for y in range(H):
        if y < 700:
            a = round(top * (1 - y / 700))
            color = PAPER
        elif y > 1310:
            a = round(bottom * ((y - 1310) / 610))
            color = DARK
        else:
            a, color = 0, DARK
        if a:
            for x in range(W):
                px[x, y] = (*color, min(255, a))
    return Image.alpha_composite(base, ov)


def hook_scene():
    im = gradient(photo(1), 246, 176)
    d = ImageDraw.Draw(im)
    d.text((72, 206), "Wajah oval?", font=font(SERIF_BOLD, 82), fill=DARK)
    text_block(d, "Coba 3 framing dengan nuansa berbeda.", (72, 314),
               font(SERIF_BOLD, 66), DARK, 880, 80)
    rounded(d, (72, 562, 786, 656), radius=45, fill=(*PAPER, 232))
    d.text((112, 589), "Soft · clean · relaxed", font=font(SANS_BOLD, 32), fill=DARK)
    d.text((72, 1738), "Tiga pilihan. Tidak ada yang wajib.", font=font(SANS_BOLD, 30), fill=PAPER)
    handle(d, light=True)
    return im.convert("RGB")


def option_scene(index, letter, title, subtitle, accent):
    im = gradient(photo(index), 205, 208)
    d = ImageDraw.Draw(im)
    d.ellipse((72, 228, 170, 326), fill=accent)
    d.text((121, 277), letter, font=font(SANS_BOLD, 38), fill=PAPER, anchor="mm")
    d.text((196, 218), title, font=font(SERIF_BOLD, 65), fill=DARK)
    text_block(d, subtitle, (196, 315), font(SANS, 30), MUTED, 760, 43)
    rounded(d, (72, 1582, 1008, 1766), radius=32, fill=(*PAPER, 229), outline=LINE)
    d.text((112, 1625), "Efek visual berbeda.", font=font(SANS_BOLD, 31), fill=DARK)
    d.text((112, 1681), "Kenyamanan tetap jadi patokan.", font=font(SANS, 29), fill=DARK)
    handle(d, light=True)
    return im.convert("RGB")


def recap_scene():
    im = Image.new("RGB", (W, H), CREAM).convert("RGBA")
    d = ImageDraw.Draw(im)
    d.text((72, 166), "A, B, atau C?", font=font(SERIF_BOLD, 78), fill=DARK)
    d.text((72, 280), "Pilih yang nyaman dan sesuai bahan hijabmu.",
           font=font(SANS, 29), fill=MUTED)
    labels = [("A", "SOFT CURVE"), ("B", "CLEAN ANGLE"), ("C", "RELAXED DRAPE")]
    for i, (letter, label) in enumerate(labels):
        x = 54 + i * 342
        p = ImageOps.fit(panel(i), (306, 852), Image.Resampling.LANCZOS, centering=(.5, .39))
        im.paste(p, (x, 460))
        rounded(d, (x + 18, 1244, x + 288, 1368), radius=30, fill=PAPER, outline=LINE)
        d.text((x + 153, 1281), letter, font=font(SANS_BOLD, 30), fill=TAUPE, anchor="mm")
        d.text((x + 153, 1327), label, font=font(SANS_BOLD, 19), fill=DARK, anchor="mm")
    rounded(d, (72, 1504, 1008, 1698), radius=36, fill=TAUPE)
    d.text((112, 1550), "Simpan untuk dicoba saat styling.", font=font(SANS_BOLD, 32), fill=PAPER)
    d.text((112, 1608), "Tidak perlu menarik kain terlalu ketat.", font=font(SANS, 27), fill=PAPER)
    handle(d)
    return im.convert("RGB")


def story_teaser():
    im = gradient(photo(1), 246, 176)
    d = ImageDraw.Draw(im)
    text_block(d, "Wajah oval, tiga opsi framing.", (72, 196),
               font(SERIF_BOLD, 72), DARK, 900, 86)
    text_block(d, "Bukan aturan untuk mengoreksi wajah—hanya tiga nuansa visual yang bisa kamu coba.",
               (72, 430), font(SANS, 30), DARK, 880, 45)
    rounded(d, (72, 660, 1008, 824), radius=36, fill=(*PAPER, 229), outline=LINE)
    d.text((112, 705), "Lihat A · B · C di Reel", font=font(SANS_BOLD, 34), fill=DARK)
    handle(d, light=True)
    return im.convert("RGB")


def story_poll():
    im = gradient(photo(0), 246, 172)
    d = ImageDraw.Draw(im)
    text_block(d, "Kamu lebih suka A atau B?", (72, 196),
               font(SERIF_BOLD, 72), DARK, 900, 86)
    d.text((72, 430), "A — soft curve", font=font(SANS_BOLD, 34), fill=DARK)
    d.text((72, 486), "B — clean angle", font=font(SANS_BOLD, 34), fill=DARK)
    rounded(d, (72, 650, 1008, 930), radius=38, fill=(*PAPER, 232), outline=LINE)
    d.text((540, 724), "RUANG POLL INSTAGRAM", font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
    d.text((540, 832), "A — SOFT   /   B — CLEAN", font=font(SANS_BOLD, 34), fill=DARK, anchor="mm")
    handle(d, light=True)
    return im.convert("RGB")


def story_question():
    im = gradient(photo(2), 246, 177)
    d = ImageDraw.Draw(im)
    text_block(d, "Framing mana yang ingin kamu coba?", (72, 196),
               font(SERIF_BOLD, 68), DARK, 900, 82)
    text_block(d, "Tulis A, B, atau C. Boleh sekalian sebut bahan hijab yang biasa kamu pakai.",
               (72, 442), font(SANS, 30), DARK, 880, 45)
    rounded(d, (72, 690, 1008, 986), radius=38, fill=(*PAPER, 232), outline=LINE)
    d.text((540, 770), "RUANG QUESTIONS STICKER", font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
    d.text((540, 884), "A, B, atau C?", font=font(SANS_BOLD, 38), fill=DARK, anchor="mm")
    handle(d, light=True)
    return im.convert("RGB")


def save_png(im, path):
    tmp = path.with_name(path.stem + ".rendering.png")
    if tmp.exists():
        tmp.unlink()
    im.convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(tmp, optimize=False)
    with Image.open(tmp) as check:
        check.load()
        if check.size != im.size:
            raise ValueError(f"Dimension mismatch: {tmp}")
    tmp.replace(path)


def write_stills():
    scenes = [
        hook_scene(),
        option_scene(0, "A", "Soft curve", "Garis depan membulat, kesannya lebih lembut.", TAUPE),
        option_scene(1, "B", "Clean angle", "Sudut ringan, kesannya lebih rapi.", ROSE),
        option_scene(2, "C", "Relaxed drape", "Bukaan lebih rileks, jatuh kain memanjang.", (126, 136, 121)),
        recap_scene(),
    ]
    for i, scene in enumerate(scenes, 1):
        save_png(scene, ASSETS / f"scene-{i:02d}-{'hook' if i == 1 else 'cta' if i == 5 else ['soft-curve','clean-angle','relaxed-drape'][i-2]}.png")
    save_png(scenes[0], ASSETS / "reel-cover.png")
    stories = [story_teaser(), story_poll(), story_question()]
    for i, story in enumerate(stories, 1):
        save_png(story, ASSETS / f"story-{i:02d}.png")
    return scenes, stories


def zoom_frame(src, progress):
    scale = 1.0 + .025 * progress
    nw, nh = round(W * scale), round(H * scale)
    tmp = src.resize((nw, nh), Image.Resampling.BICUBIC)
    left, top = (nw - W) // 2, round((nh - H) * .42)
    return tmp.crop((left, top, left + W, top + H))


def render_video(scenes):
    durations = [2.0, 3.5, 3.5, 3.5, 2.5]
    command = [
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an",
        "-c:v", "libx264", "-preset", "slow", "-crf", "33", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(ASSETS / "reel-final.mp4"),
    ]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for scene, duration in zip(scenes, durations):
        total = round(duration * FPS)
        for i in range(total):
            proc.stdin.write(zoom_frame(scene, i / max(1, total - 1)).tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("FFmpeg render failed")


def sheet(images, output, cols, thumb):
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows + 56), PAPER)
    d = ImageDraw.Draw(canvas)
    d.text((24, 14), "DAY 16 — QA PREVIEW", font=font(SANS_BOLD, 25), fill=DARK)
    for i, im in enumerate(images):
        small = im.resize(thumb, Image.Resampling.LANCZOS)
        canvas.paste(small, ((i % cols) * thumb[0], 56 + (i // cols) * thumb[1]))
    save_png(canvas, output)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    scenes, stories = write_stills()
    render_video(scenes)
    sheet(scenes, ASSETS / "contact-sheet.png", 5, (216, 384))
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480))


if __name__ == "__main__":
    main()
