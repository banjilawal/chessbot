# src/chess/system/data/collection/exception/base.py

"""
Module: chess.system.data.collection.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ====================== DATA_SET EXCEPTION #======================#
    "DatasetException",
]




# ====================== DATA_SET EXCEPTION #======================#
class DatasetException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Wrapper for data collection integrity problems.
    2   Parent of exceptions raised by a collection of items a StackService owns.
    3.  Catchall for errors not covered by lower level DatasetException subclasses.
    
    # PARENT:
     *   ChessException
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DATA_SET_ERROR"
    DEFAULT_MESSAGE = "Dataset raised an exception."
