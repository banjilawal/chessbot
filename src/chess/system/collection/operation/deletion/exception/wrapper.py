# src/chess/system/collection/operation/deletion/exception/wrapper.py

"""
Module: chess.system.collection.operation.deletion.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationException

__all__ = [
    # ======================# DELETION_FAILURE #======================#
    "DeletionException",
]


# ======================# DELETION_FAILURE #======================#
class DeletionException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the deletion failed.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DELETION_FAILURE"
    DEFAULT_MESSAGE = "Deletion failed."
