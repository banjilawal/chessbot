# src/logic/rank/model/concrete/pawn/compute/peace/exception.py

"""
Module: logic.rank.model.concrete.pawn.compute.peace.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from logic.rank import SpanComputationException

__all__ = [
    # ======================# PAWN_PEACEFUL_SPAN_COMPUTATION_FAILURE #======================#
    "PawnPeacefulSpanComputationException",
]


# ======================# PAWN_PEACEFUL_SPAN_COMPUTATION_FAILURE #======================#
class PawnPeacefulSpanComputationException(SpanComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Pawn's peaceful spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PAWN_PEACEFUL_SPAN_COMPUTATION_FAILURE"
    MSG = "Pawn peaceful span computation failed."