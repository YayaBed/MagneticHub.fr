import os
from urllib.parse import urljoin

# Configuration
base_url = "https://yayabed.github.io/MagneticHub.fr/"
site_root = "PATH_VERS_DOSSIER_LOCAL_DU_SITE"  # Remplace par ton dossier local

# Fichier de sortie
sitemap_file = "sitemap.xml"

urls = []

# Explorer tous les fichiers .html
for root, _, files in os.walk(site_root):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            relative_path = os.path.relpath(filepath, site_root).replace("\\", "/")
            url = urljoin(base_url, relative_path)
            urls.append(url)

# Génération du fichier sitemap
with open(sitemap_file, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in urls:
        f.write("  <url>\n")
        f.write(f"    <loc>{url}</loc>\n")
        f.write("    <changefreq>monthly</changefreq>\n")
        f.write("    <priority>0.8</priority>\n")
        f.write("  </url>\n")
    f.write("</urlset>\n")

print(f"✅ Sitemap généré avec {len(urls)} pages dans {sitemap_file}")
