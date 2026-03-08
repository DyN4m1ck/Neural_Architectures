"""
Inverse Kinematics Module
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.1.1 - Motion Control and Kinematics
Subsection 08: Inverse Kinematics

This module provides a comprehensive database of neural network architectures
applied to inverse kinematics tasks for computing joint angles from desired
end-effector poses.

Nature: Computing joint configurations from Cartesian end-effector poses
Operations: IK solving, redundancy resolution, singularity handling, configuration optimization

Key Tasks:
    - Analytical IK Approximation: Learning closed-form IK solutions
    - Numerical IK Enhancement: Neural initialization for iterative solvers
    - Redundancy Resolution: Optimal configuration selection for redundant manipulators
    - Singularity Avoidance: Learning to avoid kinematic singularities
    - Multi-Solution Selection: Choosing optimal IK solution from multiple possibilities

Neural Architectures:
    - MLP: Direct inverse kinematics mapping with fast inference
    - VAE: Probabilistic IK with uncertainty quantification and redundancy handling
    - CNN: Visual-spatial IK from image-based end-effector targets
    - GNN: Graph-based IK for complex kinematic chains and tree structures
    - PINN: Physics-informed IK respecting joint limits and kinematic constraints

References:
    - "Learning Inverse Kinematics with Deep Neural Networks" (2023)
    - "Variational Inverse Kinematics for Redundant Manipulators" (2022)
    - "Physics-Informed Neural IK Solvers" (2023)
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

from .database import InverseKinematicsDatabase, get_inverse_kinematics_database

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "08"
SECTION_NAME = "Motion Control and Kinematics"
SUBSECTION_NAME = "Inverse Kinematics"
SUBSECTION_NAME_RU = "Обратная кинематика"

# Initialize database instance
inverse_kinematics_db = InverseKinematicsDatabase()


def get_summary():
    """Get summary of inverse kinematics module"""
    db = get_inverse_kinematics_database()
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
    print(f"Inverse Kinematics Module: {summary['total_tasks']} tasks, {summary['total_architectures']} architectures")


__all__ = [
    # Classes
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'InverseKinematicsDatabase',
    
    # Functions
    'get_all_architectures',
    'get_architecture_by_type',
    'get_all_tasks',
    'get_task_by_name',
    'get_inverse_kinematics_database',
    'get_summary',
    
    # Constants
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SECTION_NAME',
    'SUBSECTION_NAME',
    'SUBSECTION_NAME_RU',
    'inverse_kinematics_db'
]