# architectures.py
from dataclasses import dataclass, asdict
from typing import Optional, List
from connection_manager import ConnectionManager as DBManager

@dataclass
class Architecture:
    """Architecture node model"""
    name: str
    authors: List[str]
    source_url: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None

class ArchitectureManager(DBManager):
    LABEL = "Architecture"
    
    def create(self, arch: Architecture) -> str:
        """Create architecture node, return its ID"""
        query = """
            CREATE (a:Architecture {
                name: $name,
                authors: $authors,
                source_url: $source_url,
                year: $year,
                description: $description
            })
            RETURN id(a) as id
        """
        result = self.run_read(query, asdict(arch))
        return str(result[0]['id']) if result else None

    def get_by_name(self, name: str) -> Optional[Architecture]:
        """Find architecture by name"""
        query = """
            MATCH (a:Architecture {name: $name})
            RETURN a {.*} as data
        """
        result = self.run_read(query, {"name": name})
        if not result:
            return None
        data = result[0]['data']
        return Architecture(**data)

    def get_all(self) -> List[Architecture]:
        """Get all architectures"""
        query = "MATCH (a:Architecture) RETURN a {.*} as data"
        results = self.run_read(query)
        return [Architecture(**r['data']) for r in results]

    def update(self, name: str, **updates) -> bool:
        """Update architecture fields by name"""
        if not updates:
            return False
        set_clause = ", ".join(f"a.{key} = ${key}" for key in updates.keys())
        query = f"""
            MATCH (a:Architecture {{name: $name}})
            SET {set_clause}
            RETURN count(a) > 0 as success
        """
        params = {"name": name, **updates}
        result = self.run_read(query, params)
        return result[0]['success'] if result else False

    def delete(self, name: str) -> bool:
        """Delete architecture by name (with relationships)"""
        query = """
            MATCH (a:Architecture {name: $name})
            DETACH DELETE a
            RETURN count(a) > 0 as success
        """
        result = self.run_read(query, {"name": name})
        return result[0]['success'] if result else False

    def search(self, keyword: str) -> List[Architecture]:
        """Search by name or description"""
        query = """
            MATCH (a:Architecture)
            WHERE toLower(a.name) CONTAINS toLower($kw)
               OR toLower(a.description) CONTAINS toLower($kw)
            RETURN a {.*} as data
        """
        results = self.run_read(query, {"kw": keyword})
        return [Architecture(**r['data']) for r in results]