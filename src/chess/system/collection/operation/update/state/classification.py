# src/chess/system/collection/operation/update/state/classification.py

"""
Module: chess.system.collection.operation.update.state.classification
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import Enum, auto


class UpdateResultEnum(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    ORIGINAL_AND_UPDATE_ARE_SAME = auto(),