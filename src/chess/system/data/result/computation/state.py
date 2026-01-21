# src/chess/system/data/result/calculation/state.py

"""
Module: chess.system.data.result.calculation.state
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import auto, Enum


class CalculationState(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),