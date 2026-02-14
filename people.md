---
layout: page
title: People
permalink: /people/
---

> Team photos currently use local placeholders in this repository. Replace image files in `assets/img/` with official AIDA profile photos to publish the final version.

<div class="people-grid">
  {% for person in site.data.people %}
    <article class="person-card">
      <img src="{{ person.image | relative_url }}" alt="Portrait of {{ person.name }}" class="person-photo" />
      <h3>{{ person.name }}</h3>
      <p class="person-role">{{ person.role }}</p>
      <p><strong>{{ person.title }}</strong></p>
      <p>{{ person.bio }}</p>
      <p><a href="{{ person.profile_url }}" target="_blank" rel="noopener">Profile</a></p>
    </article>
  {% endfor %}
</div>
