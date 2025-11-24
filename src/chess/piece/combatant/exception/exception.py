# src/chess/piece/combatant/exception/exception.py

"""
Module: chess.piece.combatant.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""


from chess.piece import PieceException

__all__ = [
    "CombatantPieceException",
]

class CombatantPieceException(PieceException):
    ERROR_CODE = "COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece raised an exception."