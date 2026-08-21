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
  const { city: citySlug, poi: poiSlug, ci, co, rp, i } = req.query;
  let city;
  try { city = load(String(citySlug || '').replace(/[^a-z-]/g, '')); } catch { return res.status(404).send('Not found'); }
  const poi = poiSlug ? city.pois.find(p => p.slug === poiSlug) : null;
  if (poiSlug && !poi) return res.status(404).send('Not found');

  const today = new Date().toISOString().slice(0, 10);
  let checkin = ymd(ci) ? ci : plus(today, 1);
  let checkout = ymd(co) && co > checkin ? co : plus(checkin, city.default_nights || 1);
  const roompax = Math.min(Math.max(parseInt(rp) || 1, 1), 5);

  const p = new URLSearchParams({ code: city.code, name: city.name_ar, checkin: checkin.replaceAll('-', ''), checkout: checkout.replaceAll('-', ''), roompax: String(roompax) });
  if (poi) { p.set('q', poi.q); p.set('lat', poi.lat); p.set('lng', poi.lng); p.set('prox', poi.prox_km); p.set('poi', poi.poi_label); }
  else { p.set('q', city.name_ar); p.set('lat', city.lat); p.set('lng', city.lng); p.set('prox', city.default_prox); }
  p.set('utm_source', 'hotels-near'); p.set('utm_medium', 'referral');
  p.set('utm_campaign', `${city.slug}-${poi ? poi.slug : 'hub'}${i && i !== 'default' ? '-' + i : ''}`);

  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex, nofollow');
  res.redirect(302, `${BASE}?${p.toString()}`);
}
