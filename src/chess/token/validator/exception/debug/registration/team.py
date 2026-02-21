# src/chess/token/validator/exception/registration/team.py

"""
Module: chess.token.validator.exception.registration.team
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.token import TokenNotRegisteredException

__all__ = [
    #======================# TOKEN_NOT_REGISTERED_WITH_TEAM EXCEPTION #======================#
    "TokenNotRegisteredWithTeamException"
]


#======================# TOKEN_NOT_REGISTERED_WITH_TEAM EXCEPTION #======================#
class TokenNotRegisteredWithTeamException(TokenNotRegisteredException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Token has assigned itself to a Team but the occupant is not included in the
        Team's roster.
    2.  That is occupant.team = team but occupant not in team.roster.

    # PARENT:
        *   TokenRegistrationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_NOT_REGISTERED_WITH_TEAM_ERROR"
    DEFAULT_MESSAGE = (
        "Token is not registered in Team.roster. Only the occupant-side of the relationship is set."
    )