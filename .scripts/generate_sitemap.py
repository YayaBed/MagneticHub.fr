import os
from datetime import datetime
from urllib.parse import quote

# Configuration
BASE_URL = "https://yayabed.github.io/MagneticHub.fr"  # Remplace par ton vrai domaine
ARTICLES_DIR = "articles"             # Ton répertoire d'articles
SITEMAP_PATH = "sitemap.xml"

def get_articles():
    articles = []
    for filename in os.listdir(ARTICLES_DIR):
        if filename.endswith(".md") or filename.endswith(".markdown"):
            slug = os.path.splitext(filename)[0]
            url = f"{BASE_URL}/{quote(slug)}"
            lastmod = datetime.utcnow().date().isoformat()
            articles.append((url, lastmod))
    return articles

def generate_sitemap(articles):
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url, lastmod in articles:
        sitemap.append("  <url>")
        sitemap.append(f"    <loc>{url}</loc>")
        sitemap.append(f"    <lastmod>{lastmod}</lastmod>")
        sitemap.append("    <changefreq>weekly</changefreq>")
        sitemap.append("    <priority>0.8</priority>")
        sitemap.append("  </url>")
    sitemap.append("</urlset>")
    return "\n".join(sitemap)

def save_sitemap(content):
    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Sitemap généré avec {len(content.splitlines())} lignes.")

if __name__ == "__main__":
    articles = get_articles()
    sitemap_content = generate_sitemap(articles)
    save_sitemap(sitemap_content)
