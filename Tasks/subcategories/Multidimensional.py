"""
Module for Multidimensional Projections subcategory.
Part of HYBRID category - Combined/Multi-domain tasks
"""

class Multidimensional:
    """Category: MULTIDIMENSIONAL PROJECTIONS"""

    name = "Многомерные проекции"
    description = "3D→2D визуализация, 4D→3D проекция, N-D embedding, dimensionality reduction"

    subcategories = [
        {
            "name": "3D → 2D визуализация",
            "description": "3D to 2D visualization - projecting three-dimensional data to two dimensions"
        },
        {
            "name": "4D → 3D проекция",
            "description": "4D to 3D projection - visualizing four-dimensional data in three dimensions"
        },
        {
            "name": "N-D embedding",
            "description": "N-dimensional embedding - representing high-dimensional data in lower dimensions"
        },
        {
            "name": "Dimensionality reduction",
            "description": "Dimensionality reduction - techniques like PCA, t-SNE, UMAP for data compression"
        }
    ]

__all__ = ["Multidimensional"]
