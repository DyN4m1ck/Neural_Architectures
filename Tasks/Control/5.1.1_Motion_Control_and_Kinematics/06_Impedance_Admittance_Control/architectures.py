"""
Impedance and Admittance Control - Neural Network Architectures
================================================================

This module defines neural network architectures for impedance and admittance control tasks.

Impedance Control: Regulates the relationship between force and position (F = Z(x))
Admittance Control: Regulates the relationship between position and force (x = Y(F))

These are essential for compliant interaction, safe HRI, and delicate manipulation.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional


class ArchitectureType(Enum):
    """Types of neural network architectures for impedance/admittance control"""
    
    NEURAL_ODE = "Neural Ordinary Differential Equation"
    RNN = "Recurrent Neural Network"
    LSTM = "Long Short-Term Memory"
    GRU = "Gated Recurrent Unit"
    PINN = "Physics-Informed Neural Network"
    TRANSFORMER = "Transformer Architecture"
    MLP = "Feedforward Neural Network (MLP)"
    CNN = "Convolutional Neural Network"
    GNN = "Graph Neural Network"
    HYBRID = "Hybrid Architecture"
    VAE = "Variational Autoencoder"
    SAC = "Soft Actor-Critic"
    TD3 = "Twin Delayed DDPG"


@dataclass
class NeuralArchitecture:
    """
    Represents a neural network architecture for impedance/admittance control.
    
    Attributes:
        architecture_type: Type of neural network architecture
        use_case: Specific application scenario
        input_format: Expected input data format
        output_format: Output data format
        advantages: List of advantages
        limitations: List of limitations
        integration_with_classical: How it integrates with classical methods
        example_papers: Relevant research papers
        computational_complexity: Big-O complexity
        memory_requirements: Memory usage level
        sample_efficiency: Data efficiency level
        real_time_capable: Whether suitable for real-time use
        safety_critical: Whether used in safety-critical applications
    """
    architecture_type: ArchitectureType
    use_case: str
    input_format: str
    output_format: str
    advantages: List[str]
    limitations: List[str]
    integration_with_classical: str
    example_papers: List[str]
    computational_complexity: str
    memory_requirements: str
    sample_efficiency: str
    real_time_capable: bool
    safety_critical: bool


def get_architectures_for_impedance_learning() -> List[NeuralArchitecture]:
    """Get architectures for impedance parameter learning"""
    return [
        NeuralArchitecture(
            architecture_type=ArchitectureType.NEURAL_ODE,
            use_case="Learning continuous-time impedance models from demonstration",
            input_format="Time series of position, velocity, force interactions",
            output_format="Continuous impedance parameters (M, B, K) as functions of state",
            advantages=[
                "Natural representation of continuous dynamics",
                "Physically consistent predictions",
                "Can interpolate between observed states",
                "Interpretable as mechanical system"
            ],
            limitations=[
                "Requires careful numerical integration",
                "Training can be unstable",
                "Computationally expensive during training",
                "Requires smooth data"
            ],
            integration_with_classical="Directly provides parameters for classical impedance controller M·ẍ + B·ẋ + K·x = F",
            example_papers=[
                "Neural ODEs for Robotic Impedance Control (ICRA 2021)",
                "Learning Continuous-Time Impedance Models (RSS 2020)",
                "Physics-Informed Neural ODEs for Manipulation (CoRL 2021)"
            ],
            computational_complexity="O(n)",
            memory_requirements="Medium",
            sample_efficiency="High",
            real_time_capable=False,
            safety_critical=True
        ),
        NeuralArchitecture(
            architecture_type=ArchitectureType.MLP,
            use_case="Fast impedance parameter prediction from context",
            input_format="Task context, object properties, interaction phase",
            output_format="Discrete impedance parameters (stiffness, damping, inertia)",
            advantages=[
                "Very fast inference",
                "Simple to implement",
                "Works well with limited data",
                "Easy to deploy on embedded systems"
            ],
            limitations=[
                "No temporal modeling",
                "Cannot capture dynamic changes",
                "Limited generalization",
                "Requires manual feature engineering"
            ],
            integration_with_classical="Provides setpoint parameters for adaptive impedance controller",
            example_papers=[
                "Learning Impedance Parameters for Robot Manipulation (IROS 2019)",
                "Context-Adaptive Impedance Control (ICRA 2020)"
            ],
            computational_complexity="O(1)",
            memory_requirements="Low",
            sample_efficiency="Medium",
            real_time_capable=True,
            safety_critical=True
        )
    ]


def get_architectures_for_admittance_control() -> List[NeuralArchitecture]:
    """Get architectures for admittance control"""
    return [
        NeuralArchitecture(
            architecture_type=ArchitectureType.RNN,
            use_case="Learning admittance behavior from human demonstration",
            input_format="Sequence of force/torque measurements and desired motion",
            output_format="Motion commands respecting learned admittance relationship",
            advantages=[
                "Captures temporal dependencies in interaction",
                "Can learn complex force-motion relationships",
                "Handles variable interaction dynamics",
                "Natural for sequential decision making"
            ],
            limitations=[
                "Requires sequential training data",
                "May suffer from gradient issues",
                "Slower than feedforward networks",
                "Needs careful initialization"
            ],
            integration_with_classical="Enhances classical admittance filter with learned dynamics",
            example_papers=[
                "RNN-based Admittance Control for HRI (HRI 2020)",
                "Learning Admittance from Demonstration (ICRA 2021)"
            ],
            computational_complexity="O(n)",
            memory_requirements="Medium",
            sample_efficiency="Medium",
            real_time_capable=True,
            safety_critical=True
        ),
        NeuralArchitecture(
            architecture_type=ArchitectureType.PINN,
            use_case="Physics-informed admittance control ensuring stability",
            input_format="Force inputs, physical constraints, stability criteria",
            output_format="Motion outputs satisfying passivity and stability conditions",
            advantages=[
                "Guarantees physical consistency",
                "Enforces stability by design",
                "Respects energy conservation",
                "Safe for physical interaction"
            ],
            limitations=[
                "Complex training procedure",
                "Requires accurate physics model",
                "Limited to known physics",
                "Sensitive to parameter uncertainty"
            ],
            integration_with_classical="Implements admittance filter with learned parameters constrained by physics",
            example_papers=[
                "Physics-Informed Learning for Safe Admittance Control (CDC 2021)",
                "Passivity-Guaranteed Neural Admittance (ICRA 2022)"
            ],
            computational_complexity="O(n)",
            memory_requirements="Low",
            sample_efficiency="High",
            real_time_capable=False,
            safety_critical=True
        )
    ]


def get_architectures_for_variable_stiffness() -> List[NeuralArchitecture]:
    """Get architectures for variable stiffness/impedance control"""
    return [
        NeuralArchitecture(
            architecture_type=ArchitectureType.TRANSFORMER,
            use_case="Context-aware variable stiffness modulation",
            input_format="Multi-modal: vision, force, task description, environment state",
            output_format="Time-varying stiffness profiles with attention to critical phases",
            advantages=[
                "Excellent multi-modal fusion",
                "Attention to relevant context",
                "Long-range dependency modeling",
                "Adapts stiffness based on task phase"
            ],
            limitations=[
                "High computational cost",
                "Requires large datasets",
                "Quadratic complexity with sequence length",
                "Complex training"
            ],
            integration_with_classical="Provides stiffness references for variable impedance controller",
            example_papers=[
                "Transformer-based Variable Stiffness Control (ICRA 2022)",
                "Attention Mechanisms for Compliant Manipulation (RSS 2021)"
            ],
            computational_complexity="O(n²)",
            memory_requirements="High",
            sample_efficiency="High",
            real_time_capable=False,
            safety_critical=True
        ),
        NeuralArchitecture(
            architecture_type=ArchitectureType.GRU,
            use_case="Smooth stiffness transition learning",
            input_format="Interaction history, contact state, task progress",
            output_format="Smooth stiffness trajectories avoiding abrupt changes",
            advantages=[
                "Handles temporal smoothing naturally",
                "More efficient than LSTM",
                "Good for shorter sequences",
                "Stable training"
            ],
            limitations=[
                "Limited long-term memory",
                "Still sequential computation",
                "May oversmooth rapid changes"
            ],
            integration_with_classical="Generates smooth stiffness references for classical VSA controllers",
            example_papers=[
                "GRU for Variable Stiffness Actuation (IROS 2020)",
                "Learning Smooth Impedance Transitions (ICRA 2021)"
            ],
            computational_complexity="O(n)",
            memory_requirements="Medium",
            sample_efficiency="Medium",
            real_time_capable=True,
            safety_critical=True
        )
    ]


def get_architectures_for_contact_rich_manipulation() -> List[NeuralArchitecture]:
    """Get architectures for contact-rich manipulation tasks"""
    return [
        NeuralArchitecture(
            architecture_type=ArchitectureType.HYBRID,
            use_case="Hybrid learning for contact-rich manipulation with mode switching",
            input_format="Force/torque, position, contact state estimates, visual feedback",
            output_format="Combined impedance/admittance commands with contact mode selection",
            advantages=[
                "Handles multiple contact modes",
                "Learned mode transitions",
                  "Combines reactive and planned behavior",
                "Robust to contact uncertainty"
            ],
            limitations=[
                "Complex architecture design",
                "Multiple objectives to optimize",
                "Mode switching can be unstable",
                "Requires extensive training"
            ],
            integration_with_classical="Classical hybrid position/force control with learned mode detection",
            example_papers=[
                "Hybrid Learning for Contact-Rich Manipulation (CoRL 2021)",
                "Neural Mode Detection for Assembly Tasks (ICRA 2022)"
            ],
            computational_complexity="O(n)",
            memory_requirements="High",
            sample_efficiency="Low",
            real_time_capable=True,
            safety_critical=True
        ),
        NeuralArchitecture(
            architecture_type=ArchitectureType.CNN,
            use_case="Visual-tactile fusion for contact state estimation",
            input_format="Camera images + tactile sensor arrays + force readings",
            output_format="Contact location, force distribution, slip detection",
            advantages=[
                "Excellent spatial feature extraction",
                "Multi-modal sensor fusion",
                "Detects subtle contact changes",
                "Translation invariant"
            ],
            limitations=[
                "Requires synchronized multi-modal data",
                "High computational cost for vision",
                "Limited temporal reasoning",
                "Sensitive to lighting conditions"
            ],
            integration_with_classical="Provides contact state for classical impedance modulation",
            example_papers=[
                "Visual-Tactile Fusion for Contact Estimation (RSS 2020)",
                "CNN-based Slip Detection (IROS 2021)"
            ],
            computational_complexity="O(n²)",
            memory_requirements="High",
            sample_efficiency="Medium",
            real_time_capable=False,
            safety_critical=True
        )
    ]


def get_architectures_for_human_robot_interaction() -> List[NeuralArchitecture]:
    """Get architectures for safe human-robot interaction"""
    return [
        NeuralArchitecture(
            architecture_type=ArchitectureType.SAC,
            use_case="Safe reinforcement learning for HRI with impedance adaptation",
            input_format="Human pose, robot state, interaction forces, safety metrics",
            output_format="Impedance parameters optimizing safety and performance",
            advantages=[
                "Optimizes cumulative safety",
                "Handles uncertainty in human behavior",
                "Continuous action space",
                "Sample-efficient among RL methods"
            ],
            limitations=[
                "Requires careful reward design",
                "Safety during exploration critical",
                "Slow convergence",
                "Sim-to-real gap"
            ],
            integration_with_classical="RL policy modulates classical impedance controller parameters",
            example_papers=[
                "Safe RL for Human-Robot Collaboration (ICRA 2021)",
                "SAC for Adaptive Impedance in HRI (CoRL 2020)"
            ],
            computational_complexity="O(1)",
            memory_requirements="Very High",
            sample_efficiency="Low",
            real_time_capable=False,
            safety_critical=True
        ),
        NeuralArchitecture(
            architecture_type=ArchitectureType.VAE,
            use_case="Probabilistic human intent prediction for proactive impedance adjustment",
            input_format="Human motion history, task context, environmental cues",
            output_format="Distribution over human intentions and predicted trajectories",
            advantages=[
                "Uncertainty quantification",
                "Proactive safety measures",
                "Handles ambiguous situations",
                "Generates diverse predictions"
            ],
            limitations=[
                "Complex training",
                "Requires probabilistic interpretation",
                "May be overly conservative",
                "Latent space interpretability"
            ],
            integration_with_classical="Intent predictions inform impedance parameter scheduling",
            example_papers=[
                "VAE for Human Intent Prediction in HRI (HRI 2021)",
                "Probabilistic Human Motion Forecasting (ICRA 2022)"
            ],
            computational_complexity="O(1)",
            memory_requirements="Medium",
            sample_efficiency="Medium",
            real_time_capable=False,
            safety_critical=True
        )
    ]


# Convenience function to get all architectures
def get_all_architectures() -> List[NeuralArchitecture]:
    """Get all neural architectures for impedance/admittance control"""
    all_archs = []
    all_archs.extend(get_architectures_for_impedance_learning())
    all_archs.extend(get_architectures_for_admittance_control())
    all_archs.extend(get_architectures_for_variable_stiffness())
    all_archs.extend(get_architectures_for_contact_rich_manipulation())
    all_archs.extend(get_architectures_for_human_robot_interaction())
    return all_archs