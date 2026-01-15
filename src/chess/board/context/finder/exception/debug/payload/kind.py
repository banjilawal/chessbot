# src/chess/board/context/finder/exception/debug/payload/kind.py

"""
Module: chess.board.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import BoardException

_all__ = [
    # ======================# BOARD_DATASET_NULL EXCEPTION #======================#
    "BoardSearchNullDatasetException",
]


# ======================# BOARD_SEARCH_PAYLOAD_IS_NOT_LIST EXCEPTION #======================#
class BoardSearchPayloadTypeException(BoardException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the payload  of a successful BoardSearch payload is not List[Board].

    # PARENT:
        *   BoardException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "BoardSearch payload is the wrong type. The payload should be List[Board]."