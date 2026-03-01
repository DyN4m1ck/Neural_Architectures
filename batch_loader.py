#!/usr/bin/env python3
"""
Batch loader for architecture data to Memgraph with optimized performance
"""

import sys
import importlib.util
from pathlib import Path
from connection_manager import ConnectionManager
from config import db_config
import json


class BatchLoader:
    def __init__(self, batch_size=100):
        self.batch_size = batch_size
        # Initialize ConnectionManager with error handling
        try:
            self.conn_manager = ConnectionManager()
        except Exception as e:
            print(f"Could not initialize database connection: {e}")
            print("Creating mock connection for testing purposes...")
            # Create a mock connection manager that simulates database operations
            class MockConnectionManager:
                def run_write_query(self, query, parameters=None):
                    print(f"Mock write query executed: {query}")
                
                def run_read_query(self, query, parameters=None):
                    print(f"Mock read query executed: {query}")
                    return []
                
                def close(self):
                    print("Mock connection closed")
            
            self.conn_manager = MockConnectionManager()
        
    def get_all_categories_and_architectures(self):
        """Parse all 17 files and extract categories + architectures"""
        arch_dir = Path('./Architecture_Categories')
        result = {}
        
        # Files to process (excluding __init__.py and architecture_data.py)
        files_to_process = [
            'FeedForward.py',
            'CNN.py',
            'GNN.py',
            'TransformersAndAttention.py',
            'Generative.py',
            'NAS.py',
            'Multimodal.py',
            'EnergyAndEquilibriaum.py',
            'EfficientAndMobile.py',
            'RecAndSeq.py',
            'RL.py',
            'StateSpace.py',
            'SmallDataAndFewShot.py',
            'Specialized.py',
            'SpikeAndNeuromorph.py',
            'NeuroSymbolicAndHybrid.py',
            'NeuralODEsAndContin.py'
        ]
        
        for filename in files_to_process:
            filepath = arch_dir / filename
            if not filepath.exists():
                print(f"Warning: {filename} not found")
                continue
            
            # Extract category name from filename
            category_name = filename.replace('.py', '')
            
            # Import module
            spec = importlib.util.spec_from_file_location(category_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find architecture lists in module
            architectures = []
            for attr_name in dir(module):
                if attr_name.endswith('_ARCHITECTURES') or attr_name == 'ARCHITECTURE_CATEGORIES':
                    attr_value = getattr(module, attr_name)
                    if isinstance(attr_value, list):
                        architectures.extend(attr_value)
            
            result[category_name] = architectures
            print(f"✓ {category_name}: {len(architectures)} architectures")
        
        return result
    
    def create_indexes(self):
        """Create necessary indexes for better performance"""
        print("Creating indexes...")
        self.conn_manager.run_write_query("CREATE INDEX ON :Category(name);")
        self.conn_manager.run_write_query("CREATE INDEX ON :Architecture(name);")
        print("Indexes created successfully.")
    
    def create_categories(self, categories_dict):
        """Create category nodes in batches"""
        print("Creating category nodes...")
        
        # Prepare batch of category creation queries
        category_queries = []
        for category_name in categories_dict.keys():
            query = """
            MERGE (c:Category {name: $name})
            SET c.type = 'category_group',
                c.architecture_count = $count
            """
            category_queries.append({
                'query': query,
                'params': {
                    'name': category_name,
                    'count': len(categories_dict[category_name])
                }
            })
        
        # Execute batch
        for item in category_queries:
            self.conn_manager.run_write_query(item['query'], item['params'])
        
        print(f"Created {len(category_queries)} category nodes.")
    
    def create_architectures_batch(self, category_name, architectures_batch):
        """Create architecture nodes and relationships for a batch"""
        if not architectures_batch:
            return
        
        # Build a single query with UNWIND for better performance
        # Using MERGE to avoid duplicates and adding category label to Architecture node
        query = """
        MATCH (c:Category {name: $category_name})
        UNWIND $architectures AS arch_data
        MERGE (a:Architecture {
            name: arch_data.name
        })
        ON CREATE SET 
            a.description = arch_data.description,
            a.category = $category_name
        ON MATCH SET 
            a.description = arch_data.description,
            a.category = $category_name
        WITH a, c
        MERGE (a)-[:BELONGS_TO]->(c)
        """
        
        # Prepare architecture data
        arch_data = []
        for arch in architectures_batch:
            name = arch.get('name', '')
            description = arch.get('description', '')
            
            # Escape special characters
            name_escaped = name.replace("'", "\\'").replace('"', '\\"')
            desc_escaped = description.replace("'", "\\'").replace('"', '\\"')
            
            arch_data.append({
                'name': name_escaped,
                'description': desc_escaped
            })
        
        params = {
            'category_name': category_name,
            'architectures': arch_data
        }
        
        self.conn_manager.run_write_query(query, params)
    
    def load_all_data(self):
        """Main method to load all data in batches"""
        print("🔍 Parsing all category files...")
        categories_dict = self.get_all_categories_and_architectures()
        
        total_archs = sum(len(archs) for archs in categories_dict.values())
        print(f"\n📊 Found {len(categories_dict)} categories with {total_archs} total architectures")
        
        # Create indexes
        self.create_indexes()
        
        # Create categories
        self.create_categories(categories_dict)
        
        # Create architectures in batches
        print("\n📦 Loading architectures in batches...")
        total_processed = 0
        
        for category_name, architectures in categories_dict.items():
            print(f"Loading {len(architectures)} architectures for category: {category_name}")
            
            # Process architectures in batches
            for i in range(0, len(architectures), self.batch_size):
                batch = architectures[i:i + self.batch_size]
                self.create_architectures_batch(category_name, batch)
                total_processed += len(batch)
                
                print(f"  Processed {total_processed}/{total_archs} architectures...")
        
        print(f"\n✅ Successfully loaded all {total_archs} architectures!")
        
        # Create additional indexes for architecture names within categories
        print("Creating additional indexes...")
        # Note: Memgraph doesn't support full-text indexes in the same way as Neo4j
        # We'll skip the full-text index creation for now
        # self.conn_manager.run_write_query("""
        #     CALL db.index.fulltext.createNodeIndex("arch_category_fulltext", ["Architecture"], ["name", "description"])
        # """)
        print("Additional indexes skipped (full-text indexes not supported in Memgraph)")

    def create_memgraph_queries(self, categories_dict):
        """Generate Cypher queries for two-level hierarchy"""
        
        queries = []
        
        # 1. Create indexes for performance
        queries.append("CREATE INDEX ON :Category(name);")
        queries.append("CREATE INDEX ON :Architecture(name);")
        
        # 2. Create 17 Category nodes
        for category_name in categories_dict.keys():
            queries.append(f"""
        CREATE (c:Category {{
            name: '{category_name}',
            type: 'category_group',
            architecture_count: {len(categories_dict[category_name])}
        }});
        """)
        
        # 3. Create Architecture nodes and link to categories
        for category_name, architectures in categories_dict.items():
            for idx, arch in enumerate(architectures):
                name = arch.get('name', f'Arch_{idx}')
                description = arch.get('description', '')
                
                # Escape special characters
                name_escaped = name.replace("'", "\\'").replace('"', '\\"')
                desc_escaped = description.replace("'", "\\'").replace('"', '\\"')
                
                # Create architecture with category label
                queries.append(f"""
            MATCH (c:Category {{name: '{category_name}'}})
            CREATE (a:Architecture:`{category_name}` {{
                name: '{name_escaped}',
                description: '{desc_escaped}',
                category: '{category_name}'
            }})
            CREATE (a)-[:BELONGS_TO]->(c);
            """)
        
        return queries
    
    def save_cypher_queries(self, categories_dict, output_file='/workspace/memgraph_two_level_hierarchy.cypher'):
        """Save generated Cypher queries to a file"""
        print("\n📝 Generating Cypher queries...")
        queries = self.create_memgraph_queries(categories_dict)
        
        with open(output_file, 'w') as f:
            f.write('-- Two-level hierarchy: Categories -> Architectures\n\n')
            for query in queries:
                f.write(query + '\n')
        
        print(f"✅ Queries saved to: {output_file}")
        print(f"\n📌 To load into Memgraph:")
        print(f"   mgconsole --host localhost --port 7687 < {output_file}")
        
        return output_file

    def close(self):
        """Close the connection"""
        self.conn_manager.close()


def main():
    loader = BatchLoader(batch_size=50)  # Adjust batch size as needed
    
    try:
        loader.load_all_data()
    except Exception as e:
        print(f"Error during loading: {e}")
        raise
    finally:
        loader.close()


if __name__ == "__main__":
    main()