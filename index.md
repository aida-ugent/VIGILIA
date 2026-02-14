---
layout: page
title: VIGILIA
permalink: /
---

## VIGILIA

**VIGILIA** is an ERC Advanced Grant project led by **Prof. Tijl De Bie** at Ghent University, embedded in the [AIDA-IDLab research group](https://aida.ugent.be/).

### Project information

- **Grant type:** ERC Advanced Grant
- **Project acronym:** VIGILIA
- **Grant agreement ID:** 101142229
- **Host institution:** Ghent University
- **Start date:** 1 October 2024
- **End date:** 30 September 2029

For official project information and administrative details, see:

- [CORDIS project page](https://cordis.europa.eu/project/id/101142229)
- [Ghent University research portal](https://research.ugent.be/web/result/project/7002006f-8385-4200-89ba-7a220755e2b1/details/nl)

### Team

{% assign core_team = site.data.people | where_exp: 'p', 'p.role != "PI"' | sort: 'name' %}

- **Principal Investigator:** [Tijl De Bie]({{ '/people/' | relative_url }})
- **Core team members:** {% for person in core_team %}{{ person.name }}{% unless forloop.last %}, {% endunless %}{% endfor %}

➡ Visit the [People page]({{ '/people/' | relative_url }}) for profiles and photos.

### News

See the [blog]({{ '/blog/' | relative_url }}) for events, publications, talks, awards, and other project updates.
