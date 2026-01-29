# src/chess/system/collectionoperation/deletion/exception/wrapper.py

"""
Module: chess.system.collection.operation.deletion.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DatasetException, OperationFailedException

__all__ = [
    # ======================# DELETION_FAILURE EXCEPTION #======================#
    "DeletionFailedException",
]


# ======================# DELETION_FAILURE EXCEPTION #======================#
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
