# src/chess/system/data/collection/stack/service/unique/exception/catchall.py

"""
Module: chess.system.data.collection.stack.service.unique.exception.catchall
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
    1.  Parent of exception raised by DatabaseService objects.
    2.  Wraps an exception that hits the try-finally block of an DatabaseService object.

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
    DEFAULT_MESSAGE = "DatabaseService raised an exception."