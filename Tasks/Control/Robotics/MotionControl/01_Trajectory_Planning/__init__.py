"""
01_Trajectory_Planning - Trajectory Planning for Motion Control

This module contains neural network architectures for trajectory planning tasks,
including prediction of future states, long-horizon planning, and physics-informed
trajectory optimization.

Tasks:
- Trajectory Planning: Planning optimal motion trajectories considering dynamics, 
  obstacles, and constraints
"""

from .architectures import (
    ArchitectureType,
    NeuralArchitecture,
    get_trajectory_planning_architectures
)

from .tasks import (
    ControlTask,
    TaskConstraints,
    get_trajectory_planning_tasks
)

from .database import (
    TrajectoryPlanningDatabase,
    get_database
)

TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "01_Trajectory_Planning"
SUBSECTION_NAME = "Trajectory Planning"

__all__ = [
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'TrajectoryPlanningDatabase',
    'get_trajectory_planning_architectures',
    'get_trajectory_planning_tasks',
    'get_database',
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SUBSECTION_NAME'
]
