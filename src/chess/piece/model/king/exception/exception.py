# src/chess/piece/model/king/exception/exception.py

"""
Module: chess.piece.model.king.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.piece import PieceException

__all__ = [
    # ======================# KING EXCEPTIONS #======================#
    "KingPieceException",
]

# ======================# KING EXCEPTIONS #======================#
class KingPieceException(PieceException):
    ERROR_CODE = "KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece raised an exception."
