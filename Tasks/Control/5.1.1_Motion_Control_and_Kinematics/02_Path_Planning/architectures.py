"""
Neural Architectures for Path Planning
Архитектуры нейронных сетей для планирования путей
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class ArchitectureType(Enum):
    """Types of neural architectures used in path planning"""
    CNN = "Convolutional Neural Network"
    GNN = "Graph Neural Network"
    TRANSFORMER = "Transformer Architecture"
    MLP = "Feedforward Neural Network (MLP)"
    RNN = "Recurrent Neural Network"
    LSTM = "Long Short-Term Memory"
    DQN = "Deep Q-Network"
    PPO = "Proximal Policy Optimization"


@dataclass
class NeuralArchitecture:
    """Base class for neural architecture specifications"""
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


@dataclass
class CNNPathPlanning(NeuralArchitecture):
    """CNN-based path planning from environmental maps"""
    
    def __post_init__(self):
        self.architecture_type = ArchitectureType.CNN
        self.use_case = "Visual path planning from occupancy grid maps"
        self.input_format = "Occupancy grid map or image representation of environment"
        self.output_format = "Discrete path as sequence of waypoints"
        self.advantages = [
            "Excellent spatial feature extraction",
            "Handles high-dimensional visual input",
            "Translation invariant"
        ]
        self.limitations = [
            "Limited long-range reasoning",
            "Fixed receptive field",
            "May miss global optima"
        ]
        self.integration_with_classical = "Post-processing with A* or RRT for path refinement"
        self.example_papers = [
            "Learning Continuous Path Planning",
            "CNN-based Path Finding"
        ]
        self.computational_complexity = "O(n²)"
        self.memory_requirements = "Medium"
        self.sample_efficiency = "Medium"
        self.real_time_capable = True
        self.safety_critical = True


@dataclass
class GNNPathPlanning(NeuralArchitecture):
    """Graph Neural Network for topological path planning"""
    
    def __post_init__(self):
        self.architecture_type = ArchitectureType.GNN
        self.use_case = "Graph-based path planning with topological reasoning"
        self.input_format = "Graph structure with nodes as locations and edges as connections"
        self.output_format = "Optimal path as sequence of graph nodes"
        self.advantages = [
            "Natural representation for spatial relationships",
            "Handles variable connectivity",
            "Global reasoning capability"
        ]
        self.limitations = [
            "Complex message passing",
            "Scalability issues",
            "Requires graph construction"
        ]
        self.integration_with_classical = "Enhanced with classical graph algorithms like Dijkstra"
        self.example_papers = [
            "Graph Neural Networks for Path Planning",
            "Topological Path Learning"
        ]
        self.computational_complexity = "O(E + V)"
        self.memory_requirements = "High"
        self.sample_efficiency = "High"
        self.real_time_capable = False
        self.safety_critical = True


@dataclass
class TransformerPathPlanning(NeuralArchitecture):
    """Transformer-based path planning with attention mechanisms"""
    
    def __post_init__(self):
        self.architecture_type = ArchitectureType.TRANSFORMER
        self.use_case = "Long-horizon path planning with global attention"
        self.input_format = "Multi-modal inputs: maps, obstacles, goals as sequences"
        self.output_format = "Optimized path with attention weights for critical points"
        self.advantages = [
            "Excellent for long-range dependencies",
            "Parallelizable",
            "Attention to important waypoints"
        ]
        self.limitations = [
            "High computational overhead",
            "Requires large amounts of data",
            "Quadratic complexity with sequence length"
        ]
        self.integration_with_classical = "Can provide initial guesses for optimization-based planners"
        self.example_papers = [
            "Transformers for Robot Path Planning",
            "Attention-based Motion Planning"
        ]
        self.computational_complexity = "O(n²)"
        self.memory_requirements = "High"
        self.sample_efficiency = "High"
        self.real_time_capable = False
        self.safety_critical = True


@dataclass
class MLPPathPlanning(NeuralArchitecture):
    """Simple MLP for direct path planning mapping"""
    
    def __post_init__(self):
        self.architecture_type = ArchitectureType.MLP
        self.use_case = "Direct path planning in simple environments"
        self.input_format = "Start position, goal position, obstacle features"
        self.output_format = "Waypoint sequence or control commands"
        self.advantages = [
            "Simple and fast",
            "Easy to implement",
            "Low computational cost"
        ]
        self.limitations = [
            "Limited generalization",
            "Cannot handle complex environments",
            "No temporal modeling"
        ]
        self.integration_with_classical = "Used as heuristic for classical planners"
        self.example_papers = [
            "Neural Network Path Planning",
            "MLP for Mobile Robot Navigation"
        ]
        self.computational_complexity = "O(1)"
        self.memory_requirements = "Low"
        self.sample_efficiency = "Low"
        self.real_time_capable = True
        self.safety_critical = False
