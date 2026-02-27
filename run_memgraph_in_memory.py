
---

## Быстрое решение (можете использовать прямо сейчас):

```python
#!/usr/bin/env python3
"""
Script to create two-level hierarchy in Memgraph:
Level 1: 17 Category nodes
Level 2: Architecture nodes linked to categories
"""

import os
import sys
import importlib.util
from pathlib import Path

sys.path.append('/workspace')

def get_all_categories_and_architectures():
    """Parse all 17 files and extract categories + architectures"""
    
    arch_dir = Path('/workspace/Architecture_Categories')
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
        'EnergyAndEquilibrium.py',
        'EfficientAndMobile.py',
        'RecAndSeq.py',
        'RL.py',
        'StateSpace.py',
        'SmallDataAndFewShot.py',
        'Specialized.py',
        'SpikeAndNeuromorphic.py',
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


def create_memgraph_queries(categories_dict):
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


def main():
    print("🔍 Parsing all 17 category files...")
    categories_dict = get_all_categories_and_architectures()
    
    total_archs = sum(len(archs) for archs in categories_dict.values())
    print(f"\n📊 Found {len(categories_dict)} categories with {total_archs} total architectures")
    
    print("\n📝 Generating Cypher queries...")
    queries = create_memgraph_queries(categories_dict)
    
    # Save to file
    output_file = '/workspace/memgraph_two_level_hierarchy.cypher'
    with open(output_file, 'w') as f:
        f.write('-- Two-level hierarchy: Categories -> Architectures\n\n')
        for query in queries:
            f.write(query + '\n')
    
    print(f"✅ Queries saved to: {output_file}")
    print(f"\n📌 To load into Memgraph:")
    print(f"   mgconsole --host localhost --port 7687 < {output_file}")
    
    # Also save summary
    print("\n📋 Category summary:")
    for cat_name, archs in categories_dict.items():
        print(f"   {cat_name}: {len(archs)} architectures")


if __name__ == "__main__":
    main()