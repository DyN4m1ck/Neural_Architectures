"""
Module for Архитектуры для малых данных и FEW-SHOT LEARNING
"""
from dataclasses import dataclass
from typing import Optional

# RL Architectures data
RL_ARCHITECTURES = [
    {
        "name": "Архитектуры для малых данных и FEW-SHOT LEARNING",
        "description": "Models are able to draw accurate conclusions based on an extremely limited set of examples (literally 1-5 samples), simulating the human ability to learn quickly."
    }
]

@dataclass
class SmallDataAndFewShow:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Small Data and Few-Shot Learning Architectures
Networks designed for limited data scenarios
"""

SMALL_DATA_FEWSHOT_ARCHITECTURES = [
    {
        "name": "ProtoNet",
        "description": "Prototypical Networks for few-shot classification"
    },
    {
        "name": "ProtoNet-ResNet12",
        "description": "ProtoNet with ResNet-12 backbone"
    },
    {
        "name": "ProtoNet-Conv4",
        "description": "ProtoNet with simple Conv4 backbone"
    },
    {
        "name": "ProtoNet-TiResNet",
        "description": "ProtoNet with Tiny ResNet backbone"
    },
    {
        "name": "MatchingNet",
        "description": "Matching Networks for one-shot learning"
    },
    {
        "name": "MatchingNet-Conv",
        "description": "Matching Network with convolutional encoder"
    },
    {
        "name": "MatchingNet-LSTM",
        "description": "Matching Network with LSTM encoder"
    },
    {
        "name": "RelationNet",
        "description": "Learning to compare for few-shot learning"
    },
    {
        "name": "RelationNet-ResNet",
        "description": "Relation Network with ResNet backbone"
    },
    {
        "name": "MAML",
        "description": "Model-Agnostic Meta-Learning for fast adaptation"
    },
    {
        "name": "MAML-ResNet",
        "description": "MAML with ResNet architecture"
    },
    {
        "name": "MAML-Conv",
        "description": "MAML with convolutional network"
    },
    {
        "name": "Meta-SGD",
        "description": "Meta-learning with learned optimizer"
    },
    {
        "name": "Reptile",
        "description": "Simple meta-learning algorithm"
    },
    {
        "name": "ANIL",
        "description": "Almost No Inner Loop for efficient meta-learning"
    },
    {
        "name": "BOIL",
        "description": "Body Only Inner Loop meta-learning"
    },
    {
        "name": "MetaOptNet",
        "description": "Meta-learning with differentiable optimization"
    },
    {
        "name": "MetaOptNet-ResNet",
        "description": "MetaOptNet with ResNet backbone"
    },
    {
        "name": "MetaOptNet-Conv",
        "description": "MetaOptNet with Conv backbone"
    },
    {
        "name": "LEO",
        "description": "Latent Embedding Optimization for few-shot"
    },
    {
        "name": "TADAM",
        "description": "Task-dependent adaptive metric for few-shot"
    },
    {
        "name": "SNAIL",
        "description": "Simple Neural Attentive Meta-Learner"
    },
    {
        "name": "MTL",
        "description": "Meta Transfer Learning for few-shot"
    },
    {
        "name": "MetaBaseline",
        "description": "Simple baseline for few-shot learning"
    },
    {
        "name": "SimpleShot",
        "description": "Revisiting nearest neighbor for few-shot"
    },
    {
        "name": "FEAT",
        "description": "Feature Transformation for few-shot learning"
    },
    {
        "name": "DeepEMD",
        "description": "Deep Earth Mover's Distance for few-shot"
    },
    {
        "name": "RENé",
        "description": "Rectified Embeddings for few-shot learning"
    },
    {
        "name": "FRN",
        "description": "Feature Reweighting Network for few-shot"
    },
    {
        "name": "SIB",
        "description": "Self-Imitation Learning for few-shot"
    },
    {
        "name": "EPNet",
        "description": "Edge Propagation Network for few-shot"
    },
    {
        "name": "AttMAML",
        "description": "Attention-based MAML for few-shot"
    },
    {
        "name": "CAMONet",
        "description": "Context Attention Modulation for few-shot"
    },
    {
        "name": "DCNet",
        "description": "Dense Classification Network for few-shot"
    },
    {
        "name": "FSCE",
        "description": "Few-Shot Contrastive Embedding"
    },
    {
        "name": "CovaMNet",
        "description": "Covariance Metric Network for few-shot"
    },
    {
        "name": "DeepBDC",
        "description": "Deep Brownian Distance Covariance"
    },
    {
        "name": "K-shot-NN",
        "description": "K-shot Nearest Neighbor classifier"
    },
    {
        "name": "Transductive-ProtoNet",
        "description": "ProtoNet with transductive inference"
    },
    {
        "name": "LaplacianShot",
        "description": "Laplacian regularization for few-shot"
    },
    {
        "name": "TIM",
        "description": "Transductive Information Maximization"
    },
    {
        "name": "Simple-CNAPS",
        "description": "Simple Conditional Neural Adaptive Processes"
    },
    {
        "name": "CNAPS",
        "description": "Conditional Neural Adaptive Processes"
    },
    {
        "name": "SUR",
        "description": "Self-Supervised Representation for few-shot"
    },
    {
        "name": "SelfSupervised-ProtoNet",
        "description": "ProtoNet with self-supervised pretraining"
    },
    {
        "name": "SimCLR-FewShot",
        "description": "SimCLR pretraining for few-shot learning"
    },
    {
        "name": "MoCo-FewShot",
        "description": "MoCo pretraining for few-shot learning"
    },
    {
        "name": "BYOL-FewShot",
        "description": "BYOL pretraining for few-shot learning"
    },
    {
        "name": "SwAV-FewShot",
        "description": "SwAV pretraining for few-shot learning"
    },
    {
        "name": "DINO-FewShot",
        "description": "DINO pretraining for few-shot learning"
    },
    {
        "name": "MAE-FewShot",
        "description": "Masked Autoencoder for few-shot learning"
    },
    {
        "name": "BEiT-FewShot",
        "description": "BEiT pretraining for few-shot learning"
    },
    {
        "name": "CrossTransformers",
        "description": "Cross-transformers for few-shot learning"
    },
    {
        "name": "FewShot-ViT",
        "description": "Vision Transformer for few-shot learning"
    },
    {
        "name": "FewShot-Swin",
        "description": "Swin Transformer for few-shot learning"
    },
    {
        "name": "Tip-Adapter",
        "description": "Training-free adapter for few-shot CLIP"
    },
    {
        "name": "Tip-Adapter-F",
        "description": "Fine-tuned Tip-Adapter for few-shot"
    },
    {
        "name": "LP-CLIP",
        "description": "Linear Probe CLIP for few-shot"
    },
    {
        "name": "CoOp",
        "description": "Context Optimization for CLIP few-shot"
    },
    {
        "name": "CoCoOp",
        "description": "Conditional Context Optimization"
    },
    {
        "name": "MaPLe",
        "description": "Multi-modal Prompt Learning"
    },
    {
        "name": "PromptSRC",
        "description": "Prompt Source for few-shot learning"
    },
    {
        "name": "AdaPT",
        "description": "Adaptive Prompt Tuning for few-shot"
    },
    {
        "name": "MetaPrompt",
        "description": "Meta-learning for prompt optimization"
    },
    {
        "name": "ProGrad",
        "description": "Prompt Gradient for few-shot CLIP"
    },
    {
        "name": "LoRA-FewShot",
        "description": "Low-Rank Adaptation for few-shot learning"
    },
    {
        "name": "Adapter-FewShot",
        "description": "Adapter modules for few-shot learning"
    },
    {
        "name": "Prefix-FewShot",
        "description": "Prefix tuning for few-shot learning"
    },
    {
        "name": "IA3-FewShot",
        "description": "Infused Adapter for few-shot learning"
    }
]