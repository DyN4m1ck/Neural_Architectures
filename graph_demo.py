"""
Comprehensive Graph Demo for Neural Network Architectures
This file combines all necessary functionality in one place to demonstrate
the graph structure of neural network architectures in Memgraph.
"""

from dataclasses import dataclass, asdict
from typing import Optional, List
from neo4j import GraphDatabase
from dataclasses import dataclass


@dataclass
class DBConfig:
    """Database configuration"""
    URI: str = "bolt://localhost:7687"
    USER: str = ""
    PASSWORD: str = ""
    DATABASE: str = "memgraph"


# Global config instance
db_config = DBConfig()


@dataclass
class Architecture:
    """Architecture node model"""
    name: str
    authors: List[str]
    source_url: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None


class DBManager:
    """Base database manager class"""
    
    def __init__(self, uri: str = None, user: str = None, password: str = None):
        self.uri = uri or db_config.URI
        self.user = user or db_config.USER
        self.password = password or db_config.PASSWORD
        auth = (self.user, self.password) if self.user and self.password else None
        self.driver = GraphDatabase.driver(self.uri, auth=auth)

    def close(self):
        """Close connection"""
        if self.driver:
            self.driver.close()

    def clear_db(self):
        """Clear entire database (for development)"""
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        print("✅ Database cleared")

    def run_write(self, query: str, params: Optional[dict] = None) -> None:
        """Execute write query"""
        with self.driver.session() as session:
            session.run(query, params or {})

    def run_read(self, query: str, params: Optional[dict] = None) -> List[dict]:
        """Execute read query and return results"""
        with self.driver.session() as session:
            result = session.run(query, params or {})
            return [record.data() for record in result]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class ArchitectureManager(DBManager):
    """Manager class for handling architecture operations in the database"""
    
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


def initialize_database():
    """
    Initialize the database with required schema and indexes
    """
    try:
        # Create connection manager instance directly
        uri = db_config.URI
        user = db_config.USER
        password = db_config.PASSWORD
        auth = (user, password) if user and password else None
        driver = GraphDatabase.driver(uri, auth=auth)

        # Test connection first
        with driver.session() as session:
            result = session.run("RETURN 'Connection successful' AS status")
            record = result.single()
            if record["status"] != "Connection successful":
                raise ConnectionError("Failed to connect to the database")
        
        print("✅ Database connection established")

        # Create indexes if they don't exist
        indexes = [
            "CREATE INDEX ON :Architecture(name);",
        ]

        for index_query in indexes:
            try:
                with driver.session() as session:
                    session.run(index_query)
            except Exception:
                # Index might already exist, which is fine
                pass

        print("✅ Database indexes created (if not existed)")

        # Return a DBManager instance instead of the raw driver
        db_manager = DBManager()
        return db_manager
    except Exception as e:
        print(f"⚠️  Could not connect to database: {e}")
        print("⚠️  This is expected if Memgraph is not running.")
        print("💡 To run this script properly, please ensure Memgraph is installed and running on port 7687.")
        return None


def display_graph_structure():
    """
    Display the entire graph structure including all nodes and relationships
    """
    print("\n🌐 Displaying full graph structure:")
    
    # Get all architectures
    with ArchitectureManager() as arch_db:
        all_nodes = arch_db.run_read("MATCH (n) RETURN n LIMIT 100")
        print(f"📊 Total nodes in graph: {len(all_nodes)}")
        
        # Show all architecture nodes
        architectures = arch_db.get_all()
        print(f"\n🧠 Architecture Nodes ({len(architectures)}):")
        for i, arch in enumerate(architectures, 1):
            print(f"  {i}. {arch.name} ({arch.year})")
            print(f"     Authors: {', '.join(arch.authors[:3])}{'...' if len(arch.authors) > 3 else ''}")
            print(f"     Description: {arch.description}")
            if arch.source_url:
                print(f"     Source: {arch.source_url}")
            print()
        
        # Show relationships (if any exist)
        relationships = arch_db.run_read("MATCH ()-[r]->() RETURN type(r) AS rel_type, count(r) AS count")
        if relationships:
            print(f"🔗 Relationships in graph ({sum(rel['count'] for rel in relationships)} total):")
            for rel in relationships:
                print(f"  - {rel['rel_type']}: {rel['count']} relationships")
        else:
            print("🔗 No relationships found in the graph")


def demo():
    """Main demonstration function"""
    # Initialize database connection
    db = initialize_database()
    
    if db is None:
        print("❌ Cannot proceed without database connection.")
        print("\n📋 Sample Architecture Data (without database connection):")
        print("  • CNN (1998) — Yann LeCun et al.")
        print("  • Transformer (2017) — Ashish Vaswani et al.")
        print("\n💡 When Memgraph is running, this script will create these nodes in the graph database.")
        return
    
    print("✅ Database initialized")

    with ArchitectureManager() as arch_db:
        # Clear database (commented out as requested)
        # arch_db.clear_db()

        # Create architectures
        cnn = Architecture(
            name="CNN",
            authors=["Yann LeCun", "Leon Bottou", "Yoshua Bengio", "Patrick Haffner"],
            source_url="http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf",
            year=1998,
            description="Convolutional Neural Network for image recognition"
        )
        cnn_id = arch_db.create(cnn)
        print(f"✓ Created CNN, ID: {cnn_id}")

        transformer = Architecture(
            name="Transformer",
            authors=["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."],
            source_url="https://arxiv.org/abs/1706.03762",
            year=2017,
            description="Attention Is All You Need"
        )
        tf_id = arch_db.create(transformer)
        print(f"✓ Created Transformer, ID: {tf_id}")

        # Read all
        print("\n📋 All architectures:")
        for arch in arch_db.get_all():
            print(f"  • {arch.name} ({arch.year}) — {arch.authors[0]} et al.")

        # Search
        print("\n🔍 Search for 'attention':")
        for arch in arch_db.search("attention"):
            print(f"  • {arch.name}: {arch.description}")

        # Update
        arch_db.update("CNN", description="Foundation of modern computer vision")
        print("\n✏️ Updated CNN description")

        # Verify update
        updated = arch_db.get_by_name("CNN")
        print(f"  New description: {updated.description}")
        
        # Display full graph structure
        display_graph_structure()


if __name__ == "__main__":
    demo()