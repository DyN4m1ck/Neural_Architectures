"""
Module for Мультимодальные архитектуры (Multimodal Architectures).
"""
from dataclasses import dataclass
from typing import Optional


# Multimodal Architectures data
MULTIMODAL_ARCHITECTURES = [
    {
        "name": "Мультимодальные архитектуры",
        "description": "Архитектуры, способные обрабатывать несколько различных типов данных одновременно."
    }
]

@dataclass
class Multimodal:
    """
    Represents a Multimodal Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None