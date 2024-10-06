import time
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import AIMessage, HumanMessage
from typing import List, Tuple, Type, TypeVar, Optional
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings

T = TypeVar('T', bound=BaseModel)


def generate(
    model,
    embeddings: HuggingFaceEmbeddings(),
    pydantic_object: Type[T],
    texts,
    query: str,
    chat_history: List[Tuple[str, str]],
    after_query=[],
    max_attempts: int = 50,
    verbose: bool = False
) -> Optional[T]:
    try:
        if verbose:
            print("Initializing vector store and retriever...")
        retriever = None
        if texts:
            vectorstore = FAISS.from_texts(texts, embeddings)
            retriever = vectorstore.as_retriever()

        if verbose:
            print("Setting up parser...")
        parser = PydanticOutputParser(pydantic_object=pydantic_object)

        if verbose:
            print("Creating prompt template...")

        messages = chat_history + [
                ("system",
                 "Answer the user query. Wrap the output in `json` tags\n{format_instructions}. " + ("The context is {context}" if retriever else "")),
                HumanMessage(content=query)
            ]
        if after_query:
            messages += chat_history + [
                ("system",
                 "Answer the user query. Wrap the output in `json` tags\n{format_instructions}. " + ("The context is {context}" if retriever else "")),
                HumanMessage(content=query),
                after_query
            ]

        prompt_template = ChatPromptTemplate.from_messages(
            messages
        ).partial(format_instructions=parser.get_format_instructions())

        if verbose:
            print("Combining prompt and model...")
        prompt_and_model = {"context": retriever or {}, "query": RunnablePassthrough()} | prompt_template | model

    except Exception as e:
        if verbose:
            print("Initialization failed with error:", str(e))
        return None

    current_attempt = 0
    while current_attempt < max_attempts:
        try:
            if verbose:
                print(f"Attempt {current_attempt + 1} to generate response...")
            output = prompt_and_model.invoke(query)
            result = parser.invoke(output)
            if result:
                if verbose:
                    print("Successfully generated response.")
                return result
            else:
                raise ValueError("Parser returned None or invalid data.")

        except Exception as e:
            current_attempt += 1
            if verbose:
                print(f"Error on attempt {current_attempt}: {str(e)}")
                print("Retrying...")
            # Optional: Implement exponential backoff
            time.sleep(2 ** current_attempt * 0.1)  # Waits 0.2s, 0.4s, 0.8s, etc.

    if verbose:
        print("Max attempts reached. Failed to generate a valid response.")
    return None