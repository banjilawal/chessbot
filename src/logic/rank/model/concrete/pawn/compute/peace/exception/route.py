# src/logic/rank/model/concrete/pawn/compute/peace/exception/route.py

"""
Module: logic.rank.model.concrete.pawn.compute.peace.exception.route
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PAWN_PEACEFUL_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
    "PawnPeacefulSpanComputationRouteException",
]

from logic.system import ExecutionRouteException


# ======================# NO_PAWN_PEACEFUL_SPAN_COMPUTATION_ROUTE EXCEPTION #======================#
class PawnPeacefulSpanComputationRouteException(ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PawnPeacefulSpan build failed because there was no computation route for the Pawn's MoveState.

    # PARENT:
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PAWN_PEACEFUL_SPAN_COMPUTATION_ROUTE_EXCEPTION"
    MSG = "PawnPeacefulSpan computation failed: No spanning set computation route for Pawn's MoveState."