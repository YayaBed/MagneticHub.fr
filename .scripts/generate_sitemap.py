import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Configuration
REPO_OWNER = "YayaBed"
REPO_NAME = "MagneticHub.fr"
BRANCH = "main"
ARTICLES_DIR = "articles"
BASE_URL = "https://yayabed.github.io/MagneticHub.fr"
SITEMAP_FILE = "sitemap.xml"

def get_github_file_list():
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{ARTICLES_DIR}?ref={BRANCH}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Erreur de récupération des fichiers depuis GitHub API: {response.status_code}")
    return response.json()

def generate_sitemap(entries):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for entry in entries:
        if entry["name"].endswith(".md"):
            slug = entry["name"].replace(".md", "")
            url = f"{BASE_URL}/{slug}.html"  # suppose que GitHub Pages rend les .md en .html
            url_el = ET.SubElement(urlset, "url")
            ET.SubElement(url_el, "loc").text = url
            ET.SubElement(url_el, "lastmod").text = datetime.utcnow().date().isoformat()
            ET.SubElement(url_el, "changefreq").text = "weekly"
            ET.SubElement(url_el, "priority").text = "0.8"
    return ET.tostring(urlset, encoding="utf-8", xml_declaration=True).decode("utf-8")

def save_sitemap(xml_content):
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"✅ sitemap.xml mis à jour avec {xml_content.count('<url>')} URLs.")

if __name__ == "__main__":
    files = get_github_file_list()
    sitemap_xml = generate_sitemap(files)
    save_sitemap(sitemap_xml)
