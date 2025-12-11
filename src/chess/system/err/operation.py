# src/chess/system/err/operation.py

"""
Module: chess.system.err.operation
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    # ======================# OPERATION EXCEPTION #======================#
    "OperationFailedException",
]




# ======================# OPERATION EXCEPTION #======================#
class OperationFailedException(ChessException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a method that returns a Result object caught an unhandled exception in its try-catch-finally block.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "OPERATION_ERROR"
    DEFAULT_MESSAGE = "Operation failed."