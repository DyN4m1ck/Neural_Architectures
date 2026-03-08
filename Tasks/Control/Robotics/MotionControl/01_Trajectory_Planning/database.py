"""
Database for Trajectory Planning

This module provides a database interface for trajectory planning tasks and architectures.
"""

from typing import List, Optional, Dict, Any
from .architectures import NeuralArchitecture, get_trajectory_planning_architectures
from .tasks import ControlTask, TaskConstraints, get_trajectory_planning_tasks


class TrajectoryPlanningDatabase:
    """
    Database class for managing trajectory planning tasks and architectures.
    
    Provides methods to query and retrieve information about neural network
    architectures applicable to trajectory planning tasks.
    """
    
    def __init__(self):
        """Initialize the trajectory planning database."""
        self.tasks = get_trajectory_planning_tasks()
        self.architectures = get_trajectory_planning_architectures()
    
    def get_all_tasks(self) -> List[ControlTask]:
        """Get all trajectory planning tasks."""
        return self.tasks
    
    def get_all_architectures(self) -> List[NeuralArchitecture]:
        """Get all neural architectures for trajectory planning."""
        return self.architectures
    
    def get_task_by_name(self, task_name: str) -> Optional[ControlTask]:
        """
        Get a specific task by name.
        
        Args:
            task_name: Name of the task to find
            
        Returns:
            ControlTask if found, None otherwise
        """
        for task in self.tasks:
            if task.task_name.lower() == task_name.lower():
                return task
        return None
    
    def get_architectures_for_task(self, task_name: str) -> List[NeuralArchitecture]:
        """
        Get all architectures applicable to a specific task.
        
        Args:
            task_name: Name of the task
            
        Returns:
            List of NeuralArchitecture objects
        """
        task = self.get_task_by_name(task_name)
        if task:
            return task.neural_architectures
        return []
    
    def get_real_time_capable_architectures(self) -> List[NeuralArchitecture]:
        """Get all architectures capable of real-time execution."""
        return [arch for arch in self.architectures if arch.real_time_capable]
    
    def get_safety_critical_architectures(self) -> List[NeuralArchitecture]:
        """Get all architectures used in safety-critical applications."""
        return [arch for arch in self.architectures if arch.safety_critical]
    
    def get_architecture_by_type(self, arch_type_name: str) -> Optional[NeuralArchitecture]:
        """
        Get architecture by type name.
        
        Args:
            arch_type_name: Name of the architecture type
            
        Returns:
            NeuralArchitecture if found, None otherwise
        """
        for arch in self.architectures:
            if arch.architecture_type.name.lower() == arch_type_name.lower():
                return arch
        return None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert database contents to dictionary representation."""
        return {
            "taxonomy_section": "5.1.1",
            "subsection": "01_Trajectory_Planning",
            "subsection_name": "Trajectory Planning",
            "tasks": [task.to_dict() for task in self.tasks],
            "architectures": [arch.to_dict() for arch in self.architectures],
            "summary": {
                "total_tasks": len(self.tasks),
                "total_architectures": len(self.architectures),
                "real_time_capable": len(self.get_real_time_capable_architectures()),
                "safety_critical": len(self.get_safety_critical_architectures())
            }
        }
    
    def print_summary(self):
        """Print a summary of the database contents."""
        print("=" * 60)
        print("TRAJECTORY PLANNING DATABASE SUMMARY")
        print("=" * 60)
        print(f"Taxonomy Section: 5.1.1")
        print(f"Subsection: 01_Trajectory_Planning")
        print(f"Total Tasks: {len(self.tasks)}")
        print(f"Total Architectures: {len(self.architectures)}")
        print(f"Real-time Capable: {len(self.get_real_time_capable_architectures())}")
        print(f"Safety Critical: {len(self.get_safety_critical_architectures())}")
        print("\nTasks:")
        for task in self.tasks:
            print(f"  - {task.task_name}: {task.description[:60]}...")
        print("\nArchitectures:")
        for arch in self.architectures:
            print(f"  - {arch.architecture_type.value}: {arch.use_case[:50]}...")
        print("=" * 60)


# Global database instance
_database_instance: Optional[TrajectoryPlanningDatabase] = None


def get_database() -> TrajectoryPlanningDatabase:
    """
    Get or create the global trajectory planning database instance.
    
    Returns:
        TrajectoryPlanningDatabase instance
    """
    global _database_instance
    if _database_instance is None:
        _database_instance = TrajectoryPlanningDatabase()
    return _database_instance


# Initialize database on module import
db = get_database()
