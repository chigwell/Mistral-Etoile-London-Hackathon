from .relations import RELATIONS

prompts = {
    "generate_nodes": """
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
    """,
    "generate_relationships": """
        Generate relationships from the given texts and given nodes.
        Relationships are the connections between nodes in a knowledge graph.
        The output will be a list of relationships.
        Example:
        {
            "relationships": [
                {
                    "source": "Node 1",
                    "target": "Node 2",
                    "relationship_name": "is_a"
                },
                {
                    "source": "Node 2",
                    "target": "Node 3",
                    "relationship_name": "measured_by"
                }
            ]
        }
        relationship_name can be something from this list: """ + str(RELATIONS) + """
        Write the response in JSON format within ``` tags and provide the response only, without any additional explanation.
    """
}