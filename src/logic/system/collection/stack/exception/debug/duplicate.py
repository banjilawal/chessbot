# src/logic/system/collection/stack/exception/duplicate.py

"""
Module: logic.system.collection.stack.exception.duplicate
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from logic.system import DebugException

__all__ = [
    #======================# CANNOT_ADD_DUPLICATE_ITEM EXCEPTION  #======================#
    "AddingDuplicateItemException",
]


#======================# CANNOT_ADD_DUPLICATE_ITEM EXCEPTION  #======================#
class AddingDuplicateItemException(DebugException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    Indicate an attempt was made to add a duplicate item o a collection that only allows uniques.

    Super Class:
        *   CollectionException

    Provides:

    
    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "CANNOT_ADD_DUPLICATE_ITEM ERROR"
    MSG = "The data already exists. Adding duplicate data is not allowed."
