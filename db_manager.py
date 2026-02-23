# db_manager.py
from neo4j import GraphDatabase
from typing import Optional, List
from config import db_config

class DBManager:
    def __init__(self, uri: str = None, user: str = None, password: str = None):
        self.uri = uri or db_config.URI
        self.user = user or db_config.USER
        self.password = password or db_config.PASSWORD
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        """Close connection"""
        if self.driver:
            self.driver.close()

    def clear_db(self):
        """Clear entire database (for development)"""
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        print("✓ Database cleared")

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