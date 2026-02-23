# src/chess/system/err/operation.py

"""
Module: chess.system.err.operation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# OPERATION_FAILURE #======================#
    "OperationException",
]

from chess.system import WrapperException


# ======================# OPERATION_FAILURE #======================#
class OperationException(WrapperException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate what operation failed.
    2.  Contains Layer 1 of the exception chain.
    2.  Encapsulate DebugException raised by the failure's source.

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
    

