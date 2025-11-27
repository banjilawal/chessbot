# src/chess/piece/model/combatant/pawn/exception/exception.py

"""
Module: chess.piece.model.combatant.pawn.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""



from chess.piece import CombatantPieceException, NullPieceException

__all__ =[
    "PawnPieceException",
    "NullPawnException",
]

class PawnPieceException(CombatantPieceException):
    ERROR_CODE = "PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece raised an exception."


class NullPawnException(PawnPieceException, NullPieceException):
    """Raised if an entity, method, or operation expects a PawnPiece but gets null instead."""
    ERROR_CODE = "NULL_PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece cannot be null."
    
