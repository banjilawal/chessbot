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
    1.  Indicate there was an attempt to build a DataResult that did not contain neither a payload nor an exception.
        Data transactions are
            *   insertion
            *   deletions
            *   updates
            *   calculations
        Data transactions either succeed or fail.

    # PARENT:
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    ERROR_CODE = "EMPTY_DATA_RESULT_ERROR"
    DEFAULT_MESSAGE = "DataResult must contain either a payload or an exception. It cannot be empty."