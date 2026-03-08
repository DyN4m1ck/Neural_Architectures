"""
Tasks for Trajectory Planning

This module defines control tasks and constraints for trajectory planning.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from .architectures import NeuralArchitecture


@dataclass
class TaskConstraints:
    """
    Represents constraints and requirements for a control task.
    
    Attributes:
        real_time: Whether real-time execution is required
        safety_critical: Whether this is a safety-critical task
        latency_requirements: Latency requirements (microseconds, milliseconds, seconds)
        reliability: Required reliability (0.0 to 1.0)
        hardware_constraints: List of hardware constraints
        sample_efficiency_requirement: Sample efficiency requirement level
    """
    
    real_time: bool = False
    safety_critical: bool = False
    latency_requirements: str = "milliseconds"
    reliability: float = 0.99
    hardware_constraints: List[str] = field(default_factory=list)
    sample_efficiency_requirement: str = "Medium"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert constraints to dictionary representation."""
        return {
            "real_time": self.real_time,
            "safety_critical": self.safety_critical,
            "latency_requirements": self.latency_requirements,
            "reliability": self.reliability,
            "hardware_constraints": self.hardware_constraints,
            "sample_efficiency_requirement": self.sample_efficiency_requirement
        }


@dataclass
class ControlTask:
    """
    Represents a control task for trajectory planning.
    
    Attributes:
        task_name: Name of the task
        description: Detailed description of the task
        neural_architectures: List of applicable neural network architectures
        constraints: Task constraints and requirements
        typical_applications: List of typical applications
        benchmark_datasets: List of relevant benchmark datasets
    """
    
    task_name: str
    description: str
    neural_architectures: List[NeuralArchitecture]
    constraints: TaskConstraints
    typical_applications: List[str] = field(default_factory=list)
    benchmark_datasets: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary representation."""
        return {
            "task_name": self.task_name,
            "description": self.description,
            "neural_architectures": [arch.to_dict() for arch in self.neural_architectures],
            "constraints": self.constraints.to_dict(),
            "typical_applications": self.typical_applications,
            "benchmark_datasets": self.benchmark_datasets
        }


def get_trajectory_planning_task() -> ControlTask:
    """Create the main trajectory planning task."""
    from .architectures import (
        get_lstm_architecture,
        get_transformer_architecture,
        get_pinn_architecture
    )
    
    return ControlTask(
        task_name="Trajectory Planning",
        description="Planning optimal motion trajectories considering dynamics, obstacles, and constraints",
        neural_architectures=[
            get_lstm_architecture(),
            get_transformer_architecture(),
            get_pinn_architecture()
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.99,
            hardware_constraints=["GPU", "Real-time processor"],
            sample_efficiency_requirement="Medium"
        ),
        typical_applications=[
            "Quadrotor trajectory optimization",
            "Robotic arm path planning",
            "Autonomous vehicle motion planning",
            "Industrial robot trajectory generation"
        ],
        benchmark_datasets=[
            "Robotics Trajectory Dataset",
            "Dynamic Obstacle Avoidance",
            "Physics-based Motion Planning"
        ]
    )


def get_trajectory_planning_tasks() -> List[ControlTask]:
    """Get all trajectory planning tasks."""
    return [get_trajectory_planning_task()]
