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
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a computation operation failed. The exception chain 
        traces the ultimate source of failure.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Computation failed."
