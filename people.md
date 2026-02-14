---
layout: page
title: People
permalink: /people/
---

## Principal Investigator

### Tijl De Bie (PI)

Tijl De Bie is Professor of AI and Data Mining at Ghent University and a core member of the AIDA-IDLab research group. His work focuses on machine learning, data mining, and trustworthy AI. He leads the ERC Advanced Grant project **VIGILIA**.

**Very brief CV (selected):**
- Professor at Ghent University (IDLab / AIDA).
- Internationally recognized researcher in machine learning and data mining.
- Principal Investigator of ERC Advanced Grant VIGILIA.

---

## VIGILIA team

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
