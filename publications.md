---
layout: page
title: Publications
permalink: /publications/
---

This page lists publications acknowledging ERC Advanced Grant **VIGILIA (101142229)**.
Data is maintained in `_data/publications.yml` and can be refreshed automatically using `scripts/fetch_biblio_publications.py`.

{% assign pubs = site.data.publications | sort: 'year' | reverse %}

{% if pubs and pubs.size > 0 %}
  {% for pub in pubs %}
  <article class="pub-item">
    <h3>
      {% if pub.url %}
      <a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a>
      {% else %}
      {{ pub.title }}
      {% endif %}
    </h3>
    <p>
      <strong>{{ pub.authors }}</strong><br/>
      {{ pub.venue }}{% if pub.year %}, {{ pub.year }}{% endif %}
    </p>
  </article>
  {% endfor %}
{% else %}
  <div class="empty-state">
    <h3>No publications listed yet</h3>
    <p>Once publications are indexed in the Ghent University biblio database with VIGILIA funding acknowledgement, they will appear here.</p>
  </div>
{% endif %}
