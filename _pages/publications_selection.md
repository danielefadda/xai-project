---
layout: page
title: Selected Publications
permalink: /publications_selection/
description: A list of selected publications from our research
horizontal: true
header: main
---

{% if page.selected_papers %}
    <div class="container my-5">
        <h2>
            <a href="{{ '/publications/' | relative_url }}"
               style="color: inherit">selected publications</a>
        </h2>
        <div class="publications">
            {% bibliography --group_by none --query @*[visible_on_site = true]* %}
        </div>
    </div>
{% endif %}