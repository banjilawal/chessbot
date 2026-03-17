# src/logic/system/collection/stack/exception/empty.py

"""
Module: logic.system.collection.stack.exception.empty
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from logic.system import StackServiceException

__all__ = [
    # ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
    "PoppingEmptyStackException",
]

# ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
class PoppingEmptyStackException(StackServiceException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    Indicate there was an attempt to pop an empty stack.

    Super Class:
        *   StackServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_STACK_EXCEPTION"
    MSG = "Stack is empty. There is nothing to pop."