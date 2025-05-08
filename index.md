---
layout: default
title: Bienvenue sur MagneticHub.fr
---

# Bienvenue !

Découvrez nos derniers articles :

<ul>
  {% for article in site.pages %}
    {% if article.url contains '/articles/' %}
      <li><a href="{{ article.url }}">{{ article.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
