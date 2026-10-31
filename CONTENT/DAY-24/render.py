from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import subprocess

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "pashmina-shift-three-checks.png"
W, H, FPS = 1080, 1920, 30
SCENE_FRAMES = [72, 81, 81, 81, 72, 63]

CREAM = "#F7F0E8"
INK = "#302824"
MUTED = "#70625B"
ROSE = "#A55E69"
TAUPE = "#88756C"
BROWN = "#65483A"
WHITE = "#FFFDFC"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)


def fit(img, size, centering=(0.5, 0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=centering)


def panels(src):
    w = src.width / 3
    out = []
    for i in range(3):
        left = round(i * w) + (5 if i else 0)
        right = round((i + 1) * w) - (5 if i < 2 else 0)
        out.append(src.crop((left, 0, right, src.height)))
    return out


def wrap(draw, value, box, fnt, fill=INK, spacing=10):
    x0, y0, x1, _ = box
    rows, row = [], ""
    for word in value.split():
        trial = (row + " " + word).strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= x1 - x0:
            row = trial
        else:
            if row:
                rows.append(row)
            row = word
    if row:
        rows.append(row)
    y = y0
    for row in rows:
        draw.text((x0, y), row, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), row, font=fnt)[3] + spacing
    return y


def brand(draw):
    draw.ellipse((72, 1812, 90, 1830), fill=ROSE)
    draw.text((104, 1804), "HIJAB SYARI INDONESIA", font=font(22, True), fill=MUTED)


def photo(panel, zoom=1.0, center=(0.5, 0.43)):
    base = fit(panel, (W, H), center)
    if zoom <= 1:
        return base
    nw, nh = int(W * zoom), int(H * zoom)
    z = base.resize((nw, nh), Image.Resampling.LANCZOS)
    return z.crop(((nw-W)//2, int((nh-H)*center[1]), (nw-W)//2+W, int((nh-H)*center[1])+H))


def card(image, title, subtitle, badge=None):
    base = image.copy()
    d = ImageDraw.Draw(base, "RGBA")
    d.rounded_rectangle((54, 104, 1026, 610), radius=46, fill=(247, 240, 232, 244))
    y = 168
    if badge:
        d.rounded_rectangle((94, 152, 345, 218), radius=30, fill=ROSE)
        d.text((220, 185), badge, font=font(24, True), fill=WHITE, anchor="mm")
        y = 272
    y = wrap(d, title, (94, y, 976, 455), font(59, True), INK, 10)
    wrap(d, subtitle, (94, min(y + 24, 490), 976, 570), font(30), MUTED, 8)
    brand(d)
    return base


def triptych(src, title, subtitle, zoom=1.0):
    image = fit(src, (W, H), (0.5, 0.46))
    if zoom > 1:
        nw, nh = int(W*zoom), int(H*zoom)
        image = image.resize((nw, nh), Image.Resampling.LANCZOS)
        image = image.crop(((nw-W)//2, (nh-H)//2, (nw-W)//2+W, (nh-H)//2+H))
    d = ImageDraw.Draw(image, "RGBA")
    d.rounded_rectangle((54, 106, 1026, 590), radius=46, fill=(247, 240, 232, 244))
    y = wrap(d, title, (94, 185, 976, 390), font(59, True), INK, 10)
    wrap(d, subtitle, (94, y + 30, 976, 520), font(31), MUTED, 8)
    brand(d)
    return image


def scene_at(src, p, index, progress):
    zoom = 1.0 + 0.025 * max(0.0, min(1.0, progress))
    if index == 0:
        return card(photo(p[0], zoom), "Pashmina gampang bergeser?", "Cek 3 titik ini dulu.")
    if index == 1:
        return card(photo(p[0], zoom), "Pasangan permukaan",
                    "Kain + inner yang licin bisa lebih mudah berpindah.", "1")
    if index == 2:
        return card(photo(p[1], zoom), "Titik anchor",
                    "Stabil, nyaman, tidak terlalu tegang.", "2")
    if index == 3:
        return card(photo(p[2], zoom, (0.5, 0.46)), "Panjang & drape",
                    "Beban yang timpang bisa menarik satu sisi.", "3")
    if index == 4:
        return triptych(src, "Tes 30 detik", "Noleh · angkat tangan · jalan.", 1.0 + 0.012*progress)
    return triptych(src, "Ubah satu hal dulu.", "Simpan checklist-nya.", 1.0 + 0.008*progress)


def save_static(src, p):
    names = [
        "scene-01-hook.png", "scene-02-surface.png", "scene-03-anchor.png",
        "scene-04-balance.png", "scene-05-test.png", "scene-06-cta.png"
    ]
    paths = []
    for i, name in enumerate(names):
        im = scene_at(src, p, i, 0.5)
        path = ASSETS / name
        im.save(path, compress_level=6)
        paths.append(path)
    scene_at(src, p, 0, 0.35).save(ASSETS / "reel-cover.png", compress_level=6)
    return paths


def stories(src, p):
    s1 = triptych(src, "Pashmina bergeser?", "Cek permukaan, anchor, dan drape.")
    s2 = card(photo(p[0], 1.01), "Paling sering bergeser di mana?",
              "Pilih di Poll ↓")
    d2 = ImageDraw.Draw(s2, "RGBA")
    d2.rounded_rectangle((94, 1370, 986, 1640), radius=36, fill=(255,253,252,240), outline=ROSE, width=3)
    d2.text((540, 1455), "CROWN / DEPAN", font=font(31, True), fill=INK, anchor="mm")
    d2.text((540, 1552), "BAHU / TAIL", font=font(31, True), fill=INK, anchor="mm")
    s3 = card(photo(p[2], 1.01, (0.5, 0.46)), "Bantu diagnosisnya lebih spesifik.",
              "Jawab di sticker ↓")
    d3 = ImageDraw.Draw(s3, "RGBA")
    d3.rounded_rectangle((94, 1350, 986, 1655), radius=36, fill=(255,253,252,240), outline=ROSE, width=3)
    d3.text((540, 1450), "Bahan + kapan mulai bergeser", font=font(31, True), fill=INK, anchor="mm")
    d3.text((540, 1553), "Tambahkan konteks aktivitasmu", font=font(25), fill=MUTED, anchor="mm")
    out=[]
    for i, im in enumerate([s1,s2,s3],1):
        path=ASSETS/f"story-{i:02d}.png"; im.save(path,compress_level=6); out.append(path)
    return out


def contact_sheet(paths, name, thumb=(270,480)):
    sheet=Image.new("RGB",(thumb[0]*len(paths),thumb[1]),"#DCD2CA")
    for i,path in enumerate(paths):
        im=Image.open(path).convert("RGB").resize(thumb,Image.Resampling.LANCZOS)
        sheet.paste(im,(i*thumb[0],0))
    sheet.save(ASSETS/name,compress_level=6)


def render_video(src, p):
    cmd=["ffmpeg","-y","-f","rawvideo","-vcodec","rawvideo","-pix_fmt","rgb24",
         "-s",f"{W}x{H}","-r",str(FPS),"-i","-","-an","-c:v","libx264",
         "-preset","medium","-crf","18","-pix_fmt","yuv420p","-movflags","+faststart",
         str(ASSETS/"reel-final.mp4")]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for si,count in enumerate(SCENE_FRAMES):
            for local in range(count):
                frame=scene_at(src,p,si,local/max(1,count-1))
                proc.stdin.write(frame.tobytes())
    finally:
        if proc.stdin: proc.stdin.close()
    code=proc.wait()
    if code: raise RuntimeError(f"FFmpeg failed: {code}")


def main():
    ASSETS.mkdir(parents=True,exist_ok=True)
    src=Image.open(SOURCE).convert("RGB")
    p=panels(src)
    scenes=save_static(src,p)
    story_paths=stories(src,p)
    contact_sheet(scenes,"contact-sheet.png")
    contact_sheet(story_paths,"stories-contact-sheet.png")
    render_video(src,p)


if __name__=="__main__":
    main()
