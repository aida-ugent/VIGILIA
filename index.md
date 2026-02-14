---
layout: page
title: VIGILIA
permalink: /
---

## Vigilant AI for high-stakes decisions

**VIGILIA** is an ERC Advanced Grant project led by **Prof. Tijl De Bie** at the [AIDA-IDLab research group](https://aida.ugent.be/), Ghent University. The project investigates how machine learning systems can become more reliable, transparent, and accountable in high-stakes settings.

### Project at a glance

- **Grant type:** ERC Advanced Grant
- **Project acronym:** VIGILIA
- **Grant ID:** 101142229
- **Host institution:** Ghent University
- **Research group:** AIDA-IDLab

For official administrative details, see the [CORDIS project page](https://cordis.europa.eu/project/id/101142229) and the [Ghent University research portal](https://research.ugent.be/web/result/project/7002006f-8385-4200-89ba-7a220755e2b1/details/nl).

### Objectives

VIGILIA studies principles, methods, and tools for building AI systems that can be **trusted under uncertainty**, especially when decisions affect people directly. The project focuses on:

1. Better uncertainty awareness and risk-sensitive decision support.
2. Robust learning in evolving and imperfect real-world environments.
3. Interpretable, auditable, and responsible AI workflows.

### Team

{% assign core_team = site.data.people | where_exp: 'p', 'p.role != "PI"' %}

- **Principal Investigator:** [Tijl De Bie]({{ '/people/' | relative_url }})
- **Core team members:** {% for person in core_team %}{{ person.name }}{% unless forloop.last %}, {% endunless %}{% endfor %}

➡ Visit the [People page]({{ '/people/' | relative_url }}) for photos and short bios.

### News and updates

We publish project updates in our [blog]({{ '/blog/' | relative_url }}), including events, awards, publications, and perspectives from the team.
