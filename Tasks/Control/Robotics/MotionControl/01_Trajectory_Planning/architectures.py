"""
Neural Network Architectures for Trajectory Planning

This module defines neural network architectures commonly used for trajectory planning
tasks in robotics and autonomous systems.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


class ArchitectureType(Enum):
    """Enumeration of neural network architecture types used in trajectory planning."""
    
    MLP = "Feedforward Neural Network (MLP)"
    CNN = "Convolutional Neural Network"
    RNN = "Recurrent Neural Network"
    LSTM = "Long Short-Term Memory"
    GRU = "Gated Recurrent Unit"
    TRANSFORMER = "Transformer Architecture"
    GNN = "Graph Neural Network"
    VAE = "Variational Autoencoder"
    PINN = "Physics-Informed Neural Network"
    NEURAL_ODE = "Neural Ordinary Differential Equation"
    DQN = "Deep Q-Network"
    PPO = "Proximal Policy Optimization"
    SAC = "Soft Actor-Critic"
    TD3 = "Twin Delayed DDPG"
    HYBRID = "Hybrid Architecture"


@dataclass
class NeuralArchitecture:
    """
    Represents a neural network architecture for trajectory planning tasks.
    
    Attributes:
        architecture_type: Type of neural network architecture
        use_case: Specific use case description
        input_format: Description of expected input format
        output_format: Description of output format
        advantages: List of advantages of this architecture
        limitations: List of limitations of this architecture
        integration_with_classical: How it integrates with classical methods
        example_papers: List of relevant research papers
        computational_complexity: Big-O notation for computational complexity
        memory_requirements: Memory requirements (Low, Medium, High)
        sample_efficiency: Sample efficiency (Low, Medium, High)
        real_time_capable: Whether the architecture can run in real-time
        safety_critical: Whether this is used in safety-critical applications
    """
    
    architecture_type: ArchitectureType
    use_case: str
    input_format: str
    output_format: str
    advantages: List[str]
    limitations: List[str]
    integration_with_classical: str
    example_papers: List[str]
    computational_complexity: str = "O(n)"
    memory_requirements: str = "Medium"
    sample_efficiency: str = "Medium"
    real_time_capable: bool = False
    safety_critical: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert architecture to dictionary representation."""
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


def get_lstm_architecture() -> NeuralArchitecture:
    """Create LSTM architecture for trajectory prediction."""
    return NeuralArchitecture(
        architecture_type=ArchitectureType.LSTM,
        use_case="Predicting future states for trajectory optimization",
        input_format="Sequence of states [x, y, z, vx, vy, vz, t] + environment context",
        output_format="Future trajectory points [x(t), y(t), z(t), vx(t), vy(t), vz(t)]",
        advantages=[
            "Handles temporal dependencies",
            "Works with variable-length sequences",
            "Can learn complex dynamics"
        ],
        limitations=[
            "Requires sequential training",
            "May suffer from vanishing gradients",
            "Computationally expensive for long sequences"
        ],
        integration_with_classical="Combined with MPC for improved predictions and constraint handling",
        example_papers=[
            "Learning to Plan Motion with Physics Prior",
            "LSTM-based Trajectory Prediction for Robot Manipulation"
        ],
        computational_complexity="O(n)",
        memory_requirements="Medium",
        sample_efficiency="Medium",
        real_time_capable=True,
        safety_critical=False
    )


def get_transformer_architecture() -> NeuralArchitecture:
    """Create Transformer architecture for long-horizon trajectory planning."""
    return NeuralArchitecture(
        architecture_type=ArchitectureType.TRANSFORMER,
        use_case="Long-horizon trajectory planning with attention mechanisms",
        input_format="Multi-modal inputs: states, obstacles, goals, constraints as sequence",
        output_format="Optimized trajectory with attention weights for critical points",
        advantages=[
            "Excellent for long-range dependencies",
            "Parallelizable",
            "Attention to important states"
        ],
        limitations=[
            "High computational overhead",
            "Requires large amounts of data",
            "Quadratic complexity with sequence length"
        ],
        integration_with_classical="Can provide initial guesses for optimization-based planners",
        example_papers=[
            "Transformers for Robot Trajectory Planning",
            "Attention-based Motion Planning"
        ],
        computational_complexity="O(n²)",
        memory_requirements="High",
        sample_efficiency="High",
        real_time_capable=False,
        safety_critical=False
    )


def get_pinn_architecture() -> NeuralArchitecture:
    """Create Physics-Informed Neural Network architecture for trajectory optimization."""
    return NeuralArchitecture(
        architecture_type=ArchitectureType.PINN,
        use_case="Physics-informed trajectory optimization respecting dynamical constraints",
        input_format="Time variable t, boundary conditions, physical parameters",
        output_format="Continuous trajectory satisfying differential equations of motion",
        advantages=[
            "Incorporates physical laws directly",
            "Continuous solutions",
            "Respects constraints by design"
        ],
        limitations=[
            "Training can be unstable",
            "Requires careful initialization",
            "Limited to known physics"
        ],
        integration_with_classical="Direct integration with classical mechanics equations",
        example_papers=[
            "Physics-Informed Neural Networks for Motion Planning",
            "PINNs for Optimal Control"
        ],
        computational_complexity="O(n)",
        memory_requirements="Low",
        sample_efficiency="High",
        real_time_capable=False,
        safety_critical=True
    )


def get_trajectory_planning_architectures() -> List[NeuralArchitecture]:
    """Get all neural architectures for trajectory planning."""
    return [
        get_lstm_architecture(),
        get_transformer_architecture(),
        get_pinn_architecture()
    ]
