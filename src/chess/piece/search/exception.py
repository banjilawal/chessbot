# src/chess/piece/searcher/base.py

"""
Module: chess.piece.searcher.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    # ======================# PIECE_SEARCH EXCEPTIONS #======================#
    "PieceFinderException",
]


# ======================# PIECE_SEARCH EXCEPTIONS #======================#
class PieceFinderException(FinderException):
    """
    Super class of exceptions raised by PieceFinder objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "PIECE_SEARCH_ERROR"
    DEFAULT_MESSAGE = "PieceFinder raised an exception."