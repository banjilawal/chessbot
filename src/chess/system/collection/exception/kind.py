# src/chess/system/collection/exception/kind.py

"""
Module: chess.system.collection.exception.kind
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import CollectionException

__all__ = [
    # ====================== WRONG_COLLECTION_TYPE EXCEPTION #======================#
    "WrongCollectionTypeException",
]


# ====================== WRONG_COLLECTION_TYPE EXCEPTION #======================#
class WrongCollectionTypeException(CollectionException):
    """
    # ROLE: Exception Wrapper
    
    # RESPONSIBILITIES:
    1.  The Collection contains the wrong type of data.
    
    # PARENT:
     *   CollectionException
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "WRONG_COLLECTION_TYPE_ERROR"
    DEFAULT_MESSAGE = "The collection is not of the correct type."