"""
Impedance and Admittance Control - Comprehensive Database
==========================================================

This module provides a comprehensive database of neural network architectures
and control tasks for impedance and admittance control applications.
"""

from typing import List, Dict, Optional
from .architectures import (
    NeuralArchitecture, 
    ArchitectureType,
    get_architectures_for_impedance_learning,
    get_architectures_for_admittance_control,
    get_architectures_for_variable_stiffness,
    get_architectures_for_contact_rich_manipulation,
    get_architectures_for_human_robot_interaction,
    get_all_architectures
)
from .tasks import (
    ControlTask,
    TaskConstraints,
    ImpedanceAdmittanceTasks
)


class ImpedanceAdmittanceDatabase:
    """
    Comprehensive database for impedance and admittance control.
    
    Provides access to neural architectures, tasks, and utility methods
    for querying and filtering based on requirements.
    """
    
    def __init__(self):
        """Initialize the database with all tasks and architectures"""
        self.tasks = self._initialize_tasks()
        self.architectures = get_all_architectures()
    
    def _initialize_tasks(self) -> List[ControlTask]:
        """Initialize all tasks with their corresponding architectures"""
        tasks = ImpedanceAdmittanceTasks.get_all_tasks()
        
        # Map tasks to their relevant architectures
        task_arch_mapping = {
            "Impedance Parameter Learning": get_architectures_for_impedance_learning(),
            "Admittance Control": get_architectures_for_admittance_control(),
            "Variable Stiffness Control": get_architectures_for_variable_stiffness(),
            "Contact-Rich Manipulation": get_architectures_for_contact_rich_manipulation(),
            "Human-Robot Interaction": get_architectures_for_human_robot_interaction()
        }
        
        # Populate architectures for each task
        for task in tasks:
            if task.task_name in task_arch_mapping:
                task.neural_architectures = task_arch_mapping[task.task_name]
        
        return tasks
    
    def get_all_tasks(self) -> List[ControlTask]:
        """Get all control tasks in the database"""
        return self.tasks
    
    def get_task_by_name(self, task_name: str) -> Optional[ControlTask]:
        """
        Get a specific task by name.
        
        Args:
            task_name: Name of the task (case-insensitive)
            
        Returns:
            ControlTask if found, None otherwise
        """
        for task in self.tasks:
            if task.task_name.lower() == task_name.lower():
                return task
        return None
    
    def get_all_architectures(self) -> List[NeuralArchitecture]:
        """Get all neural architectures in the database"""
        return self.architectures
    
    def get_architectures_by_type(self, arch_type: ArchitectureType) -> List[NeuralArchitecture]:
        """
        Get all architectures of a specific type.
        
        Args:
            arch_type: The architecture type to filter by
            
        Returns:
            List of matching architectures
        """
        return [arch for arch in self.architectures if arch.architecture_type == arch_type]
    
    def get_architectures_for_task(self, task_name: str) -> List[NeuralArchitecture]:
        """
        Get all architectures applicable to a specific task.
        
        Args:
            task_name: Name of the task
            
        Returns:
            List of applicable architectures
        """
        task = self.get_task_by_name(task_name)
        if task:
            return task.neural_architectures
        return []
    
    def get_tasks_requiring_real_time(self) -> List[ControlTask]:
        """Get all tasks that require real-time execution"""
        return [task for task in self.tasks if task.constraints.real_time]
    
    def get_safety_critical_tasks(self) -> List[ControlTask]:
        """Get all safety-critical tasks"""
        return [task for task in self.tasks if task.constraints.safety_critical]
    
    def get_tasks_by_latency_requirement(self, latency_level: str) -> List[ControlTask]:
        """
        Get tasks by latency requirement.
        
        Args:
            latency_level: 'microseconds', 'milliseconds', or 'seconds'
            
        Returns:
            List of matching tasks
        """
        return [task for task in self.tasks 
                if task.constraints.latency_requirements == latency_level]
    
    def get_architectures_by_capability(self, 
                                        real_time: Optional[bool] = None,
                                        safety_critical: Optional[bool] = None,
                                        sample_efficiency: Optional[str] = None) -> List[NeuralArchitecture]:
        """
        Filter architectures by capabilities.
        
        Args:
            real_time: Filter by real-time capability (None = don't filter)
            safety_critical: Filter by safety-critical usage (None = don't filter)
            sample_efficiency: Filter by sample efficiency level (None = don't filter)
            
        Returns:
            List of matching architectures
        """
        result = self.architectures
        
        if real_time is not None:
            result = [arch for arch in result if arch.real_time_capable == real_time]
        
        if safety_critical is not None:
            result = [arch for arch in result if arch.safety_critical == safety_critical]
        
        if sample_efficiency is not None:
            result = [arch for arch in result if arch.sample_efficiency == sample_efficiency]
        
        return result
    
    def get_summary_statistics(self) -> Dict:
        """
        Get summary statistics about the database.
        
        Returns:
            Dictionary with counts and statistics
        """
        return {
            "total_tasks": len(self.tasks),
            "total_architectures": len(self.architectures),
            "real_time_tasks": len(self.get_tasks_requiring_real_time()),
            "safety_critical_tasks": len(self.get_safety_critical_tasks()),
            "microsecond_latency_tasks": len(self.get_tasks_by_latency_requirement("microseconds")),
            "millisecond_latency_tasks": len(self.get_tasks_by_latency_requirement("milliseconds")),
            "real_time_architectures": len([a for a in self.architectures if a.real_time_capable]),
            "architecture_types": list(set(arch.architecture_type.value for arch in self.architectures))
        }
    
    def print_summary(self):
        """Print a human-readable summary of the database"""
        stats = self.get_summary_statistics()
        print("=" * 60)
        print("IMPEDANCE AND ADMITTANCE CONTROL DATABASE SUMMARY")
        print("=" * 60)
        print(f"Total Tasks: {stats['total_tasks']}")
        print(f"Total Architectures: {stats['total_architectures']}")
        print("-" * 60)
        print("Task Requirements:")
        print(f"  - Real-time tasks: {stats['real_time_tasks']}")
        print(f"  - Safety-critical tasks: {stats['safety_critical_tasks']}")
        print(f"  - Microsecond latency: {stats['microsecond_latency_tasks']}")
        print(f"  - Millisecond latency: {stats['millisecond_latency_tasks']}")
        print("-" * 60)
        print("Architecture Capabilities:")
        print(f"  - Real-time capable: {stats['real_time_architectures']}")
        print("-" * 60)
        print("Architecture Types:")
        for arch_type in stats['architecture_types']:
            print(f"  - {arch_type}")
        print("=" * 60)


# Convenience function to create database instance
def get_database() -> ImpedanceAdmittanceDatabase:
    """Create and return a new database instance"""
    return ImpedanceAdmittanceDatabase()


# Initialize default database instance
database = ImpedanceAdmittanceDatabase()

if __name__ == "__main__":
    # Example usage
    db = get_database()
    db.print_summary()
    
    print("\nExample: Getting architectures for Variable Stiffness Control")
    archs = db.get_architectures_for_task("Variable Stiffness Control")
    for arch in archs:
        print(f"  - {arch.architecture_type.value}: {arch.use_case}")