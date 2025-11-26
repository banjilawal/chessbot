# src/chess/piece/combatant/pawn/exception/exception.py

"""
Module: chess.piece.combatant.pawn.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""



from chess.piece import CombatantPieceException

__all__ =[
    "PawnPieceException",
]

class PawnPieceException(CombatantPieceException):
    ERROR_CODE = "PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece raised an exception."
    
