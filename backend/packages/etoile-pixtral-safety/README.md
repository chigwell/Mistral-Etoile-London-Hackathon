[![PyPI version](https://badge.fury.io/py/etoile_pixtral_safety.svg)](https://badge.fury.io/py/etoile_pixtral_safety)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/etoile_pixtral_safety)](https://pepy.tech/project/etoile_pixtral_safety)

# etoile_pixtral_safety

`etoile_pixtral_safety` is a Python package developed as part of the Mistral Étoile project during the London Hackathon. This package provides tools for detecting various types of potentially harmful content in images using advanced machine learning models, tailored specifically for online safety and content monitoring.

## Installation

To install `etoile_pixtral_safety`, use pip:

```bash
pip install etoile_pixtral_safety
```

## Usage

This package contains functions to check for harmful content and locate specific sections within images that may contain undesirable elements. It utilizes LangChain and HuggingFace technologies for deep learning inference.

### Setting Up the Model

```python
from langchain_mistralai import ChatMistralAI

CVISION_MODEL = "pixtral-12b-2409"

llm = ChatMistralAI(
    model=CVISION_MODEL,
    temperature=0,
    max_retries=2,
)
```

### Checking for Harmful Content

```python
from etoile_pixtral_safety import check_image

# `display_url` should be a string containing the URL to the image you want to check.
display_url = "https://example.com/path/to/image.jpg"
result = check_image(llm, display_url, verbose=True)
print(result)
```

### Finding Location of Harmful Content

```python
from etoile_pixtral_safety import find_location

result = find_location(llm, display_url, verbose=True)
print(result)
```

## Features

- Detects a wide range of harmful content in images including explicit material, violence, and other undesirable elements.
- Provides precise location data for identified content within images.
- Integrates seamlessly with state-of-the-art machine learning platforms.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/Mistral-Etoile-London-Hackathon/issues).

## License

`etoile_pixtral_safety` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgements

This package was developed by [Evgenii (Eugene) Evstafev](https://www.linkedin.com/in/eugene-evstafev-716669181/) as part of the comprehensive suite of tools for the Mistral Étoile project at the London Hackathon. More details about the project can be found on the [GitHub repository](https://github.com/chigwell/Mistral-Etoile-London-Hackathon).
