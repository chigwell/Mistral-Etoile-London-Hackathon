[![PyPI version](https://badge.fury.io/py/etoile_pixtral_description.svg)](https://badge.fury.io/py/etoile_pixtral_description)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/etoile_pixtral_description)](https://pepy.tech/project/etoile_pixtral_description)

# etoile_pixtral_description

`etoile_pixtral_description` is a Python package designed to extract detailed descriptions from images using advanced language models. It focuses on providing concrete descriptions of visible content characteristics on web pages or other digital media, making it particularly useful for content analysis, accessibility improvements, and SEO enhancements.

## Installation

To install `etoile_pixtral_description`, use pip:

```bash
pip install etoile_pixtral_description
```

## Usage

The package provides a function `describe_image` that generates a detailed description of the content found within an image. It uses the `ScreenContentSimplified` model for structured output.

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

### Describing an Image

```python
from etoile_pixtral_description import describe_image

# `screenshot.link` should be a string containing the URL to the image you want to describe.
screenshot_link = "https://example.com/path/to/screenshot.jpg"
result = describe_image(llm, screenshot_link, verbose=True)
print(result)
# Assuming `result` contains a property `description` which holds the detailed description.
```

This function returns a structured response with a detailed description of each content characteristic on the screen, which is useful for various applications, including digital asset management and accessibility compliance.

## Features

- Provides detailed and concrete descriptions of images for enhanced understanding and analysis.
- Utilizes advanced machine learning models to interpret and describe visual content.
- Supports detailed descriptions including the semantics of textual content and the aesthetics of visual elements.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/Mistral-Etoile-London-Hackathon/issues).

## License

`etoile_pixtral_description` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgements

This package was developed by [Evgenii (Eugene) Evstafev](https://www.linkedin.com/in/eugene-evstafev-716669181/) as part of the Mistral Étoile suite during the London Hackathon. It aims to provide tools that assist in the detailed analysis of digital content for various professional fields.
