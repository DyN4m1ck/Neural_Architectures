"""
Module for Generative Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Generative Architectures",
        "description": "A type of machine learning algorithms and neural networks designed to create new, original content (text, images, sound, video, code) that mimics the structure and style of training data"
    }
]

@dataclass
class Generative:
    """
    Represents a Generative Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None