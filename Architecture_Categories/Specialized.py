"""
Module for Специализированные архитектуры (Specialized Architectures).
"""
from dataclasses import dataclass
from typing import Optional

# Specialized Architectures data
SPECIALIZED_ARCHITECTURES = [
    {
        "name": "Специализированные архитектуры",
        "description": "Архитектуры, разработанные для конкретных задач или областей применения."
    }
]

@dataclass
class Specialized:
    """
    Represents a Specialized Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Specialized Neural Network Architectures
Domain-specific and task-specific architectures
"""

SPECIALIZED_ARCHITECTURES = [
    {
        "name": "U-Net",
        "description": "Convolutional network for biomedical image segmentation"
    },
    {
        "name": "U-Net-ResNet",
        "description": "U-Net with ResNet encoder backbone"
    },
    {
        "name": "U-Net-EfficientNet",
        "description": "U-Net with EfficientNet encoder"
    },
    {
        "name": "Attention-U-Net",
        "description": "U-Net with attention gates for segmentation"
    },
    {
        "name": "U-Net++",
        "description": "Nested U-Net architecture for segmentation"
    },
    {
        "name": "U-Net-3+",
        "description": "Full-scale skip connections in U-Net"
    },
    {
        "name": "TransU-Net",
        "description": "U-Net with Transformer encoder"
    },
    {
        "name": "Swin-U-Net",
        "description": "U-Net with Swin Transformer backbone"
    },
    {
        "name": "DeepLab-v3",
        "description": "DeepLab semantic segmentation with atrous convolution"
    },
    {
        "name": "DeepLab-v3+",
        "description": "Improved DeepLab with encoder-decoder"
    },
    {
        "name": "DeepLab-Cityscapes",
        "description": "DeepLab optimized for Cityscapes dataset"
    },
    {
        "name": "PSPNet",
        "description": "Pyramid Scene Parsing Network for segmentation"
    },
    {
        "name": "FCN-8s",
        "description": "Fully Convolutional Network with 8x upsampling"
    },
    {
        "name": "FCN-16s",
        "description": "FCN with 16x upsampling"
    },
    {
        "name": "FCN-32s",
        "description": "FCN with 32x upsampling"
    },
    {
        "name": "Mask-RCNN",
        "description": "Mask Region CNN for instance segmentation"
    },
    {
        "name": "Mask-RCNN-ResNet50",
        "description": "Mask R-CNN with ResNet-50 backbone"
    },
    {
        "name": "Mask-RCNN-ResNet101",
        "description": "Mask R-CNN with ResNet-101 backbone"
    },
    {
        "name": "YOLO-v3",
        "description": "You Only Look Once v3 for object detection"
    },
    {
        "name": "YOLO-v4",
        "description": "YOLO v4 with improved detection"
    },
    {
        "name": "YOLO-v5-Small",
        "description": "YOLO v5 small variant"
    },
    {
        "name": "YOLO-v5-Medium",
        "description": "YOLO v5 medium variant"
    },
    {
        "name": "YOLO-v5-Large",
        "description": "YOLO v5 large variant"
    },
    {
        "name": "YOLO-v5-XL",
        "description": "YOLO v5 extra-large variant"
    },
    {
        "name": "YOLO-v7",
        "description": "YOLO v7 with extended efficient layer aggregation"
    },
    {
        "name": "YOLO-v8-Nano",
        "description": "YOLO v8 nano variant"
    },
    {
        "name": "YOLO-v8-Small",
        "description": "YOLO v8 small variant"
    },
    {
        "name": "YOLO-v8-Medium",
        "description": "YOLO v8 medium variant"
    },
    {
        "name": "YOLO-v8-Large",
        "description": "YOLO v8 large variant"
    },
    {
        "name": "YOLO-v8-XL",
        "description": "YOLO v8 extra-large variant"
    },
    {
        "name": "YOLOX-Small",
        "description": "YOLOX small variant"
    },
    {
        "name": "YOLOX-Medium",
        "description": "YOLOX medium variant"
    },
    {
        "name": "YOLOX-Large",
        "description": "YOLOX large variant"
    },
    {
        "name": "YOLOX-XL",
        "description": "YOLOX extra-large variant"
    },
    {
        "name": "Faster-RCNN",
        "description": "Faster R-CNN with region proposal network"
    },
    {
        "name": "Faster-RCNN-ResNet50",
        "description": "Faster R-CNN with ResNet-50"
    },
    {
        "name": "Faster-RCNN-ResNet101",
        "description": "Faster R-CNN with ResNet-101"
    },
    {
        "name": "RetinaNet",
        "description": "Focal loss for dense object detection"
    },
    {
        "name": "RetinaNet-ResNet50",
        "description": "RetinaNet with ResNet-50 backbone"
    },
    {
        "name": "FCOS",
        "description": "Fully Convolutional One-Stage detector"
    },
    {
        "name": "CenterNet",
        "description": "Objects as points for detection"
    },
    {
        "name": "CornerNet",
        "description": "Detecting objects as paired keypoints"
    },
    {
        "name": "DETR",
        "description": "Detection Transformer for end-to-end detection"
    },
    {
        "name": "DETR-ResNet50",
        "description": "DETR with ResNet-50 backbone"
    },
    {
        "name": "Deformable-DETR",
        "description": "DETR with deformable attention"
    },
    {
        "name": "DINO-DETR",
        "description": "DETR with improved de-noising training"
    },
    {
        "name": "Sparse-RCNN",
        "description": "Sparse R-CNN for end-to-end detection"
    },
    {
        "name": "GFL",
        "description": "Generalized Focal Loss for detection"
    },
    {
        "name": "ATSS",
        "description": "Automatic Target Sampling Strategy"
    },
    {
        "name": "SRNet",
        "description": "Super-Resolution Network"
    },
    {
        "name": "ESPCN",
        "description": "Efficient Sub-Pixel CNN for SR"
    },
    {
        "name": "FSRCNN",
        "description": "Fast Super-Resolution CNN"
    },
    {
        "name": "VDSR",
        "description": "Very Deep Super-Resolution Network"
    },
    {
        "name": "EDSR",
        "description": "Enhanced Deep Residual Networks for SR"
    },
    {
        "name": "SRGAN",
        "description": "Super-Resolution GAN"
    },
    {
        "name": "ESRGAN",
        "description": "Enhanced SRGAN for realistic images"
    },
    {
        "name": "Real-ESRGAN",
        "description": "Practical SR for real-world images"
    },
    {
        "name": "SwinIR",
        "description": "Swin Transformer for Image Restoration"
    },
    {
        "name": "HAT",
        "description": "Hybrid Attention Transformer for SR"
    },
    {
        "name": "DAT",
        "description": "Dual Aggregation Transformer for SR"
    },
    {
        "name": "NAFNet",
        "description": "Nonlinear Activation Free Network for restoration"
    },
    {
        "name": "Restormer",
        "description": "Efficient Transformer for image restoration"
    },
    {
        "name": "MPRNet",
        "description": "Multi-Stage Progressive Restoration Network"
    },
    {
        "name": "Uformer",
        "description": "U-Net shaped Transformer for restoration"
    },
    {
        "name": "IRNet",
        "description": "Infrared Small Target Detection Network"
    },
    {
        "name": "SAR-Net",
        "description": "Synthetic Aperture Radar processing network"
    },
    {
        "name": "LiDAR-Net",
        "description": "LiDAR point cloud processing network"
    },
    {
        "name": "Medical-Net",
        "description": "3D medical image analysis network"
    },
    {
        "name": "Pathology-Net",
        "description": "Computational pathology analysis network"
    },
    {
        "name": "Genomics-Net",
        "description": "Genomic sequence analysis network"
    },
    {
        "name": "Protein-Net",
        "description": "Protein structure prediction network"
    },
    {
        "name": "Drug-Discovery-Net",
        "description": "Molecular property prediction network"
    }
]