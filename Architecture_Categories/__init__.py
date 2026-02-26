"""
Architecture Categories module initialization.
"""

from .CNN import CNN
from .EfficientAndMobile import EfficientAndMobile
from .EnergyAndEquilibriaum import EnergyAndEquilibriaum
from .FeedForward import FeedForward
from .GNN import GNN
from .Generative import Generative
from .Multimodal import Multimodal
from .NAS import NAS
from .NeuralODEsAndContin import NeuralODEsAndContin
from .NeuroSymbolicAndHybrid import NeuroSymbolicAndHybrid
from .RL import RL
from .RecAndSeq import RecAndSeq
from .SmallDataAndFewShot import SmallDataAndFewShow
from .Specialized import Specialized
from .SpikeAndNeuromorph import SpikeAndNeuromorph
from .StateSpace import StateSpace
from .TransformersAndAttention import TransformersAndAttention

__all__ = [
    "CNN",
    "EfficientMobile",
    "EnergyEquilibrium",
    "FeedForward",
    "GNN",
    "Generative",
    "Multimodal",
    "NAS",
    "NeuralODEsContin",
    "NeuroSymbolicHybrid",
    "RL",
    "RecSeq",
    "SmallDataFewShot",
    "Specialized",
    "SpikeNeuromorph",
    "StateSpace",
    "TransformersAttention"
]