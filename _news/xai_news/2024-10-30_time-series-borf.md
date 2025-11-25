---
layout: article
date: '2024-10-30 00:00:00-0000'
inline: False
onlylink: False
related_posts: false
categories: 'Publication'
permalink: '/news/borf-interpretable-time-series-classification'
title: 'BORF: Trasformazione Interpretabile per Serie Temporali'
thumb: '/assets/img/news/borf-2024.jpg'
---

New research from the XAI project, published in *IEEE Access*, introduces the Bag-Of-Receptive-Fields (BORF) {% cite SGB2024 %}, a fast, interpretable, and deterministic transformation for time series.

The current trend in time series classification is the development of highly accurate but black-box algorithms. BORF bridges the gap between convolutional operators and discretization, improving Symbolic Aggregate Approximation (SAX) with dilation and stride to better capture temporal patterns at multiple scales.

The proposed method includes an algorithmic speedup that reduces the temporal complexity associated with SAX-based classifiers, enabling a more flexible representation as a sparse multivariate tensor. Experiments demonstrate that BORF maintains high accuracy while remaining fully interpretable and deterministic.

---

## References
<div class="publications">
{% bibliography --cited %}
</div>
