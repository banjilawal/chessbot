# src/chess/system/collection/stack/exception/base.py

"""
Module: chess.system.collection.stack.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import CollectionException, ServiceException

__all__ = [
    # ====================== STACK_SERVICE EXCEPTION #======================#
    "StackException",
]


# ====================== STACK_SERVICE EXCEPTION #======================#
class StackException(CollectionException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by StackServices.
    2.  Wraps an exception that hits the try-finally block of a StackService method.

    # PARENT:
        *   CollectionException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "StackService raised an exception."