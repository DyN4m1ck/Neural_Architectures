"""
Trajectory Planning - Планирование траекторий

Раздел 5.1.1 Управление движением и кинематика

Природа задач:
- Планирование оптимальных траекторий движения с учётом динамики, препятствий и ограничений
- Генерация плавных и выполнимых траекторий для роботов и автономных систем
- Баланс между оптимальностью, безопасностью и вычислительной эффективностью

Основные задачи:
- Trajectory optimization (оптимизация траектории)
- Motion planning in dynamic environments (планирование в динамической среде)
- Time-optimal trajectory generation (временно-оптимальные траектории)
- Smooth trajectory generation (сглаженные траектории)
- Constraint-aware trajectory planning (учёт ограничений)

Применяемые архитектуры нейронных сетей:
- LSTM/GRU - для временных зависимостей и предсказания состояний
- Transformer - для долгосрочного планирования с механизмами внимания
- Physics-Informed Neural Networks (PINN) - для учёта физических законов
- Neural ODEs - для непрерывного представления траекторий
- Deep Reinforcement Learning (PPO, SAC, TD3) - для обучения с подкреплением

Интеграция с классическими методами:
- Model Predictive Control (MPC)
- Optimal control (LQR, iLQR)
- Sampling-based planners (RRT*, PRM*)
- Optimization-based planners (CHOMP, STOMP)
"""

from .architectures import (
    get_trajectory_architectures,
    ArchitectureCatalog
)
from .tasks import (
    get_trajectory_tasks,
    TaskCatalog
)
from .database import (
    TrajectoryPlanningDatabase,
    get_database
)

__all__ = [
    'get_trajectory_architectures',
    'ArchitectureCatalog',
    'get_trajectory_tasks',
    'TaskCatalog',
    'TrajectoryPlanningDatabase',
    'get_database'
]

# Taxonomy information
TAXONOMY_SECTION = "5.1.1"
SUBSECTION = "01"
NAME_RU = "Планирование траекторий"
NAME_EN = "Trajectory Planning"
