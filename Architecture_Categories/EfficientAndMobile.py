"""
Module for Efficient & Mobile Architectures
"""
from dataclasses import dataclass
from typing import Optional


# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Efficient & Mobile Architectures",
        "description": "structured software design patterns (MVC, MVP, MVVM, MVI) that ensure high performance, ease of support, and scalability of applications."
    }
]

@dataclass
class EfficientAndMobile:
    """
    Represents a Convolutional Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Efficient and Mobile Neural Network Architectures
Optimized for resource-constrained environments
"""

EFFICIENT_MOBILE_ARCHITECTURES = [
    {
        "name": "MobileNet-v1-0.25",
        "description": "Ultra-lightweight MobileNet with 0.25 width multiplier for extreme efficiency"
    },
    {
        "name": "MobileNet-v1-0.5",
        "description": "MobileNet with 0.5 width multiplier balancing speed and accuracy"
    },
    {
        "name": "MobileNet-v1-0.75",
        "description": "MobileNet with 0.75 width multiplier for mobile applications"
    },
    {
        "name": "MobileNet-v2-0.35",
        "description": "Lightweight MobileNet-v2 with inverted residuals and reduced width"
    },
    {
        "name": "MobileNet-v2-1.4",
        "description": "Wider MobileNet-v2 for improved accuracy on mobile devices"
    },
    {
        "name": "MobileNet-v3-Small",
        "description": "Small variant optimized for latency using neural architecture search"
    },
    {
        "name": "MobileNet-v3-Large",
        "description": "Large MobileNet-v3 with advanced squeeze-and-excitation blocks"
    },
    {
        "name": "MobileNetV4-Conv-Small",
        "description": "Latest MobileNetV4 optimized for mobile convolution operations"
    },
    {
        "name": "MobileNetV4-Hybrid",
        "description": "Hybrid MobileNetV4 combining convolution and attention mechanisms"
    },
    {
        "name": "ShuffleNet-v1-0.5x",
        "description": "ShuffleNet with 0.5x channels for ultra-fast mobile inference"
    },
    {
        "name": "ShuffleNet-v1-1x",
        "description": "Standard ShuffleNet with channel shuffle for efficient computation"
    },
    {
        "name": "ShuffleNet-v1-2x",
        "description": "Wider ShuffleNet for better accuracy on mobile platforms"
    },
    {
        "name": "ShuffleNet-v2-0.5x",
        "description": "Improved ShuffleNet-v2 with optimized memory access patterns"
    },
    {
        "name": "ShuffleNet-v2-1x",
        "description": "Standard ShuffleNet-v2 balancing speed and accuracy"
    },
    {
        "name": "ShuffleNet-v2-1.5x",
        "description": "Wider ShuffleNet-v2 for enhanced mobile performance"
    },
    {
        "name": "ShuffleNet-v2-2x",
        "description": "Maximum width ShuffleNet-v2 for mobile applications"
    },
    {
        "name": "SqueezeNet-1.0",
        "description": "Original SqueezeNet with fire modules achieving AlexNet accuracy"
    },
    {
        "name": "SqueezeNet-1.1",
        "description": "Improved SqueezeNet with 2.4x fewer parameters than v1.0"
    },
    {
        "name": "EfficientNet-Lite0",
        "description": "Mobile-friendly EfficientNet without squeeze-and-excitation"
    },
    {
        "name": "EfficientNet-Lite1",
        "description": "Scaled EfficientNet-Lite for mobile and edge devices"
    },
    {
        "name": "EfficientNet-Lite2",
        "description": "Medium EfficientNet-Lite variant for mobile deployment"
    },
    {
        "name": "EfficientNet-Lite3",
        "description": "Larger EfficientNet-Lite with improved mobile accuracy"
    },
    {
        "name": "EfficientNet-Lite4",
        "description": "Largest EfficientNet-Lite for high-performance mobile inference"
    },
    {
        "name": "EfficientNet-EdgeTPU-S",
        "description": "Small EfficientNet optimized for Google Edge TPU accelerators"
    },
    {
        "name": "EfficientNet-EdgeTPU-M",
        "description": "Medium EfficientNet designed for Edge TPU deployment"
    },
    {
        "name": "EfficientNet-EdgeTPU-L",
        "description": "Large EfficientNet optimized for Edge TPU performance"
    },
    {
        "name": "GhostNet-1.0",
        "description": "GhostNet generating more feature maps from cheap operations"
    },
    {
        "name": "GhostNet-1.3",
        "description": "Wider GhostNet for improved accuracy on mobile devices"
    },
    {
        "name": "MixNet-S",
        "description": "Small MixNet using mixed depthwise convolution kernel sizes"
    },
    {
        "name": "MixNet-M",
        "description": "Medium MixNet balancing efficiency and accuracy"
    },
    {
        "name": "MixNet-L",
        "description": "Large MixNet achieving high accuracy with mixed kernels"
    },
    {
        "name": "MNASNet-0.5",
        "description": "Lightweight MNASNet discovered by platform-aware NAS"
    },
    {
        "name": "MNASNet-0.75",
        "description": "Medium MNASNet optimized for mobile latency"
    },
    {
        "name": "MNASNet-1.0",
        "description": "Standard MNASNet balancing accuracy and latency"
    },
    {
        "name": "MNASNet-1.3",
        "description": "Larger MNASNet for improved mobile performance"
    },
    {
        "name": "FBNet-A",
        "description": "Hardware-aware FBNet variant A for specific mobile devices"
    },
    {
        "name": "FBNet-B",
        "description": "FBNet variant B optimized for mobile inference speed"
    },
    {
        "name": "FBNet-C",
        "description": "FBNet variant C balancing accuracy and latency"
    },
    {
        "name": "ProxylessNAS-Mobile",
        "description": "Mobile-optimized architecture from ProxylessNAS search"
    },
    {
        "name": "ProxylessNAS-GPU",
        "description": "GPU-optimized architecture from ProxylessNAS"
    },
    {
        "name": "TinyNet-A",
        "description": "Ultra-efficient TinyNet variant A for extreme constraints"
    },
    {
        "name": "TinyNet-B",
        "description": "TinyNet variant B balancing size and performance"
    },
    {
        "name": "FastNet-Small",
        "description": "FastNet optimized for speed on mobile processors"
    },
    {
        "name": "FastNet-Medium",
        "description": "Medium FastNet for balanced mobile performance"
    },
    {
        "name": "FastNet-Large",
        "description": "Large FastNet for high-accuracy mobile applications"
    },
    {
        "name": "LCNet-0.35",
        "description": "Lightweight ConvNet with 0.35 scale for mobile devices"
    },
    {
        "name": "LCNet-0.50",
        "description": "LCNet with 0.50 scale balancing efficiency and accuracy"
    },
    {
        "name": "LCNet-0.75",
        "description": "LCNet with 0.75 scale for improved mobile performance"
    },
    {
        "name": "LCNet-1.0",
        "description": "Full-scale LCNet for mobile and edge deployment"
    },
    {
        "name": "MobileViT-XS",
        "description": "Extra-small Mobile Vision Transformer for mobile devices"
    },
    {
        "name": "MobileViT-S",
        "description": "Small MobileViT combining CNN and Transformer benefits"
    },
    {
        "name": "MobileViT-M",
        "description": "Medium MobileViT for balanced mobile vision tasks"
    },
    {
        "name": "MobileViT-L",
        "description": "Large MobileViT for high-accuracy mobile applications"
    },
    {
        "name": "EdgeNeXt-XXSmall",
        "description": "Extra-extra-small EdgeNeXt for extreme edge deployment"
    },
    {
        "name": "EdgeNeXt-XSmall",
        "description": "Extra-small EdgeNeXt optimized for edge devices"
    },
    {
        "name": "EdgeNeXt-Small",
        "description": "Small EdgeNeXt balancing efficiency and accuracy"
    },
    {
        "name": "EdgeNeXt-Medium",
        "description": "Medium EdgeNeXt for edge computing applications"
    }
]