"""
Module for Convolutional Architectures (CNN).
"""
from dataclasses import dataclass
from typing import Optional


# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Convolutional Architectures (CNN)",
        "description": "Neural network architectures primarily based on convolutional layers, commonly used for image processing and computer vision tasks."
    }
]


@dataclass
class CNN:
    """
    Represents a Convolutional Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None