"""
Velocity Control - Database Module
Section 5.1.1.04
Unified database interface for velocity control architectures and tasks.
"""

from typing import List, Dict, Optional
from .architectures import VelocityControlArchitectures, VelocityArchitecture, ArchitectureType
from .tasks import VelocityControlTasks, VelocityControlTask


class VelocityControlDatabase:
    """
    Unified database for velocity control information.
    
    This class provides a centralized interface to access both neural network
    architectures and task specifications for velocity control applications.
    It enables querying, filtering, and cross-referencing between architectures
    and tasks.
    """
    
    def __init__(self):
        self.architectures_catalog = VelocityControlArchitectures()
        self.tasks_catalog = VelocityControlTasks()
    
    def get_all_architectures(self) -> List[VelocityArchitecture]:
        """Get all available architectures"""
        return self.architectures_catalog.get_all_architectures()
    
    def get_all_tasks(self) -> List[VelocityControlTask]:
        """Get all available tasks"""
        return self.tasks_catalog.get_all_tasks()
    
    def get_architecture_by_type(self, arch_type: ArchitectureType) -> Optional[VelocityArchitecture]:
        """Get architecture by type"""
        return self.architectures_catalog.get_architecture_by_type(arch_type)
    
    def get_task_by_name(self, task_name: str) -> Optional[VelocityControlTask]:
        """Get task by name"""
        return self.tasks_catalog.get_task_by_name(task_name)
    
    def get_real_time_architectures(self) -> List[VelocityArchitecture]:
        """Get architectures capable of real-time operation"""
        return self.architectures_catalog.get_real_time_architectures()
    
    def get_safety_critical_architectures(self) -> List[VelocityArchitecture]:
        """Get safety-critical architectures"""
        return self.architectures_catalog.get_safety_critical_architectures()
    
    def get_real_time_tasks(self) -> List[VelocityControlTask]:
        """Get tasks requiring real-time execution"""
        return self.tasks_catalog.get_real_time_tasks()
    
    def get_safety_critical_tasks(self) -> List[VelocityControlTask]:
        """Get safety-critical tasks"""
        return self.tasks_catalog.get_safety_critical_tasks()
    
    def find_architectures_for_task(self, task_name: str) -> List[VelocityArchitecture]:
        """Find recommended architectures for a specific task"""
        task = self.get_task_by_name(task_name)
        if not task:
            return []
        
        recommended_types = task.recommended_architectures
        architectures = []
        for arch_type in recommended_types:
            arch = self.get_architecture_by_type(arch_type)
            if arch:
                architectures.append(arch)
        return architectures
    
    def find_tasks_for_architecture(self, arch_type: ArchitectureType) -> List[VelocityControlTask]:
        """Find tasks that recommend a specific architecture"""
        matching_tasks = []
        for task in self.get_all_tasks():
            if arch_type in task.recommended_architectures:
                matching_tasks.append(task)
        return matching_tasks
    
    def get_summary(self) -> Dict:
        """Get comprehensive summary of the database"""
        arch_summary = self.architectures_catalog.summary()
        task_summary = self.tasks_catalog.summary()
        
        return {
            "section": "5.1.1.04",
            "section_name": "Velocity Control",
            "parent_section": "5.1.1 Motion Control and Kinematics",
            "architectures": arch_summary,
            "tasks": task_summary,
            "total_architectures": arch_summary["total_architectures"],
            "total_tasks": task_summary["total_tasks"],
            "real_time_capable_architectures": arch_summary["real_time_capable"],
            "safety_critical_architectures": arch_summary["safety_critical"],
            "real_time_tasks": task_summary["real_time_tasks"],
            "safety_critical_tasks": task_summary["safety_critical_tasks"]
        }
    
    def export_to_dict(self) -> Dict:
        """Export complete database to dictionary format"""
        return {
            "metadata": self.get_summary(),
            "architectures": [
                {
                    "type": arch.architecture_type.value,
                    "use_case": arch.use_case,
                    "input_format": arch.input_format,
                    "output_format": arch.output_format,
                    "advantages": arch.advantages,
                    "limitations": arch.limitations,
                    "integration_with_classical": arch.integration_with_classical,
                    "example_papers": arch.example_papers,
                    "computational_complexity": arch.computational_complexity,
                    "memory_requirements": arch.memory_requirements,
                    "sample_efficiency": arch.sample_efficiency,
                    "real_time_capable": arch.real_time_capable,
                    "safety_critical": arch.safety_critical
                }
                for arch in self.get_all_architectures()
            ],
            "tasks": [
                {
                    "task_name": task.task_name,
                    "description": task.description,
                    "typical_applications": task.typical_applications,
                    "input_specifications": task.input_specifications,
                    "output_specifications": task.output_specifications,
                    "recommended_architectures": [a.value for a in task.recommended_architectures],
                    "constraints": {
                        "real_time": task.constraints.real_time if task.constraints else None,
                        "safety_critical": task.constraints.safety_critical if task.constraints else None,
                        "latency_requirements": task.constraints.latency_requirements if task.constraints else None,
                        "reliability": task.constraints.reliability if task.constraints else None,
                        "hardware_constraints": task.constraints.hardware_constraints if task.constraints else None,
                        "sample_efficiency_requirement": task.constraints.sample_efficiency_requirement if task.constraints else None
                    } if task.constraints else None,
                    "benchmark_datasets": task.benchmark_datasets,
                    "performance_metrics": task.performance_metrics
                }
                for task in self.get_all_tasks()
            ]
        }
    
    def print_summary(self):
        """Print formatted summary to console"""
        summary = self.get_summary()
        print("=" * 60)
        print(f"VELOCITY CONTROL DATABASE - Section {summary['section']}")
        print("=" * 60)
        print(f"Parent Section: {summary['parent_section']}")
        print(f"\nTotal Architectures: {summary['total_architectures']}")
        print(f"  - Real-time capable: {summary['real_time_capable_architectures']}")
        print(f"  - Safety-critical: {summary['safety_critical_architectures']}")
        print(f"\nTotal Tasks: {summary['total_tasks']}")
        print(f"  - Real-time required: {summary['real_time_tasks']}")
        print(f"  - Safety-critical: {summary['safety_critical_tasks']}")
        print("\nArchitecture Types:")
        for arch_type in summary['architectures']['architecture_types']:
            print(f"  - {arch_type}")
        print("\nTask Names:")
        for task_name in summary['tasks']['task_names']:
            print(f"  - {task_name}")
        print("=" * 60)


# Convenience function to create database instance
def create_velocity_control_database() -> VelocityControlDatabase:
    """Create and return a VelocityControlDatabase instance"""
    return VelocityControlDatabase()


# Initialize default database instance
database = VelocityControlDatabase()

if __name__ == "__main__":
    # Example usage
    db = create_velocity_control_database()
    db.print_summary()
    
    print("\n\nExample: Architectures for Smooth Velocity Profiling")
    archs = db.find_architectures_for_task("Smooth Velocity Profiling")
    for arch in archs:
        print(f"  - {arch.architecture_type.value}: {arch.use_case}")
    
    print("\n\nExample: Tasks using GRU Architecture")
    tasks = db.find_tasks_for_architecture(ArchitectureType.GRU)
    for task in tasks:
        print(f"  - {task.task_name}: {task.description}")