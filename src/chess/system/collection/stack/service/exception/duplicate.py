# src/chess/system/collection/unique/exception.duplicate.py

"""
Module: chess.system.collection.service.unique.exception.duplicate
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionException

__all__ = [
    #======================# CANNOT_ADD_DUPLICATE_ITEM EXCEPTION  #======================#
    "CannotAddDuplicateException",
]


#======================# CANNOT_ADD_DUPLICATE_ITEM EXCEPTION  #======================#
class CannotAddDuplicateException(CollectionException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate an attempt was made to add a duplicate item o a collection that only allows uniques.

    # PARENT:
        *   CollectionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CANNOT_ADD_DUPLICATE_ITEM ERROR"
    DEFAULT_MESSAGE = "The data already exists. Adding duplicate data is not allowed."
