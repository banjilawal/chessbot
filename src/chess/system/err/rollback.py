# src/chess/system/err/rollback.py

"""
Module: chess.system.err.rollback
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


from chess.system.err import ChessException

__all__ = [
    "RollbackException",
    "RollbackFailedException"
]


class RollbackException(ChessException):
    """Base class for rollback-related errors."""
    DEFAULT_CODE = "ROLLBACK"
    DEFAULT_MESSAGE = "Operation rolled back due to failure in update consistency."


class RollbackFailedException(RollbackException):
    ERROR_CODE = "ROLLBACK_FAILED_ERROR"
    DEFAULT_MESSAGE = "Rollback failed."
