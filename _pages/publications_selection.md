---
layout: page
title: Selected Publications
permalink: /publications_selection/
description: A list of selected publications from our research
horizontal: true
header: main
selected_papers: true
---

This section presents the **most significant scientific publications** produced within the ERC XAI project. The works listed here have been selected for their **strategic importance and foundational impact** on the project's research lines. They represent the main **contributions** to the development of **Explainable Artificial Intelligence (XAI)** methodologies and algorithms. The selection covers key progress across our research areas (RA1-RA5), with a particular focus on the impact in critical sectors such as healthcare, finance, and mobility, outlining our vision for a more **transparent and trustworthy AI**.

{% if page.selected_papers %}

<div class="container my-5">

<div class="publications">
{% bibliography --query @*[selected~=true] %}
</div>

</div>

{% endif %}