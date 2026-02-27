"""
Module for State Space Models and Post-Transformer architectures.
"""
from dataclasses import dataclass
from typing import Optional

# State Space Models and Post-Transformer architectures data
STATE_SPACE_ARCHITECTURES = [
    {
        "name": "State Space Models and Post-Transformer Architectures",
        "description": "Modern architectures including state space models and other approaches that emerged after transformer dominance."
    }
]

@dataclass
class StateSpace:
    """
    Represents a State Space Model Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
State Space Models and Transformer Architectures
Modern sequence modeling with state space approaches
"""

STATE_SPACE_ARCHITECTURES = [
    {
        "name": "S4",
        "description": "Structured State Space sequence model for long-range dependencies"
    },
    {
        "name": "S4D",
        "description": "S4 with diagonal state matrix for efficiency"
    },
    {
        "name": "S4-LegS",
        "description": "S4 with Legendre polynomial basis"
    },
    {
        "name": "S4-FouT",
        "description": "S4 with Fourier transform basis"
    },
    {
        "name": "S5",
        "description": "Simplified S4 with parallel scan for speed"
    },
    {
        "name": "Mamba",
        "description": "Selective State Space Model with input-dependent parameters"
    },
    {
        "name": "Mamba-130M",
        "description": "Small Mamba model with 130 million parameters"
    },
    {
        "name": "Mamba-370M",
        "description": "Medium Mamba model with 370 million parameters"
    },
    {
        "name": "Mamba-790M",
        "description": "Large Mamba model with 790 million parameters"
    },
    {
        "name": "Mamba-1.4B",
        "description": "Mamba model with 1.4 billion parameters"
    },
    {
        "name": "Mamba-2.8B",
        "description": "Mamba model with 2.8 billion parameters"
    },
    {
        "name": "Jamba",
        "description": "Hybrid Mamba-Transformer architecture"
    },
    {
        "name": "Jamba-1.5-Mini",
        "description": "Smaller Jamba variant for efficient inference"
    },
    {
        "name": "Jamba-1.5-Large",
        "description": "Larger Jamba variant for high performance"
    },
    {
        "name": "H3",
        "description": "Hungry Hungry Hippo state space model"
    },
    {
        "name": "H3-125M",
        "description": "Small H3 model with 125M parameters"
    },
    {
        "name": "H3-350M",
        "description": "Medium H3 model with 350M parameters"
    },
    {
        "name": "H3-1.3B",
        "description": "Large H3 model with 1.3B parameters"
    },
    {
        "name": "Hyena",
        "description": "Sub-quadratic sequence model with implicit convolutions"
    },
    {
        "name": "HyenaDNA",
        "description": "Hyena model for genomic sequence modeling"
    },
    {
        "name": "Long-Conv",
        "description": "Long convolution sequence model"
    },
    {
        "name": "Griffin",
        "description": "Gated linear attention with convolutions"
    },
    {
        "name": "Griffin-2B",
        "description": "Griffin model with 2 billion parameters"
    },
    {
        "name": "Griffin-6B",
        "description": "Griffin model with 6 billion parameters"
    },
    {
        "name": "RWKV",
        "description": "Receptance Weighted Key Value for RNN-Transformer hybrid"
    },
    {
        "name": "RWKV-4-169M",
        "description": "Small RWKV v4 model"
    },
    {
        "name": "RWKV-4-430M",
        "description": "Medium RWKV v4 model"
    },
    {
        "name": "RWKV-4-1.5B",
        "description": "Large RWKV v4 model"
    },
    {
        "name": "RWKV-4-3B",
        "description": "RWKV v4 with 3 billion parameters"
    },
    {
        "name": "RWKV-4-7B",
        "description": "RWKV v4 with 7 billion parameters"
    },
    {
        "name": "RWKV-4-14B",
        "description": "RWKV v4 with 14 billion parameters"
    },
    {
        "name": "RWKV-5-Eagle",
        "description": "RWKV v5 with improved attention mechanism"
    },
    {
        "name": "RWKV-6-Falcon",
        "description": "RWKV v6 with enhanced performance"
    },
    {
        "name": "RetNet",
        "description": "Retentive Network for efficient sequence modeling"
    },
    {
        "name": "RetNet-Base",
        "description": "Base RetNet model"
    },
    {
        "name": "RetNet-Large",
        "description": "Large RetNet model"
    },
    {
        "name": "RetNet-XL",
        "description": "Extra-large RetNet model"
    },
    {
        "name": "GLA",
        "description": "Gated Linear Attention for efficient transformers"
    },
    {
        "name": "DeltaNet",
        "description": "Delta rule based state space model"
    },
    {
        "name": "VMamba",
        "description": "Visual Mamba for computer vision tasks"
    },
    {
        "name": "Vim",
        "description": "Vision Mamba for image recognition"
    },
    {
        "name": "Vim-Tiny",
        "description": "Tiny Vision Mamba variant"
    },
    {
        "name": "Vim-Small",
        "description": "Small Vision Mamba variant"
    },
    {
        "name": "Vim-Base",
        "description": "Base Vision Mamba variant"
    },
    {
        "name": "Vamamba",
        "description": "Video Mamba for video understanding"
    },
    {
        "name": "AudioMamba",
        "description": "Mamba for audio processing"
    },
    {
        "name": "Mamba-2",
        "description": "Second generation Mamba with improved efficiency"
    },
    {
        "name": "Mamba-2-130M",
        "description": "Small Mamba-2 model"
    },
    {
        "name": "Mamba-2-370M",
        "description": "Medium Mamba-2 model"
    },
    {
        "name": "Mamba-2-780M",
        "description": "Large Mamba-2 model"
    },
    {
        "name": "Mamba-2-1.3B",
        "description": "Mamba-2 with 1.3B parameters"
    },
    {
        "name": "Mamba-2-2.7B",
        "description": "Mamba-2 with 2.7B parameters"
    },
    {
        "name": "Zamba",
        "description": "Hybrid SSM-Transformer model"
    },
    {
        "name": "Zamba-1.3B",
        "description": "Small Zamba model"
    },
    {
        "name": "Zamba-7B",
        "description": "Large Zamba model"
    },
    {
        "name": "Minerva",
        "description": "State space model for mathematical reasoning"
    },
    {
        "name": "LSSL",
        "description": "Linear State Space Layer for sequences"
    },
    {
        "name": "DSS",
        "description": "Diagonal State Space model"
    },
    {
        "name": "GSS",
        "description": "Gated State Space model"
    },
    {
        "name": "SSM-Conv",
        "description": "State Space Model with convolutional layers"
    },
    {
        "name": "Bi-Mamba",
        "description": "Bidirectional Mamba for context understanding"
    },
    {
        "name": "Cross-Mamba",
        "description": "Cross-modal Mamba for multimodal tasks"
    },
    {
        "name": "Mamba-LLaMA",
        "description": "Mamba integrated with LLaMA architecture"
    },
    {
        "name": "Mambaformer",
        "description": "Hybrid Mamba-Transformer architecture"
    },
    {
        "name": "Sparse-Mamba",
        "description": "Sparse Mamba for efficient computation"
    },
    {
        "name": "Quantized-Mamba",
        "description": "Quantized Mamba for edge deployment"
    },
    {
        "name": "Distilled-Mamba",
        "description": "Distilled Mamba for smaller footprint"
    },
    {
        "name": "Multi-Scale-Mamba",
        "description": "Mamba with multi-scale processing"
    },
    {
        "name": "Hierarchical-Mamba",
        "description": "Hierarchical Mamba for complex sequences"
    }
]