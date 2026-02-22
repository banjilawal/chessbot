# src/chess/system/err/operation.py

"""
Module: chess.system.err.operation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# OPERATION_FAILURE #======================#
    "OperationFailedException",
]

from chess.system import WrapperException


# ======================# OPERATION_FAILURE #======================#
class OperationFailedException(WrapperException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Subclass of Wrapper exception. See parent class for responsibilities.

    # PARENT:
        *   WrapperException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "OPERATION_FAILURE"
    DEFAULT_MESSAGE = "Operation failed."