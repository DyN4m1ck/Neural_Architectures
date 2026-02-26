#!/usr/bin/env python3
"""
Script to run Memgraph in-memory and load all architecture categories as labels
"""

import tempfile
import subprocess
import time
import sys
import os
import signal
from pathlib import Path

# Add workspace to path
sys.path.append('/workspace')

from Architecture_Categories.architecture_data import ARCHITECTURE_CATEGORIES
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


def create_memgraph_startup_script(categories):
    """Create a startup script to populate Memgraph with all architecture categories"""
    
    # Generate Cypher queries to create nodes with labels for each architecture
    cypher_commands = []
    
    for idx, category in enumerate(categories):
        name = category.get('name', f'Architecture_{idx}')
        description = category.get('description', '')
        
        # Create a label based on the architecture name (replacing spaces and special characters)
        label = name.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("&", "").replace(",", "").replace(".", "")
        
        # Escape quotes in name and description
        escaped_name = name.replace("'", "\\'").replace('"', '\\"')
        escaped_description = description.replace("'", "\\'").replace('"', '\\"')
        
        query = f"CREATE (a:`{label}` {{name: '{escaped_name}', description: '{escaped_description}'}});"
        cypher_commands.append(query)
    
    # Create startup script content
    script_content = "#!/usr/bin/bash\n\n"
    script_content += "# Memgraph startup script to load architecture categories\n\n"
    
    # Add each Cypher command
    for cmd in cypher_commands:
        script_content += f'mgconsole --host localhost --port 7687 << EOF\n{cmd}\nEOF\n'
    
    return script_content


def main():
    """Main function to prepare Memgraph startup script"""
    print("Preparing architecture categories for Memgraph...")
    
    # Get all architecture categories
    all_categories = get_all_architecture_categories()
    
    print(f"Found {len(all_categories)} architecture categories:")
    for cat in all_categories[:10]:  # Print first 10 for preview
        print(f"  - {cat['name']}")
    if len(all_categories) > 10:
        print(f"  ... and {len(all_categories) - 10} more")
    
    # Create startup script
    startup_script = create_memgraph_startup_script(all_categories)
    
    # Write the startup script to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='_memgraph_startup.sh', delete=False) as f:
        f.write(startup_script)
        startup_script_path = f.name
    
    print(f"\nStartup script created at: {startup_script_path}")
    print("Make sure to run this script after starting Memgraph:")
    print(f"chmod +x {startup_script_path}")
    print(f"./{startup_script_path}")
    
    # Also save the categories to a file that can be imported by other scripts
    categories_file_path = "/workspace/all_architecture_categories.py"
    with open(categories_file_path, 'w', encoding='utf-8') as f:
        f.write("# Generated file with all architecture categories\n\n")
        f.write("ALL_ARCHITECTURE_CATEGORIES = [\n")
        for cat in all_categories:
            f.write(f"    {repr(cat)},\n")
        f.write("]\n")
    
    print(f"\nAll architecture categories also saved to: {categories_file_path}")


if __name__ == "__main__":
    main()