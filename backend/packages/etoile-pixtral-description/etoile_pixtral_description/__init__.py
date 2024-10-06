from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import HumanMessage


from .prompts import prompts
from .models import ScreenContentSimplified

from etoile_generate import generate

def describe_image(llm, image_url, verbose=False):
    after_query = HumanMessage(content=[{
         "type": "image_url",
         "image_url": {"url": image_url}
    }])
    return generate(
        model=llm,
        embeddings=HuggingFaceEmbeddings(),
        pydantic_object=ScreenContentSimplified,
        texts=[],
        query=prompts["describe_image"],
        chat_history=[],
        after_query=after_query,
        verbose=verbose
   )