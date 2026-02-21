# src/chess/system/collection/operation/deletion/exception/wrapper.py

"""
Module: chess.system.collection.operation.deletion.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationFailedException

__all__ = [
    # ======================# DELETION_FAILURE #======================#
    "DeletionException",
]


# ======================# DELETION_FAILURE #======================#
class DeletionException(CollectionOperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a deletion operation failed. The exception chain 
        traces the ultimate source of failure.

    # PARENT:
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DELETION_FAILURE"
    DEFAULT_MESSAGE = "Deletion failed."
