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
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Shows what type of class method experienced the error.
    2.  Encapsulates the DebugException which identifies the method's code block that raised the error.
    3.  Middle part of the 3-layer exception chain. Should only contain a DebugException.

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
    

