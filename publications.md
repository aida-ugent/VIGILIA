---
layout: page
title: Publications
permalink: /publications/
---

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
  </div>
{% endif %}
