"""
Tasks Subcategories Module
"""

# Semantic subcategories
from .Linguistics import Linguistics
from .Programming import Programming
from .Mathematics import Mathematics
from .Logic import Logic
from .Cybersecurity import Cybersecurity
from .Philosophy import Philosophy
from .Law import Law

# Perceptual subcategories
from .ComputerVision import ComputerVision
from .MedicalImaging import MedicalImaging
from .Audio import Audio
from .Tactile import Tactile
from .MultiSensor import MultiSensor

# Structured subcategories
from .TabularData import TabularData
from .TimeSeries import TimeSeries
from .Graphs import Graphs
from .Biology import Biology
from .MedicalData import MedicalData
from .Hierarchies import Hierarchies

# Physical subcategories
from .Physics import Physics
from .QuantumMechanics import QuantumMechanics
from .Astrophysics import Astrophysics
from .Chemistry import Chemistry
from .EarthSciences import EarthSciences
from .MaterialsScience import MaterialsScience
from .Ecology import Ecology

# Control subcategories
from .Robotics import Robotics
from .ControlTheory import ControlTheory
from .Optimization import Optimization
from .DecisionMaking import DecisionMaking
from .AutonomousSystems import AutonomousSystems
from .Logistics import Logistics
from .Energy import Energy

# Hybrid subcategories
from .Multimodal import Multimodal
from .Multidimensional import Multidimensional
from .CrossDomain import CrossDomain
from .MedicalTech import MedicalTech
from .MetaTasks import MetaTasks
from .Combinatorial import Combinatorial

__all__ = [
    # Semantic
    "Linguistics",
    "Programming",
    "Mathematics",
    "Logic",
    "Cybersecurity",
    "Philosophy",
    "Law",
    # Perceptual
    "ComputerVision",
    "MedicalImaging",
    "Audio",
    "Tactile",
    "MultiSensor",
    # Structured
    "TabularData",
    "TimeSeries",
    "Graphs",
    "Biology",
    "MedicalData",
    "Hierarchies",
    # Physical
    "Physics",
    "QuantumMechanics",
    "Astrophysics",
    "Chemistry",
    "EarthSciences",
    "MaterialsScience",
    "Ecology",
    # Control
    "Robotics",
    "ControlTheory",
    "Optimization",
    "DecisionMaking",
    "AutonomousSystems",
    "Logistics",
    "Energy",
    # Hybrid
    "Multimodal",
    "Multidimensional",
    "CrossDomain",
    "MedicalTech",
    "MetaTasks",
    "Combinatorial",
]