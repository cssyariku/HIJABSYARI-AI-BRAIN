"""Day 3 photoreal photo-based Reel, reproducible deterministic scene layout.
Requires Pillow and ffmpeg. The five source photos are AI editorial visuals.
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
import subprocess, json

ROOT=Path(__file__).resolve().parents[1]; A=ROOT/'assets'; A.mkdir(exist_ok=True)
W,H=1080,1920
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
COLORS=['cream','taupe','mocha','dusty-rose','burgundy']
LABELS=['CREAM','TAUPE','MOCHA','DUSTY ROSE','BURGUNDY']
MOODS=['terang & lembut','netral yang tenang','hangat & dalam','sentuhan warna','kontras lebih tegas']

def ff(*args):
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y',*map(str,args)],check=True)
def font(n,bold=False):return ImageFont.truetype(BOLD if bold else FONT,n)
def txt(d,xy,s,size,color='#292824',bold=False):d.text(xy,s,font=font(size,bold),fill=color,stroke_width=0)
def base(name):
 im=Image.open(A/f'photo-{name}.jpg').convert('RGB')
 # Center crop preserves the face, body, and photographed background.
 return ImageOps.fit(im,(W,H),method=Image.Resampling.LANCZOS,centering=(.5,.5))
def line(d,y):d.line((78,y,W-78,y),fill='#bcb2a6',width=2)
def save(im,name):im.save(A/name,quality=92,optimize=True)
def header(d):
 txt(d,(80,70),'HIJAB SYARI INDONESIA',27,'#3b3934',True)
 line(d,119)
def footer(d):
 line(d,1810);txt(d,(80,1830),'@hijabsyaricoid',29,'#3b3934',True)
def card(name,num):
 im=base(name);d=ImageDraw.Draw(im,'RGBA')
 # Only transparent color behind words; photographic image remains the focus.
 d.rounded_rectangle((52,140,1028,412),radius=24,fill=(246,243,237,235))
 txt(d,(88,169),f'{num:02d}  {LABELS[num-1]}',68,'#262523',True)
 txt(d,(90,274),MOODS[num-1],43,'#5e5953')
 d.rounded_rectangle((58,1690,1022,1802),radius=22,fill=(246,243,237,232))
 txt(d,(91,1714),'Outfit hitam yang sama. Hijabnya berganti.',31,'#33302c')
 save(im,f'scene-{num:02d}-{name}.jpg')

intro=base('cream');di=ImageDraw.Draw(intro,'RGBA')
di.rounded_rectangle((50,134,1030,450),radius=24,fill=(247,243,238,240))
txt(di,(82,168),'OUTFIT HITAM',54,'#38342e',True)
txt(di,(82,246),'5 warna hijab,',72,'#22211f',True)
txt(di,(82,336),'5 nuansa berbeda.',60,'#22211f',True)
di.rounded_rectangle((56,1650,1024,1790),radius=18,fill=(247,243,238,233))
txt(di,(88,1683),'Lihat perbedaannya →',46,'#38342e',True)
save(intro,'scene-00-intro.jpg')
for i,name in enumerate(COLORS,1):card(name,i)

recap=Image.new('RGB',(W,H),'#f4f0e9');dr=ImageDraw.Draw(recap)
txt(dr,(75,145),'OUTFIT HITAM,',70,'#262523',True)
txt(dr,(75,245),'LIMA NUANSA.',66,'#262523',True)
for i,name in enumerate(COLORS):
 p=base(name).crop((115,330,965,1330)).resize((280,330))
 x=76+(i%3)*313;y=455+(i//3)*464
 recap.paste(p,(x,y));txt(dr,(x,y+341),LABELS[i],26,'#393630',True)
txt(dr,(76,1650),'Mana yang paling kamu suka?',41,'#38342e',True)
save(recap,'scene-06-recap.jpg')

end=base('burgundy');de=ImageDraw.Draw(end,'RGBA')
de.rounded_rectangle((52,148,1028,545),radius=24,fill=(247,243,238,241))
txt(de,(85,180),'Coba dengan',70,'#262523',True)
txt(de,(85,265),'outfit yang sama',68,'#262523',True)
txt(de,(85,380),'& cahaya yang serupa.',45,'#5c5650')
de.rounded_rectangle((54,1610,1026,1790),radius=20,fill=(247,243,238,239))
txt(de,(86,1640),'Simpan untuk referensi.',47,'#262523',True)
txt(de,(86,1712),'@hijabsyaricoid',34,'#56504a')
save(end,'scene-07-cta.jpg')

cover=base('burgundy');dc=ImageDraw.Draw(cover,'RGBA')
dc.rounded_rectangle((47,58,1033,474),radius=26,fill=(247,243,238,243))
txt(dc,(83,86),'5 WARNA HIJAB',74,'#282622',True)
txt(dc,(83,178),'UNTUK OUTFIT',67,'#282622',True)
txt(dc,(83,269),'HITAM',90,'#282622',True)
txt(dc,(83,388),'Satu outfit, lima nuansa.',36,'#625b54')
dc.rounded_rectangle((61,1705,1019,1802),radius=18,fill=(247,243,238,226))
txt(dc,(90,1727),'@hijabsyaricoid',34,'#34312d',True)
cover.save(A/'cover_day3.png',optimize=True)

order=['scene-00-intro.jpg']+[f'scene-{i:02d}-{c}.jpg' for i,c in enumerate(COLORS,1)]+['scene-06-recap.jpg','scene-07-cta.jpg']
durations=[2.0]+[2.0]*5+[2.0,2.0]
segments=[]
for i,(file,duration) in enumerate(zip(order,durations)):
 seg=A/f'_segment-{i:02d}.mp4';segments.append(seg)
 # A restrained 2% push-in supplies motion without deforming face or fabric.
 ff('-loop','1','-framerate','30','-i',A/file,'-vf',"zoompan=z='min(zoom+0.00033,1.02)':d=1:s=1080x1920:fps=30,format=yuv420p",'-t',str(duration),'-an','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p',seg)
lst=A/'_segments.txt';lst.write_text(''.join(f"file '{p.name}'\n" for p in segments))
ff('-f','concat','-safe','0','-i',lst,'-c','copy','-movflags','+faststart',A/'reel_day3.mp4')
for p in segments+[lst]:p.unlink()

def story(name,title,sub,file):
 im=base(name);d=ImageDraw.Draw(im,'RGBA')
 d.rounded_rectangle((55,158,1025,490),radius=25,fill=(247,243,238,239))
 for j,s in enumerate(title.split('\n')):txt(d,(84,187+j*76),s,61,'#292722',True)
 txt(d,(85,403),sub,32,'#645c55')
 d.rounded_rectangle((60,1320,1020,1600),radius=20,fill=(247,243,238,225))
 txt(d,(86,1742),'@hijabsyaricoid',29,'#272522',True)
 im.save(A/file,optimize=True)
story('cream','Outfit hitam,\nhijab warna apa?','Cream atau burgundy?', 'story-01-poll.png')
story('taupe','Lima warna,\nsatu outfit.','Lihat Reel terbaru di feed.', 'story-02-recap.png')
story('dusty-rose','Selanjutnya,\nbahas warna apa?','Jawab lewat Questions sticker.', 'story-03-question.png')

from PIL import ImageDraw
thumb=Image.new('RGB',(1200,1800),'#ddd8d0');dt=ImageDraw.Draw(thumb)
for i,file in enumerate(order):
 im=Image.open(A/file);im.thumbnail((270,735));x=(i%4)*300+15;y=(i//4)*880+42
 thumb.paste(im,(x,y));txt(dt,(x,y-35),file,18)
thumb.save(A/'contact-sheet.jpg',quality=85,optimize=True)
print(json.dumps({'duration_target':sum(durations),'scenes':order,'cover':str(A/'cover_day3.png'),'reel':str(A/'reel_day3.mp4')}))
