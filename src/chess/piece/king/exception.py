# src/chess/piece/king/exception.py

"""
Module: chess.piece.king.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.piece import PieceException

__all__ = [
    "KingPieceException",
]

class KingPieceException(PieceException):
    ERROR_CODE = "KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece raised an exception."