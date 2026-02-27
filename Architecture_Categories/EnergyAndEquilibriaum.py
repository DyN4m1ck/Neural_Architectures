"""
Module for Energy & Equilibrium Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Energy & Equilibrium Architectures",
        "description": "analytical tools used to predict the state of complex systems (economic or physico-chemical) based on the balance of supply and demand, minimizing costs and optimizing the use of resources. They find the optimal balance by ensuring consistency between production capacity, commodity/energy flows, and consumption."
    }
]

@dataclass
class EnergyAndEquilibriaum:
    """
    Represents a Convolutional Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Energy-Based and Equilibrium Models
Networks that use energy functions or implicit depth
"""

ENERGY_EQUILIBRIUM_ARCHITECTURES = [
    {
        "name": "Hopfield-Network",
        "description": "Classic recurrent network with energy function for associative memory"
    },
    {
        "name": "Modern-Hopfield-Network",
        "description": "Dense associative memory with continuous states and higher capacity"
    },
    {
        "name": "Boltzmann-Machine",
        "description": "Stochastic recurrent network using energy-based learning"
    },
    {
        "name": "Restricted-Boltzmann-Machine",
        "description": "Two-layer undirected graphical model for unsupervised learning"
    },
    {
        "name": "Deep-Belief-Network",
        "description": "Stack of RBMs trained greedily for deep representation learning"
    },
    {
        "name": "Deep-Boltzmann-Machine",
        "description": "Deep undirected network with hidden layers for complex modeling"
    },
    {
        "name": "Contrastive-Divergence-RBM",
        "description": "RBM trained with contrastive divergence for efficient learning"
    },
    {
        "name": "Persistent-Contrastive-Divergence",
        "description": "Improved RBM training with persistent Markov chains"
    },
    {
        "name": "Energy-Based-Model",
        "description": "General framework learning energy functions for data modeling"
    },
    {
        "name": "Joint-Energy-Based-Model",
        "description": "EBM modeling joint distribution of inputs and labels"
    },
    {
        "name": "Implicit-Energy-Model",
        "description": "Energy-based model with implicit density estimation"
    },
    {
        "name": "Deep-Equilibrium-Model",
        "description": "Network finding fixed point instead of finite layers"
    },
    {
        "name": "Monotone-Deep-Equilibrium",
        "description": "DEQ with monotone operator for guaranteed convergence"
    },
    {
        "name": "Multiscale-Deep-Equilibrium",
        "description": "MDEQ with multiple equilibrium points for different scales"
    },
    {
        "name": "Optimization-Equilibrium",
        "description": "Network interpreting layers as optimization steps"
    },
    {
        "name": "Neural-ODE",
        "description": "Continuous-depth model using ordinary differential equations"
    },
    {
        "name": "Augmented-Neural-ODE",
        "description": "Neural ODE with augmented state space for expressiveness"
    },
    {
        "name": "FFJORD",
        "description": "Free-form continuous normalizing flow for density estimation"
    },
    {
        "name": "ANODE-v2",
        "description": "Improved augmented Neural ODE with better stability"
    },
    {
        "name": "Latent-ODE",
        "description": "ODE modeling latent dynamics for irregular time series"
    },
    {
        "name": "ODE-RNN",
        "description": "RNN with ODE-based hidden state evolution"
    },
    {
        "name": "GRU-ODE",
        "description": "Gated recurrent unit with continuous-time dynamics"
    },
    {
        "name": "Continuous-RNN",
        "description": "RNN operating in continuous time domain"
    },
    {
        "name": "Neural-CDE",
        "description": "Neural controlled differential equation for time series"
    },
    {
        "name": "Neural-SDE",
        "description": "Neural stochastic differential equation for uncertainty"
    },
    {
        "name": "Hamiltonian-Neural-Network",
        "description": "Network learning Hamiltonian dynamics for physical systems"
    },
    {
        "name": "Lagrangian-Neural-Network",
        "description": "Network learning Lagrangian mechanics from data"
    },
    {
        "name": "Symplectic-ODE-Net",
        "description": "Energy-conserving network for physical system modeling"
    },
    {
        "name": "Deep-Hamiltonian",
        "description": "Deep network learning Hamiltonian from observations"
    },
    {
        "name": "Implicit-Layer-Network",
        "description": "Network with layers defined implicitly by fixed point"
    },
    {
        "name": "Deep-Implicit-Layer",
        "description": "Multi-layer implicit network for complex functions"
    },
    {
        "name": "Equilibrium-RNN",
        "description": "RNN reaching equilibrium state for sequence processing"
    },
    {
        "name": "Convergent-RNN",
        "description": "RNN with guaranteed convergence to fixed point"
    },
    {
        "name": "Stable-Equilibrium-Net",
        "description": "Network with provably stable equilibrium points"
    },
    {
        "name": "Monotone-Operator-Network",
        "description": "Network using monotone operators for implicit depth"
    },
    {
        "name": "Proximal-Recurrence-Network",
        "description": "Network with proximal operator for stable recurrence"
    },
    {
        "name": "Deep-Equilibrium-Transformer",
        "description": "Transformer with implicit depth through equilibrium"
    },
    {
        "name": "Energy-Transformer",
        "description": "Transformer using energy-based attention mechanisms"
    },
    {
        "name": "Implicit-Transformer",
        "description": "Transformer with implicit layer computation"
    },
    {
        "name": "Score-Based-Model",
        "description": "Model learning score function for density estimation"
    },
    {
        "name": "Denoising-Score-Matching",
        "description": "Score-based model trained with denoising objective"
    },
    {
        "name": "Noise-Conditional-Score-Network",
        "description": "Score network conditioned on noise level"
    },
    {
        "name": "Score-SDE",
        "description": "Score-based model with stochastic differential equations"
    },
    {
        "name": "Consistency-Model",
        "description": "Model learning consistent mappings for fast generation"
    },
    {
        "name": "Equilibrium-Consistency-Model",
        "description": "Consistency model with equilibrium constraints"
    },
    {
        "name": "Energy-Based-GAN",
        "description": "GAN using energy-based discriminator"
    },
    {
        "name": "Wasserstein-Energy-Model",
        "description": "Energy model with Wasserstein distance training"
    },
    {
        "name": "Contrastive-Energy-Model",
        "description": "Energy model trained with contrastive learning"
    },
    {
        "name": "Deep-Energy-Model",
        "description": "Deep network parameterizing energy function"
    },
    {
        "name": "Compositional-Energy-Model",
        "description": "Energy model with compositional structure"
    }
]