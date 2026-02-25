# src/chess/system/collection/operation/update/exception/wrapper.py

"""
Module: chess.system.collection.operation.update.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationException

__all__ = [
    # ======================# UPDATE_FAILURE #======================#
    "UpdateException",
]


# ======================# UPDATE_FAILURE #======================#
class UpdateException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the update failed.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "UPDATE_FAILURE"
    MSG = "Update failed."