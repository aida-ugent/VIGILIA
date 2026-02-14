---
layout: page
title: People
permalink: /people/
---

## VIGILIA team

<div class="people-grid">
  {% assign sorted_people = site.data.people | sort: 'last_name' %}
  {% for person in sorted_people %}
    <article class="person-card">
      <img src="{{ person.image }}" alt="Portrait of {{ person.name }}" class="person-photo" />
      <h3>{{ person.name }}</h3>
      <p class="person-role">{{ person.role }}</p>
      <p><strong>{{ person.title }}</strong></p>
      <p>{{ person.bio }}</p>
      <p><a href="{{ person.profile_url }}" target="_blank" rel="noopener">Profile</a></p>
    </article>
  {% endfor %}
</div>
