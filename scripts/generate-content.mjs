/**
 * يولّد محتوى فريداً لكل POI عبر Claude API ويحفظه في data/content/<city>/<poi>.json
 * التشغيل: ANTHROPIC_API_KEY=... node scripts/generate-content.mjs [city-slug] [--force]
 * الصفحات تقرأ هذه الملفات تلقائياً؛ وبدونها تستخدم محتوى احتياطياً من البيانات.
 */
import fs from 'node:fs';
import path from 'node:path';
const KEY = process.env.ANTHROPIC_API_KEY;
if (!KEY) { console.error('ANTHROPIC_API_KEY مفقود'); process.exit(1); }
const only = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : null;
const force = process.argv.includes('--force');
const cities = JSON.parse(fs.readFileSync('data/cities.json','utf8')).filter(c => !only || c.slug === only);

const SYSTEM = `أنت كاتب محتوى سياحي عربي لشركة عطلات السعودية. تكتب بلهجة بيضاء واضحة للمسافر الخليجي، بدون مبالغة تسويقية، وبمعلومات عملية فقط (المواقف، المترو، المسافات، ما يناسب العوائل). لا تذكر أسماء فنادق محددة. أعد JSON فقط بلا أي نص آخر.`;

async function gen(city, poi) {
  const nb = poi.neighbours.map(n => `${n.name_ar} (${n.km} كم)`).join('، ');
  const user = `المدينة: ${city.name_ar} (${city.country})
المعلم/المنطقة: ${poi.name_ar} (${poi.name_en}) — النوع: ${poi.type} — النطاق: ${poi.prox_km} كم
${poi.nearest_metro ? 'أقرب محطة: '+poi.nearest_metro : ''}
${poi.event ? 'حدث موسمي من '+poi.event.start+' إلى '+poi.event.end : ''}
النوايا: ${poi.intents.join('، ')}
الكلمات المستهدفة: ${poi.keywords.join('، ')}
المعالم المجاورة: ${nb}

أعد JSON بهذا الشكل:
{"title": "عنوان H1 يحتوي الكلمة المستهدفة الأولى (أقل من 65 حرفاً)",
 "meta": "وصف ميتا 140-155 حرفاً يذكر النطاق والأسعار شاملة الضرائب",
 "intro": "فقرة افتتاحية 60-90 كلمة تجيب مباشرة: لماذا يسكن الزائر هنا ومن يناسبه",
 "about": "فقرة 120-180 كلمة عن المكان: طابعه، الوصول إليه، المواقف/المترو، وقت الذروة، ما يناسب العوائل",
 "tips": ["3-5 نصائح عملية قصيرة"],
 "faq": [{"q":"سؤال بصيغة بحث حقيقية","a":"جواب 25-50 كلمة"}] (5 أسئلة، أحدها عن المسافة وأحدها عن السعر وأحدها عن العوائل)}`;
  const r = await fetch('https://api.anthropic.com/v1/messages', { method:'POST', headers:{ 'content-type':'application/json','x-api-key':KEY,'anthropic-version':'2023-06-01' },
    body: JSON.stringify({ model:'claude-sonnet-4-6', max_tokens:1800, system:SYSTEM, messages:[{role:'user',content:user}] }) });
  const j = await r.json();
  const txt = j.content?.map(b=>b.text||'').join('') ?? '';
  return JSON.parse(txt.replace(/```json|```/g,'').trim());
}

for (const c of cities) {
  const city = JSON.parse(fs.readFileSync(`data/${c.slug}.json`,'utf8'));
  fs.mkdirSync(`data/content/${c.slug}`, { recursive:true });
  for (const poi of city.pois) {
    const out = `data/content/${c.slug}/${poi.slug}.json`;
    if (fs.existsSync(out) && !force) continue;
    try { const data = await gen(city, poi); data.generated_at = new Date().toISOString(); data.reviewed = false;
      fs.writeFileSync(out, JSON.stringify(data,null,2)); console.log('✓', c.slug, poi.slug); }
    catch(e){ console.error('✗', c.slug, poi.slug, e.message); }
    await new Promise(r=>setTimeout(r,400));
  }
}
