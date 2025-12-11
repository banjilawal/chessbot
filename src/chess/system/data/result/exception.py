# src/chess/system/data/result/exception.py

"""
Module: chess.system.data.result.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ResultException

__all__ = [
    "EmptyDataResultException"
]

# ====================== EMPTY_DATA_RESULT EXCEPTION #======================#
class EmptyDataResultException(ResultException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicates an attempt to build a DataResult  which does not contain neither a payload nor an exception.
    Data transactions are solely insertions, deletions, updates, and calculations. Data transactions either
    put something into a collection, remove something from it, or generate a new value from the existing data.
    All these operations either succeed or fail.

    # PARENT:
        *   ResultException

    # PROVIDES:
    EmptyDataResultException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EMPTY_DATA_RESULT_ERROR"
    DEFAULT_MESSAGE = "DataResult must contain either a payload or an exception. It cannot be empty."