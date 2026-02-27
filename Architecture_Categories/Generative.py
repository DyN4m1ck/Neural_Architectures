"""
Module for Generative Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Generative Architectures",
        "description": "A type of machine learning algorithms and neural networks designed to create new, original content (text, images, sound, video, code) that mimics the structure and style of training data"
    }
]

@dataclass
class Generative:
    """
    Represents a Generative Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Generative Model Architectures
Networks for generating new data samples
"""

GENERATIVE_ARCHITECTURES = [
    {
        "name": "Vanilla-GAN",
        "description": "Original Generative Adversarial Network with generator and discriminator"
    },
    {
        "name": "DCGAN",
        "description": "Deep Convolutional GAN with architectural constraints for stability"
    },
    {
        "name": "WGAN",
        "description": "Wasserstein GAN using Earth Mover distance for better training"
    },
    {
        "name": "WGAN-GP",
        "description": "WGAN with gradient penalty for improved stability"
    },
    {
        "name": "WGAN-LP",
        "description": "WGAN with Lipschitz penalty for stable training"
    },
    {
        "name": "LSGAN",
        "description": "Least Squares GAN using least squares loss function"
    },
    {
        "name": "HingeGAN",
        "description": "GAN trained with hinge loss for discriminator"
    },
    {
        "name": "Relativistic-GAN",
        "description": "GAN with relativistic discriminator comparing real and fake"
    },
    {
        "name": "SAGAN",
        "description": "Self-Attention GAN with attention mechanisms for global consistency"
    },
    {
        "name": "BigGAN",
        "description": "Large-scale GAN with high-resolution image generation"
    },
    {
        "name": "StyleGAN",
        "description": "Style-based generator for controllable high-quality synthesis"
    },
    {
        "name": "StyleGAN2",
        "description": "Improved StyleGAN with better image quality and training"
    },
    {
        "name": "StyleGAN3",
        "description": "StyleGAN with alias-free generation for better quality"
    },
    {
        "name": "StyleGAN-XL",
        "description": "Extended StyleGAN for higher resolution and diversity"
    },
    {
        "name": "Progressive-GAN",
        "description": "Progressively growing GAN for high-resolution synthesis"
    },
    {
        "name": "CycleGAN",
        "description": "Unpaired image-to-image translation with cycle consistency"
    },
    {
        "name": "Pix2Pix",
        "description": "Paired image-to-image translation with conditional GAN"
    },
    {
        "name": "Pix2PixHD",
        "description": "High-definition Pix2Pix for semantic image synthesis"
    },
    {
        "name": "SPADE",
        "description": "Spatially-Adaptive Denormalization for semantic synthesis"
    },
    {
        "name": "StarGAN",
        "description": "Unified GAN for multi-domain image-to-image translation"
    },
    {
        "name": "StarGAN-v2",
        "description": "Improved StarGAN with diverse image synthesis"
    },
    {
        "name": "MUNIT",
        "description": "Multimodal Unsupervised Image-to-Image Translation"
    },
    {
        "name": "DRIT",
        "description": "Diverse Image-to-Image Translation via disentangled representations"
    },
    {
        "name": "UNIT",
        "description": "Unsupervised Image-to-Image Translation with shared latent space"
    },
    {
        "name": "FUNIT",
        "description": "Few-shot Unsupervised Image-to-Image Translation"
    },
    {
        "name": "VAE",
        "description": "Variational Autoencoder for probabilistic latent representation"
    },
    {
        "name": "Beta-VAE",
        "description": "VAE with disentangled latent representation learning"
    },
    {
        "name": "CVAE",
        "description": "Conditional VAE for controlled generation"
    },
    {
        "name": "AAE",
        "description": "Adversarial Autoencoder combining VAE and GAN"
    },
    {
        "name": "WAE",
        "description": "Wasserstein Autoencoder with optimal transport"
    },
    {
        "name": "InfoVAE",
        "description": "VAE maximizing mutual information in latent space"
    },
    {
        "name": "VQ-VAE",
        "description": "Vector Quantized VAE with discrete latent representation"
    },
    {
        "name": "VQ-VAE-2",
        "description": "Hierarchical VQ-VAE for high-fidelity generation"
    },
    {
        "name": "NVAE",
        "description": "Normalizing Flow VAE with hierarchical latent variables"
    },
    {
        "name": "FlowVAE",
        "description": "VAE with normalizing flow for flexible posterior"
    },
    {
        "name": "Flow",
        "description": "Normalizing Flow for exact likelihood modeling"
    },
    {
        "name": "RealNVP",
        "description": "Real Non-Volume Preserving flow for density estimation"
    },
    {
        "name": "Glow",
        "description": "Generative flow with invertible 1x1 convolutions"
    },
    {
        "name": "FFJORD",
        "description": "Free-form continuous normalizing flow"
    },
    {
        "name": "PixelCNN",
        "description": "Autoregressive pixel-level image generation model"
    },
    {
        "name": "PixelCNN++",
        "description": "Improved PixelCNN with better distribution modeling"
    },
    {
        "name": "PixelRNN",
        "description": "Recurrent neural network for pixel-level generation"
    },
    {
        "name": "WaveNet",
        "description": "Autoregressive model for raw audio generation"
    },
    {
        "name": "Parallel-WaveNet",
        "description": "Fast WaveNet using parallel generation"
    },
    {
        "name": "WaveGlow",
        "description": "Flow-based model for high-quality audio synthesis"
    },
    {
        "name": "EBM",
        "description": "Energy-Based Model for implicit density estimation"
    },
    {
        "name": "JEM",
        "description": "Joint Energy-based Model for classification and generation"
    },
    {
        "name": "Diffusion-Model",
        "description": "Denoising diffusion probabilistic model for generation"
    },
    {
        "name": "DDPM",
        "description": "Denoising Diffusion Probabilistic Model"
    },
    {
        "name": "DDIM",
        "description": "Denoising Diffusion Implicit Model for faster sampling"
    },
    {
        "name": "Score-SDE",
        "description": "Score-based generative model with stochastic differential equations"
    },
    {
        "name": "NCSN",
        "description": "Noise Conditional Score Network for score matching"
    },
    {
        "name": "NCSNv2",
        "description": "Improved NCSN with better score estimation"
    },
    {
        "name": "ADM",
        "description": "Improved Denoising Diffusion Probabilistic Model"
    },
    {
        "name": "Guided-Diffusion",
        "description": "Diffusion model with classifier guidance"
    },
    {
        "name": "GLIDE",
        "description": "Text-guided diffusion model for image generation"
    },
    {
        "name": "DALL-E",
        "description": "Autoregressive transformer for text-to-image generation"
    },
    {
        "name": "DALL-E-2",
        "description": "Improved DALL-E with diffusion model for higher quality"
    },
    {
        "name": "Stable-Diffusion",
        "description": "Latent diffusion model for efficient text-to-image synthesis"
    },
    {
        "name": "Midjourney",
        "description": "Text-to-image diffusion model with artistic capabilities"
    },
    {
        "name": "Imagen",
        "description": "Text-to-image diffusion with cascaded architecture"
    }
]