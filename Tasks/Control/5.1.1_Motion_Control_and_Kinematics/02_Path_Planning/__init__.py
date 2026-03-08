"""
Path Planning Module
Планирование путей (Path Planning) - Section 5.1.1

Finding collision-free paths in configuration space using neural architectures.
"""

from .architectures import (
    CNNPathPlanning,
    GNNPathPlanning,
    TransformerPathPlanning,
    MLPPathPlanning
)

from .tasks import (
    PathPlanningTask,
    VisualPathPlanning,
    GraphBasedPathPlanning,
    DynamicEnvironmentPathPlanning
)

from .database import PathPlanningDatabase

__all__ = [
    'CNNPathPlanning',
    'GNNPathPlanning', 
    'TransformerPathPlanning',
    'MLPPathPlanning',
    'PathPlanningTask',
    'VisualPathPlanning',
    'GraphBasedPathPlanning',
    'DynamicEnvironmentPathPlanning',
    'PathPlanningDatabase'
]

TAXONOMY_SECTION = "5.1.1.2"
SECTION_NAME = "Path Planning"
DESCRIPTION = "Finding collision-free paths in configuration space"
