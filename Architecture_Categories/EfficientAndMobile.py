"""
Module for Efficient & Mobile Architectures
"""
from dataclasses import dataclass
from typing import Optional


# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Efficient & Mobile Architectures",
        "description": "structured software design patterns (MVC, MVP, MVVM, MVI) that ensure high performance, ease of support, and scalability of applications."
    }
]

@dataclass
class EfficientAndMobile:
    """
    Represents a Convolutional Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None