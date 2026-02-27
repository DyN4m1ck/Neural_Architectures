"""
Module for Convolutional Architectures (CNN).
"""
from dataclasses import dataclass
from typing import Optional


# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Convolutional Architectures (CNN)",
        "description": "Neural network architectures primarily based on convolutional layers, commonly used for image processing and computer vision tasks."
    }
]


@dataclass
class CNN:
    """
    Represents a Convolutional Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Convolutional Neural Networks (CNN) Architectures
"""

CNN_ARCHITECTURES = [
    {
        "name": "LeNet-5",
        "description": "Pioneering CNN architecture for handwritten digit recognition, introduced by Yann LeCun in 1998"
    },
    {
        "name": "AlexNet",
        "description": "Breakthrough deep CNN that won ImageNet 2012, featuring ReLU activations and dropout"
    },
    {
        "name": "VGG-11",
        "description": "Simple CNN architecture with 11 layers using small 3x3 convolution filters"
    },
    {
        "name": "VGG-13",
        "description": "13-layer VGG variant with increased depth for better feature extraction"
    },
    {
        "name": "VGG-16",
        "description": "Popular 16-layer VGG architecture widely used for transfer learning"
    },
    {
        "name": "VGG-19",
        "description": "19-layer VGG variant providing deeper hierarchical feature representations"
    },
    {
        "name": "GoogLeNet/Inception-v1",
        "description": "22-layer CNN with inception modules for efficient computation and accuracy"
    },
    {
        "name": "Inception-v2",
        "description": "Improved inception architecture with batch normalization and factorized convolutions"
    },
    {
        "name": "Inception-v3",
        "description": "Further optimized inception with label smoothing and advanced factorization"
    },
    {
        "name": "Inception-v4",
        "description": "Advanced inception architecture with improved training stability"
    },
    {
        "name": "Inception-ResNet-v1",
        "description": "Hybrid architecture combining inception modules with residual connections"
    },
    {
        "name": "Inception-ResNet-v2",
        "description": "Deeper hybrid model with enhanced inception-residual blocks"
    },
    {
        "name": "ResNet-18",
        "description": "18-layer residual network with skip connections for easier training"
    },
    {
        "name": "ResNet-34",
        "description": "34-layer residual network balancing depth and computational efficiency"
    },
    {
        "name": "ResNet-50",
        "description": "50-layer residual network with bottleneck architecture for deep learning"
    },
    {
        "name": "ResNet-101",
        "description": "101-layer deep residual network for high-accuracy image recognition"
    },
    {
        "name": "ResNet-152",
        "description": "152-layer extremely deep residual network achieving state-of-the-art results"
    },
    {
        "name": "ResNeXt-50",
        "description": "50-layer network using cardinality (split-transform-merge) strategy"
    },
    {
        "name": "ResNeXt-101",
        "description": "101-layer ResNeXt with grouped convolutions for improved performance"
    },
    {
        "name": "DenseNet-121",
        "description": "121-layer densely connected network with feature reuse across layers"
    },
    {
        "name": "DenseNet-169",
        "description": "169-layer DenseNet with enhanced gradient flow and parameter efficiency"
    },
    {
        "name": "DenseNet-201",
        "description": "201-layer DenseNet providing maximum feature reuse and connectivity"
    },
    {
        "name": "SE-ResNet-50",
        "description": "ResNet-50 with Squeeze-and-Excitation blocks for channel attention"
    },
    {
        "name": "SE-ResNet-101",
        "description": "ResNet-101 enhanced with channel-wise attention mechanisms"
    },
    {
        "name": "SE-ResNet-152",
        "description": "ResNet-152 with squeeze-and-excitation for improved feature calibration"
    },
    {
        "name": "Xception",
        "description": "Extreme inception architecture using depthwise separable convolutions"
    },
    {
        "name": "MobileNet-v1",
        "description": "Lightweight CNN using depthwise separable convolutions for mobile devices"
    },
    {
        "name": "MobileNet-v2",
        "description": "Improved MobileNet with inverted residuals and linear bottlenecks"
    },
    {
        "name": "MobileNet-v3",
        "description": "Neural architecture search optimized MobileNet with attention mechanisms"
    },
    {
        "name": "ShuffleNet-v1",
        "description": "Efficient CNN with channel shuffling for mobile applications"
    },
    {
        "name": "ShuffleNet-v2",
        "description": "Improved ShuffleNet with better speed-accuracy tradeoff"
    },
    {
        "name": "SqueezeNet",
        "description": "Compact CNN achieving AlexNet accuracy with 50x fewer parameters"
    },
    {
        "name": "EfficientNet-B0",
        "description": "Baseline efficient CNN with compound scaling of depth, width, and resolution"
    },
    {
        "name": "EfficientNet-B7",
        "description": "Largest EfficientNet variant with state-of-the-art accuracy and efficiency"
    },
    {
        "name": "NASNet-A",
        "description": "Neural Architecture Search discovered CNN with optimal cell structure"
    },
    {
        "name": "NASNet-Large",
        "description": "Large-scale NAS-discovered architecture for high-performance tasks"
    },
    {
        "name": "Darknet-53",
        "description": "53-layer backbone network for YOLO object detection"
    },
    {
        "name": "CSPDarknet53",
        "description": "Cross Stage Partial Darknet for improved gradient flow in YOLOv4"
    },
    {
        "name": "ConvNeXt-Tiny",
        "description": "Modernized CNN architecture matching Transformer performance"
    },
    {
        "name": "ConvNeXt-Base",
        "description": "Base ConvNeXt model with pure CNN design and Transformer-like accuracy"
    },
    {
        "name": "RegNetX-400MF",
        "description": "400MF parameter network from design space exploration"
    },
    {
        "name": "RegNetY-800MF",
        "description": "800MF RegNet with optimized design principles"
    },
    {
        "name": "GhostNet",
        "description": "Efficient network generating ghost feature maps for mobile deployment"
    },
    {
        "name": "MixNet-S",
        "description": "Small MixNet using mixed depthwise convolutions for efficiency"
    },
    {
        "name": "MixNet-M",
        "description": "Medium MixNet balancing accuracy and computational cost"
    },
    {
        "name": "MixNet-L",
        "description": "Large MixNet achieving high accuracy with mixed convolution kernels"
    }
]