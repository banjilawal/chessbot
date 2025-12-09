# src/chess/system/data/service/unique/exception.py

"""
Module: chess.system.data.service.unique.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import UniqueDataServiceException

__all__ = [
    #======================# ADDING_DUPLICATE_DATA_EXCEPTION  #======================#
    "AddingDuplicateDataException",
]


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
