# src/chess/rank/model/concrete/pawn/compute/engine/engine.py

"""
Module: chess.rank.model.concrete.pawn.compute.engine.engine
Author: Banji Lawal
Created: 2026-01-23
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# PAWN_SOLUTION_ENGINE_FAILURE EXCEPTION #======================#
    "PawnSolutionEngineException",
]


# ======================# PAWN_SOLUTION_ENGINE_FAILURE EXCEPTION #======================#
class PawnSolutionEngineException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the PawnSolutionEngine from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_SOLUTION_ENGINE_FAILURE"
    DEFAULT_MESSAGE = "The PawnSolutionEngine failed."