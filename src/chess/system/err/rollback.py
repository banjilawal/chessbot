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
]


#======================# FAILED_OPERATION_ROLLED_BACK EXCEPTION #======================#
class RollbackException(ChessException):
    """Base class for rollback-related errors."""
    DEFAULT_CODE = "FAILED_OPERATION_ROLLED_BACK"
    DEFAULT_MESSAGE = "The operation failed. The operation was rolled back before this exception was raised"
