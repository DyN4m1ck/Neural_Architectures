"""
Module for Meta-Tasks subcategory.
Part of HYBRID category - Combined/Multi-domain tasks
"""

class MetaTasks:
    """Category: META-TASKS"""

    name = "Мета-задачи"
    description = "AutoML, NAS, Transfer Learning, Meta-Learning, Few-Shot, Multi-Task Learning"

    subcategories = [
        {
            "name": "AutoML",
            "description": "Automated machine learning - automating model selection and hyperparameter tuning"
        },
        {
            "name": "NAS (Neural Architecture Search)",
            "description": "Neural architecture search - automatically designing neural network architectures"
        },
        {
            "name": "Transfer Learning",
            "description": "Transfer learning - applying knowledge from one domain to another"
        },
        {
            "name": "Meta-Learning",
            "description": "Meta-learning - learning to learn, adapting quickly to new tasks"
        },
        {
            "name": "Few-Shot Learning",
            "description": "Few-shot learning - learning from very few examples"
        },
        {
            "name": "Multi-Task Learning",
            "description": "Multi-task learning - training models to perform multiple related tasks"
        }
    ]

__all__ = ["MetaTasks"]
