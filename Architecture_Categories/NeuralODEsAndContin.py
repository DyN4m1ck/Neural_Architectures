"""
Module for NeuralODEs&Continuous Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "NeuralODEs&Continuous",
        "description": "They allow simulating the continuous change of latent states, which opens up new possibilities for time series analysis, signal processing, and dynamic systems"
    }
]

@dataclass
class NeuralODEsAndContin:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None