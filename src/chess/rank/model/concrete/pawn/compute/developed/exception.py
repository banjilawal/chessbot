# src/chess/rank/model/concrete/pawn/compute/developed/exception.py

"""
Module: chess.rank.model.concrete.pawn.compute.developedexception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# PAWN_DEVELOPED_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "PawnDevelopedSpanComputationFailedException",
]


# ======================# PAWN_DEVELOPED_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class PawnDevelopedSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Pawn's developed spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_DEVELOPED_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Pawn developed span computation failed."