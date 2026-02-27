"""
Module for Архитектуры для поиска архитектур (NAS - Neural Architecture Search).
"""
from dataclasses import dataclass
from typing import Optional

# NAS Architectures data
NAS_ARCHITECTURES = [
    {
        "name": "Архитектуры для поиска архитектур (NAS)",
        "description": "Архитектуры, используемые для автоматического поиска оптимальных архитектур нейронных сетей."
    }
]

@dataclass
class NAS:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Neural Architecture Search (NAS) Architectures
Automatically discovered network architectures
"""

NAS_ARCHITECTURES = [
    {
        "name": "NASNet-A",
        "description": "Neural Architecture Search discovered normal and reduction cells"
    },
    {
        "name": "NASNet-B",
        "description": "Alternative NASNet variant with different cell structure"
    },
    {
        "name": "NASNet-C",
        "description": "Third NASNet variant optimized for mobile devices"
    },
    {
        "name": "ENAS",
        "description": "Efficient Neural Architecture Search with parameter sharing"
    },
    {
        "name": "DARTS",
        "description": "Differentiable Architecture Search using gradient-based optimization"
    },
    {
        "name": "DARTS-v2",
        "description": "Improved DARTS with second-order approximation"
    },
    {
        "name": "PDARTS",
        "description": "Progressive DARTS with increasing depth during search"
    },
    {
        "name": "SDARTS",
        "description": "Stabilized DARTS with adversarial training"
    },
    {
        "name": "PC-DARTS",
        "description": "Partial Channel DARTS for reduced memory consumption"
    },
    {
        "name": "DARTS+",
        "description": "Improved DARTS with early stopping and zero-cost proxies"
    },
    {
        "name": "AmoebaNet-A",
        "description": "Evolutionary NAS with regularized evolution algorithm"
    },
    {
        "name": "AmoebaNet-B",
        "description": "Improved AmoebaNet with better cell structure"
    },
    {
        "name": "AmoebaNet-C",
        "description": "Third generation AmoebaNet with enhanced performance"
    },
    {
        "name": "PNAS",
        "description": "Progressive Neural Architecture Search"
    },
    {
        "name": "PNAS-LS",
        "description": "PNAS with layer-wise search strategy"
    },
    {
        "name": "MNASNet",
        "description": "Platform-aware NAS optimizing for mobile latency"
    },
    {
        "name": "MNASNet-A1",
        "description": "MNASNet variant A1 balancing accuracy and latency"
    },
    {
        "name": "MNASNet-A2",
        "description": "MNASNet variant A2 with different trade-offs"
    },
    {
        "name": "MNASNet-B1",
        "description": "MNASNet variant B1 optimized for speed"
    },
    {
        "name": "FBNet-A",
        "description": "Facebook NAS variant A for specific hardware"
    },
    {
        "name": "FBNet-B",
        "description": "Facebook NAS variant B with different constraints"
    },
    {
        "name": "FBNet-C",
        "description": "Facebook NAS variant C optimized for accuracy"
    },
    {
        "name": "FBNet-v2",
        "description": "Second generation FBNet with improved search"
    },
    {
        "name": "FBNet-v3",
        "description": "Third generation FBNet with multi-objective optimization"
    },
    {
        "name": "ProxylessNAS",
        "description": "Direct architecture search on target task without proxy"
    },
    {
        "name": "ProxylessNAS-Mobile",
        "description": "ProxylessNAS optimized for mobile devices"
    },
    {
        "name": "ProxylessNAS-GPU",
        "description": "ProxylessNAS optimized for GPU inference"
    },
    {
        "name": "ProxylessNAS-FPGA",
        "description": "ProxylessNAS optimized for FPGA deployment"
    },
    {
        "name": "Once-for-All",
        "description": "OFA network supporting multiple architectures from one model"
    },
    {
        "name": "OFA-ResNet-50",
        "description": "Once-for-All ResNet-50 with elastic depth and width"
    },
    {
        "name": "OFA-MobileNet-v3",
        "description": "OFA variant of MobileNet-v3 with flexible kernels"
    },
    {
        "name": "AutoML-MobileNet",
        "description": "AutoML discovered MobileNet architecture"
    },
    {
        "name": "MNasNet-1.3",
        "description": "MNASNet with 1.3x depth multiplier"
    },
    {
        "name": "EfficientNet-NAS",
        "description": "NAS-discovered EfficientNet architecture"
    },
    {
        "name": "TinyNAS",
        "description": "NAS for extreme resource constraints"
    },
    {
        "name": "MicroNet",
        "description": "Ultra-efficient NAS for micro-controllers"
    },
    {
        "name": "MCUNet",
        "description": "NAS for micro-controllers with tiny memory"
    },
    {
        "name": "AutoKeras-CNN",
        "description": "AutoKeras discovered CNN architecture"
    },
    {
        "name": "AutoKeras-ResNet",
        "description": "AutoKeras discovered ResNet variant"
    },
    {
        "name": "AutoML-Zero",
        "description": "NAS discovering algorithms from scratch"
    },
    {
        "name": "Evolving-Transformer",
        "description": "Evolutionary search for optimal Transformer"
    },
    {
        "name": "Evolved-Transformer",
        "description": "NAS-discovered Transformer for sequence modeling"
    },
    {
        "name": "NAS-Bench-101",
        "description": "Tabular NAS benchmark with 423K architectures"
    },
    {
        "name": "NAS-Bench-201",
        "description": "Extended NAS benchmark with 15K architectures"
    },
    {
        "name": "NAS-Bench-301",
        "description": "Surrogate-based NAS benchmark"
    },
    {
        "name": "TransNAS-Bench",
        "description": "NAS benchmark for transfer learning"
    },
    {
        "name": "HW-NAS-Bench",
        "description": "Hardware-aware NAS benchmark"
    },
    {
        "name": "NAS-FPN",
        "description": "NAS-discovered Feature Pyramid Network"
    },
    {
        "name": "NAS-FCOS",
        "description": "NAS-discovered FCOS for object detection"
    },
    {
        "name": "DetNAS",
        "description": "NAS for object detection backbones"
    }
]