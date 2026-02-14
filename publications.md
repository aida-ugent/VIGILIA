---
layout: page
title: Publications
permalink: /publications/
---

This page is automatically synchronized with UGent biblio records for ERC Advanced Grant **VIGILIA (101142229)**.
The cache file (`_data/publications.yml`) is refreshed by CI on a schedule via `scripts/fetch_biblio_publications.py`, so no manual list maintenance is required.

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
    <p>When entries are indexed in UGent biblio with VIGILIA-linked metadata or matching project identifiers, they are picked up automatically during the next sync run.</p>
  </div>
{% endif %}
