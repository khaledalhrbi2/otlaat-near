"""يولّد صور OG (1200x630) لكل مدينة + صورة افتراضية. يعمل قبل البناء."""
import json, os
from PIL import Image, ImageDraw, ImageFont
H=os.path.dirname(__file__); B=os.path.join(H,'IBMPlexSansArabic-Bold.ttf'); R=os.path.join(H,'IBMPlexSansArabic-Regular.ttf')
NAVY=(31,39,82); ORANGE=(245,136,36); WHITE=(255,255,255); SOFT=(201,209,230)
def ar(t): return t
def make(path, title, sub, count=None):
    im=Image.new('RGB',(1200,630),NAVY); d=ImageDraw.Draw(im)
    d.rectangle([0,0,1200,14],fill=ORANGE)
    d.text((1120,70),ar('عطلات'),font=ImageFont.truetype(B,54),fill=WHITE,anchor='ra',direction='rtl',language='ar')
    d.text((1120,140),ar('فنادق قريبة من'),font=ImageFont.truetype(R,30),fill=ORANGE,anchor='ra',direction='rtl',language='ar')
    f=ImageFont.truetype(B,78 if len(title)<22 else 62); d.text((1120,300),ar(title),font=f,fill=WHITE,anchor='rm',direction='rtl',language='ar')
    d.text((1120,400),ar(sub),font=ImageFont.truetype(R,34),fill=SOFT,anchor='rm',direction='rtl',language='ar')
    if count: 
        d.rounded_rectangle([80,500,400,570],radius=35,fill=ORANGE)
        d.text((240,535),ar(f'{count} معلماً ومنطقة'),font=ImageFont.truetype(B,28),fill=NAVY,anchor='mm',direction='rtl',language='ar')
    d.text((1120,545),ar('أسعار شاملة الضرائب · إلغاء مجاني · تقسيط تابي وتمارا'),font=ImageFont.truetype(R,26),fill=SOFT,anchor='rm',direction='rtl',language='ar')
    im.save(path,'JPEG',quality=72,optimize=True)
out=os.path.join(H,'..','public','og'); os.makedirs(out,exist_ok=True)
cities=json.load(open(os.path.join(H,'..','data','cities.json'),encoding='utf-8'))
make(os.path.join(out,'default.jpg'),'فندقك على بُعد دقائق من المكان الذي جئت لأجله','16 مدينة · ابدأ من المعلم أو الحدث وشاهد الفنادق القريبة منه',333)
for c in cities:
    make(os.path.join(out,f"{c['slug']}.jpg"),f"فنادق {c['name_ar']} حسب المعلم",f"{c['country']} · فنادق قريبة من المعالم والأحياء والمطارات",c['poi_count'])
import sys
if '--pois' in sys.argv:
    n=0
    for c in cities:
        city=json.load(open(os.path.join(H,'..','data',f"{c['slug']}.json"),encoding='utf-8'))
        for p in city['pois']:
            f=os.path.join(out,f"{c['slug']}-{p['slug']}.jpg")
            if os.path.exists(f): continue
            lab={'district':'فنادق في','event':'','intent_hub':''}.get(p['type'],'فنادق قريبة من')
            make(f,f"{lab} {p['name_ar']}".strip(),f"{c['name_ar']} · ضمن {p['prox_km']} كم · أسعار شاملة الضرائب"); n+=1
    print('poi og',n)
print('ok',len(cities)+1)
