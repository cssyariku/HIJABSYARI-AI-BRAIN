from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parent
ASSET = ROOT / "assets"
ASSET.mkdir(parents=True, exist_ok=True)
SRC = ASSET / "hijab-laundry-triptych.png"

W, H = 1080, 1350
SW, SH = 1080, 1920
CREAM = "#F7F0E7"
CREAM2 = "#EFE1D4"
ROSE = "#A85F69"
ROSE2 = "#D8A3A8"
TAUPE = "#7D6A5E"
INK = "#292522"
MUTED = "#716861"
WHITE = "#FFFDFC"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)

def rounded(draw, box, fill, radius=32, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def fit_crop(img, size, anchor=(0.5,0.5)):
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=anchor)

def panel(src, idx):
    pw = src.width // 3
    return src.crop((idx*pw, 0, (idx+1)*pw if idx<2 else src.width, src.height))

def lines(draw, text, box, fnt, fill, spacing=10, max_lines=None):
    x0,y0,x1,y1=box
    words=text.split()
    out=[]; cur=""
    for word in words:
        test=(cur+" "+word).strip()
        if draw.textbbox((0,0), test, font=fnt)[2] <= x1-x0:
            cur=test
        else:
            if cur: out.append(cur)
            cur=word
    if cur: out.append(cur)
    if max_lines: out=out[:max_lines]
    y=y0
    for ln in out:
        draw.text((x0,y),ln,font=fnt,fill=fill)
        y += draw.textbbox((0,0),ln,font=fnt)[3] + spacing
    return y

def logo(draw, y, color=INK):
    draw.ellipse((72,y,90,y+18), fill=ROSE)
    draw.text((104,y-6),"HIJAB SYARI INDONESIA",font=font(22,True),fill=color)

def footer(draw, n, h=H):
    draw.text((72,h-72),"@hijabsyaricoid",font=font(20,True),fill=MUTED)
    num=f"{n:02d} / 08"
    tw=draw.textbbox((0,0),num,font=font(20,True))[2]
    draw.text((W-72-tw,h-72),num,font=font(20,True),fill=MUTED)

def save(im, name):
    im.save(ASSET/name,"PNG",compress_level=6)

def photo_card(base, img, box, radius=36):
    crop=fit_crop(img,(box[2]-box[0],box[3]-box[1]))
    mask=Image.new("L",crop.size,0); md=ImageDraw.Draw(mask)
    md.rounded_rectangle((0,0,crop.width,crop.height),radius=radius,fill=255)
    base.paste(crop,(box[0],box[1]),mask)

def make_cover(src):
    im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im)
    photo_card(im,panel(src,0),(0,0,W,760),0)
    overlay=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(overlay)
    od.rectangle((0,390,W,760),fill=(35,30,27,65)); im=Image.alpha_composite(im.convert("RGBA"),overlay).convert("RGB"); d=ImageDraw.Draw(im)
    rounded(d,(56,650,1024,1220),CREAM,44)
    d.text((96,704),"Hijab berubah",font=font(72,True),fill=INK)
    d.text((96,792),"setelah dicuci?",font=font(72,True),fill=INK)
    d.text((96,934),"Cek 5 kebiasaan ini.",font=font(45,True),fill=ROSE)
    d.line((96,1030,280,1030),fill=ROSE,width=8)
    d.text((96,1072),"Checklist praktis, tetap ikuti care label.",font=font(27),fill=MUTED)
    logo(d,1260); save(im,"carousel-01.png")

def make_text_slide(n,title,body,src_panel,accent=ROSE):
    im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im)
    photo_card(im,src_panel,(560,90,1008,560),34)
    d.ellipse((72,90,156,174),fill=accent)
    d.text((100,105),f"{n-2:02d}" if n>=3 else "i",font=font(36,True),fill=WHITE,anchor="mm")
    y=240 if n==2 else 220
    y=lines(d,title,(72,y,520,680),font(54,True),INK,12)
    d.line((72,y+20,310,y+20),fill=accent,width=8)
    rounded(d,(72,700,1008,1168),WHITE,34)
    lines(d,body,(116,754,958,1115),font(35),MUTED,17)
    footer(d,n); save(im,f"carousel-{n:02d}.png")

def make_dose(src):
    im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im)
    d.ellipse((72,90,156,174),fill=ROSE); d.text((114,132),"03",font=font(30,True),fill=WHITE,anchor="mm")
    lines(d,"Deterjen pakai feeling",(72,220,1008,460),font(60,True),INK,10)
    rounded(d,(72,560,1008,930),WHITE,34)
    d.rounded_rectangle((128,646,300,838),radius=28,outline=ROSE,width=8)
    d.line((165,704,263,704),fill=ROSE,width=6); d.line((165,750,246,750),fill=ROSE2,width=6)
    d.text((352,632),"Ikuti takaran pada",font=font(38,True),fill=INK)
    d.text((352,688),"label produk.",font=font(38,True),fill=INK)
    d.text((352,785),"Lebih banyak tidak selalu",font=font(31),fill=MUTED)
    d.text((352,833),"berarti lebih bersih.",font=font(31),fill=MUTED)
    photo_card(im,panel(src,1),(72,990,1008,1168),28)
    footer(d,5); save(im,"carousel-05.png")

def make_summary(src):
    im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im)
    logo(d,72)
    d.text((72,154),"Checklist sebelum mulai",font=font(58,True),fill=INK)
    steps=[("1","Baca label"),("2","Pisahkan"),("3","Ukur deterjen"),("4","Beri ruang"),("5","Keringkan sesuai petunjuk")]
    y=280
    for num,txt in steps:
        d.ellipse((76,y,132,y+56),fill=ROSE)
        d.text((104,y+28),num,font=font(25,True),fill=WHITE,anchor="mm")
        d.text((160,y+4),txt,font=font(34,True),fill=INK)
        if num!="5": d.line((104,y+62,104,y+94),fill=ROSE2,width=5)
        y+=112
    photo_card(im,src,(72,866,1008,1115),28)
    d.text((72,1160),"Simpan untuk cucian berikutnya.",font=font(34,True),fill=ROSE)
    footer(d,8); save(im,"carousel-08.png")

def make_story(idx,title,body,img,question=False):
    im=Image.new("RGB",(SW,SH),CREAM); d=ImageDraw.Draw(im)
    photo_card(im,img,(0,0,SW,960),0)
    rounded(d,(54,830,1026,1790),CREAM,46)
    d.text((92,900),title,font=font(57,True),fill=INK)
    lines(d,body,(92,1010,976,1480),font(38),MUTED,18)
    if idx==1:
        rounded(d,(92,1360,988,1490),WHITE,28,ROSE2,3); d.text((132,1396),"Takaran deterjen",font=font(31,True),fill=INK)
        rounded(d,(92,1520,988,1650),WHITE,28,ROSE2,3); d.text((132,1556),"Suhu & siklus",font=font(31,True),fill=INK)
        d.text((92,1690),"Tambahkan Poll native saat unggah",font=font(22),fill=MUTED)
    elif question:
        rounded(d,(92,1370,988,1620),WHITE,30,ROSE2,3)
        d.text((132,1415),"Tambahkan jawabanmu…",font=font(29),fill="#9A9088")
        d.text((92,1660),"Tambahkan Questions sticker native",font=font(22),fill=MUTED)
    else:
        d.text((92,1530),"Simpan checklist ini.",font=font(38,True),fill=ROSE)
    logo(d,1810); save(im,f"story-{idx:02d}.png")

def contacts():
    thumbs=[]
    for i in range(1,9):
        im=Image.open(ASSET/f"carousel-{i:02d}.png").convert("RGB")
        thumbs.append(im.resize((270,338),Image.Resampling.LANCZOS))
    sheet=Image.new("RGB",(1080,676),"#DDD4CC")
    for i,t in enumerate(thumbs): sheet.paste(t,((i%4)*270,(i//4)*338))
    save(sheet,"contact-sheet.png")
    st=[]
    for i in range(1,4): st.append(Image.open(ASSET/f"story-{i:02d}.png").convert("RGB").resize((270,480),Image.Resampling.LANCZOS))
    ss=Image.new("RGB",(810,480),"#DDD4CC")
    for i,t in enumerate(st): ss.paste(t,(i*270,0))
    ss.save(ASSET/"stories-contact-sheet.png","PNG",compress_level=6)

def main():
    src=Image.open(SRC).convert("RGB")
    make_cover(src)
    make_text_slide(2,"Satu cara tidak cocok untuk semua hijab.","Mulai dari label: cara cuci, suhu, pengeringan, dan setrika bisa berbeda.",panel(src,0),TAUPE)
    make_text_slide(3,"Langsung campur semua", "Pisahkan warna baru, gelap, atau terang pada pencucian awal. Lindungi kain halus dari ritsleting dan kait.",panel(src,1))
    make_text_slide(4,"Mesin terlalu penuh", "Kain perlu ruang untuk bergerak. Muatan terlalu padat dapat membuat pencucian kurang efektif dan menambah gesekan.",panel(src,1),TAUPE)
    make_dose(src)
    make_text_slide(6,"Suhu dan siklus asal pilih", "Gunakan cara cuci dan suhu yang diizinkan label. Pilih perlakuan lebih lembut bila bahan memang membutuhkannya.",panel(src,0),TAUPE)
    make_text_slide(7,"Semua kain diperlakukan keras", "Pada kain yang rentan, gosokan atau puntiran kuat bisa menambah kerutan atau abrasi. Bentuk ulang dan keringkan sesuai label.",panel(src,2))
    make_summary(src)
    make_story(1,"Saat cuci hijab,","yang paling bikin ragu?",panel(src,0))
    make_story(2,"Checklist 5 langkah","Label → pisahkan → ukur deterjen → beri ruang → keringkan sesuai petunjuk.",src)
    make_story(3,"Bahan hijab apa", "yang paling sering terasa berubah setelah dicuci? Tambahkan bahan + apa yang berubah.",panel(src,2),True)
    contacts()

if __name__ == "__main__":
    main()
