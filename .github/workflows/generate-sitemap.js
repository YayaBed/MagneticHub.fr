const fs = require('fs');
const path = require('path');

// Répertoire des pages HTML (dossier racine du projet GitHub Pages)
const baseDir = path.join(__dirname, 'dist'); // remplace par '.' si à la racine
const baseUrl = 'https://yayabed.github.io/MagneticHub.fr';

const getAllHtmlFiles = (dir, fileList = []) => {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory()) {
      getAllHtmlFiles(fullPath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(fullPath);
    }
  });
  return fileList;
};

const formatDate = () => {
  return new Date().toISOString();
};

const generateSitemap = () => {
  const pages = getAllHtmlFiles(baseDir);
  const urls = pages.map(pagePath => {
    const relativePath = path.relative(baseDir, pagePath).replace(/\\/g, '/');
    const loc = `${baseUrl}/${relativePath}`.replace(/index\.html$/, '');
    return `
  <url>
    <loc>${loc}</loc>
    <lastmod>${formatDate()}</lastmod>
    <priority>0.80</priority>
  </url>`;
  });

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>  
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.join('\n')}
</urlset>`;

  fs.writeFileSync(path.join(baseDir, 'sitemap.xml'), sitemap, 'utf8');
  console.log('✅ Sitemap généré avec succès.');
};

generateSitemap();
