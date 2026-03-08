"""
Position Control Module
Управление положением (Position Control) - Section 5.1.1

Precise control of end-effector or platform position using neural architectures.
"""

from .architectures import (
    MLPPositionControl,
    RNNPositionControl,
    PIDNeuralEnhancement,
    TransformerPositionControl
)

from .tasks import (
    PositionControlTask,
    PrecisionPositionControl,
    MultiAxisPositionControl,
    AdaptivePositionControl
)

from .database import PositionControlDatabase

__all__ = [
    'MLPPositionControl',
    'RNNPositionControl',
    'PIDNeuralEnhancement',
    'TransformerPositionControl',
    'PositionControlTask',
    'PrecisionPositionControl',
    'MultiAxisPositionControl',
    'AdaptivePositionControl',
    'PositionControlDatabase'
]

TAXONOMY_SECTION = "5.1.1.3"
SECTION_NAME = "Position Control"
DESCRIPTION = "Precise control of end-effector or platform position"