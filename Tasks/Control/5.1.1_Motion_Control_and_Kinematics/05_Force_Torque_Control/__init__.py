"""
05_Force_Torque_Control - Управление силой и моментом

Section 5.1.1.05: Controlling interaction forces and torques during contact tasks

This module provides a comprehensive database of neural network architectures 
and tasks for force/torque control in robotics applications.

Submodules:
-----------
- architectures: Neural architecture definitions for force/torque control
- tasks: Task definitions with constraints and requirements  
- database: Unified database interface

Key Architectures:
------------------
- Hybrid Force-Position Neural Controller
- Neural Impedance Controller
- Recurrent Neural Network for Force Prediction
- Convolutional Network for Tactile Force Sensing
- Adaptive MLP for Force Control
- Transformer for Multi-modal Force Control
- Physics-Informed Neural Network for Force Dynamics
- Reinforcement Learning for Force Policy

Key Tasks:
----------
- Assembly and Insertion Tasks
- Surface Finishing and Polishing
- Physical Human-Robot Interaction
- Delicate Object Manipulation
- Force-Controlled Grasping
- Contact Transition Control
- Multi-Contact Manipulation
- Force-Based Path Following

Example Usage:
--------------
```python
from .database import get_database, get_summary

# Get database instance
db = get_database()

# Get summary
summary = get_summary()
print(f"Total architectures: {summary['total_architectures']}")
print(f"Total tasks: {summary['total_tasks']}")

# Get specific task
task = db.get_task("Assembly_Insertion")
print(f"Task: {task.task_name}")
print(f"Architectures: {[a.architecture_type.value for a in task.neural_architectures]}")

# Export to dictionary
full_export = db.export_to_dict()
```
"""

from .architectures import (
    ForceTorqueArchitectureType,
    ForceTorqueNeuralArchitecture,
    ARCHITECTURES,
    get_architecture,
    get_all_architectures,
    get_architectures_by_type,
    get_real_time_architectures,
    get_safety_critical_architectures
)

from .tasks import (
    TaskConstraints,
    ForceTorqueTask,
    TASKS,
    get_task,
    get_all_tasks,
    get_real_time_tasks,
    get_safety_critical_tasks,
    get_tasks_by_application
)

from .database import (
    ForceTorqueDatabase,
    database,
    get_database,
    get_summary
)

# Metadata
__version__ = "1.0.0"
__taxonomy_section__ = "5.1.1.05"
__section_name__ = "Force/Torque Control"
__description__ = "Controlling interaction forces and torques during contact tasks"

__all__ = [
    # Architecture types
    'ForceTorqueArchitectureType',
    'ForceTorqueNeuralArchitecture',
    'ARCHITECTURES',
    'get_architecture',
    'get_all_architectures',
    'get_architectures_by_type',
    'get_real_time_architectures',
    'get_safety_critical_architectures',
    
    # Task types
    'TaskConstraints',
    'ForceTorqueTask',
    'TASKS',
    'get_task',
    'get_all_tasks',
    'get_real_time_tasks',
    'get_safety_critical_tasks',
    'get_tasks_by_application',
    
    # Database
    'ForceTorqueDatabase',
    'database',
    'get_database',
    'get_summary'
]