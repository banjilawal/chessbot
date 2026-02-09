# src/chess/token/service/exception/promote/route.py

"""
Module: chess.token.service.exception.promote.route
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PROMOTION_ROUTE_TO_NEW_RANK  EXCEPTION #======================#
    "PawnPromotionRouteException",
]

from chess.token import PawnTokenException
from chess.system import NoExecutionRouteException


# ======================# NO_PROMOTION_ROUTE_TO_NEW_RANK EXCEPTION #======================#
class PawnPromotionRouteException(PawnTokenException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that promoting a PawnToken failed because there was no promotion route to the new rank.

    # PARENT:
        *   PawnTokenException
        *   NoRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_PROMOTION_ROUTE_TO_NEW_RANK_ERROR"
    DEFAULT_MESSAGE = "Pawn promotion failed: The promotion route was provided for the new rank."