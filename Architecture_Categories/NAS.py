"""
Module for Архитектуры для поиска архитектур (NAS - Neural Architecture Search).
"""
from dataclasses import dataclass
from typing import Optional

# NAS Architectures data
NAS_ARCHITECTURES = [
    {
        "name": "Архитектуры для поиска архитектур (NAS)",
        "description": "Архитектуры, используемые для автоматического поиска оптимальных архитектур нейронных сетей."
    }
]

@dataclass
class NAS:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None