import json, math, os
H=os.path.join(os.path.dirname(__file__),'..','data')
def P(slug, ar, en, lat, lng, prox, q, poi, typ, intents=None, metro=None, kw=None, event=None):
    d=dict(slug=slug,name_ar=ar,name_en=en,lat=lat,lng=lng,prox_km=prox,q=q,poi_label=poi,type=typ,intents=intents or ["family","apartments","5-star"],nearest_metro=metro,keywords=kw or [])
    if event: d["event"]=event
    return d
S=["family","shopping","apartments"]; B=["budget","family","apartments"]; M=["family","medical","apartments"]
NEW=[
dict(slug="jeddah",code=None,name_ar="جدة",name_en="Jeddah",country="السعودية",lat=21.5433,lng=39.1728,default_prox=15,date_profile="weekend_thu_sat",default_nights=2,pois=[
 P("corniche","كورنيش جدة","Jeddah Corniche",21.5800,39.1050,4,"كورنيش جدة","الكورنيش","landmark",["family","5-star","beach"],kw=["فنادق كورنيش جدة","فنادق مطلة على البحر جدة"]),
 P("red-sea-mall","رد سي مول","Red Sea Mall",21.6210,39.1200,3,"رد سي مول","رد سي مول","landmark",S),
 P("the-venue","ذا فينيو","The Venue",21.6350,39.1060,3,"ذا فينيو","ذا فينيو","landmark",["family","5-star"]),
 P("al-balad","البلد التاريخية","Al Balad",21.4850,39.1870,2,"البلد جدة","البلد","landmark",["budget","family"]),
 P("mall-of-arabia","مول العرب","Mall of Arabia",21.6160,39.1670,3,"مول العرب","مول العرب","landmark",S),
 P("jeddah-airport","مطار الملك عبدالعزيز","KAIA",21.6700,39.1560,6,"مطار جدة","المطار","airport",["transit","budget"]),
 P("haramain-jeddah","محطة قطار الحرمين","Haramain Station Jeddah",21.5630,39.2170,3,"محطة قطار الحرمين جدة","محطة القطار","transport",["transit","family"]),
 P("al-hamra","الحمراء","Al Hamra",21.5200,39.1500,3,"الحمراء جدة","الحمراء","district",["5-star","family"]),
 P("al-rawdah","الروضة","Al Rawdah",21.5600,39.1600,3,"الروضة جدة","الروضة","district",B),
 P("al-shati","الشاطئ","Al Shati",21.6050,39.1050,3,"الشاطئ جدة","الشاطئ","district",["family","5-star","beach"]),
 P("obhur","أبحر","Obhur",21.7200,39.1000,5,"ابحر","أبحر","district",["family","beach","villa"]),
 P("al-salamah","السلامة","Al Salamah",21.5950,39.1450,3,"السلامة جدة","السلامة","district",B),
 P("king-abdullah-sports-city","الجوهرة","King Abdullah Sports City",21.7630,39.1130,6,"ملعب الجوهرة","الجوهرة","stadium",["budget","family"]),
 P("jeddah-corniche-circuit","حلبة الكورنيش","Jeddah Corniche Circuit",21.6320,39.1050,5,"حلبة جدة","حلبة الكورنيش","stadium",["5-star","family"]),
 P("kfsh-jeddah","مستشفى الملك فيصل التخصصي جدة","KFSH Jeddah",21.6100,39.1640,3,"مستشفى التخصصي جدة","التخصصي","hospital",M),
 P("jeddah-season","موسم جدة","Jeddah Season",21.6050,39.1050,8,"موسم جدة","موسم جدة","event",kw=["فنادق موسم جدة"],event=dict(start="2027-05-20",end="2027-07-31",note="تقريبي")),
 P("formula-1-jeddah","فورمولا 1 جدة","Jeddah F1",21.6320,39.1050,6,"حلبة جدة","فورمولا 1","event",["5-star","family"],kw=["فنادق فورمولا 1 جدة"],event=dict(start="2027-04-16",end="2027-04-19",note="تقريبي")),
]),
dict(slug="abu-dhabi",code=None,name_ar="أبوظبي",name_en="Abu Dhabi",country="الإمارات",lat=24.4539,lng=54.3773,default_prox=15,date_profile="next_weekend",default_nights=3,pois=[
 P("yas-island","جزيرة ياس","Yas Island",24.4880,54.6030,5,"جزيرة ياس","ياس","district",["family","5-star"],kw=["فنادق جزيرة ياس","فنادق ياس للعوائل"]),
 P("ferrari-world","فيراري وورلد","Ferrari World",24.4840,54.6070,4,"فيراري وورلد","فيراري وورلد","landmark",["family"]),
 P("yas-waterworld","ياس ووتر وورلد","Yas Waterworld",24.4870,54.5970,4,"ياس ووتر وورلد","ياس ووتر وورلد","landmark",["family"]),
 P("warner-bros-world","وارنر براذرز","Warner Bros World",24.4890,54.6100,4,"وارنر براذرز ابوظبي","وارنر براذرز","landmark",["family"]),
 P("yas-mall","ياس مول","Yas Mall",24.4890,54.6080,3,"ياس مول","ياس مول","landmark",S),
 P("corniche-abu-dhabi","كورنيش أبوظبي","Abu Dhabi Corniche",24.4780,54.3400,3,"كورنيش ابوظبي","الكورنيش","landmark",["5-star","family","beach"]),
 P("sheikh-zayed-mosque","جامع الشيخ زايد","Sheikh Zayed Grand Mosque",24.4128,54.4750,4,"جامع الشيخ زايد","جامع الشيخ زايد","landmark"),
 P("louvre-abu-dhabi","اللوفر أبوظبي","Louvre Abu Dhabi",24.5338,54.3983,3,"اللوفر ابوظبي","اللوفر","landmark",["5-star","couples"]),
 P("saadiyat-island","جزيرة السعديات","Saadiyat Island",24.5450,54.4350,5,"السعديات","السعديات","district",["5-star","beach","couples"]),
 P("al-reem-island","جزيرة الريم","Al Reem Island",24.4980,54.4050,3,"جزيرة الريم","الريم","district",["apartments","family"]),
 P("marina-mall","مارينا مول","Marina Mall",24.4760,54.3220,3,"مارينا مول ابوظبي","مارينا مول","landmark",S),
 P("abu-dhabi-mall","أبوظبي مول","Abu Dhabi Mall",24.4960,54.3840,2,"ابوظبي مول","أبوظبي مول","landmark",S),
 P("auh-airport","مطار زايد الدولي","Zayed International Airport",24.4330,54.6510,6,"مطار ابوظبي","المطار","airport",["transit","budget"]),
 P("al-khalidiyah-ad","الخالدية","Al Khalidiyah",24.4700,54.3450,2,"الخالدية ابوظبي","الخالدية","district",B),
 P("cleveland-clinic","كليفلاند كلينك","Cleveland Clinic Abu Dhabi",24.5010,54.3900,3,"كليفلاند كلينك ابوظبي","كليفلاند كلينك","hospital",M),
 P("etihad-arena","اتحاد أرينا","Etihad Arena",24.4750,54.6020,4,"اتحاد ارينا","اتحاد أرينا","stadium",["family","5-star"]),
 P("formula-1-abu-dhabi","فورمولا 1 أبوظبي","Abu Dhabi Grand Prix",24.4670,54.6030,6,"حلبة ياس مارينا","فورمولا 1","event",["5-star","family"],event=dict(start="2026-12-03",end="2026-12-06",note="تقريبي")),
]),
dict(slug="dammam-khobar",code=None,name_ar="الدمام والخبر",name_en="Dammam & Khobar",country="السعودية",lat=26.2800,lng=50.2000,default_prox=20,date_profile="weekend_thu_sat",default_nights=2,pois=[
 P("khobar-corniche","كورنيش الخبر","Khobar Corniche",26.2900,50.2200,3,"كورنيش الخبر","كورنيش الخبر","landmark",["family","5-star","beach"]),
 P("dhahran-mall","الظهران مول","Dhahran Mall",26.2810,50.1890,3,"الظهران مول","الظهران مول","landmark",S),
 P("al-rashid-mall-khobar","الراشد مول الخبر","Al Rashid Mall",26.3050,50.2020,3,"الراشد مول الخبر","الراشد مول","landmark",S),
 P("king-fahd-causeway","جسر الملك فهد","King Fahd Causeway",26.2080,50.2050,5,"جسر الملك فهد","الجسر","transport",["transit","family"]),
 P("dammam-airport","مطار الملك فهد","King Fahd Airport",26.4710,49.7980,10,"مطار الدمام","المطار","airport",["transit"]),
 P("half-moon-bay","الخليج نصف القمر","Half Moon Bay",26.0850,50.0400,6,"نصف القمر","نصف القمر","landmark",["family","beach","villa"]),
 P("dammam-corniche","كورنيش الدمام","Dammam Corniche",26.4400,50.1100,3,"كورنيش الدمام","كورنيش الدمام","landmark",["family","budget"]),
 P("aramco-dhahran","أرامكو الظهران","Aramco Dhahran",26.2950,50.1370,4,"ارامكو الظهران","أرامكو","landmark",["corporate","apartments"]),
 P("al-olaya-khobar","العليا الخبر","Al Olaya Khobar",26.2870,50.2000,2,"العليا الخبر","العليا","district",B),
 P("kfupm","جامعة الملك فهد للبترول","KFUPM",26.3070,50.1450,3,"جامعة الملك فهد للبترول","جامعة البترول","landmark",["budget","apartments"]),
]),
dict(slug="manama",code=None,name_ar="المنامة",name_en="Manama",country="البحرين",lat=26.2285,lng=50.5860,default_prox=12,date_profile="weekend_thu_sat",default_nights=2,pois=[
 P("seef","السيف","Seef",26.2330,50.5400,3,"السيف","السيف","district",["family","shopping","apartments"],kw=["فنادق السيف البحرين","فنادق قريبة من سيتي سنتر البحرين"]),
 P("city-centre-bahrain","سيتي سنتر البحرين","City Centre Bahrain",26.2330,50.5480,2,"سيتي سنتر البحرين","سيتي سنتر","landmark",S),
 P("juffair","الجفير","Juffair",26.2130,50.6050,3,"الجفير","الجفير","district",["apartments","budget","family"]),
 P("adliya","العدلية","Adliya",26.2140,50.5860,2,"العدلية","العدلية","district",["couples","budget"]),
 P("bahrain-bay","خليج البحرين","Bahrain Bay",26.2450,50.5850,2,"خليج البحرين","خليج البحرين","district",["5-star","corporate"]),
 P("amwaj-islands","جزر أمواج","Amwaj Islands",26.2880,50.6650,5,"امواج","أمواج","district",["family","beach","villa"]),
 P("bahrain-airport","مطار البحرين","Bahrain Airport",26.2700,50.6330,5,"مطار البحرين","المطار","airport",["transit"]),
 P("bahrain-circuit","حلبة البحرين","Bahrain International Circuit",26.0325,50.5106,10,"حلبة البحرين","حلبة البحرين","stadium",["5-star","family"]),
 P("manama-souq","سوق المنامة","Manama Souq",26.2290,50.5780,2,"سوق المنامة","سوق المنامة","landmark",B),
 P("formula-1-bahrain","فورمولا 1 البحرين","Bahrain Grand Prix",26.0325,50.5106,12,"حلبة البحرين","فورمولا 1","event",["5-star","family"],event=dict(start="2027-03-05",end="2027-03-07",note="تقريبي")),
]),
dict(slug="doha",code=None,name_ar="الدوحة",name_en="Doha",country="قطر",lat=25.2854,lng=51.5310,default_prox=12,date_profile="next_weekend",default_nights=3,pois=[
 P("the-pearl","اللؤلؤة","The Pearl",25.3690,51.5460,4,"اللؤلؤة قطر","اللؤلؤة","district",["5-star","family","apartments"]),
 P("west-bay","الخليج الغربي","West Bay",25.3220,51.5300,3,"الخليج الغربي","الخليج الغربي","district",["5-star","corporate"]),
 P("souq-waqif","سوق واقف","Souq Waqif",25.2876,51.5330,2,"سوق واقف","سوق واقف","landmark",["family","budget"]),
 P("doha-corniche","كورنيش الدوحة","Doha Corniche",25.3000,51.5300,3,"كورنيش الدوحة","الكورنيش","landmark",["5-star","family"]),
 P("lusail","لوسيل","Lusail",25.4280,51.4900,5,"لوسيل","لوسيل","district",["family","5-star","apartments"]),
 P("katara","كتارا","Katara",25.3590,51.5260,3,"كتارا","كتارا","landmark",["family","5-star"]),
 P("villaggio-mall","فيلاجيو مول","Villaggio Mall",25.2600,51.4420,3,"فيلاجيو","فيلاجيو","landmark",S),
 P("hamad-airport","مطار حمد الدولي","Hamad International",25.2730,51.6080,6,"مطار حمد","المطار","airport",["transit"]),
 P("msheireb","مشيرب","Msheireb",25.2850,51.5280,2,"مشيرب","مشيرب","district",["5-star","couples"]),
 P("lusail-stadium","استاد لوسيل","Lusail Stadium",25.4210,51.4900,5,"استاد لوسيل","استاد لوسيل","stadium",["family","budget"]),
 P("place-vendome-qatar","بلاس فاندوم","Place Vendome Qatar",25.4100,51.5000,3,"بلاس فاندوم قطر","بلاس فاندوم","landmark",S),
]),
dict(slug="cairo",code=None,name_ar="القاهرة",name_en="Cairo",country="مصر",lat=30.0444,lng=31.2357,default_prox=12,date_profile="next_weekend",default_nights=4,pois=[
 P("pyramids","الأهرامات","Giza Pyramids",29.9773,31.1325,4,"الاهرامات","الأهرامات","landmark",["5-star","family"],kw=["فنادق مطلة على الأهرامات"]),
 P("tahrir","ميدان التحرير","Tahrir Square",30.0444,31.2357,2,"ميدان التحرير","التحرير","landmark",["budget","family"]),
 P("zamalek","الزمالك","Zamalek",30.0620,31.2190,2,"الزمالك","الزمالك","district",["5-star","couples","apartments"]),
 P("nile-corniche","كورنيش النيل","Nile Corniche",30.0500,31.2300,3,"كورنيش النيل","النيل","landmark",["5-star","couples"],kw=["فنادق مطلة على النيل"]),
 P("new-cairo","القاهرة الجديدة","New Cairo",30.0300,31.4700,6,"القاهرة الجديدة","القاهرة الجديدة","district",["family","apartments"]),
 P("cairo-festival-city","كايرو فستيفال سيتي","Cairo Festival City",30.0290,31.4090,3,"كايرو فستيفال","فستيفال سيتي","landmark",S),
 P("mall-of-egypt","مول مصر","Mall of Egypt",29.9720,31.0170,4,"مول مصر","مول مصر","landmark",S),
 P("cairo-airport","مطار القاهرة","Cairo Airport",30.1219,31.4056,6,"مطار القاهرة","المطار","airport",["transit"]),
 P("heliopolis","مصر الجديدة","Heliopolis",30.0900,31.3300,3,"مصر الجديدة","مصر الجديدة","district",B),
 P("maadi","المعادي","Maadi",29.9600,31.2600,3,"المعادي","المعادي","district",["family","apartments"]),
 P("khan-el-khalili","خان الخليلي","Khan El Khalili",30.0477,31.2623,2,"خان الخليلي","خان الخليلي","landmark",B),
 P("grand-egyptian-museum","المتحف المصري الكبير","Grand Egyptian Museum",29.9940,31.1190,4,"المتحف المصري الكبير","المتحف الكبير","landmark",["family","5-star"]),
 P("sheikh-zayed-city","الشيخ زايد","Sheikh Zayed City",30.0400,30.9800,5,"الشيخ زايد","الشيخ زايد","district",["family","apartments"]),
]),
dict(slug="kuwait",code=None,name_ar="الكويت",name_en="Kuwait City",country="الكويت",lat=29.3759,lng=47.9774,default_prox=12,date_profile="weekend_thu_sat",default_nights=2,pois=[
 P("the-avenues","الأفنيوز","The Avenues",29.3030,47.9370,3,"الافنيوز","الأفنيوز","landmark",S,kw=["فنادق قريبة من الافنيوز"]),
 P("salmiya","السالمية","Salmiya",29.3330,48.0760,3,"السالمية","السالمية","district",["family","apartments","beach"]),
 P("kuwait-towers","أبراج الكويت","Kuwait Towers",29.3890,48.0020,3,"ابراج الكويت","أبراج الكويت","landmark",["5-star","family"]),
 P("marina-mall-kuwait","مارينا مول","Marina Mall Kuwait",29.3390,48.0720,2,"مارينا مول الكويت","مارينا مول","landmark",S),
 P("360-mall","360 مول","360 Mall",29.2700,47.9900,3,"360 مول","360 مول","landmark",S),
 P("kuwait-airport","مطار الكويت","Kuwait Airport",29.2267,47.9689,6,"مطار الكويت","المطار","airport",["transit"]),
 P("sharq","شرق","Sharq",29.3800,47.9900,2,"شرق الكويت","شرق","district",["5-star","corporate"]),
 P("hawally","حولي","Hawally",29.3330,48.0280,2,"حولي","حولي","district",B),
 P("mahboula","المهبولة","Mahboula",29.1400,48.1300,3,"المهبولة","المهبولة","district",["apartments","budget","beach"]),
 P("sabah-al-salem-hospital","مستشفى مبارك الكبير","Mubarak Al-Kabeer Hospital",29.3300,48.0200,3,"مستشفى مبارك الكبير","مبارك الكبير","hospital",M),
]),
]
# seasonal events for existing cities
EXTRA_EVENTS={
 "riyadh":[P("eid-al-fitr-2027","فنادق الرياض عيد الفطر 2027","Riyadh Eid Al Fitr",24.7694,46.6046,8,"الرياض","الرياض","event",["family"],event=dict(start="2027-03-09",end="2027-03-14",note="تقريبي")),
           P("midyear-break-2027","فنادق الرياض إجازة منتصف العام","Riyadh Midyear Break",24.7694,46.6046,8,"الرياض","الرياض","event",["family","budget"],event=dict(start="2026-11-19",end="2026-11-28",note="حسب تقويم التعليم")),
           P("dakar-rally-2027","رالي داكار 2027","Dakar Rally",24.7136,46.6753,15,"الرياض","الرياض","event",["5-star","corporate"],event=dict(start="2027-01-03",end="2027-01-17",note="تقريبي")),
           P("riyadh-book-fair","معرض الرياض للكتاب","Riyadh Book Fair",24.7750,46.7190,5,"مركز الرياض للمعارض","معرض الكتاب","event",["family","budget"],event=dict(start="2026-10-01",end="2026-10-10",note="تقريبي"))],
 "dubai":[P("eid-al-fitr-2027","فنادق دبي عيد الفطر 2027","Dubai Eid",25.1972,55.2744,10,"دبي","دبي","event",["family","5-star"],event=dict(start="2027-03-09",end="2027-03-14",note="تقريبي")),
          P("dubai-shopping-festival","مهرجان دبي للتسوق","Dubai Shopping Festival",25.1985,55.2796,8,"دبي","دبي","event",["family","shopping"],event=dict(start="2026-12-05",end="2027-01-11",note="تقريبي")),
          P("new-year-2027","فنادق دبي رأس السنة","Dubai New Year",25.1972,55.2744,4,"داون تاون دبي","برج خليفة","event",["5-star","couples"],kw=["فنادق دبي راس السنة مطلة على برج خليفة"],event=dict(start="2026-12-30",end="2027-01-02",note="")),
          P("midyear-break-2027","فنادق دبي إجازة منتصف العام","Dubai Midyear Break",25.1972,55.2744,10,"دبي","دبي","event",["family"],event=dict(start="2026-11-19",end="2026-11-28",note="تقويم التعليم السعودي"))],
 "istanbul":[P("summer-2027","فنادق إسطنبول الصيف 2027","Istanbul Summer",41.0370,28.9850,8,"اسطنبول","إسطنبول","event",["family","apartments"],event=dict(start="2027-06-15",end="2027-08-31",note="")),
             P("eid-al-adha-2027","فنادق إسطنبول عيد الأضحى 2027","Istanbul Eid Al Adha",41.0370,28.9850,8,"اسطنبول","إسطنبول","event",["family"],event=dict(start="2027-05-15",end="2027-05-22",note="تقريبي"))],
 "london":[P("summer-2027","فنادق لندن الصيف 2027","London Summer",51.5190,-0.1680,6,"لندن","لندن","event",["family","apartments"],event=dict(start="2027-06-20",end="2027-08-31",note=""))],
 "paris":[P("summer-2027","فنادق باريس الصيف 2027","Paris Summer",48.8698,2.3075,6,"باريس","باريس","event",["family"],event=dict(start="2027-06-20",end="2027-08-31",note=""))],
 "makkah":[P("eid-al-fitr-2027","فنادق مكة عيد الفطر 2027","Makkah Eid",21.4225,39.8262,2,"الحرم المكي","الحرم","event",["family","haram-view"],event=dict(start="2027-03-09",end="2027-03-14",note="تقريبي"))],
 "madinah":[P("eid-al-fitr-2027","فنادق المدينة عيد الفطر 2027","Madinah Eid",24.4672,39.6112,2,"المسجد النبوي","المسجد النبوي","event",["family"],event=dict(start="2027-03-09",end="2027-03-14",note="تقريبي"))],
}
def hav(a,b):
    R=6371; p1,p2=math.radians(a["lat"]),math.radians(b["lat"]); d1=p2-p1; d2=math.radians(b["lng"]-a["lng"])
    h=math.sin(d1/2)**2+math.cos(p1)*math.cos(p2)*math.sin(d2/2)**2
    return 2*R*math.asin(math.sqrt(h))
def finalize(c):
    for p in c["pois"]:
        others=[o for o in c["pois"] if o is not p and o["type"] not in("event","intent_hub")]
        others.sort(key=lambda o: hav(p,o))
        p["neighbours"]=[dict(slug=o["slug"],name_ar=o["name_ar"],km=round(hav(p,o),1)) for o in others[:5]]
    c["poi_count"]=len(c["pois"])
idx=json.load(open(os.path.join(H,"cities.json"),encoding="utf-8"))
have={i["slug"] for i in idx}
for c in NEW:
    if c["slug"] in have: continue
    finalize(c); json.dump(c,open(os.path.join(H,f"{c['slug']}.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    idx.append(dict(slug=c["slug"],code=c["code"],name_ar=c["name_ar"],name_en=c["name_en"],country=c["country"],lat=c["lat"],lng=c["lng"],default_prox=c["default_prox"],date_profile=c["date_profile"],default_nights=c["default_nights"],poi_count=c["poi_count"],priority=2))
for slug,ev in EXTRA_EVENTS.items():
    f=os.path.join(H,f"{slug}.json"); c=json.load(open(f,encoding="utf-8")); hv={p["slug"] for p in c["pois"]}
    c["pois"]+=[p for p in ev if p["slug"] not in hv]; finalize(c); json.dump(c,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
for i in idx: i["poi_count"]=json.load(open(os.path.join(H,f"{i['slug']}.json"),encoding="utf-8"))["poi_count"]
json.dump(idx,open(os.path.join(H,"cities.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print(len(idx),"cities",sum(i["poi_count"] for i in idx),"pois")
