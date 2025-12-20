# src/chess/piece/model/king/exception/validation/exception.py

"""
Module: chess.piece.model.king.exception.validation.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import NullException
from chess.piece import InvalidPieceException, KingPieceException

__all__ = [
    #======================# NULL KING EXCEPTION #======================#
    "InvalidKingPieceException",
    "NullKingException",
]


#======================# INVALID KING EXCEPTION #======================#
class InvalidKingPieceException(KingPieceException, InvalidPieceException):
    ERROR_CODE = "KING_PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "KingPiece validation failed."
    

#======================# NULL KING EXCEPTION #======================#
class NullKingException(InvalidKingPieceException, NullException):
    """Raised if an entity, method, or operation expects a KingPiece but gets null instead."""
    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece cannot be null."