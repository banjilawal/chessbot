# src/chess/board/context/finder/exception/debug/payload/kind.py

"""
Module: chess.board.context.finder.exception.debug.payload.kind
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import ResultException

_all__ = [
    # ======================# BOARD_DATASET_NULL EXCEPTION #======================#
    "BoardSearchNullDatasetException",
]


# ======================# SEARCH_PAYLOAD_IS_NOT_LIST_OF_BOARDS EXCEPTION #======================#
class BoardSearchPayloadTypeException(BoardException, ResultException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that after the BoardSearch ran successfully the payload was not a List[Board]. This exception makes
        sure search payloads follow the convention of returning an array of matches not a single item.

    # PARENT:
        *   BoardException
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "BoardSearch payload is the wrong type. The payload should be List[Board]."