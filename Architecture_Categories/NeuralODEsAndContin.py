"""
Module for NeuralODEs&Continuous Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "NeuralODEs&Continuous",
        "description": "They allow simulating the continuous change of latent states, which opens up new possibilities for time series analysis, signal processing, and dynamic systems"
    }
]

@dataclass
class NeuralODEsAndContin:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Neural ODEs and Continuous-Time Neural Networks
Differential equation-based neural architectures
"""

NEURAL_ODE_CONTIN_ARCHITECTURES = [
    {
        "name": "Neural-ODE",
        "description": "Neural Ordinary Differential Equation"
    },
    {
        "name": "Neural-ODE-Base",
        "description": "Base Neural ODE architecture"
    },
    {
        "name": "Neural-ODE-ResNet",
        "description": "Neural ODE with ResNet parameterization"
    },
    {
        "name": "Neural-ODE-CNN",
        "description": "Convolutional Neural ODE"
    },
    {
        "name": "Neural-ODE-RNN",
        "description": "Recurrent Neural ODE"
    },
    {
        "name": "Augmented-Neural-ODE",
        "description": "Augmented Neural ODE with extra dimensions"
    },
    {
        "name": "ANODE-v1",
        "description": "First version of Augmented Neural ODE"
    },
    {
        "name": "ANODE-v2",
        "description": "Improved Augmented Neural ODE"
    },
    {
        "name": "FFJORD",
        "description": "Free-form Continuous Normalizing Flow"
    },
    {
        "name": "CNF",
        "description": "Continuous Normalizing Flow"
    },
    {
        "name": "OT-CNF",
        "description": "Optimal Transport Continuous Normalizing Flow"
    },
    {
        "name": "Wasserstein-CNF",
        "description": "Wasserstein Continuous Normalizing Flow"
    },
    {
        "name": "Latent-ODE",
        "description": "Latent Neural ODE for time series"
    },
    {
        "name": "ODE-RNN",
        "description": "ODE-based Recurrent Neural Network"
    },
    {
        "name": "ODE-LSTM",
        "description": "LSTM with ODE dynamics"
    },
    {
        "name": "GRU-ODE",
        "description": "GRU with continuous ODE evolution"
    },
    {
        "name": "GRU-ODE-Bayes",
        "description": "Bayesian GRU-ODE for uncertainty"
    },
    {
        "name": "Continuous-RNN",
        "description": "Continuous-time Recurrent Neural Network"
    },
    {
        "name": "Neural-CDE",
        "description": "Neural Controlled Differential Equation"
    },
    {
        "name": "Neural-SDE",
        "description": "Neural Stochastic Differential Equation"
    },
    {
        "name": "SDE-Net",
        "description": "Stochastic Differential Equation Network"
    },
    {
        "name": "Diffusion-SDE",
        "description": "SDE for diffusion models"
    },
    {
        "name": "Score-SDE",
        "description": "Score-based SDE for generation"
    },
    {
        "name": "Hamiltonian-NN",
        "description": "Hamiltonian Neural Network"
    },
    {
        "name": "HNN",
        "description": "Hamiltonian Neural Network for physics"
    },
    {
        "name": "Lagrangian-NN",
        "description": "Lagrangian Neural Network"
    },
    {
        "name": "LNN",
        "description": "Lagrangian Neural Network for mechanics"
    },
    {
        "name": "Symplectic-ODENet",
        "description": "Symplectic ODE Network for conservation"
    },
    {
        "name": "Deep-Hamiltonian",
        "description": "Deep Hamiltonian Neural Network"
    },
    {
        "name": "Deep-Lagrangian",
        "description": "Deep Lagrangian Neural Network"
    },
    {
        "name": "Physics-Informed-NN",
        "description": "Physics-Informed Neural Network"
    },
    {
        "name": "PINN",
        "description": "PINN for solving differential equations"
    },
    {
        "name": "XPINN",
        "description": "Extended PINN with domain decomposition"
    },
    {
        "name": "B-PINN",
        "description": "Bayesian Physics-Informed Neural Network"
    },
    {
        "name": "VPINN",
        "description": "Variational Physics-Informed Neural Network"
    },
    {
        "name": "fPINN",
        "description": "Fractional PINN for fractional PDEs"
    },
    {
        "name": "DeepONet",
        "description": "Deep Operator Network"
    },
    {
        "name": "Fourier-DeepONet",
        "description": "Fourier Neural Operator"
    },
    {
        "name": "FNO",
        "description": "Fourier Neural Operator for PDEs"
    },
    {
        "name": "FNO-2D",
        "description": "2D Fourier Neural Operator"
    },
    {
        "name": "FNO-3D",
        "description": "3D Fourier Neural Operator"
    },
    {
        "name": "Geo-FNO",
        "description": "Geometry-aware Fourier Neural Operator"
    },
    {
        "name": "U-NO",
        "description": "U-Net shaped Neural Operator"
    },
    {
        "name": "WNO",
        "description": "Wavelet Neural Operator"
    },
    {
        "name": "LOCA",
        "description": "Learning Operators with Coupled Attention"
    },
    {
        "name": "GNO",
        "description": "Graph Neural Operator"
    },
    {
        "name": "Continuous-Transformer",
        "description": "Transformer in continuous time"
    },
    {
        "name": "Neural-Flow",
        "description": "Neural Flow model"
    },
    {
        "name": "Continuous-Flow",
        "description": "Continuous Flow-based model"
    },
    {
        "name": "Neural-CP-Flow",
        "description": "Neural Continuous Piecewise Flow"
    },
    {
        "name": "Neural-Transport",
        "description": "Neural Transport model"
    },
    {
        "name": "Continuous-Depth-ResNet",
        "description": "ResNet with continuous depth"
    },
    {
        "name": "Infinitesimal-Transformer",
        "description": "Transformer with infinitesimal layers"
    },
    {
        "name": "Neural-Process",
        "description": "Neural Process for function learning"
    },
    {
        "name": "CNP",
        "description": "Conditional Neural Process"
    },
    {
        "name": "ANP",
        "description": "Attentive Neural Process"
    },
    {
        "name": "TNP",
        "description": "Transformer Neural Process"
    },
    {
        "name": "GNP",
        "description": "Gaussian Neural Process"
    },
    {
        "name": "Continuous-Bayesian-NN",
        "description": "Continuous-time Bayesian Neural Network"
    },
    {
        "name": "Neural-SPDE",
        "description": "Neural Stochastic Partial Differential Equation"
    },
    {
        "name": "Continuous-GNN",
        "description": "Continuous-time Graph Neural Network"
    },
    {
        "name": "Graph-ODE",
        "description": "Graph Neural ODE"
    },
    {
        "name": "Graph-CDE",
        "description": "Graph Controlled Differential Equation"
    },
    {
        "name": "Neural-Manifold",
        "description": "Neural Network on manifolds"
    },
    {
        "name": "Riemannian-NN",
        "description": "Riemannian Neural Network"
    },
    {
        "name": "Lie-Group-NN",
        "description": "Lie Group Neural Network"
    },
    {
        "name": "Equivariant-ODE",
        "description": "Equivariant Neural ODE"
    },
    {
        "name": "Continuous-Attention",
        "description": "Continuous-time Attention mechanism"
    },
    {
        "name": "Neural-Integral",
        "description": "Neural Integral Equation solver"
    },
    {
        "name": "Volterra-NN",
        "description": "Volterra Neural Network"
    },
    {
        "name": "Fredholm-NN",
        "description": "Fredholm Neural Network"
    }
]