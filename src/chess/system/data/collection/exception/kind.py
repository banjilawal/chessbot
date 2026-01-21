# src/chess/system/data/collection/exception/kind.py

"""
Module: chess.system.data.collection.exception.kind
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DatasetException

__all__ = [
    # ====================== WRONG_TYPE_IN_DATA_SET EXCEPTION #======================#
    "WrongTypeInDatasetException",
]


# ====================== WRONG_TYPE_IN_DATA_SET EXCEPTION #======================#
class WrongTypeInDatasetException(DatasetException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  The Dataset contains the wrong type of data.
    
    # PARENT:
     *   ChessException
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "WRONG_TYPE_IN_DATA_SETERROR"
    DEFAULT_MESSAGE = "The dataset is not of the correct type."