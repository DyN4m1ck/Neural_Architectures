"""
Module for Мультимодальные архитектуры (Multimodal Architectures).
"""
from dataclasses import dataclass
from typing import Optional


# Multimodal Architectures data
MULTIMODAL_ARCHITECTURES = [
    {
        "name": "Мультимодальные архитектуры",
        "description": "Архитектуры, способные обрабатывать несколько различных типов данных одновременно."
    }
]

@dataclass
class Multimodal:
    """
    Represents a Multimodal Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Multimodal Neural Network Architectures
Networks processing multiple data modalities
"""

"""
Multimodal Neural Network Architectures (Extended)
Additional multimodal and cross-modal architectures
"""

MULTIMODAL_EXTENDED_ARCHITECTURES = [
    {
        "name": "CLIP-Text-Encoder",
        "description": "CLIP text encoder component"
    },
    {
        "name": "CLIP-Image-Encoder",
        "description": "CLIP image encoder component"
    },
    {
        "name": "OpenCLIP",
        "description": "Open-source CLIP implementation"
    },
    {
        "name": "OpenCLIP-ViT-H",
        "description": "OpenCLIP with ViT-Huge"
    },
    {
        "name": "OpenCLIP-ViT-G",
        "description": "OpenCLIP with ViT-Giant"
    },
    {
        "name": "SigLIP",
        "description": "Sigmoid Loss for Language-Image Pre-training"
    },
    {
        "name": "LiT-Base",
        "description": "Locked-image text tuning Base model"
    },
    {
        "name": "LiT-Large",
        "description": "Locked-image text tuning Large model"
    },
    {
        "name": "ALIGN-Base",
        "description": "ALIGN Base model"
    },
    {
        "name": "ALIGN-Large",
        "description": "ALIGN Large model"
    },
    {
        "name": "BasicVSR",
        "description": "Basic Video Super-Resolution"
    },
    {
        "name": "BasicVSR++",
        "description": "Improved Basic Video Super-Resolution"
    },
    {
        "name": "EDVR",
        "description": "Enhanced Deep Video Restoration"
    },
    {
        "name": "TTVSR",
        "description": "Temporal Transformer Video Super-Resolution"
    },
    {
        "name": "VSR-Transformer",
        "description": "Transformer for Video Super-Resolution"
    },
    {
        "name": "Video-CLIP",
        "description": "CLIP for video understanding"
    },
    {
        "name": "CLIP4Clip",
        "description": "CLIP for video retrieval"
    },
    {
        "name": "X-CLIP",
        "description": "Cross-modal CLIP for video"
    },
    {
        "name": "ViViT",
        "description": "Video Vision Transformer"
    },
    {
        "name": "ViViT-Factorised",
        "description": "ViViT with factorised encoder"
    },
    {
        "name": "ViViT-Decoder",
        "description": "ViViT with decoder"
    },
    {
        "name": "TimeSformer",
        "description": "Space-Time Vision Transformer"
    },
    {
        "name": "VideoMAE",
        "description": "Masked Autoencoder for Video"
    },
    {
        "name": "VideoMAE-v2",
        "description": "Improved VideoMAE"
    },
    {
        "name": "SlowFast",
        "description": "SlowFast networks for video recognition"
    },
    {
        "name": "I3D",
        "description": "Inflated 3D ConvNet"
    },
    {
        "name": "R(2+1)D",
        "description": "Residual 2+1D ConvNet"
    },
    {
        "name": "S3D",
        "description": "Separated 3D ConvNet"
    },
    {
        "name": "CSN",
        "description": "Channel-Separated ConvNet"
    },
    {
        "name": "X3D",
        "description": "Expanded 3D ConvNet"
    },
    {
        "name": "MViT",
        "description": "Multiscale Vision Transformer"
    },
    {
        "name": "MViT-v2",
        "description": "Improved Multiscale Vision Transformer"
    },
    {
        "name": "UniFormer",
        "description": "Unified Transformer for video"
    },
    {
        "name": "Video-Swin",
        "description": "Swin Transformer for video"
    },
    {
        "name": "Video-Swin-Tiny",
        "description": "Tiny Video Swin Transformer"
    },
    {
        "name": "Video-Swin-Small",
        "description": "Small Video Swin Transformer"
    },
    {
        "name": "Video-Swin-Base",
        "description": "Base Video Swin Transformer"
    },
    {
        "name": "Video-MAE-Pretrain",
        "description": "Video MAE pre-trained model"
    },
    {
        "name": "Audio-Visual",
        "description": "Audio-Visual learning network"
    },
    {
        "name": "AV-HuBERT",
        "description": "Audio-Visual HuBERT"
    },
    {
        "name": "AV-Speech",
        "description": "Audio-Visual speech recognition"
    },
    {
        "name": "Lip-Reading",
        "description": "Lip reading network"
    },
    {
        "name": "TalkNet",
        "description": "TalkNet for audio-visual"
    },
    {
        "name": "SyncNet",
        "description": "Synchronization network"
    },
    {
        "name": "Wav2Lip",
        "description": "Accurate lip-sync network"
    },
    {
        "name": "MakeItTalk",
        "description": "Audio-driven talking head"
    },
    {
        "name": "ATVG",
        "description": "Audio-Visual Talking Face"
    },
    {
        "name": "Speech2Face",
        "description": "Speech to face reconstruction"
    },
    {
        "name": "Voice2Face",
        "description": "Voice to face generation"
    },
    {
        "name": "Multimodal-Fusion",
        "description": "General multimodal fusion network"
    },
    {
        "name": "Early-Fusion",
        "description": "Early fusion multimodal network"
    },
    {
        "name": "Late-Fusion",
        "description": "Late fusion multimodal network"
    },
    {
        "name": "Hybrid-Fusion",
        "description": "Hybrid fusion multimodal network"
    },
    {
        "name": "Cross-Modal-Attention",
        "description": "Cross-modal attention network"
    },
    {
        "name": "Multimodal-Transformer",
        "description": "Transformer for multimodal data"
    },
    {
        "name": "Multimodal-BERT",
        "description": "BERT for multimodal understanding"
    },
    {
        "name": "Oscar-Base",
        "description": "Oscar Base model"
    },
    {
        "name": "Oscar-Large",
        "description": "Oscar Large model"
    },
    {
        "name": "VinVL-Base",
        "description": "VinVL Base model"
    },
    {
        "name": "VinVL-Large",
        "description": "VinVL Large model"
    },
    {
        "name": "UniVL",
        "description": "Unified Video-Language model"
    },
    {
        "name": "Hero-Base",
        "description": "Hero Base model"
    },
    {
        "name": "Hero-Large",
        "description": "Hero Large model"
    },
    {
        "name": "VIOLET-Base",
        "description": "VIOLET Base model"
    },
    {
        "name": "VIOLET-Large",
        "description": "VIOLET Large model"
    },
    {
        "name": "All-in-One",
        "description": "All-in-One multimodal model"
    },
    {
        "name": "UniPT",
        "description": "Universal Pre-trained Transformer"
    },
    {
        "name": "OFA-Base",
        "description": "OFA Base model"
    },
    {
        "name": "OFA-Large",
        "description": "OFA Large model"
    }
]