import json, math, os
H=os.path.join(os.path.dirname(__file__),'..','data')
T=["transit","budget","apartments","family"]
def P(slug,ar,en,lat,lng,line,prox=1.5,kw=None):
    return dict(slug=slug,name_ar=ar,name_en=en,lat=lat,lng=lng,prox_km=prox,q=ar.replace('محطة ',''),poi_label=ar,type="metro",
                intents=T,nearest_metro=line,keywords=kw or [f"فنادق قريبة من {ar}",f"فنادق قريبة من مترو {ar.replace('محطة ','')}"])
ADD={
"riyadh":[
 P("kafd-metro-station","محطة مترو كافد","KAFD Metro Station",24.7667,46.6428,"المسار الأزرق · الأحمر · الأصفر (محطة رئيسية)",2),
 P("olaya-metro-station","محطة مترو العليا","Olaya Metro Station",24.6960,46.6860,"المسار الأزرق"),
 P("king-fahd-road-metro","محطة مترو طريق الملك فهد","King Fahd Road Metro",24.7040,46.6790,"المسار الأزرق"),
 P("kingdom-centre-metro","محطة مترو المملكة","Kingdom Centre Metro",24.7110,46.6740,"المسار الأزرق"),
 P("qasr-al-hokm-metro","محطة مترو قصر الحكم","Qasr Al Hokm Metro",24.6290,46.7130,"المسار الأزرق · البرتقالي"),
 P("national-museum-metro","محطة مترو المتحف الوطني","National Museum Metro",24.6470,46.7130,"المسار الأزرق · الأخضر"),
 P("stc-metro-station","محطة مترو STC","STC Metro Station",24.7480,46.6940,"المسار الأحمر · الأخضر"),
 P("airport-metro-terminal-3","محطة مترو المطار","Airport Metro Station",24.9560,46.7020,"المسار الأزرق",4),
 P("ministry-of-education-metro","محطة مترو وزارة التعليم","Ministry of Education Metro",24.7010,46.7120,"المسار الأخضر"),
 P("king-abdullah-road-metro","محطة مترو طريق الملك عبدالله","King Abdullah Road Metro",24.7350,46.6700,"المسار الأحمر"),
],
"dubai":[
 P("burj-khalifa-dubai-mall-metro","محطة مترو برج خليفة/دبي مول","Burj Khalifa/Dubai Mall Metro",25.2011,55.2699,"الخط الأحمر"),
 P("mall-of-the-emirates-metro","محطة مترو مول الإمارات","Mall of the Emirates Metro",25.1210,55.2000,"الخط الأحمر"),
 P("dmcc-metro","محطة مترو DMCC","DMCC Metro",25.0730,55.1430,"الخط الأحمر"),
 P("sobha-realty-metro","محطة مترو صبحا ريالتي (المارينا)","Sobha Realty Metro",25.0830,55.1480,"الخط الأحمر"),
 P("business-bay-metro","محطة مترو الخليج التجاري","Business Bay Metro",25.1920,55.2620,"الخط الأحمر"),
 P("union-metro","محطة مترو الاتحاد","Union Metro",25.2660,55.3130,"الخط الأحمر · الأخضر"),
 P("burjuman-metro","محطة مترو برجمان","BurJuman Metro",25.2550,55.3040,"الخط الأحمر · الأخضر"),
 P("al-rigga-metro","محطة مترو الرقة","Al Rigga Metro",25.2650,55.3210,"الخط الأحمر"),
 P("airport-terminal-1-metro","محطة مترو المطار مبنى 1","Airport Terminal 1 Metro",25.2480,55.3600,"الخط الأحمر",3),
 P("airport-terminal-3-metro","محطة مترو المطار مبنى 3","Airport Terminal 3 Metro",25.2440,55.3550,"الخط الأحمر",3),
 P("deira-city-centre-metro","محطة مترو سيتي سنتر ديرة","Deira City Centre Metro",25.2530,55.3320,"الخط الأحمر"),
 P("al-jafiliya-metro","محطة مترو الجافلية","Al Jafiliya Metro",25.2340,55.2850,"الخط الأحمر"),
 P("expo-2020-metro","محطة مترو إكسبو","Expo Metro",24.9640,55.1520,"الخط الأحمر (Route 2020)",3),
 P("creek-metro","محطة مترو الخور","Creek Metro",25.2180,55.3330,"الخط الأخضر"),
],
"istanbul":[
 P("taksim-metro","محطة مترو تقسيم","Taksim Metro",41.0369,28.9850,"M2"),
 P("sisli-mecidiyekoy-metro","محطة مترو شيشلي-مجيدية كوي","Sisli-Mecidiyekoy Metro",41.0620,28.9910,"M2 · M7"),
 P("osmanbey-metro","محطة مترو عثمان بيه","Osmanbey Metro",41.0510,28.9870,"M2"),
 P("levent-metro","محطة مترو ليفنت","Levent Metro",41.0790,29.0110,"M2 · M6"),
 P("vezneciler-metro","محطة مترو وزنجيلر","Vezneciler Metro",41.0130,28.9580,"M2"),
 P("yenikapi-metro","محطة يني كابي","Yenikapi Station",41.0050,28.9510,"M1 · M2 · مرمراي"),
 P("sultanahmet-tram","محطة ترام السلطان أحمد","Sultanahmet Tram",41.0065,28.9760,"T1"),
 P("eminonu-tram","محطة ترام أمينونو","Eminonu Tram",41.0170,28.9710,"T1"),
 P("kabatas-tram","محطة كاباتاش","Kabatas Station",41.0340,28.9930,"T1 · F1"),
 P("aksaray-metro","محطة مترو أكسراي","Aksaray Metro",41.0120,28.9500,"M1"),
 P("istanbul-airport-metro","محطة مترو مطار إسطنبول","Istanbul Airport Metro",41.2620,28.7420,"M11",4),
 P("sabiha-gokcen-metro","محطة مترو مطار صبيحة","Sabiha Gokcen Metro",40.9000,29.3100,"M4",3),
 P("uskudar-marmaray","محطة أوسكودار مرمراي","Uskudar Marmaray",41.0250,29.0130,"مرمراي · M5"),
 P("kadikoy-metro","محطة مترو كاديكوي","Kadikoy Metro",40.9900,29.0250,"M4"),
],
"london":[
 P("paddington-station","محطة بادينغتون","Paddington Station",51.5170,-0.1770,"Bakerloo · Circle · District · Elizabeth · Heathrow Express"),
 P("kings-cross-st-pancras","محطة كينغز كروس سانت بانكراس","King's Cross St Pancras",51.5308,-0.1238,"6 خطوط + يوروستار"),
 P("victoria-station","محطة فيكتوريا","Victoria Station",51.4952,-0.1441,"Victoria · Circle · District · Gatwick Express"),
 P("oxford-circus-station","محطة أكسفورد سيركس","Oxford Circus",51.5154,-0.1410,"Central · Bakerloo · Victoria"),
 P("bond-street-station","محطة بوند ستريت","Bond Street",51.5142,-0.1494,"Central · Jubilee · Elizabeth"),
 P("marble-arch-station","محطة ماربل آرش","Marble Arch",51.5136,-0.1586,"Central"),
 P("edgware-road-station","محطة إدجوير رود","Edgware Road",51.5203,-0.1679,"Bakerloo · Circle · District · H&C"),
 P("knightsbridge-station","محطة نايتسبريدج","Knightsbridge",51.5015,-0.1607,"Piccadilly"),
 P("green-park-station","محطة غرين بارك","Green Park",51.5067,-0.1428,"Piccadilly · Victoria · Jubilee"),
 P("waterloo-station","محطة ووترلو","Waterloo",51.5036,-0.1143,"Jubilee · Northern · Bakerloo · W&C"),
 P("liverpool-street-station","محطة ليفربول ستريت","Liverpool Street",51.5178,-0.0823,"Central · Elizabeth · Circle · Met · H&C"),
 P("euston-station","محطة يوستون","Euston",51.5282,-0.1337,"Northern · Victoria"),
 P("earls-court-station","محطة إيرلز كورت","Earl's Court",51.4913,-0.1935,"District · Piccadilly"),
 P("queensway-station","محطة كوينزواي","Queensway",51.5104,-0.1875,"Central"),
],
"paris":[
 P("gare-du-nord-station","محطة الشمال","Gare du Nord",48.8809,2.3553,"RER B/D · M4 · M5 · يوروستار"),
 P("gare-de-lyon-station","محطة ليون","Gare de Lyon",48.8443,2.3739,"RER A/D · M1 · M14"),
 P("chatelet-les-halles","شاتليه لي آل","Chatelet-Les Halles",48.8620,2.3470,"RER A/B/D · M1 · M4 · M7 · M11 · M14"),
 P("opera-metro","محطة مترو أوبرا","Opera Metro",48.8710,2.3320,"M3 · M7 · M8"),
 P("charles-de-gaulle-etoile","شارل ديغول إيتوال","Charles de Gaulle-Etoile",48.8738,2.2950,"M1 · M2 · M6 · RER A"),
 P("trocadero-metro","محطة مترو تروكاديرو","Trocadero Metro",48.8633,2.2870,"M6 · M9"),
 P("bir-hakeim-metro","محطة مترو بير حكيم","Bir-Hakeim Metro",48.8538,2.2895,"M6 · RER C (برج إيفل)"),
 P("saint-lazare-station","محطة سان لازار","Saint-Lazare",48.8760,2.3250,"M3 · M12 · M13 · M14"),
 P("montparnasse-station","محطة مونبارناس","Montparnasse",48.8410,2.3200,"M4 · M6 · M12 · M13 · TGV"),
 P("la-defense-station","محطة لا ديفانس","La Defense",48.8920,2.2380,"M1 · RER A · T2"),
 P("franklin-roosevelt-metro","محطة مترو فرانكلين روزفلت","Franklin D. Roosevelt",48.8690,2.3100,"M1 · M9 (الشانزليزيه)"),
],
"milan":[
 P("milano-centrale-station","محطة ميلانو سنترالي","Milano Centrale",45.4860,9.2040,"M2 · M3 · Malpensa Express"),
 P("duomo-metro","محطة مترو الدومو","Duomo Metro",45.4640,9.1900,"M1 · M3"),
 P("cadorna-station","محطة كادورنا","Cadorna",45.4680,9.1760,"M1 · M2 · Malpensa Express"),
 P("garibaldi-station","محطة غاريبالدي","Porta Garibaldi",45.4850,9.1880,"M2 · M5"),
 P("san-babila-metro","محطة مترو سان بابيلا","San Babila Metro",45.4660,9.1980,"M1 · M4"),
 P("loreto-metro","محطة مترو لوريتو","Loreto Metro",45.4860,9.2160,"M1 · M2"),
 P("lotto-san-siro-metro","محطة مترو سان سيرو","San Siro Stadio Metro",45.4790,9.1260,"M5"),
],
"vienna":[
 P("stephansplatz-ubahn","محطة شتيفانسبلاتز","Stephansplatz U-Bahn",48.2083,16.3720,"U1 · U3"),
 P("karlsplatz-ubahn","محطة كارلسبلاتز","Karlsplatz",48.2000,16.3700,"U1 · U2 · U4"),
 P("hauptbahnhof-station","محطة فيينا الرئيسية","Wien Hauptbahnhof",48.1850,16.3760,"U1 · قطارات"),
 P("westbahnhof-station","محطة ويست بانهوف","Westbahnhof",48.1970,16.3380,"U3 · U6"),
 P("praterstern-station","محطة براترشترن","Praterstern",48.2180,16.3920,"U1 · U2 · S-Bahn"),
 P("schwedenplatz-ubahn","محطة شفيدنبلاتز","Schwedenplatz",48.2115,16.3775,"U1 · U4"),
 P("schonbrunn-ubahn","محطة مترو شونبرون","Schonbrunn U-Bahn",48.1870,16.3210,"U4"),
],
"prague":[
 P("mustek-metro","محطة مترو موستيك","Mustek Metro",50.0840,14.4240,"A · B"),
 P("muzeum-metro","محطة مترو موزيوم","Muzeum Metro",50.0800,14.4300,"A · C"),
 P("hlavni-nadrazi-station","المحطة الرئيسية","Hlavni Nadrazi",50.0830,14.4350,"C · قطارات"),
 P("malostranska-metro","محطة مترو مالوسترانسكا","Malostranska Metro",50.0910,14.4140,"A"),
 P("namesti-republiky-metro","محطة مترو ساحة الجمهورية","Namesti Republiky Metro",50.0890,14.4290,"B"),
 P("andel-metro","محطة مترو أنديل","Andel Metro",50.0700,14.4040,"B"),
],
"barcelona":[
 P("placa-catalunya-station","محطة ساحة كاتالونيا","Placa de Catalunya",41.3870,2.1700,"L1 · L3 · FGC · Rodalies · Aerobus"),
 P("passeig-de-gracia-station","محطة باسيج دي غراسيا","Passeig de Gracia",41.3920,2.1650,"L2 · L3 · L4 · Rodalies"),
 P("sants-estacio","محطة سانتس","Sants Estacio",41.3790,2.1400,"L3 · L5 · AVE"),
 P("sagrada-familia-metro","محطة مترو ساغرادا فاميليا","Sagrada Familia Metro",41.4040,2.1740,"L2 · L5"),
 P("diagonal-metro","محطة مترو دياغونال","Diagonal Metro",41.3960,2.1610,"L3 · L5"),
 P("liceu-metro","محطة مترو ليسيو","Liceu Metro",41.3800,2.1730,"L3 (لا رامبلا)"),
 P("barceloneta-metro","محطة مترو برشلونيتا","Barceloneta Metro",41.3820,2.1850,"L4"),
 P("universitat-metro","محطة مترو أونيفرسيتات","Universitat Metro",41.3860,2.1640,"L1 · L2"),
],
"amsterdam":[
 P("centraal-station","المحطة المركزية","Amsterdam Centraal",52.3791,4.9003,"كل الخطوط · قطار المطار"),
 P("amsterdam-zuid-station","محطة أمستردام زاود","Amsterdam Zuid",52.3390,4.8740,"52 · 50 · قطارات"),
 P("sloterdijk-station","محطة سلوترديك","Sloterdijk",52.3890,4.8380,"50 · قطارات"),
 P("amstel-station","محطة أمستل","Amstel Station",52.3460,4.9180,"51 · 53 · 54 · قطارات"),
 P("rokin-metro","محطة مترو روكين","Rokin Metro",52.3700,4.8920,"52"),
 P("de-pijp-metro","محطة مترو دي بايب","De Pijp Metro",52.3540,4.8920,"52"),
],
"rome":[
 P("termini-station","محطة تيرميني","Roma Termini",41.9010,12.5020,"A · B · قطارات · Leonardo Express"),
 P("spagna-metro","محطة مترو سبانيا","Spagna Metro",41.9060,12.4830,"A (الدرج الإسباني)"),
 P("barberini-metro","محطة مترو باربيريني","Barberini Metro",41.9040,12.4880,"A (تريفي)"),
 P("ottaviano-metro","محطة مترو أوتافيانو","Ottaviano Metro",41.9100,12.4580,"A (الفاتيكان)"),
 P("colosseo-metro","محطة مترو كولوسيو","Colosseo Metro",41.8905,12.4930,"B"),
 P("flaminio-metro","محطة مترو فلامينيو","Flaminio Metro",41.9110,12.4760,"A (بيازا ديل بوبولو)"),
 P("tiburtina-station","محطة تيبورتينا","Roma Tiburtina",41.9100,12.5310,"B · قطارات",2),
],
"zurich":[
 P("zurich-hb-station","محطة زيورخ الرئيسية","Zurich HB",47.3780,8.5400,"كل القطارات · S-Bahn · الترام"),
 P("stadelhofen-station","محطة شتادلهوفن","Stadelhofen",47.3665,8.5485,"S-Bahn · الترام (البحيرة)"),
 P("oerlikon-station","محطة أورليكون","Zurich Oerlikon",47.4110,8.5440,"S-Bahn · قطار المطار"),
 P("enge-station","محطة إنغه","Zurich Enge",47.3640,8.5310,"S-Bahn"),
],
"geneva":[
 P("cornavin-station","محطة كورنافان","Geneve Cornavin",46.2100,6.1420,"كل القطارات · الترام · قطار المطار"),
 P("eaux-vives-station","محطة أو-فيف","Geneve Eaux-Vives",46.2000,6.1660,"Leman Express"),
 P("geneva-airport-station","محطة مطار جنيف","Geneve Aeroport",46.2310,6.1090,"قطارات مباشرة",3),
],
}
def hav(a,b):
    R=6371; p1,p2=math.radians(a["lat"]),math.radians(b["lat"]); d1=p2-p1; d2=math.radians(b["lng"]-a["lng"])
    h=math.sin(d1/2)**2+math.cos(p1)*math.cos(p2)*math.sin(d2/2)**2
    return 2*R*math.asin(math.sqrt(h))
total=0; added=0
for slug,extra in ADD.items():
    f=os.path.join(H,f"{slug}.json"); c=json.load(open(f,encoding="utf-8"))
    have={p["slug"] for p in c["pois"]}; new=[p for p in extra if p["slug"] not in have]; added+=len(new)
    c["pois"]+=new
    # fill nearest_metro for POIs lacking it
    metros=[p for p in c["pois"] if p["type"]=="metro"]
    for p in c["pois"]:
        if p["type"]!="metro" and not p.get("nearest_metro") and metros:
            m=min(metros,key=lambda o:hav(p,o)); d=hav(p,m)
            if d<=2.5: p["nearest_metro"]=f"{m['name_ar']} ({d:.1f} كم)"
        others=[o for o in c["pois"] if o is not p and o["type"] not in("event","intent_hub")]
        others.sort(key=lambda o: hav(p,o))
        p["neighbours"]=[dict(slug=o["slug"],name_ar=o["name_ar"],km=round(hav(p,o),1)) for o in others[:5]]
    c["poi_count"]=len(c["pois"]); json.dump(c,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
idx=json.load(open(os.path.join(H,"cities.json"),encoding="utf-8"))
for i in idx: i["poi_count"]=json.load(open(os.path.join(H,f"{i['slug']}.json"),encoding="utf-8"))["poi_count"]
json.dump(idx,open(os.path.join(H,"cities.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("added",added,"total",sum(i["poi_count"] for i in idx))
