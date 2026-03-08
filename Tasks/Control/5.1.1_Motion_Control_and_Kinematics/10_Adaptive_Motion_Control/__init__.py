"""
Adaptive Motion Control Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.1.1 - Motion Control and Kinematics
Subsection 10: Adaptive Motion Control

This module provides a comprehensive database of neural network architectures
applied to adaptive motion control tasks for learning and adapting to changing
dynamics, environments, and task requirements.

Nature: Online adaptation and learning for changing system parameters and environments
Operations: Parameter adaptation, model updating, policy learning, transfer learning

Key Tasks:
    - Payload Adaptation: Adapting control to varying payloads and mass properties
    - Wear Compensation: Learning and compensating for mechanical wear over time
    - Environmental Adaptation: Adjusting control for changing environmental conditions
    - Multi-Task Learning: Single policy for multiple related motion tasks
    - Sim-to-Real Transfer: Adapting policies learned in simulation to real robots

Neural Architectures:
    - RNN: Online adaptation with temporal memory of system changes
    - TD3: Twin Delayed DDPG for sample-efficient reinforcement learning
    - Meta-Learning Networks: Learning to adapt quickly to new conditions
    - Hybrid Networks: Classical adaptive control with neural parameter updates
    - Transformer: Attention-based adaptation to relevant context changes

References:
    - "Adaptive Control with Deep Neural Networks" (2023)
    - "Online Learning for Robotic Motion Control" (2022)
    - "Deep Reinforcement Learning for Adaptive Robot Control" (2023)
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

from .database import AdaptiveMotionControlDatabase, get_adaptive_motion_control_database

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "10"
SECTION_NAME = "Motion Control and Kinematics"
SUBSECTION_NAME = "Adaptive Motion Control"
SUBSECTION_NAME_RU = "Адаптивное управление движением"

# Initialize database instance
adaptive_motion_control_db = AdaptiveMotionControlDatabase()


def get_summary():
    """Get summary of adaptive motion control module"""
    db = get_adaptive_motion_control_database()
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
    print(f"Adaptive Motion Control Module: {summary['total_tasks']} tasks, {summary['total_architectures']} architectures")


__all__ = [
    # Classes
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'AdaptiveMotionControlDatabase',
    
    # Functions
    'get_all_architectures',
    'get_architecture_by_type',
    'get_all_tasks',
    'get_task_by_name',
    'get_adaptive_motion_control_database',
    'get_summary',
    
    # Constants
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SECTION_NAME',
    'SUBSECTION_NAME',
    'SUBSECTION_NAME_RU',
    'adaptive_motion_control_db'
]