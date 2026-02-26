"""
Module for Energy & Equilibrium Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Energy & Equilibrium Architectures",
        "description": "analytical tools used to predict the state of complex systems (economic or physico-chemical) based on the balance of supply and demand, minimizing costs and optimizing the use of resources. They find the optimal balance by ensuring consistency between production capacity, commodity/energy flows, and consumption."
    }
]

@dataclass
class EnergyAndEquilibriaum:
    """
    Represents a Convolutional Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None