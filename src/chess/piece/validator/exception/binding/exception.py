# src/chess/piece/validator/exception/binding/exception.py
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


class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an active Piece.team is set but Team.roster does not contain the Piece."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece on the board, with Piece.team attribute set is not on it's team's roster."
    )


class PieceRequiresInitialPlacementException(PieceException):
    """Raised when team_name potential actor_candidate has not been placed on the board_validator."""
    ERROR_CODE = "PIECE_WITH_NO_INITIAL_PLACEMENT_ERROR"
    DEFAULT_MESSAGE = "Piece has not received its initial placement on the board."
