# src/chess/system/collection/operation/exception.py

"""
Module: chess.system.operation.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionException, OperationException

__all__ = [
    # ======================# COLLECTION_OPERATION_FAILURE #======================#
    "CollectionOperationException",
]


# ======================# COLLECTION_OPERATION_FAILURE #======================#
class CollectionOperationException(CollectionException, OperationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wraps collection operation debug exceptions to create an exception chain.

    # PARENT:
        *   CollectionOperation
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COLLECTION_OPERATION_FAILURE"
    DEFAULT_MESSAGE = "Calculation failed."