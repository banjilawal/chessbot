# src/chess/system/collection/operation/insertion/exception/wrapper.py

"""
Module: chess.system.collection.operation.insertion.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationFailedException

__all__ = [
    # ======================# INSERTION_FAILURE #======================#
    "InsertionException",
]


# ======================# INSERTION_FAILURE #======================#
class InsertionException(CollectionOperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a insertion operation failed. The exception chain 
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
    ERROR_CODE = "INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Insertion failed."
