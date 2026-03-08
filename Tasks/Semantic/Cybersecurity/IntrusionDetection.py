"""
Обнаружение вторжений
Системы обнаружения несанкционированного доступа (IDS)
"""

NAME = "Обнаружение вторжений"
DESCRIPTION = "Системы обнаружения несанкционированного доступа (IDS)"

TASKS = [
    {
        "name": "Network IDS",
        "description": "Обнаружение атак в сетевом трафике"
    },
    {
        "name": "Host-based IDS",
        "description": "Мониторинг отдельных хостов"
    },
    {
        "name": "Anomaly detection",
        "description": "Обнаружение аномального поведения"
    },
    {
        "name": "Signature-based detection",
        "description": "Обнаружение по известным паттернам атак"
    },
    {
        "name": "Intrusion prevention",
        "description": "Активное предотвращение атак (IPS)"
    }
]
