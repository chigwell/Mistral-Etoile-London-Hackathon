from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Interest(BaseModel):
    interest_name: str = Field(..., title="Name of the interest")
    interest_value: int = Field(..., title="Value of the interest from 0 to 100 (0 being not interested, 100 being very interested for a user)")

class Interests(BaseModel):
    interests: List[Interest] = Field(..., title="List of interests")


class PsychologicalInsight(BaseModel):
    insight: str = Field(..., title="Description of a psychological trait or behavior")

class PsychologicalInsights(BaseModel):
    insights: List[PsychologicalInsight] = Field(..., title="List of psychological insights")


class ProfessionalPotential(BaseModel):
    potential: str = Field(..., title="Description of a professional career potential")

class ProfessionalPotentials(BaseModel):
    potentials: List[ProfessionalPotential] = Field(..., title="List of professional career potentials")
