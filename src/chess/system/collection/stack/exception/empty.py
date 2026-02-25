# src/chess/system/collection/stack/exception/empty.py

"""
Module: chess.system.collection.stack.exception.empty
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
    ERR_CODE = "POPPING_EMPTY_STACK_ERROR"
    MSG = "Stack is empty. There is nothing to pop."