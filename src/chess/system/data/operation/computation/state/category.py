# src/chess/system/data/operation/computation/state/category.py

"""
Module: chess.system.data.operation.computation.state.category
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import auto, Enum


class ComputationResultEnum(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    EMPTY = auto(),
    TIMED_OUT = auto(),
    NO_SEARCH_HITS = auto(),
    NOTHING_TO_DELETE = auto(),
    CURRENT_AND_PREVIOUS_THE_SAME = auto(),