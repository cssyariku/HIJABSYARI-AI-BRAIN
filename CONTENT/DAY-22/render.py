from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import subprocess

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "face-framing-square-triptych.png"
W, H, FPS = 1080, 1920, 30
SCENE_FRAMES = [72, 90, 90, 90, 108]

CREAM = "#F7F0E8"
INK = "#2A2522"
MUTED = "#6C615B"
ROSE = "#A65F6A"
TAUPE = "#8A7468"
WHITE = "#FFFDFC"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def fit(img, size, centering=(0.5, 0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=centering)


def split_panels(src):
    w = src.width // 3
    return [
        src.crop((0, 0, w, src.height)),
        src.crop((w, 0, w * 2, src.height)),
        src.crop((w * 2, 0, src.width, src.height)),
    ]


def wrapped(draw, value, box, fnt, fill=INK, spacing=10):
    x0, y0, x1, _ = box
    words = value.split()
    lines, cur = [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= x1 - x0:
            cur = test
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


def brand(draw):
    draw.ellipse((72, 1812, 90, 1830), fill=ROSE)
    draw.text((104, 1804), "HIJAB SYARI INDONESIA", font=font(22, True), fill=MUTED)


def photo_panel(panel_img, zoom=1.0):
    base = fit(panel_img, (W, H), (0.5, 0.42))
    if zoom <= 1:
        return base
    nw, nh = int(W * zoom), int(H * zoom)
    z = base.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - W) // 2
    top = int((nh - H) * 0.42)
    return z.crop((left, top, left + W, top + H))


def overlay_scene(image, title, subtitle, badge=None):
    base = image.copy()
    d = ImageDraw.Draw(base, "RGBA")
    d.rounded_rectangle((54, 106, 1026, 595), radius=46, fill=(247, 240, 232, 242))
    y = 170
    if badge:
        d.rounded_rectangle((94, 155, 318, 219), radius=30, fill=ROSE)
        d.text((206, 187), badge, font=font(25, True), fill=WHITE, anchor="mm")
        y = 270
    y = wrapped(d, title, (94, y, 976, 440), font(62, True), INK, 10)
    d.text((94, min(y + 25, 505)), subtitle, font=font(31), fill=MUTED)
    brand(d)
    return base


def recap(src, zoom=1.0):
    image = fit(src, (W, H), (0.5, 0.45))
    if zoom > 1:
        nw, nh = int(W * zoom), int(H * zoom)
        image = image.resize((nw, nh), Image.Resampling.LANCZOS)
        image = image.crop(((nw-W)//2, (nh-H)//2, (nw-W)//2+W, (nh-H)//2+H))
    d = ImageDraw.Draw(image, "RGBA")
    d.rounded_rectangle((54, 108, 1026, 580), radius=46, fill=(247, 240, 232, 244))
    wrapped(d, "Soft, clean, atau relaxed?", (94, 190, 976, 405), font(61, True), INK, 10)
    d.text((94, 460), "Simpan referensinya.", font=font(34, True), fill=ROSE)
    brand(d)
    return image


def scene_at(src, panels, index, progress):
    zoom = 1.0 + 0.025 * max(0.0, min(1.0, progress))
    if index == 0:
        return overlay_scene(
            photo_panel(panels[0], zoom),
            "Wajah square?",
            "Coba 3 framing dengan nuansa berbeda."
        )
    if index == 1:
        return overlay_scene(photo_panel(panels[0], zoom), "Soft curve",
                             "Garis depan membulat lembut.", "A")
    if index == 2:
        return overlay_scene(photo_panel(panels[1], zoom), "Clean line",
                             "Garis depan rapi dan terstruktur.", "B")
    if index == 3:
        return overlay_scene(photo_panel(panels[2], zoom), "Relaxed frame",
                             "Drape samping lebih santai.", "C")
    return recap(src, 1.0 + 0.012 * progress)


def exact_scenes(src, panels):
    names = [
        "scene-01-hook.png",
        "scene-02-soft-curve.png",
        "scene-03-clean-line.png",
        "scene-04-relaxed-frame.png",
        "scene-05-recap.png",
    ]
    paths = []
    for i, name in enumerate(names):
        im = scene_at(src, panels, i, 0.5)
        path = ASSETS / name
        im.save(path, compress_level=6)
        paths.append(path)
    return paths


def cover(src, panels):
    im = scene_at(src, panels, 0, 0.35)
    im.save(ASSETS / "reel-cover.png", compress_level=6)


def stories(src, panels):
    story1 = overlay_scene(photo_panel(panels[0], 1.01), "Satu wajah, tiga framing.",
                           "Semuanya opsi, bukan koreksi.")
    story2 = recap(src, 1.0)
    d2 = ImageDraw.Draw(story2, "RGBA")
    d2.rounded_rectangle((94, 1370, 986, 1640), radius=36, fill=(255,253,252,238), outline=ROSE, width=3)
    d2.text((540, 1452), "A — SOFT     atau     B — CLEAN?", font=font(31, True), fill=INK, anchor="mm")
    d2.text((540, 1553), "Tambahkan Poll native", font=font(25), fill=MUTED, anchor="mm")
    story3 = recap(src, 1.0)
    d3 = ImageDraw.Draw(story3, "RGBA")
    d3.rounded_rectangle((94, 1320, 986, 1665), radius=36, fill=(255,253,252,240), outline=ROSE, width=3)
    d3.text((540, 1400), "Kamu pilih A, B, atau C?", font=font(34, True), fill=INK, anchor="mm")
    d3.text((540, 1480), "Untuk daily, kantor, kampus, atau acara?", font=font(25), fill=MUTED, anchor="mm")
    d3.text((540, 1572), "Tambahkan Questions sticker native", font=font(23), fill=MUTED, anchor="mm")
    outputs = []
    for i, im in enumerate([story1, story2, story3], 1):
        path = ASSETS / f"story-{i:02d}.png"
        im.save(path, compress_level=6)
        outputs.append(path)
    return outputs


def contact_sheet(paths, out_name, thumb_w=270, thumb_h=480):
    sheet = Image.new("RGB", (thumb_w * len(paths), thumb_h), "#DCD2CA")
    for i, path in enumerate(paths):
        im = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(im, (i * thumb_w, 0))
    sheet.save(ASSETS / out_name, compress_level=6)


def render_video(src, panels):
    raw_cmd = [
        "ffmpeg", "-y", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        str(ASSETS / "reel-final.mp4")
    ]
    proc = subprocess.Popen(raw_cmd, stdin=subprocess.PIPE)
    try:
        for scene_i, count in enumerate(SCENE_FRAMES):
            for local in range(count):
                progress = local / max(1, count - 1)
                frame = scene_at(src, panels, scene_i, progress)
                proc.stdin.write(frame.tobytes())
    finally:
        if proc.stdin:
            proc.stdin.close()
    code = proc.wait()
    if code != 0:
        raise RuntimeError(f"FFmpeg failed with code {code}")


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    src = Image.open(SOURCE).convert("RGB")
    panels = split_panels(src)
    scenes = exact_scenes(src, panels)
    cover(src, panels)
    story_paths = stories(src, panels)
    contact_sheet(scenes, "contact-sheet.png")
    contact_sheet(story_paths, "stories-contact-sheet.png")
    render_video(src, panels)


if __name__ == "__main__":
    main()
