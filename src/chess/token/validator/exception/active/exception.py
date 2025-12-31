# src/chess/token/validator/exception/active/collision.py

"""
Module: chess.token.validator.exception.active.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import InvalidPieceException

class ActivePieceException(InvalidPieceException):
    """
    # RESPONSIBILITY
    Raised when an active Token cannot do something.
    
    
    # RELATED EXCEPTION
        *   BindingException
        *   InconsistencyException
        *   NullException
        *   Related Exception
    """

class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an disabled Token.team is set but Team.roster does not contain the Token."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Token on the board, with Token.team attribute set is not on it's team's roster."
    )