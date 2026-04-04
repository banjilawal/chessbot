# src/logic/system/collection/exception/anchor.py

"""
Module: logic.system.collection.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from system import ChessException

__all__ = [
    # ====================== COLLECTION EXCEPTION #======================#
    "CollectionException",
]




# ====================== COLLECTION EXCEPTION #======================#
class CollectionException(ChessException):
    """
    Role:Exception Work
    
    Responsibilities:
    1.  Work for data collection integrity problems.
    2   Parent of exceptions raised by a collection of bag a StackService owns.
    3.  Super for errors not covered by lower level CollectionException subclasses.
    
    Super Class:
     *   ChessException
    
    Provides:
    
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "COLLECTION_EXCEPTION"
    MSG = "Dataset raised an exception."
