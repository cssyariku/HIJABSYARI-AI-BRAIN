"""Render Day 19 Reel, cover, Stories, and QA previews.

Run: python CONTENT/DAY-19/render.py
Requires: Pillow and FFmpeg.
"""

from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "clean-looks-triptych.jpg"

W, H, FPS = 1080, 1920, 30
PAPER = (250, 247, 241)
CREAM = (242, 236, 226)
DARK = (47, 41, 37)
MUTED = (101, 91, 84)
TAUPE = (145, 125, 111)
SAGE = (128, 134, 108)
CHARCOAL = (58, 58, 58)
LINE = (207, 195, 184)
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


def photo(index, shade=0):
    base = ImageOps.fit(panel(index), (W, H), Image.Resampling.LANCZOS,
                        centering=(.5, .48)).convert("RGBA")
    if shade:
        base = Image.alpha_composite(base, Image.new("RGBA", (W, H), (35, 28, 24, shade)))
    return base


def gradient(base, top=240, bottom=180):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for y in range(0, 720):
        a = round(top * (1 - y / 720))
        d.line((0, y, W, y), fill=(*PAPER, a))
    for y in range(1320, H):
        a = round(bottom * ((y - 1320) / 600))
        d.line((0, y, W, y), fill=(*DARK, a))
    return Image.alpha_composite(base, ov)


def hook_scene():
    im = gradient(photo(1), 246, 170)
    d = ImageDraw.Draw(im)
    text_block(d, "Clean look nggak harus serba putih.", (72, 196),
               font(SERIF_BOLD, 72), DARK, 900, 86)
    rounded(d, (72, 510, 780, 610), 46, (*PAPER, 233))
    d.text((112, 540), "Tiga nuansa. Tetap clean.", font=font(SANS_BOLD, 30), fill=DARK)
    d.text((72, 1734), "Light · soft · deep", font=font(SANS_BOLD, 32), fill=PAPER)
    handle(d, light=True)
    return im.convert("RGB")


def look_scene(index, number, title, palette, descriptors, accent):
    im = gradient(photo(index), 220, 195)
    d = ImageDraw.Draw(im)
    d.ellipse((72, 220, 174, 322), fill=accent)
    d.text((123, 271), number, font=font(SANS_BOLD, 27), fill=PAPER, anchor="mm")
    d.text((202, 210), title, font=font(SERIF_BOLD, 64), fill=DARK)
    d.text((202, 302), palette, font=font(SANS_BOLD, 27), fill=MUTED)
    rounded(d, (72, 1560, 1008, 1760), 36, (*PAPER, 232), LINE)
    d.text((112, 1610), descriptors, font=font(SANS_BOLD, 30), fill=DARK)
    d.text((112, 1680), "Siluet sederhana · detail tenang", font=font(SANS, 27), fill=MUTED)
    handle(d, light=True)
    return im.convert("RGB")


def recap_scene():
    im = Image.new("RGB", (W, H), CREAM).convert("RGBA")
    d = ImageDraw.Draw(im)
    d.text((72, 150), "Light, soft, atau deep?", font=font(SERIF_BOLD, 67), fill=DARK)
    d.text((72, 254), "Pilih yang paling dekat dengan isi lemarimu.",
           font=font(SANS, 28), fill=MUTED)
    labels = [("01", "LIGHT"), ("02", "SOFT"), ("03", "DEEP")]
    for i, (num, label) in enumerate(labels):
        x = 54 + i * 342
        p = ImageOps.fit(panel(i), (306, 1000), Image.Resampling.LANCZOS, centering=(.5, .48))
        im.paste(p, (x, 400))
        rounded(d, (x + 18, 1315, x + 288, 1437), 30, PAPER, LINE)
        d.text((x + 153, 1353), num, font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
        d.text((x + 153, 1398), label, font=font(SANS_BOLD, 21), fill=DARK, anchor="mm")
    rounded(d, (72, 1540, 1008, 1718), 36, TAUPE)
    d.text((540, 1592), "Simpan referensinya.", font=font(SANS_BOLD, 34), fill=PAPER, anchor="mm")
    d.text((540, 1654), "Kamu pilih 1, 2, atau 3?", font=font(SANS, 28), fill=PAPER, anchor="mm")
    handle(d)
    return im.convert("RGB")


def cover():
    im = gradient(photo(1), 248, 166)
    d = ImageDraw.Draw(im)
    text_block(d, "3 clean hijab looks", (72, 188), font(SERIF_BOLD, 78), DARK, 900, 92)
    rounded(d, (72, 404, 714, 506), 46, (*PAPER, 233))
    d.text((112, 435), "Light · soft · deep", font=font(SANS_BOLD, 31), fill=DARK)
    handle(d, light=True)
    return im.convert("RGB")


def story_teaser():
    im = recap_scene()
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 350), fill=PAPER)
    text_block(d, "Tiga clean hijab looks", (72, 115), font(SERIF_BOLD, 69), DARK, 900, 82)
    return im


def story_poll():
    im = gradient(photo(2), 245, 170)
    d = ImageDraw.Draw(im)
    text_block(d, "Kalau harus pilih satu…", (72, 180), font(SERIF_BOLD, 72), DARK, 900, 86)
    d.text((72, 410), "Light minimal atau deep clean?", font=font(SANS_BOLD, 31), fill=DARK)
    rounded(d, (72, 590, 1008, 880), 40, (*PAPER, 235), LINE)
    d.text((540, 670), "RUANG POLL INSTAGRAM", font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
    d.text((540, 780), "LIGHT   /   DEEP", font=font(SANS_BOLD, 39), fill=DARK, anchor="mm")
    handle(d, light=True)
    return im.convert("RGB")


def story_question():
    im = gradient(photo(0), 245, 174)
    d = ImageDraw.Draw(im)
    text_block(d, "Look mana yang paling dekat dengan gayamu?", (72, 180),
               font(SERIF_BOLD, 68), DARK, 900, 82)
    rounded(d, (72, 610, 1008, 930), 40, (*PAPER, 235), LINE)
    d.text((540, 695), "RUANG QUESTIONS STICKER", font=font(SANS_BOLD, 25), fill=TAUPE, anchor="mm")
    d.text((540, 812), "1, 2, atau 3 + dipakai ke mana?", font=font(SANS_BOLD, 31), fill=DARK, anchor="mm")
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
            raise ValueError(f"Dimension mismatch: {path}")
    tmp.replace(path)


def write_stills():
    scenes = [
        hook_scene(),
        look_scene(0, "01", "Light minimal", "Ivory + oatmeal", "Ringan · tonal · lembut", TAUPE),
        look_scene(1, "02", "Soft contrast", "Taupe + cream + muted sage", "Tenang · berlapis · clean", SAGE),
        look_scene(2, "03", "Deep clean", "Charcoal + dark mocha", "Dalam · sederhana · tegas", CHARCOAL),
        recap_scene(),
    ]
    names = ["hook", "light-minimal", "soft-contrast", "deep-clean", "recap"]
    for i, (scene, name) in enumerate(zip(scenes, names), 1):
        save_png(scene, ASSETS / f"scene-{i:02d}-{name}.png")
    save_png(cover(), ASSETS / "reel-cover.png")
    stories = [story_teaser(), story_poll(), story_question()]
    for i, story in enumerate(stories, 1):
        save_png(story, ASSETS / f"story-{i:02d}.png")
    return scenes, stories


def zoom_frame(src, progress):
    scale = 1.0 + .025 * progress
    nw, nh = round(W * scale), round(H * scale)
    temp = src.resize((nw, nh), Image.Resampling.BICUBIC)
    left, top = (nw - W) // 2, round((nh - H) * .46)
    return temp.crop((left, top, left + W, top + H))


def render_video(scenes):
    frames = [66, 93, 93, 93, 105]
    command = [
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an",
        "-c:v", "libx264", "-preset", "slow", "-crf", "32", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(ASSETS / "reel-final.mp4"),
    ]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for scene, total in zip(scenes, frames):
        for i in range(total):
            proc.stdin.write(zoom_frame(scene, i / max(1, total - 1)).tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("FFmpeg render failed")


def sheet(images, output, cols, thumb):
    rows = (len(images) + cols - 1) // cols
    canvas = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows + 56), PAPER)
    d = ImageDraw.Draw(canvas)
    d.text((24, 14), "DAY 19 — QA PREVIEW", font=font(SANS_BOLD, 25), fill=DARK)
    for i, im in enumerate(images):
        canvas.paste(im.resize(thumb, Image.Resampling.LANCZOS),
                     ((i % cols) * thumb[0], 56 + (i // cols) * thumb[1]))
    save_png(canvas, output)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    scenes, stories = write_stills()
    render_video(scenes)
    sheet(scenes, ASSETS / "contact-sheet.png", 5, (216, 384))
    sheet(stories, ASSETS / "stories-contact-sheet.png", 3, (270, 480))


if __name__ == "__main__":
    main()

