"""
Neural Architectures for Force/Torque Control
Section 5.1.1.05 - Controlling interaction forces and torques during contact tasks
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any

class ForceTorqueArchitectureType(Enum):
    """Types of neural architectures used in force/torque control"""
    HYBRID_FORCE_POSITION = "Hybrid Force-Position Neural Controller"
    IMPEDANCE_NEURAL = "Neural Impedance Controller"
    FORCE_RNN = "Recurrent Neural Network for Force Prediction"
    TACTILE_CNN = "Convolutional Network for Tactile Force Sensing"
    ADAPTIVE_FORCE_MLP = "Adaptive MLP for Force Control"
    TRANSFORMER_FORCE_MULTI_MODAL = "Transformer for Multi-modal Force Control"
    PINN_FORCE_DYNAMICS = "Physics-Informed Neural Network for Force Dynamics"
    RL_FORCE_POLICY = "Reinforcement Learning for Force Policy"

@dataclass
class ForceTorqueNeuralArchitecture:
    """Definition of a neural architecture for force/torque control tasks"""
    architecture_type: ForceTorqueArchitectureType
    use_case: str
    input_format: str
    output_format: str
    advantages: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    integration_with_classical: str = ""
    example_papers: List[str] = field(default_factory=list)
    computational_complexity: str = "O(n)"
    memory_requirements: str = "Medium"
    sample_efficiency: str = "Medium"
    real_time_capable: bool = True
    safety_critical: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            "architecture_type": self.architecture_type.value,
            "use_case": self.use_case,
            "input_format": self.input_format,
            "output_format": self.output_format,
            "advantages": self.advantages,
            "limitations": self.limitations,
            "integration_with_classical": self.integration_with_classical,
            "example_papers": self.example_papers,
            "computational_complexity": self.computational_complexity,
            "memory_requirements": self.memory_requirements,
            "sample_efficiency": self.sample_efficiency,
            "real_time_capable": self.real_time_capable,
            "safety_critical": self.safety_critical
        }

# Predefined architectures for Force/Torque Control
ARCHITECTURES = {
    "Hybrid_Force_Position_Neural": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.HYBRID_FORCE_POSITION,
        use_case="Hybrid force-position control with learned switching between modes",
        input_format="Force/torque measurements [Fx, Fy, Fz, Tx, Ty, Tz], position feedback [x, y, z], contact state binary, environment stiffness estimate",
        output_format="Separate force control outputs [F_cmd] and position control outputs [x_cmd] with learned coordination weights",
        advantages=[
            "Combines multiple control modalities seamlessly",
            "Learned switching between force and position modes",
            "Adaptive behavior based on contact conditions",
            "Handles transitions between free space and contact"
        ],
        limitations=[
            "Complex training requiring multi-objective optimization",
            "Multiple competing objectives (force accuracy vs position accuracy)",
            "Interaction between force and position components can cause instability"
        ],
        integration_with_classical="Classical hybrid control framework with neural network learning mode selection and parameter adaptation",
        example_papers=[
            "Hybrid Force-Position Learning for Assembly Tasks (2022)",
            "Neural Impedance Control with Adaptive Switching (2021)",
            "Learning Contact-Rich Manipulation Policies (2020)"
        ],
        computational_complexity="O(n)",
        memory_requirements="High",
        sample_efficiency="Low",
        real_time_capable=True,
        safety_critical=True
    ),
    
    "Neural_Impedance_Controller": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.IMPEDANCE_NEURAL,
        use_case="Learning optimal impedance parameters for compliant interaction",
        input_format="Desired impedance profile, current state [position, velocity, force], task phase indicator",
        output_format="Impedance parameters [stiffness K, damping B, inertia M] for each DOF",
        advantages=[
            "Learns task-specific impedance profiles",
            "Adapts compliance based on interaction context",
            "Enables safe human-robot interaction",
            "Can optimize energy efficiency while maintaining performance"
        ],
        limitations=[
            "Requires careful stability analysis",
            "May need extensive tuning of learning parameters",
            "Generalization to unseen contact scenarios can be limited"
        ],
        integration_with_classical="Direct parameterization of classical impedance controller gains using neural network",
        example_papers=[
            "Learning Impedance Control for Physical Interaction (2023)",
            "Neural Impedance Adaptation in Collaborative Robots (2022)",
            "Variable Impedance Control using Deep Learning (2021)"
        ],
        computational_complexity="O(1)",
        memory_requirements="Medium",
        sample_efficiency="Medium",
        real_time_capable=True,
        safety_critical=True
    ),
    
    "Force_Prediction_RNN": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.FORCE_RNN,
        use_case="Predicting future contact forces for proactive control",
        input_format="Historical force/torque sequence, robot motion commands, object properties",
        output_format="Predicted future force/torque trajectory over prediction horizon",
        advantages=[
            "Anticipates force changes before they occur",
            "Handles temporal dependencies in contact dynamics",
            "Enables model predictive force control",
            "Can predict contact transitions"
        ],
        limitations=[
            "Prediction accuracy degrades with longer horizons",
            "Requires large datasets of contact interactions",
            "Sensitive to modeling errors in object properties"
        ],
        integration_with_classical="Used as disturbance predictor in MPC framework for force control",
        example_papers=[
            "RNN-based Force Prediction for Robotic Manipulation (2022)",
            "Temporal Modeling of Contact Forces (2021)",
            "Predictive Force Control using Recurrent Networks (2020)"
        ],
        computational_complexity="O(n)",
        memory_requirements="Medium",
        sample_efficiency="Medium",
        real_time_capable=True,
        safety_critical=True
    ),
    
    "Tactile_CNN_Force_Estimation": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.TACTILE_CNN,
        use_case="Estimating contact forces from tactile sensor images",
        input_format="Tactile sensor image or pressure distribution map (2D array)",
        output_format="Estimated 3-axis force and torque at contact point",
        advantages=[
            "Direct force estimation from raw tactile data",
            "Spatial feature extraction from pressure patterns",
            "Works with various tactile sensor modalities",
            "Can detect contact location and area simultaneously"
        ],
        limitations=[
            "Requires calibration for each tactile sensor type",
            "Limited by tactile sensor resolution",
            "May struggle with multi-contact scenarios"
        ],
        integration_with_classical="Provides force feedback for impedance and hybrid controllers",
        example_papers=[
            "CNN-based Force Estimation from Tactile Images (2023)",
            "Deep Learning for Tactile Sensing in Robotics (2022)",
            "Vision-based Tactile Force Reconstruction (2021)"
        ],
        computational_complexity="O(n²)",
        memory_requirements="Medium-High",
        sample_efficiency="Medium",
        real_time_capable=True,
        safety_critical=False
    ),
    
    "Adaptive_Force_MLP": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.ADAPTIVE_FORCE_MLP,
        use_case="Direct adaptive force control with online parameter adjustment",
        input_format="Force error, force error integral, rate of change, environmental estimates",
        output_format="Force control command with adaptive gain scheduling",
        advantages=[
            "Fast adaptation to changing contact conditions",
            "Simple architecture suitable for embedded deployment",
            "Can handle non-linear force-response relationships"
        ],
        limitations=[
            "Limited temporal memory",
            "Requires careful initialization",
            "May oscillate if learning rate is too high"
        ],
        integration_with_classical="Augments traditional force PID with adaptive gain tuning",
        example_papers=[
            "Adaptive Neural Force Control for Industrial Applications (2021)",
            "MLP-based Gain Scheduling in Force Loops (2020)"
        ],
        computational_complexity="O(1)",
        memory_requirements="Low",
        sample_efficiency="Low",
        real_time_capable=True,
        safety_critical=True
    ),
    
    "Transformer_Force_MultiModal": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.TRANSFORMER_FORCE_MULTI_MODAL,
        use_case="Multi-modal force control integrating vision, touch, and proprioception",
        input_format="Multi-modal inputs: visual features, tactile readings, joint torques, contact states as sequence",
        output_format="Coordinated force/torque commands with attention-weighted modality fusion",
        advantages=[
            "Effectively fuses information from multiple sensor modalities",
            "Attention mechanism identifies most relevant sensory inputs",
            "Handles missing or noisy sensor data gracefully",
            "Scales well with number of sensor types"
        ],
        limitations=[
            "High computational overhead for attention computation",
            "Requires large multi-modal training datasets",
            "Complex interpretation of attention patterns"
        ],
        integration_with_classical="Provides high-level force references to classical low-level force controllers",
        example_papers=[
            "Multi-modal Transformer for Robotic Force Control (2023)",
            "Attention-based Sensor Fusion in Contact Tasks (2022)",
            "Vision-Tactile-Proprioceptive Integration for Manipulation (2023)"
        ],
        computational_complexity="O(n²)",
        memory_requirements="High",
        sample_efficiency="High",
        real_time_capable=False,
        safety_critical=True
    ),
    
    "PINN_Force_Dynamics": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.PINN_FORCE_DYNAMICS,
        use_case="Physics-informed learning of contact force dynamics",
        input_format="Time variable, boundary conditions, material properties, contact geometry",
        output_format="Continuous force profile satisfying contact mechanics equations",
        advantages=[
            "Incorporates physical laws of contact mechanics directly",
            "Ensures physically consistent force predictions",
            "Respects friction cone and other physical constraints",
            "Generalizes better to unseen scenarios"
        ],
        limitations=[
            "Training can be unstable with complex contact models",
            "Requires accurate knowledge of physical parameters",
            "Computationally intensive during training"
        ],
        integration_with_classical="Direct implementation of contact physics with neural correction terms",
        example_papers=[
            "Physics-Informed Neural Networks for Contact Force Modeling (2023)",
            "PINNs in Robotic Manipulation with Friction (2022)",
            "Learning Contact Dynamics with Physical Constraints (2021)"
        ],
        computational_complexity="O(n)",
        memory_requirements="Low-Medium",
        sample_efficiency="High",
        real_time_capable=False,
        safety_critical=True
    ),
    
    "RL_Force_Policy": ForceTorqueNeuralArchitecture(
        architecture_type=ForceTorqueArchitectureType.RL_FORCE_POLICY,
        use_case="Reinforcement learning for optimal force control policies",
        input_format="State observations [forces, positions, velocities], reward signals (task success, force accuracy, safety)",
        output_format="Optimal force/torque actions or policy parameters",
        advantages=[
            "Optimizes cumulative task performance",
            "Can learn complex force application strategies",
            "Self-improving through interaction",
            "Handles sparse reward scenarios"
        ],
        limitations=[
            "Very sample inefficient for force control tasks",
            "Safety concerns during exploration phase",
            "Risk of damaging hardware during learning",
            "Complex sim-to-real transfer"
        ],
        integration_with_classical="RL policy provides force references; classical controller ensures stability and safety",
        example_papers=[
            "Safe Reinforcement Learning for Force-Controlled Assembly (2023)",
            "Deep RL for Contact-Rich Manipulation (2022)",
            "Sim-to-Real Transfer of Force Control Policies (2021)"
        ],
        computational_complexity="O(1) inference, O(n) training",
        memory_requirements="Very High",
        sample_efficiency="Low",
        real_time_capable=False,
        safety_critical=False
    )
}

def get_architecture(name: str) -> Optional[ForceTorqueNeuralArchitecture]:
    """Get a specific architecture by name"""
    return ARCHITECTURES.get(name)

def get_all_architectures() -> Dict[str, ForceTorqueNeuralArchitecture]:
    """Get all available architectures"""
    return ARCHITECTURES

def get_architectures_by_type(arch_type: ForceTorqueArchitectureType) -> List[ForceTorqueNeuralArchitecture]:
    """Get all architectures of a specific type"""
    return [arch for arch in ARCHITECTURES.values() if arch.architecture_type == arch_type]

def get_real_time_architectures() -> List[ForceTorqueNeuralArchitecture]:
    """Get all architectures capable of real-time execution"""
    return [arch for arch in ARCHITECTURES.values() if arch.real_time_capable]

def get_safety_critical_architectures() -> List[ForceTorqueNeuralArchitecture]:
    """Get all safety-critical architectures"""
    return [arch for arch in ARCHITECTURES.values() if arch.safety_critical]