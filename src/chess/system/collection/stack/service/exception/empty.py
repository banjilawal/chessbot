# src/chess/system/collection/exception/pop.py

"""
Module: chess.system.collection.service.exception.pop
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import StackServiceException

__all__ = [
    # ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
    "PoppingEmptyStackException",
]

# ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
class PoppingEmptyStackException(StackServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate there was an attempt to pop an empty stack.

    # PARENT:
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_STACK_ERROR"
    DEFAULT_MESSAGE = "Stack is empty. There is nothing to pop."