# src/chess/node/context/finder/exception/debug/payload/kind.py

"""
Module: chess.node.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.node import NodeException
from chess.system import ResultException

_all__ = [
    # ======================# NODE_DATASET_NULL EXCEPTION #======================#
    "NodeSearchNullDatasetException",
]


# ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_NODES EXCEPTION #======================#
class NodeSearchPayloadTypeException(NodeException, ResultException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that after the NodeSearch ran successfully the payload was not a List[Node]. This exception makes
        sure search payloads follow the convention of returning an array of matches not a single item.

    # PARENT:
        *   NodeException
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "NodeSearch payload is the wrong type. The payload should be List[Node]."