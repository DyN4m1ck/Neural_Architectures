"""
Module containing architecture categories data as general parameters.
"""
from . import FeedForward
# Architecture categories data

ARCHITECTURE_CATEGORIES = FeedForward.ARCHITECTURE_CATEGORIES

# Additional general parameters
DEFAULT_CATEGORY_NAMES = [category["name"] for category in FeedForward.ARCHITECTURE_CATEGORIES]
CATEGORY_COUNT = len(FeedForward.ARCHITECTURE_CATEGORIES)