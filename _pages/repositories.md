---
layout: page
permalink: /resources/
title: Selected resources
description:
nav: true
nav_order: 5
header: main
---

## Repositories

{% if site.data.repositories.github_repos %}

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}


{% if site.display_tags or site.display_categories %}
    <div class="tag-category-list">
        <ul class="p-0 m-0">
            {% for tag in site.display_tags %}
                <li>
                    <i class="fa-solid fa-hashtag fa-sm"></i>
                    <a href="{{ tag | slugify | prepend: '/blog/tag/' | relative_url }}">{{ tag }}</a>
                </li>
                {% unless forloop.last %}
                    <p>&bull;</p>
                {% endunless %}
            {% endfor %}
            {% if site.display_categories.size > 0 and site.display_tags.size > 0 %}
                <p>&bull;</p>
            {% endif %}
            {% for category in site.display_categories %}
                <li>
                    <i class="fa-solid fa-tag fa-sm"></i>
                    <a href="{{ category | slugify | prepend: '/blog/category/' | relative_url }}">{{ category }}</a>
                </li>
                {% unless forloop.last %}
                    <p>&bull;</p>
                {% endunless %}
            {% endfor %}
        </ul>
    </div>
{% endif %}

{% assign featured_posts = site.posts | where: "featured", "true" %}
{% if featured_posts.size > 0 %}
    <br>
    <div class="container featured-posts">
        {% assign is_even = featured_posts.size | modulo: 2 %}
        <div class="row row-cols-{% if featured_posts.size <= 2 or is_even == 0 %}2{% else %}3{% endif %}">
            {% for post in featured_posts %}
                <div class="col mb-4">
                    <a href="{{ post.url | relative_url }}">
                        <div class="card hoverable">
                            <div class="row g-0">
                                <div class="col-md-12">
                                    <div class="card-body">
                                        <div class="float-right">
                                            <i class="fa-solid fa-thumbtack fa-xs"></i>
                                        </div>
                                        <h5 class="card-title text-lowercase">{{ post.title }}</h5>
                                        <p class="card-text">{{ post.description }}</p>

                                        {% if post.external_source == blank %}
                                            {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
                                        {% else %}
                                            {% assign read_time = post.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
                                        {% endif %}
                                        {% assign year = post.date | date: "%Y" %}

                                        <p class="post-meta">
                                            {{ read_time }} min read &nbsp; &middot; &nbsp;
                                            <a href="{{ year | prepend: '/blog/' | prepend: site.baseurl }}">
                                                <i class="fa-solid fa-calendar fa-sm"></i> {{ year }} </a>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            {% endfor %}
        </div>
    </div>
    <hr>

{% endif %}