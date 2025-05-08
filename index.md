---
layout: default
title: "MagneticHub.fr"
permalink: /
---

# Bienvenue sur MagneticHub.fr !

Bienvenue sur notre blog dédié aux microservices et aux revenus passifs en ligne. Découvrez nos derniers articles ci-dessous.

## Derniers Articles

<div class="posts-list">
  {% for post in site.posts %}
    <div class="post-item">
      <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
      <span class="post-date">{{ post.date | date: "%d/%m/%Y" }}</span>
      {% if post.excerpt %}
        <p>{{ post.excerpt }}</p>
      {% endif %}
      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Lire la suite →</a>
    </div>
  {% endfor %}
</div>

## À propos

MagneticHub.fr est votre source de conseils pour maximiser vos revenus passifs en ligne à travers l'utilisation des microservices et autres stratégies efficaces.

N'hésitez pas à explorer notre contenu et à partager vos commentaires !
