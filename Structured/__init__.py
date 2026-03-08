"""
Structured Category Module Initialization.
Природа: Данные с явной структурой и связями
Операции: Анализ связей, прогнозирование, кластеризация
"""

from .TabularData import TabularData
from .TimeSeries import TimeSeries
from .Graphs import Graphs
from .Biology import Biology
from .MedicalData import MedicalData
from .Hierarchies import Hierarchies

__all__ = [
    "TabularData",
    "TimeSeries",
    "Graphs",
    "Biology",
    "MedicalData",
    "Hierarchies"
]
