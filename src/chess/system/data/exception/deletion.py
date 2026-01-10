# src/chess/system/data/exception/deletion.py

"""
Module: chess.system.data.exception.deletion
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import DatasetException, OperationFailedException

__all__ = [
    # ======================# DELETION_FAILED EXCEPTION #======================#
    "DeletionFailedException",
]


# ======================# DELETION_FAILED EXCEPTION #======================#
class DeletionFailedException(DatasetException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a deletion operation failed. The encapsulated
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
    ERROR_CODE = "DELETION_FAILED"
    DEFAULT_MESSAGE = "Deletion failed."
