# src/chess/rank/model/concrete/pawn/compute/opening/exception.py

"""
Module: chess.rank.model.concrete.pawn.compute.openingexception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# PAWN_OPENING_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "PawnOpeningSpanComputationFailedException",
]


# ======================# PAWN_OPENING_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class PawnOpeningSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Pawn's opening spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_OPENING_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Pawn opening span computation failed."