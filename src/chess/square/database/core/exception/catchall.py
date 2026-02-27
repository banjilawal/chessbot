# src/chess/square/database/core/super.py

"""
Module: chess.square.database.core.super
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_STACK_SERVICE EXCEPTION #======================#
    "SquareStackServiceException",
]

from chess.system import StackServiceException


# ======================# SQUARE_STACK_SERVICE EXCEPTION #======================#
class SquareStackServiceException(StackServiceException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in SquareStackService.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_STACK_EXCEPTION"
    MSG = "SquareStackService raised an exception."