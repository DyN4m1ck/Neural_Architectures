"""
Module for Graph Neural Networks (GNN).
"""
from dataclasses import dataclass
from typing import Optional

# Graph Neural Networks data
GRAPH_NEURAL_NETWORKS = [
    {
        "name": "Graph Neural Networks (GNN)",
        "description": "Neural networks specifically designed to operate on graph-structured data, processing relationships between entities."
    }
]

@dataclass
class GNN:
    """
    Represents a Graph Neural Network category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None

"""
Graph Neural Network Architectures
Networks operating on graph-structured data
"""

GNN_ARCHITECTURES = [
    {
        "name": "GCN",
        "description": "Graph Convolutional Network using spectral graph convolutions"
    },
    {
        "name": "ChebNet",
        "description": "Chebyshev spectral CNN for efficient graph convolutions"
    },
    {
        "name": "CayleyNet",
        "description": "Spectral GNN using Cayley polynomials for graph filtering"
    },
    {
        "name": "GAT",
        "description": "Graph Attention Network using attention for neighbor aggregation"
    },
    {
        "name": "GATv2",
        "description": "Improved GAT with dynamic attention mechanism"
    },
    {
        "name": "Multi-Head-GAT",
        "description": "GAT with multiple attention heads for diverse features"
    },
    {
        "name": "GraphSAGE",
        "description": "Inductive GNN sampling and aggregating neighbor features"
    },
    {
        "name": "Mean-GraphSAGE",
        "description": "GraphSAGE using mean aggregator for neighbors"
    },
    {
        "name": "LSTM-GraphSAGE",
        "description": "GraphSAGE with LSTM aggregator for sequential neighbors"
    },
    {
        "name": "Pooling-GraphSAGE",
        "description": "GraphSAGE using pooling aggregator for neighbor features"
    },
    {
        "name": "GIN",
        "description": "Graph Isomorphism Network with injective aggregation"
    },
    {
        "name": "GIN-0",
        "description": "GIN variant with epsilon=0 for maximum expressiveness"
    },
    {
        "name": "GraphCNN",
        "description": "Graph CNN with hierarchical pooling for graph classification"
    },
    {
        "name": "DGCNN",
        "description": "Deep Graph CNN with SortPooling for graph classification"
    },
    {
        "name": "DiffPool",
        "description": "Differentiable pooling for hierarchical GNN"
    },
    {
        "name": "MinCutPool",
        "description": "GNN with min-cut pooling for graph coarsening"
    },
    {
        "name": "SAGPool",
        "description": "Self-attention graph pooling for hierarchical representation"
    },
    {
        "name": "EdgeConv",
        "description": "Dynamic graph CNN operating on edge features"
    },
    {
        "name": "PointNet",
        "description": "Deep learning on point sets for 3D classification"
    },
    {
        "name": "PointNet++",
        "description": "Hierarchical PointNet for local feature learning"
    },
    {
        "name": "DGCNN-Point",
        "description": "Dynamic Graph CNN for point cloud processing"
    },
    {
        "name": "PCT",
        "description": "Point Cloud Transformer using self-attention on points"
    },
    {
        "name": "Graph-Transformer",
        "description": "Transformer architecture adapted for graph data"
    },
    {
        "name": "Graphormer",
        "description": "Transformer with centrality encoding for graphs"
    },
    {
        "name": "SAN",
        "description": "Spectral Attention Network for graph representation"
    },
    {
        "name": "GPS",
        "description": "Graph Product of Sum combining local and global attention"
    },
    {
        "name": "MoNet",
        "description": "Geometric deep learning with mixture models on graphs"
    },
    {
        "name": "SplineCNN",
        "description": "Continuous kernel convolution on irregular domains"
    },
    {
        "name": "FeaStNet",
        "description": "Feature Steerable CNN for graph-structured data"
    },
    {
        "name": "GatedGCN",
        "description": "Gated Graph Convolutional Network with edge features"
    },
    {
        "name": "ResGatedGCN",
        "description": "Residual Gated GCN for deep graph learning"
    },
    {
        "name": "TAGCN",
        "description": "Topology Adaptive Graph CNN with learnable filters"
    },
    {
        "name": "ARMA",
        "description": "Auto-Regressive Moving Average graph filter"
    },
    {
        "name": "APPNP",
        "description": "Approximate Personalized Propagation of Neural Predictions"
    },
    {
        "name": "SGC",
        "description": "Simplified Graph Convolution removing non-linearities"
    },
    {
        "name": "SIGN",
        "description": "Scalable Inception Graph Network with precomputed features"
    },
    {
        "name": "Cluster-GCN",
        "description": "GCN using graph clustering for efficient training"
    },
    {
        "name": "GraphSAINT",
        "description": "Graph sampling and aggregation for scalable GNN"
    },
    {
        "name": "FastGCN",
        "description": "Fast GCN using importance sampling for efficiency"
    },
    {
        "name": "LADIES",
        "description": "Layer-wise sampling for deep GCN training"
    },
    {
        "name": "VRGCN",
        "description": "Variance Reduced GCN for stable training"
    },
    {
        "name": "Graph-BERT",
        "description": "BERT-style pre-training for graph representation"
    },
    {
        "name": "GraphMAE",
        "description": "Masked AutoEncoder for self-supervised graph learning"
    },
    {
        "name": "BGRL",
        "description": "Bootstrapped Graph Representation Learning"
    },
    {
        "name": "GRACE",
        "description": "Graph Representation learning via Adaptive Contrastive Enhancement"
    },
    {
        "name": "GCA",
        "description": "Graph Contrastive Augmentation for self-supervised learning"
    },
    {
        "name": "MVGRL",
        "description": "Multi-View Graph Representation Learning"
    },
    {
        "name": "DGI",
        "description": "Deep Graph Infomax for unsupervised representation"
    },
    {
        "name": "GMI",
        "description": "Graph Mutual Information maximization for learning"
    },
    {
        "name": "GCL",
        "description": "Graph Contrastive Learning framework"
    }
]