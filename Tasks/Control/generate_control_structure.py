import json
import os

def create_structure():
    # Путь к файлу таксономии
    taxonomy_file = '/home/dynamick/Test/memgraph-neuro/Tasks/Control/control_taxonomy.json'
    base_dir = 'Tasks/Control'
    
    if not os.path.exists(taxonomy_file):
        print(f"Error: {taxonomy_file} not found.")
        return

    with open(taxonomy_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Generating structure for: {data['section_name']}")

    for subsection in data['subsections']:
        sub_id = subsection['id']
        sub_name = subsection['name']
        
        # Создаем папку подраздела (например, 5.1_Robotics)
        # Для простоты используем формат ID_Name
        sub_dir_name = f"{sub_id}_{sub_name}"
        sub_path = os.path.join(base_dir, sub_dir_name)
        os.makedirs(sub_path, exist_ok=True)
        
        # Создаем README для подраздела
        with open(os.path.join(sub_path, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(f"# {sub_name}\n\nTaxonomy ID: {sub_id}\n\n")
            f.write("## Tasks\n")

        for child in subsection.get('children', []):
            child_id = child['id']
            child_name = child['name']
            
            # Если есть список задач (листья)
            tasks = child.get('tasks', [])
            
            if tasks:
                # Создаем папку для группы задач (например, 5.1.1_Motion_Control)
                child_dir_name = f"{child_id}_{child_name}"
                child_path = os.path.join(sub_path, child_dir_name)
                os.makedirs(child_path, exist_ok=True)
                
                # README для группы
                with open(os.path.join(child_path, 'README.md'), 'w', encoding='utf-8') as f:
                    f.write(f"# {child_name}\n\nParent: {sub_name}\nID: {child_id}\n")
                    f.write("\n## Specific Tasks\n")

                # Создаем папки для каждой конкретной задачи
                for task in tasks:
                    task_path = os.path.join(child_path, task)
                    os.makedirs(task_path, exist_ok=True)
                    
                    # Создаем пустые файлы-заглушки
                    files_to_create = ['__init__.py', 'README.md', 'architectures.json', 'metadata.yaml']
                    for file in files_to_create:
                        file_path = os.path.join(task_path, file)
                        if not os.path.exists(file_path):
                            with open(file_path, 'w', encoding='utf-8') as f:
                                if file == 'README.md':
                                    f.write(f"# {task}\n\nStatus: Pending Definition\n")
                                elif file == 'architectures.json':
                                    f.write('{\n  "architectures": [],\n  "notes": "Define applicable NN architectures here"\n}')
                                elif file == 'metadata.yaml':
                                    f.write(f"task_id: {task}\nparent_id: {child_id}\nstatus: draft\n")
                    
                    # Добавляем задачу в README родителя
                    with open(os.path.join(child_path, 'README.md'), 'a', encoding='utf-8') as f:
                        f.write(f"- [ ] {task}\n")

        print(f"Processed: {sub_dir_name}")

    print("\nStructure generation complete!")
    print("Check the Tasks/Control directory.")

if __name__ == "__main__":
    create_structure()