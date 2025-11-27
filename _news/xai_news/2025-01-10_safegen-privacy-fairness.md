---
layout: article
date: '2025-01-10 00:00:00-0000'
inline: False
onlylink: False
related_posts: false
categories: 'Publication'
permalink: '/news/safegen-privacy-fairness-machine-learning'
title: 'SafeGen: Integrating Privacy and Fairness in Machine Learning'
thumb: '/assets/img/news/safeGen.webp'
---

A new contribution from the XAI project published in *Machine Learning* (Springer) introduces SafeGen {% cite CMM2025 %}, a preprocessing method that simultaneously addresses privacy and fairness in tabular data.

The research demonstrates that separately optimizing privacy and fairness can lead to undesirable conflicts: privacy preservation techniques can worsen fairness and vice versa. SafeGen uses a genetic algorithm to generate synthetic data that maintains the necessary statistical properties while protecting sensitive attributes.

Experiments show that SafeGen achieves robust anonymization while preserving or improving dataset fairness, demonstrating the importance of integrated approaches when multiple ethical objectives must be met simultaneously.

---

## References
<div class="publications">
{% bibliography --cited %}
</div>
