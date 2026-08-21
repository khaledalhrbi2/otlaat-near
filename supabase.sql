-- جدول قياس ضغطات /go/ — نفّذه في Supabase SQL Editor ثم أضف SUPABASE_URL و SUPABASE_SERVICE_KEY في Vercel
create table if not exists go_clicks (
  id bigint generated always as identity primary key,
  ts timestamptz default now(),
  city text, poi text, intent text, hotel text,
  checkin date, checkout date, roompax int,
  referer text, ua text, country text
);
create index on go_clicks (ts desc);
create index on go_clicks (city, poi);
-- استعلام سريع: أكثر الصفحات تحويلاً آخر 30 يوم
-- select city, poi, count(*) from go_clicks where ts > now()-interval '30 days' group by 1,2 order by 3 desc limit 50;
