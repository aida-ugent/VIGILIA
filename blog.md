---
layout: page
title: Blog
permalink: /blog.html
---

{% if site.posts.size > 0 %}
<ul class="post-list">
  {% for post in site.posts %}
    <li>
      <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
      <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
      {% if post.excerpt %}
      <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
<div class="empty-state">
  <h3>News coming soon</h3>
  <p>
    We will share updates here on publications, events, talks, team milestones, and project highlights.
    Please check back soon.
  </p>
</div>
{% endif %}
