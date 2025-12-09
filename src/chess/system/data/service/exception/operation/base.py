# src/chess/system/data/service/exception/operation/base.py

"""
Module: chess.system.data.service.exception.operation.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import ServiceException

__all__ = [
    # ====================== DATA_SERVICE_EXCEPTION #======================#
    "DataServiceException",
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