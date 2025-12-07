# src/chess/coord/searcher/exception.py

"""
Module: chess.coord.searcher.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import FinderException

__all__ = ["CoordFinderException"]

class CoordFinderException(FinderException):
    """
    Super class of exceptions raised by CoordSearche objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_SEARCH_ERROR"
    DEFAULT_MESSAGE = "CoordFinder raised an exception."

