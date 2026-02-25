# src/chess/system/collection/operation/computation/exception/wrapper.py

"""
Module: chess.system.collection.operation.computation.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionOperationException

__all__ = [
    # ======================# COMPUTATION_FAILURE #======================#
    "ComputationException",
]


# ======================# COMPUTATION_FAILURE #======================#
class ComputationException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the computation failed.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "COMPUTATION_FAILURE"
    MSG = "Computation failed."
