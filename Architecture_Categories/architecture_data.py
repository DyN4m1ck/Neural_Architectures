"""
Module containing architecture categories data as general parameters.
"""
from .FeedForward import ARCHITECTURE_CATEGORIES
# Architecture categories data


# Additional general parameters
DEFAULT_CATEGORY_NAMES = [category["name"] for category in ARCHITECTURE_CATEGORIES]
CATEGORY_COUNT = len(ARCHITECTURE_CATEGORIES)