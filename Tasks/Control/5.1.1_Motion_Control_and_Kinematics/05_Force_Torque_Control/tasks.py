"""
Tasks for Force/Torque Control
Section 5.1.1.05 - Controlling interaction forces and torques during contact tasks
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from .architectures import ForceTorqueNeuralArchitecture, ARCHITECTURES, get_architecture

@dataclass
class TaskConstraints:
    """Constraints and requirements for force/torque control tasks"""
    real_time: bool
    safety_critical: bool
    latency_requirements: str  # "microseconds", "milliseconds", "seconds"
    reliability: float  # 0.0 to 1.0
    hardware_constraints: List[str] = field(default_factory=list)
    sample_efficiency_requirement: str = "Medium"
    force_accuracy: Optional[float] = None  # in Newtons
    torque_accuracy: Optional[float] = None  # in Nm
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "real_time": self.real_time,
            "safety_critical": self.safety_critical,
            "latency_requirements": self.latency_requirements,
            "reliability": self.reliability,
            "hardware_constraints": self.hardware_constraints,
            "sample_efficiency_requirement": self.sample_efficiency_requirement,
            "force_accuracy": self.force_accuracy,
            "torque_accuracy": self.torque_accuracy
        }

@dataclass
class ForceTorqueTask:
    """Definition of a force/torque control task"""
    task_name: str
    description: str
    neural_architectures: List[ForceTorqueNeuralArchitecture]
    constraints: TaskConstraints
    typical_applications: List[str] = field(default_factory=list)
    benchmark_datasets: List[str] = field(default_factory=list)
    input_modalities: List[str] = field(default_factory=list)
    output_modalities: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_name": self.task_name,
            "description": self.description,
            "neural_architectures": [arch.to_dict() for arch in self.neural_architectures],
            "constraints": self.constraints.to_dict(),
            "typical_applications": self.typical_applications,
            "benchmark_datasets": self.benchmark_datasets,
            "input_modalities": self.input_modalities,
            "output_modalities": self.output_modalities
        }

# Predefined tasks for Force/Torque Control
TASKS = {
    "Assembly_Insertion": ForceTorqueTask(
        task_name="Assembly and Insertion Tasks",
        description="Precise force control for inserting pegs into holes, assembling parts with tight tolerances",
        neural_architectures=[
            get_architecture("Hybrid_Force_Position_Neural"),
            get_architecture("Neural_Impedance_Controller"),
            get_architecture("Force_Prediction_RNN")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="microseconds",
            reliability=0.9999,
            hardware_constraints=["6-axis force/torque sensor", "High-bandwidth actuators", "Precision encoders"],
            sample_efficiency_requirement="Low",
            force_accuracy=0.1,
            torque_accuracy=0.01
        ),
        typical_applications=[
            "Electronics assembly (PCB component insertion)",
            "Automotive part assembly",
            "Precision mechanical assembly",
            "Aerospace component fitting"
        ],
        benchmark_datasets=["Peg-in-Hole Dataset", "Industrial Assembly Benchmarks", "Contact-Rich Manipulation Dataset"],
        input_modalities=["Force/Torque", "Position", "Velocity", "Contact State"],
        output_modalities=["Force Commands", "Position Commands"]
    ),
    
    "Surface_Finishing": ForceTorqueTask(
        task_name="Surface Finishing and Polishing",
        description="Maintaining constant contact force while moving along complex surfaces for polishing, deburring, grinding",
        neural_architectures=[
            get_architecture("Neural_Impedance_Controller"),
            get_architecture("Adaptive_Force_MLP"),
            get_architecture("PINN_Force_Dynamics")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.999,
            hardware_constraints=["Force/torque sensor", "Compliant end-effector", "Surface profiling sensor"],
            sample_efficiency_requirement="Medium",
            force_accuracy=0.5,
            torque_accuracy=0.05
        ),
        typical_applications=[
            "Automotive body polishing",
            "Metal deburring",
            "Wood surface finishing",
            "Composite material sanding"
        ],
        benchmark_datasets=["Surface Finishing Dataset", "Polishing Force Profiles", "Industrial Grinding Benchmarks"],
        input_modalities=["Force/Torque", "Position", "Surface Normal", "Material Properties"],
        output_modalities=["Force Commands", "Trajectory Adjustments"]
    ),
    
    "Physical_HRI": ForceTorqueTask(
        task_name="Physical Human-Robot Interaction",
        description="Safe and compliant force control during physical interaction with humans",
        neural_architectures=[
            get_architecture("Neural_Impedance_Controller"),
            get_architecture("Transformer_Force_MultiModal"),
            get_architecture("Tactile_CNN_Force_Estimation")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="microseconds",
            reliability=0.99999,
            hardware_constraints=["Joint torque sensors", "Tactile skin", "Safety-rated monitoring"],
            sample_efficiency_requirement="High",
            force_accuracy=0.2,
            torque_accuracy=0.02
        ),
        typical_applications=[
            "Collaborative assembly tasks",
            "Physical guidance and teaching",
            "Rehabilitation robotics",
            "Assistive manipulation"
        ],
        benchmark_datasets=["HRI Force Interaction Dataset", "Collaborative Robot Benchmarks", "Safe Contact Dataset"],
        input_modalities=["Force/Torque", "Tactile", "Vision", "Human Intent"],
        output_modalities=["Impedance Parameters", "Force Commands"]
    ),
    
    "Delicate_Object_Manipulation": ForceTorqueTask(
        task_name="Delicate Object Manipulation",
        description="Controlling grasp and manipulation forces for fragile objects without damage",
        neural_architectures=[
            get_architecture("Tactile_CNN_Force_Estimation"),
            get_architecture("Force_Prediction_RNN"),
            get_architecture("RL_Force_Policy")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.999,
            hardware_constraints=["Tactile sensors", "Underactuated grippers", "Force-sensitive fingertips"],
            sample_efficiency_requirement="Low",
            force_accuracy=0.05,
            torque_accuracy=0.005
        ),
        typical_applications=[
            "Food handling and packaging",
            "Pharmaceutical product manipulation",
            "Electronic component handling",
            "Glass and ceramic object manipulation"
        ],
        benchmark_datasets=["Fragile Object Dataset", "Grasp Force Benchmarks", "Tactile Manipulation Dataset"],
        input_modalities=["Tactile", "Force/Torque", "Vision", "Object Properties"],
        output_modalities=["Grasp Force", "Manipulation Forces"]
    ),
    
    "Force_Controlled_Grasping": ForceTorqueTask(
        task_name="Force-Controlled Grasping",
        description="Adaptive grasp force control based on object properties and task requirements",
        neural_architectures=[
            get_architecture("Tactile_CNN_Force_Estimation"),
            get_architecture("Adaptive_Force_MLP"),
            get_architecture("Hybrid_Force_Position_Neural")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.999,
            hardware_constraints=["Tactile gripper", "Force sensors", "Adjustable grip mechanism"],
            sample_efficiency_requirement="Medium",
            force_accuracy=0.1,
            torque_accuracy=0.01
        ),
        typical_applications=[
            "Warehouse picking operations",
            "Multi-object grasping",
            "Deformable object handling",
            "Tool grasping and use"
        ],
        benchmark_datasets=["Grasp Force Dataset", "DexNet Force Extensions", "Tactile Grasping Benchmarks"],
        input_modalities=["Tactile", "Vision", "Object Weight Estimate"],
        output_modalities=["Grasp Force", "Finger Positions"]
    ),
    
    "Contact_Transition_Control": ForceTorqueTask(
        task_name="Contact Transition Control",
        description="Smooth transitions between free-space motion and contact phases",
        neural_architectures=[
            get_architecture("Hybrid_Force_Position_Neural"),
            get_architecture("Force_Prediction_RNN"),
            get_architecture("PINN_Force_Dynamics")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="microseconds",
            reliability=0.9999,
            hardware_constraints=["High-bandwidth force sensors", "Fast actuators", "Impact detection"],
            sample_efficiency_requirement="Medium",
            force_accuracy=0.2,
            torque_accuracy=0.02
        ),
        typical_applications=[
            "Robotic writing and drawing",
            "Touch-based exploration",
            "Probe-based inspection",
            "Sequential assembly operations"
        ],
        benchmark_datasets=["Contact Transition Dataset", "Impact Control Benchmarks", "Hybrid Motion Dataset"],
        input_modalities=["Force/Torque", "Position", "Velocity", "Contact Detection"],
        output_modalities=["Control Mode Selection", "Force/Position Commands"]
    ),
    
    "Multi_Contact_Manipulation": ForceTorqueTask(
        task_name="Multi-Contact Manipulation",
        description="Coordinating multiple simultaneous contact points with independent force control",
        neural_architectures=[
            get_architecture("Transformer_Force_MultiModal"),
            get_architecture("Hybrid_Force_Position_Neural"),
            get_architecture("RL_Force_Policy")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.999,
            hardware_constraints=["Multiple force sensors", "Multi-fingered hand", "Whole-body control"],
            sample_efficiency_requirement="Low",
            force_accuracy=0.3,
            torque_accuracy=0.03
        ),
        typical_applications=[
            "Bimanual manipulation",
            "Multi-fingered grasping",
            "In-hand manipulation",
            "Collaborative multi-robot tasks"
        ],
        benchmark_datasets=["Multi-Contact Dataset", "Dexterous Manipulation Benchmarks", "Bimanual Coordination Dataset"],
        input_modalities=["Multiple Force/Torque Sensors", "Tactile Arrays", "Proprioception"],
        output_modalities=["Multiple Force Commands", "Coordination Parameters"]
    ),
    
    "Force_Based_Path_Following": ForceTorqueTask(
        task_name="Force-Based Path Following",
        description="Following a path while maintaining specified contact forces with the environment",
        neural_architectures=[
            get_architecture("Neural_Impedance_Controller"),
            get_architecture("PINN_Force_Dynamics"),
            get_architecture("Adaptive_Force_MLP")
        ],
        constraints=TaskConstraints(
            real_time=True,
            safety_critical=True,
            latency_requirements="milliseconds",
            reliability=0.999,
            hardware_constraints=["Force/torque sensor", "Path planning system", "Compliance control"],
            sample_efficiency_requirement="Medium",
            force_accuracy=0.5,
            torque_accuracy=0.05
        ),
        typical_applications=[
            "Welding seam tracking",
            "Glue dispensing along paths",
            "Cleaning operations",
            "Inspection scanning"
        ],
        benchmark_datasets=["Path Following Force Dataset", "Welding Track Benchmarks", "Surface Scanning Dataset"],
        input_modalities=["Force/Torque", "Path Reference", "Surface Geometry"],
        output_modalities=["Force Commands", "Path Deviations"]
    )
}

def get_task(name: str) -> Optional[ForceTorqueTask]:
    """Get a specific task by name"""
    return TASKS.get(name)

def get_all_tasks() -> Dict[str, ForceTorqueTask]:
    """Get all available tasks"""
    return TASKS

def get_real_time_tasks() -> List[ForceTorqueTask]:
    """Get all tasks requiring real-time execution"""
    return [task for task in TASKS.values() if task.constraints.real_time]

def get_safety_critical_tasks() -> List[ForceTorqueTask]:
    """Get all safety-critical tasks"""
    return [task for task in TASKS.values() if task.constraints.safety_critical]

def get_tasks_by_application(application_keyword: str) -> List[ForceTorqueTask]:
    """Get tasks that include a specific application keyword"""
    return [
        task for task in TASKS.values()
        if any(application_keyword.lower() in app.lower() for app in task.typical_applications)
    ]