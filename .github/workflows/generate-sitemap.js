const fs = require('fs');
const { SitemapStream, streamToPromise } = require('sitemap');
const { readdirSync } = require('fs');

const sitemap = new SitemapStream({ hostname: 'https://yayabed.github.io/MagneticHub.fr/' });

(async () => {
  sitemap.write({ url: '/', changefreq: 'daily', priority: 1.0 });

  const files = readdirSync('./articles');

  files.forEach(file => {
    sitemap.write({
      url: `/articles/${file}`,
      changefreq: 'weekly',
      priority: 0.8
    });
  });

  sitemap.end();
  const data = await streamToPromise(sitemap);
  fs.writeFileSync('sitemap.xml', data.toString());
})();
