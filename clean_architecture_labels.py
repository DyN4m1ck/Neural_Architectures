from neo4j import GraphDatabase

# --- НАСТРОЙКИ ПОДКЛЮЧЕНИЯ ---
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "" 

def delete_all_architecture_categories():
    print(f"Подключение к Memgraph ({URI})...")
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    try:
        with driver.session() as session:
            # Запрос удаляет ВСЕ узлы с меткой ArchitectureCategory
            # DETACH DELETE удаляет и сам узел, и все его связи
            query = """
            MATCH (n:ArchitectureCategory)
            DETACH DELETE n
            """
            
            result = session.run(query)
            summary = result.consume()
            
            count = summary.counters.nodes_deleted
            
            if count > 0:
                print(f"✅ Успешно! Удалено узлов с меткой ArchitectureCategory: {count}")
            else:
                print("ℹ️ Узлы с меткой ArchitectureCategory не найдены (база уже чиста).")
                
    except Exception as e:
        print(f"❌ Ошибка при удалении: {e}")
    finally:
        driver.close()

if __name__ == "__main__":
    delete_all_architecture_categories()