# src/chess/square/context/finder/exception/debug/payload/kind.py

"""
Module: chess.square.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import ResultException

_all__ = [
    # ======================# SQUARE_DATASET_NULL EXCEPTION #======================#
    "SquareSearchNullDatasetException",
]


# ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_SQUARES EXCEPTION #======================#
class SquareSearchPayloadTypeException(SquareException, ResultException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that after the SquareSearch ran successfully the payload was not a List[Square]. This exception makes
        sure search payloads follow the convention of returning an array of matches not a single item.

    # PARENT:
        *   SquareException
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "SquareSearch payload is the wrong type. The payload should be List[Square]."