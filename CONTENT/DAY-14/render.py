from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "denim-five-color-source.png"
W, H = 1080, 1920
FPS = 30

CREAM = "#F3EDE5"
PAPER = "#FFFDF9"
INK = "#282522"
MUTED = "#6B625B"
BLUE = "#53708B"
IVORY = "#D5CBBE"
TAUPE = "#8D7668"
ROSE = "#A87078"
OLIVE = "#69705B"
BURGUNDY = "#752A3A"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def txt(draw, xy, value, size, fill=INK, bold=False, anchor="la", spacing=10):
    draw.multiline_text(xy, value, font=font(size, bold), fill=fill,
                        anchor=anchor, spacing=spacing)


def fit_crop(image, size, focus_x=0.5, focus_y=0.42):
    target = size[0] / size[1]
    ratio = image.width / image.height
    if ratio > target:
        nw = int(image.height * target)
        left = int((image.width - nw) * focus_x)
        image = image.crop((left, 0, left + nw, image.height))
    else:
        nh = int(image.width / target)
        top = int((image.height - nh) * focus_y)
        top = max(0, min(top, image.height - nh))
        image = image.crop((0, top, image.width, top + nh))
    return image.resize(size, Image.Resampling.LANCZOS)


def footer(draw):
    txt(draw, (70, 1845), "@hijabsyaricoid", 28, fill=MUTED)


def panels(source):
    step = source.height // 5
    return [source.crop((0, i * step, source.width,
                         source.height if i == 4 else (i + 1) * step)) for i in range(5)]


def soft_top(base, height=760):
    over = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    for y in range(height):
        alpha = int(236 * (1 - y / height))
        d.line((0, y, W, y), fill=(243, 237, 229, alpha))
    return Image.alpha_composite(base.convert("RGBA"), over).convert("RGB")


def hook_scene(source):
    base = soft_top(fit_crop(source, (W, H), 0.5, 0.5), 820)
    d = ImageDraw.Draw(base)
    txt(d, (70, 105), "Outfit denim +\nhijab apa?", 88, bold=True, spacing=8)
    txt(d, (70, 336), "Coba 5 arah warna ini.", 43, fill=MUTED, bold=True)
    d.rounded_rectangle((70, 1475, 1010, 1735), radius=44, fill="#FFFDFCEC")
    txt(d, (540, 1548), "Satu outfit, lima nuansa", 39,
        bold=True, anchor="ma")
    txt(d, (540, 1636), "Bandingkan dengan denim yang benar-benar kamu punya.",
        29, fill=MUTED, anchor="ma")
    footer(d)
    return base


def color_scene(panel, number, name, descriptor, accent):
    base = Image.new("RGB", (W, H), CREAM)
    portrait = fit_crop(panel, (W, 1390), 0.5, 0.48)
    base.paste(portrait, (0, 0))
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((54, 1230, 1026, 1790), radius=52, fill=PAPER)
    d.rounded_rectangle((84, 1288, 164, 1368), radius=28, fill=accent)
    txt(d, (124, 1328), str(number), 33, fill="white", bold=True, anchor="mm")
    txt(d, (204, 1295), name, 54, bold=True)
    txt(d, (84, 1434), descriptor, 40, fill=MUTED, bold=True, spacing=9)
    txt(d, (84, 1606), "Amati hasilnya pada wash denim\ndan cahaya yang kamu pakai.",
        31, fill=INK, spacing=8)
    footer(d)
    return base


def comparison_scene(source):
    base = Image.new("RGB", (W, H), CREAM)
    base.paste(fit_crop(source, (W, 1390), 0.5, 0.5), (0, 0))
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((54, 1235, 1026, 1790), radius=52, fill=PAPER)
    txt(d, (84, 1300), "Denim yang sama,\nnuansanya bisa berubah.", 54,
        bold=True, spacing=8)
    txt(d, (84, 1470), "Ivory terasa ringan · taupe terasa netral\nrose lebih lembut · olive lebih earthy\nburgundy memberi kontras lebih kuat",
        31, fill=MUTED, spacing=10)
    footer(d)
    return base


def end_scene(source):
    base = fit_crop(source, (W, H), 0.5, 0.5)
    veil = Image.new("RGBA", (W, H), (243, 237, 229, 226))
    base = Image.alpha_composite(base.convert("RGBA"), veil).convert("RGB")
    d = ImageDraw.Draw(base)
    txt(d, (70, 160), "Tes sebelum memilih", 72, bold=True)
    checks = [
        "Samakan outfit dan pencahayaan.",
        "Foto satu warna per frame.",
        "Bandingkan berdampingan.",
        "Pilih nuansa yang kamu suka.",
    ]
    y = 430
    for item in checks:
        d.ellipse((78, y + 10, 108, y + 40), fill=BLUE)
        txt(d, (140, y), item, 38, bold=True)
        y += 148
    d.rounded_rectangle((70, 1180, 1010, 1505), radius=46, fill=PAPER)
    txt(d, (540, 1270), "Simpan untuk referensi\noutfit denim berikutnya.",
        51, bold=True, anchor="ma", spacing=8)
    footer(d)
    return base


def story_poll(source):
    base = soft_top(fit_crop(source, (W, H), 0.5, 0.5), 790)
    d = ImageDraw.Draw(base)
    txt(d, (70, 130), "Kalau pakai denim,\nkamu pilih…", 78, bold=True, spacing=8)
    txt(d, (70, 346), "Arah netral atau berwarna?", 37, fill=MUTED, bold=True)
    d.rounded_rectangle((70, 1390, 1010, 1715), radius=46, fill="#FFFDFCEC")
    txt(d, (540, 1460), "TAMBAHKAN POLL", 27, fill=TAUPE, bold=True, anchor="mm")
    txt(d, (540, 1580), "NETRAL  /  COLOR", 47, bold=True, anchor="mm")
    footer(d)
    return base


def story_palette(source):
    ps = panels(source)
    base = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(base)
    txt(d, (70, 130), "5 arah warna\nuntuk outfit denim", 72, bold=True, spacing=8)
    names = ["SOFT IVORY", "WARM TAUPE", "DUSTY ROSE", "MUTED OLIVE", "BURGUNDY"]
    colors = [IVORY, TAUPE, ROSE, OLIVE, BURGUNDY]
    y = 400
    for panel, name, color in zip(ps, names, colors):
        image = fit_crop(panel, (265, 238), 0.5, 0.42)
        base.paste(image, (70, y))
        d = ImageDraw.Draw(base)
        d.rounded_rectangle((365, y, 1010, y + 238), radius=34, fill=PAPER)
        d.ellipse((405, y + 74, 495, y + 164), fill=color)
        txt(d, (535, y + 119), name, 35, bold=True, anchor="lm")
        y += 264
    footer(d)
    return base


def story_question(panel):
    base = fit_crop(panel, (W, H), 0.5, 0.46)
    veil = Image.new("RGBA", (W, H), (34, 31, 28, 68))
    base = Image.alpha_composite(base.convert("RGBA"), veil).convert("RGB")
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((54, 120, 1026, 1035), radius=50, fill="#FFFDF0EE")
    txt(d, (96, 205), "Pilihanmu untuk\ndenim: warna apa?", 68, bold=True, spacing=8)
    txt(d, (96, 420), "Tulis warna hijab dan wash denim\nyang paling sering kamu pakai.",
        34, fill=MUTED, spacing=9)
    d.rounded_rectangle((96, 640, 984, 924), radius=38,
                        fill="#F2EAE2", outline="#D5C7BB", width=3)
    txt(d, (540, 718), "TAMBAHKAN QUESTIONS", 26,
        fill=TAUPE, bold=True, anchor="mm")
    txt(d, (540, 822), "Denim-ku… + hijab…", 38, bold=True, anchor="mm")
    footer(d)
    return base


def save_png(image, path):
    # Save through a verified sibling, then replace atomically. This prevents
    # a partially written PNG from surviving an interrupted render.
    tmp = path.with_name(path.stem + ".rendering.png")
    encoded = image.convert("RGB").quantize(
        colors=256, method=Image.Quantize.MEDIANCUT)
    if tmp.exists():
        tmp.unlink()
    for attempt in range(3):
        encoded.save(tmp, optimize=False)
        try:
            with Image.open(tmp) as check:
                check.load()
            tmp.replace(path)
            return
        except (OSError, SyntaxError):
            if tmp.exists():
                tmp.unlink()
            if attempt == 2:
                raise


def save_assets(source):
    ps = panels(source)
    scenes = [
        hook_scene(source),
        color_scene(ps[0], 1, "Soft ivory", "Ringan, clean, dan kontras lembut.", IVORY),
        color_scene(ps[1], 2, "Warm taupe", "Netral hangat yang tetap tenang.", TAUPE),
        color_scene(ps[2], 3, "Dusty rose", "Lembut dengan sentuhan warna.", ROSE),
        color_scene(ps[3], 4, "Muted olive", "Arah earthy yang lebih grounded.", OLIVE),
        color_scene(ps[4], 5, "Deep burgundy", "Kontras yang lebih kuat dan rich.", BURGUNDY),
        comparison_scene(source),
        end_scene(source),
    ]
    scene_paths = []
    for i, scene in enumerate(scenes, 1):
        path = ASSETS / f"scene-{i:02d}.png"
        save_png(scene, path)
        scene_paths.append(path)
    save_png(hook_scene(source), ASSETS / "reel-cover.png")
    stories = [story_poll(source), story_palette(source), story_question(ps[3])]
    story_paths = []
    for i, story in enumerate(stories, 1):
        path = ASSETS / f"story-{i:02d}.png"
        save_png(story, path)
        story_paths.append(path)
    sheet = Image.new("RGB", (1080, 960), "white")
    for i, scene in enumerate(scenes):
        thumb = scene.convert("RGB").resize((270, 480), Image.Resampling.LANCZOS)
        sheet.paste(thumb, ((i % 4) * 270, (i // 4) * 480))
    save_png(sheet, ASSETS / "contact-sheet.png")
    story_sheet = Image.new("RGB", (810, 480), "white")
    for i, story in enumerate(stories):
        thumb = story.convert("RGB").resize((270, 480), Image.Resampling.LANCZOS)
        story_sheet.paste(thumb, (i * 270, 0))
    save_png(story_sheet, ASSETS / "stories-contact-sheet.png")
    return scenes


def render_video(scenes):
    # Exactly 510 frames = 17.00 seconds at 30 fps.
    frame_counts = [60, 66, 66, 66, 66, 66, 60, 60]
    small = [im.resize((720, 1280), Image.Resampling.LANCZOS) for im in scenes]
    cmd = [
        "ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", "720x1280", "-r", str(FPS), "-i", "-",
        "-vf", "scale=1080:1920:flags=lanczos,format=yuv420p",
        "-c:v", "libx264", "-preset", "slow", "-crf", "29",
        "-maxrate", "330k", "-bufsize", "660k", "-movflags", "+faststart",
        "-an", str(ASSETS / "reel-final.mp4")
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    transition = 6
    for idx, (scene, count) in enumerate(zip(small, frame_counts)):
        nxt = small[idx + 1] if idx + 1 < len(small) else None
        for frame_no in range(count):
            progress = frame_no / max(1, count - 1)
            scale = 1.0 + 0.012 * progress
            zw, zh = int(720 * scale), int(1280 * scale)
            frame = scene.resize((zw, zh), Image.Resampling.BICUBIC)
            frame = frame.crop(((zw - 720) // 2, (zh - 1280) // 2,
                                (zw - 720) // 2 + 720, (zh - 1280) // 2 + 1280))
            if nxt is not None and frame_no >= count - transition:
                alpha = (frame_no - (count - transition)) / transition
                frame = Image.blend(frame, nxt, alpha)
            proc.stdin.write(frame.convert("RGB").tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("FFmpeg render failed")


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    scenes = save_assets(source)
    render_video(scenes)


if __name__ == "__main__":
    main()
