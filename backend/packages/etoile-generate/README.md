[![PyPI version](https://badge.fury.io/py/etoile_generate.svg)](https://badge.fury.io/py/etoile_generate)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/etoile_generate)](https://pepy.tech/project/etoile_generate)

# etoile_generate

`etoile_generate` is a Python package developed for the Mistral AI <> a16z London Hackathon held on 06/10/2024. This package facilitates the generation of structured data from natural language queries using machine learning models, integrating with LangChain and HuggingFace technologies to provide seamless experience in transforming text into actionable insights within knowledge graphs.

## Installation

To install `etoile_generate`, use pip:

```bash
pip install etoile_generate
```

## Usage

Here is a detailed example of using `etoile_generate` to extract nodes from natural language texts and transform them into structured JSON format:

### Define the Model

```python
from langchain_mistralai import ChatMistralAI

MODEL = "mistral-large-latest"
llm = ChatMistralAI(
    model=MODEL,
    temperature=0,
    max_retries=2
)
```

### Define the Pydantic Models

```python
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Node(BaseModel):
    node_name: str = Field(..., title="Name of the node")

class Nodes(BaseModel):
    nodes: List[Node] = Field(..., title="List of nodes")
```

### Generate Nodes

```python
from etoile_generate import generate
from langchain_huggingface import HuggingFaceEmbeddings

texts = ["Your text data..."]
query = """
Generate nodes from the given texts.
Nodes are the basic building blocks of a knowledge graph.
The output will be a list of nodes.
Example:
{
    "nodes": [
        {
            "node_name": "Node 1"
        },
        {
            "node_name": "Node 2"
        }
    ]
}
Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
"""

# Invoke the generation function
result = generate(
    model=llm,
    embeddings=HuggingFaceEmbeddings(),
    pydantic_object=Nodes,
    texts=texts,
    query=query,
    chat_history=[]
)
print(result)
# Example Output: Nodes(nodes=[Node(node_name='Playwright'), ... (list all example nodes) ...])
```

### Image Processing

`etoile_generate` can also process images by accepting image URLs as part of the input:

```python
after_query = HumanMessage(content=[{
    "type": "image_url",
    "image_url": {"url": "https://example.com/path/to/image.jpg"}
}])

result = generate(
    model=llm,
    embeddings=HuggingFaceEmbeddings(),
    pydantic_object=TestContentSafety,
    texts=[],
    query="Query to analyze the image content for safety",
    chat_history=[],
    after_query=after_query,
    verbose=True
)
print(result)
```

## Features

- Generate structured JSON outputs from natural language inputs.
- Integrated vector storage and retrieval through FAISS.
- Utilizes state-of-the-art embeddings and LLMs from HuggingFace and LangChain.

## Contributing

Contributions, issues, and feature requests are welcome! Please feel free to check the [issues page](https://github.com/chigwell/Mistral-Etoile-London-Hackathon/issues).

## License

`etoile_generate` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgements

This package was created by [Evgenii (Eugene) Evstafev](https://www.linkedin.com/in/eugene-evstafev-716669181/) for the project Mistral Étoile at the Mistral AI <> a16z London Hackathon. More details about the event can be found [here](https://cerebralvalley.notion.site/Mistral-AI-a16z-London-Hackathon-Event-Details-Hackers-62cdf3e742a745aa9f4c31d20a8882af).
