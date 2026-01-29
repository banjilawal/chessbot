# src/chess/system/data/operation/insertion/exception/wrapper.py

"""
Module: chess.system.data.operation.insertion.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DatasetException, OperationFailedException

__all__ = [
    # ======================# INSERTION_FAILURE EXCEPTION #======================#
    "InsertionFailedException",
]


# ======================# INSERTION_FAILURE EXCEPTION #======================#
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
