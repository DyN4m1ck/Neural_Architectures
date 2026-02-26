"""
Module for Архитектуры для малых данных и FEW-SHOT LEARNING
"""
from dataclasses import dataclass
from typing import Optional

# RL Architectures data
RL_ARCHITECTURES = [
    {
        "name": "Архитектуры для малых данных и FEW-SHOT LEARNING",
        "description": "Models are able to draw accurate conclusions based on an extremely limited set of examples (literally 1-5 samples), simulating the human ability to learn quickly."
    }
]

@dataclass
class SmallDataAndFewShow:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None