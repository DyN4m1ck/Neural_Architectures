#!/usr/bin/env python3
"""
Optimized Cypher query generator that creates parameterized queries instead of hardcoded values
to avoid the large static file issue
"""

import sys
import importlib.util
from pathlib import Path
import json


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


def generate_parameterized_cypher_queries(categories_dict):
    """Generate parameterized Cypher queries that can be called with parameters"""
    
    # Define the template queries as a JSON structure that can be used programmatically
    queries_template = {
        "create_indexes": [
            "CREATE INDEX ON :Category(name);",
            "CREATE INDEX ON :Architecture(name);"
        ],
        "create_categories": """
        UNWIND $categories AS cat_data
        MERGE (c:Category {name: cat_data.name})
        SET c.type = 'category_group',
            c.architecture_count = cat_data.count
        """,
        "create_architectures_for_category": """
        MATCH (c:Category {name: $category_name})
        UNWIND $architectures AS arch_data
        MERGE (a:Architecture {name: arch_data.name})
        SET a.description = arch_data.description,
            a.category = $category_name
        WITH a, c
        MERGE (a)-[:BELONGS_TO]->(c)
        """
    }
    
    return queries_template


def generate_sample_execution_script(categories_dict):
    """Generate a sample script showing how to execute the parameterized queries"""
    
    # Generate sample data to demonstrate how the parameters would be structured
    categories_data = []
    for category_name, architectures in categories_dict.items():
        categories_data.append({
            "name": category_name,
            "count": len(architectures)
        })
    
    # Example of how to use the parameterized queries
    example_usage = f'''
// Example of how to use these parameterized queries:

// 1. First, create indexes
CREATE INDEX ON :Category(name);
CREATE INDEX ON :Architecture(name);

// 2. Then create categories with parameters:
// Parameters: {{
//   "categories": {json.dumps(categories_data, indent=4)}
// }}
UNWIND $categories AS cat_data
MERGE (c:Category {{name: cat_data.name}})
SET c.type = 'category_group',
    c.architecture_count = cat_data.count;

// 3. Then create architectures for each category with parameters:
// For each category, you would run:
// Parameters: {{
//   "category_name": "FeedForward",
//   "architectures": [/* array of architecture objects */]
// }}
MATCH (c:Category {{name: $category_name}})
UNWIND $architectures AS arch_data
MERGE (a:Architecture {{name: arch_data.name}})
SET a.description = arch_data.description,
    a.category = $category_name
WITH a, c
MERGE (a)-[:BELONGS_TO]->(c);
'''
    
    return example_usage


def main():
    print("🔍 Parsing all 17 category files...")
    categories_dict = get_all_categories_and_architectures()
    
    total_archs = sum(len(archs) for archs in categories_dict.values())
    print(f"\n📊 Found {len(categories_dict)} categories with {total_archs} total architectures")
    
    print("\n📝 Generating parameterized Cypher queries...")
    queries_template = generate_parameterized_cypher_queries(categories_dict)
    
    # Save the template
    template_file = '/workspace/parameterized_queries.json'
    with open(template_file, 'w') as f:
        json.dump(queries_template, f, indent=2)
    
    print(f"✅ Parameterized query templates saved to: {template_file}")
    
    # Save the example usage
    example_file = '/workspace/parameterized_queries_example.cypher'
    example_content = generate_sample_execution_script(categories_dict)
    with open(example_file, 'w') as f:
        f.write(example_content)
    
    print(f"✅ Example usage saved to: {example_file}")
    
    # Also save summary
    print("\n📋 Category summary:")
    for cat_name, archs in categories_dict.items():
        print(f"   {cat_name}: {len(archs)} architectures")


if __name__ == "__main__":
    main()