# src/chess/system/data/service/exception/base.py

"""
Module: chess.system.data.service.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import DatasetException, ServiceException

__all__ = [
    # ====================== DATA_SERVICE EXCEPTION #======================#
    "DataServiceException",
]


# ====================== DATA_SERVICE EXCEPTION #======================#
class DataServiceException(DatasetException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by DataServices.
    2.  Wraps an exception that hits the try-finally block of a ListService method.

    # PARENT:
        *   DatasetException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "ListService raised an exception."