"""
5.1.1 Motion Control and Kinematics
Управление движением и кинематика

Основной модуль раздела 5.1.1, объединяющий все подразделы планирования движения
"""

from . import (
    # Подразделы будут добавлены по мере заполнения
)

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SECTION_NAME_RU = "Управление движением и кинематика"
SECTION_NAME_EN = "Motion Control and Kinematics"

# Subsections (will be populated as they are created)
SUBSECTIONS = [
    {
        "id": "01",
        "name_ru": "Планирование траекторий",
        "name_en": "Trajectory Planning",
        "module": "01_Trajectory_Planning"
    },
    {
        "id": "02", 
        "name_ru": "Планирование путей",
        "name_en": "Path Planning",
        "module": "02_Path_Planning"
    },
    {
        "id": "03",
        "name_ru": "Управление положением",
        "name_en": "Position Control",
        "module": "03_Position_Control"
    },
    {
        "id": "04",
        "name_ru": "Управление скоростью",
        "name_en": "Velocity Control",
        "module": "04_Velocity_Control"
    },
    {
        "id": "05",
        "name_ru": "Управление силой и моментом",
        "name_en": "Force/Torque Control",
        "module": "05_Force_Torque_Control"
    },
    {
        "id": "06",
        "name_ru": "Импедансное и адмиттансное управление",
        "name_en": "Impedance/Admittance Control",
        "module": "06_Impedance_Admittance_Control"
    },
    {
        "id": "07",
        "name_ru": "Гибридное управление позиция/сила",
        "name_en": "Hybrid Position/Force Control",
        "module": "07_Hybrid_Position_Force_Control"
    },
    {
        "id": "08",
        "name_ru": "Обратная кинематика",
        "name_en": "Inverse Kinematics",
        "module": "08_Inverse_Kinematics"
    },
    {
        "id": "09",
        "name_ru": "Обратная динамика",
        "name_en": "Inverse Dynamics",
        "module": "09_Inverse_Dynamics"
    },
    {
        "id": "10",
        "name_ru": "Адаптивное управление движением",
        "name_en": "Adaptive Motion Control",
        "module": "10_Adaptive_Motion_Control"
    }
]


def get_section_info():
    """Получить информацию о разделе"""
    return {
        "taxonomy_section": TAXONOMY_SECTION,
        "section_name_ru": SECTION_NAME_RU,
        "section_name_en": SECTION_NAME_EN,
        "total_subsections": len(SUBSECTIONS),
        "subsections": SUBSECTIONS
    }


def get_completed_subsections():
    """Получить список заполненных подразделов"""
    completed = []
    for subsection in SUBSECTIONS:
        try:
            module_name = subsection["module"]
            module = __import__(
                f".{module_name}", 
                fromlist=[""]
            )
            if hasattr(module, "get_database") or hasattr(module, "summary"):
                completed.append({
                    **subsection,
                    "status": "completed"
                })
            else:
                completed.append({
                    **subsection,
                    "status": "in_progress"
                })
        except (ImportError, AttributeError):
            completed.append({
                **subsection,
                "status": "not_started"
            })
    return completed


def get_full_summary():
    """Получить полную сводку по разделу"""
    return {
        "section_info": get_section_info(),
        "completion_status": get_completed_subsections()
    }


# Print summary on import
if __name__ == "__main__":
    import json
    print(json.dumps(get_full_summary(), indent=2, ensure_ascii=False))
