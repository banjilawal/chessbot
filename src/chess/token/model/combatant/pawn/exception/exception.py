# src/chess/token/model/combatant/pawn/exception/exception.py

"""
Module: chess.token.model.combatant.pawn.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""

from chess.piece import CombatantPieceException
from chess.system import BuildFailedException, NullException, ValidationException


__all__ = [
#======================# PAWN_PIECE EXCEPTION #======================#
    "PawnPieceException",
    
#======================# PAWN_PIECE VALIDATION EXCEPTION #======================#
    "InvalidPawnPieceException",
    "NullPawnException",
    
#======================# PAWN_PIECE BUILD EXCEPTION #======================#
    "PawnPieceBuildFailedException",
]

#======================# PAWN_PIECE EXCEPTION #======================#
class PawnPieceException(CombatantPieceException):
    """Super class for PawnPiece exception."""
    ERROR_CODE = "PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece raised an exception."


#======================# PAWN_PIECE VALIDATION EXCEPTION #======================#
class InvalidPawnPieceException(PawnPieceException, ValidationException):
    """Raised by PieceValidator when a pawn candidate fails a sanity check."""
    ERROR_CODE = "PAWN_PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PawnPiece validation failed."
    

class NullPawnException(PawnPieceException, NullException):
    """Raised if an entity, method, or operation expects a PawnPiece but gets null instead."""
    ERROR_CODE = "NULL_PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece cannot be null."


#======================# PAWN_PIECE BUILD EXCEPTION #======================#
class PawnPieceBuildFailedException(PawnPieceException, BuildFailedException):
    ERROR_CODE = "PAWN_PIECE_BUILD_FAILED"
    DEFAULT_MESSAGE = "PawnPiece build failed."
    
