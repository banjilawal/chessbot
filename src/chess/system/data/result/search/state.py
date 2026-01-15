# src/chess/system/data/result/search/state.py

"""
Module: chess.system.data.result.search.state
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import auto, Enum


class SearchState(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    EMPTY = auto(),
    TIMED_OUT = auto(),