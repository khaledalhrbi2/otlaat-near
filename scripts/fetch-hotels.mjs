/**
 * يسحب أفضل الفنادق لكل مدينة وفئة من Google Places (Text Search) مرتبة بتقييم الناس،
 * ويحفظ الاسم والنجوم والإحداثيات فقط في data/hotels/<city>.json (بدون تقييمات، التزاماً بشروط جوجل).
 *
 * التشغيل:  GOOGLE_PLACES_KEY=AIza... node scripts/fetch-hotels.mjs [city-slug]
 * المفتاح: console.cloud.google.com → APIs → Places API (New) → Credentials
 * الكلفة: ~8 طلبات/مدينة × 23 = ~190 طلباً — ضمن الرصيد المجاني الشهري.
 */
import fs from 'node:fs';
const KEY = process.env.GOOGLE_PLACES_KEY;
if (!KEY) { console.error('GOOGLE_PLACES_KEY مفقود'); process.exit(1); }
const only = process.argv[2];
const cities = JSON.parse(fs.readFileSync('data/cities.json','utf8')).filter(c => !only || c.slug === only);
const AR = { cheap:'cheap hotels', '5-star':'best 5 star hotels', '4-star':'best 4 star hotels', '3-star':'best 3 star hotels', apartments:'hotel apartments', family:'family friendly hotels', beach:'beach resorts', pool:'hotels with pool' };
const MIN_RATING = 4.0, MIN_COUNT = 300;

async function search(q, lat, lng) {
  const r = await fetch('https://places.googleapis.com/v1/places:searchText', { method:'POST',
    headers:{ 'content-type':'application/json', 'X-Goog-Api-Key':KEY, 'X-Goog-FieldMask':'places.id,places.displayName,places.location,places.rating,places.userRatingCount,places.types,places.formattedAddress' },
    body: JSON.stringify({ textQuery:q, languageCode:'en', maxResultCount:15, locationBias:{ circle:{ center:{ latitude:lat, longitude:lng }, radius:25000 } } }) });
  const j = await r.json(); return j.places ?? [];
}
const starsFromName = (n) => /5\s*star|resort|palace|ritz|four seasons|waldorf|st\. regis|sofitel|kempinski|fairmont|shangri|mandarin|jumeirah|address|raffles|bulgari|armani|w\s+dubai|edition|intercontinental|conrad|hilton|marriott|hyatt|sheraton|westin|jw|anantara|taj|rotana/i.test(n) ? 5 : /ibis|rove|premier inn|holiday inn express|citymax|budget/i.test(n) ? 3 : 4;

for (const c of cities) {
  const out = `data/hotels/${c.slug}.json`;
  const map = new Map();
  for (const [tag, q] of Object.entries(AR)) {
    const res = await search(`${q} ${c.name_en}`, c.lat, c.lng);
    res.filter(p => (p.rating ?? 0) >= MIN_RATING && (p.userRatingCount ?? 0) >= MIN_COUNT && (p.types||[]).some(t => /hotel|lodging|resort/.test(t)))
       .forEach(p => { const h = map.get(p.id) ?? { name:p.displayName.text, name_ar:'', stars:(tag==='5-star'?5:tag==='3-star'||tag==='cheap'?3:tag==='4-star'?4:starsFromName(p.displayName.text)), lat:+p.location.latitude.toFixed(4), lng:+p.location.longitude.toFixed(4), area:null, tags:[], _r:p.rating, _n:p.userRatingCount };
         if (!h.tags.includes(tag)) h.tags.push(tag); map.set(p.id, h); });
    await new Promise(r => setTimeout(r, 200));
  }
  // ربط كل فندق بأقرب حي/معلم من بيانات المدينة
  const city = JSON.parse(fs.readFileSync(`data/${c.slug}.json`,'utf8'));
  const hav = (a,b) => { const R=6371,p1=a.lat*Math.PI/180,p2=b.lat*Math.PI/180,d1=p2-p1,d2=(b.lng-a.lng)*Math.PI/180; const h=Math.sin(d1/2)**2+Math.cos(p1)*Math.cos(p2)*Math.sin(d2/2)**2; return 2*R*Math.asin(Math.sqrt(h)); };
  const hotels = [...map.values()].sort((a,b) => (b._r*Math.log10(b._n)) - (a._r*Math.log10(a._n))).map(h => {
    const near = city.pois.filter(p => p.type==='district').map(p => [p, hav(h,p)]).sort((a,b)=>a[1]-b[1])[0];
    h.area = near && near[1] <= 3 ? near[0].slug : null; delete h._r; delete h._n; return h; });
  fs.writeFileSync(out, JSON.stringify({ city:c.slug, updated:new Date().toISOString().slice(0,10), hotels }, null, 1));
  console.log('✓', c.slug, hotels.length, 'hotels');
}
