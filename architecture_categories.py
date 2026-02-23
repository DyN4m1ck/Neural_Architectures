"""
Module for managing architecture categories in the database.
"""

from dataclasses import dataclass
from typing import Optional, List
from db_manager import DBManager


@dataclass
class ArchitectureCategory:
    """
    Represents an architecture category in the database.
    """
    name: str
    description: str
    id: Optional[str] = None


class CategoryManager(DBManager):
    """
    Manager class for handling architecture category operations in the database.
    """

    def create(self, name: str, description: str) -> ArchitectureCategory:
        """
        Create a new architecture category in the database.

        Args:
            name: Name of the category
            description: Description of the category

        Returns:
            Created ArchitectureCategory object
        """
        query = """
        CREATE (c:ArchitectureCategory {name: $name, description: $description})
        RETURN c.name AS name, c.description AS description
        """
        result = self.run_write(query, {"name": name, "description": description})
        
        # Return the created category
        return ArchitectureCategory(name=name, description=description)

    def get_all(self) -> List[ArchitectureCategory]:
        """
        Retrieve all architecture categories from the database.

        Returns:
            List of ArchitectureCategory objects
        """
        query = """
        MATCH (c:ArchitectureCategory)
        RETURN c.name AS name, c.description AS description
        ORDER BY c.name
        """
        records = self.run_read(query)
        return [
            ArchitectureCategory(
                name=record["name"],
                description=record["description"]
            )
            for record in records
        ]

    def get_by_name(self, name: str) -> Optional[ArchitectureCategory]:
        """
        Retrieve an architecture category by its name.

        Args:
            name: Name of the category to find

        Returns:
            ArchitectureCategory object if found, None otherwise
        """
        query = """
        MATCH (c:ArchitectureCategory)
        WHERE c.name = $name
        RETURN c.name AS name, c.description AS description
        """
        records = self.run_read(query, {"name": name})
        if records:
            record = records[0]
            return ArchitectureCategory(
                name=record["name"],
                description=record["description"]
            )
        return None

    def delete(self, name: str) -> bool:
        """
        Delete an architecture category by its name.

        Args:
            name: Name of the category to delete

        Returns:
            True if deletion was successful, False otherwise
        """
        query = """
        MATCH (c:ArchitectureCategory)
        WHERE c.name = $name
        DETACH DELETE c
        """
        try:
            self.run_write(query, {"name": name})
            return True
        except Exception:
            return False

    def seed_default_categories(self) -> None:
        """
        Create default architecture categories if they don't exist in the database.
        """
        default_categories = [
            {
                "name": "Convolutional Architectures (CNN)",
                "description": "Neural network architectures primarily based on convolutional layers, commonly used for image processing and computer vision tasks."
            },
            {
                "name": "Transformers & Attention",
                "description": "Architectures utilizing attention mechanisms, particularly transformers, widely used in NLP and other domains requiring sequence modeling."
            },
            {
                "name": "Feedforward Architectures",
                "description": "Traditional neural networks with connections that flow only in one direction, from input to output, without cycles."
            },
            {
                "name": "Generative Models",
                "description": "Models designed to generate new data samples, including GANs, VAEs, and diffusion models."
            },
            {
                "name": "State Space Models and Post-Transformer Architectures",
                "description": "Modern architectures including state space models and other approaches that emerged after transformer dominance."
            },
            {
                "name": "Recurrent and Sequential Architectures (RNN)",
                "description": "Architectures designed for sequential data processing, including RNNs, LSTMs, and GRUs."
            },
            {
                "name": "Graph Neural Networks (GNN)",
                "description": "Neural networks specifically designed to operate on graph-structured data, processing relationships between entities."
            },
            {
                "name": "Нейронные ОДУ и непрерывные модели",
                "description": "Архитектуры, основанные на обыкновенных дифференциальных уравнениях и непрерывных во времени моделях."
            },
            {
                "name": "Спайковые и нейроморфные архитектуры",
                "description": "Архитектуры, имитирующие биологические нейронные сети с использованием спайковых сигналов и нейроморфных принципов."
            },
            {
                "name": "Нейросимволические и гибридные архитектуры",
                "description": "Архитектуры, сочетающие нейронные и символические методы обработки информации."
            },
            {
                "name": "Архитектуры для обучения с усилением (RL)",
                "description": "Архитектуры, разработанные специально для задач обучения с подкреплением."
            },
            {
                "name": "Эффективные и мобильные архитектуры",
                "description": "Архитектуры, оптимизированные для работы на ограниченных вычислительных ресурсах."
            },
            {
                "name": "Архитектуры для малых данных и few-shot learning",
                "description": "Архитектуры, способные эффективно обучаться на ограниченных объемах данных."
            },
            {
                "name": "Архитектуры для поиска архитектур (NAS)",
                "description": "Архитектуры, используемые для автоматического поиска оптимальных архитектур нейронных сетей."
            },
            {
                "name": "Мультимодальные архитектуры",
                "description": "Архитектуры, способные обрабатывать несколько различных типов данных одновременно."
            },
            {
                "name": "Энергетические и равновесные модели",
                "description": "Модели, основанные на энергетических функциях и принципах термодинамического равновесия."
            },
            {
                "name": "Специализированные архитектуры",
                "description": "Архитектуры, разработанные для конкретных задач или областей применения."
            }
        ]

        for category_data in default_categories:
            # Check if category already exists
            existing_category = self.get_by_name(category_data["name"])
            if not existing_category:
                self.create(
                    name=category_data["name"],
                    description=category_data["description"]
                )