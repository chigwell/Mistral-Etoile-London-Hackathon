from langchain_huggingface import HuggingFaceEmbeddings

from .prompts import prompts
from .models import Nodes, Relationships

from etoile_generate import generate

def generate_nodes(llm, texts=[], embeddings=HuggingFaceEmbeddings(), chat_history=[], verbose=False):
    return generate(
        model=llm,
        embeddings=embeddings,
        pydantic_object=Nodes,
        texts=texts,
        query=prompts["generate_nodes"],
        chat_history=chat_history,
        verbose=verbose
    )

def genererate_relationships(llm, texts=[], embeddings=HuggingFaceEmbeddings(), chat_history=[], verbose=False):
    return generate(
        model=llm,
        embeddings=embeddings,
        pydantic_object=Relationships,
        texts=texts,
        query=prompts["generate_relationships"],
        chat_history=chat_history,
        verbose=verbose
    )

def generate_graph(llm, texts=[], embeddings=HuggingFaceEmbeddings(), chat_history=[], verbose=False):
    nodes = generate_nodes(llm, texts, embeddings, chat_history, verbose)
    texts.append("The existing nodes are:" + str(nodes))
    return genererate_relationships(llm, texts, embeddings, chat_history, verbose=verbose)