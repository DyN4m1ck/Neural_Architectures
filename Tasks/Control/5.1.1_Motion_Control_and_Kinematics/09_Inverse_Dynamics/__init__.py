"""
Inverse Dynamics Module
~~~~~~~~~~~~~~~~~~~~~~~

Section 5.1.1 - Motion Control and Kinematics
Subsection 09: Inverse Dynamics

This module provides a comprehensive database of neural network architectures
applied to inverse dynamics tasks for computing required joint torques from
desired motion trajectories.

Nature: Computing joint torques from position, velocity, and acceleration trajectories
Operations: Dynamics identification, torque prediction, compensation learning, model enhancement

Key Tasks:
    - Forward Dynamics Prediction: Predicting motion from applied torques
    - Inverse Dynamics Computation: Computing torques from desired motion
    - Friction Compensation: Learning and compensating for joint friction
    - Payload Adaptation: Adapting dynamics to varying payloads
    - Model-Based Control Enhancement: Neural correction of analytical dynamics models

Neural Architectures:
    - PINN: Physics-informed inverse dynamics respecting Newton-Euler equations
    - MLP: Fast inverse dynamics approximation for real-time control
    - LSTM: Temporal dynamics learning with history-dependent effects
    - Hybrid Networks: Combined analytical-neural dynamics with learned residuals
    - GNN: Graph-based dynamics for complex multi-body systems

References:
    - "Physics-Informed Inverse Dynamics Learning" (2023)
    - "Neural Inverse Dynamics Approximation for Real-Time Control" (2022)
    - "Learning Robot Dynamics with Deep Neural Networks" (2023)
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

from .database import InverseDynamicsDatabase, get_inverse_dynamics_database

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "09"
SECTION_NAME = "Motion Control and Kinematics"
SUBSECTION_NAME = "Inverse Dynamics"
SUBSECTION_NAME_RU = "Обратная динамика"

# Initialize database instance
inverse_dynamics_db = InverseDynamicsDatabase()


def get_summary():
    """Get summary of inverse dynamics module"""
    db = get_inverse_dynamics_database()
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
    print(f"Inverse Dynamics Module: {summary['total_tasks']} tasks, {summary['total_architectures']} architectures")


__all__ = [
    # Classes
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'InverseDynamicsDatabase',
    
    # Functions
    'get_all_architectures',
    'get_architecture_by_type',
    'get_all_tasks',
    'get_task_by_name',
    'get_inverse_dynamics_database',
    'get_summary',
    
    # Constants
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SECTION_NAME',
    'SUBSECTION_NAME',
    'SUBSECTION_NAME_RU',
    'inverse_dynamics_db'
]