# src/chess/rank/model/concrete/pawn/compute/attack/exception/route.py

"""
Module: chess.rank.model.concrete.pawn.compute.attack.exception.route
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
    "PawnAttackSpanComputationRouteException",
]


from chess.system import ExecutionRouteException


# ======================# NO_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
class PawnAttackSpanComputationRouteException(ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PawnAttackSpan build failed because there was no computation route for the Pawn's MoveState.

    # PARENT:
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PAWN_ATTACK_SPAN_COMPUTATION_ROUTE_EXCEPTION"
    MSG = "PawnAttackSpan computation failed: No spanning set computation route for Pawn's MoveState."