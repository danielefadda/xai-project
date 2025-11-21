---
layout: page
title: Technical Reports
permalink: /technical-reports/
importance: 1
category: Technical Report
related_publications: false
header: main
toc:
  sidebar: left
---

<style>
/* Reduce all h2 size on this page */
h2 {
  font-size: 1.4rem;
  line-height: 1.3;
  font-weight: 600;
}
</style>


<h1>{{page.subtitle}}</h1>
<div class="lead mb-5">
This section presents the technical reports developed within the European XAI project, covering cognitive, healthcare, financial, and hybrid perspectives on algorithm-supported decision making. The reports illustrate the methodologies adopted, the experiments conducted with industrial partners, and the key findings that emerged from these thematic activities.
</div>


## TR1. Human decision-making with AI systems: A cognitive perspective 

**author: Andrea Beretta**

This technical report examines the intricate relationship between human decision-making and AI systems from a cognitive perspective. By drawing insights from decision-making research, psychology, and human-computer interaction (HCI), I aim to provide a comprehensive understanding of the challenges and opportunities that arise when humans interact with AI systems in decision-making contexts.

The report begins with an exploration of the historical foundations of decision-making theories, including the normative approach, game theory, behavioral decision-making, and naturalistic decision making. These theories provide a solid framework for understanding the various approaches and perspectives in decision-making research.

Building upon this foundation, I delve into the realm of psychology and examine the cognitive aspects of decision-making. Mental models, cognitive processes, and the characteristics that influence rational decision-making styles are explored. I also address the cognitive processes that can lead to decision errors and present strategies for improving decision quality.

The report then shifts its focus to the field of HCI and its implications for decision-making. I highlight the pervasive roles of algorithms in supporting decision-making processes and the importance of algorithm-based applications in enhancing decision outcomes. User-centered design principles and the concept of computers as social actors are discussed, shedding light on the unique dynamics that occur when humans interact with AI systems. The phenomena of algorithm aversion, algorithm overreliance, and the role of trust in automation are also examined.

In conclusion, this technical report presents a multidisciplinary perspective on human decision-making with AI systems. By integrating knowledge from decision-making research, psychology, HCI, and design, I provide insights into the cognitive factors, psychological insights, and HCI considerations that influence decision-making processes. The report concludes with key takeaways and implications for future research, emphasizing the importance of user-centered design, ethical considerations, and collaboration between disciplines to ensure effective and responsible human decision-making in the era of AI systems.

*published: October 2023*

<div class="alert alert-warning" role="alert">
Write an email to <strong>Andrea Beretta</strong> for the full technical report
</div>

---

## TR2. Towards transparent healthcare: advancing local explanation methods in explainable artificial intelligence

**authors: C Metta, A Beretta, R Pellungrini, S Rinzivillo, F Giannotti**

This report focuses on the use of local Explainable Artificial Intelligence (XAI) methods, particularly the Local Rule-Based Explanations (LORE) technique, within healthcare and medical settings. It emphasizes the critical role of interpretability and transparency in AI systems for diagnosing diseases, predicting patient outcomes, and
creating personalized treatment plans. While acknowledging the complexities and inherent trade-offs between interpretability and model performance, our work underscores the significance of local XAI methods in enhancing decision-making processes in healthcare. By providing granular, case-specific insights, local XAI methods like LORE enhance
physicians’ and patients’ understanding of machine learning models and their outcome. Our paper reviews significant contributions to local XAI in healthcare, highlighting its potential to improve clinical decision making, ensure fairness, and comply with regulatory standards.

published: April 2024

<div class="alert alert-warning" role="alert">
Write an email to <strong>Carlo Metta</strong> for the full technical report
</div>


---


## TR3. XAI use case on Finance, 

**authors: Francesca Naretto et al.**

Abstract Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista probare, quae sunt a te dicta? Quid de Platone aut de Democrito loquar? Quis est tam dissimile homini. Duo Reges: constructio interrete. At iam decimum annum in spelunca iacet. Quid de Platone aut de Democrito loquar? Quis est tam dissimile homini. Duo Reges: constructio interrete. At iam decimum annum in spelunca iacet.

<div class="alert alert-warning" role="alert">
Write an email to <strong>Francesca Naretto</strong> for the full technical report
</div>


---

## TR4. Towards Hybrid Decision making

**author: Roberto Pellungrini et al.**

Abstract Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonne merninisti licere mihi ista probare, quae sunt a te dicta? Quid de Platone aut de Democrito loquar? Quis est tam dissimile homini. Duo Reges: constructio interrete. At iam decimum annum in spelunca iacet. Quid de Platone aut de Democrito loquar? Quis est tam dissimile homini. Duo Reges: constructio interrete. At iam decimum annum in spelunca iacet.

<div class="alert alert-warning" role="alert">
Write an email to <strong>Roberto Pellungrini</strong> for the full technical report
</div>

---



## TR5. A simulation framework to assess the impacts of recommender systems on purchase dynamics

**author: Margherita Lalli**

Recommender systems have become a pervasive form of algorithmic mediation, shaping individual decisions and collective dynamics across digital ecosystems—from online retail to social media. Despite their predictive success, their black-box nature obscures both their internal logic and their long-term systemic effects. This opacity is deepened by a fundamental recursive process: recommender systems do not merely influence users but are continually shaped by them through the data feedback loop that connects model outputs and user behavior. Understanding these coevolutionary dynamics requires moving beyond static evaluation toward mechanistic explanations of how human–AI interactions evolve over time. This project addresses that challenge by introducing a simulation framework that enables the experimental study of recommender-driven feedback loops under controlled conditions. The framework models an online-retail-like environment where user–item interactions evolve as recommender systems are periodically retrained on the data they generate. By incorporating a “null” baseline, representing a world without algorithmic personalization, it supports systematic comparison across algorithms and isolates the mechanisms driving emergent systemic effects. Building on real data gathered from an open sample of Amazon log-data, we examined phenomena such as demand concentration, purchase diversity, and behavioral homogenization. Our results confirm a nuanced interplay between individual and collective outcomes: while personalization can diversify individual consumption, it often amplifies global concentration and popularity biases. These findings advance a mechanistic understanding of the human–AI coevolution underlying recommender systems, bridging theoretical insights on feedback dynamics with a principled experimental methodology for studying their long-term societal impact.

*published: October 2025*


<div class="alert alert-warning" role="alert">
Write an email to <strong>Margherita Lalli</strong> for the full technical report
</div>


---

## TR6. Interpretable-by-Design Models for Business Networks

**author: Marzio di Vece**

This report develops interpretable-by-design models for business networks by combining conditional (hurdle-type) specifications with maximum-entropy ensembles. On the estimation side, we embed deterministic, annealed, and quenched recipes in a unified Kull-back–Leibler program and characterize when they coincide or diverge. Annealed estimation, based on a generalized likelihood averaged over a calibrated binary ensemble, emerges as the preferred default: it is unbiased by construction, numerically convenient, and preserves a stable mapping between parameters and economic mechanisms, whereas deterministic and quenched estimators can drift or destabilize, especially in sparse networks.
On the structural side, we analyze a 187-layer Dutch Production Multiplex and test whether binary and weighted triadic motifs are already explained once degree, strength, and
reciprocity constraints are enforced. A reciprocity-aware benchmark (RBCM + CRWCM) reproduces most triadic counts and monetary loads, revealing that many apparent motifs in
aggregated views are artifacts of ignoring directionality or product specificity. When deviations persist, they admit clear business interpretations: for instance, concentration of commodity-specific monetary flux on open-V patterns highlights vulnerability to supply shocks. Together with the open-source NuMeTriS package, these results deliver a compact,
auditable toolkit for reconstruction, uncertainty quantification, and motif-based outlier detection in production, trade, and payment networks.

*published: October 2025*


<div class="alert alert-warning" role="alert">
Write an email to <strong>Marzio di Vece</strong> for the full technical report
</div>