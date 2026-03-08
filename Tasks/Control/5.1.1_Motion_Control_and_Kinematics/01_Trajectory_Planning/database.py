"""
Database for Trajectory Planning

Единая база данных для планирования траекторий, объединяющая архитектуры и задачи
"""

from typing import List, Dict, Optional

# Use absolute imports for standalone usage
try:
    from .architectures import NeuralArchitecture, ArchitectureCatalog, get_trajectory_architectures
    from .tasks import ControlTask, TaskCatalog, get_trajectory_tasks
except ImportError:
    from architectures import NeuralArchitecture, ArchitectureCatalog, get_trajectory_architectures
    from tasks import ControlTask, TaskCatalog, get_trajectory_tasks


class TrajectoryPlanningDatabase:
    """
    Центральная база данных для раздела "Планирование траекторий"
    
    Предоставляет доступ к:
    - Архитектурам нейронных сетей
    - Задачам управления
    - Связям между архитектурами и задачами
    - Методам поиска и фильтрации
    """
    
    def __init__(self):
        self.architecture_catalog = ArchitectureCatalog()
        self.task_catalog = TaskCatalog()
        self.architectures = self.architecture_catalog.get_all()
        self.tasks = self.task_catalog.get_all()
    
    def get_architecture_by_type(self, arch_type_name: str) -> Optional[NeuralArchitecture]:
        """Получить архитектуру по названию типа"""
        for arch in self.architectures:
            if arch.architecture_type.name == arch_type_name:
                return arch
        return None
    
    def get_task_by_name(self, task_name: str) -> Optional[ControlTask]:
        """Получить задачу по имени"""
        return self.task_catalog.get_by_name(task_name)
    
    def get_architectures_for_task(self, task_name: str) -> List[NeuralArchitecture]:
        """Получить все архитектуры, применимые к задаче"""
        task = self.get_task_by_name(task_name)
        if task:
            return task.neural_architectures
        return []
    
    def get_tasks_for_architecture(self, arch_type_name: str) -> List[ControlTask]:
        """Получить все задачи, где применяется данная архитектура"""
        matching_tasks = []
        for task in self.tasks:
            for arch in task.neural_architectures:
                if arch.architecture_type.name == arch_type_name:
                    matching_tasks.append(task)
                    break
        return matching_tasks
    
    def search_architectures(self, keyword: str) -> List[NeuralArchitecture]:
        """Поиск архитектур по ключевому слову"""
        return self.architecture_catalog.search_by_use_case(keyword)
    
    def search_tasks(self, keyword: str) -> List[ControlTask]:
        """Поиск задач по ключевому слову в приложениях"""
        return self.task_catalog.search_by_application(keyword)
    
    def get_real_time_capable_architectures(self) -> List[NeuralArchitecture]:
        """Получить архитектуры, поддерживающие реальное время"""
        return self.architecture_catalog.get_real_time_capable()
    
    def get_safety_critical_architectures(self) -> List[NeuralArchitecture]:
        """Получить архитектуры для safety-critical задач"""
        return self.architecture_catalog.get_safety_critical()
    
    def get_real_time_tasks(self) -> List[ControlTask]:
        """Получить задачи реального времени"""
        return self.task_catalog.get_real_time_tasks()
    
    def get_safety_critical_tasks(self) -> List[ControlTask]:
        """Получить safety-critical задачи"""
        return self.task_catalog.get_safety_critical_tasks()
    
    def get_compatible_architectures(self, task_name: str, 
                                      real_time_only: bool = False,
                                      safety_critical_only: bool = False) -> List[NeuralArchitecture]:
        """
        Получить совместимые архитектуры для задачи с фильтрами
        
        Args:
            task_name: Имя задачи
            real_time_only: Только архитектуры реального времени
            safety_critical_only: Только safety-critical архитектуры
        
        Returns:
            Список совместимых архитектур
        """
        task = self.get_task_by_name(task_name)
        if not task:
            return []
        
        candidates = task.neural_architectures
        
        if real_time_only:
            candidates = [a for a in candidates if a.real_time_capable]
        
        if safety_critical_only:
            candidates = [a for a in candidates if a.safety_critical]
        
        return candidates
    
    def summary(self) -> Dict:
        """Получить сводную статистику базы данных"""
        return {
            "taxonomy_section": "5.1.1",
            "subsection": "01",
            "name_ru": "Планирование траекторий",
            "name_en": "Trajectory Planning",
            "total_architectures": len(self.architectures),
            "total_tasks": len(self.tasks),
            "architecture_summary": self.architecture_catalog.summary(),
            "task_summary": self.task_catalog.summary(),
            "real_time_architectures": len(self.get_real_time_capable_architectures()),
            "safety_critical_architectures": len(self.get_safety_critical_architectures()),
            "real_time_tasks": len(self.get_real_time_tasks()),
            "safety_critical_tasks": len(self.get_safety_critical_tasks())
        }
    
    def export_to_dict(self) -> Dict:
        """Экспорт всей базы данных в словарь"""
        return {
            "metadata": self.summary(),
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
                for arch in self.architectures
            ],
            "tasks": [
                {
                    "task_name": task.task_name,
                    "description": task.description,
                    "architectures": [a.architecture_type.name for a in task.neural_architectures],
                    "constraints": {
                        "real_time": task.constraints.real_time,
                        "safety_critical": task.constraints.safety_critical,
                        "latency_requirements": task.constraints.latency_requirements,
                        "reliability": task.constraints.reliability,
                        "hardware_constraints": task.constraints.hardware_constraints,
                        "sample_efficiency_requirement": task.constraints.sample_efficiency_requirement
                    },
                    "typical_applications": task.typical_applications,
                    "benchmark_datasets": task.benchmark_datasets,
                    "related_tasks": task.related_tasks
                }
                for task in self.tasks
            ]
        }


# Singleton instance
_database_instance = None


def get_database() -> TrajectoryPlanningDatabase:
    """Получить экземпляр базы данных (singleton)"""
    global _database_instance
    if _database_instance is None:
        _database_instance = TrajectoryPlanningDatabase()
    return _database_instance


# Initialize on import
db = get_database()
