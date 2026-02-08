# src/chess/system/collection/operation/computation/exception/wrapper.py

"""
Module: chess.system.collection.operation.computation.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionException, OperationFailedException

__all__ = [
    # ======================# CALCULATION_FAILURE EXCEPTION #======================#
    "ComputationFailedException",
]


# ======================# CALCULATION_FAILURE EXCEPTION #======================#
class ComputationFailedException(CollectionException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a calculation operation failed. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   DataException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CALCULATION_FAILURE"
    DEFAULT_MESSAGE = "Calculation failed."
