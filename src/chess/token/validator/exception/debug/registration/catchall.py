# src/chess/token/validator/exception/registration/catchall.py

"""
Module: chess.token.validator.exception.registration.catchall
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamException


__all__ = [
    #======================# TOKEN_NOT_REGISTERED EXCEPTION #======================#
    "TokenNotRegisteredException"
]

#======================# TOKEN_NOT_REGISTERED EXCEPTION #======================#
class TokenNotRegisteredException(TeamException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall Exception for when an Token has set its owner correctly but the owner does not
        have the occupant in its collection.

    # PARENT:
        *   NoRegistrationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_NOT_REGISTERED_ERROR"
    DEFAULT_MESSAGE = "Token not registered with parent."