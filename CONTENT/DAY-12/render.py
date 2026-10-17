from pathlib import Path
import subprocess
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "four-color-source.png"
W, H = 1080, 1920
FPS = 30

CREAM = "#F4EEE7"
WHITE = "#FFFDFC"
INK = "#282522"
MUTED = "#6B625B"
PEACH = "#D7A58E"
ROSE = "#AA7C83"
TEAL = "#557A7C"
IVORY = "#C9BDAE"

REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def txt(draw, xy, value, size, fill=INK, bold=False, anchor="la", spacing=10):
    draw.multiline_text(xy, value, font=font(size, bold), fill=fill,
                        anchor=anchor, spacing=spacing)


def fit_crop(image, size, focus_y=0.42):
    target = size[0] / size[1]
    ratio = image.width / image.height
    if ratio > target:
        new_w = int(image.height * target)
        left = (image.width - new_w) // 2
        image = image.crop((left, 0, left + new_w, image.height))
    else:
        new_h = int(image.width / target)
        top = int((image.height - new_h) * focus_y)
        top = max(0, min(top, image.height - new_h))
        image = image.crop((0, top, image.width, top + new_h))
    return image.resize(size, Image.Resampling.LANCZOS)


def add_gradient(base, top_alpha=225, height=720):
    over = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    for y in range(height):
        a = int(top_alpha * (1 - y / height))
        d.line((0, y, W, y), fill=(244, 238, 231, a))
    return Image.alpha_composite(base.convert("RGBA"), over).convert("RGB")


def footer(draw):
    txt(draw, (70, 1840), "@hijabsyaricoid", 28, fill=MUTED)


def split_panels(source):
    step = source.height // 4
    return [source.crop((0, i * step, source.width, (i + 1) * step)) for i in range(4)]


def hook_scene(source):
    base = fit_crop(source, (W, H), 0.5)
    base = add_gradient(base, 235, 800)
    d = ImageDraw.Draw(base)
    txt(d, (70, 110), "Wajah terlihat\nkurang fresh?", 86, bold=True, spacing=8)
    txt(d, (70, 325), "Coba ganti arah warnanya.", 40, fill=MUTED, bold=True)
    d.rounded_rectangle((70, 1470, 1010, 1735), radius=44, fill="#FFFDFCEB")
    txt(d, (540, 1540), "4 arah warna, satu kondisi yang sama", 36,
        bold=True, anchor="ma")
    txt(d, (540, 1625), "Bandingkan efek visualnya—bukan mencari warna universal.",
        27, fill=MUTED, anchor="ma")
    footer(d)
    return base


def color_scene(panel, number, color_name, descriptor, accent):
    base = Image.new("RGB", (W, H), CREAM)
    portrait = fit_crop(panel, (W, 1390), 0.45)
    base.paste(portrait, (0, 0))
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((54, 1230, 1026, 1785), radius=52, fill=WHITE)
    d.rounded_rectangle((84, 1290, 164, 1370), radius=30, fill=accent)
    txt(d, (124, 1330), str(number), 34, fill=WHITE, bold=True, anchor="mm")
    txt(d, (205, 1295), color_name, 55, bold=True)
    txt(d, (84, 1435), descriptor, 38, fill=MUTED, bold=True, spacing=9)
    txt(d, (84, 1605), "Amati wajahmu sendiri\ndi cahaya yang sama.", 32, fill=INK, spacing=8)
    footer(d)
    return base


def comparison_scene(source):
    base = Image.new("RGB", (W, H), CREAM)
    grid = fit_crop(source, (W, 1380), 0.5)
    base.paste(grid, (0, 0))
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((54, 1205, 1026, 1785), radius=52, fill=WHITE)
    txt(d, (84, 1270), "Tidak ada satu warna universal\nyang terasa fresh\nuntuk semua orang.", 50,
        bold=True, spacing=8)
    txt(d, (84, 1510), "Skin tone, pencahayaan, kamera, makeup,\ndan warna outfit bisa mengubah hasil visual.",
        31, fill=MUTED, spacing=9)
    footer(d)
    return base


def final_scene(source):
    base = fit_crop(source, (W, H), 0.5)
    veil = Image.new("RGBA", (W, H), (244, 238, 231, 225))
    base = Image.alpha_composite(base.convert("RGBA"), veil).convert("RGB")
    d = ImageDraw.Draw(base)
    txt(d, (70, 155), "Tes warna dalam\n30 detik", 82, bold=True, spacing=8)
    checks = [
        "Dekat jendela, tanpa filter.",
        "Outfit dan posisi kamera sama.",
        "Foto satu warna per frame.",
        "Pilih hasil yang kamu suka.",
    ]
    y = 510
    for item in checks:
        d.ellipse((76, y + 9, 102, y + 35), fill=TEAL)
        txt(d, (130, y), item, 40, bold=True)
        y += 145
    d.rounded_rectangle((70, 1190, 1010, 1515), radius=48, fill=WHITE)
    txt(d, (540, 1280), "Simpan untuk tes warna\ndi rumah.", 52,
        bold=True, anchor="ma", spacing=9)
    footer(d)
    return base


def story_poll(source):
    base = add_gradient(fit_crop(source, (W, H), 0.5), 235, 780)
    d = ImageDraw.Draw(base)
    txt(d, (70, 120), "Arah warna mana\nterasa paling fresh?", 78, bold=True, spacing=8)
    txt(d, (70, 330), "Pilih berdasarkan wajahmu sendiri.", 35, fill=MUTED, bold=True)
    d.rounded_rectangle((70, 1420, 1010, 1710), radius=46, fill="#FFFDFCEB")
    footer(d)
    return base


def story_checklist(source):
    base = Image.new("RGB", (W, H), CREAM)
    base.paste(fit_crop(source, (W, 760), 0.5), (0, 0))
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((54, 650, 1026, 1790), radius=54, fill=WHITE)
    txt(d, (84, 735), "Tes warna tanpa bias", 66, bold=True)
    items = ["Cahaya alami", "Tanpa filter", "Outfit yang sama", "Kamera di posisi sama"]
    y = 940
    for i, item in enumerate(items, 1):
        d.rounded_rectangle((84, y, 164, y + 80), radius=28, fill=TEAL)
        txt(d, (124, y + 40), str(i), 32, fill=WHITE, bold=True, anchor="mm")
        txt(d, (205, y + 15), item, 39, bold=True)
        y += 160
    footer(d)
    return base


def story_question(panels):
    base = Image.new("RGB", (W, H), CREAM)
    portrait = fit_crop(panels[1], (W, 940), 0.45)
    base.paste(portrait, (0, 0))
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((54, 810, 1026, 1790), radius=54, fill=WHITE)
    txt(d, (84, 905), "Warna hijab yang\npaling bikin ragu?", 68, bold=True, spacing=8)
    txt(d, (84, 1125), "Tulis warnanya. Bisa jadi bahan\nColor Lab berikutnya.", 34, fill=MUTED, spacing=9)
    d.rounded_rectangle((84, 1350, 996, 1630), radius=40,
                        fill="#F2ECE6", outline="#D7CBC1", width=3)
    footer(d)
    return base


def save_images(source):
    panels = split_panels(source)
    scenes = [
        hook_scene(source),
        color_scene(panels[0], 1, "Muted peach", "Memberi arah hangat\nyang lembut.", PEACH),
        color_scene(panels[1], 2, "Dusty rose", "Menambah warna\ntanpa terasa terlalu terang.", ROSE),
        color_scene(panels[2], 3, "Muted teal", "Memberi kontras dingin\nyang lebih tegas.", TEAL),
        color_scene(panels[3], 4, "Soft ivory", "Terasa ringan dan bersih—\ncek agar tidak terlalu menyatu.", IVORY),
        comparison_scene(source),
        final_scene(source),
    ]
    scene_paths = []
    for i, scene in enumerate(scenes, 1):
        path = ASSETS / f"scene-{i:02d}.png"
        scene.save(path, compress_level=6)
        scene_paths.append(path)

    cover = hook_scene(source)
    cover.save(ASSETS / "reel-cover.png", compress_level=6)

    stories = [story_poll(source), story_checklist(source), story_question(panels)]
    story_paths = []
    for i, story in enumerate(stories, 1):
        path = ASSETS / f"story-{i:02d}.png"
        story.save(path, compress_level=6)
        story_paths.append(path)

    sheet = Image.new("RGB", (1080, 960), WHITE)
    for i, path in enumerate(scene_paths):
        thumb = Image.open(path).convert("RGB").resize((270, 480), Image.Resampling.LANCZOS)
        sheet.paste(thumb, ((i % 4) * 270, (i // 4) * 480))
    sheet.save(ASSETS / "contact-sheet.png", compress_level=6)

    story_sheet = Image.new("RGB", (810, 480), WHITE)
    for i, path in enumerate(story_paths):
        thumb = Image.open(path).convert("RGB").resize((270, 480), Image.Resampling.LANCZOS)
        story_sheet.paste(thumb, (i * 270, 0))
    story_sheet.save(ASSETS / "stories-contact-sheet.png", compress_level=6)
    return scenes


def render_video(scenes):
    # Exactly 480 frames = 16.00 seconds at 30 fps.
    frame_counts = [60, 68, 68, 68, 68, 74, 74]
    small = [im.resize((720, 1280), Image.Resampling.LANCZOS) for im in scenes]
    cmd = [
        "ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", "720x1280", "-r", str(FPS), "-i", "-",
        "-vf", "scale=1080:1920:flags=lanczos,format=yuv420p",
        "-c:v", "libx264", "-preset", "slow", "-crf", "28",
        "-maxrate", "420k", "-bufsize", "840k", "-movflags", "+faststart",
        "-an", str(ASSETS / "reel-final.mp4")
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    transition = int(0.20 * FPS)
    for idx, (scene, frames) in enumerate(zip(small, frame_counts)):
        next_scene = small[idx + 1] if idx + 1 < len(small) else None
        for frame_no in range(frames):
            progress = frame_no / max(1, frames - 1)
            scale = 1.0 + 0.012 * progress
            zw, zh = int(720 * scale), int(1280 * scale)
            frame = scene.resize((zw, zh), Image.Resampling.BICUBIC)
            frame = frame.crop(((zw - 720) // 2, (zh - 1280) // 2,
                                (zw - 720) // 2 + 720, (zh - 1280) // 2 + 1280))
            if next_scene is not None and frame_no >= frames - transition:
                alpha = (frame_no - (frames - transition)) / transition
                frame = Image.blend(frame, next_scene, alpha)
            proc.stdin.write(frame.convert("RGB").tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("FFmpeg render failed")


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGB")
    scenes = save_images(source)
    render_video(scenes)


if __name__ == "__main__":
    main()
