# src/chess/square/search/exception.py

"""
Module: chess.square.search.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import SearchException

__all__ = [
    "SquareSearchException",
]
class SquareSearchException(SearchException):
    ERROR_CODE = "SQUARE_SEARCH_ERROR"
    DEFAULT_MESSAGE = "SquareSearch raised an exception."