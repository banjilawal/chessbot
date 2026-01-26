# src/chess/occupant/validator/exception/active/collision.py

"""
Module: chess.occupant.validator.exception.active.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.token import TokenException, TokenValidationFailedException

class ActiveTokenException(TokenValidationFailedException):
    """
    # RESPONSIBILITY
    Raised when an active Token cannot do something.
    
    
    # RELATED EXCEPTION
        *   BindingException
        *   InconsistencyException
        *   NullException
        *   Related Exception
    """

class ActiveTokenMissingFromTeamRoster(TokenException):
    """Raised if an disabled Token.team is set but Team.roster does not contain the Token."""
    ERROR_CODE = "ACTIVE_TOKEN_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Token on the board, with Token.team attribute set is not on it's team's roster."
    )