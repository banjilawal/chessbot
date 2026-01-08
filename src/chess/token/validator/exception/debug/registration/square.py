# src/chess/token/validator/exception/registration/square_name

"""
Module: chess.token.validator.exception.registration.square_name
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


__all__ = [
    #======================# TOKEN_NOT_REGISTERED_WITH_SQUARE EXCEPTION #======================#
    "TokenNotRegisteredWithSquareException"
]

from chess.token import TokenNotRegisteredException


#======================# TOKEN_NOT_REGISTERED_WITH_SQUARE EXCEPTION #======================#
class TokenNotRegisteredWithSquareException(TokenNotRegisteredException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Token has assigned itself to a Square instance but the Square
        has not registered the token as its occupant.
    2.  That is token.coord == square_name.coord but square_name.occupant != token.

    # PARENT:
        *   TokenRegistrationException

    # PROVIDES:
    TokenNotRegisteredWithSquareException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_NOT_REGISTERED_WITH_SQUARE_ERROR"
    DEFAULT_MESSAGE = (
        "Token is not registered as Square.occupant. There is no relationship between them."
    )

