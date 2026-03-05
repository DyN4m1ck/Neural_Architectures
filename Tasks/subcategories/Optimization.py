"""
Module for Optimization subcategory.
Part of CONTROL category - Decision making over time
"""

class Optimization:
    """Category: OPTIMIZATION"""

    name = "Оптимизация"
    description = "Линейное, нелинейное, комбинаторное и многокритериальное программирование"

    subcategories = [
        {
            "name": "Линейное программирование",
            "description": "Linear programming - optimization with linear objective and constraints"
        },
        {
            "name": "Нелинейная оптимизация",
            "description": "Nonlinear optimization - optimization with nonlinear functions"
        },
        {
            "name": "Комбинаторная оптимизация",
            "description": "Combinatorial optimization - finding optimal solutions in discrete spaces"
        },
        {
            "name": "Многокритериальная оптимизация",
            "description": "Multi-objective optimization - optimizing multiple conflicting objectives"
        },
        {
            "name": "Global optimization",
            "description": "Global optimization - finding global optima in complex landscapes"
        },
        {
            "name": "Стохастическая оптимизация",
            "description": "Stochastic optimization - optimization under uncertainty"
        }
    ]

__all__ = ["Optimization"]