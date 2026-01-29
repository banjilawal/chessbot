# src/chess/system/collectionservice/unique/exception.duplicate.py

"""
Module: chess.system.collection.service.unique.exception.duplicate
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DatabaseException

__all__ = [
    #======================# ADDING_DUPLICATE_DATA_EXCEPTION  #======================#
    "AddingDuplicateDataException",
]


#======================# ADDING_DUPLICATE_DATA_EXCEPTION  #======================#
class AddingDuplicateDataException(DatabaseException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate an attempt was made to add a duplicate item o a collection that only allows uniques.

    # PARENT:
        *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_DATA_ERROR"
    DEFAULT_MESSAGE = "The data already exists. Adding duplicate data is not allowed."
