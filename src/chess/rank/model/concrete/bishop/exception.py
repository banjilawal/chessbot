# src/chess/rank/model/concrete/bishop/exception.py

"""
Module: chess.rank.model.concrete.bishop.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

# src/chess/rank/compute/span/bishop/exception.py

"""
Module: chess.rank.compute.span.bishop.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# BISHOP_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "BishopSpanComputationFailedException",
]


# ======================# BISHOP_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class BishopSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Bishop's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BISHOP_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Bishop span computation failed."