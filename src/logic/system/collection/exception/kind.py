# src/logic/system/collection/exception/kind.py

"""
Module: logic.system.collection.exception.kind
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from logic.system import CollectionException

__all__ = [
    # ====================== WRONG_COLLECTION_TYPE EXCEPTION #======================#
    "WrongCollectionTypeException",
]


# ====================== WRONG_COLLECTION_TYPE EXCEPTION #======================#
class WrongCollectionTypeException(CollectionException):
    """
    Role:Exception Work
    
    Responsibilities:
    1.  The Collection contains the wrong type of data.
    
    Super Class:
     *   CollectionException
    
    Provides:
    
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "WRONG_COLLECTION_TYPE_EXCEPTION"
    MSG = "The collection is not of the correct type."