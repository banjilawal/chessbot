# src/chess/rank/model/concrete/knight/exception.py

"""
Module: chess.rank.model.concrete.knight.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

# src/chess/rank/compute/span/knight/exception.py

"""
Module: chess.rank.compute.span.knight.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# KNIGHT_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "KnightSpanComputationFailedException",
]


# ======================# KNIGHT_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class KnightSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Knight's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "KNIGHT_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Knight span computation failed."