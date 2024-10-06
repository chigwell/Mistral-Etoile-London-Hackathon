[![PyPI version](https://badge.fury.io/py/etoile_insights.svg)](https://badge.fury.io/py/etoile_insights)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/etoile_insights)](https://pepy.tech/project/etoile_insights)

# etoile_insights

`etoile_insights` is a Python package developed to analyze and generate structured insights into a person's interests, psychological traits, and professional potentials using advanced natural language processing models. This package is part of the Mistral Étoile project suite and is designed to support careers advisors, psychologists, and educational professionals in understanding and guiding individuals based on textual data analysis.

## Installation

To install `etoile_insights`, use pip:

```bash
pip install etoile_insights
```

## Usage

The package provides three main functions: `get_interests`, `get_psychological_insights`, and `get_professional_potentials`. These functions analyze text data and output structured insights.

### Setting Up the Model

```python
from langchain_mistralai import ChatMistralAI

MISTRAL_LARGE_LATEST = "mistral-large-latest"

llm = ChatMistralAI(
    model=MISTRAL_LARGE_LATEST,
    temperature=0,
    max_retries=2,
)
```

### Generating Insights

#### Interests

```python
texts = ["Text data that might reveal interests..."]
interests = get_interests(llm, texts, verbose=True)
print(interests)
```

#### Psychological Insights

```python
texts = ["Text data relevant to psychological analysis..."]
psych_insights = get_psychological_insights(llm, texts, verbose=True)
print(psych_insights)
```

#### Professional Potentials

```python
texts = ["Text data that might indicate professional potentials..."]
prof_potentials = get_professional_potentials(llm, texts, verbose=True)
print(prof_potentials)
```

These functions use text data to predict structured insights, which can be valuable in various professional contexts, from education to career planning.

## Features

- Analyzes textual data to generate structured insights into interests, psychological traits, and professional potentials.
- Utilizes state-of-the-art language models to provide accurate and meaningful interpretations.
- Provides outputs in a structured format that is easy to integrate into professional reports or systems.

## Contributing

Contributions, issues, and feature requests are welcome! Please feel free to check the [issues page](https://github.com/chigwell/etoile_insights/issues).

## License

`etoile_insights` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgements

This package was developed by [Evgenii (Eugene) Evstafev](https://www.linkedin.com/in/eugene-evstafev-716669181/) as part of the innovative tools offered by the Mistral Étoile project, aiming to provide deep insights into human behavior and potential through text analysis.
