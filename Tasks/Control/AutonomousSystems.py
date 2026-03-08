"""
Module for Autonomous Systems subcategory.
Part of CONTROL category - Decision making over time
"""

class AutonomousSystems:
    """Category: AUTONOMOUS SYSTEMS"""

    name = "Автономные системы"
    description = "Принятие решений во времени для автономных систем"

    subcategories = [
        {
            "name": "Автономное вождение",
            "description": "Autonomous driving - self-driving vehicles navigation and control"
        },
        {
            "name": "Автономные дроны",
            "description": "Autonomous drones - unmanned aerial vehicles control"
        },
        {
            "name": "Autonomous navigation",
            "description": "Autonomous navigation - path planning and obstacle avoidance"
        },
        {
            "name": "Автономные суда",
            "description": "Autonomous vessels - unmanned maritime vehicles"
        }
    ]

__all__ = ["AutonomousSystems"]