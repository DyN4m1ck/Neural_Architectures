# main.py
from architectures import Architecture, ArchitectureManager
from connection_manager import initialize_database

def demo():
    # Initialize database connection
    db = initialize_database()
    print("✅ Database initialized")
    
    with ArchitectureManager() as arch_db:
        # Clear database
        # arch_db.clear_db()
        
        # Create architectures
        cnn = Architecture(
            name="CNN",
            authors=["Yann LeCun", "Leon Bottou", "Yoshua Bengio", "Patrick Haffner"],
            source_url="http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf",
            year=1998,
            description="Convolutional Neural Network for image recognition"
        )
        cnn_id = arch_db.create(cnn)
        print(f"✓ Created CNN, ID: {cnn_id}")
        
        transformer = Architecture(
            name="Transformer",
            authors=["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."],
            source_url="https://arxiv.org/abs/1706.03762",
            year=2017,
            description="Attention Is All You Need"
        )
        tf_id = arch_db.create(transformer)
        print(f"✓ Created Transformer, ID: {tf_id}")
        
        # Read all
        print("\n📋 All architectures:")
        for arch in arch_db.get_all():
            print(f"  • {arch.name} ({arch.year}) — {arch.authors[0]} et al.")
        
        # Search
        print("\n🔍 Search for 'attention':")
        for arch in arch_db.search("attention"):
            print(f"  • {arch.name}: {arch.description}")
        
        # Update
        arch_db.update("CNN", description="Foundation of modern computer vision")
        print("\n✏️ Updated CNN description")
        
        # Verify update
        updated = arch_db.get_by_name("CNN")
        print(f"  New description: {updated.description}")

if __name__ == "__main__":
    demo()