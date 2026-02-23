# src/chess/system/collection/operation/exception.py

"""
Module: chess.system.operation.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import OperationException

__all__ = [
    # ======================# COLLECTION_OPERATION_FAILURE #======================#
    "CollectionOperationException",
]


# ======================# COLLECTION_OPERATION_FAILURE #======================#
class CollectionOperationException(OperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate what Collection Operation failed.
    2.  Encapsulate the DebugException which describes the failure condition.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COLLECTION_OPERATION_FAILURE"
    DEFAULT_MESSAGE = "Calculation operation failed."