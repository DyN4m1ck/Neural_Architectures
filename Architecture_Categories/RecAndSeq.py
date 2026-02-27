"""
Module for Recurant&Sequental Architectures
"""
from dataclasses import dataclass
from typing import Optional

# Convolutional Architectures data
CONVOLUTIONAL_ARCHITECTURES = [
    {
        "name": "Recurant&Sequental Architectures",
        "description": "These are architectures that perceive the world not as a set of frozen frames, but as a continuous stream, where the past determines the understanding of the present"
    }
]

@dataclass
class RecAndSeq:
    """
    Represents a NAS Architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Recurrent and Sequential Neural Network Architectures
Networks for sequence modeling and time series
"""

REC_SEQ_ARCHITECTURES = [
    {
        "name": "Vanilla-RNN",
        "description": "Simple recurrent neural network with hidden state"
    },
    {
        "name": "Elman-RNN",
        "description": "Simple RNN with context units"
    },
    {
        "name": "Jordan-RNN",
        "description": "RNN with output feedback to input"
    },
    {
        "name": "LSTM",
        "description": "Long Short-Term Memory with gates for long-range dependencies"
    },
    {
        "name": "LSTM-Forward",
        "description": "Unidirectional LSTM processing sequences forward"
    },
    {
        "name": "LSTM-Backward",
        "description": "Unidirectional LSTM processing sequences backward"
    },
    {
        "name": "BiLSTM",
        "description": "Bidirectional LSTM with forward and backward passes"
    },
    {
        "name": "Stacked-LSTM",
        "description": "Multiple LSTM layers for hierarchical representation"
    },
    {
        "name": "Deep-LSTM",
        "description": "Deep LSTM with multiple hidden layers"
    },
    {
        "name": "Peephole-LSTM",
        "description": "LSTM with peephole connections from cell state"
    },
    {
        "name": "GRU",
        "description": "Gated Recurrent Unit with simplified gates"
    },
    {
        "name": "BiGRU",
        "description": "Bidirectional GRU for sequence modeling"
    },
    {
        "name": "Stacked-GRU",
        "description": "Multiple GRU layers for deep representation"
    },
    {
        "name": "Deep-GRU",
        "description": "Deep GRU architecture with multiple layers"
    },
    {
        "name": "MGU",
        "description": "Minimal Gated Unit with simplified gating"
    },
    {
        "name": "UGRNN",
        "description": "Unidirectional Gated Recurrent Neural Network"
    },
    {
        "name": "LSTM-Attention",
        "description": "LSTM with attention mechanism for focus"
    },
    {
        "name": "BiLSTM-Attention",
        "description": "Bidirectional LSTM with attention"
    },
    {
        "name": "GRU-Attention",
        "description": "GRU with attention for sequence tasks"
    },
    {
        "name": "Seq2Seq",
        "description": "Sequence-to-Sequence model with encoder-decoder"
    },
    {
        "name": "Seq2Seq-LSTM",
        "description": "Seq2Seq using LSTM encoder and decoder"
    },
    {
        "name": "Seq2Seq-GRU",
        "description": "Seq2Seq using GRU encoder and decoder"
    },
    {
        "name": "Seq2Seq-Attention",
        "description": "Seq2Seq with attention mechanism"
    },
    {
        "name": "Bahdanau-Attention",
        "description": "Additive attention for neural machine translation"
    },
    {
        "name": "Luong-Attention",
        "description": "Multiplicative attention variants (dot, general, concat)"
    },
    {
        "name": "Global-Attention",
        "description": "Global attention considering all source positions"
    },
    {
        "name": "Local-Attention",
        "description": "Local attention focusing on subset of positions"
    },
    {
        "name": "Self-Attention",
        "description": "Attention mechanism relating different positions"
    },
    {
        "name": "Multi-Head-Attention",
        "description": "Multiple attention heads for diverse representations"
    },
    {
        "name": "Transformer-Encoder",
        "description": "Transformer encoder stack for sequence encoding"
    },
    {
        "name": "Transformer-Decoder",
        "description": "Transformer decoder stack for sequence generation"
    },
    {
        "name": "QRNN",
        "description": "Quasi-Recurrent Neural Network for parallelism"
    },
    {
        "name": "SRU",
        "description": "Simple Recurrent Unit for faster training"
    },
    {
        "name": "SRU++",
        "description": "Improved SRU with layer normalization"
    },
    {
        "name": "IndRNN",
        "description": "Independently Recurrent Neural Network"
    },
    {
        "name": "Dilated-RNN",
        "description": "RNN with dilated connections for long dependencies"
    },
    {
        "name": "Clockwork-RNN",
        "description": "RNN with partitioned hidden state at different speeds"
    },
    {
        "name": "Phased-LSTM",
        "description": "LSTM with time gates for irregular sequences"
    },
    {
        "name": "NADE",
        "description": "Neural Autoregressive Distribution Estimator"
    },
    {
        "name": "RNN-NADE",
        "description": "RNN-based NADE for sequence modeling"
    },
    {
        "name": "PixelRNN",
        "description": "Pixel-level RNN for image generation"
    },
    {
        "name": "PixelCNN",
        "description": "Pixel-level CNN for autoregressive generation"
    },
    {
        "name": "Row-LSTM",
        "description": "Row-wise LSTM for 2D sequence processing"
    },
    {
        "name": "Diagonal-BiLSTM",
        "description": "Diagonal bidirectional LSTM for images"
    },
    {
        "name": "ConvLSTM",
        "description": "Convolutional LSTM for spatiotemporal sequences"
    },
    {
        "name": "TrajGRU",
        "description": "Trajectory GRU for precipitation nowcasting"
    },
    {
        "name": "MDCN",
        "description": "Multi-Depth Convolutional Network for sequences"
    },
    {
        "name": "Temporal-ConvNet",
        "description": "Temporal Convolutional Network for sequences"
    },
    {
        "name": "WaveNet",
        "description": "Dilated causal CNN for audio generation"
    },
    {
        "name": "ByteNet",
        "description": "Fast density estimator with dilated convolutions"
    }
]