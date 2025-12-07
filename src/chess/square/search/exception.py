# src/chess/square/searcher/base.py

"""
Module: chess.square.searcher.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import FinderException

__all__ = [
    "SquareFinderException",
]
class SquareFinderException(FinderException):
    ERROR_CODE = "SQUARE_SEARCH_ERROR"
    DEFAULT_MESSAGE = "SquareFinder raised an exception."