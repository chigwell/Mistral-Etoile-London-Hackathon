from langchain_core.pydantic_v1 import BaseModel, Field


class ScreenContentSimplified(BaseModel):
    description: str = Field(..., title="Detailed description of all content characteristics on the screen")