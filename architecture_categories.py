"""
Module for managing architecture categories in the database.
"""

from dataclasses import dataclass
from typing import Optional, List
from connection_manager import ConnectionManager as DBManager
from architecture_data import ARCHITECTURE_CATEGORIES


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
        default_categories = ARCHITECTURE_CATEGORIES

        for category_data in default_categories:
            # Check if category already exists
            existing_category = self.get_by_name(category_data["name"])
            if not existing_category:
                self.create(
                    name=category_data["name"],
                    description=category_data["description"]
                )