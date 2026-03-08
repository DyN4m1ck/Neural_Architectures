"""
Hybrid Position/Force Control Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.1.1 - Motion Control and Kinematics
Subsection 07: Hybrid Position/Force Control

This module provides a comprehensive database of neural network architectures
applied to hybrid position/force control tasks for simultaneous control of
position in unconstrained directions and force in constrained directions.

Nature: Simultaneous control of position and force in different task space directions
Operations: Mode switching, coordination learning, constraint handling, multi-objective optimization

Key Tasks:
    - Assembly with Insertion: Precise positioning with contact force control
    - Surface Following: Maintaining contact while following contours
    - Contour Tracking: Force-regulated path following
    - Coordinated Manipulation: Multi-arm position/force coordination
    - Deburring and Polishing: Consistent force application during motion

Neural Architectures:
    - Transformer: Multi-task learning with attention to contact states
    - Hybrid Networks: Separate position and force channels with learned coordination
    - LSTM: Temporal coordination of position and force transitions
    - PINN: Physics-informed hybrid control respecting contact constraints
    - Multi-Head Networks: Parallel processing of position and force modalities

References:
    - "Transformer-based Hybrid Control for Assembly Tasks" (2023)
    - "Attention in Multi-Modal Position/Force Control" (2022)
    - "Learning Coordination for Hybrid Control" (2023)
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

from .database import HybridPositionForceControlDatabase, get_hybrid_position_force_control_database

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "07"
SECTION_NAME = "Motion Control and Kinematics"
SUBSECTION_NAME = "Hybrid Position/Force Control"
SUBSECTION_NAME_RU = "Гибридное управление позиция/сила"

# Initialize database instance
hybrid_position_force_control_db = HybridPositionForceControlDatabase()


def get_summary():
    """Get summary of hybrid position/force control module"""
    db = get_hybrid_position_force_control_database()
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
    print(f"Hybrid Position/Force Control Module: {summary['total_tasks']} tasks, {summary['total_architectures']} architectures")


__all__ = [
    # Classes
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'HybridPositionForceControlDatabase',
    
    # Functions
    'get_all_architectures',
    'get_architecture_by_type',
    'get_all_tasks',
    'get_task_by_name',
    'get_hybrid_position_force_control_database',
    'get_summary',
    
    # Constants
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SECTION_NAME',
    'SUBSECTION_NAME',
    'SUBSECTION_NAME_RU',
    'hybrid_position_force_control_db'
]