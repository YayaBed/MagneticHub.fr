---
layout: default
title: "MagneticHub.fr"
---

# Bienvenue sur MagneticHub.fr !

Bienvenue sur notre blog dédié aux microservices et aux revenus passifs en ligne.  
Voici la liste de tous les articles publiés :

<ul>
  {% assign pages_sorted = site.pages | where_exp: "page", "page.path contains 'articles/'" %}
  {% for page in pages_sorted %}
    <li><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name }}</a></li>
  {% endfor %}
</ul>
