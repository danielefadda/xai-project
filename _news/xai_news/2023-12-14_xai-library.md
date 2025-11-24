---
layout: article
date: '2023-12-14 00:00:00-0000'
event-date: '2023-12-14 00:00:00-0000'
inline: False
onlylink: False
related_posts: false
categories: 'Project Resources'
permalink: '/news/Xai Library'
title: 'XAI-Lib: Unified Library for Explainable AI'
thumb: '/assets/img/xai_lib_logo.png'
link: 'https://github.com/kdd-lab/XAI-Lib'
repository: 'kdd-lab/XAI-Lib'
---

**An integrated Python library for Explainable AI with a unified interface for various explanation methods!**

### What is XAI-Lib?

XAI-Lib is an integrated Python library for Explainable AI (XAI) that provides a unified interface for various explanation methods. Developed as part of the **Xai Project**, XAI-Lib simplifies the process of explaining black-box models across different data types, making machine learning models more interpretable and transparent.

{% include repository/repo.liquid repository='kdd-lab/XAI-Lib' %}

### Key Features

XAI-Lib is designed to be modular, extensible, and easy to use:

- **Unified Interface**: Simple, consistent API for multiple explanation methods
- **Multiple Data Types**: Support for tabular, image, text, and time-series data
- **Extensible Architecture**: Easy integration of new explanation methods
- **Model-Agnostic**: Works with any black-box machine learning model
- **Well-Documented**: Comprehensive documentation and examples

### Supported Explanation Methods

**For Tabular Data:**

- **SHAP** - SHapley Additive exPlanations
- **LIME** - Local Interpretable Model-agnostic Explanations
- **Anchors** - High-precision model-agnostic explanations
- **LORE** - LOcal Rule-based Explanations

**For Image Data:**

- **GradCAM** - Gradient-weighted Class Activation Mapping
- **LIME** - Local Interpretable Model-agnostic Explanations
- **SHAP** - SHapley Additive exPlanations
- **ABELE** - Adversarial Black-box Explainer generating Latent Exemplars

**For Text and Time Series Data:**

- Work in Progress - Coming soon!

### Installation

The easiest way to install XAI-Lib is using pip:

```bash
pip install XAI-Library
```

For the latest development version, clone the repository and install in editable mode:

```bash
git clone https://github.com/kdd-lab/XAI-Lib.git
cd XAI-Lib
pip install -e .
```

### Quick Start

Here's a simple example of using LIME for tabular data explanation:

```python
from xailib import Explainer

# Initialize your black-box model
# model = YourModel()

# Create an explainer
explainer = Explainer(model, method='lime')

# Generate explanation for a sample
explanation = explainer.explain(sample_data)

# Visualize the explanation
explainer.visualize(explanation)
```

For more examples and detailed usage, please check the [examples/](https://github.com/kdd-lab/XAI-Lib/tree/main/examples) directory.

### Documentation

Complete documentation, tutorials, and API reference are available at:

- **GitHub Repository**: [https://github.com/kdd-lab/XAI-Lib](https://github.com/kdd-lab/XAI-Lib)
- **Issue Tracker**: [https://github.com/kdd-lab/XAI-Lib/issues](https://github.com/kdd-lab/XAI-Lib/issues)

### Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/kdd-lab/XAI-Lib/blob/main/CONTRIBUTING.rst) for details on how to:

- Report bugs and request features
- Submit pull requests
- Improve documentation
- Add new explanation methods

### Contact

For questions and support:

- **Email**: [rinzivillo@isti.cnr.it](mailto:rinzivillo@isti.cnr.it)
- **Issue Tracker**: [https://github.com/kdd-lab/XAI-Lib/issues](https://github.com/kdd-lab/XAI-Lib/issues)

---
