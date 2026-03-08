"""
02_Path_Planning - Path Planning for Motion Control

This module contains neural network architectures for path planning tasks,
including visual path planning from maps, graph-based planning, and collision-free
path finding in configuration space.

Tasks:
- Path Planning: Finding collision-free paths in configuration space
"""

from .architectures import (
    ArchitectureType,
    NeuralArchitecture,
    get_path_planning_architectures
)

from .tasks import (
    ControlTask,
    TaskConstraints,
    get_path_planning_tasks
)

from .database import (
    PathPlanningDatabase,
    get_database
)

TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "02_Path_Planning"
SUBSECTION_NAME = "Path Planning"

__all__ = [
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'PathPlanningDatabase',
    'get_path_planning_architectures',
    'get_path_planning_tasks',
    'get_database',
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SUBSECTION_NAME'
]