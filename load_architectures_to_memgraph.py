#!/usr/bin/env python3
"""
Script to load all architecture categories from files into Memgraph as labels
"""

import sys
import os
sys.path.append('/workspace')

from Architecture_Categories.architecture_data import ARCHITECTURE_CATEGORIES
from connection_manager import ConnectionManager
from config import db_config
import importlib.util


def get_all_architecture_categories():
    """Get all architecture categories from all files in Architecture_Categories directory"""
    categories = []
    
    # Add the main FeedForward categories
    categories.extend(ARCHITECTURE_CATEGORIES)
    
    # Get all Python files in Architecture_Categories directory
    arch_dir = '/workspace/Architecture_Categories'
    for filename in os.listdir(arch_dir):
        if filename.endswith('.py') and filename != '__init__.py' and filename != 'architecture_data.py':
            filepath = os.path.join(arch_dir, filename)
            
            # Import the module dynamically
            spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Look for any list attributes in the module that contain architecture data
            for attr_name in dir(module):
                attr_value = getattr(module, attr_name)
                if isinstance(attr_value, list) and attr_name != '__builtins__':
                    for item in attr_value:
                        if isinstance(item, dict) and 'name' in item:
                            categories.append(item)
    
    return categories


def load_architectures_to_memgraph():
    """Load all architecture categories as labels in Memgraph"""
    try:
        # Connect to Memgraph
        conn_manager = ConnectionManager(db_config.URI)
        # Use run_write_query method to execute queries
        
        # Get all architecture categories
        all_categories = get_all_architecture_categories()
        
        print(f"Found {len(all_categories)} architecture categories to load")
        
        # Create nodes with labels for each architecture
        for idx, category in enumerate(all_categories):
            name = category.get('name', f'Architecture_{idx}')
            description = category.get('description', '')
            
            # Create a node with the architecture name as both property and label
            # We'll create a label based on the architecture name (replacing spaces and special characters)
            label = name.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("&", "")
            
            query = f"""
            CREATE (a:`{label}` {{
                name: $name,
                description: $description
            }})
            """
            
            conn_manager.run_write_query(query, {'name': name, 'description': description})
            
            print(f"Created node with label: {label}, name: {name}")
        
        print("Successfully loaded all architectures to Memgraph!")
        
    except Exception as e:
        print(f"Error loading architectures to Memgraph: {e}")
        raise
    finally:
        conn_manager.close()


if __name__ == "__main__":
    load_architectures_to_memgraph()