"""
Velocity Control Tasks
======================
Subsection 5.1.1.4: Velocity Control

Task definitions for velocity control applications:
- Velocity tracking with disturbance rejection
- Smooth profile generation
- Coordinated multi-axis velocity control
- Jerk-limited motion
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from .architectures import VelocityArchitecture, ArchitectureType

@dataclass
class TaskConstraints:
    """Constraints for velocity control tasks"""
    real_time: bool
    safety_critical: bool
    latency_requirements: str  # "microseconds", "milliseconds", "seconds"
    reliability: float  # 0.0 to 1.0
    hardware_constraints: List[str]
    sample_efficiency_requirement: str
    max_velocity: Optional[float] = None
    max_acceleration: Optional[float] = None
    max_jerk: Optional[float] = None

@dataclass
class VelocityControlTask:
    """Base class for velocity control tasks"""
    task_name: str
    description: str
    neural_architectures: List[VelocityArchitecture]
    constraints: TaskConstraints
    typical_applications: List[str]
    benchmark_datasets: List[str]
    input_dimensions: Dict[str, int]
    output_dimensions: Dict[str, int]

class VelocityTrackingTask(VelocityControlTask):
    """Velocity tracking with disturbance rejection"""
    
    def __init__(self):
        from .architectures import GRUVelocityController, PINNVelocityController
        
        architectures = [
            GRUVelocityController(),
            PINNVelocityController()
        ]
        
        constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="microseconds",
            reliability=0.999,
            hardware_constraints=["Encoder feedback", "High-bandwidth actuators", "Real-time controller"],
            sample_efficiency_requirement="Medium",
            max_velocity=10.0,
            max_acceleration=5.0,
            max_jerk=20.0
        )
        
        super().__init__(
            task_name="Velocity Tracking",
            description="Precise velocity tracking with active disturbance rejection and load compensation",
            neural_architectures=architectures,
            constraints=constraints,
            typical_applications=[
                "Conveyor belt speed control",
                "Spindle speed control in CNC machines",
                "Robot joint velocity control",
                "Vehicle cruise control"
            ],
            benchmark_datasets=[
                "Industrial Motor Control Dataset",
                "Robotics Velocity Tracking Benchmark",
                "Automotive Speed Control Data"
            ],
            input_dimensions={"state": 6, "reference": 3, "disturbances": 4},
            output_dimensions={"velocity_command": 3}
        )

class SmoothProfileGenerationTask(VelocityControlTask):
    """Smooth velocity profile generation with jerk limits"""
    
    def __init__(self):
        from .architectures import LSTMVelocityProfiler, GRUVelocityController
        
        architectures = [
            LSTMVelocityProfiler(),
            GRUVelocityController()
        ]
        
        constraints = TaskConstraints(
            real_time=True,
            safety_critical=False,
            latency_requirements="milliseconds",
            reliability=0.99,
            hardware_constraints=["Motion planner", "Trajectory generator"],
            sample_efficiency_requirement="Medium"
        )
        
        super().__init__(
            task_name="Smooth Profile Generation",
            description="Generation of smooth velocity profiles with bounded acceleration and jerk for comfortable and efficient motion",
            neural_architectures=architectures,
            constraints=constraints,
            typical_applications=[
                "Elevator motion control",
                "Camera gimbal smoothing",
                "Robotic arm motion planning",
                "Autonomous vehicle comfort optimization"
            ],
            benchmark_datasets=[
                "Smooth Motion Planning Dataset",
                "Jerk-Limited Trajectory Benchmark",
                "Comfort Optimization Data"
            ],
            input_dimensions={"waypoints": 10, "constraints": 6},
            output_dimensions={"velocity_profile": 100}
        )

class CoordinatedVelocityControlTask(VelocityControlTask):
    """Multi-axis coordinated velocity control"""
    
    def __init__(self):
        from .architectures import TransformerVelocityPlanner, GRUVelocityController
        
        architectures = [
            TransformerVelocityPlanner(),
            GRUVelocityController()
        ]
        
        constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.995,
            hardware_constraints=["Multi-axis controller", "Synchronized actuators", "Communication bus"],
            sample_efficiency_requirement="High"
        )
        
        super().__init__(
            task_name="Coordinated Velocity Control",
            description="Synchronized velocity control across multiple axes or robots for coordinated motion",
            neural_architectures=architectures,
            constraints=constraints,
            typical_applications=[
                "Multi-robot formation control",
                "Parallel kinematic machines",
                "Cooperative manipulation",
                "Swarm robotics velocity coordination"
            ],
            benchmark_datasets=[
                "Multi-Robot Coordination Dataset",
                "Formation Control Benchmark",
                "Cooperative Manipulation Data"
            ],
            input_dimensions={"agent_states": 18, "formation_params": 9, "environment": 12},
            output_dimensions={"velocity_commands": 18}
        )

class DisturbanceRejectionTask(VelocityControlTask):
    """Velocity control with active disturbance rejection"""
    
    def __init__(self):
        from .architectures import PINNVelocityController, CNNVelocityEstimator
        
        architectures = [
            PINNVelocityController(),
            CNNVelocityEstimator()
        ]
        
        constraints = TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="microseconds",
            reliability=0.9999,
            hardware_constraints=["Disturbance observer", "High-frequency sensing", "Fast actuators"],
            sample_efficiency_requirement="Low"
        )
        
        super().__init__(
            task_name="Disturbance Rejection",
            description="Active rejection of external disturbances and model uncertainties in velocity control",
            neural_architectures=architectures,
            constraints=constraints,
            typical_applications=[
                "Wind disturbance rejection for drones",
                "Load variation compensation in robotics",
                "Road grade compensation in vehicles",
                "Wave compensation for marine vessels"
            ],
            benchmark_datasets=[
                "Disturbance Rejection Benchmark",
                "External Force Estimation Dataset",
                "Uncertain Environment Control Data"
            ],
            input_dimensions={"state": 6, "disturbance_estimate": 6, "model_uncertainty": 3},
            output_dimensions={"compensated_velocity": 3, "disturbance_estimate": 6}
        )

class JerkLimitedMotionTask(VelocityControlTask):
    """Jerk-limited velocity control for smooth transitions"""
    
    def __init__(self):
        from .architectures import GRUVelocityController, PINNVelocityController
        
        architectures = [
            GRUVelocityController(),
            PINNVelocityController()
        ]
        
        constraints = TaskConstraints(
            real_time=True,
            safety_critical=False,
            latency_requirements="milliseconds",
            reliability=0.99,
            hardware_constraints=["Jerk-limited trajectory generator", "Smooth actuator commands"],
            sample_efficiency_requirement="Medium"
        )
        
        super().__init__(
            task_name="Jerk-Limited Motion",
            description="Velocity control with explicit jerk limitations for smooth motion transitions and reduced mechanical stress",
            neural_architectures=architectures,
            constraints=constraints,
            typical_applications=[
                "Precision manufacturing equipment",
                "Passenger elevator control",
                "Camera stabilization systems",
                "Medical robotics for patient comfort"
            ],
            benchmark_datasets=[
                "Jerk-Limited Motion Dataset",
                "Smooth Transition Benchmark",
                "Mechanical Stress Reduction Data"
            ],
            input_dimensions={"current_state": 9, "target_state": 9, "jerk_limits": 3},
            output_dimensions={"velocity_command": 3, "acceleration_command": 3}
        )

# Factory function to create tasks
def get_velocity_task(task_name: str) -> Optional[VelocityControlTask]:
    """Factory function to create velocity control tasks"""
    tasks = {
        "VelocityTrackingTask": VelocityTrackingTask(),
        "SmoothProfileGenerationTask": SmoothProfileGenerationTask(),
        "CoordinatedVelocityControlTask": CoordinatedVelocityControlTask(),
        "DisturbanceRejectionTask": DisturbanceRejectionTask(),
        "JerkLimitedMotionTask": JerkLimitedMotionTask()
    }
    return tasks.get(task_name)

def list_all_tasks() -> List[str]:
    """List all available velocity control tasks"""
    return [
        "VelocityTrackingTask",
        "SmoothProfileGenerationTask",
        "CoordinatedVelocityControlTask",
        "DisturbanceRejectionTask",
        "JerkLimitedMotionTask"
    ]