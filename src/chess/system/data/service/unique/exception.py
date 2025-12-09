# src/chess/system/data/service/unique/exception.py

"""
Module: chess.system.data.service.unique.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    #======================# UNIQUE_DATA_SERVICE EXCEPTION SUPER CLASS #======================#
    "UniqueDataServiceException",
    #======================# ADDING_DUPLICATE_DATA_EXCEPTION  #======================#
    "AddingDuplicateDataException",
]


#======================# UNIQUE_DATA_SERVICE EXCEPTION SUPER CLASS #======================#
class UniqueDataServiceException(DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by UniqueDataService objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an UniqueDataService object.

    # PARENT
        *   DataServiceException

    # PROVIDES:
    UniqueDataServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueDataService raised an exception."


#======================# ADDING_DUPLICATE_DATA_EXCEPTION  #======================#
class AddingDuplicateDataException(UniqueDataServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate an attempt was made to add a duplicate item o a collection that only allows uniques.

    # PARENT
        *   UniqueDataServiceException

    # PROVIDES:
    AddingDuplicateDataException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_DATA_ERROR"
    DEFAULT_MESSAGE = "The data already exists. Adding duplicate data is not allowed."
