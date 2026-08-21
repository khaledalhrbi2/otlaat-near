# near.otlaat.sa — صفحات "فنادق قريبة من"

Astro (ثابت) + Vercel. 16 مدينة، 156 صفحة معلم، كل صفحة تحوّل إلى بحث جاهز على otlaat.com بالإحداثيات ونصف القطر والتواريخ المحسوبة لحظياً.

## تشغيل محلي
```bash
npm install
npm run dev
```

## توليد المحتوى الفريد (مرة واحدة ثم عند الإضافة)
```bash
cp .env.example .env   # ضع ANTHROPIC_API_KEY
npm run content            # كل المدن
node scripts/generate-content.mjs riyadh   # مدينة واحدة
```
الناتج في `data/content/<city>/<poi>.json` مع `reviewed:false` — راجعه فريق المحتوى ثم غيّره إلى `true`. الصفحات تعمل بدون هذه الملفات (محتوى احتياطي من البيانات) لكنها ستكون أقل تميّزاً لجوجل.

## النشر على Vercel
1. ارفع الريبو إلى GitHub.
2. Vercel → New Project → اختر الريبو → Framework: Astro (يُكتشف تلقائياً) → Deploy.
3. أضف الدومين `near.otlaat.sa` في Settings → Domains، وأضف CNAME في Cloudflare يشير إلى `cname.vercel-dns.com` (بدون بروكسي برتقالي أو مع Full SSL).
4. غيّر `site` في `astro.config.mjs` إذا اخترت دوميناً آخر.

## إضافة مدينة أو معلم
عدّل `data/<city>.json` (أو أضف ملفاً جديداً وسجّله في `data/cities.json`)، ثم `npm run content` و`git push`. Vercel يعيد البناء تلقائياً.

## الهيكل
- `src/pages/[city]/index.astro` — Hub المدينة
- `src/pages/[city]/near/[poi].astro` — صفحة المعلم (خريطة + شريط حجز + محتوى + FAQ + روابط السايلو)
- `src/lib/bookingLink.js` — منطق الرابط والتواريخ وUTM
- `src/components/BookingBar.astro`, `MapRing.astro`
