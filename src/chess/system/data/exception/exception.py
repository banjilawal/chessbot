# src/chess/system/data/service/exception.py

"""
Module: chess.system.data.service.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import NullException, ServiceException

__all__ = [
    # ====================== DATA_SERVICE_EXCEPTION #======================#
    "DataServiceException",
    # ====================== REMOVING_NULL_DATA EXCEPTION #======================#
    "RemovingNullDataException",
    # ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
    "PoppingEmptyStackException",
]


# ====================== DATA_SERVICE_EXCEPTION #======================#
class DataServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by DataServices.
    2.  Wraps unhandled exceptions that hit the try-finally block of a DataService method.

    # PARENT
        *   ServiceException

    # PROVIDES:
    DataServiceException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "DataService raised an exception."


# ====================== REMOVING_NULL_DATA EXCEPTION #======================#
class RemovingNullDataException(DataServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate someone is trying to remove an item that does not exist in a collection.

    # PARENT
        *   DataServiceException
        *   NullException

    # PROVIDES:
    RemovingNullDataException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "REMOVING_NULL_DATA_ERROR"
    DEFAULT_MESSAGE = "Cannot remove data that does not exist in the set."


# ====================== POPPING_EMPTY_STACK EXCEPTION #======================#
class PoppingEmptyStackException(DataServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicates an attempt to pop an empty stack.

    # PARENT
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