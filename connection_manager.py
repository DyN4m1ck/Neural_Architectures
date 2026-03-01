"""
Connection Manager for Memgraph Lab
Handles database connections and dependency management for the project
"""
import os
from neo4j import GraphDatabase
from typing import Optional, List
from config import db_config


class ConnectionManager:
    """
    Manages connections to Memgraph database with support for both Neo4j driver compatibility
    and specific Memgraph features
    """
    
    def __init__(self, uri: str = None, user: str = None, password: str = None, database: str = None):
        """
        Initialize connection manager
        
        Args:
            uri: Database connection URI
            user: Database username
            password: Database password
            database: Database name (for multi-tenant setups)
        """
        self.uri = uri or db_config.URI
        self.user = user or db_config.USER
        self.password = password or db_config.PASSWORD
        self.database = database or getattr(db_config, 'DATABASE', None)
        
        # Create driver with appropriate settings for Memgraph
        auth = (self.user, self.password) if self.user and self.password else None
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=auth)
        except Exception as e:
            print(f"Could not connect to database: {e}")
            print("Creating mock connection for testing purposes...")
            self.driver = None
        
    def test_connection(self) -> bool:
        """
        Test if connection to database is successful
        
        Returns:
            True if connection is successful, False otherwise
        """
        if not self.driver:
            print("No active database connection")
            return False
            
        try:
            with self.driver.session() as session:
                # Run a simple query to test connection
                result = session.run("RETURN 'Connection successful' AS status")
                record = result.single()
                return record["status"] == "Connection successful"
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False
    
    def close(self):
        """Close the database connection"""
        if self.driver:
            self.driver.close()
    
    def run_query(self, query: str, parameters: Optional[dict] = None) -> List[dict]:
        """
        Execute a Cypher query and return results
        
        Args:
            query: Cypher query string
            parameters: Query parameters dictionary
            
        Returns:
            List of dictionaries representing query results
        """
        if not self.driver:
            print(f"Mock read query executed: {query}")
            return []
            
        parameters = parameters or {}
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]
    
    def run_write_query(self, query: str, parameters: Optional[dict] = None) -> None:
        """
        Execute a write Cypher query
        
        Args:
            query: Cypher query string for write operations
            parameters: Query parameters dictionary
        """
        if not self.driver:
            print(f"Mock write query executed: {query}")
            return
            
        parameters = parameters or {}
        with self.driver.session() as session:
            session.run(query, parameters)
    
    def clear_database(self):
        """Clear all nodes and relationships in the database"""
        if not self.driver:
            print("Mock: Database cleared")
            return
            
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        print("✓ Database cleared")
    
    def get_database_info(self) -> dict:
        """
        Get basic information about the connected database
        
        Returns:
            Dictionary with database information
        """
        if not self.driver:
            return {"error": "No active database connection"}
            
        info_queries = {
            "version": "SHOW DATABASE INFO YIELD * RETURN version;",
            "memory_usage": "SHOW STORAGE INFO YIELD * RETURN *;",
            "node_count": "MATCH (n) RETURN count(n) AS node_count;",
            "relationship_count": "MATCH ()-[r]->() RETURN count(r) AS relationship_count;"
        }
        
        info = {}
        with self.driver.session() as session:
            for key, query in info_queries.items():
                try:
                    result = session.run(query)
                    record = result.single()
                    if record:
                        info[key] = record.values()[0] if len(record.values()) == 1 else dict(record)
                    else:
                        info[key] = None
                except Exception as e:
                    info[key] = f"Error retrieving {key}: {str(e)}"
        
        return info
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


def get_connection_manager() -> ConnectionManager:
    """
    Factory function to create a connection manager instance
    
    Returns:
        ConnectionManager instance
    """
    return ConnectionManager()


def initialize_database():
    """
    Initialize the database with required schema and indexes
    """
    cm = get_connection_manager()
    
    # Test connection first
    if not cm.test_connection():
        raise ConnectionError("Failed to connect to the database")
    
    print("✓ Database connection established")
    
    # Create indexes if they don't exist
    indexes = [
        "CREATE INDEX ON :Architecture(name);",
        "CREATE INDEX ON :Tag(name);"
    ]
    
    for index_query in indexes:
        try:
            cm.run_write_query(index_query)
        except Exception:
            # Index might already exist, which is fine
            pass
    
    print("✓ Database indexes created (if not existed)")
    
    return cm