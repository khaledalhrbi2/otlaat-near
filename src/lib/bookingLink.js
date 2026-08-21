/**
 * bookingLink.js — يبني رابط البحث على otlaat.com من سجل مدينة + POI
 * يُستخدم في المتصفح (لحساب التواريخ لحظياً) أو في Astro وقت البناء.
 *
 * الرابط الناتج:
 * https://www.otlaat.com/hotels?code=..&name=..&checkin=YYYYMMDD&checkout=YYYYMMDD
 *   &roompax=N&q=..&lat=..&lng=..&prox=..&poi=..&utm_source=..&utm_medium=..&utm_campaign=..
 */

const BASE = "https://www.otlaat.com/hotels";

const fmt = (d) =>
  `${d.getFullYear()}${String(d.getMonth() + 1).padStart(2, "0")}${String(d.getDate()).padStart(2, "0")}`;

const addDays = (d, n) => { const x = new Date(d); x.setDate(x.getDate() + n); return x; };

/** أقرب خميس قادم (إن كان اليوم خميس → بعد أسبوع إلا إذا كان قبل الظهر) */
function nextThursday(from) {
  const d = new Date(from);
  const diff = (4 - d.getDay() + 7) % 7 || 7;
  return addDays(d, diff);
}

/**
 * منطق التواريخ حسب ملف المدينة (date_profile) ونوع الـ POI
 *  - weekend_thu_sat : الرياض/جدة — خميس→سبت (ليلتان)
 *  - tomorrow_plus   : مكة/المدينة — الغد + default_nights
 *  - next_weekend    : دبي/إسطنبول — الخميس القادم + default_nights
 *  - two_weeks_out   : روما/بالي/أوروبا — +14 يوم + default_nights
 *  الحدث (poi.event) يتقدم على كل ما سبق إذا كان في المستقبل.
 */
export function computeDates(city, poi, now = new Date()) {
  const nights = city.default_nights || 1;

  if (poi?.event?.start) {
    const s = new Date(poi.event.start);
    const e = new Date(poi.event.end);
    if (now < e) {
      const checkin = now < s ? s : nextThursday(now);
      return { checkin, checkout: addDays(checkin, nights) };
    }
  }

  let checkin;
  switch (city.date_profile) {
    case "weekend_thu_sat": checkin = nextThursday(now); return { checkin, checkout: addDays(checkin, 2) };
    case "tomorrow_plus":   checkin = addDays(now, 1); break;
    case "next_weekend":    checkin = nextThursday(now); break;
    case "two_weeks_out":
    default:                checkin = addDays(now, 14); break;
  }
  return { checkin, checkout: addDays(checkin, nights) };
}

/** roompax حسب النية */
const ROOMPAX = { family: 2, b2b: 5, corporate: 1, couples: 1, default: 1 };

export function buildBookingLink(city, poi, opts = {}) {
  const { intent = "default", checkin, checkout, roompax, utm = {} } = opts;
  const dates = checkin && checkout ? { checkin, checkout } : computeDates(city, poi);

  const p = new URLSearchParams({
    code: city.code,
    name: city.name_ar,
    checkin: typeof dates.checkin === "string" ? dates.checkin : fmt(dates.checkin),
    checkout: typeof dates.checkout === "string" ? dates.checkout : fmt(dates.checkout),
    roompax: String(roompax ?? ROOMPAX[intent] ?? 1),
  });

  if (poi) {
    p.set("q", poi.q);
    p.set("lat", poi.lat);
    p.set("lng", poi.lng);
    p.set("prox", poi.prox_km);
    p.set("poi", poi.poi_label);
  } else {
    p.set("q", city.name_ar);
    p.set("lat", city.lat);
    p.set("lng", city.lng);
    p.set("prox", city.default_prox);
  }

  p.set("utm_source", utm.source || "poi-pages");
  p.set("utm_medium", utm.medium || "organic");
  p.set("utm_campaign", utm.campaign || `${city.slug}-${poi ? poi.slug : "hub"}${intent !== "default" ? "-" + intent : ""}`);

  return `${BASE}?${p.toString()}`;
}

/* ---------- مثال ----------
import cities from "./data/cities.json";
import riyadh from "./data/riyadh.json";
const poi = riyadh.pois.find(p => p.slug === "boulevard-city");
buildBookingLink(riyadh, poi, { intent: "family" });
// → https://www.otlaat.com/hotels?code=1f566&name=الرياض&checkin=20260827&checkout=20260829&roompax=2&q=بوليفارد الرياض&lat=24.7694&lng=46.6046&prox=3&poi=البوليفارد&utm_source=poi-pages&utm_medium=organic&utm_campaign=riyadh-boulevard-city-family
---------------------------- */
