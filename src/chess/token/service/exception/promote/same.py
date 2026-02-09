# src/chess/token/service/exception/promote/same.py

"""
Module: chess.token.service.exception.promote.same
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

from chess.token import PawnTokenException

__all__ = [
    # ======================# NEW_RANK_IS_STILL_PAWN_RANK EXCEPTION #======================#
    "NewRankSameAsCurrentRankException",
]


# ======================# NEW_RANK_IS_STILL_PAWN_RANK EXCEPTION #======================#
class NewRankSameAsCurrentRankException(PawnTokenException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that promoting a PawnToken failed because the new rank was still a Pawn's rank.
    
    # PARENT:
        *   PawnTokenException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NEW_RANK_IS_STILL_PAWN_RANK_ERROR"
    DEFAULT_MESSAGE = "Pawn promotion failed: The new rank is still a Pawn's rank."