"""
Tasks for Path Planning
Задачи планирования путей
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from .architectures import NeuralArchitecture, ArchitectureType


@dataclass
class TaskConstraints:
    """Constraints for path planning tasks"""
    real_time: bool
    safety_critical: bool
    latency_requirements: str
    reliability: float
    hardware_constraints: List[str] = field(default_factory=list)
    sample_efficiency_requirement: str = ""


@dataclass
class PathPlanningTask:
    """Base class for path planning tasks"""
    task_name: str
    description: str
    neural_architectures: List[NeuralArchitecture] = field(default_factory=list)
    constraints: Optional[TaskConstraints] = None
    typical_applications: List[str] = field(default_factory=list)
    benchmark_datasets: List[str] = field(default_factory=list)


@dataclass
class VisualPathPlanning(PathPlanningTask):
    """Visual path planning from environmental maps"""
    
    def __post_init__(self):
        self.task_name = "Visual Path Planning"
        self.description = "Finding collision-free paths from visual representations of environment"
        self.neural_architectures = [
            # CNN architecture would be instantiated here
        ]
        self.constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.995,
            hardware_constraints=["GPU", "Camera sensors"],
            sample_efficiency_requirement="Medium"
        )
        self.typical_applications = [
            "Mobile robot navigation",
            "Drone path planning",
            "Autonomous vehicle navigation",
            "Warehouse robot routing"
        ]
        self.benchmark_datasets = [
            "2D Navigation Maps",
            "3D Path Planning Dataset",
            "Dynamic Environment Path Planning"
        ]


@dataclass
class GraphBasedPathPlanning(PathPlanningTask):
    """Graph-based path planning with topological reasoning"""
    
    def __post_init__(self):
        self.task_name = "Graph-Based Path Planning"
        self.description = "Finding optimal paths using graph representations and GNNs"
        self.neural_architectures = [
            # GNN architecture would be instantiated here
        ]
        self.constraints = TaskConstraints(
            real_time=False,
            safety_critical=True,
            latency_requirements="seconds",
            reliability=0.99,
            hardware_constraints=["GPU", "Memory"],
            sample_efficiency_requirement="High"
        )
        self.typical_applications = [
            "Road network navigation",
            "Building floor navigation",
            "Multi-floor path planning",
            "Transportation network routing"
        ]
        self.benchmark_datasets = [
            "OpenStreetMap",
            "Indoor Navigation Graphs",
            "City-Scale Path Planning"
        ]


@dataclass
class DynamicEnvironmentPathPlanning(PathPlanningTask):
    """Path planning in dynamic environments with moving obstacles"""
    
    def __post_init__(self):
        self.task_name = "Dynamic Environment Path Planning"
        self.description = "Real-time path planning with moving obstacles and changing conditions"
        self.neural_architectures = [
            # Transformer or RNN architectures would be instantiated here
        ]
        self.constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.999,
            hardware_constraints=["GPU", "Real-time sensors", "Fast actuators"],
            sample_efficiency_requirement="High"
        )
        self.typical_applications = [
            "Crowded environment navigation",
            "Human-robot coexistence",
            "Traffic-aware routing",
            "Dynamic obstacle avoidance"
        ]
        self.benchmark_datasets = [
            "Social Navigation Dataset",
            "Pedestrian Trajectory Dataset",
            "Dynamic Obstacle Avoidance Benchmark"
        ]
