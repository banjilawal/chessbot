# src/chess/edge/context/finder/exception/debug/payload/kind.py

"""
Module: chess.edge.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.edge import EdgeException
from chess.system import ResultException

_all__ = [
    # ======================# EDGE_DATASET_NULL EXCEPTION #======================#
    "EdgeSearchNullDatasetException",
]


# ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_EDGES EXCEPTION #======================#
class EdgeSearchPayloadTypeException(EdgeException, ResultException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that after the EdgeSearch ran successfully the payload was not a List[Edge]. This exception makes
        sure search payloads follow the convention of returning an array of matches not a single item.

    # PARENT:
        *   EdgeException
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "EdgeSearch payload is the wrong type. The payload should be List[Edge]."