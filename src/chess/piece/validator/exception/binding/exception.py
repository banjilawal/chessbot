# src/chess/piece/validator/exception/binding/collision.py
"""
Module: chess.piece.validator.exception.binding.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import (
    ChessException, BuilderException, InconsistencyException, NullException, ValidationException
)

__all__ = [
    "PieceException",
    
    # ======================# PIECE NULL EXCEPTIONS #======================#
    "NullPieceException",
    "NullKingException",
    "NullCombatantException",
    "PieceTeamFieldIsNullException",
    "PieceNoCoordStackServiceException",
    "PieceNullCoordStackException",
    "PieceRosterNumberIsNullException",
    
    # ======================# PIECE VALIDATION EXCEPTIONS #======================#
    "InvalidPieceException",
    "ActivePieceMissingFromTeamRoster",
    "CheckmatedKingException",
    "CapturedPieceException",
    "PieceRequiresInitialPlacementException",
    
    "PieceRankOutOfBoundsException",
    "PieceMissingDiscoveriesException",

]



# ======================# PIECE VALIDATION EXCEPTIONS #======================#

