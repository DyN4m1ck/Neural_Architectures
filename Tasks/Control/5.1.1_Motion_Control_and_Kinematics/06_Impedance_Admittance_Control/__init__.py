"""
Impedance/Admittance Control Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 5.1.1 - Motion Control and Kinematics
Subsection 06: Impedance/Admittance Control

This module provides a comprehensive database of neural network architectures
applied to impedance and admittance control tasks for compliant robot interaction.

Nature: Controlling mechanical impedance characteristics for compliant interaction
Operations: Impedance regulation, admittance control, compliance adjustment, safe HRI

Key Tasks:
    - Variable Impedance Control: Adapting stiffness and damping in real-time
    - Admittance Control: Velocity response to applied forces
    - Compliance Learning: Learning optimal compliance for tasks
    - Safe Human-Robot Interaction: Ensuring safety through controlled impedance
    - Haptic Rendering: Generating realistic force feedback

Neural Architectures:
    - Neural ODE: Continuous-time impedance model learning
    - LSTM: Temporal impedance adaptation based on interaction history
    - PINN: Physics-informed impedance respecting mechanical laws
    - Transformer: Multi-modal attention for contact state and impedance selection
    - Hybrid Networks: Combined impedance-position control with learned switching

References:
    - "Neural ODEs for Impedance Control" (2023)
    - "Learning Mechanical Impedance for Safe HRI" (2022)
    - "Physics-Informed Admittance Control" (2023)
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

from .database import ImpedanceAdmittanceControlDatabase, get_impedance_admittance_control_database

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "06"
SECTION_NAME = "Motion Control and Kinematics"
SUBSECTION_NAME = "Impedance/Admittance Control"
SUBSECTION_NAME_RU = "Импедансное и адмиттансное управление"

# Initialize database instance
impedance_admittance_control_db = ImpedanceAdmittanceControlDatabase()


def get_summary():
    """Get summary of impedance/admittance control module"""
    db = get_impedance_admittance_control_database()
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
    print(f"Impedance/Admittance Control Module: {summary['total_tasks']} tasks, {summary['total_architectures']} architectures")


__all__ = [
    # Classes
    'ArchitectureType',
    'NeuralArchitecture',
    'ControlTask',
    'TaskConstraints',
    'ImpedanceAdmittanceControlDatabase',
    
    # Functions
    'get_all_architectures',
    'get_architecture_by_type',
    'get_all_tasks',
    'get_task_by_name',
    'get_impedance_admittance_control_database',
    'get_summary',
    
    # Constants
    'TAXONOMY_SECTION',
    'SUBSECTION',
    'SECTION_NAME',
    'SUBSECTION_NAME',
    'SUBSECTION_NAME_RU',
    'impedance_admittance_control_db'
]