---
layout: default
title: "MagneticHub.fr"
permalink: /
---

<div class="home-container">
  <div class="header-section">
    <h1 class="site-title">Bienvenue sur MagneticHub.fr !</h1>
    <p class="site-description">Votre ressource spécialisée dans les microservices et les revenus passifs en ligne.</p>
  </div>

  <div class="content-section">
    <h2>Derniers Articles</h2>
    <div class="article-list">
      {% for post in site.posts %}
        <div class="article-item">
          <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
          <span class="post-date">{{ post.date | date: "%d/%m/%Y" }}</span>
          {% if post.excerpt %}
            <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
          {% endif %}
          <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Lire la suite →</a>
        </div>
      {% endfor %}
    </div>
  </div>

  <div class="about-section">
    <h2>À propos</h2>
    <p>MagneticHub.fr est votre source de conseils pour maximiser vos revenus passifs en ligne à travers l'utilisation des microservices et autres stratégies efficaces.</p>
    <p>N'hésitez pas à explorer notre contenu et à partager vos commentaires !</p>
  </div>
</div>
