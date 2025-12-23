import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  i18n: {
    defaultLocale: 'az',
    locales: ['az', 'en', 'ar', 'fr', 'de', 'zh', 'fa', 'tr'],
    routing: {
      prefixDefaultLocale: false
    },
    fallback: {
      az: 'en'
    }
  },
  site: 'https://quba.cottage',
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto'
  },
  prefetch: {
    defaultStrategy: 'viewport',
    prefetchAll: true
  }
});
