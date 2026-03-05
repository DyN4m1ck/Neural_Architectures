"""
Анализ уязвимостей (Code Security)
Обнаружение потенциальных уязвимостей в коде
"""

NAME = "Анализ уязвимостей"
DESCRIPTION = "Обнаружение потенциальных уязвимостей в коде"

TASKS = [
    {
        "name": "Статический анализ безопасности",
        "description": "Поиск уязвимостей без выполнения кода"
    },
    {
        "name": "SQL Injection detection",
        "description": "Обнаружение уязвимостей к SQL-инъекциям"
    },
    {
        "name": "XSS detection",
        "description": "Обнаружение跨站脚本 уязвимостей"
    },
    {
        "name": "Buffer overflow detection",
        "description": "Поиск переполнений буфера"
    },
    {
        "name": "Security pattern matching",
        "description": "Поиск опасных паттернов в коде"
    }
]
