# src/chess/system/data/result/classif  .py

"""
Module: chess.system.data.result.classification
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import auto, Enum


class DataResultEnum(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    EMPTY = auto(),
    TIMED_OUT = auto(),
    CURRENT_AND_PREVIOUS_THE_SAME = auto(),