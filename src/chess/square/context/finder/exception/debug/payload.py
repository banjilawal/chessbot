# src/chess/square/context/finder/exception/debug/payload/kind.py

"""
Module: chess.square.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.square.context import SquareContextDebugException

_all__ = [
    # ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_SQUARES EXCEPTION #======================#
    "SquareSearchPayloadTypeException",
]


# ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_SQUARES EXCEPTION #======================#
class SquareSearchPayloadTypeException(SquareContextDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because a square was sent in the payload instead of List[Square].

    # PARENT:
        *   SquareContextDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SSEARCH_PAYLOAD_IS_NOT_LIST_OF_SQUARES_ERROR"
    DEFAULT_MESSAGE = "Square search failed: The payload contained a single square instead of List[Square]."