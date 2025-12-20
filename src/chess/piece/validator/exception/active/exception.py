# src/chess/piece/number_bounds_validator/exception/active/collision.py

"""
Module: chess.piece.number_bounds_validator.exception.active.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import InvalidPieceException

class ActivePieceException(InvalidPieceException):
    """
    # RESPONSIBILITY
    Raised when an active Piece cannot do something.
    
    
    # RELATED EXCEPTION
        *   BindingException
        *   InconsistencyException
        *   NullException
        *   Related Exception
    """

class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an disabled Piece.team is set but Team.roster does not contain the Piece."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece on the board, with Piece.team attribute set is not on it's team's roster."
    )