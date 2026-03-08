"""
Impedance and Admittance Control - Task Definitions
====================================================

This module defines specific control tasks for impedance and admittance control,
including their requirements, constraints, and applicable neural architectures.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from .architectures import NeuralArchitecture, ArchitectureType


@dataclass
class TaskConstraints:
    """
    Represents constraints and requirements for a control task.
    
    Attributes:
        real_time: Whether real-time execution is required
        safety_critical: Whether the task is safety-critical
        latency_requirements: Required latency (microseconds, milliseconds, seconds)
        reliability: Required reliability (0.0 to 1.0)
        hardware_constraints: List of hardware requirements
        sample_efficiency_requirement: Required sample efficiency level
    """
    real_time: bool
    safety_critical: bool
    latency_requirements: str
    reliability: float
    hardware_constraints: List[str]
    sample_efficiency_requirement: str


@dataclass
class ControlTask:
    """
    Represents a specific impedance/admittance control task.
    
    Attributes:
        task_name: Name of the task
        description: Detailed description
        neural_architectures: List of applicable neural architectures
        constraints: Task constraints and requirements
        typical_applications: List of typical applications
        benchmark_datasets: Relevant benchmark datasets
    """
    task_name: str
    description: str
    neural_architectures: List[NeuralArchitecture]
    constraints: TaskConstraints
    typical_applications: List[str]
    benchmark_datasets: List[str]


class ImpedanceAdmittanceTasks:
    """Factory class for creating impedance/admittance control tasks"""
    
    @staticmethod
    def get_impedance_parameter_learning_task() -> ControlTask:
        """Task: Learning impedance parameters from demonstration"""
        return ControlTask(
            task_name="Impedance Parameter Learning",
            description="Learning optimal impedance parameters (mass, damping, stiffness) from human demonstration or trial-and-error",
            neural_architectures=[],  # Will be populated by database
            constraints=TaskConstraints(
                real_time=False,
                safety_critical=True,
                latency_requirements="milliseconds",
                reliability=0.99,
                hardware_constraints=["Force/torque sensors", "Motion capture system"],
                sample_efficiency_requirement="High"
            ),
            typical_applications=[
                "Teaching robots compliant behavior",
                "Adaptive assembly operations",
                "Human-robot collaborative tasks",
                "Rehabilitation robotics"
            ],
            benchmark_datasets=[
                "Learning from Demonstration Dataset",
                "Compliant Manipulation Benchmark",
                "HRI Interaction Records"
            ]
        )
    
    @staticmethod
    def get_admittance_control_task() -> ControlTask:
        """Task: Admittance control for physical interaction"""
        return ControlTask(
            task_name="Admittance Control",
            description="Implementing admittance control to regulate robot motion in response to external forces",
            neural_architectures=[],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="microseconds",
                reliability=0.999,
                hardware_constraints=["High-bandwidth force sensors", "Fast control loop"],
                sample_efficiency_requirement="Medium"
            ),
            typical_applications=[
                "Collaborative robot guidance",
                "Teleoperation with force feedback",
                "Physical human-robot interaction",
                "Assistive robotics"
            ],
            benchmark_datasets=[
                "Admittance Control Benchmarks",
                "Force-Controlled Interaction Data",
                "Haptic Interaction Dataset"
            ]
        )
    
    @staticmethod
    def get_variable_stiffness_control_task() -> ControlTask:
        """Task: Variable stiffness/impedance control"""
        return ControlTask(
            task_name="Variable Stiffness Control",
            description="Dynamically adjusting stiffness and damping parameters based on task requirements and environment",
            neural_architectures=[],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="milliseconds",
                reliability=0.99,
                hardware_constraints=["Variable stiffness actuators", "Context sensors"],
                sample_efficiency_requirement="High"
            ),
            typical_applications=[
                "Adaptive grasping",
                "Safe human-robot collaboration",
                "Multi-task manipulation",
                "Unstructured environment operation"
            ],
            benchmark_datasets=[
                "Variable Stiffness Dataset",
                "Adaptive Compliance Benchmark",
                "Task-Phase Transition Data"
            ]
        )
    
    @staticmethod
    def get_contact_rich_manipulation_task() -> ControlTask:
        """Task: Contact-rich manipulation with impedance control"""
        return ControlTask(
            task_name="Contact-Rich Manipulation",
            description="Performing complex manipulation tasks involving multiple contact modes and transitions",
            neural_architectures=[],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="microseconds",
                reliability=0.999,
                hardware_constraints=["Tactile sensors", "Force/torque sensors", "Vision system"],
                sample_efficiency_requirement="Low"
            ),
            typical_applications=[
                "Assembly with tight tolerances",
                "Surface finishing and polishing",
                "Insertion tasks",
                "Contour following"
            ],
            benchmark_datasets=[
                "Contact-Rich Manipulation Dataset",
                "Assembly Task Benchmark",
                "Multi-Modal Interaction Data"
            ]
        )
    
    @staticmethod
    def get_human_robot_interaction_task() -> ControlTask:
        """Task: Safe human-robot interaction with adaptive impedance"""
        return ControlTask(
            task_name="Human-Robot Interaction",
            description="Ensuring safe and natural physical interaction between humans and robots through adaptive impedance control",
            neural_architectures=[],
            constraints=TaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="microseconds",
                reliability=0.9999,
                hardware_constraints=["Safety-rated sensors", "Collision detection", "Emergency stop"],
                sample_efficiency_requirement="Low"
            ),
            typical_applications=[
                "Collaborative manufacturing",
                "Healthcare assistance",
                "Rehabilitation therapy",
                "Service robotics"
            ],
            benchmark_datasets=[
                "HRI Safety Dataset",
                "Human Motion Prediction Data",
                "Collaborative Task Benchmark"
            ]
        )
    
    @staticmethod
    def get_all_tasks() -> List[ControlTask]:
        """Get all impedance/admittance control tasks"""
        return [
            ImpedanceAdmittanceTasks.get_impedance_parameter_learning_task(),
            ImpedanceAdmittanceTasks.get_admittance_control_task(),
            ImpedanceAdmittanceTasks.get_variable_stiffness_control_task(),
            ImpedanceAdmittanceTasks.get_contact_rich_manipulation_task(),
            ImpedanceAdmittanceTasks.get_human_robot_interaction_task()
        ]