# src/chess/system/collection/operation/update/exception/wrapper.py

"""
Module: chess.system.collection.operation.update.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationFailedException

__all__ = [
    # ======================# UPDATE_FAILURE #======================#
    "UpdateException",
]


# ======================# UPDATE_FAILURE #======================#
class UpdateException(CollectionOperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a update operation failed. The exception chain 
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
    ERROR_CODE = "UPDATE_FAILURE"
    DEFAULT_MESSAGE = "Update failed."