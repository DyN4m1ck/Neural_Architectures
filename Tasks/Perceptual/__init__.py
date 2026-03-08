"""
Perceptual Tasks Subcategories Module
"""

from .ComputerVision import ComputerVision
from .MedicalImaging import MedicalImaging
from .Audio import Audio
from .Tactile import Tactile
from .MultiSensor import MultiSensor

__all__ = [
    "ComputerVision",
    "MedicalImaging",
    "Audio",
    "Tactile",
    "MultiSensor",
]
