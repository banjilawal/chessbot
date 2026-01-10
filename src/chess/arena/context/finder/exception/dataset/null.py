# src/chess/arena/context/finder/exception/dataset/null.py

"""
Module: chess.arena.context.finder.exception.dataset.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.arena import ArenaException
from chess.system import NullDatasetException

_all__ = [
    # ======================# ARENA_DATASET_NULL EXCEPTION #======================#
    "ArenaDatasetNullException",
]


# ======================# ARENA_DATASET_NULL EXCEPTION #======================#
class ArenaDatasetNullException(ArenaException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that ArenaContext validation failed because the candidate was null.

    # PARENT:
        *   ArenaDatasetNullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "Arena dataset cannot be null."