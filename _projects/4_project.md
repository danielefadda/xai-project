---
layout: page
title: Line 4
permalink: /research-lines/line-4
subtitle: Case studies
description: A repertoire of case studies aimed at in involving also final users
importance: 4

category: Research Line
header: main
---
<h1>{{page.subtitle}}</h1>
<div class="lead mb-5">
In recent years, the development of AI systems focused on uncovering black-box systems through a wide range of explainability methods to make users more aware of why the AI gives the suggestion.
</div>
The scientific community's interest on eXplainable Artificial Intelligence (XAI) has produced a multitude of research on computational methods to make explainability possible. Nevertheless, the attention on the final user has been studied with less effort.
This line address two main aspects:

the user’s decision-making process with the eXplainable AI systems used to support high stakes decision;
use cases to test explanation methods developed in XAI project.
Since the beginning of XAI project, we focused on mainly on the healthcare high-stakes decision. In the healthcare application domain, both AI and human doctors will have complementary roles reflecting their strengths and weaknesses. Therefore, it is of pivotal importance to develop an AI technology able to work synergistically with doctors. Current AI technologies have many shortcomings that hinder their adoption in the real world. In recent years, developing methods to explain AI models' reasoning has become the focus of many of the scientific community, particularly those in the field of eXplainable AI (XAI). While several XAI methods have been developed in the past years, only a few considered the specific application domain. Consider, for example, two of the most popular XAI methods: LIME and SHAP These two methods model-agnostic and application-agnostic, meaning that they can extract an explanation from any type of black-box AI model regardless of the application domain. While the model-agnostic approach to XAI offers great flexibility to the use of these methods, the application-agnostic approach implies that the specific user needs are not considered. A few works have tried to close such a gap in the medical field by involving the doctors in the design procedure or by performing exploratory surveys e.g. Despite these recent efforts, most of the research has been focused on laypeople

In our first work, we tested the impact of AI explanation with healthcare professionals. Specifically, the context of this work is AI-supported decision-making for clinicians. Imagine, for example, a doctor who wants to have a second opinion before making a decision about the risk of a patient’s myocardial infarction. She forms her opinion on the previous visits and symptoms of the patient and then an AI suggestion is presented to her. What happens to her when she gets a second opinion? Does she trust herself or she will be more prone to follow the algorithmic suggestion to make her final decision? To answer this question, we collected data from 36 healthcare professionals to understand the impact of advice from a clinical DSS in two different cases: the case in which the clinical DSS explains the given suggestion and the case in which it does not. We adapted the judge-advisor system framework from Sniezek & Van Swol [Sniezek2001] to evaluate participants’ trust and behavioral intention to use the system in an online estimation task. Our main measure was the Weight of Advice, a measure of the degree to which the algorithmic suggestion (with or without explanation) influences the participant’s estimate. To have more meaningful insights from the participants, we collected qualitative and quantitative measures. Our results showed that participants relied more on the condition with the explanation compared to the condition with the sole suggestion. This happened even if participants found the explanation unsatisfying. It is interesting to notice that, despite the low perceived explanation quality, participants were influenced by it and relied more on the advice of the AI system. This finding might be in line with previous research on automation bias in medicine, i.e., the tendency to over-rely on automation. From the open questions at the end of the study, healthcare professionals showed an aversion to the use of algorithmic advice and a fear of being replaced by such AI systems. The importance of these results is twofold. Firstly, even if the explanation provided left most of the participants unsatisfied, they were strongly influenced by it and relied more on the advice given by the AI with the suggestion. Secondly, the importance of the ethnographic method, i.e., the open-ended questions, to get more insights from the participants that cannot be caught only with quantitative measures.

The limitations of this study need to be found in the presentation of a decision from the AI that was always correct. In future work, we aim to carry out a similar study testing if the overreliance is still maintained even when the suggestions are wrong. In the second work we performed, we tested how users react to a wrong suggestion when they have to evaluate different types of skin lesions images. The need is to develop AI systems that can assist doctors in making more informed decisions, complementing their own knowledge with the information and suggestion yielded by the AI system [MGY2021, PPP2020]. However, if the logic for the decisions of AI systems is not available it would be impossible to accomplish this goal. Skin image classification is a typical example of this problem. Here, the explanation is formed by synthetic exemplars and counter-exemplars of skin lesions (i.e. images generated and classified with the same outcome as the initial dataset, and with an outcome other than the original dataset, correspondingly). This explanation offers the practitioner a way to highlight the crucial traits responsible for the algorithmic classification decision We conducted a validation survey with 156 domain experts, novices, and laypeople to test whether the explanation increases the reliance and the confidence in the automatic decision system. The task was organized into ten questions. Each of those questions was presented as an image of a skin lesion without any label and its explanation was generated by ABELE. The participants were shown with two exemplars, classified as the presented skin lesion, and two counter-exemplars, i.e. another lesion class. They had to classify the presented image in a binary decision task to decide whether the class of the nevus by using the presented explanation. Here, one of the main points was to see how participants regain their trust after receiving a misclassified suggestion by the AI system. The results showed a slight reduction of trust towards the black box when the presented suggestion is wrong, although there is no statistically significant drop in confidence after receiving wrong advice from an AI model. However, if we restrict our analysis to the sub-sample of medical experts, we have noticed that they are more prone to lower their confidence in the system’s advice even in the subsequent trials compared to the other participants (beginners and laypeople). This study showed how domain experts are more prone to detect and adjust their estimates when the suggestion is not correct. This aspect can be important for the role of the final users of the system. That is to say, explanation methods without a consistent validation can be not taken into account as expected by the developers of such methods. Healthcare is one of the main areas in which we have put our effort to include real participants to get an insight into the effect of AI explanations during the use of clinical assisted decision-making systems. We are focusing on how to improve the explanations in the diagnosis forecasts to inform the design of healthcare systems to promote human-AI cooperation, avoid algorithm aversion and improve the overall decision-making process.

<br>
---


## Research line people
{% assign porfiles = site.data.people %}
<div class="container-fluid">
    <div class="row">
        {% for profile in porfiles %}
            {% if profile.r4 == '1' %}
            <div class="col-md-4 col-sm-12">
                <div class="peopole">
                    <div class="card">
                        <div class="card-body">
                            {% if profile.image %}
                                {% assign profile_image_path = profile.image | prepend: '../assets/img/people_img/' %}
                                <div class="card-img"><img src="{{ profile_image_path }}"
                                                           alt="img {{ profile.lastName }}"></div>
                            {% else %}
                                <div class="card-img"><img src="../../assets/img/people_img/p_Giannotti.jpg"
                                                           alt="img {{ profile.lastName }}"></div>
                            {% endif %}
                            <div class="card-content">
                                <strong class="card-title">{{ profile.firstName }}<br>{{ profile.lastName }}
                                </strong>
                                <hr>
                                <p class="card-text">{{ profile.role }}<br><em>{{ profile.affiliation }}</em></p>
                                {% if profile.researchLine %}
                                    <hr>
                                    <p class="card-text"><strong>R.LINE {{ profile.researchLine }}</strong></p>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {% endif %}
        {% endfor %}
    </div>
</div>