"""
Module for Спайковые и нейроморфные архитектуры
"""
from dataclasses import dataclass
from typing import Optional

# Specialized Architectures data
SPECIALIZED_ARCHITECTURES = [
    {
        "name": "Spike and neuromorphic architectures",
        "description": "simulations of the biological principles of the brain at the hardware and software levels to achieve extreme energy efficiency and real-time operation"
    }
]

@dataclass
class SpikeAndNeuromorph:
    """
    Represents a Specialized Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None