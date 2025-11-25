---
layout: page
title: Repositories
permalink: /repositories/
description: The following repositories are related to the projects we are working on
horizontal: true
header: main
---

{% if site.data.repositories.github_repos %}

{% comment %}
Check if Vercel API is available by trying to load a test image
If it fails, fallback to official GitHub badges
{% endcomment %}

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const testImg = new Image();
    const timeout = setTimeout(function() {
      // Timeout after 3 seconds - use official badges
      document.body.classList.add('use-official-badges');
    }, 3000);
    
    testImg.onload = function() {
      clearTimeout(timeout);
      // Vercel API works - keep using it
    };
    
    testImg.onerror = function() {
      clearTimeout(timeout);
      // Vercel API failed - switch to official badges
      document.body.classList.add('use-official-badges');
    };
    
    testImg.src = 'https://github-readme-stats.vercel.app/api/pin/?username=kdd-lab&repo=LORE_sa&theme={{ site.repo_theme_light }}&show_owner=true&_t=' + Date.now();
  });
</script>

<div class="repositories">
    {% for repo in site.data.repositories.github_repos %}
        <div class="repo-wrapper">
            <div class="repo-vercel">
                {% include repository/repo.liquid repository=repo %}
            </div>
            <div class="repo-official" style="display: none;">
                {% include repository/repo_official.liquid repository=repo %}
            </div>
        </div>
    {% endfor %}
</div>

<style>
  .repositories {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 1rem 0;
  }
  
  @media (max-width: 768px) {
    .repositories {
      grid-template-columns: 1fr;
    }
  }
  
  .use-official-badges .repo-vercel {
    display: none !important;
  }
  .use-official-badges .repo-official {
    display: block !important;
  }
  
  .repo-wrapper {
    width: 100%;
  }
  
  .repo-card {
    border: 1px solid var(--global-divider-color);
    border-radius: 8px;
    padding: 1rem;
    background: var(--global-bg-color);
    transition: transform 0.2s, box-shadow 0.2s;
    width: 100%;
    max-width: 400px;
    margin: 0 auto;
  }
  
  .repo-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  .repo-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
    font-weight: 600;
    color: var(--global-text-color);
  }
  
  .repo-icon {
    flex-shrink: 0;
  }
  
  .repo-name {
    font-size: 1rem;
    word-break: break-word;
  }
  
  .repo-badges {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
  }
  
  .repo-badges img {
    justify-self: center;
  }
  
  .repo-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
  }
  
  .repo-stats img {
    justify-self: center;
  }
  
  .repo-link {
    text-decoration: none;
  }
</style>

{% endif %}