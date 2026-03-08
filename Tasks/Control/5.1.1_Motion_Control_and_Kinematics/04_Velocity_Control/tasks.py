"""
Velocity Control - Task Catalog
Section 5.1.1.04
Catalog of velocity control tasks with specifications and requirements.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from .architectures import VelocityArchitecture, ArchitectureType


@dataclass
class VelocityTaskConstraints:
    """Constraints and requirements for velocity control tasks"""
    real_time: bool
    safety_critical: bool
    latency_requirements: str  # "microseconds", "milliseconds", "seconds"
    reliability: float  # 0.0 to 1.0
    hardware_constraints: List[str] = field(default_factory=list)
    sample_efficiency_requirement: str  # "Low", "Medium", "High"
    max_velocity: Optional[float] = None
    acceleration_limits: Optional[float] = None
    jerk_limits: Optional[float] = None


@dataclass
class VelocityControlTask:
    """Data class representing a velocity control task"""
    task_name: str
    description: str
    typical_applications: List[str] = field(default_factory=list)
    input_specifications: str = ""
    output_specifications: str = ""
    recommended_architectures: List[ArchitectureType] = field(default_factory=list)
    constraints: Optional[VelocityTaskConstraints] = None
    benchmark_datasets: List[str] = field(default_factory=list)
    performance_metrics: List[str] = field(default_factory=list)


class VelocityControlTasks:
    """
    Catalog of velocity control tasks for robotic systems.
    
    This class provides comprehensive information about various velocity control
    applications, including their requirements, constraints, and recommended
    neural network architectures.
    """
    
    def __init__(self):
        self.tasks = self._initialize_tasks()
    
    def _initialize_tasks(self) -> List[VelocityControlTask]:
        """Initialize the catalog of velocity control tasks"""
        return [
            self._create_smooth_velocity_profiling(),
            self._create_velocity_tracking(),
            self._create_disturbance_rejection(),
            self._create_multi_axis_coordination(),
            self._create_adaptive_velocity_control(),
            self._create_jerk_limited_motion(),
            self._create_high_speed_precision(),
            self._create_low_speed_stability()
        ]
    
    def _create_smooth_velocity_profiling(self) -> VelocityControlTask:
        """Smooth velocity profile generation task"""
        return VelocityControlTask(
            task_name="Smooth Velocity Profiling",
            description="Generation of smooth velocity trajectories with bounded derivatives (acceleration, jerk)",
            typical_applications=[
                "Robot manipulator motion planning",
                "CNC machine tool control",
                "Autonomous vehicle speed planning",
                "Camera gimbal stabilization"
            ],
            input_specifications="Desired end velocity, current state, kinematic constraints (max velocity, acceleration, jerk)",
            output_specifications="Time-parameterized velocity profile with smooth transitions",
            recommended_architectures=[
                ArchitectureType.GRU,
                ArchitectureType.LSTM,
                ArchitectureType.PINN
            ],
            constraints=VelocityTaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="milliseconds",
                reliability=0.99,
                hardware_constraints=["Motion controller", "Encoder feedback"],
                sample_efficiency_requirement="Medium",
                acceleration_limits=10.0,
                jerk_limits=50.0
            ),
            benchmark_datasets=["Robot Motion Profiles", "CNC Trajectory Dataset"],
            performance_metrics=["Smoothness (jerk integral)", "Tracking error", "Computation time"]
        )
    
    def _create_velocity_tracking(self) -> VelocityControlTask:
        """Velocity tracking and regulation task"""
        return VelocityControlTask(
            task_name="Velocity Tracking",
            description="Precise tracking of reference velocity commands under varying conditions",
            typical_applications=[
                "Motor speed control",
                "Conveyor belt systems",
                "Fan and pump control",
                "Vehicle cruise control"
            ],
            input_specifications="Reference velocity, measured velocity, control history",
            output_specifications="Control signal (voltage, current, PWM duty cycle)",
            recommended_architectures=[
                ArchitectureType.MLP,
                ArchitectureType.RNN,
                ArchitectureType.DDPG
            ],
            constraints=VelocityTaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="microseconds",
                reliability=0.999,
                hardware_constraints=["High-frequency PWM", "Current sensors"],
                sample_efficiency_requirement="Low"
            ),
            benchmark_datasets=["Motor Control Benchmarks", "Industrial Drive Data"],
            performance_metrics=["Steady-state error", "Rise time", "Overshoot", "Disturbance rejection"]
        )
    
    def _create_disturbance_rejection(self) -> VelocityControlTask:
        """Active disturbance rejection in velocity control"""
        return VelocityControlTask(
            task_name="Disturbance Rejection",
            description="Maintaining velocity performance despite external disturbances and load variations",
            typical_applications=[
                "Robotics under payload changes",
                "Wind disturbance compensation for drones",
                "Terrain adaptation for mobile robots",
                "Cutting force compensation in machining"
            ],
            input_specifications="Velocity error history, disturbance estimates, load measurements",
            output_specifications="Compensatory control signals",
            recommended_architectures=[
                ArchitectureType.RNN,
                ArchitectureType.LSTM,
                ArchitectureType.HYBRID
            ],
            constraints=VelocityTaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="milliseconds",
                reliability=0.99,
                hardware_constraints=["Force/torque sensors", "Load cells"],
                sample_efficiency_requirement="Medium"
            ),
            benchmark_datasets=["Disturbance Rejection Dataset", "Variable Load Control"],
            performance_metrics=["Disturbance attenuation", "Recovery time", "Robustness margin"]
        )
    
    def _create_multi_axis_coordination(self) -> VelocityControlTask:
        """Multi-axis coordinated velocity control"""
        return VelocityControlTask(
            task_name="Multi-Axis Coordination",
            description="Synchronized velocity control across multiple degrees of freedom",
            typical_applications=[
                "Parallel kinematics machines",
                "Multi-joint robot coordination",
                "Omni-directional mobile robots",
                "Hexapod platforms"
            ],
            input_specifications="Multi-axis states, coordination constraints, path parameters",
            output_specifications="Coordinated velocity commands for all axes",
            recommended_architectures=[
                ArchitectureType.TRANSFORMER,
                ArchitectureType.GNN,
                ArchitectureType.HYBRID
            ],
            constraints=VelocityTaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="milliseconds",
                reliability=0.995,
                hardware_constraints=["Multi-axis controller", "Synchronized encoders"],
                sample_efficiency_requirement="High"
            ),
            benchmark_datasets=["Multi-Robot Coordination", "Parallel Manipulator Data"],
            performance_metrics=["Coordination error", "Synchronization accuracy", "Path following error"]
        )
    
    def _create_adaptive_velocity_control(self) -> VelocityControlTask:
        """Adaptive velocity control for changing dynamics"""
        return VelocityControlTask(
            task_name="Adaptive Velocity Control",
            description="Learning and adapting velocity control policies to changing system dynamics",
            typical_applications=[
                "Wear compensation in industrial robots",
                "Battery degradation adaptation in EVs",
                "Temperature-dependent motor control",
                "Aging mechanism compensation"
            ],
            input_specifications="Performance metrics, system identification data, environmental conditions",
            output_specifications="Adapted control parameters or policies",
            recommended_architectures=[
                ArchitectureType.DDPG,
                ArchitectureType.SAC,
                ArchitectureType.RNN
            ],
            constraints=VelocityTaskConstraints(
                real_time=False,
                safety_critical=False,
                latency_requirements="seconds",
                reliability=0.95,
                hardware_constraints=["Online learning capability", "Safety monitoring"],
                sample_efficiency_requirement="Low"
            ),
            benchmark_datasets=["Adaptive Control Challenges", "System Variation Data"],
            performance_metrics=["Adaptation speed", "Post-adaptation performance", "Stability during adaptation"]
        )
    
    def _create_jerk_limited_motion(self) -> VelocityControlTask:
        """Jerk-limited velocity control for precision applications"""
        return VelocityControlTask(
            task_name="Jerk-Limited Motion",
            description="Velocity control with strict jerk constraints for high-precision applications",
            typical_applications=[
                "Semiconductor manufacturing equipment",
                "Precision optical systems",
                "Medical robotics",
                "Metrology systems"
            ],
            input_specifications="Target velocity, strict jerk limits, vibration constraints",
            output_specifications="Ultra-smooth velocity profiles with bounded higher derivatives",
            recommended_architectures=[
                ArchitectureType.PINN,
                ArchitectureType.NEURAL_ODE,
                ArchitectureType.GRU
            ],
            constraints=VelocityTaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="microseconds",
                reliability=0.9999,
                hardware_constraints=["High-resolution encoders", "Low-vibration actuators"],
                sample_efficiency_requirement="High",
                jerk_limits=5.0
            ),
            benchmark_datasets=["Precision Motion Data", "Vibration-Sensitive Applications"],
            performance_metrics=["Jerk RMS", "Vibration amplitude", "Settling time"]
        )
    
    def _create_high_speed_precision(self) -> VelocityControlTask:
        """High-speed velocity control with precision requirements"""
        return VelocityControlTask(
            task_name="High-Speed Precision Control",
            description="Velocity control at high speeds while maintaining precision",
            typical_applications=[
                "High-speed machining",
                "Pick-and-place robots",
                "Printing systems",
                "Packaging machinery"
            ],
            input_specifications="High velocity commands, precision requirements, dynamic constraints",
            output_specifications="High-bandwidth control signals",
            recommended_architectures=[
                ArchitectureType.MLP,
                ArchitectureType.DDPG,
                ArchitectureType.HYBRID
            ],
            constraints=VelocityTaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="microseconds",
                reliability=0.999,
                hardware_constraints=["High-bandwidth actuators", "Fast sensors"],
                sample_efficiency_requirement="Medium",
                max_velocity=100.0
            ),
            benchmark_datasets=["High-Speed Robotics", "Fast Motion Control"],
            performance_metrics=["Maximum achievable speed", "Precision at speed", "Cycle time"]
        )
    
    def _create_low_speed_stability(self) -> VelocityControlTask:
        """Low-speed stability and smoothness control"""
        return VelocityControlTask(
            task_name="Low-Speed Stability",
            description="Stable and smooth velocity control at very low speeds, overcoming friction effects",
            typical_applications=[
                "Telescope tracking",
                "Precision positioning stages",
                "Underwater ROVs",
                "Spacecraft attitude control"
            ],
            input_specifications="Very low velocity commands, friction models, stiction compensation",
            output_specifications="Smooth control signals overcoming stick-slip phenomena",
            recommended_architectures=[
                ArchitectureType.RNN,
                ArchitectureType.LSTM,
                ArchitectureType.PINN
            ],
            constraints=VelocityTaskConstraints(
                real_time=True,
                safety_critical=True,
                latency_requirements="milliseconds",
                reliability=0.999,
                hardware_constraints=["High-resolution encoders", "Direct drive motors"],
                sample_efficiency_requirement="Medium"
            ),
            benchmark_datasets=["Low-Speed Control", "Friction Compensation Data"],
            performance_metrics=["Minimum stable velocity", "Stick-slip elimination", "Smoothness"]
        )
    
    def get_task_by_name(self, task_name: str) -> Optional[VelocityControlTask]:
        """Get a specific task by name"""
        for task in self.tasks:
            if task.task_name.lower() == task_name.lower():
                return task
        return None
    
    def get_real_time_tasks(self) -> List[VelocityControlTask]:
        """Get all tasks requiring real-time execution"""
        return [task for task in self.tasks if task.constraints and task.constraints.real_time]
    
    def get_safety_critical_tasks(self) -> List[VelocityControlTask]:
        """Get all safety-critical tasks"""
        return [task for task in self.tasks if task.constraints and task.constraints.safety_critical]
    
    def get_all_tasks(self) -> List[VelocityControlTask]:
        """Get complete list of tasks"""
        return self.tasks
    
    def summary(self) -> Dict:
        """Get summary statistics"""
        return {
            "section": "5.1.1.04",
            "section_name": "Velocity Control",
            "total_tasks": len(self.tasks),
            "real_time_tasks": len(self.get_real_time_tasks()),
            "safety_critical_tasks": len(self.get_safety_critical_tasks()),
            "task_names": [task.task_name for task in self.tasks]
        }