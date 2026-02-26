"""
Module for Graph Neural Networks (GNN).
"""
from dataclasses import dataclass
from typing import Optional

# Graph Neural Networks data
GRAPH_NEURAL_NETWORKS = [
    {
        "name": "Graph Neural Networks (GNN)",
        "description": "Neural networks specifically designed to operate on graph-structured data, processing relationships between entities."
    }
]

@dataclass
class GNN:
    """
    Represents a Graph Neural Network category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None