# src/chess/square/service/exception/occupant/add/opening.py

"""
Module: chess.square.service.exception.occupant.add.opening
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_PICKED_WRONG_OPENING_SQUARE EXCEPTION #======================#
    "TokenEnteringWrongOpeningSquareException",
]

from chess.square import SquareDebugException


# ======================# TOKEN_PICKED_WRONG_OPENING_SQUARE EXCEPTION #======================#
class TokenEnteringWrongOpeningSquareException(SquareDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a square occupation attempt failed because the token picked the wrong
        square for its initial placement.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_PICKED_WRONG_OPENING_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Token entering a square failed: The token is assigned a different opening square."