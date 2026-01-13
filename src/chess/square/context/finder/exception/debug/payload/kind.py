# src/chess/square/context/finder/exception/debug/payload/kind.py

"""
Module: chess.square.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.square import SquareException

_all__ = [
    # ======================# SQUARE_DATASET_NULL EXCEPTION #======================#
    "SquareSearchNullDatasetException",
]


# ======================# SQUARE_SEARCH_PAYLOAD_IS_NOT_LIST EXCEPTION #======================#
class SquareSearchPayloadTypeException(SquareException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the payload  of a successful SquareSearch payload is not List[Square].

    # PARENT:
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "SquareSearch payload is the wrong type. The payload should be List[Square]."