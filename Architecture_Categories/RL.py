"""
Module for Архитектуры для обучения с усилением (RL Architectures).
"""
from dataclasses import dataclass
from typing import Optional

# RL Architectures data
RL_ARCHITECTURES = [
    {
        "name": "Архитектуры для обучения с усилением (RL)",
        "description": "Архитектуры, разработанные специально для задач обучения с подкреплением."
    }
]

@dataclass
class RL:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Reinforcement Learning Neural Network Architectures
Networks for decision making and control
"""

RL_ARCHITECTURES = [
    {
        "name": "DQN",
        "description": "Deep Q-Network for value-based reinforcement learning"
    },
    {
        "name": "Double-DQN",
        "description": "DQN with double Q-learning to reduce overestimation"
    },
    {
        "name": "Dueling-DQN",
        "description": "DQN with separate value and advantage streams"
    },
    {
        "name": "Prioritized-DQN",
        "description": "DQN with prioritized experience replay"
    },
    {
        "name": "Rainbow-DQN",
        "description": "Combining improvements to DQN"
    },
    {
        "name": "C51",
        "description": "Categorical DQN for distributional RL"
    },
    {
        "name": "QR-DQN",
        "description": "Quantile Regression DQN for distributional RL"
    },
    {
        "name": "IQN",
        "description": "Implicit Quantile Networks for distributional RL"
    },
    {
        "name": "FQF",
        "description": "Fully Parameterized Quantile Function"
    },
    {
        "name": "A3C",
        "description": "Asynchronous Advantage Actor-Critic"
    },
    {
        "name": "A2C",
        "description": "Advantage Actor-Critic synchronous variant"
    },
    {
        "name": "GA3C",
        "description": "GPU-optimized Asynchronous Advantage Actor-Critic"
    },
    {
        "name": "TRPO",
        "description": "Trust Region Policy Optimization"
    },
    {
        "name": "PPO",
        "description": "Proximal Policy Optimization with clipped objective"
    },
    {
        "name": "PPO-Clip",
        "description": "PPO with clipped surrogate objective"
    },
    {
        "name": "PPO-Penalty",
        "description": "PPO with KL penalty constraint"
    },
    {
        "name": "ACKTR",
        "description": "Actor-Critic using Kronecker-factored Trust Region"
    },
    {
        "name": "DDPG",
        "description": "Deep Deterministic Policy Gradient for continuous actions"
    },
    {
        "name": "TD3",
        "description": "Twin Delayed DDPG with improved stability"
    },
    {
        "name": "DDPGf",
        "description": "DDPG with further improvements"
    },
    {
        "name": "SAC",
        "description": "Soft Actor-Critic with entropy maximization"
    },
    {
        "name": "SAC-Alpha",
        "description": "SAC with automatic temperature tuning"
    },
    {
        "name": "REDQ",
        "description": "Randomized Ensemble Double Q-learning"
    },
    {
        "name": "TD7",
        "description": "TD3 with seven improvements"
    },
    {
        "name": "REINFORCE",
        "description": "Monte Carlo policy gradient algorithm"
    },
    {
        "name": "Actor-Critic",
        "description": "Basic actor-critic architecture"
    },
    {
        "name": "GAE",
        "description": "Generalized Advantage Estimation"
    },
    {
        "name": "NPG",
        "description": "Natural Policy Gradient"
    },
    {
        "name": "FAC",
        "description": "Feudal Actor-Critic for hierarchical RL"
    },
    {
        "name": "HIRO",
        "description": "Hierarchical Reinforcement Learning with Off-policy correction"
    },
    {
        "name": "HAC",
        "description": "Hierarchical Actor-Critic"
    },
    {
        "name": "Option-Critic",
        "description": "Learning options and policies end-to-end"
    },
    {
        "name": "Feudal-Network",
        "description": "Feudal reinforcement learning architecture"
    },
    {
        "name": "MAXQ",
        "description": "Hierarchical decomposition of value function"
    },
    {
        "name": "DyNA",
        "description": "Dynamic Neural Architecture for RL"
    },
    {
        "name": "MB-MPO",
        "description": "Model-Based Meta Policy Optimization"
    },
    {
        "name": "MBPO",
        "description": "Model-Based Policy Optimization"
    },
    {
        "name": "STEVE",
        "description": "Sample-efficient model-based RL"
    },
    {
        "name": "PETS",
        "description": "Probabilistic Ensembles with Trajectory Sampling"
    },
    {
        "name": "Dyna",
        "description": "Integrated model-based and model-free RL"
    },
    {
        "name": "World-Model",
        "description": "Learning world models for planning"
    },
    {
        "name": "Dreamer",
        "description": "Learning long-horizon predictions for RL"
    },
    {
        "name": "Dreamer-v2",
        "description": "Improved Dreamer with discrete representations"
    },
    {
        "name": "Dreamer-v3",
        "description": "Third generation Dreamer with better scaling"
    },
    {
        "name": "PlaNet",
        "description": "Planning with latent dynamics models"
    },
    {
        "name": "MuZero",
        "description": "Mastering Atari, Go, chess without rules"
    },
    {
        "name": "AlphaZero",
        "description": "General reinforcement learning algorithm"
    },
    {
        "name": "AlphaGo",
        "description": "Deep neural networks for Go"
    },
    {
        "name": "AlphaGo-Zero",
        "description": "AlphaGo learning from self-play"
    },
    {
        "name": "AlphaStar",
        "description": "Mastering StarCraft II with deep RL"
    }
]