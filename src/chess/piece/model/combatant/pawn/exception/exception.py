# src/chess/piece/model/combatant/pawn/exception/exception.py

"""
Module: chess.piece.model.combatant.pawn.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""

from chess.piece import CombatantPieceException
from chess.system import BuildFailedException, NullException, ValidationException


__all__ = [
#======================# PAWN_PIECE EXCEPTION SUPER CLASS #======================#
    "PawnPieceException",
    
#======================# PAWN_PIECE VALIDATION EXCEPTIONS #======================#
    "InvalidPawnPieceException",
    "NullPawnException",
    
#======================# PAWN_PIECE BUILD EXCEPTIONS #======================#
    "PawnPieceBuildFailedException",
]

#======================# PAWN_PIECE EXCEPTION SUPER CLASS #======================#
class PawnPieceException(CombatantPieceException):
    """Super class for PawnPiece exceptions."""
    ERROR_CODE = "PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece raised an exception."


#======================# PAWN_PIECE VALIDATION EXCEPTIONS #======================#
class InvalidPawnPieceException(PawnPieceException, ValidationException):
    """Raised by PieceValidator when a pawn candidate fails a sanity check."""
    ERROR_CODE = "PAWN_PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PawnPiece validation failed."
    

class NullPawnException(PawnPieceException, NullException):
    """Raised if an entity, method, or operation expects a PawnPiece but gets null instead."""
    ERROR_CODE = "NULL_PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece cannot be null."


#======================# PAWN_PIECE BUILD EXCEPTIONS #======================#
class PawnPieceBuildFailedException(PawnPieceException, BuildFailedException):
    ERROR_CODE = "PAWN_PIECE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "PawnPiece build failed."
    
