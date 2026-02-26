"""
Module for Транформеры и механизмы внимания
"""
from dataclasses import dataclass
from typing import Optional

# Specialized Architectures data
SPECIALIZED_ARCHITECTURES = [
    {
        "name": "Transformers and mechanisms of attention",
        "description": "abandoning sequential data processing in favor of parallelism and the ability of the model to instantly determine the significance of relationships between any data elements, regardless of the distance between them."
    }
]

@dataclass
class TransformersAndAttention:
    """
    Represents a State Space Model Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None
