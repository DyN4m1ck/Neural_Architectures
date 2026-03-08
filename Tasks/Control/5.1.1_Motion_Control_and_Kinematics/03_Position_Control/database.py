"""
Position Control Database
База данных для управления положением
"""

from typing import List, Dict, Optional
from .architectures import (
    NeuralArchitecture,
    MLPPositionControl,
    RNNPositionControl,
    PIDNeuralEnhancement,
    TransformerPositionControl
)
from .tasks import (
    PositionControlTask,
    PrecisionPositionControl,
    MultiAxisPositionControl,
    AdaptivePositionControl,
    TaskConstraints
)


class PositionControlDatabase:
    """Database of neural architectures for position control tasks"""
    
    def __init__(self):
        self.tasks = self._initialize_tasks()
    
    def _initialize_tasks(self) -> List[PositionControlTask]:
        """Initialize all position control tasks with their architectures"""
        
        # Precision Position Control Task
        precision_task = PrecisionPositionControl()
        precision_task.neural_architectures = [
            MLPPositionControl(),
            PIDNeuralEnhancement()
        ]
        
        # Multi-Axis Position Control Task
        multi_axis_task = MultiAxisPositionControl()
        multi_axis_task.neural_architectures = [
            TransformerPositionControl(),
            MLPPositionControl()
        ]
        
        # Adaptive Position Control Task
        adaptive_task = AdaptivePositionControl()
        adaptive_task.neural_architectures = [
            RNNPositionControl(),
            PIDNeuralEnhancement()
        ]
        
        return [precision_task, multi_axis_task, adaptive_task]
    
    def get_task_by_name(self, task_name: str) -> Optional[PositionControlTask]:
        """Get a specific position control task by name"""
        for task in self.tasks:
            if task.task_name.lower() == task_name.lower():
                return task
        return None
    
    def get_all_tasks(self) -> List[PositionControlTask]:
        """Get all position control tasks"""
        return self.tasks
    
    def get_architectures_for_task(self, task_name: str) -> List[NeuralArchitecture]:
        """Get all architectures for a specific task"""
        task = self.get_task_by_name(task_name)
        if task:
            return task.neural_architectures
        return []
    
    def get_real_time_tasks(self) -> List[PositionControlTask]:
        """Get all tasks that require real-time execution"""
        return [task for task in self.tasks 
                if task.constraints and task.constraints.real_time]
    
    def get_safety_critical_tasks(self) -> List[PositionControlTask]:
        """Get all safety-critical tasks"""
        return [task for task in self.tasks 
                if task.constraints and task.constraints.safety_critical]
    
    def get_summary(self) -> Dict:
        """Get summary statistics about the database"""
        return {
            "taxonomy_section": "5.1.1.3",
            "section_name": "Position Control",
            "total_tasks": len(self.tasks),
            "tasks": [task.task_name for task in self.tasks],
            "total_architectures": sum(len(task.neural_architectures) for task in self.tasks),
            "real_time_tasks": len(self.get_real_time_tasks()),
            "safety_critical_tasks": len(self.get_safety_critical_tasks())
        }


# Example usage
if __name__ == "__main__":
    db = PositionControlDatabase()
    
    print("Position Control Database initialized:")
    summary = db.get_summary()
    print(f"- Section: {summary['taxonomy_section']} - {summary['section_name']}")
    print(f"- Total tasks: {summary['total_tasks']}")
    print(f"- Total architectures: {summary['total_architectures']}")
    print(f"- Real-time tasks: {summary['real_time_tasks']}")
    print(f"- Safety-critical tasks: {summary['safety_critical_tasks']}")
    
    print("\nTasks:")
    for task in db.get_all_tasks():
        print(f"  - {task.task_name}: {len(task.neural_architectures)} architectures")