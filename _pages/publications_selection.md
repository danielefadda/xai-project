---
layout: page
title: Selected Publications
permalink: /publications_selection/
description: A list of selected publications from our research
horizontal: true
header: main
selected_papers: true
---

{% if page.selected_papers %}

<div class="container my-5">

<div class="publications">
{% bibliography --query @*[selected~=true] %}
</div>

</div>

{% endif %}