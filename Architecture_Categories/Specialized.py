"""
Module for Специализированные архитектуры (Specialized Architectures).
"""
from dataclasses import dataclass
from typing import Optional

# Specialized Architectures data
SPECIALIZED_ARCHITECTURES = [
    {
        "name": "Специализированные архитектуры",
        "description": "Архитектуры, разработанные для конкретных задач или областей применения."
    }
]

@dataclass
class Specialized:
    """
    Represents a Specialized Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None