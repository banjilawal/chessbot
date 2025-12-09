# src/chess/piece/combatant/exception/exception.py

"""
Module: chess.piece.combatant.exception.exception
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""


from chess.piece import PieceException
from chess.system import BuildFailedException, NullException, ValidationException


__all__ = [
    #======================# COMBATANT_PIECE EXCEPTION SUPER CLASS #======================#
    "CombatantPieceException",
    
    #======================# COMBATANT_PIECE VALIDATION EXCEPTIONS #======================#
    "InvalidCombatantPieceException",
    "NullCombatantException",
    
    #======================# COMBATANT_PIECE BUILD EXCEPTIONS #======================#
    "CombatantPieceBuildFailedException",
]


#======================# COMBATANT_PIECE EXCEPTION SUPER CLASS #======================#
class CombatantPieceException(PieceException):
    """Super class for CombatantPiece exceptions."""
    ERROR_CODE = "COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece raised an exception."


#======================# COMBATANT_PIECE VALIDATION EXCEPTIONS #======================#
class InvalidCombatantPieceException(CombatantPieceException, ValidationException):
    """Raised by PieceValidator when a combatant candidate fails a sanity check."""
    ERROR_CODE = "COMBATANT_PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece validation failed."


class NullCombatantException(CombatantPieceException, NullException):
    """Raised if an entity, method, or operation expects a CombatantPiece but gets null instead."""
    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece cannot be null."


#======================# COMBATANT_PIECE BUILD EXCEPTIONS #======================#
class CombatantPieceBuildFailedException(CombatantPieceException, BuildFailedException):
    ERROR_CODE = "COMBATANT_PIECE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece build failed."