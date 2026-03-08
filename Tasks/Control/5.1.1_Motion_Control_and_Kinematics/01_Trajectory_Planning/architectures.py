"""
Architectures for Trajectory Planning

Каталог архитектур нейронных сетей для планирования траекторий
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class ArchitectureType(Enum):
    """Типы архитектур нейронных сетей"""
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
    """Описание архитектуры нейронной сети"""
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
    safety_critical: bool = False


def get_trajectory_architectures() -> List[NeuralArchitecture]:
    """Получить все архитектуры для планирования траекторий"""
    
    lstm_arch = NeuralArchitecture(
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
    
    transformer_arch = NeuralArchitecture(
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
    
    pinn_arch = NeuralArchitecture(
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
    
    neural_ode_arch = NeuralArchitecture(
        architecture_type=ArchitectureType.NEURAL_ODE,
        use_case="Continuous-time trajectory representation and optimization",
        input_format="Initial state, time span, control inputs",
        output_format="Continuous trajectory as solution of learned ODE",
        advantages=[
            "Natural for continuous dynamics",
            "Adaptive step size",
            "Memory efficient"
        ],
        limitations=[
            "Numerical integration required",
            "Training can be slow",
            "Stability concerns"
        ],
        integration_with_classical="Combines with optimal control theory",
        example_papers=[
            "Neural ODEs for Trajectory Optimization",
            "Continuous-Depth Models for Control"
        ],
        computational_complexity="O(n)",
        memory_requirements="Low",
        sample_efficiency="High",
        real_time_capable=False,
        safety_critical=False
    )
    
    ppo_arch = NeuralArchitecture(
        architecture_type=ArchitectureType.PPO,
        use_case="End-to-end trajectory learning through reinforcement learning",
        input_format="State observations, reward signals",
        output_format="Action sequence or trajectory parameters",
        advantages=[
            "Stable policy updates",
            "Good sample efficiency for on-policy",
            "Handles complex objectives"
        ],
        limitations=[
            "Requires extensive training",
            "Safety during exploration",
            "Hyperparameter sensitive"
        ],
        integration_with_classical="Can use classical planners as initial policy",
        example_papers=[
            "Proximal Policy Optimization for Robotics",
            "Deep RL for Trajectory Learning"
        ],
        computational_complexity="O(1) inference",
        memory_requirements="Very High",
        sample_efficiency="Low",
        real_time_capable=True,
        safety_critical=False
    )
    
    sac_arch = NeuralArchitecture(
        architecture_type=ArchitectureType.SAC,
        use_case="Off-policy trajectory learning with entropy regularization",
        input_format="State-action-reward transitions",
        output_format="Stochastic policy for trajectory generation",
        advantages=[
            "Sample efficient off-policy learning",
            "Exploration through entropy",
            "Good for continuous control"
        ],
        limitations=[
            "Complex implementation",
            "Multiple networks to train",
            "Temperature tuning"
        ],
        integration_with_classical="Can incorporate model-based predictions",
        example_papers=[
            "Soft Actor-Critic for Robot Learning",
            "SAC for Continuous Control Tasks"
        ],
        computational_complexity="O(1) inference",
        memory_requirements="High",
        sample_efficiency="Medium",
        real_time_capable=True,
        safety_critical=False
    )
    
    return [
        lstm_arch,
        transformer_arch,
        pinn_arch,
        neural_ode_arch,
        ppo_arch,
        sac_arch
    ]


class ArchitectureCatalog:
    """Каталог архитектур с методами поиска и фильтрации"""
    
    def __init__(self):
        self.architectures = get_trajectory_architectures()
        self._index_by_type()
    
    def _index_by_type(self):
        """Создать индекс по типам архитектур"""
        self.by_type = {}
        for arch in self.architectures:
            key = arch.architecture_type.name
            if key not in self.by_type:
                self.by_type[key] = []
            self.by_type[key].append(arch)
    
    def get_by_type(self, arch_type: ArchitectureType) -> List[NeuralArchitecture]:
        """Получить архитектуры по типу"""
        return self.by_type.get(arch_type.name, [])
    
    def get_real_time_capable(self) -> List[NeuralArchitecture]:
        """Получить архитектуры, поддерживающие реальное время"""
        return [arch for arch in self.architectures if arch.real_time_capable]
    
    def get_safety_critical(self) -> List[NeuralArchitecture]:
        """Получить архитектуры для safety-critical задач"""
        return [arch for arch in self.architectures if arch.safety_critical]
    
    def get_by_sample_efficiency(self, level: str) -> List[NeuralArchitecture]:
        """Получить архитектуры по эффективности обучения"""
        return [arch for arch in self.architectures if arch.sample_efficiency == level]
    
    def search_by_use_case(self, keyword: str) -> List[NeuralArchitecture]:
        """Поиск архитектур по ключевым словам в описании использования"""
        keyword_lower = keyword.lower()
        return [
            arch for arch in self.architectures
            if keyword_lower in arch.use_case.lower()
        ]
    
    def get_all(self) -> List[NeuralArchitecture]:
        """Получить все архитектуры"""
        return self.architectures
    
    def summary(self) -> Dict:
        """Получить сводную статистику"""
        return {
            "total_architectures": len(self.architectures),
            "real_time_capable": len(self.get_real_time_capable()),
            "safety_critical": len(self.get_safety_critical()),
            "by_type": {k: len(v) for k, v in self.by_type.items()},
            "sample_efficiency_distribution": {
                "high": len(self.get_by_sample_efficiency("High")),
                "medium": len(self.get_by_sample_efficiency("Medium")),
                "low": len(self.get_by_sample_efficiency("Low"))
            }
        }
