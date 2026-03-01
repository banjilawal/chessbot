# src/logic/token/service/exception/promote/wrapper.py

"""
Module: logic.token.service.exception.promote.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# PAWN_PROMOTION_FAILURE #======================#
    "PawnPromotionException",
]

from logic.token import PawnTokenException
from logic.system import OperationException


# ======================# PAWN_PROMOTION_FAILURE #======================#
class PawnPromotionException(PawnTokenException, OperationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a Pawn was not promoted. The exception chain traces
        the ultimate source of failure.

    # PARENT:
        *   PawnTokenException
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PAWN_PROMOTION_FAILURE"
    MSG = "Pawn promotion failed."