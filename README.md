# Neural Architecture Knowledge Graph

A graph-based knowledge base for neural network architectures built with Python and Neo4j/Memgraph.

## Overview

This project creates a comprehensive knowledge graph of neural network architectures, allowing for structured storage, retrieval, and analysis of deep learning models and their relationships.

## Features

- **Architecture Management**: Store and manage neural network architectures with metadata
- **Category Classification**: Organize architectures into predefined categories
- **Search Functionality**: Find architectures by name or description
- **Relationship Modeling**: Represent connections between different architectures
- **Extensible Design**: Easy to add new architectures and categories

## Architecture Categories

The system includes over 40 predefined categories covering:
- Convolutional Architectures (CNN)
- Transformers & Attention Mechanisms
- Recurrent Architectures (RNN/LSTM/GRU)
- Generative Models
- Graph Neural Networks
- Autoencoders
- And many more specialized architectures

## Requirements

- Python 3.8+
- Neo4j or Memgraph database
- Dependencies listed in `requirements.txt`

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up Neo4j or Memgraph database
3. Configure database connection in `config.py`

## Configuration

Update `config.py` with your database credentials:

```python
@dataclass
class DBConfig:
    URI: str = "bolt://localhost:7687"
    USER: str = "neo4j"
    PASSWORD: str = "your_password"
```

## Usage

Run the main demo:
```bash
python main.py
```

Initialize categories:
```bash
python initialize_categories.py
```

## Project Structure

- `main.py` - Demo application showing CRUD operations
- `architectures.py` - Architecture entity and manager
- `architecture_categories.py` - Category management
- `architecture_data.py` - Predefined categories data
- `db_manager.py` - Database connection management
- `config.py` - Database configuration
- `connection_manager.py` - Alternative database manager implementation
- `initialize_categories.py` - Script to populate categories

## Data Model

### Architecture Node Properties
- `name`: Architecture name (indexed)
- `authors`: List of author names
- `source_url`: Paper URL
- `year`: Publication year
- `description`: Brief description

### Planned Relationships
- `ARCHITECTURE_HAS_CATEGORY` - Connect architectures to categories
- `INSPIRED_BY` - Show architectural influences
- `APPLIES_TO_DOMAIN` - Connect to application domains

## Development Roadmap

### Short-term Improvements
1. Consolidate duplicate database managers
2. Add input validation and sanitization
3. Implement proper error handling
4. Add unit tests
5. Improve security (connection parameters)

### Medium-term Goals
1. Implement relationships between architectures
2. Add advanced search capabilities
3. Create web interface
4. Add user authentication
5. Implement versioning for architectures

### Long-term Vision
1. ML-powered recommendation engine
2. Visualization tools for architecture relationships
3. API for external integrations
4. Collaborative editing features
5. Research paper integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

See LICENSE file for licensing information.