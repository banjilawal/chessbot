# src/chess/system/collection/exception/base.py

"""
Module: chess.system.collection.service.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import DatasetException, ServiceException

__all__ = [
    # ====================== DATA_SERVICE EXCEPTION #======================#
    "StackServiceException",
]


# ====================== DATA_SERVICE EXCEPTION #======================#
class StackServiceException(DatasetException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by DataServices.
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
    ERROR_CODE = "DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "StackService raised an exception."