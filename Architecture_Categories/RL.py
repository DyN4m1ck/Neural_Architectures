"""
Module for Архитектуры для обучения с усилением (RL Architectures).
"""
from dataclasses import dataclass
from typing import Optional

# RL Architectures data
RL_ARCHITECTURES = [
    {
        "name": "Архитектуры для обучения с усилением (RL)",
        "description": "Архитектуры, разработанные специально для задач обучения с подкреплением."
    }
]

@dataclass
class RL:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None