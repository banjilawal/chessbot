# src/chess/piece/search/exception.py

"""
Module: chess.piece.search.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.system import SearchException

__all__ = [
    "PieceSearchException",
]


class PieceSearchException(SearchException):
    """
    Super class of exceptions raised by PieceSearch objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "PIECE_SEARCH_ERROR"
    DEFAULT_MESSAGE = "PieceSearch raised an exception."