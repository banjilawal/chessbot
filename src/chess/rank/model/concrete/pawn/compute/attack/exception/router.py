# src/chess/rank/model/concrete/pawn/compute/attack/exception/route.py

"""
Module: chess.rank.model.concrete.pawn.compute.attack.exception.route
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
    "PawnAttackSpanComputationRouteException",
]


from chess.system import NoExecutionRouteException


# ======================# UNHANDLED_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
class PawnAttackSpanComputationRouteException(NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PawnAttackSpan build failed because there was no computation route for the Pawn's MoveState..

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PawnAttackSpan computation failed: No spanning set computation route for Pawn's MoveState."