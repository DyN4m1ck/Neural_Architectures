"""
Module for Decision Making subcategory.
Part of CONTROL category - Decision making over time
"""

class DecisionMaking:
    """Category: DECISION MAKING"""

    name = "Принятие решений"
    description = "Reinforcement Learning, игры, стратегии, multi-agent системы"

    subcategories = [
        {
            "name": "Reinforcement Learning",
            "description": "Learning optimal policies through interaction with environment"
        },
        {
            "name": "Игры (Chess, Go, StarCraft)",
            "description": "Game playing - strategic decision making in competitive environments"
        },
        {
            "name": "Стратегии",
            "description": "Strategic planning - long-term decision making"
        },
        {
            "name": "Multi-agent systems",
            "description": "Multi-agent systems - coordination and competition among multiple agents"
        },
        {
            "name": "Game theory",
            "description": "Game theory - mathematical modeling of strategic interactions"
        }
    ]

__all__ = ["DecisionMaking"]