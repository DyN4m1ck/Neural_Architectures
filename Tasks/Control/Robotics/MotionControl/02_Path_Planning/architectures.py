"""
Neural Network Architectures for Path Planning

This module defines neural network architectures commonly used for path planning
tasks in robotics and autonomous systems.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


class ArchitectureType(Enum):
    """Enumeration of neural network architecture types used in path planning."""
    
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
    Represents a neural network architecture for path planning tasks.
    
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


def get_cnn_architecture() -> NeuralArchitecture:
    """Create CNN architecture for visual path planning."""
    return NeuralArchitecture(
        architecture_type=ArchitectureType.CNN,
        use_case="Visual path planning from environmental maps",
        input_format="Occupancy grid map or image representation of environment",
        output_format="Discrete path as sequence of waypoints",
        advantages=[
            "Excellent spatial feature extraction",
            "Handles high-dimensional visual input",
            "Translation invariant"
        ],
        limitations=[
            "Limited long-range reasoning",
            "Fixed receptive field",
            "May miss global optima"
        ],
        integration_with_classical="Post-processing with A* or RRT for path refinement",
        example_papers=[
            "Learning Continuous Path Planning",
            "CNN-based Path Finding"
        ],
        computational_complexity="O(n²)",
        memory_requirements="Medium",
        sample_efficiency="Medium",
        real_time_capable=True,
        safety_critical=True
    )


def get_gnn_architecture() -> NeuralArchitecture:
    """Create GNN architecture for graph-based path planning."""
    return NeuralArchitecture(
        architecture_type=ArchitectureType.GNN,
        use_case="Graph-based path planning with topological reasoning",
        input_format="Graph structure with nodes as locations and edges as connections",
        output_format="Optimal path as sequence of graph nodes",
        advantages=[
            "Natural representation for spatial relationships",
            "Handles variable connectivity",
            "Global reasoning capability"
        ],
        limitations=[
            "Complex message passing",
            "Scalability issues",
            "Requires graph construction"
        ],
        integration_with_classical="Enhanced with classical graph algorithms like Dijkstra",
        example_papers=[
            "Graph Neural Networks for Path Planning",
            "Topological Path Learning"
        ],
        computational_complexity="O(E + V)",
        memory_requirements="High",
        sample_efficiency="High",
        real_time_capable=False,
        safety_critical=True
    )


def get_path_planning_architectures() -> List[NeuralArchitecture]:
    """Get all neural architectures for path planning."""
    return [
        get_cnn_architecture(),
        get_gnn_architecture()
    ]