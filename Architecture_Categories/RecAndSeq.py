"""
Module for Recurant&Sequental Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Recurant&Sequental Architectures",
        "description": "These are architectures that perceive the world not as a set of frozen frames, but as a continuous stream, where the past determines the understanding of the present"
    }
]

@dataclass
class RecAndSeq:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None