# src/chess/system/data/service/exception/operation/pop.py

"""
Module: chess.system.data.service.exception.operation.pop
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import DataServiceException

__all__ = [
    # ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
    "PoppingEmptyStackException",
]

# ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
class PoppingEmptyStackException(DataServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicates an attempt to pop an empty stack.

    # PARENT:
        *   DataServiceException

    # PROVIDES:
    PoppingEmptyStackException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_STACK_ERROR"
    DEFAULT_MESSAGE = "Stack is empty. There is nothing to pop."