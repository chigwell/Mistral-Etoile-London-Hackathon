from .models import Interests, PsychologicalInsights, ProfessionalPotentials
from .prompts import prompts

from langchain_huggingface import HuggingFaceEmbeddings

from etoile_generate import generate

def get_interests(llm, texts=[], verbose=False):
    return generate(
        model=llm,
        embeddings=HuggingFaceEmbeddings(),
        pydantic_object=Interests,
        texts=texts,
        query=prompts["get_interests"],
        chat_history=[],
        verbose=verbose
    )

def get_psychological_insights(llm, texts=[], verbose=False):
    return generate(
        model=llm,
        embeddings=HuggingFaceEmbeddings(),
        pydantic_object=PsychologicalInsights,
        texts=texts,
        query=prompts["get_psychological_insights"],
        chat_history=[],
        verbose=verbose
    )

def get_professional_potentials(llm, texts=[], verbose=False):
    return generate(
        model=llm,
        embeddings=HuggingFaceEmbeddings(),
        pydantic_object=ProfessionalPotentials,
        texts=texts,
        query=prompts["get_professional_potentials"],
        chat_history=[],
        verbose=verbose
    )