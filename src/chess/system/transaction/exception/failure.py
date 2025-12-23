# src/chess/system/transaction/failure.py

"""
Module: chess.system.transaction.failure
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""
from chess.system import TransactionException


__all__ = [
    # ======================# OPERATION EXCEPTION #======================#
    "OperationFailedException",
]




# ======================# OPERATION EXCEPTION #======================#
class OperationFailedException(TransactionException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate That  a method that returns a Result object caught an unhandled exception in its try-catch-finally block.

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