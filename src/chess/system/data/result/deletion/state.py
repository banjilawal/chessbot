# src/chess/system/data/result/deletion/state.py

"""
Module: chess.system.data.result.deletion.state
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import auto, Enum


class DeletionState(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    EMPTY = auto(),
    TIMED_OUT = auto(),