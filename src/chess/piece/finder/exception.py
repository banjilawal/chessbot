# src/chess/piece/finder/exception.py

"""
Module: chess.piece.finder.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    #======================# PIECE_SEARCH EXCEPTIONS #======================#
    "PieceFinderException",
]


#======================# PIECE_SEARCH EXCEPTIONS #======================#
class PieceFinderException(FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by PieceFinder objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of a PieceFinder method.

    # PARENT
        *   FinderException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_SEARCH_ERROR"
    DEFAULT_MESSAGE = "PieceFinder raised an exception."