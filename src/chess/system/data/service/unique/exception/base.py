# src/chess/system/data/service/unique/exception.base.py

"""
Module: chess.system.data.service.unique.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    #======================# UNIQUE_DATA_SERVICE EXCEPTION #======================#
    "UniqueDataServiceException",
]


#======================# UNIQUE_DATA_SERVICE EXCEPTION #======================#
class UniqueDataServiceException(DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by UniqueDataService objects.
    2.  Wraps unhandled exception that hit the try-finally block of an UniqueDataService object.

    # PARENT:
        *   DataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueDataService raised an exception."