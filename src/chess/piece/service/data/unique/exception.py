# src/chess/piece/service/data/unique/exception.py

"""
Module: chess.piece.service.data.unique.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    # ======================# UNIQUE_PIECE_DATA_SERVICE EXCEPTIONS #======================#
    "UniquePieceDataServiceException",
    "AddingDuplicatePieceException",
]


# ======================# UNIQUE_PIECE_DATA_SERVICE EXCEPTIONS #======================#
class UniquePieceDataServiceException(DataServiceException):
    """
    Super class of exceptions raised by UniquePieceDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "UNIQUE_PIECE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniquePieceDataService raised an exception."


class AddingDuplicatePieceException(UniquePieceDataServiceException):
    """Raised when trying to add a duplicate Piece to a list of Pieces."""
    ERROR_CODE = "DUPLICATE_PIECE_ADDITION_ERROR"
    DEFAULT_MESSAGE = "UniquePieceDataService cannot add duplicate Pieces to the list."