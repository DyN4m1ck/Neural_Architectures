"""
Velocity Control Database
=========================
Subsection 5.1.1.4: Velocity Control

Database of neural network architectures and tasks for velocity control applications.
Provides unified access to all velocity control capabilities.
"""

from typing import List, Dict, Optional
from .architectures import VelocityArchitecture, ArchitectureType, get_velocity_architecture, list_all_architectures
from .tasks import VelocityControlTask, TaskConstraints, get_velocity_task, list_all_tasks

class VelocityControlDatabase:
    """
    Centralized database for velocity control architectures and tasks.
    
    Provides methods to:
    - Query available architectures
    - Query available tasks
    - Find architectures suitable for specific tasks
    - Get summary statistics
    """
    
    def __init__(self):
        """Initialize the velocity control database"""
        self._architectures = self._load_architectures()
        self._tasks = self._load_tasks()
    
    def _load_architectures(self) -> Dict[str, VelocityArchitecture]:
        """Load all available velocity control architectures"""
        return {
            "GRUVelocityController": get_velocity_architecture("GRUVelocityController"),
            "LSTMVelocityProfiler": get_velocity_architecture("LSTMVelocityProfiler"),
            "CNNVelocityEstimator": get_velocity_architecture("CNNVelocityEstimator"),
            "TransformerVelocityPlanner": get_velocity_architecture("TransformerVelocityPlanner"),
            "PINNVelocityController": get_velocity_architecture("PINNVelocityController")
        }
    
    def _load_tasks(self) -> Dict[str, VelocityControlTask]:
        """Load all available velocity control tasks"""
        return {
            "VelocityTrackingTask": get_velocity_task("VelocityTrackingTask"),
            "SmoothProfileGenerationTask": get_velocity_task("SmoothProfileGenerationTask"),
            "CoordinatedVelocityControlTask": get_velocity_task("CoordinatedVelocityControlTask"),
            "DisturbanceRejectionTask": get_velocity_task("DisturbanceRejectionTask"),
            "JerkLimitedMotionTask": get_velocity_task("JerkLimitedMotionTask")
        }
    
    def get_all_architectures(self) -> List[VelocityArchitecture]:
        """Get all available architectures"""
        return [arch for arch in self._architectures.values() if arch is not None]
    
    def get_all_tasks(self) -> List[VelocityControlTask]:
        """Get all available tasks"""
        return [task for task in self._tasks.values() if task is not None]
    
    def get_architecture_by_name(self, name: str) -> Optional[VelocityArchitecture]:
        """Get a specific architecture by name"""
        return self._architectures.get(name)
    
    def get_task_by_name(self, name: str) -> Optional[VelocityControlTask]:
        """Get a specific task by name"""
        return self._tasks.get(name)
    
    def get_real_time_architectures(self) -> List[VelocityArchitecture]:
        """Get all architectures capable of real-time execution"""
        return [arch for arch in self.get_all_architectures() if arch.real_time_capable]
    
    def get_safety_critical_tasks(self) -> List[VelocityControlTask]:
        """Get all safety-critical tasks"""
        return [task for task in self.get_all_tasks() if task.constraints.safety_critical]
    
    def get_architectures_for_task(self, task_name: str) -> List[VelocityArchitecture]:
        """Get architectures suitable for a specific task"""
        task = self.get_task_by_name(task_name)
        if task:
            return task.neural_architectures
        return []
    
    def get_summary(self) -> Dict:
        """Get summary statistics of the database"""
        all_architectures = self.get_all_architectures()
        all_tasks = self.get_all_tasks()
        
        return {
            "taxonomy_section": "5.1.1.4",
            "section_name": "Velocity Control",
            "section_name_ru": "Управление скоростью",
            "total_architectures": len(all_architectures),
            "total_tasks": len(all_tasks),
            "real_time_architectures": len([a for a in all_architectures if a.real_time_capable]),
            "safety_critical_tasks": len([t for t in all_tasks if t.constraints.safety_critical]),
            "architecture_types": list(set(arch.architecture_type.value for arch in all_architectures)),
            "task_names": [task.task_name for task in all_tasks]
        }
    
    def print_summary(self):
        """Print a formatted summary of the database"""
        summary = self.get_summary()
        print("=" * 60)
        print(f"Velocity Control Database Summary")
        print("=" * 60)
        print(f"Taxonomy Section: {summary['taxonomy_section']}")
        print(f"Section Name: {summary['section_name']} ({summary['section_name_ru']})")
        print(f"Total Architectures: {summary['total_architectures']}")
        print(f"  - Real-time Capable: {summary['real_time_architectures']}")
        print(f"Total Tasks: {summary['total_tasks']}")
        print(f"  - Safety Critical: {summary['safety_critical_tasks']}")
        print(f"\nArchitecture Types:")
        for arch_type in summary['architecture_types']:
            print(f"  - {arch_type}")
        print(f"\nTasks:")
        for task_name in summary['task_names']:
            print(f"  - {task_name}")
        print("=" * 60)


# Convenience function to get database instance
def get_velocity_control_database() -> VelocityControlDatabase:
    """Get an instance of the velocity control database"""
    return VelocityControlDatabase()


# Initialize database when module is imported
database = VelocityControlDatabase()

if __name__ == "__main__":
    # Print summary when run directly
    database.print_summary()