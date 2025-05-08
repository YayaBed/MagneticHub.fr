---
title: Bienvenue sur MagneticHub.fr
layout: default
---

# Bienvenue !

## Articles publiés

{% for file in site.pages %}
  {% if file.path contains 'articles/' and file.extname == '.md' %}
- [{{ file.title | default: file.name }}]({{ file.url }})
  {% endif %}
{% endfor %}
