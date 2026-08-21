import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
export default defineConfig({
  site: 'https://near.otlaat.sa',
  output: 'static',
  trailingSlash: 'always',
  integrations: [sitemap()],
});
