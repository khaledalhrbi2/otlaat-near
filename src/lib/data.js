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
    meta: `قارن فنادق ${city.name_ar} ضمن ${poi.prox_km} كم من ${poi.name_ar} مع المسافة الفعلية والأسعار شاملة الضرائب وإلغاء مجاني. احجز عبر عطلات.`,
    intro: isMetro ? `تبحث عن فندق قريب من ${poi.name_ar}؟ الإقامة بجوار محطة ${poi.nearest_metro ? `(${poi.nearest_metro})` : ''} تعني وصولاً سريعاً لكل المدينة دون سيارة. هذه الصفحة تعرض الفنادق ضمن ${poi.prox_km} كم من المحطة مع المسافة الفعلية سيراً، والسعر شاملاً الضرائب. المعالم المجاورة: ${near}.` : `تبحث عن فندق قريب من ${poi.name_ar}؟ هذه الصفحة تعرض الفنادق الواقعة ضمن ${poi.prox_km} كم من ${poi.name_ar} في ${city.name_ar}، مع المسافة الفعلية لكل فندق، والسعر شاملاً الضرائب، وخيارات التقسيط عبر تابي وتمارا. ${poi.nearest_metro ? `أقرب محطة: ${poi.nearest_metro}.` : ''} المعالم المجاورة: ${near}.`,
    about: isMetro ? `${poi.name_ar} تخدم ${poi.nearest_metro || 'خطوط المترو الرئيسية'}، وتناسب من يعتمد على المواصلات العامة أو يصل بالقطار من المطار. الفنادق في محيطها غالباً أقل سعراً من المعالم السياحية مع نفس سهولة الوصول.` : `${poi.name_ar} من أكثر المناطق طلباً للإقامة في ${city.name_ar}${poi.type === 'airport' ? '، ويناسب المسافرين العابرين والرحلات المبكرة' : poi.type === 'district' ? '، ويجمع بين قرب الخدمات وتنوع خيارات الإقامة من الشقق الفندقية إلى فنادق الخمس نجوم' : '، ويبحث عنه الزوار الخليجيون لقربه من الفعاليات والتسوق والمطاعم'}.`,
    faq: [
      { q: `كم تبعد فنادق هذه الصفحة عن ${poi.name_ar}؟`, a: `جميع النتائج ضمن ${poi.prox_km} كم، والمسافة الدقيقة تظهر على كل فندق في صفحة النتائج.` },
      { q: `هل الأسعار شاملة الضرائب؟`, a: `نعم، كل الأسعار المعروضة في عطلات شاملة الضرائب ورسوم الخدمة، بدون رسوم مخفية عند الوصول.` },
      { q: `هل يمكن الدفع بالتقسيط؟`, a: `نعم، يتوفر التقسيط عبر تابي وتمارا على أغلب الحجوزات، إضافة إلى مدى وApple Pay.` },
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
