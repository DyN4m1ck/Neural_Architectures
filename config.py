# config.py
from dataclasses import dataclass

@dataclass
class DBConfig:
    URI: str = "bolt://localhost:7687"
    USER: str = ""
    PASSWORD: str = ""
    DATABASE: str = "memgraph"  # можно добавить при использовании нескольких БД

# Глобальный экземпляр
db_config = DBConfig()
