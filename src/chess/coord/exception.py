# src/chess/square/collision.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-09-27
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "CoordException",
]


class CoordException(ChessException):
    """
    Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_ERROR"
    DEFAULT_MESSAGE = "Coord raised an exception."
