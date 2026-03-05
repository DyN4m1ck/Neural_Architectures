"""
Module for Energy subcategory.
Part of CONTROL category - Decision making over time
"""

class Energy:
    """Category: ENERGY"""

    name = "Энергетика и инфраструктура"
    description = "Smart grids, оптимизация энергосистем, управление трафиком"

    subcategories = [
        {
            "name": "Smart grids",
            "description": "Smart grids - intelligent electricity distribution systems"
        },
        {
            "name": "Оптимизация энергосистем",
            "description": "Energy system optimization - efficient power generation and distribution"
        },
        {
            "name": "Управление трафиком",
            "description": "Traffic management - optimizing traffic flow and congestion control"
        }
    ]

__all__ = ["Energy"]