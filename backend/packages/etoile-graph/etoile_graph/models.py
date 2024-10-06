from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Node(BaseModel):
    node_name: str = Field(..., title="Name of the node")

class Nodes(BaseModel):
    nodes: List[Node] = Field(..., title="List of nodes")

class Relationship(BaseModel):
    source: str = Field(..., title="Name of the source node")
    target: str = Field(..., title="Name of the target node")
    relationship_name: str = Field(..., title="Name of the relationship")

class Relationships(BaseModel):
    relationships: List[Relationship] = Field(..., title="List of relationships")