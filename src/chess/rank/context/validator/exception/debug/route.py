# src/chess/rank/context/validator/exception/debug/route.py

"""
Module: chess.rank.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "RankContextValidationRouteException",
]

from chess.rank import RankContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_RANK_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class RankContextValidationRouteException(RankContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the RankContext validation failed because there was no build route for the RankContext key.

    # PARENT:
        *   RankContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_RANK_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "RankContext validation failed: No validation route was provided for the Rank attribute."