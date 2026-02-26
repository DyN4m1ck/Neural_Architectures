#!/usr/bin/env python3
"""
Script to initialize architecture categories in the database.
"""

from architecture_categories import CategoryManager
from Architecture_Categories import architecture_data

def main():
    print("Initializing architecture categories...")
    
    with CategoryManager() as cm:
        # This will create the default categories if they don't exist
        cm.seed_default_categories()
        
        print("Retrieving all categories from database:")
        categories = cm.get_all()
        
        for category in categories:
            print(f"- {category.name}: {category.description}")
        
        print(f"\nTotal categories created: {len(categories)}")

if __name__ == "__main__":
    main()