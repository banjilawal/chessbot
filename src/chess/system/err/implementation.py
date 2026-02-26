# src/chess/system/err/implementation.py

"""
Module: chess.system.err.implementation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import DebugException

__all__ = [
    # ======================# NOT_IMPLEMENTED EXCEPTION #======================#
    "MethodNotImplementedException",
]

from chess.system import ChessException


# ======================# NOT_IMPLEMENTED EXCEPTION #======================#
class MethodNotImplementedException(ChessException):
    """
    # ROLE: Information, Reporting, Debug

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
    ERR_CODE = "NOT_IMPLEMENTED_WARNING"
    MSG = "The method is not implemented."
