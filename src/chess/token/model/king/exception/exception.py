# src/chess/piece/model/king/exception/exception.py

"""
Module: chess.piece.model.king.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.piece import PieceException
from chess.system import BuildFailedException, NullException, ValidationException

__all__ = [
    #======================# KING_PIECE EXCEPTION #======================#
    "KingPieceException",
    
    #======================# KING_PIECE VALIDATION EXCEPTION #======================#
    "InvalidKingPieceException",
    "NullKingException",
    
    #======================# KING_PIECE BUILD EXCEPTION #======================#
    "KingPieceBuildFailedException",
]


#======================# KING_PIECE EXCEPTION #======================#
class KingPieceException(PieceException):
    """Super class for KingPiece exception."""
    ERROR_CODE = "KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece raised an exception."


#======================# KING_PIECE VALIDATION EXCEPTION #======================#
class InvalidKingPieceException(KingPieceException, ValidationException):
    """Raised by PieceValidator when a king candidate fails a sanity check."""
    ERROR_CODE = "KING_PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "KingPiece validation failed."


class NullKingException(KingPieceException, NullException):
    """Raised if an entity, method, or operation expects a KingPiece but gets null instead."""
    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece cannot be null."


#======================# KING_PIECE BUILD EXCEPTION #======================#
class KingPieceBuildFailedException(KingPieceException, BuildFailedException):
    ERROR_CODE = "KING_PIECE_BUILD_FAILED"
    DEFAULT_MESSAGE = "KingPiece build failed."