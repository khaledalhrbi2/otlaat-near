import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve('data');
export const cities = JSON.parse(fs.readFileSync(path.join(root, 'cities.json'), 'utf8'));
export function loadCity(slug) {
  return JSON.parse(fs.readFileSync(path.join(root, `${slug}.json`), 'utf8'));
}
export function loadContent(city, poi) {
  const f = path.join(root, 'content', city, `${poi}.json`);
  return fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, 'utf8')) : null;
}
/** محتوى احتياطي مولَّد من البيانات عند غياب ملف المحتوى */
export function fallbackContent(city, poi) {
  const isMetro = poi.type === 'metro';
  const near = poi.neighbours.slice(0, 3).map(n => `${n.name_ar} (${n.km} كم)`).join('، ');
  return {
    title: `أفضل الفنادق القريبة من ${poi.name_ar} في ${city.name_ar}`,
    seo_title: `فنادق قريبة من ${poi.name_ar} | حجز بأفضل سعر وتقسيط تابي وتمارا — عطلات`,
    sections: [
      { h2: `حجز فنادق قريبة من ${poi.name_ar}`, p: `الحجز يتم في ثلاث خطوات: اختر تواريخك وعدد الغرف أعلاه، اضغط "تحقق من التوفر" لتظهر لك فنادق ${city.name_ar} الواقعة ضمن ${poi.prox_km} كم من ${poi.name_ar} مرتبة بالمسافة، ثم ادفع بالطريقة التي تناسبك. تأكيد الحجز فوري على البريد والواتساب، وأغلب الفنادق تتيح الإلغاء المجاني حتى يومين قبل الوصول.` },
      { h2: `أسعار الفنادق القريبة من ${poi.name_ar}`, p: `الأسعار تختلف حسب المسافة والفئة والموسم: الفنادق الملاصقة لـ${poi.name_ar} هي الأعلى سعراً، وكل كيلومتر إضافي يخفض السعر بشكل ملحوظ دون أن يؤثر على سهولة الوصول${poi.nearest_metro ? ` خصوصاً مع قرب ${poi.nearest_metro}` : ''}. كل الأسعار المعروضة شاملة الضرائب ورسوم الخدمة، ولا توجد رسوم إضافية عند الوصول.` },
      { h2: `تقسيط الفنادق القريبة من ${poi.name_ar} عبر تابي وتمارا`, p: `يمكنك تقسيم قيمة الحجز على 4 دفعات بدون فوائد أو رسوم عبر تابي أو تمارا، تُخصم الدفعة الأولى عند الحجز والبقية كل شهر. التقسيط متاح للمقيمين في السعودية والإمارات والكويت والبحرين على أغلب الحجوزات، وتظهر الخيارات المتاحة في صفحة الدفع. يتوفر أيضاً الدفع بمدى وApple Pay وSTC Pay والبطاقات الائتمانية.` },
    ],
    meta: `قارن فنادق ${city.name_ar} ضمن ${poi.prox_km} كم من ${poi.name_ar} مع المسافة الفعلية والأسعار شاملة الضرائب وإلغاء مجاني. احجز عبر عطلات.`,
    intro: isMetro ? `تبحث عن فندق قريب من ${poi.name_ar}؟ الإقامة بجوار محطة ${poi.nearest_metro ? `(${poi.nearest_metro})` : ''} تعني وصولاً سريعاً لكل المدينة دون سيارة. هذه الصفحة تعرض الفنادق ضمن ${poi.prox_km} كم من المحطة مع المسافة الفعلية سيراً، والسعر شاملاً الضرائب. المعالم المجاورة: ${near}.` : `تبحث عن فندق قريب من ${poi.name_ar}؟ هذه الصفحة تعرض الفنادق الواقعة ضمن ${poi.prox_km} كم من ${poi.name_ar} في ${city.name_ar}، مع المسافة الفعلية لكل فندق، والسعر شاملاً الضرائب، وخيارات التقسيط عبر تابي وتمارا. ${poi.nearest_metro ? `أقرب محطة: ${poi.nearest_metro}.` : ''} المعالم المجاورة: ${near}.`,
    about: isMetro ? `${poi.name_ar} تخدم ${poi.nearest_metro || 'خطوط المترو الرئيسية'}، وتناسب من يعتمد على المواصلات العامة أو يصل بالقطار من المطار. الفنادق في محيطها غالباً أقل سعراً من المعالم السياحية مع نفس سهولة الوصول.` : `${poi.name_ar} من أكثر المناطق طلباً للإقامة في ${city.name_ar}${poi.type === 'airport' ? '، ويناسب المسافرين العابرين والرحلات المبكرة' : poi.type === 'district' ? '، ويجمع بين قرب الخدمات وتنوع خيارات الإقامة من الشقق الفندقية إلى فنادق الخمس نجوم' : '، ويبحث عنه الزوار الخليجيون لقربه من الفعاليات والتسوق والمطاعم'}.`,
    faq: [
      { q: `كم تبعد فنادق هذه الصفحة عن ${poi.name_ar}؟`, a: `جميع النتائج ضمن ${poi.prox_km} كم، والمسافة الدقيقة تظهر على كل فندق في صفحة النتائج.` },
      { q: `هل الأسعار شاملة الضرائب؟`, a: `نعم، كل الأسعار المعروضة في عطلات شاملة الضرائب ورسوم الخدمة، بدون رسوم مخفية عند الوصول.` },
      { q: `هل أقدر أحجز فندق قريب من ${poi.name_ar} بالتقسيط؟`, a: `نعم، التقسيط على 4 دفعات بدون فوائد عبر تابي أو تمارا متاح على أغلب فنادق ${city.name_ar}، إضافة إلى مدى وApple Pay وSTC Pay.` },
      { q: `كم سعر الفنادق القريبة من ${poi.name_ar}؟`, a: `يعتمد على المسافة والفئة والموسم. أدخل تواريخك أعلاه لتظهر الأسعار الفعلية شاملة الضرائب مرتبة بالمسافة من ${poi.name_ar}.` },
      { q: `هل الإلغاء مجاني؟`, a: `أغلب الفنادق تتيح الإلغاء المجاني حتى يومين قبل الوصول، وتظهر سياسة الإلغاء بوضوح على كل فندق قبل الدفع.` },
    ],
  };
}

/** مسار الصفحة حسب نوع المعلم — الكلمة المفتاحية كاملة في الرابط */
export function poiPath(city, poi) {
  const t = poi.type;
  const seg = t === 'district' ? `hotels-in-${poi.slug}`
    : t === 'event' || t === 'intent_hub' ? `hotels-${poi.slug}`
    : `hotels-near-${poi.slug}`;
  return `/${city.slug}/${seg}/`;
}

export const intents = JSON.parse(fs.readFileSync(path.join(root, 'intents.json'), 'utf8'));
export const comparisons = JSON.parse(fs.readFileSync(path.join(root, 'compare.json'), 'utf8'));
export function hav(a, b) {
  const R = 6371, p1 = a.lat * Math.PI / 180, p2 = b.lat * Math.PI / 180, d1 = p2 - p1, d2 = (b.lng - a.lng) * Math.PI / 180;
  const h = Math.sin(d1/2)**2 + Math.cos(p1) * Math.cos(p2) * Math.sin(d2/2)**2;
  return 2 * R * Math.asin(Math.sqrt(h));
}
export function variantPath(city, poi, key) { return `/${city.slug}/${intents.variants[key].prefix}-${poi.slug}/`; }
export function variantContent(city, poi, key) {
  const v = intents.variants[key];
  const near = poi.neighbours.slice(0, 3).map(n => `${n.name_ar} (${n.km} كم)`).join('، ');
  const L = `${v.label} ${poi.name_ar}`;
  return {
    title: `${L} في ${city.name_ar}`,
    seo_title: `${L} | أسعار شاملة الضرائب وتقسيط تابي وتمارا — عطلات`,
    meta: `${L}: ${v.desc}. ضمن ${poi.prox_km} كم مع المسافة الفعلية، إلغاء مجاني، وتقسيط. احجز عبر عطلات.`,
    intro: `${L} — ${v.desc}. تعرض هذه الصفحة فقط ${v.q_suffix} الواقعة ضمن ${poi.prox_km} كم من ${poi.name_ar} في ${city.name_ar}، مرتبة بالمسافة، والسعر شاملاً الضرائب. المعالم المجاورة: ${near}.`,
    about: `${poi.name_ar} ${poi.type === 'district' ? 'من الأحياء' : 'من المعالم'} الأكثر طلباً للإقامة في ${city.name_ar}، و${v.q_suffix} هناك ${key === 'cheap' ? 'تكون غالباً على بعد 1–3 كم من المعلم نفسه، وهو فرق بسيط مقابل توفير ملحوظ' : key === '5-star' ? 'تتركز في الحلقة الأقرب للمعلم وتوفر نقلاً مجانياً أحياناً' : key === 'apartments' ? 'تناسب الإقامة 4 ليالٍ فأكثر لأن فرق السعر مع الفندق يعوضه المطبخ والمساحة' : 'توفر غرفاً متصلة وأسرّة إضافية ومسابح مناسبة للأطفال'}.`,
    sections: [
      { h2: `حجز ${L}`, p: `اختر التواريخ وعدد الغرف أعلاه ثم "تحقق من التوفر"؛ النتائج تكون ${v.q_suffix} فقط ضمن النطاق، مع سياسة الإلغاء لكل خيار قبل الدفع.` },
      { h2: `تقسيط ${L}`, p: `التقسيط على 4 دفعات بدون فوائد عبر تابي وتمارا متاح على أغلب الخيارات، إضافة إلى مدى وApple Pay وSTC Pay والبطاقات الائتمانية.` },
    ],
    faq: [
      { q: `ما أفضل ${v.q_suffix} قريبة من ${poi.name_ar}؟`, a: `الأفضل يعتمد على تواريخك؛ أدخلها أعلاه لتظهر الخيارات المتاحة مرتبة بالمسافة والتقييم مع السعر شاملاً الضرائب.` },
      { q: `كم تبعد عن ${poi.name_ar}؟`, a: `كل النتائج ضمن ${poi.prox_km} كم، والمسافة الدقيقة تظهر على كل خيار.` },
      { q: `هل التقسيط متاح؟`, a: `نعم عبر تابي أو تمارا على 4 دفعات بدون فوائد، مع مدى وApple Pay.` },
    ],
  };
}

export function loadHotels(citySlug) {
  const f = path.join(root, 'hotels', `${citySlug}.json`);
  return fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, 'utf8')).hotels : [];
}
/** فنادق قريبة من معلم: ضمن النطاق، مع فلتر نية اختياري، مرتبة بالمسافة */
export function hotelsNear(citySlug, poi, { tag = null, limit = 10, maxKm = null } = {}) {
  const km = maxKm ?? Math.max(poi.prox_km, 2);
  return loadHotels(citySlug).map(h => ({ ...h, km: hav(h, poi) }))
    .filter(h => h.km <= km && (!tag || h.tags.includes(tag) || (tag === '5-star' && h.stars === 5) || (tag === 'cheap' && h.stars <= 3) || (tag === '3-star' && h.stars === 3) || (tag === '4-star' && h.stars === 4)))
    .sort((a,b) => a.km - b.km).slice(0, limit);
}
/** فنادق المدينة حسب الفئة (ترتيب الملف = ترتيب التقييم) */
export function hotelsByTag(citySlug, tag, limit = 10) {
  return loadHotels(citySlug).filter(h => h.tags.includes(tag) || (tag === '5-star' && h.stars === 5) || (tag === 'cheap' && h.stars <= 3) || (tag === '3-star' && h.stars === 3) || (tag === '4-star' && h.stars === 4)).slice(0, limit);
}
