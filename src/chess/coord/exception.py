# src/chess/coord.base.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-09-27
version: 1.0.0
"""

from chess.system import ChessException

___all__ = [
    # ======================# COORD EXCEPTION #======================#
    "CoordException",
]


# ======================# COORD EXCEPTION #======================#
class CoordException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Coord errors not covered by CoordException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_ERROR"
    DEFAULT_MESSAGE = "Coord raised an exception."