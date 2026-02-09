# src/chess/token/service/exception/promote/king.py

"""
Module: chess.token.service.exception.promote.king
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.token import PawnTokenException

__all__ = [
    # ======================# PROMOTING_TO_KING_NOT_ALLOWED EXCEPTION #======================#
    "CannotPromotePawnToKingException",
]


# ======================# PROMOTING_TO_KING_NOT_ALLOWED EXCEPTION #======================#
class CannotPromotePawnToKingException(PawnTokenException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that promoting a PawnToken failed because promoting to a King's rank is not allowed.
    
    # PARENT:
        *   PawnTokenException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PROMOTING_TO_KING_NOT_ALLOWED_ERROR"
    DEFAULT_MESSAGE = "Pawn promotion failed: Promoting to a King is not allowed."