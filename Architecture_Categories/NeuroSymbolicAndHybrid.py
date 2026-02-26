"""
Module for Neuro-Symbolic&Hybrid Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Neuro-Symbolic&Hybrid Architectures",
        "description": "architectures where learnability (the ability to extract knowledge from experience) is combined with determinism (the ability to follow strict rules)"
    }
]

@dataclass
class NeuroSymbolicAndHybrid:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None