# src/chess/token/validator/exception/registration/square_name

"""
Module: chess.token.validator.exception.registration.square_name
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import PieceRegistrationException

__all__ = [
    #======================# PIECE_NOT_REGISTERED_WITH_SQUARE EXCEPTION #======================#
    "PieceNotRegisteredWithSquareException"
]

#======================# PIECE_NOT_REGISTERED_WITH_SQUARE EXCEPTION #======================#
class PieceNotRegisteredWithSquareException(PieceRegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Token has assigned itself to a Square instance but the Square
        has not registered the piece as its occupant.
    2.  That is piece.coord == square_name.coord but square_name.occupant != piece.

    # PARENT:
        *   PieceRegistrationException

    # PROVIDES:
    PieceNotRegisteredWithSquareException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_NOT_REGISTERED_WITH_SQUARE_ERROR"
    DEFAULT_MESSAGE = (
        "Token is not registered as Square.occupant. There is no relationship between them."
    )

