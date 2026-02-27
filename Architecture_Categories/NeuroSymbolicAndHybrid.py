"""
Module for Neuro-Symbolic&Hybrid Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Neuro-Symbolic&Hybrid Architectures",
        "description": "architectures where learnability (the ability to extract knowledge from experience) is combined with determinism (the ability to follow strict rules)"
    }
]

@dataclass
class NeuroSymbolicAndHybrid:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Neuro-Symbolic and Hybrid Neural Architectures
Combining neural networks with symbolic reasoning
"""

NEURO_SYMBOLIC_HYBRID_ARCHITECTURES = [
    {
        "name": "Neural-Theorem-Prover",
        "description": "Neural network for automated theorem proving"
    },
    {
        "name": "DeepProbLog",
        "description": "Deep probabilistic logic programming"
    },
    {
        "name": "Neural-Logic-Network",
        "description": "Neural network implementing logical operations"
    },
    {
        "name": "NLN-AND",
        "description": "Neural Logic Network with AND gate"
    },
    {
        "name": "NLN-OR",
        "description": "Neural Logic Network with OR gate"
    },
    {
        "name": "NLN-NOT",
        "description": "Neural Logic Network with NOT gate"
    },
    {
        "name": "TensorLog",
        "description": "Differentiable logic programming framework"
    },
    {
        "name": "Logic-LM",
        "description": "Logic-enhanced Language Model"
    },
    {
        "name": "Neural-Symbolic-Learner",
        "description": "Combined neural and symbolic learning"
    },
    {
        "name": "NS-CL",
        "description": "Neuro-Symbolic Concept Learner"
    },
    {
        "name": "NS-VQA",
        "description": "Neuro-Symbolic Visual Question Answering"
    },
    {
        "name": "NS-DR",
        "description": "Neuro-Symbolic Dynamic Reasoning"
    },
    {
        "name": "MAC-Network",
        "description": "Memory, Attention, Composition for reasoning"
    },
    {
        "name": "Graph-Network",
        "description": "Graph Neural Network for relational reasoning"
    },
    {
        "name": "Relation-Network",
        "description": "Network for learning relationships"
    },
    {
        "name": "Compositional-NN",
        "description": "Compositional Neural Network"
    },
    {
        "name": "Module-Network",
        "description": "Modular architecture for reasoning"
    },
    {
        "name": "Neural-Program-Interpreter",
        "description": "Neural network interpreting programs"
    },
    {
        "name": "Neural-Programmer",
        "description": "Neural network that writes programs"
    },
    {
        "name": "Neural-GPU",
        "description": "Neural network with GPU-like memory"
    },
    {
        "name": "Neural-Turing-Machine",
        "description": "Neural network with external memory"
    },
    {
        "name": "Differentiable-Neural-Computer",
        "description": "DNC with advanced memory addressing"
    },
    {
        "name": "Memory-Network",
        "description": "Network with explicit memory component"
    },
    {
        "name": "End-to-End-Memory-Network",
        "description": "End-to-end trainable memory network"
    },
    {
        "name": "Dynamic-Memory-Network",
        "description": "Memory network with dynamic updates"
    },
    {
        "name": "Key-Value-Memory-Network",
        "description": "Memory network with key-value addressing"
    },
    {
        "name": "Sparse-Differentiable-Neural-Computer",
        "description": "Sparse DNC for efficiency"
    },
    {
        "name": "Neural-Stack",
        "description": "Neural network with stack memory"
    },
    {
        "name": "Neural-Queue",
        "description": "Neural network with queue memory"
    },
    {
        "name": "Neural-Dictionary",
        "description": "Neural network with dictionary memory"
    },
    {
        "name": "Neural-Program-Synthesis",
        "description": "Neural network for program synthesis"
    },
    {
        "name": "RobustFill",
        "description": "Neural program synthesis for string manipulation"
    },
    {
        "name": "DeepCoder",
        "description": "Learning to write programs from examples"
    },
    {
        "name": "Solar",
        "description": "Synthesis of programs with neural guidance"
    },
    {
        "name": "Neural-Symbolic-VQA",
        "description": "VQA with neuro-symbolic reasoning"
    },
    {
        "name": "Neural-Symbolic-RL",
        "description": "Reinforcement Learning with symbolic reasoning"
    },
    {
        "name": "Symbolic-DQN",
        "description": "DQN with symbolic state representation"
    },
    {
        "name": "Neural-Logic-RL",
        "description": "RL with neural logic reasoning"
    },
    {
        "name": "Concept-Bottleneck",
        "description": "Model with interpretable concept layer"
    },
    {
        "name": "Explainable-NN",
        "description": "Neural network with built-in explanations"
    },
    {
        "name": "Interpretable-CNN",
        "description": "CNN with interpretable features"
    },
    {
        "name": "Attention-Explanation",
        "description": "Attention mechanism for explanations"
    },
    {
        "name": "Rationale-Network",
        "description": "Network generating rationales for predictions"
    },
    {
        "name": "Self-Explaining-NN",
        "description": "Neural network that explains itself"
    },
    {
        "name": "Prototype-Network",
        "description": "Network using prototypes for classification"
    },
    {
        "name": "Case-Based-NN",
        "description": "Neural network with case-based reasoning"
    },
    {
        "name": "Analogical-NN",
        "description": "Neural network for analogical reasoning"
    },
    {
        "name": "Causal-NN",
        "description": "Neural network with causal reasoning"
    },
    {
        "name": "Counterfactual-NN",
        "description": "Neural network for counterfactual reasoning"
    },
    {
        "name": "Bayesian-NN",
        "description": "Bayesian Neural Network for uncertainty"
    },
    {
        "name": "Probabilistic-NN",
        "description": "Probabilistic Neural Network"
    },
    {
        "name": "Fuzzy-NN",
        "description": "Fuzzy Neural Network for uncertain reasoning"
    },
    {
        "name": "Rough-NN",
        "description": "Rough set-based Neural Network"
    },
    {
        "name": "Quantum-NN",
        "description": "Quantum Neural Network architecture"
    },
    {
        "name": "Hybrid-Classical-Quantum",
        "description": "Hybrid classical-quantum neural network"
    },
    {
        "name": "Analog-NN",
        "description": "Analog Neural Network for continuous processing"
    },
    {
        "name": "Digital-Analog-Hybrid",
        "description": "Hybrid digital-analog neural network"
    },
    {
        "name": "Optical-NN",
        "description": "Optical Neural Network for light-based computing"
    },
    {
        "name": "Photonic-NN",
        "description": "Photonic Neural Network architecture"
    },
    {
        "name": "Memristor-NN",
        "description": "Memristor-based Neural Network"
    },
    {
        "name": "Spintronic-NN",
        "description": "Spintronic Neural Network architecture"
    },
    {
        "name": "DNA-NN",
        "description": "DNA-based Neural Network"
    },
    {
        "name": "Molecular-NN",
        "description": "Molecular Neural Network architecture"
    },
    {
        "name": "Chemical-NN",
        "description": "Chemical reaction-based Neural Network"
    },
    {
        "name": "Biological-NN",
        "description": "Biological Neural Network using cells"
    },
    {
        "name": "Organoid-NN",
        "description": "Brain organoid-based computing"
    },
    {
        "name": "Wetware-NN",
        "description": "Wetware Neural Network architecture"
    },
    {
        "name": "Biohybrid-NN",
        "description": "Biological-electronic hybrid neural network"
    },
    {
        "name": "Cyborg-NN",
        "description": "Cyborg neural network architecture"
    }
]