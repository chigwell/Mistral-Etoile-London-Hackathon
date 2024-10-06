[![PyPI version](https://badge.fury.io/py/etoile_graph.svg)](https://badge.fury.io/py/etoile_graph)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/etoile_graph)](https://pepy.tech/project/etoile_graph)

# etoile_graph

`etoile_graph` is a Python package developed to streamline the creation of knowledge graphs from natural language data using machine learning models. The package leverages the capabilities of LangChain and HuggingFace technologies, enabling the extraction and linking of nodes and relationships directly from text.

## Installation

To install `etoile_graph`, use pip:

```bash
pip install etoile_graph
```

## Usage

The package includes three primary functions: `generate_nodes`, `generate_relationships`, and `generate_graph`. Here is how you can use these functions to generate a knowledge graph:

### Setting Up the Model

```python
from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2
)
```

### Generating a Graph

```python
from etoile_graph import generate_graph

# Assume `description` is a string containing the textual description.
texts = [description]
result = generate_graph(llm, texts, verbose=True)
print(result)
```

This function first generates nodes from the input texts and then uses these nodes to generate relationships, constructing a knowledge graph.

## Features

- Generates nodes and relationships from text using machine learning.
- Builds comprehensive knowledge graphs with nodes and relationships.
- Integrates smoothly with LangChain and HuggingFace for advanced text processing and embedding generation.

## Contributing

Contributions, issues, and feature requests are welcome! Please feel free to check the [issues page](https://github.com/chigwell/Mistral-Etoile-London-Hackathon/issues).

## License

`etoile_graph` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgements

This package was developed by [Evgenii (Eugene) Evstafev](https://www.linkedin.com/in/eugene-evstafev-716669181/) for advanced knowledge graph generation tasks. It aims to assist developers in creating structured data models from unstructured text inputs.
