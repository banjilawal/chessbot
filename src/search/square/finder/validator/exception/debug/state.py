# src/logic/square/validation/exception/model.py

"""
Module: logic.square.validation.exception.square
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# SQUARE_SQUARE_STATE EXCEPTION #======================#
    "SquareSquareStateException",
]

from system import DebugException, SquareException

# ======================# SQUARE_SQUARE_STATE EXCEPTION #======================#
class SquareSquareStateException(DebugException, SquareException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failure ValidationResult was returned because the validation rank was square instead of
        being a SquareState.

    Super Class:
        *   DebugException
        *   SquareException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_SQUARE_STATE"
    MSG = "SquareState validation failed: The rank cannot be square."