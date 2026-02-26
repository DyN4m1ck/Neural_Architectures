"""
Module for State Space Models and Post-Transformer architectures.
"""
from dataclasses import dataclass
from typing import Optional

# State Space Models and Post-Transformer architectures data
STATE_SPACE_ARCHITECTURES = [
    {
        "name": "State Space Models and Post-Transformer Architectures",
        "description": "Modern architectures including state space models and other approaches that emerged after transformer dominance."
    }
]

@dataclass
class StateSpace:
    """
    Represents a State Space Model Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None