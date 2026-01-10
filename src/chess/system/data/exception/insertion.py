# src/chess/system/data/exception/insertion.py

"""
Module: chess.system.data.exception.insertion
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import DatasetException, OperationFailedException

__all__ = [
    # ======================# INSERTION_FAILED EXCEPTION #======================#
    "InsertionFailedException",
]


# ======================# INSERTION_FAILED EXCEPTION #======================#
class InsertionFailedException(DatasetException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a insertion operation failed. The encapsulated 
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   DataException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "INSERTION_FAILED"
    DEFAULT_MESSAGE = "Insertion failed."
