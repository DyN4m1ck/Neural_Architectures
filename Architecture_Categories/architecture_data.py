"""
Module containing architecture categories data as general parameters.
"""
from .FeedForward import FEEDFORWARD_ARCHITECTURES
# Architecture categories data

# Additional general parameters
DEFAULT_CATEGORY_NAMES = [category["name"] for category in FEEDFORWARD_ARCHITECTURES]
CATEGORY_COUNT = len(FEEDFORWARD_ARCHITECTURES)