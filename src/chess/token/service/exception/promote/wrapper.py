# src/chess/token/service/exception/promote/wrapper.py

"""
Module: chess.token.service.exception.promote.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# PAWN_PROMOTION_FAILURE #======================#
    "PawnPromotionFailedException",
]

from chess.token import PawnTokenException
from chess.system import OperationFailedException


# ======================# PAWN_PROMOTION_FAILURE #======================#
class PawnPromotionFailedException(PawnTokenException, OperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a Pawn was not promoted. The exception chain traces
        the ultimate source of failure.

    # PARENT:
        *   PawnTokenException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_PROMOTION_FAILURE"
    DEFAULT_MESSAGE = "Pawn promotion failed."