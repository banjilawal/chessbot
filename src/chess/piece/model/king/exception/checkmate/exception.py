# src/chess/piece/model/king/exception/checkmate/exception.py

"""
Module: chess.piece.model.king.exception.checkmate.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.piece import KingPieceException


__all__ = [
    # ======================# CHECKMATED KING EXCEPTIONS #======================#
    "CheckmatedKingException",
]


# ======================# CHECKMATED KING EXCEPTIONS #======================#
class CheckmatedKingException(KingPieceException):
    """Catchall for when a Checkmated king tries to do something."""
    ERROR_CODE = "CHECKMATED_KING_ERROR"
    DEFAULT_MESSAGE = (
        "King is in checkmate. King cannot perform any actions. The game ends "
        "when the King is checkmated."
    )