"""
Tasks for Trajectory Planning

Каталог задач планирования траекторий с описанием и характеристиками
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

# Use absolute imports for standalone usage
try:
    from .architectures import NeuralArchitecture, ArchitectureType
except ImportError:
    from architectures import NeuralArchitecture, ArchitectureType


@dataclass
class TaskConstraints:
    """Ограничения и требования задачи"""
    real_time: bool
    safety_critical: bool
    latency_requirements: str  # "microseconds", "milliseconds", "seconds"
    reliability: float  # 0.0 to 1.0
    hardware_constraints: List[str]
    sample_efficiency_requirement: str  # "Low", "Medium", "High"


@dataclass
class ControlTask:
    """Описание задачи управления"""
    task_name: str
    description: str
    neural_architectures: List[NeuralArchitecture]
    constraints: TaskConstraints
    typical_applications: List[str]
    benchmark_datasets: List[str]
    related_tasks: List[str] = field(default_factory=list)


def get_trajectory_tasks() -> List[ControlTask]:
    """Получить все задачи планирования траекторий"""
    
    # Import architectures - handle both relative and absolute imports
    try:
        from .architectures import get_trajectory_architectures
    except ImportError:
        from architectures import get_trajectory_architectures
    
    all_archs = {arch.architecture_type.name: arch for arch in get_trajectory_architectures()}
    
    # Task 1: Dynamic Obstacle Avoidance
    dynamic_obstacle_task = ControlTask(
        task_name="Dynamic Obstacle Avoidance",
        description="Planning trajectories that avoid moving obstacles in real-time",
        neural_architectures=[
            all_archs.get("LSTM"),
            all_archs.get("TRANSFORMER"),
            all_archs.get("PPO")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.99,
            hardware_constraints=["GPU", "Real-time processor", "Obstacle detection sensors"],
            sample_efficiency_requirement="Medium"
        ),
        typical_applications=[
            "Autonomous vehicle navigation",
            "Drone flight in populated areas",
            "Mobile robot in warehouses",
            "Human-robot collaborative environments"
        ],
        benchmark_datasets=[
            "ARGOVERSE",
            "nuScenes",
            "KITTI Tracking",
            "Dynamic Obstacle Avoidance Dataset"
        ],
        related_tasks=["Path Planning", "Motion Prediction", "Collision Detection"]
    )
    
    # Task 2: Time-Optimal Trajectory Generation
    time_optimal_task = ControlTask(
        task_name="Time-Optimal Trajectory Generation",
        description="Generating trajectories that minimize execution time while respecting dynamics constraints",
        neural_architectures=[
            all_archs.get("PINN"),
            all_archs.get("NEURAL_ODE"),
            all_archs.get("SAC")
        ],
        constraints=TaskConstraints(
            real_time=False,
            safety_critical=True,
            latency_requirements="seconds",
            reliability=0.995,
            hardware_constraints=["High-performance CPU/GPU", "Accurate dynamics model"],
            sample_efficiency_requirement="High"
        ),
        typical_applications=[
            "Industrial robot manipulation",
            "Quadrotor racing",
            "Autonomous vehicle overtaking",
            "Pick-and-place optimization"
        ],
        benchmark_datasets=[
            "Robotics Trajectory Dataset",
            "Time-Optimal Path Parametrization Benchmark",
            "Dynamic Motion Primitives Dataset"
        ],
        related_tasks=["Trajectory Optimization", "Motion Planning", "Dynamic Constraints"]
    )
    
    # Task 3: Smooth Trajectory Generation
    smooth_traj_task = ControlTask(
        task_name="Smooth Trajectory Generation",
        description="Generating continuously differentiable trajectories with bounded jerk and acceleration",
        neural_architectures=[
            all_archs.get("NEURAL_ODE"),
            all_archs.get("LSTM"),
            all_archs.get("PINN")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=False,
            latency_requirements="milliseconds",
            reliability=0.95,
            hardware_constraints=["Standard processor", "Trajectory executor"],
            sample_efficiency_requirement="Medium"
        ),
        typical_applications=[
            "Camera motion control",
            "Surgical robotics",
            "Service robot navigation",
            "Animation and simulation"
        ],
        benchmark_datasets=[
            "Smooth Motion Dataset",
            "Minimum Jerk Trajectories",
            "Robot Motion Capture Data"
        ],
        related_tasks=["Trajectory Smoothing", "Motion Blending", "Path Refinement"]
    )
    
    # Task 4: Multi-Agent Trajectory Planning
    multi_agent_task = ControlTask(
        task_name="Multi-Agent Trajectory Planning",
        description="Coordinating trajectories of multiple agents to avoid collisions and achieve goals",
        neural_architectures=[
            all_archs.get("TRANSFORMER"),
            all_archs.get("GNN"),
            all_archs.get("PPO")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.99,
            hardware_constraints=["Distributed computing", "Communication network", "Shared state estimation"],
            sample_efficiency_requirement="Low"
        ),
        typical_applications=[
            "Swarm robotics",
            "Autonomous vehicle fleets",
            "Drone swarms",
            "Warehouse robot coordination"
        ],
        benchmark_datasets=[
            "Multi-Agent Particle Environment",
            "Crowd Simulation Dataset",
            "Vehicle Platooning Data"
        ],
        related_tasks=["Collision Avoidance", "Formation Control", "Task Allocation"]
    )
    
    # Task 5: Constraint-Aware Trajectory Planning
    constraint_aware_task = ControlTask(
        task_name="Constraint-Aware Trajectory Planning",
        description="Planning trajectories that satisfy complex kinematic, dynamic, and environmental constraints",
        neural_architectures=[
            all_archs.get("PINN"),
            all_archs.get("NEURAL_ODE"),
            all_archs.get("TRANSFORMER")
        ],
        constraints=TaskConstraints(
            real_time=False,
            safety_critical=True,
            latency_requirements="seconds",
            reliability=0.999,
            hardware_constraints=["High-performance computing", "Constraint solver"],
            sample_efficiency_requirement="High"
        ),
        typical_applications=[
            "Legged robot locomotion",
            "Manipulator in confined spaces",
            "Underwater vehicle navigation",
            "Spacecraft maneuvering"
        ],
        benchmark_datasets=[
            "Constrained Motion Planning Benchmark",
            "Kinematic Constraints Dataset",
            "Dynamic Feasibility Dataset"
        ],
        related_tasks=["Constraint Satisfaction", "Feasibility Analysis", "Motion Validation"]
    )
    
    # Task 6: Learning from Demonstration Trajectories
    lfd_task = ControlTask(
        task_name="Learning from Demonstration (LfD) Trajectories",
        description="Learning trajectory patterns from human or expert demonstrations",
        neural_architectures=[
            all_archs.get("LSTM"),
            all_archs.get("VAE"),
            all_archs.get("TRANSFORMER")
        ],
        constraints=TaskConstraints(
            real_time=False,
            safety_critical=False,
            latency_requirements="seconds",
            reliability=0.9,
            hardware_constraints=["Motion capture system", "Demonstration recording"],
            sample_efficiency_requirement="High"
        ),
        typical_applications=[
            "Robot programming by demonstration",
            "Skill learning",
            "Imitation learning",
            "Human-like motion generation"
        ],
        benchmark_datasets=[
            "CMU Motion Capture Database",
            "Robot Learning from Demonstration Dataset",
            "Human Activity Recognition Dataset"
        ],
        related_tasks=["Imitation Learning", "Skill Transfer", "Motion Retargeting"]
    )
    
    return [
        dynamic_obstacle_task,
        time_optimal_task,
        smooth_traj_task,
        multi_agent_task,
        constraint_aware_task,
        lfd_task
    ]


class TaskCatalog:
    """Каталог задач с методами поиска и фильтрации"""
    
    def __init__(self):
        self.tasks = get_trajectory_tasks()
        self._index_by_name()
    
    def _index_by_name(self):
        """Создать индекс по именам задач"""
        self.by_name = {task.task_name: task for task in self.tasks}
    
    def get_by_name(self, name: str) -> Optional[ControlTask]:
        """Получить задачу по имени"""
        return self.by_name.get(name)
    
    def get_real_time_tasks(self) -> List[ControlTask]:
        """Получить задачи реального времени"""
        return [task for task in self.tasks if task.constraints.real_time]
    
    def get_safety_critical_tasks(self) -> List[ControlTask]:
        """Получить safety-critical задачи"""
        return [task for task in self.tasks if task.constraints.safety_critical]
    
    def search_by_application(self, keyword: str) -> List[ControlTask]:
        """Поиск задач по ключевым словам в приложениях"""
        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks
            if any(keyword_lower in app.lower() for app in task.typical_applications)
        ]
    
    def get_all(self) -> List[ControlTask]:
        """Получить все задачи"""
        return self.tasks
    
    def summary(self) -> Dict:
        """Получить сводную статистику"""
        return {
            "total_tasks": len(self.tasks),
            "real_time_tasks": len(self.get_real_time_tasks()),
            "safety_critical_tasks": len(self.get_safety_critical_tasks()),
            "tasks": [task.task_name for task in self.tasks],
            "latency_distribution": self._get_latency_distribution()
        }
    
    def _get_latency_distribution(self) -> Dict[str, int]:
        """Распределение задач по требованиям к задержке"""
        dist = {}
        for task in self.tasks:
            lat = task.constraints.latency_requirements
            dist[lat] = dist.get(lat, 0) + 1
        return dist
