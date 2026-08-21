import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const now = new Date().toISOString();

export default defineConfig({
  site: 'https://hotels-near.otlaat.sa',
  output: 'static',
  trailingSlash: 'always',
  build: { inlineStylesheets: 'always' },
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/go/') && !page.includes('/api/'),
      changefreq: 'weekly',
      lastmod: new Date(now),
      serialize(item) {
        const path = new URL(item.url).pathname;
        const depth = path.split('/').filter(Boolean).length;
        if (depth === 0) { item.priority = 1.0; item.changefreq = 'daily'; }
        else if (depth === 1) { item.priority = 0.9; item.changefreq = 'daily'; }          // hub المدينة
        else if (/\/hotels-(riyadh-season|ramadan|hajj|keukenhof)/.test(path)) { item.priority = 0.9; item.changefreq = 'weekly'; } // موسمي
        else if (path.includes('/hotels-near-')) { item.priority = 0.8; }
        else { item.priority = 0.7; }                                                      // أحياء ونوايا
        return item;
      },
    }),
  ],
});
