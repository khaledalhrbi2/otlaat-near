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
  const near = poi.neighbours.slice(0, 3).map(n => `${n.name_ar} (${n.km} كم)`).join('، ');
  return {
    title: `أفضل الفنادق القريبة من ${poi.name_ar} في ${city.name_ar}`,
    meta: `قارن فنادق ${city.name_ar} ضمن ${poi.prox_km} كم من ${poi.name_ar} مع المسافة الفعلية والأسعار شاملة الضرائب وإلغاء مجاني. احجز عبر عطلات.`,
    intro: `تبحث عن فندق قريب من ${poi.name_ar}؟ هذه الصفحة تعرض الفنادق الواقعة ضمن ${poi.prox_km} كم من ${poi.name_ar} في ${city.name_ar}، مع المسافة الفعلية لكل فندق، والسعر شاملاً الضرائب، وخيارات التقسيط عبر تابي وتمارا. ${poi.nearest_metro ? `أقرب محطة: ${poi.nearest_metro}.` : ''} المعالم المجاورة: ${near}.`,
    about: `${poi.name_ar} من أكثر المناطق طلباً للإقامة في ${city.name_ar}${poi.type === 'airport' ? '، ويناسب المسافرين العابرين والرحلات المبكرة' : poi.type === 'district' ? '، ويجمع بين قرب الخدمات وتنوع خيارات الإقامة من الشقق الفندقية إلى فنادق الخمس نجوم' : '، ويبحث عنه الزوار الخليجيون لقربه من الفعاليات والتسوق والمطاعم'}.`,
    faq: [
      { q: `كم تبعد فنادق هذه الصفحة عن ${poi.name_ar}؟`, a: `جميع النتائج ضمن ${poi.prox_km} كم، والمسافة الدقيقة تظهر على كل فندق في صفحة النتائج.` },
      { q: `هل الأسعار شاملة الضرائب؟`, a: `نعم، كل الأسعار المعروضة في عطلات شاملة الضرائب ورسوم الخدمة، بدون رسوم مخفية عند الوصول.` },
      { q: `هل يمكن الدفع بالتقسيط؟`, a: `نعم، يتوفر التقسيط عبر تابي وتمارا على أغلب الحجوزات، إضافة إلى مدى وApple Pay.` },
    ],
  };
}
