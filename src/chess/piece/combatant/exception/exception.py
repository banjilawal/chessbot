# src/chess/piece/combatant/exception/exception.py

"""
Module: chess.piece.combatant.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""


from chess.piece import PieceException, NullPieceException

__all__ = [
    # ======================# COMBATANT_PIECE EXCEPTION SUPER CLASS EXCEPTIONS #======================#
    "CombatantPieceException",
    
    # ======================# NULL COMBATANT_PIECE EXCEPTIONS #======================#
    "NullCombatantException",
]


# ======================# COMBATANT_PIECE EXCEPTION SUPEr CLASS EXCEPTIONS #======================#
class CombatantPieceException(PieceException):
    ERROR_CODE = "COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece raised an exception."


# ======================# NULL COMBATANT_PIECE EXCEPTIONS #======================#
class NullCombatantException(CombatantPieceException, NullPieceException):
    """Raised if an entity, method, or operation expects a CombatantPiece but gets null instead."""
    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece cannot be null."