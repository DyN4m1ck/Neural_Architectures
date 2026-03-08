"""
Module for Control Theory subcategory.
Part of CONTROL category - Decision making over time
"""

class ControlTheory:
    """Category: CONTROL THEORY"""

    name = "Теория автоматического управления"
    description = "Линейные, нелинейные, оптимальные и адаптивные системы управления"

    subcategories = [
        {
            "name": "Линейные системы",
            "description": "Linear systems - control of systems with linear dynamics"
        },
        {
            "name": "Нелинейные системы",
            "description": "Nonlinear systems - control of systems with nonlinear dynamics"
        },
        {
            "name": "Оптимальное управление",
            "description": "Optimal control - finding control policies that optimize performance criteria"
        },
        {
            "name": "Робастное управление",
            "description": "Robust control - maintaining performance under uncertainty"
        },
        {
            "name": "Адаптивное управление",
            "description": "Adaptive control - adjusting controller parameters in real-time"
        },
        {
            "name": "Распределённое управление",
            "description": "Distributed control - coordinating multiple controllers across a system"
        }
    ]

__all__ = ["ControlTheory"]