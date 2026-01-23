# src/chess/rank/model/concrete/pawn/compute/attack/exception/router.py

"""
Module: chess.rank.model.concrete.pawn.compute.attack.exception.router
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
    "PawnAttackSpanComputationRouteException",
]

from chess.hostage import PawnAttackSpanException
from chess.rank import PawnException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
class PawnAttackSpanComputationRouteException(PawnException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PawnAttackSpan build failed because there was no computation route for the Pawn's MoveState..

    # PARENT:
        *   PawnAttackSpanException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PawnAttackSpan computation failed: No spanning set computation route for Pawn's MoveState."