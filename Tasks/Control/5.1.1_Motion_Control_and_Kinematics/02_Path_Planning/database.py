"""
Path Planning Database
База данных для планирования путей
"""

from typing import List, Dict, Optional
from .architectures import (
    NeuralArchitecture,
    CNNPathPlanning,
    GNNPathPlanning,
    TransformerPathPlanning,
    MLPPathPlanning
)
from .tasks import (
    PathPlanningTask,
    VisualPathPlanning,
    GraphBasedPathPlanning,
    DynamicEnvironmentPathPlanning,
    TaskConstraints
)


class PathPlanningDatabase:
    """Database of neural architectures for path planning tasks"""
    
    def __init__(self):
        self.tasks = self._initialize_tasks()
    
    def _initialize_tasks(self) -> List[PathPlanningTask]:
        """Initialize all path planning tasks with their architectures"""
        
        # Visual Path Planning Task
        visual_task = VisualPathPlanning()
        visual_task.neural_architectures = [
            CNNPathPlanning(),
            MLPPathPlanning()
        ]
        
        # Graph-Based Path Planning Task
        graph_task = GraphBasedPathPlanning()
        graph_task.neural_architectures = [
            GNNPathPlanning()
        ]
        
        # Dynamic Environment Path Planning Task
        dynamic_task = DynamicEnvironmentPathPlanning()
        dynamic_task.neural_architectures = [
            TransformerPathPlanning(),
            CNNPathPlanning()
        ]
        
        return [visual_task, graph_task, dynamic_task]
    
    def get_task_by_name(self, task_name: str) -> Optional[PathPlanningTask]:
        """Get a specific path planning task by name"""
        for task in self.tasks:
            if task.task_name.lower() == task_name.lower():
                return task
        return None
    
    def get_all_tasks(self) -> List[PathPlanningTask]:
        """Get all path planning tasks"""
        return self.tasks
    
    def get_architectures_for_task(self, task_name: str) -> List[NeuralArchitecture]:
        """Get all architectures for a specific task"""
        task = self.get_task_by_name(task_name)
        if task:
            return task.neural_architectures
        return []
    
    def get_real_time_tasks(self) -> List[PathPlanningTask]:
        """Get all tasks that require real-time execution"""
        return [task for task in self.tasks 
                if task.constraints and task.constraints.real_time]
    
    def get_safety_critical_tasks(self) -> List[PathPlanningTask]:
        """Get all safety-critical tasks"""
        return [task for task in self.tasks 
                if task.constraints and task.constraints.safety_critical]
    
    def get_summary(self) -> Dict:
        """Get summary statistics about the database"""
        return {
            "taxonomy_section": "5.1.1.2",
            "section_name": "Path Planning",
            "total_tasks": len(self.tasks),
            "tasks": [task.task_name for task in self.tasks],
            "total_architectures": sum(len(task.neural_architectures) for task in self.tasks),
            "real_time_tasks": len(self.get_real_time_tasks()),
            "safety_critical_tasks": len(self.get_safety_critical_tasks())
        }


# Example usage
if __name__ == "__main__":
    db = PathPlanningDatabase()
    
    print("Path Planning Database initialized:")
    summary = db.get_summary()
    print(f"- Section: {summary['taxonomy_section']} - {summary['section_name']}")
    print(f"- Total tasks: {summary['total_tasks']}")
    print(f"- Total architectures: {summary['total_architectures']}")
    print(f"- Real-time tasks: {summary['real_time_tasks']}")
    print(f"- Safety-critical tasks: {summary['safety_critical_tasks']}")
    
    print("\nTasks:")
    for task in db.get_all_tasks():
        print(f"  - {task.task_name}: {len(task.neural_architectures)} architectures")
