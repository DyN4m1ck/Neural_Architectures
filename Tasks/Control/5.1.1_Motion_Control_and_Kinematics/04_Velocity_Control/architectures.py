"""
Velocity Control - Neural Network Architectures
Section 5.1.1.04
Catalog of neural architectures for velocity control tasks.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class ArchitectureType(Enum):
    """Types of neural network architectures for velocity control"""
    MLP = "Feedforward Neural Network (MLP)"
    RNN = "Recurrent Neural Network"
    LSTM = "Long Short-Term Memory"
    GRU = "Gated Recurrent Unit"
    CNN = "Convolutional Neural Network"
    TRANSFORMER = "Transformer Architecture"
    PINN = "Physics-Informed Neural Network"
    NEURAL_ODE = "Neural Ordinary Differential Equation"
    DDPG = "Deep Deterministic Policy Gradient"
    SAC = "Soft Actor-Critic"
    PPO = "Proximal Policy Optimization"
    HYBRID = "Hybrid Architecture"


@dataclass
class VelocityArchitecture:
    """Data class representing a neural architecture for velocity control"""
    architecture_type: ArchitectureType
    use_case: str
    input_format: str
    output_format: str
    advantages: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    integration_with_classical: str = ""
    example_papers: List[str] = field(default_factory=list)
    computational_complexity: str = ""
    memory_requirements: str = ""
    sample_efficiency: str = ""
    real_time_capable: bool = False
    safety_critical: bool = False


class VelocityControlArchitectures:
    """
    Catalog of neural network architectures for velocity control applications.
    
    This class provides comprehensive information about various neural architectures
    used for controlling speed and direction in robotic systems, including:
    - Smooth velocity profile generation
    - Velocity tracking with disturbance rejection
    - Adaptive velocity control
    - Multi-axis coordinated velocity control
    """
    
    def __init__(self):
        self.architectures = self._initialize_architectures()
    
    def _initialize_architectures(self) -> List[VelocityArchitecture]:
        """Initialize the catalog of velocity control architectures"""
        return [
            self._create_gru_velocity_control(),
            self._create_lstm_velocity_profiling(),
            self._create_mlp_velocity_tracking(),
            self._create_rnn_disturbance_rejection(),
            self._create_pinn_velocity_dynamics(),
            self._create_ddpg_adaptive_velocity(),
            self._create_transformer_multi_axis(),
            self._create_hybrid_velocity_force()
        ]
    
    def _create_gru_velocity_control(self) -> VelocityArchitecture:
        """GRU-based smooth velocity profile generation"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.GRU,
            use_case="Smooth velocity profile generation and tracking with jerk constraints",
            input_format="Current velocity, desired velocity, acceleration limits, jerk constraints, time horizon",
            output_format="Smooth velocity commands with bounded derivatives",
            advantages=[
                "Handles variable time constants effectively",
                "Better than LSTM for shorter sequences with less computational overhead",
                "Effective for smooth control with natural temporal dynamics",
                "Lower memory footprint than LSTM"
            ],
            limitations=[
                "Still has some gradient issues for very long sequences",
                "Can be slower than simpler methods for trivial cases",
                "Requires careful tuning of gate parameters"
            ],
            integration_with_classical="Combined with traditional PI/PID velocity controllers for stability guarantees",
            example_papers=[
                "GRU for Smooth Velocity Control in Robotic Systems",
                "Learning Velocity Profiles with Gated Recurrent Units",
                "Temporal Modeling for Motion Control"
            ],
            computational_complexity="O(n)",
            memory_requirements="Medium",
            sample_efficiency="Medium",
            real_time_capable=True,
            safety_critical=True
        )
    
    def _create_lstm_velocity_profiling(self) -> VelocityArchitecture:
        """LSTM-based velocity profile learning"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.LSTM,
            use_case="Learning complex velocity profiles from demonstrations",
            input_format="Sequence of velocity commands, environmental context, task parameters",
            output_format="Predicted velocity trajectory with learned characteristics",
            advantages=[
                "Excellent for capturing long-term dependencies in velocity patterns",
                "Can learn from human demonstrations",
                "Handles variable-length motion primitives"
            ],
            limitations=[
                "Higher computational cost than GRU",
                "May suffer from vanishing gradients for very long sequences",
                "Requires substantial training data"
            ],
            integration_with_classical="Used to generate reference trajectories for classical velocity controllers",
            example_papers=[
                "LSTM-based Learning of Velocity Profiles from Demonstration",
                "Imitation Learning for Robotic Velocity Control"
            ],
            computational_complexity="O(n)",
            memory_requirements="Medium-High",
            sample_efficiency="Medium",
            real_time_capable=True,
            safety_critical=False
        )
    
    def _create_mlp_velocity_tracking(self) -> VelocityArchitecture:
        """MLP-based direct velocity tracking"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.MLP,
            use_case="Direct velocity error to control signal mapping",
            input_format="Velocity error, integral of error, derivative of error, current state",
            output_format="Control signals (voltage, torque, PWM)",
            advantages=[
                "Simple and fast inference",
                "Easy to implement and deploy",
                "Good for well-characterized systems with stable dynamics"
            ],
            limitations=[
                "No explicit temporal modeling",
                "Cannot handle complex dynamic changes",
                "Limited generalization to unseen conditions"
            ],
            integration_with_classical="Augmentation or replacement of traditional PID velocity loops",
            example_papers=[
                "Neural Network Enhancement of Velocity Control Loops",
                "MLP-based Motor Speed Control"
            ],
            computational_complexity="O(1)",
            memory_requirements="Low",
            sample_efficiency="Low",
            real_time_capable=True,
            safety_critical=True
        )
    
    def _create_rnn_disturbance_rejection(self) -> VelocityArchitecture:
        """RNN-based disturbance estimation and rejection"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.RNN,
            use_case="Active disturbance rejection in velocity control",
            input_format="Historical velocity errors, control actions, external sensor data",
            output_format="Disturbance estimates and compensatory control signals",
            advantages=[
                "Can learn complex disturbance patterns",
                "Adapts to changing environmental conditions",
                "Handles unmodeled dynamics"
            ],
            limitations=[
                "Training stability can be challenging",
                "May require online adaptation",
                "Computational overhead for real-time operation"
            ],
            integration_with_classical="Enhanced disturbance observer combined with classical velocity control",
            example_papers=[
                "RNN-based Active Disturbance Rejection Control",
                "Learning Disturbance Models for Velocity Control"
            ],
            computational_complexity="O(n)",
            memory_requirements="Medium",
            sample_efficiency="Medium",
            real_time_capable=True,
            safety_critical=True
        )
    
    def _create_pinn_velocity_dynamics(self) -> VelocityArchitecture:
        """Physics-Informed Neural Network for velocity dynamics"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.PINN,
            use_case="Velocity control respecting physical dynamics and constraints",
            input_format="Time, boundary conditions, physical parameters (mass, friction, etc.)",
            output_format="Velocity trajectory satisfying differential equations",
            advantages=[
                "Incorporates physical laws directly into learning",
                "Ensures physically consistent solutions",
                "Better generalization with less data",
                "Respects energy and momentum constraints"
            ],
            limitations=[
                "Training can be unstable and requires careful initialization",
                "Requires accurate knowledge of system physics",
                "Computationally intensive training"
            ],
            integration_with_classical="Direct integration with Lagrangian/Hamiltonian mechanics",
            example_papers=[
                "Physics-Informed Neural Networks for Velocity Control",
                "PINNs for Mechanical System Control"
            ],
            computational_complexity="O(n)",
            memory_requirements="Low-Medium",
            sample_efficiency="High",
            real_time_capable=False,
            safety_critical=True
        )
    
    def _create_ddpg_adaptive_velocity(self) -> VelocityArchitecture:
        """Deep Reinforcement Learning for adaptive velocity control"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.DDPG,
            use_case="Reinforcement learning-based adaptive velocity policy",
            input_format="State observations (velocity, position, rewards), goal velocity",
            output_format="Optimal control actions for velocity tracking",
            advantages=[
                "Learns optimal control policies through interaction",
                "Handles continuous action spaces naturally",
                "Can optimize for complex reward functions"
            ],
            limitations=[
                "Sample inefficient - requires extensive training",
                "Safety concerns during exploration phase",
                "Hyperparameter sensitivity"
            ],
            integration_with_classical="Classical controller as initial policy or safety layer",
            example_papers=[
                "Deep Deterministic Policy Gradient for Motor Control",
                "RL-based Adaptive Velocity Control"
            ],
            computational_complexity="O(1) inference, O(n) training",
            memory_requirements="Very High",
            sample_efficiency="Low",
            real_time_capable=True,
            safety_critical=False
        )
    
    def _create_transformer_multi_axis(self) -> VelocityArchitecture:
        """Transformer-based multi-axis coordinated velocity control"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.TRANSFORMER,
            use_case="Coordinated velocity control across multiple axes with attention",
            input_format="Multi-axis states, coordination constraints, task objectives as sequence",
            output_format="Coordinated velocity commands for all axes",
            advantages=[
                "Excellent for modeling inter-axis dependencies",
                "Attention mechanism focuses on critical coordination points",
                "Parallelizable computation",
                "Handles variable number of axes"
            ],
            limitations=[
                "High computational overhead",
                "Quadratic complexity with sequence length",
                "Requires large datasets for training"
            ],
            integration_with_classical="Coordination layer on top of individual axis controllers",
            example_papers=[
                "Transformer-based Multi-Axis Motion Coordination",
                "Attention Mechanisms for Coordinated Control"
            ],
            computational_complexity="O(n²)",
            memory_requirements="High",
            sample_efficiency="High",
            real_time_capable=False,
            safety_critical=True
        )
    
    def _create_hybrid_velocity_force(self) -> VelocityArchitecture:
        """Hybrid architecture for velocity-force control transitions"""
        return VelocityArchitecture(
            architecture_type=ArchitectureType.HYBRID,
            use_case="Seamless transitions between velocity and force control modes",
            input_format="Velocity commands, force measurements, contact state, mode indicators",
            output_format="Blended velocity/force control signals with smooth transitions",
            advantages=[
                "Handles mode transitions smoothly",
                "Combines benefits of both control paradigms",
                "Adaptive to contact conditions"
            ],
            limitations=[
                "Complex architecture design",
                "Challenging training with multiple objectives",
                "Requires careful mode detection"
            ],
            integration_with_classical="Classical hybrid control with learned transition policies",
            example_papers=[
                "Hybrid Velocity-Force Control with Neural Networks",
                "Learning Mode Transitions in Manipulation"
            ],
            computational_complexity="O(n)",
            memory_requirements="High",
            sample_efficiency="Low",
            real_time_capable=True,
            safety_critical=True
        )
    
    def get_architecture_by_type(self, arch_type: ArchitectureType) -> Optional[VelocityArchitecture]:
        """Get architecture by type"""
        for arch in self.architectures:
            if arch.architecture_type == arch_type:
                return arch
        return None
    
    def get_real_time_architectures(self) -> List[VelocityArchitecture]:
        """Get all architectures capable of real-time operation"""
        return [arch for arch in self.architectures if arch.real_time_capable]
    
    def get_safety_critical_architectures(self) -> List[VelocityArchitecture]:
        """Get all architectures suitable for safety-critical applications"""
        return [arch for arch in self.architectures if arch.safety_critical]
    
    def get_all_architectures(self) -> List[VelocityArchitecture]:
        """Get complete list of architectures"""
        return self.architectures
    
    def summary(self) -> Dict:
        """Get summary statistics"""
        return {
            "section": "5.1.1.04",
            "section_name": "Velocity Control",
            "total_architectures": len(self.architectures),
            "real_time_capable": len(self.get_real_time_architectures()),
            "safety_critical": len(self.get_safety_critical_architectures()),
            "architecture_types": [arch.architecture_type.value for arch in self.architectures]
        }