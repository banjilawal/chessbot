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
    "FailedOperationRolledBackException",
]


#======================# ROLL_BACK_EXCEPTION EXCEPTION #======================#
class RollbackException(ChessException):
    """Base class for rollback-related errors."""
    DEFAULT_CODE = "ROLLBACK_ERROR"
    DEFAULT_MESSAGE = "Rollback exception raised."


#======================# FAILED_OPERATION ROLLED_BACK EXCEPTION #======================#
class FailedOperationRolledBackException(RollbackException):
    """
    Raised when an operation fails. The changes are rolled back. Then the exception
    is raised. Use this exception in production instead of the base RollbackException.
    """
    ERROR_CODE = "FAILED_OPERATION_ROLLED_BACK_ERROR"
    DEFAULT_MESSAGE = (
        "An operation failed. The data was rolled back to its last good state "
        "before this exception was raised."
    )


#======================# ROLL_BACK_EXCEPTION EXCEPTION #======================#
class RollbackException(ChessException):
    """Base class for rollback-related errors."""
    DEFAULT_CODE = "ROLLBACK_ERROR"
    DEFAULT_MESSAGE = "Rollback exception raised."


#======================# FAILED_OPERATION ROLLED_BACK EXCEPTION #======================#
class FailedOperationRolledBackException(RollbackException):
    """
    Raised when an operation fails. The changes are rolled back. Then the exception
    is raised. Use this exception in production instead of the base RollbackException.
    """
    ERROR_CODE = "FAILED_OPERATION_ROLLED_BACK_ERROR"
    DEFAULT_MESSAGE = (
        "An operation failed. The data was rolled back to its last good state "
        "before this exception was raised."
    )
