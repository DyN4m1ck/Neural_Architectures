"""
Database for Force/Torque Control
Section 5.1.1.05 - Unified database for force/torque control tasks and architectures
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from .architectures import (
    ForceTorqueNeuralArchitecture, 
    ARCHITECTURES, 
    get_architecture,
    get_all_architectures,
    get_real_time_architectures,
    get_safety_critical_architectures,
    ForceTorqueArchitectureType
)
from .tasks import (
    ForceTorqueTask,
    TASKS,
    get_task,
    get_all_tasks,
    get_real_time_tasks,
    get_safety_critical_tasks,
    TaskConstraints
)

@dataclass
class ForceTorqueDatabase:
    """Unified database for force/torque control domain"""
    taxonomy_section: str = "5.1.1.05"
    section_name: str = "Force/Torque Control"
    description: str = "Controlling interaction forces and torques during contact tasks"
    
    def get_architecture(self, name: str) -> Optional[ForceTorqueNeuralArchitecture]:
        """Get architecture by name"""
        return get_architecture(name)
    
    def get_all_architectures(self) -> Dict[str, ForceTorqueNeuralArchitecture]:
        """Get all architectures"""
        return get_all_architectures()
    
    def get_task(self, name: str) -> Optional[ForceTorqueTask]:
        """Get task by name"""
        return get_task(name)
    
    def get_all_tasks(self) -> Dict[str, ForceTorqueTask]:
        """Get all tasks"""
        return get_all_tasks()
    
    def get_summary(self) -> Dict[str, Any]:
        """Get comprehensive summary of the database"""
        all_archs = self.get_all_architectures()
        all_tasks = self.get_all_tasks()
        
        return {
            "taxonomy_section": self.taxonomy_section,
            "section_name": self.section_name,
            "description": self.description,
            "total_architectures": len(all_archs),
            "total_tasks": len(all_tasks),
            "architectures": list(all_archs.keys()),
            "tasks": list(all_tasks.keys()),
            "real_time_architectures": len(get_real_time_architectures()),
            "safety_critical_architectures": len(get_safety_critical_architectures()),
            "real_time_tasks": len(get_real_time_tasks()),
            "safety_critical_tasks": len(get_safety_critical_tasks())
        }
    
    def export_to_dict(self) -> Dict[str, Any]:
        """Export entire database to dictionary format"""
        return {
            "metadata": {
                "taxonomy_section": self.taxonomy_section,
                "section_name": self.section_name,
                "description": self.description
            },
            "architectures": {
                name: arch.to_dict() for name, arch in self.get_all_architectures().items()
            },
            "tasks": {
                name: task.to_dict() for name, task in self.get_all_tasks().items()
            },
            "summary": self.get_summary()
        }
    
    def find_architectures_for_task(self, task_name: str) -> List[Dict[str, Any]]:
        """Find all architectures applicable to a specific task"""
        task = self.get_task(task_name)
        if not task:
            return []
        return [arch.to_dict() for arch in task.neural_architectures]
    
    def find_tasks_for_architecture(self, arch_name: str) -> List[str]:
        """Find all tasks that use a specific architecture"""
        arch = self.get_architecture(arch_name)
        if not arch:
            return []
        
        matching_tasks = []
        for task_name, task in self.get_all_tasks().items():
            if any(
                t_arch.architecture_type == arch.architecture_type 
                for t_arch in task.neural_architectures
            ):
                matching_tasks.append(task_name)
        
        return matching_tasks
    
    def filter_by_constraint(self, constraint_type: str, value: bool = True) -> Dict[str, Any]:
        """Filter tasks or architectures by constraint"""
        if constraint_type == "real_time":
            return {
                "tasks": {k: v.to_dict() for k, v in self.get_all_tasks().items() if v.constraints.real_time == value},
                "architectures": {k: v.to_dict() for k, v in self.get_all_architectures().items() if v.real_time_capable == value}
            }
        elif constraint_type == "safety_critical":
            return {
                "tasks": {k: v.to_dict() for k, v in self.get_all_tasks().items() if v.constraints.safety_critical == value},
                "architectures": {k: v.to_dict() for k, v in self.get_all_architectures().items() if v.safety_critical == value}
            }
        else:
            return {}

# Create singleton instance
database = ForceTorqueDatabase()

def get_database() -> ForceTorqueDatabase:
    """Get the database instance"""
    return database

def get_summary() -> Dict[str, Any]:
    """Get database summary"""
    return database.get_summary()

if __name__ == "__main__":
    # Example usage
    db = get_database()
    summary = db.get_summary()
    
    print(f"Force/Torque Control Database")
    print(f"=============================")
    print(f"Section: {summary['taxonomy_section']} - {summary['section_name']}")
    print(f"Total Architectures: {summary['total_architectures']}")
    print(f"Total Tasks: {summary['total_tasks']}")
    print(f"\nArchitectures:")
    for arch_name in summary['architectures']:
        print(f"  - {arch_name}")
    print(f"\nTasks:")
    for task_name in summary['tasks']:
        print(f"  - {task_name}")