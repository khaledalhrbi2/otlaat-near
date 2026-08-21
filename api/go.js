/**
 * /go/:city/:poi?ci=YYYY-MM-DD&co=YYYY-MM-DD&rp=1  →  302 إلى محرك عطلات
 * الرابط الداخلي يظهر للزائر ولمحركات البحث كأنه داخلي، والتحويل يتم على السيرفر.
 */
import fs from 'node:fs';
import path from 'node:path';

const BASE = 'https://www.otlaat.com/hotels';
const root = path.join(process.cwd(), 'data');
const cache = {};
const load = (slug) => cache[slug] ??= JSON.parse(fs.readFileSync(path.join(root, `${slug}.json`), 'utf8'));

const ymd = (s) => /^\d{4}-\d{2}-\d{2}$/.test(s || '') ? s.replaceAll('-', '') : null;
const plus = (d, n) => { const x = new Date(d); x.setUTCDate(x.getUTCDate() + n); return x.toISOString().slice(0, 10); };

export default function handler(req, res) {
  const { city: citySlug, poi: poiSlug, ci, co, rp, i, h } = req.query;
  let city;
  try { city = load(String(citySlug || '').replace(/[^a-z-]/g, '')); } catch { return res.status(404).send('Not found'); }
  const poi = poiSlug ? city.pois.find(p => p.slug === poiSlug) : null;
  if (poiSlug && !poi) return res.status(404).send('Not found');

  const today = new Date().toISOString().slice(0, 10);
  let checkin = ymd(ci) ? ci : plus(today, 1);
  let checkout = ymd(co) && co > checkin ? co : plus(checkin, city.default_nights || 1);
  const INTENT = { apartments:{ q:'شقق فندقية', rp:2 }, budget:{ q:'فنادق رخيصة', rp:1 }, '5-star':{ q:'فنادق 5 نجوم', rp:1 }, family:{ q:'', rp:2 } };
  const iv = INTENT[i] || null;
  const roompax = Math.min(Math.max(parseInt(rp) || (iv?.rp ?? 1), 1), 5);

  const p = new URLSearchParams({ name: city.name_ar, checkin: checkin.replaceAll('-', ''), checkout: checkout.replaceAll('-', ''), roompax: String(roompax) });
  if (city.code) p.set('code', city.code);
  if (h) { p.set('q', String(h).slice(0, 80)); p.set('hotel', String(h).slice(0, 80)); }
  if (poi) { if (!h) p.set('q', iv?.q ? `${iv.q} ${poi.q}` : poi.q); p.set('lat', poi.lat); p.set('lng', poi.lng); p.set('prox', poi.prox_km); p.set('poi', poi.poi_label); }
  else { if (!h) p.set('q', city.name_ar); p.set('lat', city.lat); p.set('lng', city.lng); p.set('prox', city.default_prox); }
  p.set('utm_source', 'hotels-near'); p.set('utm_medium', 'referral');
  p.set('utm_campaign', `${city.slug}-${poi ? poi.slug : 'hub'}${i && i !== 'default' ? '-' + i : ''}${h ? '-hotel' : ''}`);

  const target = `${BASE}?${p.toString()}`;
  // قياس: تسجيل الضغطة في Supabase إن وُجدت المفاتيح (لا يعطل التحويل)
  if (process.env.SUPABASE_URL && process.env.SUPABASE_SERVICE_KEY) {
    fetch(`${process.env.SUPABASE_URL}/rest/v1/go_clicks`, { method:'POST', headers:{ 'content-type':'application/json', apikey:process.env.SUPABASE_SERVICE_KEY, authorization:`Bearer ${process.env.SUPABASE_SERVICE_KEY}`, prefer:'return=minimal' },
      body: JSON.stringify({ city: city.slug, poi: poi?.slug ?? null, intent: i ?? null, hotel: h ?? null, checkin, checkout, roompax, referer: req.headers.referer ?? null, ua: req.headers['user-agent'] ?? null, country: req.headers['x-vercel-ip-country'] ?? null }) }).catch(() => {});
  }
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex, nofollow');
  res.redirect(302, target);
}
