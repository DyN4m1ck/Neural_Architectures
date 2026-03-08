"""
Tasks for Position Control
Задачи управления положением
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from .architectures import NeuralArchitecture, ArchitectureType


@dataclass
class TaskConstraints:
    """Constraints for position control tasks"""
    real_time: bool
    safety_critical: bool
    latency_requirements: str
    reliability: float
    hardware_constraints: List[str] = field(default_factory=list)
    sample_efficiency_requirement: str = ""


@dataclass
class PositionControlTask:
    """Base class for position control tasks"""
    task_name: str
    description: str
    neural_architectures: List[NeuralArchitecture] = field(default_factory=list)
    constraints: Optional[TaskConstraints] = None
    typical_applications: List[str] = field(default_factory=list)
    benchmark_datasets: List[str] = field(default_factory=list)


@dataclass
class PrecisionPositionControl(PositionControlTask):
    """High-precision position control for manufacturing and surgery"""
    
    def __post_init__(self):
        self.task_name = "Precision Position Control"
        self.description = "Ultra-precise position control for micrometer-level accuracy applications"
        self.neural_architectures = []
        self.constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="microseconds",
            reliability=0.9999,
            hardware_constraints=["Real-time controller", "High-resolution encoders", "Precision actuators"],
            sample_efficiency_requirement="Medium"
        )
        self.typical_applications = [
            "Precision manufacturing",
            "Surgical robotics",
            "Micro-manipulation",
            "Coordinate measuring machines"
        ]
        self.benchmark_datasets = [
            "Precision Motion Systems Dataset",
            "Industrial Robot Control Benchmark",
            "Surgical Robotics Data"
        ]


@dataclass
class MultiAxisPositionControl(PositionControlTask):
    """Coordinated position control across multiple axes"""
    
    def __post_init__(self):
        self.task_name = "Multi-Axis Position Control"
        self.description = "Synchronized position control for multi-axis systems"
        self.neural_architectures = []
        self.constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.999,
            hardware_constraints=["Multi-axis controller", "Synchronized sensors"],
            sample_efficiency_requirement="High"
        )
        self.typical_applications = [
            "CNC machining",
            "3D printing",
            "Parallel kinematics machines",
            "Robotic manipulators"
        ]
        self.benchmark_datasets = [
            "Multi-Axis Coordination Dataset",
            "CNC Control Benchmark",
            "Parallel Robot Control Data"
        ]


@dataclass
class AdaptivePositionControl(PositionControlTask):
    """Position control that adapts to changing conditions"""
    
    def __post_init__(self):
        self.task_name = "Adaptive Position Control"
        self.description = "Position control with online adaptation to payload and environment changes"
        self.neural_architectures = []
        self.constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.995,
            hardware_constraints=["Adaptive controller", "Force/torque sensors"],
            sample_efficiency_requirement="Low"
        )
        self.typical_applications = [
            "Variable payload handling",
            "Wear compensation",
            "Environmental adaptation",
            "Human-robot collaboration"
        ]
        self.benchmark_datasets = [
            "Adaptive Control Challenges",
            "Payload Variation Dataset",
            "Human-Robot Interaction Data"
        ]