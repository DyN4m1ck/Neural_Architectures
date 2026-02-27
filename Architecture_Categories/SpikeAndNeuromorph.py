"""
Module for Спайковые и нейроморфные архитектуры
"""
from dataclasses import dataclass
from typing import Optional

# Specialized Architectures data
SPECIALIZED_ARCHITECTURES = [
    {
        "name": "Spike and neuromorphic architectures",
        "description": "simulations of the biological principles of the brain at the hardware and software levels to achieve extreme energy efficiency and real-time operation"
    }
]

@dataclass
class SpikeAndNeuromorph:
    """
    Represents a Specialized Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Spiking Neural Networks and Neuromorphic Architectures
Event-based and brain-inspired computing
"""

SPIKE_NEUROMORPHIC_ARCHITECTURES = [
    {
        "name": "LIF-Neuron",
        "description": "Leaky Integrate-and-Fire spiking neuron model"
    },
    {
        "name": "IF-Neuron",
        "description": "Integrate-and-Fire spiking neuron model"
    },
    {
        "name": "Hodgkin-Huxley",
        "description": "Biologically realistic neuron model"
    },
    {
        "name": "Izhikevich",
        "description": "Efficient biologically plausible neuron model"
    },
    {
        "name": "AdEx",
        "description": "Adaptive Exponential integrate-and-fire neuron"
    },
    {
        "name": "SNN-LIF",
        "description": "Spiking Neural Network with LIF neurons"
    },
    {
        "name": "SNN-IF",
        "description": "Spiking Neural Network with IF neurons"
    },
    {
        "name": "Deep-SNN",
        "description": "Deep Spiking Neural Network architecture"
    },
    {
        "name": "Conv-SNN",
        "description": "Convolutional Spiking Neural Network"
    },
    {
        "name": "ResNet-SNN",
        "description": "Residual Spiking Neural Network"
    },
    {
        "name": "VGG-SNN",
        "description": "VGG-style Spiking Neural Network"
    },
    {
        "name": "Spiking-YOLO",
        "description": "Spiking neural network for object detection"
    },
    {
        "name": "Spiking-ResNet-18",
        "description": "18-layer Spiking ResNet"
    },
    {
        "name": "Spiking-ResNet-34",
        "description": "34-layer Spiking ResNet"
    },
    {
        "name": "Spiking-ResNet-50",
        "description": "50-layer Spiking ResNet"
    },
    {
        "name": "SEW-ResNet",
        "description": "Spiking Element-Wise ResNet"
    },
    {
        "name": "Spikformer",
        "description": "Spiking Transformer architecture"
    },
    {
        "name": "Spiking-Transformer",
        "description": "Transformer with spiking neurons"
    },
    {
        "name": "SpikeGPT",
        "description": "Spiking neural network for language generation"
    },
    {
        "name": "Spiking-BERT",
        "description": "BERT implemented with spiking neurons"
    },
    {
        "name": "Event-CNN",
        "description": "CNN for event camera data processing"
    },
    {
        "name": "Event-ResNet",
        "description": "ResNet for event-based vision"
    },
    {
        "name": "EV-Net",
        "description": "Event-based Vision Network"
    },
    {
        "name": "EST",
        "description": "Event-based Spiking Transformer"
    },
    {
        "name": "V2E",
        "description": "Video to Event conversion network"
    },
    {
        "name": "DVS-CNN",
        "description": "CNN for Dynamic Vision Sensor data"
    },
    {
        "name": "DVS-ResNet",
        "description": "ResNet for DVS event streams"
    },
    {
        "name": "Neuromorphic-Vision",
        "description": "Vision processing for neuromorphic sensors"
    },
    {
        "name": "Loihi-SNN",
        "description": "SNN optimized for Intel Loihi chip"
    },
    {
        "name": "TrueNorth-Net",
        "description": "Network for IBM TrueNorth chip"
    },
    {
        "name": "SpiNNaker-Net",
        "description": "Network for SpiNNaker neuromorphic system"
    },
    {
        "name": "BrainScaleS-Net",
        "description": "Network for BrainScaleS platform"
    },
    {
        "name": "ODIN",
        "description": "Online Dynamic Inference for SNNs"
    },
    {
        "name": "TSSL-BP",
        "description": "Temporal Spike Sequence Learning via BP"
    },
    {
        "name": "STDP-Learning",
        "description": "Spike-Timing-Dependent Plasticity learning"
    },
    {
        "name": "R-STDP",
        "description": "Reward-modulated STDP learning"
    },
    {
        "name": "Surrogate-Gradient",
        "description": "Surrogate gradient learning for SNNs"
    },
    {
        "name": "Direct-Training-SNN",
        "description": "Direct training method for SNNs"
    },
    {
        "name": "ANN2SNN",
        "description": "ANN to SNN conversion method"
    },
    {
        "name": "Rate-Coding-SNN",
        "description": "Rate-coded Spiking Neural Network"
    },
    {
        "name": "Temporal-Coding-SNN",
        "description": "Temporally coded Spiking Neural Network"
    },
    {
        "name": "Population-Coding-SNN",
        "description": "Population-coded Spiking Neural Network"
    },
    {
        "name": "Hybrid-ANN-SNN",
        "description": "Hybrid ANN-SNN architecture"
    },
    {
        "name": "Neuromorphic-RL",
        "description": "Reinforcement Learning on neuromorphic hardware"
    },
    {
        "name": "Spiking-Actor-Critic",
        "description": "Actor-Critic with spiking neurons"
    },
    {
        "name": "Neuromorphic-ODR",
        "description": "Optical Character Recognition on neuromorphic chips"
    },
    {
        "name": "Event-Object-Detection",
        "description": "Object detection for event cameras"
    },
    {
        "name": "Event-Tracking",
        "description": "Visual tracking with event data"
    },
    {
        "name": "Neuromorphic-Audio",
        "description": "Audio processing on neuromorphic hardware"
    },
    {
        "name": "Cochlea-Net",
        "description": "Cochlea-inspired spiking audio network"
    },
    {
        "name": "Neuromorphic-Nav",
        "description": "Navigation on neuromorphic systems"
    },
    {
        "name": "Event-SLAM",
        "description": "SLAM using event camera data"
    },
    {
        "name": "Spiking-LSTM",
        "description": "LSTM implemented with spiking neurons"
    },
    {
        "name": "Spiking-GRU",
        "description": "GRU implemented with spiking neurons"
    },
    {
        "name": "Neurogrid-Net",
        "description": "Network for Neurogrid neuromorphic system"
    },
    {
        "name": "Dynap-Net",
        "description": "Network for Dynap-SEL neuromorphic chip"
    },
    {
        "name": "Speck-Net",
        "description": "Network for Speck neuromorphic sensor"
    },
    {
        "name": "Prophesee-Net",
        "description": "Network for Prophesee event cameras"
    },
    {
        "name": "IniVation-Net",
        "description": "Network for IniVation event sensors"
    },
    {
        "name": "CeleX-Net",
        "description": "Network for CeleX neuromorphic sensor"
    },
    {
        "name": "SKIM",
        "description": "Sparse Kernel Iterative Machine for SNNs"
    },
    {
        "name": "ReSuMe",
        "description": "Remote Supervised Method for SNN training"
    },
    {
        "name": "Chronotron",
        "description": "Precise spike timing learning algorithm"
    },
    {
        "name": "SPAN",
        "description": "Spike Pattern Association Neuron"
    },
    {
        "name": "Tempotron",
        "description": "Tempotron learning rule for SNNs"
    },
    {
        "name": "Multi-Spike-Tempotron",
        "description": "Extended Tempotron for multiple spikes"
    },
    {
        "name": "NormAD",
        "description": "Normalized Approximate Descent for SNNs"
    },
    {
        "name": "SLAYER",
        "description": "Spike Layer Error Reassignment in Time"
    },
    {
        "name": "RMP-Loss",
        "description": "Reset Membrane Potential Loss for SNNs"
    },
    {
        "name": "GLIF",
        "description": "Generalized Leaky Integrate-and-Fire neuron"
    },
    {
        "name": "ALIF",
        "description": "Adaptive Leaky Integrate-and-Fire neuron"
    },
    {
        "name": "PLIF",
        "description": "Parametric Leaky Integrate-and-Fire neuron"
    }
]