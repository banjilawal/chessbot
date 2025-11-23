# src/chess/square/search/exception.py

"""
Module: chess.square.search.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import SearchContextServiceException

__all__ = [
    "SquareSearchServiceException",
]
class SquareSearchServiceException(SearchContextServiceException):
    ERROR_CODE = "SQUARE_SEARCH_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareSearchService raised an exception."