"""
Module containing architecture categories data as general parameters.
"""
from Architecture_Categories import FeedForward
# Architecture categories data


# Additional general parameters
DEFAULT_CATEGORY_NAMES = [category["name"] for category in FeedForward.ARCHITECTURE_CATEGORIES]
CATEGORY_COUNT = len(FeedForward.ARCHITECTURE_CATEGORIES)