# src/chess/coord.base.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-09-27
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    #======================# COORD EXCEPTION #======================#
    "CoordException",
]


#======================# COORD EXCEPTION #======================#
class CoordException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Coord objects.
    2.  Catchall for conditions which are not covered by lower level Coord exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_ERROR"
    DEFAULT_MESSAGE = "Coord raised an exception."
