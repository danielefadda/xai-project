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

**author: Andrea Beretta, Salvatore Rinzivillo, Fosca Giannotti**

This report presents a multidisciplinary examination of human decision-making in the era of artificial intelligence (AI), drawing on perspectives from psychology, cognitive science, and human-computer interaction (HCI). Beginning with a historical overview of decision-making theories, it traces the contributions of key scholars and frameworks that have shaped our understanding of cognitive processes. Building on this foundation, the report explores psychological insights into mental models and their impact on decision quality, offering practical strategies to improve outcomes.

A central focus is placed on HCI and its implications for decision-making. The pivotal role of algorithms is highlighted, particularly in supporting complex decision processes through user-centered design. Issues of trust in AI are analyzed, including the establishment of cognitive trust and the dynamics of mixed-initiative systems that enable effective collaboration between humans and machines. The report also addresses challenges such as algorithm aversion, overreliance, and the perception of computers as social actors, underscoring the nuanced relationship between users and intelligent systems.

In conclusion, the report synthesizes these insights to emphasize the opportunities and challenges of human-AI collaboration. It argues that understanding cognitive characteristics, psychological mechanisms, and interaction dynamics is essential for designing effective decision-support systems and fostering productive partnerships. Looking ahead, continued exploration of these themes will be critical for advancing responsible and effective decision-making practices in increasingly AI-driven contexts. By adopting a cognitive and multidisciplinary approach, the report offers a roadmap for future research and development in human-AI collaboration.

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


## TR3. Collaboration between Banca Intesa Sanpaolo and Scuola Normale Superiore: a technical report

**authors: Francesca Naretto, Andrea Beretta, Michele Fontana, Fosca Giannotti**

This report summarizes a collaboration between Scuola Normale Superiore and Banca Intesa Sanpaolo to improve the explainability of the bank’s Salesforce-based AI system for product recommendations. The study has two stages. First, a focus group with Relationship Managers and Area Coordinators examines current practice, needs, and pain points. Participants value the tool but judge its explanations as generic and often unhelpful; they request clearer, multi-level justifications, examples of similar clients, and explanatory narratives they can use in client conversations. Second, we validate three explainers for tabular models (LIME, SHAP, and LORE) on three anonymized financial datasets (garanzie, impieghi, incassi) using fidelity, faithfulness, and monotonicity. All methods reach high fidelity; differences emerge on faithfulness, where LORE performs best and with lower variance. However, LORE’s exemplars and counter-exemplars are synthetic, which reduces credibility for end users in this internal setting. We hence explore a tailored strategy that retrieves real exemplars from the training data when privacy constraints permit, falling back to synthetic ones otherwise. The initial results are promising, but presentation remains too technical for non-experts. Overall, the findings indicate that combining stronger faithfulness with user-oriented, multi-level explanations and realistic exemplars is key to making the widget actionable for Relationship Managers.

published: October 2023

<div class="alert alert-warning" role="alert">
Write an email to <strong>Francesca Naretto</strong> for the full technical report
</div>


---

## TR4. Towards Hybrid Decision making

**author: Clara Punzi, Roberto Pellungrini, Mattia Setzu, Fosca Giannotti, Dino Pedreschi**

Everyday we increasingly rely on machine learning models to automate and support high-stake tasks and decisions. This growing presence means that humans are now constantly interacting with machine learning-based systems, training and using models everyday. Several different techniques in computer science literature account for the human interaction with machine learning systems, but their classification is sparse and the goals varied. This survey proposes a taxonomy of Hybrid Decision Making Systems, providing both a conceptual and technical framework for understanding how current computer science literature models interaction between humans and machines.

published: February 2024

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