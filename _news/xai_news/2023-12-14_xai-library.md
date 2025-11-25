---
layout: article
date: '2023-12-14 00:00:00-0000'
inline: False
onlylink: False
related_posts: false
categories: 'Project Resources'
permalink: '/news/Xai_Library'
title: 'XAILib: Unified Library for Explainable AI'
thumb: '/assets/img/xai_lib_logo.png'
link: 'https://github.com/kdd-lab/XAI-Lib'
repository: 'kdd-lab/XAI-Lib'
---

**An integrated Python library for Explainable AI with a unified interface for various explanation methods!**

### What is XAI-Lib?

XAI-Lib is an integrated Python library for Explainable AI (XAI) that provides a unified interface for various explanation methods. Developed as part of the **Xai Project**, XAI-Lib simplifies the process of explaining black-box models across different data types, making machine learning models more interpretable and transparent.

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const testImg = new Image();
    const repoContainer = document.getElementById('xailib-repo-badge');
    const timeout = setTimeout(function() {
      repoContainer.classList.add('use-official-badges');
    }, 3000);
    
    testImg.onload = function() {
      clearTimeout(timeout);
    };
    
    testImg.onerror = function() {
      clearTimeout(timeout);
      repoContainer.classList.add('use-official-badges');
    };
    
    testImg.src = 'https://github-readme-stats.vercel.app/api/pin/?username=kdd-lab&repo=XAI-Lib&theme=default&show_owner=true&_t=' + Date.now();
  });
</script>

<div id="xailib-repo-badge" class="single-repo-container">
  <div class="repo-vercel">
    {% include repository/repo.liquid repository='kdd-lab/XAI-Lib' %}
  </div>
  <div class="repo-official" style="display: none;">
    {% include repository/repo_official.liquid repository='kdd-lab/XAI-Lib' %}
  </div>
</div>

<style>
  #xailib-repo-badge .repo-vercel {
    display: block;
  }
  #xailib-repo-badge .repo-official {
    display: none;
  }
  #xailib-repo-badge.use-official-badges .repo-vercel {
    display: none !important;
  }
  #xailib-repo-badge.use-official-badges .repo-official {
    display: block !important;
  }
  #xailib-repo-badge .repo-official .repo-card {
    text-align: left;
  }
  #xailib-repo-badge .repo-official .repo-badges,
  #xailib-repo-badge .repo-official .repo-stats {
    justify-content: flex-start;
  }
  #xailib-repo-badge .repo-official .repo-badges img,
  #xailib-repo-badge .repo-official .repo-stats img {
    justify-self: start;
  }
</style>

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
