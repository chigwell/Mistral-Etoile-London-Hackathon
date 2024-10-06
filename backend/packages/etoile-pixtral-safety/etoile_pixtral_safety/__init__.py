from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import HumanMessage

from .prompts import prompts
from .models import TestContentSafety, ContentLocation

from etoile_generate import generate

def check_image(llm, image_url, verbose=False):
    after_query = HumanMessage(content=[{
                    "type": "image_url",
                    "image_url": {"url": image_url}
    }])
    return generate(
        model=llm,
        embeddings=HuggingFaceEmbeddings(),
        pydantic_object=TestContentSafety,
        texts=[],
        query=prompts["test_safety"],
        chat_history=[],
        after_query=after_query,
        verbose=verbose
    )

def find_location(llm, image_url, verbose=False):
    after_query = HumanMessage(content=[{
                    "type": "image_url",
                    "image_url": {"url": image_url}
    }])
    return generate(
        model=llm,
        embeddings=HuggingFaceEmbeddings(),
        pydantic_object=ContentLocation,
        texts=[],
        query=prompts["find_section"],
        chat_history=[],
        after_query=after_query,
        verbose=verbose
    )
