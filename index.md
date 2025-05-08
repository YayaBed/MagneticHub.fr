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
    <h2>Nos Articles</h2>
    <div class="article-list">
      {% assign sorted_articles = site.articles | sort: "date" | reverse %}
      {% for article in sorted_articles %}
        <div class="article-item">
          <h3><a href="{{ site.baseurl }}{{ article.url }}">{{ article.title }}</a></h3>
          {% if article.date %}
            <span class="post-date">{{ article.date | date: "%d/%m/%Y" }}</span>
          {% endif %}
          {% if article.excerpt %}
            <p>{{ article.excerpt | strip_html | truncatewords: 30 }}</p>
          {% endif %}
          <a href="{{ site.baseurl }}{{ article.url }}" class="read-more">Lire la suite →</a>
        </div>
      {% else %}
        <p>Aucun article trouvé dans la collection. Consultez le dossier /articles de votre dépôt.</p>
        
        <!-- Affichage du débogage -->
        <div class="debug-info">
          <p>Informations de débogage :</p>
          <ul>
            <li>Nombre d'articles dans site.articles : {{ site.articles.size }}</li>
            <li>Collections disponibles : 
              {% for collection in site.collections %}
                {{ collection.label }}{% unless forloop.last %}, {% endunless %}
              {% endfor %}
            </li>
            <li>Site URL: {{ site.url }}</li>
            <li>Base URL: {{ site.baseurl }}</li>
          </ul>
        </div>
      {% endfor %}
    </div>
  </div>

  <div class="about-section">
    <h2>À propos</h2>
    <p>MagneticHub.fr est votre source de conseils pour maximiser vos revenus passifs en ligne à travers l'utilisation des microservices et autres stratégies efficaces.</p>
    <p>N'hésitez pas à explorer notre contenu et à partager vos commentaires !</p>
    <p><a href="{{ site.baseurl }}/about/" class="read-more">En savoir plus sur nous →</a></p>
  </div>
</div>
