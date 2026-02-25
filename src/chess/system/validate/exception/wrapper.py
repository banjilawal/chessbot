# src/chess/system/validate/exception/wrapper.py

"""
Module: chess.system.validate.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationException

__all__ = [
    # ======================# VALIDATION_FAILURE #======================#
    "ValidationException",
]


#======================# VALIDATION_FAILURE #======================#
class ValidationException(OperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes which check the candidate failed.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "DELETION_FAILURE"
    MSG = "Deletion failed."
