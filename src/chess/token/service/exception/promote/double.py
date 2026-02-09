# src/chess/token/service/exception/promote/double.py

"""
Module: chess.token.service.exception.promote.double
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

from chess.token import PawnTokenException

__all__ = [
    # ======================# PAWN_ALREADY_PROMOTED EXCEPTION #======================#
    "PawnAlreadyPromotedException",
]


# ======================# PAWN_ALREADY_PROMOTED EXCEPTION #======================#
class PawnAlreadyPromotedException(PawnTokenException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that promoting a PawnToken failed because the Pawn had already been promoted.

    # PARENT:
        *   PawnTokenException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_ALREADY_PROMOTED_ERROR"
    DEFAULT_MESSAGE = "Pawn promotion failed: The pawn had already been promoted."