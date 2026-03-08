"""
Module for Logistics subcategory.
Part of CONTROL category - Decision making over time
"""

class Logistics:
    """Category: LOGISTICS"""

    name = "Логистика и цепи поставок"
    description = "Оптимизация маршрутов, управление запасами, прогнозирование спроса"

    subcategories = [
        {
            "name": "Оптимизация маршрутов",
            "description": "Route optimization - finding optimal paths for delivery and transportation"
        },
        {
            "name": "Управление запасами",
            "description": "Inventory management - optimizing stock levels and replenishment"
        },
        {
            "name": "Прогнозирование спроса",
            "description": "Demand forecasting - predicting future demand for products and services"
        }
    ]

__all__ = ["Logistics"]