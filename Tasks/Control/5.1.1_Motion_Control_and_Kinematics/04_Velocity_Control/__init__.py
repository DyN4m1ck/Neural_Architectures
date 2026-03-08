"""
Velocity Control Module
~~~~~~~~~~~~~~~~~~~~~~~

Section 5.1.1 - Motion Control and Kinematics
Subsection 04: Velocity Control

This module provides a comprehensive database of neural network architectures
applied to velocity control tasks in robotics and autonomous systems.

Nature: Controlling the speed and direction of motion
Operations: Speed regulation, smooth profile generation, disturbance rejection

Key Tasks:
    - Velocity Tracking: Following desired velocity profiles
    - Smooth Profile Generation: Creating jerk-limited velocity trajectories
    - Coordinated Velocity Control: Multi-axis velocity synchronization
    - Disturbance Rejection: Maintaining velocity under external disturbances
    - Jerk-Limited Motion: Smooth acceleration/deceleration profiles

Neural Architectures:
    - GRU: Gated Recurrent Units for smooth velocity profile generation
    - LSTM: Long Short-Term Memory for velocity prediction and control
    - CNN: Convolutional networks for visual velocity estimation
    - Transformer: Attention-based models for long-horizon velocity planning
    - PINN: Physics-Informed Neural Networks for dynamics-consistent control

References:
    - "GRU for Smooth Velocity Control" (2023)
    - "Learning Velocity Profiles with Deep Learning" (2022)
    - "Physics-Informed Velocity Control" (2023)
"""

from .architectures import (
    ArchitectureType,
    NeuralArchitecture,
    get_all_architectures,
    get_architecture_by_type
)

from .tasks import (
    ControlTask,
    TaskConstraints,
    get_all_tasks,
    get_task_by_name
)

from .database import VelocityControlDatabase, get_velocity_control_database

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "04"
SECTION_NAME = "Motion Control and Kinematics"
SUBSECTION_NAME = "Velocity Control"
SUBSECTION_NAME_RU = "Управление скоростью"

# Initialize database instance
velocity_control_db = VelocityControlDatabase()


def get_summary():
    """Get summary of velocity control module"""
    db = get_velocity_control_database()
    tasks = db.get_all_tasks()
    architectures = db.get_all_architectures()
    
    return {
        "taxonomy_section": TAXONOMY_SECTION,
        "subsection": SUBSECTION,
        "section_name": SECTION_NAME,
        "subsection_name": SUBSECTION_NAME,
        "subsection_name_ru": SUBSECTION_NAME_RU,
        "total_tasks": len(tasks),
        "task_names": [task.task_name for task in tasks],
        "total_architectures": len(architectures),
        "architecture_types": list(set(arch.architecture_type.value for arch in architectures)),
        "real_time_tasks": len(db.get_tasks_requiring_real_time()),
        "safety_critical_tasks": len(db.get_safety_critical_tasks())
    }


# Print summary on import
if __name__ == "__main__":
    summary = get_summary()
    print(f"Velocity Control Module: {summary['total_tasks']} tasks, {summary['total_architectures']} architectures")


__all__ = [
    # Classes
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'VelocityControlDatabase',
    
    # Functions
    'get_all_architectures',
    'get_architecture_by_type',
    'get_all_tasks',
    'get_task_by_name',
    'get_velocity_control_database',
    'get_summary',
    
    # Constants
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SECTION_NAME',
    'SUBSECTION_NAME',
    'SUBSECTION_NAME_RU',
    'velocity_control_db'
]