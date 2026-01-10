# src/chess/system/data/exception/calculation.py

"""
Module: chess.system.data.exception.calculation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import DatasetException, OperationFailedException

__all__ = [
    # ======================# CALCULATION_FAILED EXCEPTION #======================#
    "CalculationFailedException",
]


# ======================# CALCULATION_FAILED EXCEPTION #======================#
class CalculationFailedException(DatasetException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a calculation operation failed. The encapsulated exceptions create
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
    ERROR_CODE = "CALCULATION_FAILED"
    DEFAULT_MESSAGE = "Calculation failed."
