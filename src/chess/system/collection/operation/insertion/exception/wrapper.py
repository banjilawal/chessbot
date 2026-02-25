# src/chess/system/collection/operation/insertion/exception/wrapper.py

"""
Module: chess.system.collection.operation.insertion.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationException

__all__ = [
    # ======================# INSERTION_FAILURE #======================#
    "InsertionException",
]


# ======================# INSERTION_FAILURE #======================#
class InsertionException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the insertion failed.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "INSERTION_FAILURE"
    MSG = "Insertion failed."
