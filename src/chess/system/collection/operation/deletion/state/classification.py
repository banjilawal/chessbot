# src/chess/system/data/operation/deletion/state/classification.py

"""
Module: chess.system.data.operation.deletion.state.classification
Author: Banji Lawal
Created: 2026-01-25
Version: 1.0.0
"""

from enum import auto, Enum


class DeletionResultEnum(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_TO_DELETE = auto(),