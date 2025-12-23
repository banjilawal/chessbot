# src/chess/system/err/implementation.py

"""
Module: chess.system.err.implementation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NOT_IMPLEMENTED EXCEPTION #======================#
    "NotImplementedException",
]

from chess.system import ChessException


# ======================# NOT_IMPLEMENTED EXCEPTION #======================#
class NotImplementedException(ChessException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a call was made to an abstract method that the subclass does not implement.
    
    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "NOT_IMPLEMENTED_WARNING"
    DEFAULT_MESSAGE = "The method is not implemented."
